#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ABC_tmp
__author__ = zhangben 
__mtime__ = 2019/3/19 : 20:50
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import pymel.core as pm
import json
import re
import maya.cmds as mc
import os
import maya.mel as mel
import PyQt4.QtGui as qg
import PyQt4.QtCore as qc
import maya.OpenMayaUI as mui
import sip

from OCT_Pipeline.uis import abcSingleWin_ui
reload(abcSingleWin_ui)
from OCT_Pipeline.uis import abcSingleWidget_ui
reload(abcSingleWidget_ui)

if not mc.pluginInfo("AbcImport", q=True, loaded=True):
    mc.loadPlugin('AbcImport', quiet=True)



def getMayaWindow():
    """
    get the maya main window as a QMainWndow instance
    :return:
    """
    ptr = mui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr),qc.QObject)



class ABC_SingleWin(qg.QMainWindow,abcSingleWin_ui.Ui_abcS_win):
    def __init__(self,parent = getMayaWindow()):
        super(ABC_SingleWin,self).__init__(parent)
        self.setupUi(self)

        self.ccWidget = AbcSglWidget()
        self.setCentralWidget(self.ccWidget)
        self.ccWidget.move(0,0)


class AbcSglWidget(qg.QWidget):
    def __init__(self,*args,**kwargs):
        super(AbcSglWidget,self).__init__(*args,**kwargs)

        self.readDate = {}
        self.all_msg = None

        self.ui = abcSingleWidget_ui.Ui_abcS_form()
        self.ui.setupUi(self)

        self.ui.st_line.setValidator(qg.QIntValidator())
        self.ui.end_line.setValidator(qg.QIntValidator())

        cr_min = pm.playbackOptions(min=True,q=True)
        cr_max = pm.playbackOptions(max=True,q=True)
        self.ui.st_line.setText(str(cr_min))
        self.ui.end_line.setText(str(cr_max))

        self.ui.cc_pth_bt.clicked.connect(self.out_bt_choosDir)
        self.ui.rc_bt.clicked.connect(lambda: self.wr2f(0))
        self.ui.ex_cc_bt.clicked.connect(lambda:self.wr2f(1))
        self.ui.sel_cc_bt.clicked.connect(self.r4f)
        self.ui.im_cc_bt.clicked.connect(self.im_cc_bt_cmd)
    def out_bt_choosDir(self):
        # dir_choose = qg.QFileDialog.getExistingDirectory(self,'select out put diretory', pm.workspace.getName())
        dir_choose = qg.QFileDialog.getExistingDirectory(self,qc.QString(u'选择输出路径'), pm.workspace.getName())
        #dir_choose = mc.fileDialog2(dir=pm.workspace.getName(),dialogStype=2,fileMode=4)
        if dir_choose == "":
            print("\n cancle select")
            return
        self.ui.pth_line.setText(dir_choose)

    def im_cc_bt_choosFiles(self):
        dir_choose = qg.QFileDialog.getExistingDirectory(self, u'选择cache输出路径', self.cwd)

        if dir_choose == "":
            print("\n cancle select")
            return
        self.ui.pth_line.setText(dir_choose)

    def wr2f(self,doCache=True):## ===== 动画师 输出 缓存 和 记录 选择模型信息文件 执行下
        selObj = pm.ls(sl=True)
        new_add = {}
        # if selObj:
        nmsp = selObj[0].namespace().strip(':')
        for ea in selObj:
            needName = ea.stripNamespace().strip()
            new_add[needName] = None
        wsp = pm.workspace.name
        with open(r"{}/{}_caOBjList.json".format(wsp,nmsp), 'w') as f:
            f.write(json.dumps(new_add, indent=4))
        if not doCache:
            print("A file which records the information of  selected objects has been created!")
        if doCache:
            st_frm = self.ui.st_line.text()
            end_frm = self.ui.end_line.text()
            #sel_objs_nm_lst = [eaSel.longName() for eaSel in selObj]
            opt_dir = self.ui.cc_pth_bt.text()
            self.opt_cc(selObj,st_frm,end_frm,opt_dir)
            # self.ui.lineEdit.setText(cmdstr)
            # print cmdstr
            # mc.AlembicExportSelectionOptions()
    def opt_cc(self,objs_nm_lst,stfrm,endfrm,ccdir):
        #cmd = " -root {}".format(objs_nm_lst)
        cmdStr = " -root ".join([a.longName() for a in objs_nm_lst])
        exp_cc_cmd = 'AbcExport -j "-frameRange {} {} -root {} -uvWrite -worldSpace -writeVisibility   "'.format(stfrm, endfrm,cmdStr)
        mel.eval(exp_cc_cmd)
        # return exp_cc_cmd
    def r4f(self):#=== 选择缓存和记录模型的文件
        wsp = pm.workspace.name
        sel_fs = qg.QFileDialog.getOpenFileNames(self, qc.QString(u'请选择记录模型信息的json文件 和 缓存文件'), wsp)
        sel_fs_strlst = [unicode(ea.toUtf8(), 'utf-8', 'ignor') for ea in sel_fs]
        # res = '\n'.join([os.path.split(ea_file)[1] for ea_file in sel_fs_strlst])
        res = '\n'.join([ea_file for ea_file in sel_fs_strlst])
        self.ui.im_lst_tx.setText(res)
        # return res
        #singleFilter = "All Files (*.*)"
        #res = mc.fileDialog2(fileFilter=singleFilter, dialogStyle=2,fileMode=4)
        self.readDate = {}
        for af in sel_fs_strlst:
            print af
            ext = os.path.splitext(af)[-1]
            if ext == ".abc": self.readDate['abc'] = af
            elif ext == '.json': self.readDate['js'] = af
        with open(self.readDate['js'], 'r') as f:
            self.readDate['cclst']= json.load(f).keys()
        return self.readDate

    def list_rdcc_meshs(self,infor):# 根据记录的信息返回当前读取缓存的模型列表
        #infor = r4f()
        cc_meshes = infor['cclst']
        readCcMsh = {}
        sel_chr = pm.selected()[0]
        for eaMesh in sel_chr.getChildren(type='mesh',ad=True,ni=True):
            ea_nm = eaMesh.name(stripNamespace=True)
            ea_p = eaMesh.getParent()
            if ea_p.name(stripNamespace=True) in cc_meshes and eaMesh not in readCcMsh: readCcMsh[eaMesh] = ea_p
        pm.select(readCcMsh.values(),r=True)
        return readCcMsh
    #导入缓存合并模式如果有缓存物体非rigging 模式运动，读取缓存的物体的又锁定了transform定会有问题，所以如果不merge 就返回alembic node 的链接信息
    def get_im_mode(self):
        # cur_rb = self.ui.holdBx.checkedButton().text()
        #all_rb = [self.ui.ref_rb,self.ui.im_rb]
        #s = self.bx_im_rb.text()
        sel_mod = self.ui.mod_grp.checkedButton().text()
        if sel_mod == 'Reference': return 'ref'
        elif sel_mod == 'Import':  return 'imp'
        selRb = unicode(s, 'utf-8', 'ignor')
    def im_cache(self,merge=None):
        #infor = r4f()
        infor = self.readDate
        sel_chr = pm.selected()[0]
        sel_nms = sel_chr.namespace().strip(':')
        abc_f = infor['abc']
        con_cc_meshes = self.list_rdcc_meshs(infor)
        con_objs = [m.longName() for m in con_cc_meshes.values()]
        con_str = " ".join(con_objs)
        if merge:
            mc.AbcImport(abc_f, mode='import', connect=con_str)
            return None
        else:
            exist_abc = pm.ls(type='AlembicNode')
            imp_obj = mc.AbcImport(abc_f, mode='import')
            imp_abc = [eaAbc for eaAbc in pm.ls(type='AlembicNode') if eaAbc not in exist_abc]
            listCon = imp_abc[0].listConnections(p=True,c=True)
            pm.playbackOptions(e=True, min=imp_abc[0].attr('startFrame').get(), max=imp_abc[0].attr('endFrame').get())
            self.all_msg = {'conmsg':{imp_abc[0].name():listCon},'objs':{sel_nms:con_cc_meshes}}
            return self.all_msg

    def im_cc_bt_cmd(self):
        mode = self.get_im_mode()
        if mode == 'ref':self.im_cache(merge=True)
        elif mode =='imp':
            cc_date = self.im_cache(merge=False)
            self.con_cc(refreshObjs=True,delSrc=True)



    def refreshObjs(self,sel_objs):#清除要读取缓存的物体的历史，解除transform 信息的lock
        #sel_objs = pm.selected()
        ref_lst = []
        for n in sel_objs:
            if n.isReferenced() and n.referenceFile() not in ref_lst: ref_lst.append(n.referenceFile())
        for e_ref in ref_lst: e_ref.importContents()
        pm.select(sel_objs)
        mel.eval("DeleteHistory")
        for ea in sel_objs:
            for ea_attrGrp in [ea.translate, ea.rotate, ea.scale]:
                for ea_attr in ea_attrGrp.children():
                    ea_attr.unlock()
            print ("==============node history deleted {}".format(ea.name()))
        #
        # info = abct.r4f()
        # all_msg = abct.im_cache(info)

    def con_cc(self,refreshObjs=False,delSrc=False):# 通过导入的缓存信息  链接 目标物体的属性
        infor = self.readDate
        #all_msg = self.im_cache(infor)
        if refreshObjs:self.refreshObjs(pm.selected())
        objs_dic = {}
        for ea_sh in self.all_msg['objs'].values()[0].keys():
            objs_dic[ea_sh.name(stripNamespace=True)] = ea_sh
        for ea_tr in self.all_msg['objs'].values()[0].values():
            objs_dic[ea_tr.name(stripNamespace=True)] = ea_tr

        for ea_con_pare in self.all_msg['conmsg'].values()[0]:
            cc_mesh = ea_con_pare[1].node()
            if cc_mesh.name() not in objs_dic: continue
            con_cc_mesh = objs_dic[cc_mesh.name()]
            res_con = self.dup_connect(cc_mesh, con_cc_mesh,delSrc)
            print res_con

    def dup_connect(self,src_obj, targ_obj,delSrc=False):#复制链接
        con_msg = src_obj.listConnections(c=True, p=True, s=True, d=False)
        con_msg_dic = dict((y, x) for x, y in con_msg)
        con_faile = []
        for ea_con in con_msg_dic:
            try:
                ea_con >> targ_obj.attr(con_msg_dic[ea_con].attrName())
                print ("Attribute connected !!! {} >>> {}".format(ea_con.name(),targ_obj.attr(con_msg_dic[ea_con].attrName()).name()))
            except:
                con_faile.append({ea_con:targ_obj.attr(con_msg_dic[ea_con].attrName())})
        if not delSrc:print"WHY???????????????????"
        if delSrc:
            if src_obj.type() != 'transform': pm.delete(src_obj.getParent())
            else:pm.delete(src_obj)
        if len(con_faile): return con_faile
        else: return ("Connected Done!!!")

        # AlembicImportOptions;
        # performAlembicImport 1 2;
        #
        # AbcImport - mode
        # import
        # -setToStartFrame - debug - connect
        # "yi_45 KOUZI xie_L xie_R yi_48 yi_49 yi_54 yi_50 yi_53 yi_52 polySurface5 L_shoutao R_shoutao kuzi yi_55 sijin_Model head_Model dn_teeth dn_oral up_teeth up_oral tongue R_eye R_eyecon L_eye L_eyecon R_Lash L_Lash leixian_r leixian_l maozi grow_mesh" - createIfNotFound - removeIfNoUpdate
        # "E:/work/FAQ_ALL/cache/alembic/all_exp_abc_003.abc";
        # AbcExport -j "-frameRange 11861 11871 -uvWrite -worldSpace -writeVisibility -dataFormat ogawa -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_45 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:KOUZI -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_L -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_R -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_48 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_49 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_54 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_50 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_53 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_52 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_51|CDMSS_ch001001Moss_l_msAnim:polySurface5 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:L_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:R_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:kuzi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_55 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:sijin_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:head_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:tongue -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:R_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:L_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_r -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_l -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:Yeti|CDMSS_ch001001Moss_l_msAnim:Growmesh|CDMSS_ch001001Moss_l_msAnim:grow_mesh -file E:/work/FAQ_ALL/cache/alembic/all_exp_abc_004.abc";
    # AbcExport -j "-frameRange 11861 11871 -stripNamespaces -uvWrite -worldSpace -writeVisibility -dataFormat ogawa -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_45 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:KOUZI -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_L -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_R -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_48 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_49 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_54 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_50 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_53 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_52 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_51|CDMSS_ch001001Moss_l_msAnim:polySurface5 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:L_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:R_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:kuzi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_55 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:sijin_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:head_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:tongue -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:R_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:L_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_r -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_l -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:Yeti|CDMSS_ch001001Moss_l_msAnim:Growmesh|CDMSS_ch001001Moss_l_msAnim:grow_mesh -file E:/work/FAQ_ALL/cache/alembic/all_exp_abc_005.abc";
    # AbcImport -mode import -setToStartFrame -debug -connect "CDMSS_ch001002MossV2_Hair_h_msAnim:yi_45 CDMSS_ch001002MossV2_Hair_h_msAnim:KOUZI CDMSS_ch001002MossV2_Hair_h_msAnim:up_oral CDMSS_ch001002MossV2_Hair_h_msAnim:yi_54 CDMSS_ch001002MossV2_Hair_h_msAnim:L_eye CDMSS_ch001002MossV2_Hair_h_msAnim:L_shoutao CDMSS_ch001002MossV2_Hair_h_msAnim:leixian_r CDMSS_ch001002MossV2_Hair_h_msAnim:R_Lash CDMSS_ch001002MossV2_Hair_h_msAnim:up_teeth CDMSS_ch001002MossV2_Hair_h_msAnim:yi_50 CDMSS_ch001002MossV2_Hair_h_msAnim:maozi CDMSS_ch001002MossV2_Hair_h_msAnim:kuzi CDMSS_ch001002MossV2_Hair_h_msAnim:leixian_l CDMSS_ch001002MossV2_Hair_h_msAnim:xie_L CDMSS_ch001002MossV2_Hair_h_msAnim:dn_teeth CDMSS_ch001002MossV2_Hair_h_msAnim:yi_55 CDMSS_ch001002MossV2_Hair_h_msAnim:sijin_Model CDMSS_ch001002MossV2_Hair_h_msAnim:yi_53 CDMSS_ch001002MossV2_Hair_h_msAnim:L_eyecon CDMSS_ch001002MossV2_Hair_h_msAnim:R_eyecon CDMSS_ch001002MossV2_Hair_h_msAnim:head_Model CDMSS_ch001002MossV2_Hair_h_msAnim:polySurface5 CDMSS_ch001002MossV2_Hair_h_msAnim:tongue CDMSS_ch001002MossV2_Hair_h_msAnim:R_shoutao CDMSS_ch001002MossV2_Hair_h_msAnim:grow_mesh CDMSS_ch001002MossV2_Hair_h_msAnim:yi_49 CDMSS_ch001002MossV2_Hair_h_msAnim:R_eye CDMSS_ch001002MossV2_Hair_h_msAnim:yi_48 CDMSS_ch001002MossV2_Hair_h_msAnim:L_Lash CDMSS_ch001002MossV2_Hair_h_msAnim:dn_oral CDMSS_ch001002MossV2_Hair_h_msAnim:xie_R CDMSS_ch001002MossV2_Hair_h_msAnim:yi_52" -createIfNotFound -removeIfNoUpdate "E:/work/FAQ_ALL/cache/alembic/all_exp_abc_001.abc";

if __name__ == "__main__":
#先运行 下面两行代码
    import OCT_anim.ABC_tmp as abct
    reload(abct)

    # ===== 动画师 输出 缓存 和 记录 选择模型信息文件 执行下面一行代码
    abct.wr2f()
    # ==== 运行之后，会在 当前工程目录 路径 下 有一个 .json 格式的文件，这个文件是记录 选择的模型的
    # 把输出的缓存 和这个 json 文件 一并 提供给 美术师
    #===================================================================================================================
    """
    =====灯光美术师 选择要读取缓存的模型的组(要import，因为在两个leixia模型的设置并不全是rig蒙皮
    
    一共三行代码 逐行运行 选择到 当前角色读取缓存的模型，要进行解锁和删除历史操作
    """
    # 第一步 选择缓存 和记录模型信息的文件 导入相关信息
    info = abct.r4f()
    # 第二步 确保已选择要读取缓存的角色的大组(是该角色的大组）根据动画师记录的信息程序会选择相应的模型
    con_cc_objs = abct.list_rdcc_meshs(info)
    # 第三部，对当前选择的模型进行，清历史，解锁通道栏translate属性，
    # 第四部 运行下面脚本
    abct.im_cache(info, con_cc_objs)