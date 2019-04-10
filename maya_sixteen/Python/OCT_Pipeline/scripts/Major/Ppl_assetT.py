#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Ppl_checkT_asset
__author__ = zhangben 
__mtime__ = 2019/4/1 : 18:24
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

from PySide import QtGui,QtCore,QtUiTools
import maya.OpenMayaUI as mui
import sys,os,copy,re
import maya.mel as mel
import pymel.core as pm
import shiboken
from ..utility import Kits
reload(Kits)
from ..past import sk_checkTools,sk_sceneTools,sk_smoothSet
reload(sk_checkTools)
reload(sk_sceneTools)
reload(sk_smoothSet)
SCRIPT_LOC = os.path.split(__file__)[0]
class Ppl_assetT_main(QtGui.QMainWindow):
    def __init__(self):#load ui  show it
        """
        前期检测整理工具集
        """
        ppl_UI = os.path.join(Kits.Kits.get_dir(SCRIPT_LOC, 2), r'media\ppl_assetTool.ui')
        MayaMain = shiboken.wrapInstance(long(mui.MQtUtil.mainWindow()), QtGui.QWidget)
        super(Ppl_assetT_main,self).__init__(MayaMain)
        #=======program MEL path ====================
        self.mel_dir = os.path.join(Kits.Kits.get_dir(SCRIPT_LOC, 1),'MEL')
        #=======relative modules======================
        self.skchk = sk_checkTools.sk_checkTools()
        self.sksct = sk_sceneTools.sk_sceneTools()
        self.sksmth = sk_smoothSet.sk_smoothSet()
        # main window load/settings
        self.ui = self.loadUiWidget(ppl_UI,MayaMain)
        self.ui.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
        self.ui.destroyed.connect(self.cmd_onExitCode)
        self.ui.move(200,400)
        self.buttonsList = [ea_bt.objectName() for ea_bt in self.ui.findChildren(QtGui.QPushButton) if ea_bt.objectName().endswith('_bt')]

        self.ui.show()

        self.makeConnections()

    def makeConnections(self): # connect buttons to fucntions
        for each_bt in self.buttonsList:
            _fuction = getattr(self,"cmd_{}".format(each_bt)) if "cmd_{}".format(each_bt) in self.__class__.__dict__ else self._somFunc
            self.ui.findChildren(QtGui.QPushButton, each_bt)[0].clicked.connect(_fuction)
    #=========↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   connected functions ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓========================================
    def cmd_onExitCode(self):
        sys.stdout.write("You closed the demo ui !!\n")
    def _somFunc(self):
        print("some function return what a F~~")
    #  call tools buttons commands =================================
    def cmd_rnmT_bt(self):#重命名工具
        src_mel = os.path.abspath(os.path.join(self.mel_dir, 'Quick_rename_tool.mel'))
        src_mel = re.sub(r'\\','/',src_mel)
        mel.eval("source \"{}\"".format(src_mel))
        mel.eval("Quick_rename_tool()")

    def cmd_smoothSetT_bt(self): # smooth set 设置工具
        self.sksmth.UI_setSmooth()
    #  call fuction buttons commands ================================
    # 根据名字选择
    def cmd_selByNm_bt(self):
        srcStr = self.ui.pick_sel_l.text()
        ls_objs = pm.ls(srcStr)
        pm.select(ls_objs)
    # 自动重命名
    def cmd_nm_tidy_bt(self):
        from ..Minor import Ppl_rnmtools_auto
        reload(Ppl_rnmtools_auto)
        Ppl_rnmtools_auto.Pre_regNaming()
    # 添加后缀 _
    def cmd_suff_tidy_bt(self):
        self.skchk.checkRenameMSHPosfix()
    # 检查 namespace
    def cmd_chkNmsp(self):
        self.skchk.checkModelDetailsWarning("nsCheck")
    # namespace工具
    def cmd_nmsp_tidy_bt(self):
        src_mel = os.path.abspath(os.path.join(self.mel_dir,'common_namespaceTools.mel'))
        src_mel = re.sub(r'\\', '/', src_mel)
        mel.eval("source \"{}\"".format(src_mel))
        mel.eval("common_namespaceTools")
    # 清理多余的显示层
    def cmd_dsly_tidy_bt(self):
        self.sksct.checkCleanDisplayLayers()
        print("DisplayLayer Tidied!!!")
    # delete empty group
    def cmd_emgrp_tidy_bt(self):
        allTrans = pm.ls(tr=True)
        emt = []
        for e in allTrans:
            print e
    #添加 ct_an 标记 标记物体输出动画
    def cmd_anlab_tidy_bt(self):
        self.skchk.checkCTANSignAdd()
    def cmd_set_tidy_bt(self):# 自动标记set组
        self.sksct.checkCacheSetAdd()
        self.sksct.checkTransAnimSetAdd()
        self.sksct.sk_sceneCacheAnimSetConfig("Cache", "ZM")
        self.sksct.sk_sceneCacheAnimSetConfig("Anim", "ZM")
    def cmd_ref_chk_bt(self):#检查参考
        self.skchk.checkModelDetailsWarning("refCheck")
    def cmd_nmsp_chk_bt(self):#检查namespace
        self.skchk.checkModelDetailsWarning("nsCheck")
    def cmd_nm_chk_bt(self):#检查命名
        self.skchk.checkModelDetailsWarning("MSHCheck")
    def cmd_fnm_chk_bt(self):#检查面数
        self.skchk.checkModelDetailsWarning("faceCheck")
    def cmd_ins_chk_bt(self):#检查instance
        self.skchk.checkModelDetailsWarning("insCheck")
    def cmd_sm_chk_bt(self):  # 检查smooth
        self.skchk.checkModelDetailsWarning("moothCheck")
    def cmd_flg_chk_bt(self):  # 检测属性标记
        self.skchk.checkModelDetailsWarning("signCheck")
    def cmd_tautonymy_chk_bt(self):  # 检查 transform 同名
        self.skchk.checkModelDetailsWarning("sameTransformCheck")
    def cmd_tautonymyShp_chk_bt(self): # 检查 shape同名
        self.skchk.checkModelDetailsWarning("sameShapeCheck")
    def cmd_tautonymyMsh_chk_bt(self): # 检查 mesh 同名
        self.skchk.checkModelDetailsWarning("sameShapeNodeCheck")
    def cmd_smthSet_chk_bt(self): # 检查smooth set
        self.skchk.checkModelDetailsWarning("smoothSet")
    def cmd_prxTr_chk_bt(self): # 检查proxy 位移
        self.skchk.checkModelDetailsWarning("proxyInfo")
    def cmd_rndSta_chk_bt(self):#检查 render state
        self.skchk.checkModelDetailsWarning("renderState")
    def cmd_selSmth_tidy_bt(self):#选取物体smooth
        self.sksmth.smoothSetDoSmooth(useSmoothSet = 1,selMode = 1)

    # check all items
    def cmd_all_chk_bt(self):
        print("\n".join(self.buttonsList))


    # smoothSetDoSmooth(useSmoothSet = 1,selMode = 1)

    #=========↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑    connected functions  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑========================================

    def loadUiWidget(self,uifilename, parent=None): # load ui file
        """import ui file"""
        loader = QtUiTools.QUiLoader()
        uifile = QtCore.QFile(uifilename)
        uifile.open(QtCore.QFile.ReadOnly)
        ui = loader.load(uifile, parent)
        uifile.close()
        return ui


    def nonUniqueObjects(self): # a function list all taotunymy object
        all_nds = pm.ls()
        non_uniques = {}
        temp_nm_dic = {}
        for ea_nd in all_nds:
            ndTyp = ea_nd.type()
            ndShtNm = ea_nd.name()
            ndLngNm = ea_nd.longName()
            if ndShtNm not in temp_nm_dic:
                temp_nm_dic[ndShtNm] = {ndTyp: [ea_nd]}
            else:
                if ndShtNm not in non_uniques:
                    cp_date = copy.deepcopy(temp_nm_dic[ndShtNm])
                    non_uniques[ndShtNm] = cp_date
                    if ndTyp in non_uniques[ndShtNm]:
                        non_uniques[ndShtNm].append(ea_nd)
                    else:
                        non_uniques[ndShtNm][ndTyp] = [ea_nd]
                else:
                    if ndTyp in non_uniques[ndShtNm]:
                        non_uniques[ndShtNm].append(ea_nd)
                    else:
                        non_uniques[ndShtNm][ndTyp] = [ea_nd]


#
# def call_it():
#     if not mc.window('ppl_asset_win',exists=True):
#         win = Ppl_assetT_main()
#     else:
#         sys.stdout.write("Tools is already open!\n")

    #win.showUI()