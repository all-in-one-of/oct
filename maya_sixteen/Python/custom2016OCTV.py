#!/usr/bin/env python
# coding=utf-8

import os
import re
import sys
import maya.cmds as mc
import maya.mel as mm
import maya.utils as mu
import maya.OpenMaya as om
import shutil

def projectsSearch():
    MAYA_SCRIPT_PATH = mm.eval('getenv "MAYA_SCRIPT_PATH";')
    #加载各项目到MAYA_SCRIPT_PATH里
    projRoot = r"\\octvision.com\cg\Tech\maya_sixteen\scripts\Themes"
    ret = mc.getFileList(folder=projRoot)
    for item in ret:
        subfolder = projRoot + item
        if os.path.isdir(subfolder):
            MAYA_SCRIPT_PATH += ";" + subfolder
            mm.eval('putenv "MAYA_SCRIPT_PATH" "%s";' % MAYA_SCRIPT_PATH)

def RepairShader():
    import re
    import maya.cmds as mc
    import maya.mel as mm
    global RepairShader
    #修正材质问题
    allMyMeshs = []
    allMyCacheFiles = mc.ls(type='cacheFile')
    if allMyCacheFiles:
        for myCacheFile in allMyCacheFiles:
            allSwitchs = mc.listConnections(myCacheFile)
            if allSwitchs:
                for switch in allSwitchs:
                    if mc.nodeType(switch) == 'historySwitch':
                        sMeshs = mc.listConnections('%s.outputGeometry' % switch)
                        if sMeshs:
                            for sMesh in sMeshs:
                                Rmeshs = mc.listRelatives(sMesh, c=True, s=True, pa=True)
                                if Rmeshs:
                                    for Rmesh in Rmeshs:
                                        ShapeType = mc.nodeType(Rmesh)
                                        if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
                                            if not mc.getAttr("%s.intermediateObject" % Rmesh):
                                                allMyMeshs.append(Rmesh)
    if allMyMeshs:
        for a_each in allMyMeshs:
            groupIds = mc.listConnections(a_each, t='groupId', d=False, s=True)
            if groupIds:
                for b_each in groupIds:
                    mygroupParts = mc.listConnections(b_each, t='groupParts', d=True, s=False)
                    if mygroupParts:
                        if mm.eval('attributeExists "ic" "%s"' % mygroupParts[0]):
                            tmp = mc.getAttr('%s.ic' % mygroupParts[0])
                            if tmp:
                                for c_each in tmp:
                                    if re.search("f\[[A-Za-z0-9:]*\]", c_each):
                                        SG = mc.listConnections('%s.message' % b_each, t='shadingEngine', d=True, s=False)
                                        if SG:
                                            if SG[0]:
                                                try:
                                                    mc.sets('%s.%s' % (a_each, c_each), fe=SG[0])
                                                except:
                                                    pass

def CommonSceneOpened():
    import re
    import maya.cmds as mc
    import maya.mel as mm
    global CommonSceneOpened
    #检查C盘大小
    if not mc.about(batch=True):
        freeSV = mm.eval('strip(system("wmic LogicalDisk where Caption=\'C:\' get FreeSpace /value"))')
        freeMV = re.sub("\D", "", freeSV)
        if freeMV < 100000000:
            mc.confirmDialog(message=u"C:盘空间过小将影响性能，建议马上清理磁盘空间", button="OK")
    mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "";')
    mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "";')
    #加载playBlast全局变量
    mm.eval('global int $octvCrossPB;$octvCrossPB=0;')
    #设置任何文件单位为厘米
    mc.currentUnit(l='centimeter', ua=True)
#开文件触发检查C盘空间大小事件
def OCTVSceneOpenedScriptJob():
    global OCTVSceneOpenedScriptJob
    mc.scriptJob(event=("SceneOpened", CommonSceneOpened))

