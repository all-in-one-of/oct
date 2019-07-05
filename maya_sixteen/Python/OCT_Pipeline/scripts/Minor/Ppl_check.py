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
reload(Ppl_scInfo)
from types import FunctionType
from PyQt4 import QtGui,QtCore
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
        self._iffyMsg_dags = {}
        self.scinfo = Ppl_scInfo.Ppl_scInfo()
        self.fbSetsNm = "PPL_CHECK_FEEDBACK"
        self.iffyVtxs = {}
        self.abcMeshes = []
        self.iffySets = None
    def autoRun(self,chk_fnc_name='all'):# 运行检查 全部运行 或 运行指定的检测
        u"""
        >>Check all 检查所有
        """
        print(">>>{0:=>25}PIPELINE CHECK{0:=<25}".format("\t"))
        resetSets = False
        if re.search("^(all)|(_check_)",chk_fnc_name):
            resetSets = True
            self.clear_msgs()
        allAttributes = self.__class__.__dict__.items()

        if chk_fnc_name == 'all':  # 执行所有 _check_ 开头的 check  方法
            chkAll_prc, chkIndiv_prc = self.pars_needRunFuncs()
            for n in chkAll_prc:
                # exec("print self.__class__.{}.__doc__".format(n))
                exec("self.{}()".format(n))
            checkNodesLst = self.abcMeshes
            for m in chkIndiv_prc:
                # exec ("print self.__class__.{}.__doc__".format(m))
                exec("self.{}({})".format(m,checkNodesLst))
        else: #运行 指定的 方法
            if re.search(",",chk_fnc_name):
                inSpl = chk_fnc_name.split(',')
                fncnm = inSpl[0]
                argvs = ','.join(inSpl[1:])
                exec ("self.{}({})".format(fncnm,argvs))
            else:
                chk_fnc = [x for x, y in allAttributes if re.search(chk_fnc_name, x) and type(y) == FunctionType]
                exec ("self.{}()".format(chk_fnc[0]))
        if not resetSets: return
        self.creat_iffy_setsGrp()
        msgs = [n for n in self.__dict__ if re.search("^_iffyMsg_", n)]
        for msgAttr_nm in msgs:
            msgAttr_value = self.__getattribute__(msgAttr_nm)
            if msgAttr_value:
                om.MGlobal.displayInfo(self.fbSetsNm)
                for eaIffy in msgAttr_value:
                    om.MGlobal.displayInfo(eaIffy)
                    if isinstance(msgAttr_value[eaIffy], str) or isinstance(msgAttr_value[eaIffy], unicode):
                        om.MGlobal.displayInfo(u'\t{}'.format(msgAttr_value[eaIffy]))
                        continue
                    for item in msgAttr_value[eaIffy]:
                        om.MGlobal.displayInfo(u"\t{}".format(item))
                        if isinstance(msgAttr_value[eaIffy], dict):
                            for item2 in msgAttr_value[eaIffy].values():
                                om.MGlobal.displayInfo(u"\t\t {}".format(item2))
                    #     if isinstance(self._iffyMsg_name[eaIffy],list):
                    #         for item2 in self._iffyMsg_name[eaIffy]:
                    #             om.MGlobal.displayInfo(u"\t\t {}".format(item2))
                    #     elif isinstance(self._iffyMsg_name[eaIffy],dict):
                    #         for item2 in self._iffyMsg_name[eaIffy].values():
                    #             om.MGlobal.displayInfo(u"\t\t {}".format(item2))

    def pars_needRunFuncs(self):# 如果在面板上执行all check.. 则对checkbox 进行判断
        allFncs = self.__class__.__dict__.items()
        aswin = QtGui.QApplication.activeWindow()
        cbxs = dict([[str(eacbx.objectName()), eacbx] for eacbx in aswin.findChildren(QtGui.QCheckBox) if re.search("_cbx$", eacbx.objectName())])
        chkAll_prc = []
        chkIndiv_prc = []
        for x, y in allFncs:
            if re.search('_check_all_\d', x) and type(y) == FunctionType and cbxs["{}_regchk_chk".format(x)].checkState()==2:
                chkAll_prc.append(x)
            elif re.search('_check_indiv_', x) and type(y) == FunctionType and cbxs["{}_regchk_chk".format(x)].checkState()==2:
                chkIndiv_prc.append(x)
        chkAll_prc.sort()

        return chkAll_prc,chkIndiv_prc
    def get_chk_nodes(self,obtainData,objtyp='mesh',getPar=True,topNode = None):# 返回操作对象
        check_objs = pm.selected()
        if not check_objs:
            check_objs = obtainData if obtainData.__class__.__name__ == 'list' else [obtainData]
        # if not check_objs:
        #     check_objs = self.checkNodesLst
        if not check_objs:
            if topNode:
                check_objs = [n.getParent() for n in topNode.listRelatives(ad=True,c=True,type= nodeTyp,ni=True)] if getPar else [n for n in topNode.listRelatives(ad=True,c=True,type= nodeTyp,ni=True)]
            else:
                check_objs = [n.getParent() for n in pm.ls(type=objtyp, ni=True)] if getPar else [n for n in pm.ls(type=objtyp, ni=True)]
        return check_objs
    def _check_all_1_grpName(self):# outliner level name check
            # om.MGlobal.displayInfo info.__doc__
        u"""
        >>Pipeline Check: check the Name regularity of Outliner's objects and groups
                          检查outliner 组，层级，以及物体命名的规范性
                          CHR | MODEL/RIG/DEFORMER/FX|MSH_geo/MSH_outfit
        """
        self.clear_msgs('_iffyMsg_name')
        topGrpLoc = {'tx': 'CHR', 'rg': 'CHR', 'mo': 'MODEL'}
        regularGrpDict = {'tx': ['CHR', 'MODEL','FX'], 'rg': ['CHR', 'DEFORMER', 'FX', 'MODEL', 'MSH_all', 'MSH_geo', 'RIG'],'mo': ['MODEL', 'MSH_all', 'MSH_geo','MSH_outfit']}
        regularGrpDict2 = {'MODEL': ['MSH_all', 'MSH_geo', 'MSH_outfit'],'CHR':['DEFORMER', 'FX', 'MODEL', 'RIG']}

        sec = self.scinfo.section
        if not sec: self._iffyMsg_name['FileNameErro'] = u'请检查文件命名错误，无法判断文件属于哪个环节'

        topGrps = [item for item in pm.ls(assemblies=True) if item.nodeName() not in ['persp', 'top', 'front', 'side']]
        if len(topGrps) !=1: self._iffyMsg_name['>>IFFY--Mutiple Groups'] = u'请检查outliner中最大组的数量 :::{}'.format(u":::".join([grp.name() for grp in topGrps]))
        topGrp = None
        judgeTop = None
        secGrps = None
        for eaGrp in topGrps:
            if eaGrp in topGrpLoc.values(): topGrp = eaGrp
            childGrps = eaGrp.getChildren()
            if not len(childGrps):
                # if 'Mutiple Groups' in self._iffyMsg_name: self._iffyMsg_name['>>IFFY--Empty Groups'] = [u'空组 :{}'.format(eaGrp.name())]
                # else: self._iffyMsg_name['>>IFFY--Top Group Error'] = u'空组:'.format(eaGrp.name())
                self._iffyMsg_name['>>IFFY--Empty Groups'] = u'outliner 有空组 :::{}'.format(eaGrp.name())
                continue
            else:
                secGrps_nm = [n.name() for n in childGrps]
                for eaTopGrp in regularGrpDict2:
                    if set(secGrps_nm) & set(regularGrpDict2[eaTopGrp]):
                        secGrps = childGrps
                        judgeTop = eaTopGrp
                        diffSet = set(secGrps_nm) ^ set(regularGrpDict2[eaTopGrp])
                        if len(diffSet - set(regularGrpDict2[eaTopGrp])):# or len(set(regularGrpDict2[eaTopGrp]) - diffSet) :
                            self._iffyMsg_name['>>IFFY--Secondary Groups Name Error'] = u'请检查outliner中第二层级组的命名 #1:'
                            for ea in list(diffSet):
                                self._iffyMsg_name['>>IFFY--Secondary Groups Name Error'] += u':\t{}'.format(ea)
                    else:
                        continue
                        #self.iffyMsg['Secondary Groups Name Error'] = u'请检查outliner中第二层级组的命名 #2'
        if not secGrps:
            self._iffyMsg_name['>>IFFY--Secondary Groups Name Error'] = u'请检查outliner中第二层级组的命名 #2'
        if not topGrp:
            self._iffyMsg_name['>>IFFY--TopGroupNameError'] = u'请检查outliner中最大组的命名'
            #topGrp = judgeTop
        if judgeTop and topGrp:
            if judgeTop != topGrp: self.iffyMsg['>>IFFY--TopGroupNameError'] = u'请检查outliner中最大组的命名'
        #all_trans = topGrp.listRelatives(type='transform', ad=True, c=True, ni=True)
        # if self._iffyMsg_name:
        #     for item in self._iffyMsg_name:
        #         om.MGlobal.displayInfo(u">>>{:<30}: {}".format(item,self._iffyMsg_name[item]))

    def _check_all_2_abcAttr(self):#检测MODEL，Fx组下的模型 是否有alembic 属性 ,且 有alembic属性的模型，只能在MODEL组下 和 FX组下(fx组内为 毛发生长体)
        u"""
        >>Start Pipeline Check: check the objects have alembic attribute
                                检查 所有alembic属性的物体 是否在 MODEL或FX 组下
                                并且MODEL组的物体都要有alembic属性，它们最终将参与渲染
        """
        exec_cmd_dic = {'tx':"%S%.hasParent('CHR')",'rg':"%S%.hasParent('CHR')",'mo':"%S%.getParent()"}
        import OCT_Pipeline.scripts.ABC_Pipeline.ABC_DBInspect as chkIns
        inspc = chkIns.ABC_DBInspect()
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
            if len(modFxGrpLst) >1: self.update_msgs(msgAttr,">>IFFY--Multiple Group Error",u'有多个组命名为 :::{}'.format(m))
            if idx and not len(modFxGrpLst): self.update_msgs(msgAttr,'>>IFFY--MODE Group Error',u'当前资产文件并没有MODEL组')
            if modFxGrpLst:
                mesh_trns = []
                for eaGrp in modFxGrpLst:
                    execCmd = re.sub('%S%', 'eaGrp', exec_cmd_dic[self.scinfo.section])
                    res = eval(execCmd)
                    if not res: self.update_msgs(msgAttr,'>>IFFY--Hierarchical Relationship Error',u"组的层级结构存在异常 :::{}".format(eaGrp.name()))
                    ch_meshes = eaGrp.listRelatives(ad=True, c=True, ni=True, type='mesh')
                    if not len(ch_meshes) :
                        if idx:
                            self.update_msgs(msgAttr,'>>IFFY--Empty Group Error',u"组为空组:::{} ".format(eaGrp.name()))
                        continue
                    for msh in ch_meshes:
                        ea_tr = msh.getParent()
                        if idx: #如果是MODEL组 所有模型的transform 必须有alembic属性
                            if ea_tr.hasAttr('alembic'):
                                if ea_tr not in availableTrns: availableTrns.append(ea_tr)
                                else:self.update_msgs(msgAttr,">>IFFY--Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...:::{}'.format(ea_tr.name()))
                            else:
                                if ea_tr not in invalidTrns:
                                    invalidTrns.append(ea_tr)
                                    self.update_msgs(msgAttr,">>IFFY--Mesh Alembic Attr Error",u'MODEL 组下的的物体没有添加alembic属性：{} --- :::{}'.format(eaGrp.name(),ea_tr.name()))
                                else: self.update_msgs(msgAttr,">>IFFY--Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...:::{}'.format(ea_tr.name()))
                        else:
                            if ea_tr.hasAttr('alembic'):
                                if ea_tr not in availableTrns:availableTrns.append(ea_tr)
                                else: self.update_msgs(msgAttr,">>IFFY--Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...:::{}'.format(ea_tr.name()))
        for ea_mesh in pm.ls(type='mesh',ni=True):
            ea_tr2 = ea_mesh.getParent()
            if ea_tr2.hasAttr('alembic'):
                if ea_tr2 not in abcTrns:
                    abcTrns.append(ea_tr2)
                else: self.update_msgs(msgAttr,">>IFFY--Trans Node Clash Error",u'transform节点 有两个以上非 intermediate mesh shape...:::{}'.format(ea_tr.name()))

        if set(abcTrns) - set(availableTrns):
            for t in (set(abcTrns) - set(availableTrns)):
                self.update_msgs(msgAttr,">>IFFY--Alembic Mesh affiliation Error",u"有alembic 属性的节点没有在指定的组里，请检查 :::{}".format(t.name()))

        if self._iffyMsg_abcObjs:
            om.MGlobal.displayInfo(u">>>{0} 对节点的 alembic 属性检测，异常数据 记录如下{0}".format("="*15))
            for item in self._iffyMsg_abcObjs:
                om.MGlobal.displayInfo(u">>>{:<30}:{}".format(item, os.linesep))
                # for item2 in self._iffyMsg_abcObjs[item]:
                om.MGlobal.displayInfo(u"\t{}".format( self._iffyMsg_abcObjs[item]))
            om.MGlobal.displayInfo(u">>>{0} 以上是对节点的 alembic 属性检测，异常数据的记录{0}".format("="*15))
            # mc.error("Check Alembic Attribute get some Errror!!!")
        else:
            self.abcMeshes = abcTrns
            return True
    def clear_msgs(self,msgAttrNm="_iffyMsg_"):# 重置记录错误的字典或数组
        for ea in self.__dict__:
            # om.MGlobal.displayInfo ea
            # om.MGlobal.displayInfo self.__getattribute__(ea)
            if re.search(msgAttrNm,ea,re.I):
                if isinstance(self.__getattribute__(ea),dict):
                    self.__getattribute__(ea).clear()
                elif isinstance(self.__getattribute__(ea),list):
                    self.__setattr__(ea,[])
    def update_msgs(self,msgAttrNm,errMsgLabel,errMsg=""):# 刷新 错误信息
        for ea in self.__dict__:
            if re.search(msgAttrNm, ea, re.I):
                if isinstance(self.__getattribute__(ea), dict):
                    value = self.__getattribute__(ea)
                    if errMsgLabel in value:
                        tmp = copy.deepcopy(value)
                        if isinstance(tmp[errMsgLabel],list):
                            if errMsg not in tmp[errMsgLabel]:
                                tmp[errMsgLabel].append(errMsg)
                                self.__setattr__(ea, tmp)
                        elif isinstance(tmp[errMsgLabel],str):
                            if errMsg != tmp[errMsgLabel]:
                                tmp[errMsgLabel] += errMsg
                                self.__setattr__(ea, tmp)
                        elif isinstance(tmp[errMsgLabel],dict):
                            tmp[errMsgLabel].update(errMsg)
                            self.__setattr__(ea, tmp)
                    else:
                        tmp = copy.deepcopy(value)
                        tmp[errMsgLabel] = errMsg
                        self.__setattr__(ea, tmp)
                elif isinstance(self.__getattribute__(ea), list):
                    value = self.__getattribute__(ea)
                    if errMsgLabel not in value:
                        tmp = copy.deepcopy(value)
                        tmp.append(errMsgLabel)
                        self.__setattr__(ea, tmp)


    def _check_indiv_unfreezeTrns(self,checkNode = None,nrbs=False,clear=False):
        u"""
        >>Start Pipeline Check: check the transform node unfreeze
                                检查transform节点 freeze
        注意：如果当前有选择物体，将仅作用于选择的物体
        """
        chk_trns = self.get_chk_nodes(checkNode)
        msgAttr = '_iffyMsg_dags'
        if clear: self.clear_msgs(msgAttr)
        for trn in chk_trns:
            chk_attr = {'tx':0,'ty':0,'tz':0,'rx':0,'ry':0,'rz':0,'sx':1,'sy':1,'sz':1}
            for a in chk_attr:
                if not trn.attr(a).isLocked():self.update_msgs(msgAttr,">>IFFY--Transform Node Unlock attrs",u'transform节点属性默认值未锁定  :::{}.{}'.format(trn.name(),a))
                # self._iffyMsg_name[] =
                if not trn.attr(a).get() == chk_attr[a]:self.update_msgs(msgAttr,">>IFFY--Transform Node Unfreeze",u'transform节点属性默认值存在异常:::{}.{}'.format(trn.name(),a))
        if nrbs:
            chk_trns.extend([n.getParent() for n in pm.ls(type='nurbsCurve', ni=True) if n.hasParent('RIG')])
            chk_attr = {'tx': 0, 'ty': 0, 'tz': 0, 'rx': 0, 'ry': 0, 'rz': 0, 'sx': 1, 'sy': 1, 'sz': 1}
            for a in chk_attr:
                if not trn.attr(a).isLocked(): self.update_msgs(msgAttr,">>IFFY--Transform Node Unlock attrs",u'transform节点属性默认值未锁定  :::{}.{}'.format(trn.name(), a))
                if not trn.attr(a).get() == chk_attr[a]: self.update_msgs(msgAttr, ">>IFFY--Transform Node Unfreeze", u'transform节点属性默认值存在异常:::{}.{}'.format(trn.name(), a))

    def _check_indiv_UVSets(self,chkNode=None):
        u"""
        >>Start Pipeline Check: check the mesh objects that has multiple uvsets
                                检查物体是否有多个uvset
        注意：如果当前有选择物体，将仅作用于选择的物体
        """
        msgAttr = '_iffyMsg_dags'
        chk_trns = self.get_chk_nodes(chkNode)
        kMoreThanOneUVSet = []
        for i in chk_trns:
            i_shp = i.getShape(ni=True)
            kUVSets = pm.polyUVSet(i, query=True, allUVSets=1)
            if len(kUVSets) > 1:
                kMoreThanOneUVSet.append(i)
        if kMoreThanOneUVSet:
            self.update_msgs(msgAttr,">>IFFY--Multiple UVsets Objects",kMoreThanOneUVSet)
        else:
            om.MGlobal.displayInfo(u">>>mesh的没有2个以上的uvset ")
        return kMoreThanOneUVSet

    # check 没有归零的点 运行较慢
    def _check_indiv_vertexPos(self,chkNode=None):
        u"""
        >>Start Pipeline Check: check the object's vertex position
                                检查mesh 的 cv 点是否归0
        注意：如果当前有选择物体，将仅作用于选择的物体
        """
        msgAttr = '_iffyMsg_dags'
        chk_trns = self.get_chk_nodes(chkNode)
        for trnsNode in chk_trns:
            vtx = pm.polyEvaluate(trnsNode, v=True)
            for n in range(vtx):
                vtx_nm = "{}.vtx[{}]".format(trnsNode.name(), n)
                pnt_nm = "{}.pnts[{}]".format(trnsNode.name(), n)
                pntx_nm = "{}.pntx".format(pnt_nm)
                pnty_nm = "{}.pnty".format(pnt_nm)
                pntz_nm = "{}.pntz".format(pnt_nm)
                pntx_v = pm.getAttr(pntx_nm)
                pnty_v = pm.getAttr(pnty_nm)
                pntz_v = pm.getAttr(pntz_nm)
                if pntx_v or pnty_v or pntz_v:
                    self.iffyVtxs[vtx_nm] = [pntx_v, pnty_v, pntz_v]
        if self.iffyVtxs:
            self.update_msgs(msgAttr,">>IFFY--Vertex Position not 0",self.iffyVtxs)
            return self.iffyVtxs
        else:
            om.MGlobal.displayInfo(u">>>mesh的vtx的位移值已经为0 ")
    def _reg_indiv_resVtxPos(self,userInput=None, prMode='freeze'):#重置cv点的位置信息 两种模式  freeze  是不改变位置，让cv 的位移值归零 ；reset ，让cv点回到值为0 的位置
        u"""
        >> 重置 mesh cv 点 两种模式 ：
                                    1) 位置复位   将不在0 0 0 的cv点，移回 0 0 0
                                    2) 位移值归0  不移动CV点，只是将点的位移值 归 0
           userInput: 可以是某个点，可以是列表，可以是单个节点，可以是pm.pynode  可以是 节点的名字

           注意：如果当前有选择物体，将仅作用于选择的物体
        """
        # msgAttr = '_iffyMsg_dags'
        chkNodes = pm.selected()
        if not chkNodes and userInput:
            chkNodes = userInput if userInput.__class__.__name__ == 'list' else [userInput]
        if not chkNodes:return
        doneNode = []
        for each in chkNodes:
            eachNode = pm.PyNode(each).node() if each.__class__.__name__ == 'str' else each.node()
            if eachNode in doneNode: continue
            if prMode == 'freeze':
                pm.polyMoveVertex(eachNode.verts, lt=(0.0, 0.0, 0.0), ch=False)
                doneNode.append(eachNode)
            else:
                ea2pm,tr_node = None,None
                if each.__class__.__name__ in ['str', 'unicode']:
                    ea2pm = pm.PyNode(each)
                else: ea2pm = each
                if ea2pm in doneNode: continue
                if ea2pm.__class__.__name__ == 'MeshVertex':
                    self.dealWithVtxPos(ea2pm, 'setAttr', [0, 0, 0])
                    # doneNode.append(ea2pm)
                    continue
                elif ea2pm.__class__.__name__ == 'Mesh':  # 如果输入的是 transform节点
                    tr_node = ea2pm.getParent()
                elif ea2pm.__class__.__name__ == 'Transform':
                    tr_node = ea2pm
                doneNode.append(ea2pm)
                vtx = pm.polyEvaluate(tr_node, v=True)
                for n in range(vtx):
                    vtx_nm = "{}.vtx[{}]".format(tr_node.name(), n)
                    pm_vtx = pm.PyNode(vtx_nm)
                    self.dealWithVtxPos(pm_vtx, 'setAttr', [0, 0, 0])
                pm.delete(each,ch=True)
    def dealWithVtxPos(self,pm_vtx, opr='getAttr', v=[0, 0, 0]):#获得或设置cv点的位置值
        retDic = {}
        v_indx = pm_vtx.index()
        pnt_nm = "{}.pnts[{}]".format(pm_vtx.node().name(), v_indx)
        pntx_nm = "{}.pntx".format(pnt_nm)
        pnty_nm = "{}.pnty".format(pnt_nm)
        pntz_nm = "{}.pntz".format(pnt_nm)
        retDic[pm_vtx.name()] = []
        if opr == 'getAttr':
            retDic[pm_vtx.name()].append(pm.getAttr("{}.pntx".format(pnt_nm)))
            retDic[pm_vtx.name()].append(pm.getAttr("{}.pnty".format(pnt_nm)))
            retDic[pm_vtx.name()].append(pm.getAttr("{}.pntz".format(pnt_nm)))
            return retDic
        elif opr == 'setAttr':
            pm.setAttr("{}.pntx".format(pnt_nm), v[0])
            retDic[pm_vtx.name()].append(pm.getAttr("{}.pntx".format(pnt_nm)))
            pm.setAttr("{}.pnty".format(pnt_nm), v[1])
            retDic[pm_vtx.name()].append(pm.getAttr("{}.pnty".format(pnt_nm)))
            pm.setAttr("{}.pntz".format(pnt_nm), v[2])
            retDic[pm_vtx.name()].append(pm.getAttr("{}.pntz".format(pnt_nm)))
            om.MGlobal.displayInfo(">>>The Vertex position set to [0,0,0] : {}".format(pm_vtx.name()))
            return retDic

    def creat_iffy_setsGrp(self):
        nameDict = {'_iffyMsg_abcObjs':'Check_iffy_alembic_Objects','_iffyMsg_dags':'Check_iffy_DagNodes','_iffyMsg_name':'Check_iffy_object_name'}
        if pm.objExists("Pipeline_Check_iffy_sets"):
            self._reg_clearCheckSets()
        msgs = [n for n in self.__dict__ if re.search("^_iffyMsg_",n) and self.__getattribute__(n)]
        if msgs: self.iffySets = pm.sets(n="Pipeline_Check_iffy_sets",empty=True)
        for msgAttr_nm in msgs:
            msgAttr = self.__getattribute__(msgAttr_nm)
            if not msgAttr:continue
            vtxSet = False
            catgrySets = pm.sets(n = nameDict[msgAttr_nm])
            for ea_iffy in msgAttr:
                if re.search('vertext',ea_iffy,re.I): vtxSet=True
                setsnm = re.sub(" ", "_", re.sub(">>IFFY--", "CHECK_IFFY_", ea_iffy))
                members = []
                if msgAttr[ea_iffy].__class__.__name__ == 'unicode':
                    msg = msgAttr[ea_iffy]
                    if re.search(":::[\w.:|]+", msg):
                        strSpl = re.search(":::[\w.:|]+", msg).group().split(':::')
                        for e in strSpl:
                            if not e: continue
                            pmObj = pm.PyNode(e)
                            dagNode = pmObj.node()
                            if dagNode not in members: members.append(dagNode)
                elif msgAttr[ea_iffy].__class__.__name__ == 'list':
                    for msg in msgAttr[ea_iffy]:
                        if re.search(":::[\w.:|]+", msg):
                            strSpl = re.search(":::[\w.:|]+", msg).group().split(':::')
                            for e in strSpl:
                                if not e: continue
                                pmObj = pm.PyNode(e)
                                dagNode = pmObj.node()
                                if dagNode not in members: members.append(dagNode)
                elif msgAttr[ea_iffy].__class__.__name__ == 'dict':
                    for msg in msgAttr[ea_iffy]:
                        if re.search(":::[\w.:|]+", msg):
                            strSpl = re.search(":::[\w.:|]+", msg).group().split(':::')
                            for e in strSpl:
                                if not e: continue
                                pmObj = pm.PyNode(e)
                                dagNode = pmObj.node()
                                if dagNode not in members: members.append(dagNode)
                        else:
                            if pm.objExists(msg):
                                pmObj = pm.PyNode(msg)
                                if pmObj.__class__.__name__ == "MeshVertex":                 #如果是点就添加点进sets组
                                    if pmObj not in members:members.append(pmObj)
                                else:
                                    dagNode = pmObj.node()
                                    if dagNode not in members: members.append(dagNode)

                if members:
                    pm.select(members)
                    subSets = pm.sets(n=setsnm,v=vtxSet)
                    catgrySets.add(subSets)
            self.iffySets.add(catgrySets)
    def _reg_clearCheckSets(self,kw = 'check_iffy_'):
        all_iffySets = [n for n in pm.ls(type='objectSet') if re.search(kw, n.name(), re.I)]
        for ea_sets in all_iffySets:
            ea_sets.clear()
        pm.delete(all_iffySets)