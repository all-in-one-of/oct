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
import shiboken
from ..utility import Kits

SCRIPT_LOC = os.path.split(__file__)[0]


class Ppl_assetT_main(QtGui.QMainWindow):
    def __init__(self):
        ppl_UI = os.path.join(Kits.Kits.get_dir(SCRIPT_LOC, 2), r'media\ppl_assetTool.ui')
        MayaMain = shiboken.wrapInstance(long(mui.MQtUtil.mainWindow()), QtGui.QWidget)
        super(Ppl_assetT_main,self).__init__(MayaMain)

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
        self.ui.selByNm_bt.clicked.connect(lambda: self.somFunc("I'am a function!!!"))
    def onExitCode(self):
        sys.stdout.write("You closed the demo ui !!\n")
    def somFunc(self,someArg):
        print someArg

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