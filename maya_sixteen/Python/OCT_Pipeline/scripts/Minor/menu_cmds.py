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
import os
# from ..past import sk_checkTools

print("I am OCT_Pipeline -_-")
import PySide.QtGui as psqg
import PySide.QtCore as psgc
import maya.OpenMayaUI as mui
from PySide import __version__
from shiboken import wrapInstance


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
    ins_pplms._add('Action', 'assetCk_mi', u'asset 规范整理工具', asset_check_tools, menuLys=['OCT_Pipeline_mi'])

def asset_check_tools():
    asckt = sk_checkTools.sk_checkTools()
    asckt.sk_sceneUICheckTools()

if __name__ == "__main__":
    print __file__
    print __file__.split('/')[:-2]