def replaceYetiCachePath():
    #重置Yeti的路径
    try:
        allYetiCacheFiles = mc.ls(type='pgYetiMaya')
    except:
        getProMel=mc.getAttr("defaultRenderGlobals.preMel")
        getPostMel=mc.getAttr("defaultRenderGlobals.postMel")

        if getProMel and getPostMel and getProMel=="pgYetiVRayPreRender" and getPostMel=="pgYetiVRayPostRender":
            mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "";')
            mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "";')
        elif getProMel and "pgYetiVRayPreRender" in getProMel:
            if "pgYetiVRayPreRender;" in getProMel:
                getProMel=getProMel.replace("pgYetiVRayPreRender;","")
            else:
                getProMel=getProMel.replace("pgYetiVRayPreRender","")
            mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "%s";'%getProMel)

        elif getPostMel and "pgYetiVRayPostRender" in getPostMel:
            if "pgYetiVRayPostRender;" in getPostMel:
                getPostMel=getPostMel.replace("pgYetiVRayPostRender;","")
            else:
                getPostMel=getPostMel.replace("pgYetiVRayPostRender","")
            mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "%s";'%getPostMel)

    else:
        if allYetiCacheFiles:
            for myYetiCacheFile in allYetiCacheFiles:
                YetiFileMode = None
                try:
                    YetiFileMode = mc.getAttr('%s.fileMode' % myYetiCacheFile)
                except:
                    pass
                else:
                    if YetiFileMode == 2:
                        YetiCachePath = mc.getAttr('%s.cacheFileName' % myYetiCacheFile)
                        YetiCachePath = YetiCachePath.replace('\\','/')
                        if YetiCachePath:
                            mc.setAttr('%s.cacheFileName' % myYetiCacheFile, YetiCachePath, type='string')
        else:
            getProMel=mc.getAttr("defaultRenderGlobals.preMel")
            getPostMel=mc.getAttr("defaultRenderGlobals.postMel")

            if getProMel and getPostMel and getProMel=="pgYetiVRayPreRender" and getPostMel=="pgYetiVRayPostRender":
                mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "";')
                mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "";')
            elif getProMel and "pgYetiVRayPreRender" in getProMel:
                if "pgYetiVRayPreRender;" in getProMel:
                    getProMel=getProMel.replace("pgYetiVRayPreRender;","")
                else:
                    getProMel=getProMel.replace("pgYetiVRayPreRender","")
                mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "%s";'%getProMel)

            elif getPostMel and "pgYetiVRayPostRender" in getPostMel:
                if "pgYetiVRayPostRender;" in getPostMel:
                    getPostMel=getPostMel.replace("pgYetiVRayPostRender;","")
                else:
                    getPostMel=getPostMel.replace("pgYetiVRayPostRender","")
                mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "%s";'%getPostMel)
                                
    try:
        allShaveGlobals=mc.ls(type="shaveGlobals")
    except:
        getShaveProMel=mc.getAttr("defaultRenderGlobals.preMel")
        getShavePostMel=mc.getAttr("defaultRenderGlobals.postMel")

        if getShaveProMel and getShavePostMel and getShaveProMel=="shaveVrayPreRender" and getShavePostMel=="shaveVrayPostRender":
            mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "";')
            mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "";')
            
        elif getShaveProMel and "shaveVrayPreRender" in getShaveProMel:
            if "shaveVrayPreRender;" in getShaveProMel:
                getShaveProMel=getShaveProMel.replace("shaveVrayPreRender;","")
            else:
                getShaveProMel=getShaveProMel.replace("shaveVrayPreRender","")
            mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "%s";'%getShaveProMel)

        elif getShavePostMel and "shaveVrayPostRender" in getShavePostMel:
            if "shaveVrayPostRender;" in getShavePostMel:
                getShavePostMel=getShavePostMel.replace("shaveVrayPostRender;","")
            else:
                getShavePostMel=getShavePostMel.replace("shaveVrayPostRender","")
            mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "%s";'%getShavePostMel)

    else:
        if not allShaveGlobals:
            getShaveProMel=mc.getAttr("defaultRenderGlobals.preMel")
            getShavePostMel=mc.getAttr("defaultRenderGlobals.postMel")

            if getShaveProMel and getShavePostMel and getShaveProMel=="shaveVrayPreRender" and getShavePostMel=="shaveVrayPostRender":
                mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "";')
                mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "";')
                
            elif getShaveProMel and "shaveVrayPreRender" in getShaveProMel:
                if "shaveVrayPreRender;" in getShaveProMel:
                    getShaveProMel=getShaveProMel.replace("shaveVrayPreRender;","")
                else:
                    getShaveProMel=getShaveProMel.replace("shaveVrayPreRender","")
                mm.eval('setAttr -type "string" defaultRenderGlobals.preMel "%s";'%getShaveProMel)

            elif getShavePostMel and "shaveVrayPostRender" in getShavePostMel:
                if "shaveVrayPostRender;" in getShavePostMel:
                    getShavePostMel=getShavePostMel.replace("shaveVrayPostRender;","")
                else:
                    getShavePostMel=getShavePostMel.replace("shaveVrayPostRender","")
                mm.eval('setAttr -type "string" defaultRenderGlobals.postMel "%s";'%getShavePostMel)

    # #判断参考的方式是否正确
    # info=""
    # try:
    #     allReference=mc.file(q=True,reference=True)
    # except:
    #     pass
    # else:
    #     if allReference:
    #         for myReference in allReference:
    #             refer=mc.referenceQuery(myReference,namespace=True,shortName=True)
    #             if not refer:
    #                 info=info+myReference+"\n"
    #     if info:
    #         mc.confirmDialog(message=u"下列参考文件的参考方式出错了：\n"+info)



