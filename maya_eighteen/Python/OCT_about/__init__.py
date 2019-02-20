#!/usr/bin/env python
# coding=utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import sys
import os
import maya.utils
import maya.cmds as mc
import maya.mel as mm


def delMenu():
    if mc.menu('OCT_ToolSetMN', exists=1):
        mc.deleteUI('OCT_ToolSetMN', m=1)


def source():
    if not mc.pluginInfo('getAnglePlugin.py', q=True, l=True):
        mc.loadPlugin(r'D:\work_fu\work\OCT\MayaSixteenScripts\Plugins\getAnglePlugin.py')

    # allfile = os.listdir(r'\\octvision.com\cg\td\Maya\2013\Scripts\Mel')

    # for eachfile in allfile:
    #     _split = eachfile.split('.')
    #     count = len(_split)
    #     if count > 1:
    #         if _split[count-1] == 'mel' and _split[0] != 'userSetup':
    #             _cmd = r'source "\\\\octvision.com\cg\\TD\\Maya\\2013\\Scripts\\Mel\\%s"' % eachfile
    #             try:
    #                 mm.eval(_cmd)
    #             except RuntimeError:
    #                 sys.stdout.write(u'%s 加载出错，详细情况请查看加载脚本的源代码...\n' % eachfile)

def refresh():
    delMenu()
    mm.eval('OCT_reloadMod;')
    source()
    maya.utils.executeDeferred(OCT_menu.makeMenu())

def helpDoc():
    os.startfile(u'file://octvision.com/cg/Tech/maya_sixteen/Doc/maya2016_Help_1.html')

def Maya2009Help():
    os.startfile(u'file://octvision.com/cg/Tech/maya/Doc/Maya2009/en_US/index.html')

def Maya2013Help():
    os.startfile(u'file://octvision.com/cg/Tech/maya/Doc/Maya2013/zh_CN/index.html')

def Maya2012Help():
    os.startfile(u'file://octvision.com/cg/Tech/maya/Doc/Maya2012/docs/Maya2012/zh_CN/index.html')

def Maya2012SDK():
    os.startfile(u'file://octvision.com/cg/Tech/maya/Doc/Maya2012/docs/Maya2012/SDK/index.html')

def Arnold_Binary_Alchemy_Help():
    os.startfile(u'file://octvision.com/cg/Tech/maya/Doc/Arnold_Binary_Alchemy_Help/index.htm')

def feedback():
    print 'feedback'

def aboutThis():
    mc.confirmDialog( title=u'TD`s team Introduce', message=u'Team Leader:赵志杰、张仙奕\n Team members:钟文洲', button=['OK'], defaultButton='Yes', dismissString='No')

