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
import maya.mel as mel
import os,re
print("I am menu command config file")
from ..past import sk_checkTools

print("I am OCT_Pipeline -_-")
import PySide.QtGui as psqg
import PySide.QtCore as psgc
import maya.OpenMayaUI as mui
from PySide import __version__
from shiboken import wrapInstance

SCRIPT_LOC = os.path.split(__file__)[0]
class add_menuItem(object):#添加菜单项
    def __init__(self):
        pass
    def add_item(self,item_type,item_nm,lableTxt,con_func,menuLys):
        ptr = mui.MQtUtil.mainWindow()
        widget = wrapInstance(long(ptr), psqg.QWidget)
        maya_menu_bar = widget.findChild(psqg.QMenuBar)
        p_menu = maya_menu_bar
        for ea_arg in menuLys:
            tmp_menu = p_menu
            tmp_ch_menu = tmp_menu.findChild(psqg.QMenu, ea_arg)
            if tmp_ch_menu == None:
                p_menu = tmp_menu
                print("There is not a childe menu name:{}".format(ea_arg))
                break
            else: p_menu = tmp_ch_menu
        if item_type in ['seperator', 'Seperator']:
            p_menu.addSeparator()
        elif item_type == 'menu':
            newMenu = p_menu.addMenu(item_nm)
        elif item_type == 'Action':
            new_item = p_menu.addAction(item_nm)
            new_item.setObjectName(item_nm)
            new_item.setText(lableTxt)
            new_item.triggered.connect(con_func)
#============================= add variously menu item connect commands==========================
class pipeline_menu_set(object): #配置 pipeline menu
    def __init__(self):
        pass
    def _add(self,item_type='seperator',item_nm=None,labelTxt=None,con_func=None,menuLys=None):
        ami = add_menuItem()
        ami.add_item(item_type, item_nm, labelTxt, con_func, menuLys)


def main():# pipeline menu 添加 菜单项
    filePath = __file__
    tools_sc_dir = '/'.join(filePath.split('/')[:2])
    tools_MEL_dir = "{}/MEL".format(tools_sc_dir)
    scrp_pth = os.environ.get("MAYA_SCRIPT_PATH")
    new_vl = "{};{}".format(scrp_pth,tools_MEL_dir)
    os.environ["MAYA_SCRIPT_PATH"] = new_vl

    ins_pplms = pipeline_menu_set()
    ins_pplms._add('Action', 'assetCk_mi', u'asset check工具', asset_check_tools, menuLys=['OCT_Pipeline_mi'])
    ins_pplms._add('Action', 'assetT_mi', u'asset 规范整理工具', call_ppl_ast_win, menuLys=['OCT_Pipeline_mi'])
    # ins_pplms._add()
    ins_pplms._add('Action', 'animDataIO', u'动画导入导出插件', call_ppl_ainmDataIO, menuLys=['OCT_Pipeline_mi'])


def asset_check_tools():
    asckt = sk_checkTools.sk_checkTools()
    asckt.sk_sceneUICheckTools()

def call_ppl_ast_win():
    from ..Major import Ppl_assetT
    reload(Ppl_assetT)
    if mc.window('ppl_asset_win', exists=True): mc.deleteUI('ppl_asset_win')
    pplast = Ppl_assetT.Ppl_assetT_main()

def call_ppl_ainmDataIO():
    # print("CALL ANIMATION EXPROT TOOLS")
    # print SCRIPT_LOC
    melDir = os.path.join(os.path.dirname(SCRIPT_LOC),r'MEL\dkAnim_v0.7.mel')
    # print melDir
    melDir_sub = re.sub("{0}{0}".format(os.sep),"/",melDir)
    mel_Cmd = "source \"{}\"".format(melDir_sub)
    # print mel_Cmd
    mel.eval(mel_Cmd)
    mel.eval("dkAnim()")
