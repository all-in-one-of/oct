#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Ppl_inspect
__author__ = zhangben 
__mtime__ = 2019/6/19 : 16:04
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.

"""
import maya.cmds as mc
import pymel.core as pm
import maya.OpenMaya as om
import copy,re,os,sys
from ..Major import Ppl_scInfo

class Ppl_check(object):
    """
    inspect maya file when asset or shot section checkin file to server
    """
    def __init__(self):
        """

        :return:
        """
        #  _iffy mesg  attributes =============
        self._iffyMsg_name = {}
        self._iffyMsg_abcObjs = {}
        self.scinfo = Ppl_scInfo.Ppl_scInfo()
        self.fbSetsNm = "PPL_CHECK_FEEDBACK"

    def assetNameCheck_grp(self):# outliner level name check
            # print info.__doc__
        self.clear_msgs('_iffyMsg_name')
        topGrpLoc = {'tx': 'CHR', 'rg': 'CHR', 'mo': 'MODEL'}
        regularGrpDict = {'tx': ['CHR', 'MODEL','FX'], 'rg': ['CHR', 'DEFORMER', 'FX', 'MODEL', 'MSH_all', 'MSH_geo', 'RIG'],'mo': ['MODEL', 'MSH_all', 'MSH_geo','MSH_outfit']}
        regularGrpDict2 = {'MODEL': ['MSH_all', 'MSH_geo', 'MSH_outfit'],'CHR':['DEFORMER', 'FX', 'MODEL', 'RIG']}

        sec = self.scinfo.section
        if not sec: self._iffyMsg_name['FileNameErro'] = u'请检查文件命名错误，无法判断文件属于哪个环节'

        topGrps = [item for item in pm.ls(assemblies=True) if item.nodeName() not in ['persp', 'top', 'front', 'side']]
        if len(topGrps) !=1: self._iffyMsg_name['Mutiple Groups'] = u'请检查outliner中最大组的数量'
        topGrp = None
        judgeTop = None
        secGrps = None
        for eaGrp in topGrps:
            if eaGrp in topGrpLoc.values(): topGrp = eaGrp
            childGrps = eaGrp.getChildren()
            if not len(childGrps):
                if 'Mutiple Groups' in self._iffyMsg_name: self._iffyMsg_name['Mutiple Groups'] += u'！注意 {} 为空组'.format(eaGrp.name())
                else: self._iffyMsg_name['Top Group Error'] = u'：{} 为空组'.format(eaGrp.name())
                continue
            else:
                secGrps_nm = [n.name() for n in childGrps]
                for eaTopGrp in regularGrpDict2:
                    if set(secGrps_nm) & set(regularGrpDict2[eaTopGrp]):
                        secGrps = childGrps
                        judgeTop = eaTopGrp
                        diffSet = set(secGrps_nm) ^ set(regularGrpDict2[eaTopGrp])
                        if len(diffSet - set(regularGrpDict2[eaTopGrp])):
                            self._iffyMsg_name['Secondary Groups Name Error'] = u'请检查outliner中第二层级组的命名 #1:'
                            for ea in list(diffSet):
                                self._iffyMsg_name['Secondary Groups Name Error'] += u':\t{}'.format(ea)
                    else:
                        continue
                        #self.iffyMsg['Secondary Groups Name Error'] = u'请检查outliner中第二层级组的命名 #2'
        if not secGrps:
            self._iffyMsg_name['Secondary Groups Name Error'] = u'请检查outliner中第二层级组的命名 #2'
        if not topGrp:
            self._iffyMsg_name['TopGroupNameError'] = u'请检查outliner中最大组的命名'
            #topGrp = judgeTop
        if judgeTop and topGrp:
            if judgeTop != topGrp: self.iffyMsg['TopGroupNameError'] = u'请检查outliner中最大组的命名'
        #all_trans = topGrp.listRelatives(type='transform', ad=True, c=True, ni=True)
        if self._iffyMsg_name:
            for item in self._iffyMsg_name:
                om.MGlobal.displayInfo(u">>>{:<30}: {}".format(item,self._iffyMsg_name[item]))

    def abcAttrCheck(self):#检测MODEL，Fx组下的模型 是否有alembic 属性 ,且 有alembic属性的模型，只能在MODEL组下 和 FX组下(fx组内为 毛发生长体)
        exec_cmd_dic = {'tx':"%S%.hasParent('CHR')",'rg':"%S%.hasParent('CHR')",'mo':"%S%.getParent()"}
        import OCT_Pipeline.scripts.ABC_Pipeline.ABC_CheckinInspect as chkIns
        inspc = chkIns.CheckinInspect()
        if not inspc.checkProjStates(): return
        msgAttr = '_iffyMsg_abcObjs'
        self.clear_msgs(msgAttr)
        lstGrpName = ['FX','MODEL']
        abcTrns = []
        availableTrns = []
        invalidTrns = []
        for m in lstGrpName:# 列出 fx  和 model 组下的 meshes
            modFxGrpLst = pm.ls(m)
            idx = lstGrpName.index(m)
            if len(modFxGrpLst) >1: self.update_msgs(msgAttr,"Multiple Group Error",u'有多个组命名为 ：{}'.format(m))
            if idx and not len(modFxGrpLst): self.update_msgs(msgAttr,'MODE Group Error',u'当前资产文件并没有MODEL组')
            if modFxGrpLst:
                mesh_trns = []
                for eaGrp in modFxGrpLst:
                    execCmd = re.sub('%S%', 'eaGrp', exec_cmd_dic[self.scinfo.section])
                    res = eval(execCmd)
                    if not res: self.update_msgs(msgAttr,'Hierarchical Relationship Error',u"组的层级结构存在异常 ： {}".format(eaGrp.name()))
                    ch_meshes = eaGrp.listRelatives(ad=True, c=True, ni=True, type='mesh')
                    if not len(ch_meshes):
                        self.update_msgs(msgAttr,'Empty Group Error',u"组为空组： {} ".format(eaGrp.name()))
                        continue
                    for msh in ch_meshes:
                        ea_tr = msh.getParent()
                        if idx: #如果是MODEL组 所有模型的transform 必须有alembic属性
                            if ea_tr.hasAttr('alembic'):
                                if ea_tr not in availableTrns: availableTrns.append(ea_tr)
                                else:self.update_msgs(msgAttr,"Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...： {}'.format(ea_tr.name()))
                            else:
                                if ea_tr not in invalidTrns:
                                    invalidTrns.append(ea_tr)
                                    self.update_msgs(msgAttr,"Mesh Alembic Attr Error",u'MODEL 组下的的物体没有添加alembic属性：{} --- {}'.format(eaGrp.name(),ea_tr.name()))
                                else: self.update_msgs(msgAttr,"Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...： {}'.format(ea_tr.name()))
                        else:
                            if ea_tr.hasAttr('alembic'):
                                if ea_tr not in availableTrns:availableTrns.append(ea_tr)
                                else: self.update_msgs(msgAttr,"Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...： {}'.format(ea_tr.name()))
        for ea_mesh in pm.ls(type='mesh',ni=True):
            ea_tr2 = ea_mesh.getParent()
            if ea_tr2.hasAttr('alembic'):
                if ea_tr2 not in abcTrns: abcTrns.append(ea_tr2)
                else: self.update_msgs(msgAttr,"Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...： {}'.format(ea_tr.name()))

        if set(abcTrns) - set(availableTrns):
            for t in (set(abcTrns) - set(availableTrns)):
                self.update_msgs(msgAttr,"Alembic Mesh affiliation Error",u"有alembic 属性的节点没有在指定的组里，请检查：{}".format(t.name()))

        if self._iffyMsg_abcObjs:
            om.MGlobal.displayInfo(u">>>{0} 对节点的 alembic 属性检测，异常数据 记录如下{0}".format("="*15))
            for item in self._iffyMsg_abcObjs:
                om.MGlobal.displayInfo(u">>>{:<30}:{}".format(item, os.linesep))
                for item2 in self._iffyMsg_abcObjs[item]:
                    om.MGlobal.displayInfo(u"\t{}".format(item2))
            om.MGlobal.displayInfo(u">>>{0} 以上是对节点的 alembic 属性检测，异常数据的记录{0}".format("="*15))
    def clear_msgs(self,msgAttrNm="_iffyMsg_"):# 重置记录错误的字典或数组
        for ea in self.__dict__:
            # print ea
            # print self.__getattribute__(ea)
            if re.search(msgAttrNm,ea,re.I):
                if isinstance(self.__getattribute__(ea),dict): self.__getattribute__(ea).clear()
                elif isinstance(ea,list): ea=[]

    def update_msgs(self,msgAttrNm,errMsgLabel,errMsg=""):# 刷新 错误信息
        for ea in self.__dict__:
            if re.search(msgAttrNm, ea, re.I):
                if isinstance(self.__getattribute__(ea), dict):
                    value = self.__getattribute__(ea)
                    if errMsgLabel in value:
                        tmp = copy.deepcopy(value)
                        tmp[errMsgLabel].append(errMsg)
                        self.__setattr__(ea, tmp)
                    else:
                        tmp = copy.deepcopy(value)
                        tmp[errMsgLabel] = [errMsg]
                        self.__setattr__(ea, tmp)
                elif isinstance(self.__getattribute__(ea), dict):
                    value = self.__getattribute__(ea)
                    if errMsgLabel not in value:
                        tmp = copy.deepcopy(value)
                        tmp.append(errMsgLabel)
                        self.__setattr__(ea, tmp)