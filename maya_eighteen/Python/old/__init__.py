#!/usr/bin/env python
# coding=utf-8

import os
import string
import re
import sys
import math
import maya.utils
import maya.utils as mu
import maya.cmds as mc
import maya.mel as mm
import pymel as pm
import maya.OpenMaya as om

def projectsSearch():
    MAYA_SCRIPT_PATH = mm.eval('getenv "MAYA_SCRIPT_PATH";')
    #加载各项目到MAYA_SCRIPT_PATH里
    projRoot = r"\\octvision.com\cg\Tech\maya\scripts\Themes"
    ret = mc.getFileList(folder=projRoot)
    for item in ret:
        subfolder = projRoot + item
        if os.path.isdir(subfolder):
            MAYA_SCRIPT_PATH += ";" + subfolder
            mm.eval('putenv "MAYA_SCRIPT_PATH" "%s";' % MAYA_SCRIPT_PATH)
    #打印  MAYA_SCRIPT_PATH
    print MAYA_SCRIPT_PATH


def CommonSceneOpened():
    global CommonSceneOpened
    #修正材质问题
    mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "zwz_preRenderRepairShader;";')
    #加载playBlast全局变量
    mm.eval('global int $octvCrossPB;$octvCrossPB=0;')
    #设置任何文件单位为厘米
    mc.currentUnit(l='centimeter', ua=True)
    #检查并设置帧率
    # checkFrameRate()


#开文件触发检查C盘空间大小事件
def OCTVSceneOpenedScriptJob():
    global OCTVSceneOpenedScriptJob
    mc.scriptJob(event=("SceneOpened", CommonSceneOpened))


def customOCTV():
    UserName = os.environ['COMPUTERNAME']
    if UserName:
        if UserName[:4].upper() == 'PCGR' or UserName[:6].upper() == 'RENDER':
            #加载项目到Script
            sys.path.append(r'\\octvision.com\cg\Tech\maya\2013\Lib')
            try:
                from PyQt4 import QtCore, QtGui
                import maya.OpenMayaUI as mui
                import sip
            except:
                pass
            import OCT_about
            import OCT_anim
            import OCT_cam
            import OCT_generel
            import OCT_lgt
            import OCT_render
            import OCT_menu
            import OCT_mod
            import OCT_util
            import OCT_vfx
            try:
                projectsSearch()
            except:
                pass

            #载入开启maya的触发事件
            CommonSceneOpened()
            if not mc.about(batch=True):
                OCTVSceneOpenedScriptJob()
                try:
                    OCT_menu.makeMenu()
                except:
                    om.MGlobal.displayError(u'加载界面时出现异常2,请联系管理员.')
                #加载PYQT

                #设置通信端口
                if not mc.commandPort('0.0.0.0:8321', q=True):
                    mc.commandPort(n='0.0.0.0:8321', stp='python', eo=True)

                if not mc.commandPort('0.0.0.0:8322', q=True):
                    mc.commandPort(n='0.0.0.0:8322', stp='mel', eo=True)
                # mm.eval('putenv "MAYA_SCRIPT_PATH" "MAYA_TESTING_CLEANUP";')
        else:
            del OCT_about
            del OCT_anim
            del OCT_cam
            del OCT_generel
            del OCT_lgt
            del OCT_render
            del OCT_menu
            del OCT_mod
            del OCT_util
            del OCT_vfx
            sys.path.remove(r'\\octvision.com\cg\Tech\maya\2013')
            om.MGlobal.displayError(u'OCT工具初始化时出现异常,请联系管理员.')
customOCTV()