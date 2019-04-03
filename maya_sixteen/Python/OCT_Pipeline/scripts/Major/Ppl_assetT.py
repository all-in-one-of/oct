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
import sys,os
import maya.cmds as mc
import pymel.core as pm
import shiboken
from ..utility import Kits
from ..past import sk_checkTools
from ..import Minor
reload(Minor)


SCRIPT_LOC = os.path.split(__file__)[0]
class Ppl_assetT_main(QtGui.QMainWindow):
    def __init__(self):
        """
        前期检测整理工具集
        """
        ppl_UI = os.path.join(Kits.Kits.get_dir(SCRIPT_LOC, 2), r'media\ppl_assetTool.ui')
        MayaMain = shiboken.wrapInstance(long(mui.MQtUtil.mainWindow()), QtGui.QWidget)
        super(Ppl_assetT_main,self).__init__(MayaMain)
        #=======button connection procedure
        self.skct = sk_checkTools.sk_checkTools()
        # main window load/settings
        self.ui = self.loadUiWidget(ppl_UI,MayaMain)
        self.ui.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
        self.ui.destroyed.connect(self.onExitCode)
        self.ui.show()

        self.makeConnections()
        #self.showUI()
        #self.ui.show()
        #self.ppl_at_win = ""
        #self.call_it()

    def makeConnections(self):
        # select by name button
        self.ui.selByNm_bt.clicked.connect(lambda: self.selByNm())
        # rename button
        import Minor.Ppl_rnmtools_auto as prnm
        self.ui.nm_tidy_bt.clicked.connect(prnm.Pre_regNaming())



    #=========↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   connected functions ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓========================================
    def onExitCode(self):
        sys.stdout.write("You closed the demo ui !!\n")
    def somFunc(self,someArg):
        print someArg

    def selByNm(self):
        srcStr = self.ui.pick_sel_l.text()
        pm.select(srcStr)

    #=========↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑    connected functions  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑========================================

    def loadUiWidget(self,uifilename, parent=None):
        """import ui file"""
        loader = QtUiTools.QUiLoader()
        uifile = QtCore.QFile(uifilename)
        uifile.open(QtCore.QFile.ReadOnly)
        ui = loader.load(uifile, parent)
        uifile.close()
        return ui



#
# def call_it():
#     if not mc.window('ppl_asset_win',exists=True):
#         win = Ppl_assetT_main()
#     else:
#         sys.stdout.write("Tools is already open!\n")

    #win.showUI()