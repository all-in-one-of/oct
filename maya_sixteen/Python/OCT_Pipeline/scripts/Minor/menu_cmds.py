#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = OCT_Pipeline_menu
__author__ = zhangben 
__mtime__ = 2019/3/28 : 14:05
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import maya.cmds as mc
from past import sk_checkTools


print("I am OCT_Pipeline -_-")
import maya.cmds as mc
import scripts.Minor as Minor
import sys
# sys.path.append(r"F:\Development\octProj\oct\maya_sixteen\Python")
import PySide.QtGui as psqg
import PySide.QtCore as psgc
import maya.OpenMayaUI as mui
from PySide import __version__
from shiboken import wrapInstance



def call_load_pl_menu():#load pipeline menu items
    # print ("call load pl menu ----------")
    # print locals()
    # print("==============================")
    # print globals()
    # mc.menuItem('OCT_Pipline',)
    # mc.menuItem("pre_normalizeTools", label=u"asset文件check tool", ann='资产文件规范检查工具', parent="OCT_Pipeline_mi", c="import OCT_Pipeline\nreload(OCT_Pipline)")
    # mc.menuItem("waiting_mi", label=u"待添加", ann='waiting...', parent="OCT_Pipeline_mi", c="import OCT_Pipeline\nreload(OCT_Pipline)\nOCT_Pipeline.scripts.Minor.asset_check_cmd()")
    #



mui.MQtUtil.mainWindow()

ptr = mui.MQtUtil.mainWindow()
widget = wrapInstance(long(ptr), psqg.QWidget)

widget.children()

maya_menu = widget.findChild(psqg.QMenu)

maya_menu
maya_menu.aboutToHide()

maya_menu.children()

ppl_menu = mui.MQtUtil.findMenuItem('OCT_Pipeline_mi')
ppl_menu2qt = wrapInstance(long(oct_menu), psqg.QWidget)





ptr = mui.MQtUtil.mainWindow()
widget = wrapInstance(long(ptr), psqg.QWidget)


maya_menu = widget.findChild(psqg.QMenuBar)
#oct_menu = [ea_mi for ea_mi in maya_menu.children() if ea_mi.objectName()=='OCT_ToolSetMN']
oct_menu = maya_menu.findChild(psqg.QMenu,'OCT_ToolSetMN')
ppl_menu = oct_menu.findChild(psqg.QMenu,'OCT_Pipeline_mi')






def asset_check_cmd():#前期资产检测整理
    asckt = sk_checkTools.sk_checkTools()
    asckt.sk_sceneUICheckTools()