#开文件触发检查C盘空间大小事件
def YetiSceneOpenedScriptJob():
    global YetiSceneOpenedScriptJob
    mc.scriptJob(event=("SceneOpened", replaceYetiCachePath))
    
def ClosePluginAutoload():
    pluginList = mc.pluginInfo(q=True, ls=True)
    noPluginList = ['AbcImport', 'AbcExport', 'objExport', 'fbxmaya']
    if pluginList:
        for pluginName in pluginList:
            if pluginName in noPluginList:
                continue
            try:
                if mc.pluginInfo(pluginName, q=True, a=True):
                    mc.pluginInfo(pluginName, e=True, a=False)
            except:
                pass

def delVraypluginDir():
    mayaPath = os.environ['MAYA_LOCATION']
    vraypluginPath = os.path.normpath(os.path.join(mayaPath,'vray','vrayplugins'))
    if os.path.exists(vraypluginPath):
        try:
            shutil.rmtree(vraypluginPath)
        except Exception as e:
            print ('vrayplugins folder delete error , because {} '.format(e))

if os.getenv('VRIPRCOPYPATH'):
    delVraypluginDir()

def customOCTV():
    #检查机器名
    UserName = os.environ['COMPUTERNAME']
    if UserName:
        if UserName[:4].upper() == 'PCGR' or UserName[:2].upper() == 'SM' or UserName[:2].upper() == 'HW' or UserName[:6].upper() == 'TXXR' or UserName[:6].upper() == 'RENDER' or UserName[:6].upper() == 'render' or UserName[:3].upper() == 'WIN' or UserName[:6].upper() == 'YUNHAI' or UserName[:2].upper() == 'XR':
            #加载PYQT
            try:
                projectsSearch()
            except:
                pass
        #载入开启maya的触发事件
        #修复物体材质
        global OCTVSceneOpenedScriptJob
        mc.scriptJob(event=("SceneOpened", RepairShader))

        #删除插件自动加载功能
        mc.scriptJob(event=("SceneOpened", ClosePluginAutoload))

        if not mc.about(batch=True):
            #启动检查磁盘大小的命令
            global OCTVSceneOpenedScriptJob
            mc.scriptJob(event=("SceneOpened", CommonSceneOpened))

            YetiSceneOpenedScriptJob()
             #加载PYQT
            try:
                import OCT_menu
                OCT_menu.makeMenu()
            except:
                om.MGlobal.displayError(u'加载界面时出现异常3,请联系管理员.')
            # try:
            #     if not mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
            #         mc.loadPlugin('vrayformaya.mll')
            # except:
            #     om.MGlobal.displayError(u'Vray渲染器没有安装！请安装！')
            # try:
            #     if not mc.pluginInfo('mtoa.mll', query=True, loaded=True):
            #         mc.loadPlugin('mtoa.mll')
            # except:
            #     om.MGlobal.displayError(u'Arnold渲染器加载失常，请联系管理员！')
            # try:
            #     if not mc.pluginInfo('pgYetiMaya.mll', query=True, loaded=True):
            #         mc.loadPlugin('pgYetiMaya.mll')
            # except:
            #     om.MGlobal.displayError(u'Arnold渲染器加载失常，请联系管理员！')
        try:
        #设置通信端口
            if not mc.commandPort('0.0.0.0:8321', q=True):
                mc.commandPort(n='0.0.0.0:8321', stp='python', eo=True)
            if not mc.commandPort('0.0.0.0:8322', q=True):
                mc.commandPort(n='0.0.0.0:8322', stp='mel', eo=True)
        except:
            pass
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
        del OCT_check
        del OCT_vr
        del OCT_hair
        del OCT_matLib
        del OCT_proxy
        del OCT_animImEx
        del OCT_rigging
        del OCT_Projects
        sys.path.remove(r'\\octvision.com\cg\Tech\maya_sixteen')
        om.MGlobal.displayError(u'OCT工具初始化时出现异常,请联系管理员.')
customOCTV()
