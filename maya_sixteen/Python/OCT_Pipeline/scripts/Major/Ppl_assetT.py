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
from ..past import sk_checkTools
reload(sk_checkTools)
from ..past import sk_sceneTools
reload(sk_sceneTools)
SCRIPT_LOC = os.path.split(__file__)[0]
class Ppl_assetT_main(QtGui.QMainWindow):
    def __init__(self):
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
        # main window load/settings
        self.ui = self.loadUiWidget(ppl_UI,MayaMain)
        self.ui.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
        self.ui.destroyed.connect(self.cmd_onExitCode)
        self.ui.move(200,400)
        self.ui.show()

        self.makeConnections()
        #self.showUI()
        #self.ui.show()
        #self.ppl_at_win = ""
        #self.call_it()

    def makeConnections(self):
        # select by name button
        self.ui.selByNm_bt.clicked.connect(lambda: self.cmd_selByNm())
        # rename tools
        self.ui.rnmT_bt.clicked.connect(lambda: self.cmd_rename_tool())
        # name clean up  button
        self.ui.nm_tidy_bt.clicked.connect(self.cmd_renm)
        # add _ suffix
        self.ui.suff_tidy_bt.clicked.connect(self.cmd_addSuffix)
        # namespace tools
        self.ui.nmsp_tidy_bt.clicked.connect(self.cmd_nmsp)
        # display layer tidy
        self.ui.dsly_tidy_bt.clicked.connect(self.cmd_dislyTidy)
        # empty group tidy
        self.ui.emgrp_tidy_bt.clicked.connect(self.cmd_empGrpTidy)
        # add mode ct_an flag
        self.ui.anlab_tidy_bt.clicked.connect(self.cmd_add_ctan)
        #  auto create set group
        self.ui.set_tidy_bt.clicked.connect(self.cmd_add_set)
        #  check:   reference
        self.ui.ref_chk_bt.clicked.connect(self.cmd_chk_ref)
        #  check:  namespace
        self.ui.nmsp_chk_bt.clicked.connect(self.cmd_chk_nmsp)
        #  check:  name
        self.ui.nm_chk_bt.clicked.connect(self.cmd_chk_nm)
        #  check:  face number
        self.ui.fnm_chk_bt.clicked.connect(self.cmd_add_set)
        #  check:  instance
        self.ui.ins_chk_bt.clicked.connect(self.cmd_add_set)
        #  check:  smooth
        self.ui.sm_chk_bt.clicked.connect(self.cmd_add_set)
        #  check:  flag attribute
        self.ui.flg_chk_bt.clicked.connect(self.cmd_add_set)
        #  check:  tautonymy
        self.ui.tautonymy_chk_bt.clicked.connect(self.cmd_add_set)
        #  check:  shape node tautonymy
        self.ui.tautonymyShp_chk_bt.clicked.connect(self.cmd_add_set)
        #  check:  flag attribute
        self.ui.flg_chk_bt.clicked.connect(self.cmd_add_set)

    #=========↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   connected functions ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓========================================
    def cmd_onExitCode(self):
        sys.stdout.write("You closed the demo ui !!\n")
    def _somFunc(self,someArg):
        print someArg
    def cmd_rename_tool(self):#重命名工具
        src_mel = os.path.abspath(os.path.join(self.mel_dir, 'Quick_rename_tool.mel'))
        src_mel = re.sub(r'\\','/',src_mel)
        mel.eval("source \"{}\"".format(src_mel))
        mel.eval("Quick_rename_tool()")
    # 根据名字选择
    def cmd_selByNm(self):
        srcStr = self.ui.pick_sel_l.text()
        pm.select(srcStr)
    # 自动重命名
    def cmd_renm(self):
        from ..Minor import Ppl_rnmtools_auto
        reload(Ppl_rnmtools_auto)
        Ppl_rnmtools_auto.Pre_regNaming()
    # 添加后缀 _
    def cmd_addSuffix(self):
        self.skchk.checkRenameMSHPosfix()
    # 检查 namespace
    def cmd_chkNmsp(self):
        self.skchk.checkModelDetailsWarning("nsCheck")
    # namespace工具
    def cmd_nmsp(self):
        src_mel = os.path.abspath(os.path.join(self.mel_dir,'common_namespaceTools.mel'))
        src_mel = re.sub(r'\\', '/', src_mel)
        mel.eval("source \"{}\"".format(src_mel))
        mel.eval("common_namespaceTools")
    # 清理多余的显示层
    def cmd_dislyTidy(self):
        self.sksct.checkCleanDisplayLayers()
        print("DisplayLayer Tidied!!!")
    # delete empty group
    def cmd_empGrpTidy(self):
        allTrans = pm.ls(tr=True)
        emt = []
        for e in allTrans:
            print e

    #添加 ct_an 标记 标记物体输出动画
    def cmd_add_ctan(self):
        self.skchk.checkCTANSignAdd()
    def cmd_add_set(self):# 自动标记set组
        self.sksct.checkCacheSetAdd()
        self.sksct.checkTransAnimSetAdd()
        self.sksct.sk_sceneCacheAnimSetConfig("Cache", "ZM")
        self.sksct.sk_sceneCacheAnimSetConfig("Anim", "ZM")
    def cmd_chk_ref(self):#检查参考
        self.skchk.checkModelDetailsWarning("refCheck")
    def cmd_chk_nmsp(self):#检查namespace
        self.skchk.checkModelDetailsWarning("nsCheck")
    def cmd_chk_nm(self):#检查命名
        self.skchk.checkModelDetailsWarning("MSHCheck")
    #=========↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑    connected functions  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑========================================

    def loadUiWidget(self,uifilename, parent=None):
        """import ui file"""
        loader = QtUiTools.QUiLoader()
        uifile = QtCore.QFile(uifilename)
        uifile.open(QtCore.QFile.ReadOnly)
        ui = loader.load(uifile, parent)
        uifile.close()
        return ui


    def nonUniqueObjects(self):
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