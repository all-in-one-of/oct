# -*- coding: utf-8 -*-

from __future__ import with_statement #only needed for maya 2008 & 2009

import os
import maya.utils
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import string, sys
import shutil,re
import OCT_lgt

def makeMenu():
    _gMainWindow = mm.eval("global string $gMainWindow;string $temp = $gMainWindow;")
    #   _gMainWindow = 'MayaWindow'

    mc.setParent(_gMainWindow)
    mc.menu("OCT_ToolSetMN", l="OCT Vision", to=True, tearOff=False, parent=_gMainWindow)

    # mc.menuItem('subJob', label=u'提交Deadline渲染', c='OCT_menu.selectServerUI()', parent='OCT_ToolSetMN')
    mc.menuItem('checkin', l=u'Check in...', to=True, c='mm.eval("octvCheckinTool;")', parent='OCT_ToolSetMN')
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem('OCT_sub', l=u'提交任务到Deadline...', subMenu=True, to=True, parent='OCT_ToolSetMN')
    mc.menuItem('submitMayaJob_zwz_check', l=u'检查工程的完整性', ann=u'检查工程的完整性...', c='OCT_generel.submitMayaToDeadline_zwz(1)', parent='OCT_sub')
    mc.menuItem('submitMayaJob_zwz_copy', l=u'拷贝工程...', ann=u'拷贝工程...', c='OCT_generel.submitMayaToDeadline_zwz(2)', parent='OCT_sub')
    mc.menuItem('submitMayaJob_zwz_sub', l=u'提交文件至Deadline...', ann=u'提交文件至Deadline...', c='OCT_generel.submitMayaToDeadline_zwz(3)', parent='OCT_sub')
    mc.menuItem('submitMayaJob_zwz_sub_comp', l=u'提交文件至Deadline特别版(灯光组使用)...', ann=u'提交文件至Deadline，仅限合成同事使用', c='OCT_generel.submitMayaToDeadline_zwz(4)', parent='OCT_sub')
    mc.menuItem('submitMayaJob_zwz_deep', l=u'提交文件至Deadline设置deep(灯光组使用)...', ann=u'提交文件至Deadline设置deep，仅限合成同事使用', c='OCT_generel.submitMayaToDeadline_zwz(5)', parent='OCT_sub')

    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Generel", label=u"通用工具", ann=u'通用工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('OpenProjectFile', l=u'打开当前目录的相应文件夹...', ann=u'打开当前目录的相应文件夹...', c='mm.eval("zwz_OpenMyScenFile;")', parent='OCT_Generel')
    mc.menuItem("MasterAnimtoCache", label=u"根据ms_anim文件生成ms_cache文件", ann=u'根据ms_anim文件生成ms_cache文件', c='mm.eval("octvMsA2Cache")', parent="OCT_Generel")
    mc.menuItem("RenderSet_zwz", label=u"渲染面板快速设置...", ann=u'渲染面板快速设置...', c="OCT_generel.OCT_RenderSet_zwz.OCT_RenderSet_zwz_UI()", parent="OCT_Generel")
    mc.menuItem("ArnoldTools_zwz", label=u"Arnold快速设置...", ann=u'Arnold快速设置...', c="OCT_generel.callArnoldTools()", parent="OCT_Generel")
    mc.menuItem("ExportScene_zwz", label=u"导出并优化场景", ann=u'导出并优化场景', c='OCT_generel.OCT_Export_Scene_with_Optimize_zwz()', parent="OCT_Generel")
    mc.menuItem("rename", label=u"重命名...", ann=u'重命名...', c='mm.eval("NWrename_win;")', parent="OCT_Generel")
    #mc.menuItem("checkName", label=u"检查是否有重名", ann=u'检查是否有重名', c="OCT_generel.checkName()", parent="OCT_Generel")
    mc.menuItem("New_removeNamespace", l=u"新清除前缀名", ann=u'新清除前缀名', c='mm.eval("delete_name_space_zqs;")', parent="OCT_Generel")
    mc.menuItem("removeNamespace", l=u"清除前缀名工具", ann=u'清楚前缀名', c="OCT_generel.removeNamespace()", parent="OCT_Generel")
    mc.menuItem("deldefaultRenderLayer", l=u"清楚多余的DefaultRenderLayer", ann=u'清楚多余的DefaultRenderLayer', c="OCT_generel.delDefaultRenderLayer()", parent="OCT_Generel")
    mc.menuItem('cleanUnusedCameras_zwz', l=u'清除灯光物体中多余的摄像机', c="OCT_generel.cleanUnusedCamera_zwz()", parent="OCT_Generel")
    mc.menuItem('ReplaceOrOb', l=u'把许多物体改为关联复制...', ann=u'把许多物体改为关联复制...', c='OCT_generel.ReplaceOriginalObject()', parent='OCT_Generel')
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('changeRefPath', l=u'替换参考文件路径...', ann=u'替换参考文件路径...', c="OCT_generel.changeRefPath()", parent="OCT_Generel")
    mc.menuItem('fixCacheFilePath', l=u'修改点缓存节点路径...', ann=u'修改缓存节点路径...', c='OCT_generel.fixCacheFilePath()', parent='OCT_Generel')
    mc.menuItem('fixAbcCacheFilePath', l=u'修改Abc缓存节点路径...', ann=u'修改Abc缓存节点路径...', c='OCT_generel.fixAbcCacheFilePath()', parent='OCT_Generel')
    mc.menuItem('YetiCachePath', l=u'修改点Yeti缓存节点路径...', ann=u'修改点Yeti缓存节点路径...', c='OCT_generel.YetiCachePath()', parent='OCT_Generel')
    mc.menuItem('YetiFilePath', l=u'修改yeti贴图节点路径...', ann=u'修改yeti贴图节点路径...', c='OCT_generel.YetiFilePath()', parent='OCT_Generel')
    mc.menuItem('fixVRmeshFilePath', l=u'修改VRayMes节点路径...', ann=u'修改VRayMes节点路径...', c='OCT_generel.fixVRayMeshFilePath()', parent='OCT_Generel')
    mc.menuItem('fixAiStandInFilePath', l=u'修改aiStandIn节点路径...', ann=u'修改aiStandIn节点路径...', c='OCT_generel.fixaiStandInFilePath()', parent='OCT_Generel')
    mc.menuItem('VRayLightIESShapePath', l=u'修改VRayLightIESShape节点路径...', ann=u'修改VRayLightIESShape节点路径...', c='OCT_generel.VRayLightIESShapePath()', parent='OCT_Generel')
    #mc.menuItem('fixParticleFilePath', l=u'修改particle节点路径...', ann=u'修改particle节点路径...', c='OCT_generel.fixParticleFilePath()', parent='OCT_Generel')
    mc.menuItem('CopyCacheFilePath', l=u'拷贝缓存并设置路径...', ann=u'拷贝缓存并设置路径...', c='OCT_generel.CopyCacheFilePath()', parent='OCT_Generel')
    mc.menuItem('deleteUnknown', l=u'删除unknown节点...', ann=u'删除unknown节点...', c='OCT_generel.deleteUnknown()', parent='OCT_Generel')

    mc.menuItem('CopyYeti', l=u'拷贝yeti缓存和贴图到工程目录下...', ann=u'拷贝yeti缓存和贴图到工程目录下...', c='OCT_generel.CopyYeti()', parent='OCT_Generel')
    
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem("FTM", l=u"贴图管理工具(快)...", ann=u'贴图管理工具(0)...', c= 'mm.eval("FileTextureManager 0;")', parent="OCT_Generel")
    mc.menuItem("FTM_Manager", l=u"贴图管理工具(慢)...", ann=u'贴图管理工具(1)...', c='mm.eval("FileTextureManager 1;")', parent="OCT_Generel")

    mc.menuItem("uniformPathnames", l=u"自动统一贴图路径名", ann=u'自动统一贴图路径名', c='mm.eval("UniformPathnames;")', parent="OCT_Generel")
    mc.menuItem("FindTextturByPath", l=u"在指定的路径下寻找贴图...", ann=u'在制定的路径下寻找贴图', c='mm.eval("tjh_lost_textures_finder;")', parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    # mc.menuItem('instanceTransform', l=u'镜像复制并位移到后选物体', c='OCT_generel.copyAndMatchTransformWithSecond()', parent='OCT_Generel')
    mc.menuItem('NewplayBlast', l=u'新版PlayBlast工具...', ann=u'新版PlayBlast工具', c="OCT_generel.NewPlayBlsst_zwz()", parent="OCT_Generel")
    mc.menuItem('playBlast', l=u'PlayBlast工具...', ann=u'PlayBlast工具', c="OCT_generel.playBlast()", parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('Associate_attribute', l=u'模糊选择与属性关联Locator...', ann=u'模糊选择与属性关联Locator', c="OCT_generel.OCT_Associate_attribute_zwz.OCT_Associate_attribute_zwz_UI()", parent="OCT_Generel")
    mc.menuItem('Edges_Constrain', l=u'用两条边创建locator，并受其约束', ann=u'用两条边创建locator，并受其约束', c="mm.eval('tazz_EdgeConstrain;')", parent="OCT_Generel")
    mc.menuItem('BottomPivot_tazz', l=u'轴心点置底', ann=u'轴心点置底', c="mm.eval('tazz_BottomPivot;')", parent="OCT_Generel")
    mc.menuItem('Average_Vertex_PositionM', l=u'获取所选物体的中心点', ann=u'获取所选物体的中心点', c="mm.eval('Average_Vertex_Position;')", parent="OCT_Generel")
    mc.menuItem('OpenCloseRenderThumbnailUpdate', l=u'打开与关闭材质更新', ann=u'打开与关闭材质更新', c="OCT_generel.OpenCloseRenderThumbnailUpdate()", parent="OCT_Generel")
    mc.menuItem('combineBasedShaderEngens', l=u'合并工具', ann=u'合并工具', c='mm.eval("combineBasedShaderEngen;")', parent="OCT_Generel")
    mc.menuItem("changeRference", label=u"批量更换参考...", ann=u'批量更换参考...', c="OCT_generel.references()", parent="OCT_Generel")
    mc.menuItem("deleteMentalray", label=u"删除mentalrayGlobals...", ann=u'删除mentalrayGlobals...', c="OCT_menu.OCT_deleteMentalray()", parent="OCT_Generel")
    mc.menuItem("shaveGlobals", label=u"删除shaveGlobals...", ann=u'删除shaveGlobals...', c="OCT_menu.OCT_deleteShave()", parent="OCT_Generel")
    mc.menuItem("MentalrayShave", label=u"删除mentalrayGlobalsAndshaveGlobals...", ann=u'删除mentalrayGlobalsAndshaveGlobals...', c="OCT_menu.OCT_deleteMentalrayShave()", parent="OCT_Generel")
    mc.menuItem("delNurbsCurve", label=u"删除场景中的nurbsCurve...", ann=u'删除场景中的nurbsCurve...', c="OCT_generel.delNurbsCurve()", parent="OCT_Generel")
    mc.menuItem("UnDeferStandinLoad", label=u"arnold代理渲染去点DeferStandinLoad", ann=u'arnold代理渲染去点DeferStandinLoad...', c="OCT_generel.UnDeferStandinLoad()", parent="OCT_Generel")
    mc.menuItem('SetRenderDeepPath', l=u'测试拷贝文件...', ann=u'测试拷贝文件...', c='OCT_generel.SetRenderDeepPath()', parent='OCT_Generel')
   
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Mod", label=u'模型工具', ann=u'模型工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('TransferShaders', l=u'传递UV和材质...', ann=u'传递UV和材质...', c='mm.eval("tazz_TransferShaders")', parent='OCT_Mod')
    mc.menuItem('iso', label=u'根据UV选择Nurbs的线...', ann=u'根据UV选择Nurbs的线...', c='mm.eval("IC_calIso;")', parent='OCT_Mod')
    mc.menuItem('DelUvSets', label=u'删除多余的UV Sets', ann=u'删除多余的UV Sets', c='OCT_mod.OCT_DelUnuseUvSets_zxy.DelUnuseUvSets_zxy()', parent='OCT_Mod')
    mc.menuItem('UVRandomlyPlaced', label=u'UV随机排布...', ann=u'UV随机排布', c='mm.eval("RandomUVToolbox")', parent='OCT_Mod')
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('rockGen', label=u'石头创建工具...', ann=u'石头创建工具...', c='mm.eval("HXRockGenChinese;")', parent='OCT_Mod')
    mc.menuItem('createbuilding', label=u'大楼创造器...', ann=u'大楼创造器...', c='mm.eval("EdW_KludgeCity;")', parent='OCT_Mod')
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('ExShaderTools', l=u'替换材质工具...', ann=u'替换材质工具...', c='OCT_lgt.OCT_exShader()', parent='OCT_Mod')
    mc.menuItem('cleanMatTools', l=u'清理材质工具...', ann=u'清理材质工具...', c='OCT_lgt.cleanMatUI()', parent='OCT_Mod')
    mc.menuItem('repairTex_YJL', l=u'修复贴图...', ann=u'修复贴图...', c='OCT_mod.repairTex_YJL.repWin()', parent='OCT_Mod')
    mc.menuItem('smoothTools', l=u'圆滑工具...', ann=u'圆滑工具...', c='mm.eval("tazz_SmoothTool")', parent='OCT_Mod')
    mc.menuItem('PlaceOnMesh', label=u'把物体种植面上', ann=u'把物体种植面上', c='OCT_mod.placeOnMesh()', parent='OCT_Mod')
    mc.menuItem('Replacemodel', label=u'替换模型工具...', ann=u'替换模型工具', c='OCT_mod.runWhiteBoxTool()', parent='OCT_Mod')
    mc.menuItem('spPaint3', label=u'新版三维种植工具...', ann=u'新版三维种植工具', c='OCT_mod.runSpPaint3d()', parent='OCT_Mod')
    mc.menuItem('Paint3', label=u'笔刷种树工具...', ann=u'笔刷种树工具', c='OCT_mod.rPaint3d()', parent='OCT_Mod')
    #mc.menuItem('ScatterObj', label=u'新版种树工具...', ann=u'新版种树工具', c='mm.eval("createScatterObjWin;")', parent='OCT_Mod')
    # mc.menuItem('paintGeometry', label='Paint Geometry...', ann=u'把物体画在面上...', c='OCT_mod.paintGeo()', parent='Mod')
    mc.menuItem('assignShader_zwz', label=u'随机赋予指定物体指定的材质...', ann=u'随机赋予指定物体指定的材质', c='OCT_mod.OCT_AssignRandShader_zwz.OCT_AssignRandShader_UI_zwz()', parent='OCT_Mod')
    mc.menuItem('dupToCurveFlow', label=u'把物体沿曲线铺放', ann=u'把物体沿曲线铺放', c='OCT_mod.dupToCurveFlow()', parent='OCT_Mod')
    mc.menuItem('ProjectNurbsonPoly_zzj', label=u'映射nurbs到poly上...', ann=u'映射nurbs到poly上', c='mm.eval("tazz_ProjNurbs2Poly;")', parent='OCT_Mod')
    mc.menuItem('Duplicate_FPolyace', label=u'复制多个poly的面', ann=u'复制多个poly的面', c='mm.eval("tazz_MultDupFace;")', parent='OCT_Mod')
    mc.menuItem('FKSDY_SetBot', label=u'去掉File节点的Bots勾选项', ann=u'去掉File节点的Bots勾选项', c='OCT_mod.OCT_FKSDYDelBot_zwz.OCT_FKSDYDelBot_zwz()', parent='OCT_Mod')
    mc.menuItem('clearlightLinkerConnections_mod', label=u'清理灯光连接', ann=u'清理灯光连接', to=True, c='mm.eval("clearlightLinkerConnections_zqs;")', parent="OCT_Mod")
    mc.menuItem('SetUV', label=u'随机设置UV', ann=u'随机设置UV', c='OCT_mod.randomUVSet_YH()', parent='OCT_Mod')
    mc.menuItem('checkingPolyUV_tools', label=u'UV处理', ann=u'UV处理', to=True, c='mm.eval("checkingPolyUV_zqs;")', parent="OCT_Mod")
    mc.menuItem('TextureMaterialTool', label=u'arnold透明贴图材质工具', ann=u'arnold透明贴图材质工具', c='OCT_mod.TextureMaterialTool()', parent='OCT_Mod')
    mc.menuItem('selectUVEdge', label=u'选择UV边界线工具', ann=u'选择UV边界线工具', c='OCT_mod.selectUVEdge()', parent='OCT_Mod')
    mc.menuItem('displacementShader', label=u'断开与连接材质贴图', ann=u'断开与连接材质贴图', c='OCT_mod.displacementShader()', parent='OCT_Mod') 
    mc.menuItem('lbTrUIv01', label=u'随机位移、旋转、缩放工具', ann=u'随机位移、旋转、缩放工具', to=True, c='mm.eval("lbTrUIv01;")', parent="OCT_Mod")
    mc.menuItem("ArnoldBox", label=u"arnold代理显示Box", ann=u'arnold代理显示Box...', c="OCT_mod.ArnoldBox()", parent="OCT_Mod")

    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Rigging", label=u'设置工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('JointConversion', l=u'骨骼转换...', ann=u'骨骼转换', c="OCT_rigging.JointConversion()", parent="OCT_Rigging")
    mc.menuItem('modifyJointname', l=u'根据动捕命令规则修改骨骼名...', ann=u'根据动捕命令规则修改骨骼名', c="OCT_rigging.modifyJointname()", parent="OCT_Rigging")
    mc.menuItem('FK_loc', l=u'手脚FK_loc创建...', ann=u'手脚FK_loc创建', c='mm.eval("FK_loc;")', parent="OCT_Rigging")

    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Camera", label=u'摄像机工具', ann=u'摄像机工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('shakeCamera_zqs', label=u'抖动摄像机...', ann=u'抖动摄像机', c='mm.eval("camShake")', parent='OCT_Camera')
    mc.menuItem('cameraZoom_zzj', label=u'摄像机缩放...', ann=u'摄像机缩放', c='mm.eval("zoomerate")', parent='OCT_Camera')
    mc.menuItem('stereoCamera', label=u'创建环幕摄像机', ann=u'创建环幕摄像机', c='OCT_cam.zwz_CreateStereoCamera.zwz_CreateStereoCamera_menu()', parent='OCT_Camera')
    mc.menuItem('camerasCurves', label=u'创建摄像机视域范围框', ann=u'创建摄像机视域范围框', c='OCT_cam.OCT_CmeraCurves_zwz.OCT_CmeraCurves_zwz()', parent='OCT_Camera')
    mc.menuItem('MCameraPlane', label=u'多摄像机视域面', ann=u'多摄像机视域面', subMenu=True, to=True, parent='OCT_Camera')
    mc.menuItem('Scalecameras', label=u'调整预览窗口大小...', ann=u'调整预览窗口大小...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_Window_Scale()', parent='MCameraPlane')
    mc.menuItem('onecameras', label=u'1 View...', ann=u'1_水平视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_1_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('threeHcameras', label=u'3_H_View...', ann=u'3_水平视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_3_H_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('threeameras', label=u'环幕摄像机(自定义)...', ann=u'环幕摄像机(自定义)...', c='OCT_cam.Cam_3_H_Model()', parent='MCameraPlane')
    # mc.menuItem('threeH_cameras_Tdhj', label=u'3_H View for TDHJ Or MODOU...', ann=u'3_水平视图_天地浩劫...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_3_Model_Win_menu_BJCP()', parent='MCameraPlane')
    mc.menuItem('threeH_cameras_MODOU', label=u'3_H View for TDHJ Or MODOU...', ann=u'3_水平视图_魔豆...', c='OCT_cam.newCamerasTools("MODOU")', parent='MCameraPlane')
    mc.menuItem('two_cameras_SDGT', label=u'2_H View for SDGT...', ann=u'2_水平视图_圣地古塔...', c='OCT_cam.newCamerasTools("SDGT_Two")', parent='MCameraPlane')

    mc.menuItem('threeVcameras', label=u'3 V View...', ann=u'3_垂直视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_3_V_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('foureH_T_cameras', label=u'4_H_T View...', ann=u'4_水平视图_跳楼...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_4_H_T_Model_Win_menu()', parent='MCameraPlane')
    #mc.menuItem('sixcamerasAni_fkbs', label=u'4 View for FKBS(Ball)...', ann=u'6_视图...', c='OCT_cam.newCamerasTools("MODOU BALL")', parent='MCameraPlane')
    mc.menuItem('FKBS_Third', label=u'New 4 View for FKBS(Ball)...', ann=u'3_视图...', c='OCT_cam.newCamerasTools("FKBS_Four")', parent='MCameraPlane')
    mc.menuItem('fivecamerasAni', label=u'5 View...', ann=u'5_视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_5_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('fivecameras180degrees', label=u'5 View 180度球幕', ann = u'5_视图180度球幕', c = 'OCT_cam.OCT_MCameraModel_zwz.Cam_5_180degrees_Model_Win_menu()', parent='MCameraPlane')
    #mc.menuItem('servecamerasAni_fkbs', label=u'7 View for FKBS(Around)...', ann=u'7_视图...', c='OCT_cam.newCamerasTools("MODOU AROUND")', parent='MCameraPlane')
    mc.menuItem('FKBS_Six', label=u'6 View for FKBS...', ann=u'6_视图...', c='OCT_cam.newCamerasTools("FKBS_Six")', parent='MCameraPlane')

    mc.menuItem('ninecamerasAni', label=u'9 View...', ann=u'9_视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_9_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('tencamerasAni', label=u'10 View...', ann=u'10_视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_10_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('twelveCamerasAni', label=u'12_H_T View...', ann=u'12_水平跳楼视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_12_H_T_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('eighteencamerasAni', label=u'18 View...', ann=u'18_视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_18_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('SH_Six', label=u'12 View for SH...', ann=u'12_视图...', c='OCT_cam.newCamerasTools("SH_Six")', parent='MCameraPlane')
    
    mc.menuItem('toggleModelOpen', label=u'打开菜单...', ann=u'打开菜单...', c='OCT_cam.newCamerasTools("Open")', parent='MCameraPlane')
    mc.menuItem('toggleModelClose', label=u'关闭菜单...', ann=u'关闭菜单...', c='OCT_cam.newCamerasTools("Close")', parent='MCameraPlane')


    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Animation", label=u'动画工具', ann=u'动画工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('poseMan', label=u'姿态快照...', ann=u'姿态快照...', c='mm.eval("poseMan;")', parent='OCT_Animation')
    mc.menuItem('CreatrGeoCache', label=u'批量创建点缓存...', ann=u'批量创建点缓存...', c='OCT_anim.OCT_CreateGeometryCache_zwz.OCT_CreateGeometryCache_Menum_zwz()', parent='OCT_Animation')
    mc.menuItem('cachefilesTools', label=u'缓存管理工具...', ann=u'缓存管理工具...', c='OCT_anim.run_CacheFile_Tools_zwz()', parent='OCT_Animation')
    mc.menuItem('Bake_Ani_with_cache', label=u'拷贝带缓存的动画并错开帧数', ann=u'拷贝带缓存的动画并错开帧数...', c='mm.eval("Bake_Animate_With_cache_YH;")', parent='OCT_Animation')
    #mc.menuItem('Bake_Camera', label=u'Bake一个摄像机', ann=u'Bake一个摄像机...', c='mm.eval("ZW_BakeCamera();")', parent='OCT_Animation')
    mc.menuItem('Bake_Camera_all', label=u'Bake选择的摄像机', ann=u'Bake选择的摄像机...', c='OCT_anim.OCT_BakeCamera()', parent='OCT_Animation')
    #mc.menuItem('camerasAni', label=u'轨道路径相对动画导出...', ann=u'轨道路径相对动画导出...', c='OCT_anim.OCT_exp_loc_zxy.exp_loc_ui()', parent='OCT_Animation')
    mc.menuItem('tazz_rollrocks', label=u'滚石动画', ann=u'滚石动画', c='mm.eval("tazz_rollrocks;")', parent='OCT_Animation')
    mc.menuItem('ReferenceToInstance', label=u'参考转成替换', ann=u'参考转成替换', c='mm.eval("ReferenceToInstance_YH;")', parent='OCT_Animation')
    mc.menuItem('Face_Tools_YH', label=u'面部表情工具', ann=u'面部表情工具', c='OCT_anim.FaceTools()', parent='OCT_Animation')
    mc.menuItem('copyReferenceTool', label=u'拷贝参考物体到本机和修改参考的路径', ann=u'拷贝参考物体到本机和修改参考的路径', c='OCT_anim.copyReference()', parent='OCT_Animation')
    mc.menuItem('createAnimCurve', label=u'根据动画路径创建曲线', ann=u'根据动画路径创建曲线', c='OCT_anim.createAnimCurve()', parent='OCT_Animation')
    mc.menuItem('clearlightLinkerConnections_an', label=u'清理灯光连接', ann=u'清理灯光连接', to=True, c='mm.eval("clearlightLinkerConnections_zqs;")', parent="OCT_Animation")
    mc.menuItem('delMaterialAndFace', label=u'删除材质改lambert', ann=u'删除材质改lambert', to=True, c='OCT_anim.OCT_delMaterialAndFace()', parent="OCT_Animation")
    mc.menuItem('deleteKeyFrames', label=u'删除关键帧', ann=u'删除关键帧', to=True, c='OCT_anim.OCT_deleteKeyFrames()', parent="OCT_Animation")
    mc.menuItem('deleteunUserCacheNode', label=u'删除无用的缓存节点', ann=u'删除无用的缓存节点', to=True, c='mm.eval("delect_UnuseredCache;")', parent="OCT_Animation")
    #mc.menuItem('motionCapture', label=u'动捕工具', ann=u'动捕工具', to=True, c='OCT_anim.OCT_MotionCapture.motionCapture()', parent="OCT_Animation")
    mc.menuItem('miarmyGroup', label=u'群集物体打组', ann=u'群集物体打组', to=True, c='OCT_anim.miarmyGroup()', parent="OCT_Animation")
    mc.menuItem('miaryAnimCopy', label=u'群集物体替换拷贝动画', ann=u'群集物体替换拷贝动画', to=True, c='OCT_anim.miaryAnimCopy()', parent="OCT_Animation")
    mc.menuItem('fix_animation', label=u'修复动画丢失', ann=u'修复动画丢失', to=True, c='OCT_anim.OCT_fix_animation_LXJ.fix_animation()', parent="OCT_Animation")
    mc.menuItem('wind_noises', label=u'风吹动物体的工具', ann=u'风吹动物体的工具', c='mm.eval("wind_noises;")', parent='OCT_Animation')
    mc.menuItem('IKFK', label=u'IKFK无缝切换', ann=u'IKFK无缝切换', c='mm.eval("IKFK;")', parent='OCT_Animation')

    mc.menuItem('ImportExportAnim', label=u'导入导出动画', ann=u'导入导出动画', subMenu=True, to=True, parent='OCT_Animation')
    mc.menuItem('ExportAnimData', label=u'导出动画数据', ann=u'导出动画数据', to=True, c='OCT_anim.exportAnimData()', parent="ImportExportAnim")
    mc.menuItem('ImportAnimData', label=u'导入动画数据', ann=u'导入动画数据', to=True, c='OCT_anim.importAnimData()', parent="ImportExportAnim")

    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('CreateAnimationForUnity', label=u'导入数据生成动画(unity中导出的数据)', ann=u'导入数据生成动画', to=True, c='OCT_anim.CreateAnimationForUnity()', parent="OCT_Animation")
    

    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_VFX", label=u'特效工具', ann=u'特效工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('UVtoPos', label=u'查询物体某UV点世界坐标位置...', ann=u'查询物体某UV点世界坐标位置...', c='OCT_vfx.uvToPosUI()', parent='OCT_VFX')
    mc.menuItem('ExportVrayMesh_zwz1', label=u'从代理文件导出VrayMesh成FBX', ann=u'导出VrayMesh成FBX...', c='OCT_vfx.ExportVrayMeshToFbx(1)', parent='OCT_VFX')
    mc.menuItem('ExportVrayMesh_zwz2', label=u'从Mesh物体导出VrayMesh成FBX', ann=u'导出VrayMesh成FBX...', c='OCT_vfx.ExportVrayMeshToFbx(2)', parent='OCT_VFX')
    mc.menuItem('deleteNoSelMesh', label=u'选择物体并导出', ann=u'选择物体并导出...', c='OCT_vfx.deleteNoSelMesh()', parent='OCT_VFX')
    mc.menuItem('CopyObjAttrbuteToLocator', label=u'拷贝houdini引擎对象属性给locater', ann=u'拷贝houdini引擎对象属性给locater...', c='OCT_vfx.CopyObjAttrbuteToLocator()', parent='OCT_VFX')
    mc.menuItem('maya_came', label=u'CameraToMaxVrayCamera', ann=u'CameraToMaxVrayCamera...', c='OCT_vfx.OCT_maya_cam()', parent='OCT_VFX')
    mc.menuItem('ModifyMaterial', label=u'转换成选面给材质并改名', ann=u'转换成选面给材质并改名...', c='OCT_vfx.ModifyMaterial()', parent='OCT_VFX')
    mc.menuItem('ExportImportSGNodes', label=u'特效破碎物体上材质的几种方式', ann=u'特效破碎物体上材质的几种方式...', c='OCT_vfx.ExportImportSGNodes()', parent='OCT_VFX')

    mc.menuItem('ReadMaterialInfo', label=u'记录材质信息到txt文档', ann=u'记录材质信息到txt文档...', c='OCT_vfx.ReadMaterialInfo()', parent='OCT_VFX')
    mc.menuItem('WriteMaterialInfo', label=u'读取记录的材质信息将材质自动连接物体', ann=u'读取记录的材质信息将材质自动连接物体...', c='OCT_vfx.WriteMaterialInfo()', parent='OCT_VFX')
    mc.menuItem('deleteNotOpacityMaterial', label=u'删除不带透明通道的材质', ann=u'删除不带透明通道的材质...', c='OCT_vfx.deleteNotOpacityMaterial()', parent='OCT_VFX')
    mc.menuItem('findObjectSmoothness', label=u'判断所选物体是否按3', ann=u'判断所选物体是否按3...', c='OCT_vfx.findObjectSmoothness()', parent='OCT_VFX')


    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Light", label=u'灯光工具', ann=u'灯光工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('submitMayaJob_zwz_W', l=u'交接给特效环节工程M:\ALL\\transfer...', ann=u'交接给特效环节工程M:\ALL\\transfer...', c='OCT_generel.submitMayaToDeadline_zwz(6)', parent='OCT_Light')
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("renameReferenceFile_YH", label=u'把低摸的参考物体的转换成高模', ann=u'把低摸的参考物体的转换成高模', c='OCT_lgt.ChangeHReference_YH()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("ChangeShaderA_YH", label=u'统一改变默认或者Vray或者arnold标准材质球属性...', ann=u'统一改变默认或者Vray或者arnold标准材质球属性', c='OCT_lgt.ChangeShader_YH()', parent="OCT_Light")
    mc.menuItem("ChangeAttr_YH", label=u'改变所选灯光的属性', ann=u'改变所选灯光的属性', c='OCT_lgt.ChangeAttr_YH()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem('delLink', label=u'删除多余的灯光链接节点', ann=u'删除多余的灯光链接节点', c='mm.eval("IC_LightLinksCleanUp")', parent='OCT_Light')
   # mc.menuItem('exShaderTools', l=u'Replace the material tool...', c='OCT_lgt.OCT_exShader()', parent='OCT_Light')
   # mc.menuItem('cleanMatTools', l=u'Clean up the material tool...', c='OCT_lgt.cleanMatUI()', parent='OCT_Light')
    mc.menuItem('eyePointLight', l=u'眼神光', c='OCT_lgt.HYZX_eyeLight()', ann=u'眼神光', parent='OCT_Light')
    mc.menuItem('makemyVolumnLight', l=u'创建假冒的体积光', ann=u'创建假冒的体积光', c='mm.eval("tazz_CreatePointToVolumnLight();")', parent='OCT_Light')
    mc.menuItem("arnoldProxy", label=u'检查Arnold代理并拷贝', ann=u'检查Arnold代理并拷贝', c='OCT_lgt.CheckArnoldProxy_YH(1)', parent="OCT_Light")
    mc.menuItem("arnoldProxyNew", label=u'新检查Arnold代理并拷贝', ann=u'新检查Arnold代理并拷贝', c='OCT_lgt.CheckArnoldProxy_YH(2)', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
  #mc.menuItem("changeMaterial", label=u'转换材质', ann=u'转换材质', c='OCT_lgt.ChangeMaterial_YH()', parent="OCT_Light")
    mc.menuItem("ArnoldProduction", label=u'统一改变Arnold模型属性', ann=u'统一改变Arnold模型属性', c='OCT_lgt.ArnoldProduction_YH()', parent="OCT_Light")
    mc.menuItem("convertTexFormat", label=u'转换贴图格式', ann=u'转换贴图格式', c='OCT_lgt.ConvertTexFormat_YH()', parent="OCT_Light")
    mc.menuItem("VrayArnoldProxyChange", label=u'Vray与Arnold代理转换', ann=u'Vray与Arnold代理转换', c='OCT_lgt.VrayArnoldProxyChange()', parent="OCT_Light")
    mc.menuItem("changenNetworkPaths", label=u'改变网路路径与拷贝贴图', ann=u'改变网路路径与拷贝贴图', c='OCT_lgt.changenNetworkPaths()', parent="OCT_Light")
    mc.menuItem("changeShaveName", label=u'改变shave节点名', ann=u'改变shave节点名', c='OCT_lgt.changeShaveName()', parent="OCT_Light")
    mc.menuItem("FindVrayProxyes", label=u'查找VrayMesh的代表物体', ann=u'查找VrayMesh的代表物体', c='OCT_lgt.FindVrayProxys()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    #mc.menuItem("changeFrameRate", label=u'48帧装换24帧率...', ann=u'48帧装换24帧率...', c='OCT_lgt.changeFrameRate()', parent="OCT_Light")
    mc.menuItem("updateShaver", label=u'统一改变shave属性', ann=u'统一改变shave属性', c='OCT_lgt.updateShaver()', parent="OCT_Light")
    mc.menuItem("tazz_intensity", label=u'灯光闪烁工具', ann=u'灯光闪烁工具', c='mm.eval("tazz_intensity();")', parent="OCT_Light")
    mc.menuItem("sur_Occ_Layers", label=u'MR的OCC拆层工具', ann=u'MR的OCC拆层工具', c='OCT_lgt.sur_Occ_Layers()', parent="OCT_Light")
    mc.menuItem("Ar_Occ_Layers", label=u'AR的OCC拆层工具', ann=u'AR的OCC拆层工具', c='OCT_lgt.Ar_Occ_Layers()', parent="OCT_Light")
    mc.menuItem("selectTransparency", label=u"选择带透明贴图的物体...", ann=u'选择带透明贴图的物体...', c="OCT_lgt.OCT_SelectTransparency.selectTransparency()", parent="OCT_Light")
    mc.menuItem("giveNewMaterial", label=u"lambert的拆层(带透明贴图)...", ann=u'lambert的拆层(带透明贴图)...', c="OCT_lgt.giveNewMaterial()", parent="OCT_Light")
    mc.menuItem("aiPhotomeLightFile_Tools", label=u'灯光aiPhotomeLight贴图管理工具', ann=u'灯光aiPhotomeLight贴图管理工具', c='OCT_lgt.run_PhotometricLightMap_Tools()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("SelectSpotLight", label=u'选择聚光灯', ann=u'选择聚光灯', c='OCT_lgt.SelectSpotLight()', parent="OCT_Light")
    mc.menuItem("SelectAreaLight", label=u'选择面灯', ann=u'选择面灯', c='OCT_lgt.SelectAreaLight()', parent="OCT_Light")

    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Render", label=u'渲染工具', ann=u'渲染工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('LayerTools', label=u'分层工具...', ann=u'分层工具...', to=True, c='OCT_render.OpenRenderLayerTools()', parent="OCT_Render")
    mc.menuItem("resizeImage", l=u"修改图片大小...", ann=u'修改图片大小', c='OCT_render.run_zxy_resizeImage()', parent="OCT_Render")
    mc.menuItem('VFXRender', label=u'拍屏渲染工具...', ann=u'拍屏渲染工具...', c='mm.eval("DY_RenderToolsUI_zwz;")', parent='OCT_Render')
    mc.menuItem('newRender', label=u'新版拍屏渲染工具...', ann=u'拍屏渲染工具...', c='OCT_render.newPreRender_YH()', parent='OCT_Render')
    mc.menuItem("QuantituRender_zwz", label=u"批量文件拍屏工具...", ann=u'批量文件拍屏工具...', c="OCT_render.OCT_QuantityRender_zwz.OCT_QuantituRender_UI_zwz()", parent="OCT_Render")
    mc.menuItem("FixFrame_zwz", label=u"单文件多任务补帧工具...", ann=u'单文件多任务补帧工具...', c="OCT_render.OCT_SuperFixFram_zwz.SuperFixFream_mmenu_zwz()", parent="OCT_Render")
    mc.menuItem("deleteSGNode", label=u"删除所有的SG节点...", ann=u'删除所有的SG节点...', c="OCT_render.deleteSGNode_YH()", parent="OCT_Render")
    mc.menuItem("cameraConnetPlace3d", label=u"手动拆层ZD...(选择相机)", ann=u'手动拆层ZD...(选择相机)', c="OCT_render.cameraConnetPlace3d()", parent="OCT_Render")
    mc.menuItem("cameraConnetPlace3darnold", label=u"arnold类型手动拆层ZD...(选择相机)", ann=u'arnold类型手动拆层ZD...(选择相机)', c="OCT_render.cameraConnetPlace3darnold()", parent="OCT_Render")
    mc.menuItem("cameraConnetPlace3dIMP", label=u"手动拆层IMP...(选择物体)", ann=u'手动拆层IMP...(选择物体)', c="OCT_render.cameraConnetPlace3dImp()", parent="OCT_Render")
    mc.menuItem("changeShaderIMP", label=u"imp连接各种材质", ann=u'imp连接各种材质', c="OCT_render.changeShaderIMP()", parent="OCT_Render")
    mc.menuItem("OCT_materialChange", label=u"材质转换...", ann=u'材质转换...', c="OCT_render.OCT_materialChanges()", parent="OCT_Render")
    mc.menuItem("batchRender_Tool", label=u"单机批渲染...", ann=u'单机批渲染...', c="OCT_render.batchRender_Tools()", parent="OCT_Render")
    #mc.menuItem("OCT_RenderDeepSets", label=u"设置deepRender...", ann=u'设置deepRender...', c="OCT_render.OCT_RenderDeepSets()", parent="OCT_Render")

    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Optimiza", label=u'检查工具', ann=u'检查工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('del name space', label=u'1.删除命名空间(不包括referece)', ann=u'1.删除命名空间(不包括referece)', to=True, c='mm.eval("oct_delNameSpace;")', parent="OCT_Optimiza")
    mc.menuItem('reMap_tools', label=u'2.解决重名问题', ann=u'2.解决重名问题', to=True, c='mm.eval("renameTransForm_muilty_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('reLongName_Tool', label=u'3.解决名字过长问题 ', ann=u'3.解决名字过长问题', to=True, c='mm.eval("OCT_reLongName;")', parent="OCT_Optimiza")

    mc.menuItem('deleteMidMesh_tools', label=u'合法贴图名', ann=u'合法贴图名', to=True, c='mm.eval("reMap_name_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('checkYxSize_tools', label=u'检查贴图尺寸', ann=u'检查贴图尺寸', to=True, c='OCT_check.CheckTXSize()', parent="OCT_Optimiza")
    mc.menuItem('renameTransForm_tools', label=u'清理垃圾midMesh ', ann=u'清理垃圾midMesh', to=True, c='mm.eval("deleteMidMeshSafe_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('clearNoVertex_tools', label=u'清除无点polygon ', ann=u'清除无点polygon', to=True, c='mm.eval("clearNoVertex_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('clearLJ_tools', label=u'清理各种垃圾 ', ann=u'清理各种垃圾', to=True, c='mm.eval("clearLJ_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('checkingNoAnyMat_tools', label=u'检查没有赋任何材质shader的物体', ann=u'检查没有赋任何材质shader的物体', to=True, c='mm.eval("checkingNoAnyMat_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('clearInitialmat_tools', label=u'清除默认材质球', ann=u'清除默认材质球', to=True, c='mm.eval("clearInitialmat_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('checkingSmallArea_tools', label=u'检查极小面体积的物体', ann=u'检查极小面体积的物体', to=True, c='mm.eval("checkingSmallArea_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('setArnoldDsoPath_tools', label=u'修正Arnold代理路径', ann=u'修正Arnold代理路径', to=True, c='mm.eval("setArnoldDsoPath_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('OCT_Set', label=u'OCT_Set', ann=u'OCT_Set', to=True, c='mm.eval("OCT_Set;")', parent="OCT_Optimiza")
    mc.menuItem('checkReference', label=u'检查Reference', ann=u'检查Reference', subMenu=True, to=True, parent='OCT_Optimiza')
    mc.menuItem('checkUnUserReferences', label=u'检查UnUserReference', ann=u'检查UnUserReference...', c='OCT_check.checkUnusedRefence(1)', parent='checkReference')
    mc.menuItem('deleteUnUserReferences', label=u'删除UnUserReference', ann=u'删除UnUserReference...', c='OCT_check.checkUnusedRefence(2)', parent='checkReference')

    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_proxys", label=u'代理工具', ann=u'代理工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('UploadProxy', label=u'上传代理工具', ann=u'上传代理工具', c='OCT_proxy.uploadProxy()', parent="OCT_proxys")
    mc.menuItem('download', label=u'代理工具', ann=u'代理工具', c='OCT_proxy.download()', parent="OCT_proxys")
    mc.menuItem('changeProxys', label=u'根据代理库路径的代理转换', ann=u'根据代理库路径的代理转换', c='OCT_proxy.newProxyChange()', parent="OCT_proxys")
    mc.menuItem('SameNameProxyChange', label=u'相同代理名互换', ann=u'相同代理名互换', c='OCT_proxy.SameNameProxyChange()', parent="OCT_proxys")
    mc.menuItem('VRayProxyChangeModel', label=u'VRay代理转Model', ann=u'VRay代理转Model', c='OCT_proxy.VRayProxyChangeModel()', parent="OCT_proxys")
    mc.menuItem('VRayProxyChangeArnoldProxy', label=u'VRay代理转Arnold代理', ann=u'VRay代理转Arnold代理', c='OCT_proxy.proxyChanges()', parent="OCT_proxys")
    
    # mc.menuItem(d=1, parent="OCT_ToolSetMN")
    # mc.menuItem("OCT_animImEx", label=u'导动画数据工具', ann=u'导动画数据工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    # mc.menuItem('OCT_animExport', label=u'导出动画数据', ann=u'导出动画数据', c='OCT_animImEx.animExport()', parent="OCT_animImEx")
    # mc.menuItem('OCT_animImport', label=u'导入动画数据', ann=u'导入动画数据', c='OCT_animImEx.animImport()', parent="OCT_animImEx")

    mc.menuItem(d=1, parent='OCT_ToolSetMN')
    mc.menuItem('about', label=u'Help', ann=u'关于', subMenu=True, to=False, parent='OCT_ToolSetMN')
    mc.menuItem('HelpDoc', label='OCT Vision Help', ann=u'脚本帮助文档', c='OCT_about.helpDoc()', parent='about')
    mc.menuItem('Doc2012SDK', label=u'Help for MAYA2012 SDK...', ann=u'', c='OCT_about.Maya2012SDK()', parent='about')
    mc.menuItem('Binary_Alchemy_Help', label=u'Arnold_Binary_Alchemy_Help...', ann=u'', c='OCT_about.Arnold_Binary_Alchemy_Help()', parent='about')
    mc.menuItem('aboutThis', label=u'About TD', c='OCT_about.aboutThis()', parent='about')

    mc.menuItem(d=1, parent='OCT_ToolSetMN')
    # mc.menuItem('subJob', label=u'提交Deadline渲染', c='OCT_generel.OCT_deadline_submit_zwz.show()', parent='OCT_ToolSetMN')

    #加载各项目shelfTab工具架内容
    mc.evalDeferred('OCT_menu.searchTab()')
    #加载cinema4d R14文件发送插件
    # try:
    #     mm.eval("BodypaintExchangeLoadPlugin")
    # except:
    #     pass
#     mc.menuItem(d=1,parent='OCT_ToolSetMN')
#     mc.menuItem('setRenderOpt', label=u'渲染设置', c='OCT_menu.setProjRenderOpt_UI()', parent='OCT_ToolSetMN')
    OCT_UpdateReferenceRemind()
    
    mc.scriptJob(event=("PostSceneRead",OCT_UpdateReferenceRemind))

def installTab(projectName):
    mm.eval("addNewShelfTab(\"%s\")" % projectName)


def addShelfButton(projects):
    for each in projects:
        shelfButtons = mc.shelfLayout(each, q=1, ca=1)
        if shelfButtons:
            for b in shelfButtons:
                mm.eval("deleteUI -control \""+b+"\"")
        MyShelf = (maya.mel.eval("global string $gShelfTopLevel;$temp = $gShelfTopLevel") + "|%s" % each)
        if each == 'XXB_Tools':
            if not mc.shelfButton("Xxb_DeUUCameras", ex=True):
                mc.shelfButton("Xxb_DeUUCameras", parent=MyShelf, ann=u'删除不渲染的摄像机', c='OCT_mod.OCT_XXBDeleteUnUseCameras_zwz.OCT_XXBDeleteUnUseCameras_zwz()', image1="DeleteCamera.png")
            if not mc.shelfButton("Xxb_ChangeCameras", ex=True):
                mc.shelfButton("Xxb_ChangeCameras", parent=MyShelf, ann=u'修改摄像机工具', c='OCT_anim.OCT_ChangeXxbOldCameras_zwz.ChangeXxbOldCameras_zwz()', image1="ChangeCamera.png")
        elif each == 'FKNC_Tools':
            # from OCT_Projects import FKNC_Tools
            if not mc.shelfButton("Fknc_Optimize", ex=True):
                mc.shelfButton("Fknc_Optimize", parent=MyShelf, ann=u'优化场景', c='OCT_Projects.FKNC_Tools.FKNC_Optimize_run()', image1=r"\\octvision.com\cg\Tech\maya_sixteen\Python\Themes\FKNC_Tools\icons\FKNC_OpTools.png")
            if not mc.shelfButton("FKNC_SelectRootT", ex=True):
                mc.shelfButton("FKNC_SelectRootT", parent=MyShelf, ann=u'选择', c='OCT_Projects.FKNC_Tools.FKNC_SelectRoot()', image1=r"\\octvision.com\cg\Tech\maya_sixteen\Python\Themes\FKNC_Tools\icons\FKNC_SelectRoot.png")
            if not mc.shelfButton("FKNC_DeleteOp", ex=True):
                mc.shelfButton("FKNC_DeleteOp", parent=MyShelf, ann=u'删除约束和优化场景', c='OCT_Projects.FKNC_Tools.FKNC_DeleteAndOptize()', image1=r"\\octvision.com\cg\Tech\maya_sixteen\Python\Themes\FKNC_Tools\icons\FKNC_DO.png")


def searchTab():
    projects = ["FKNC_Tools"]
    DeleProjects = ["FKSDY_Tools", "XXB_Tools"]
    shelftop = maya.mel.eval("global string $gShelfTopLevel;$temp = $gShelfTopLevel")
    if mc.tabLayout(shelftop, exists=1, q=1):
        shelfTabs = mc.tabLayout(shelftop, q=1, childArray=1)
        for each in projects:
            if not each in shelfTabs:
                if not mc.shelfLayout(each, q=1, ex=True):
                    installTab(each)
        for tmp in DeleProjects:
            if tmp in shelfTabs:
                mm.eval('deleteShelfTab "%s";' % tmp)
                # shelfButtons = mc.shelfLayout('%s' % tmp, q=1, ca=1)
                # if shelfButtons:
                #     for b in shelfButtons:
                #         mm.eval("deleteUI -control \""+b+"\"")
                # mc.deleteUI("%s|%s" % (shelftop, tmp), lay=True)
        addShelfButton(projects)



class  updateReferences():
    def __init__(self):
        self.listSourceFile=[]
        self.listDestFile=[]
    def CommonNewSceneOpened(self):
        #print "mmmmm"
        PROJECT_PATH = r'//octvision.com/CG/Themes'
        PROJECT_PATHZ=r'Z:/Themes'
        allReferences=mc.file(q=True,reference=True)
        if allReferences:
            for renfence in allReferences:
                #print "------****"
                renfences=renfence.split("{")[0]
                sourceFilePath=""
                destFilePath=""
                if 'E:/REF' in renfences:
                    sourceFilePath=renfences.replace('E:/REF',PROJECT_PATH)
                    destFilePath=renfences
                elif PROJECT_PATH in renfences:
                    sourceFilePath=renfences
                    destFilePath=renfences.replace(PROJECT_PATH,'E:/REF')
                elif PROJECT_PATHZ in renfences:
                    sourceFilePath=renfences
                    destFilePath=renfences.replace(PROJECT_PATHZ,'E:/REF')
                else:
                    mc.confirmDialog(message=renfences+u"文件目录不正确!!!",button="OK")
                    return 
                if sourceFilePath!="" and destFilePath!="":
                    if os.path.exists(sourceFilePath) and os.path.exists(destFilePath) and (int(os.path.getmtime(destFilePath)) < int(os.path.getmtime(sourceFilePath))):
                        #destFile=destFilePath+"\\"+scrFilePathSplit[-1]
                        self.listSourceFile.append(sourceFilePath)
                        self.listDestFile.append(destFilePath)
                        #self.listSourceFile.update({renfences:destFile})
                    else:
                        continue
                else:
                    continue
        if self.listSourceFile:
            if mc.window("updateReferenceUI",ex=True):
                mc.deleteUI('updateReferenceUI')
            getFileWindow=mc.window('updateReferenceUI',title=u'更新参考文件',wh=(700,400))
            mc.scrollLayout("A",hst=1,vst=8)
            mc.columnLayout(adjustableColumn=True)
            mc.frameLayout('sourceFile', label=u"下列文件是场景中所用的参考文件，网络上有更新参考文件。请选择你本机上所需更新的参考文件：", borderStyle="etchedIn",enable=True) 
            
            for sou in range(len(self.listSourceFile)):
                key="a"+str(sou)
                mc.checkBox(key,label=self.listSourceFile[sou],h=30)
            mc.setParent("..")
            mc.rowLayout(numberOfColumns=4,columnWidth4=(180,180,180,140),columnAlign4=('center','center','center','center'))
    
            mc.button(l='Select All',w=80,h=30,backgroundColor = (0.7,0.7,0.0),align='center',c=lambda*arge:self.AllSelectReference())
            mc.button(l='Unselect',w=80,h=30,backgroundColor = (0.0,0.7,0.7),align='center',c=lambda*arge:self.UnselectReference())
            mc.button(l='OK',w=80,h=30,backgroundColor = (0.0,0.7,0),align='center',c=lambda*arge:self.updateReference())
            mc.button(l='Close',width=80,h=30,backgroundColor = (0.7,0.0,0),c=('mc.deleteUI(\"'+getFileWindow+'\",window=True)'))
        
            mc.showWindow('updateReferenceUI')
                
                
    def updateReference(self):
        if self.listSourceFile:
            for sou in range(len(self.listSourceFile)):
                key="a"+str(sou)
                values=mc.checkBox(key,q=True,value=True)
                if values==True:
                    freeSV=mm.eval('strip(system("wmic LogicalDisk where Caption=\'E:\' get FreeSpace /value"))')
                    freeMV = re.sub("\D", "", freeSV)
                    fileSize=os.path.getsize(self.listSourceFile[sou])
                    if freeMV<fileSize:
                        mc.confirmDialog(message=u"E:盘空间过小将影响性能，建议马上清理磁盘空间", button="OK")
                        return 
                    destFilePath=os.path.dirname(self.listDestFile[sou])
                    try:
                        #print self.listSourceFile[sou]
                        shutil.copy(self.listSourceFile[sou],destFilePath)
                        referenceNode=mc.file(self.listDestFile[sou],q=True,referenceNode=True)
                        mc.file(self.listDestFile[sou],loadReference=referenceNode)
                    except:
                        mc.confirmDialog(message=self.listSourceFile[sou]+u"文件更新出错!!!",button="OK")
                        return
          
        mc.deleteUI('updateReferenceUI')
        
    def AllSelectReference(self):
        if self.listSourceFile:
            for sou in range(len(self.listSourceFile)):
                key="a"+str(sou)
                values=mc.checkBox(key,e=True,value=True)
    def UnselectReference(self):
        if self.listSourceFile:
            for sou in range(len(self.listSourceFile)):
                key="a"+str(sou)
                values=mc.checkBox(key,e=True,value=False)

class zwCheckinCheckTextureCompareMaster():
    def __init__(self):
        pass
        
    def CommonPostSceneRead(self):
        allReferences=mc.file(q=True,reference=True)
        infos=""
        flag=0
        if allReferences:
            for referene in allReferences:
                textureFileName=""
                refer=mc.referenceQuery(referene,withoutCopyNumber=True,shortName=True,filename=True)
                masterPath=os.path.dirname(referene)
                masterPaths=masterPath+"/"+refer
                
                masterTime=os.path.getmtime(masterPaths)
                buf=refer.split("_")
                if  "_h_mc_" in refer:
                    textureFileName=buf[0]+"_"+buf[1]+"_"+buf[3]+"_tx.mb"
                elif "_h_dy_" in refer:
                    textureFileName=buf[0]+"_"+buf[1]+"_"+buf[3]+"_tx.mb"
                else:
                    textureFileName=buf[0]+"_"+buf[1]+"_"+buf[2]+"_tx.mb"
                
                texturePath=masterPath.replace("master","texture")
                texturePaths=texturePath+"/"+textureFileName
                if os.path.isfile(texturePaths):
                    textureTime=os.path.getmtime(texturePaths)
                    if masterTime<textureTime:
                        flag=1
                        infos=infos+masterPaths+u"文件更新时间比texture里面的文件更新时间早\n"
                else:
                    textureFileNameH=buf[0]+"_"+buf[1]+"_"+buf[2]+"_tx.mb"
                    textureFilePath=texturePath+"/"+textureFileNameH
                    if os.path.isfile(textureFilePath):
                        textureTime=os.path.getmtime(textureFilePath)
                        if masterTime<textureTime:
                            flag=1
                            infos=infos+masterPaths+u"文件更新时间比texture里面的文件更新时间早\n"
            if flag>0:
                mc.confirmDialog(title=u"master与texture比较更新时间",message=infos)

             
                
def OCT_UpdateReferenceRemind():
    updateReferences().CommonNewSceneOpened()
    zwCheckinCheckTextureCompareMaster().CommonPostSceneRead()  

def OCT_deleteMentalray():
    try:
        mc.delete('mentalrayGlobals')
    except:
        pass
def OCT_deleteShave():
    try:
        mc.delete('shaveGlobals')
    except:
        pass  
def OCT_deleteMentalrayShave():
    OCT_deleteMentalray()
    OCT_deleteShave()
