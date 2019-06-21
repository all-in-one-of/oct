# -*- coding: utf-8 -*-

from __future__ import with_statement #only needed for maya 2008 & 2009

import os
import maya.utils
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import string, sys
import shutil,re


def makeMenu():
    _gMainWindow = mm.eval("global string $gMainWindow;string $temp = $gMainWindow;")
    #   _gMainWindow = 'MayaWindow'

    mc.setParent(_gMainWindow)
    mc.menu("OCT_ToolSetMN", l="OCT Vision", to=True, tearOff=False, parent=_gMainWindow)
    mc.menuItem('checkin', l=u'Check in...', to=True, c='mm.eval("octvCheckinTool;")', parent='OCT_ToolSetMN')
    mc.menuItem(d=1, parent="OCT_ToolSetMN")

    #提交工具
    mc.menuItem('OCT_sub', l=u'提交任务到Deadline...', subMenu=True, to=True, parent='OCT_ToolSetMN')
    mc.menuItem('submitMayaJob_zwz_check', l=u'检查工程的完整性', ann=u'检查工程的完整性...', c='OCT_generel.submitMayaToDeadline_zwz(1)', parent='OCT_sub')
    mc.menuItem('submitMayaJob_zwz_copy', l=u'拷贝工程(先检查工程完成，再拷贝)...', ann=u'拷贝工程...', c='OCT_generel.submitMayaToDeadline_zwz(2)', parent='OCT_sub')
    mc.menuItem('submitMayaJob_zwz_sub', l=u'提交文件至Deadline(灯光组使用)...', ann=u'提交文件至Deadline...', c='OCT_generel.submitMayaToDeadline_zwz(3)', parent='OCT_sub')
    mc.menuItem('submitMayaJob_zwz_deep', l=u'提交文件至Deadline设置deep(灯光组提交文件给特效渲染deep)...', ann=u'提交文件至Deadline设置deep，仅限合成同事使用', c='OCT_generel.submitMayaToDeadline_zwz(5)', parent='OCT_sub')

    mc.menuItem('submitMayaJob_zwz_sub8.0', l=u'提交文件至Dealine10.0测试版...', ann=u'', c='OCT_generel.submitMayaToDeadline_zwz(7)', parent='OCT_sub')

    #通用工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Generel", label=u"通用工具", ann=u'通用工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('OpenProjectFile', l=u'打开当前目录的相应文件夹...', ann=u'打开当前目录的相应文件夹...', c='mm.eval("zwz_OpenMyScenFile;")', parent='OCT_Generel')
    mc.menuItem("ArnoldTools_zwz", label=u"Arnold快速设置(Custom Tool)...", ann=u'Arnold快速设置...', c="OCT_generel.callArnoldTools()", parent="OCT_Generel")
    mc.menuItem("ExportScene_zwz", label=u"导出并优化场景(不用选择物体)", ann=u'导出并优化场景', c='OCT_generel.OCT_Export_Scene_with_Optimize_zwz()', parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem("rename", label=u"重命名(打开窗口选择组或物体改名)...", ann=u'重命名(打开窗口选择组或物体改名)...', c='mm.eval("NWrename_win;")', parent="OCT_Generel")
    mc.menuItem("New_removeNamespace", l=u"新清除前缀名(查找tr节点,去掉':'之前物体名)", ann=u'新清除前缀名', c='mm.eval("delete_name_space_zqs;")', parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('ReplaceOrOb', l=u'把许多物体改为关联复制...', ann=u'把许多物体改为关联复制...', c='OCT_generel.ReplaceOriginalObject()', parent='OCT_Generel')
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('deleteSelectGroup', l=u'删除所选(锁定)组...', ann=u'删除所选(锁定)组...', c='OCT_generel.deleteSelectGroup()', parent='OCT_Generel')
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem("FTM", l=u"贴图管理工具...", ann=u'贴图管理工具...', c= 'mm.eval("FileTextureManager 0;")', parent="OCT_Generel")
    mc.menuItem('Texture Manager', l=u'贴图整理工具...', ann=u'贴图整理工具...', c="mm.eval('fh_textureManagerGUI;')", parent="OCT_Generel")
    mc.menuItem("FindTextturByPath", l=u"在指定的路径下寻找贴图...", ann=u'在制定的路径下寻找贴图', c='mm.eval("tjh_lost_textures_finder;")', parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('Associate_attribute', l=u'模糊选择与属性关联Locator(模糊找物体，选择物体和locator关联)...', ann=u'模糊选择与属性关联Locator', c="OCT_generel.OCT_Associate_attribute_zwz.OCT_Associate_attribute_zwz_UI()", parent="OCT_Generel")
    mc.menuItem('Edges_Constrain', l=u'用两条边创建locator，并受其约束(先选择相邻的两条边)', ann=u'用两条边创建locator，并受其约束', c="mm.eval('tazz_EdgeConstrain;')", parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('BottomPivot_tazz', l=u'轴心点置底(先选择dag物体,再执行)', ann=u'轴心点置底', c="mm.eval('tazz_BottomPivot;')", parent="OCT_Generel")
    mc.menuItem('Average_Vertex_PositionM', l=u'获取所选物体的中心点(先选择物体，再创建loctor置物体的中心点)', ann=u'获取所选物体的中心点', c="mm.eval('Average_Vertex_Position;')", parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('OpenCloseRenderThumbnailUpdate', l=u'打开与关闭材质更新', ann=u'打开与关闭材质更新', c="OCT_generel.OpenCloseRenderThumbnailUpdate()", parent="OCT_Generel")
    mc.menuItem('combineBasedShaderEngens', l=u'合并工具', ann=u'合并工具', c='mm.eval("combineBasedShaderEngen;")', parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('xGPUCache', l = u'创建缓存工具', ann=u'创建缓存工具', c='OCT_generel.OCT_xGPUCache.window_xGPU()', parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('importExportShaderCon', l=u'导入导出材质连接信息(导出材质连接保存txt)', ann=u'导入导出材质连接信息', c="mm.eval('shadingGroupConnectionImportExport;')", parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('UnloadPlugin', l=u'插件卸载器', ann=u'插件卸载器', c="OCT_generel.Unload_Plugins()", parent="OCT_Generel")
    mc.menuItem(d=1, parent="OCT_Generel")
    mc.menuItem('changeToBlinn', l=u'转换成blinn材质', ann=u'转换成blinn材质', c="OCT_generel.OCT_changeToBlinn.changeToBlinn().do()", parent="OCT_Generel")
    mc.menuItem('loadAnglePlugin', l=u'添加文件勾选anglePlugin插件的节点', ann=u'添加文件勾选anglePlugin插件的节点', c='mm.eval("loadAnglePlugin;")', parent="OCT_Generel")

    #检查工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Optimiza", label=u'检查工具', ann=u'检查工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('del unUseNode', label=u'1.清理工具集合', ann=u'清理工具集合', to=True, c='OCT_check.AutoOptimizeScenes()', parent="OCT_Optimiza")
    mc.menuItem('del name space', label=u'1.删除命名空间(不包括referece)', ann=u'1.删除命名空间(不包括referece)', to=True, c='mm.eval("oct_delNameSpace;")', parent="OCT_Optimiza")
    mc.menuItem('reMap_tools', label=u'2.解决重名问题', ann=u'2.解决重名问题', to=True, c='mm.eval("renameTransForm_muilty_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('reLongName_Tool', label=u'3.解决名字过长问题 ', ann=u'3.解决名字过长问题', to=True, c='mm.eval("OCT_reLongName;")', parent="OCT_Optimiza")
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem('deleteMidMesh_tools', label=u'合法贴图名', ann=u'合法贴图名', to=True, c='mm.eval("reMap_name_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('checkYxSize_tools', label=u'检查贴图尺寸', ann=u'检查贴图尺寸', to=True, c='OCT_check.CheckTXSize()', parent="OCT_Optimiza")
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem('renameTransForm_tools', label=u'清理垃圾midMesh ', ann=u'清理垃圾midMesh', to=True, c='mm.eval("deleteMidMeshSafe_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('clearNoVertex_tools', label=u'清除无点polygon ', ann=u'清除无点polygon', to=True, c='mm.eval("clearNoVertex_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('clearLJ_tools', label=u'清理各种垃圾 ', ann=u'清理各种垃圾', to=True, c='mm.eval("clearLJ_zqs;")', parent="OCT_Optimiza")
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem('checkingNoAnyMat_tools', label=u'检查没有赋任何材质shader的物体(检查没赋材质物体保存在layer_noShader显示层)', ann=u'检查没有赋任何材质shader的物体', to=True, c='mm.eval("checkingNoAnyMat_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('clearInitialmat_tools', label=u'清除默认材质球', ann=u'清除默认材质球', to=True, c='mm.eval("clearInitialmat_zqs;")', parent="OCT_Optimiza")
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem('checkingSmallArea_tools', label=u'检查极小面体积的物体(小于3个点,Box小于0.001删除)', ann=u'检查极小面体积的物体', to=True, c='mm.eval("checkingSmallArea_zqs;")', parent="OCT_Optimiza")
    mc.menuItem('setArnoldDsoPath_tools', label=u'修正Arnold代理路径', ann=u'修正Arnold代理路径', to=True, c='mm.eval("setArnoldDsoPath_zqs;")', parent="OCT_Optimiza")
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem('checkReference', label=u'检查Reference', ann=u'检查Reference', subMenu=True, to=True, parent='OCT_Optimiza')
    mc.menuItem('checkUnUserReferences', label=u'检查UnUserReference', ann=u'检查UnUserReference...', c='OCT_check.checkUnusedRefence(1)', parent='checkReference')
    mc.menuItem('deleteUnUserReferences', label=u'删除UnUserReference', ann=u'删除UnUserReference...', c='OCT_check.checkUnusedRefence(2)', parent='checkReference')
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem("delNurbsCurve", label=u"删除场景中的nurbsCurve...", ann=u'删除场景中的nurbsCurve...', c="OCT_generel.delNurbsCurve()", parent="OCT_Optimiza")
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem('clearlightLinkerConnections_an', label=u'清理灯光连接', ann=u'清理灯光连接', to=True, c='mm.eval("clearlightLinkerConnections_zqs;")', parent="OCT_Optimiza")
    mc.menuItem("deleteSGNode", label=u"删除所有的SG节点...", ann=u'删除所有的SG节点...', c="OCT_render.deleteSGNode_YH()", parent="OCT_Optimiza")
    mc.menuItem('disConSG', l=u'断开所选模型与SG节点连接(用于有参考重新给材质给不上)...', ann=u'断开所选模型与SG节点连接...', c='OCT_check.disconnectSGNode()', parent='OCT_Optimiza')
    mc.menuItem('deleteUnknown', l=u'删除unknown节点(删除未知的节点)...', ann=u'删除unknown节点...', c='OCT_generel.deleteUnknown()', parent='OCT_Optimiza')
    mc.menuItem(d=1, parent="OCT_Optimiza")
    mc.menuItem('OCT_Set', label=u'OCT_Set', ann=u'OCT_Set', to=True, c='mm.eval("OCT_Set;")', parent="OCT_Optimiza")


    #模型工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Mod", label=u'模型工具', ann=u'模型工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('TransferShaders', l=u'传递UV和材质...', ann=u'传递UV和材质...', c='mm.eval("tazz_TransferShaders")', parent='OCT_Mod')
    mc.menuItem('iso', label=u'根据UV选择Nurbs的线(先选择nurbs,执行产生等距等参数线)...', ann=u'根据UV选择Nurbs的线...', c='mm.eval("IC_calIso;")', parent='OCT_Mod')
    mc.menuItem('DelUvSets', label=u'删除多余的UV Sets(先选择物体)', ann=u'删除多余的UV Sets', c='OCT_mod.OCT_DelUnuseUvSets_zxy.DelUnuseUvSets_zxy()', parent='OCT_Mod')
    mc.menuItem('SetUV', label=u'随机设置UV(选择物体,随机分布)', ann=u'随机设置UV', c='OCT_mod.randomUVSet_YH()', parent='OCT_Mod')
    mc.menuItem('checkingPolyUV_tools', label=u'UV处理(不用选择优化UV,删除无用的UV)', ann=u'UV处理', to=True, c='mm.eval("checkingPolyUV_zqs;")', parent="OCT_Mod")
    mc.menuItem('selectUVEdge', label=u'选择UV边界线工具(先选择物体)', ann=u'选择UV边界线工具', c='OCT_mod.selectUVEdge()', parent='OCT_Mod')
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('rockGen', label=u'石头创建工具...', ann=u'石头创建工具...', c='mm.eval("HXRockGenChinese;")', parent='OCT_Mod')
    mc.menuItem('createbuilding', label=u'大楼创造器...', ann=u'大楼创造器...', c='mm.eval("EdW_KludgeCity;")', parent='OCT_Mod')
    #mc.menuItem('SeparateAndCombine', label=u'分离重合并模型', ann=u'分离重合并模型', c='OCT_mod.SeparateAndCombine()', parent='OCT_Mod')
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('ExShaderTools', l=u'替换材质工具...', ann=u'替换材质工具...', c='OCT_lgt.OCT_exShader()', parent='OCT_Mod')
    mc.menuItem('cleanMatTools', l=u'清理材质工具...', ann=u'清理材质工具...', c='OCT_lgt.cleanMatUI()', parent='OCT_Mod')
    mc.menuItem('removeDuplicateMatTools', l=u'清理材质工具...(测试版)', ann=u'清理材质工具...(测试版)', c='OCT_mod.removeDuplicateMat()', parent='OCT_Mod')
    mc.menuItem('renameTexture', l=u'修改材质贴图名称工具...(只添加项目名)', ann=u'修改材质贴图名称工具...(只添加项目名)', c='OCT_generel.renameTexture_temp()', parent='OCT_Mod')
    mc.menuItem('repairTex_YJL', l=u'修复贴图(参考关联复制材质修复工具)...', ann=u'修复贴图...', c='OCT_mod.repairTex_YJL.repWin()', parent='OCT_Mod')
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('smoothTools', l=u'圆滑工具...', ann=u'圆滑工具...', c='mm.eval("tazz_SmoothTool")', parent='OCT_Mod')
    mc.menuItem('PlaceOnMesh', label=u'把物体种植面上(先选择要种植的物体，再选择被种植的物体面)', ann=u'把物体种植面上', c='OCT_mod.placeOnMesh()', parent='OCT_Mod')
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('Replacemodel', label=u'替换模型工具...', ann=u'替换模型工具', c='OCT_mod.runWhiteBoxTool()', parent='OCT_Mod')
    mc.menuItem('spPaint3', label=u'新版三维种植工具...', ann=u'新版三维种植工具', c='OCT_mod.runSpPaint3d()', parent='OCT_Mod')
    mc.menuItem('Paint3', label=u'笔刷种树工具...', ann=u'笔刷种树工具', c='OCT_mod.rPaint3d()', parent='OCT_Mod')
    mc.menuItem('YetiPaint', label=u'新笔刷种树...', ann=u'新笔刷种树', c='OCT_mod.YetiPaintTool()', parent='OCT_Mod')
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('assignShader_zwz', label=u'随机赋予指定物体指定的材质(选择物体与材质(按钮1,2),再执行按钮3)...', ann=u'随机赋予指定物体指定的材质', c='OCT_mod.OCT_AssignRandShader_zwz.OCT_AssignRandShader_UI_zwz()', parent='OCT_Mod')
    mc.menuItem('ProjectNurbsonPoly_zzj', label=u'映射nurbs到poly上(打开窗口,选择曲线,执行)...', ann=u'映射nurbs到poly上', c='mm.eval("tazz_ProjNurbs2Poly;")', parent='OCT_Mod')
    mc.menuItem('Duplicate_FPolyace', label=u'复制多个poly的面(先选择物体)', ann=u'复制多个poly的面', c='mm.eval("tazz_MultDupFace;")', parent='OCT_Mod')
    mc.menuItem('FKSDY_SetBot', label=u'去掉File节点的Bots勾选项(批量去点file节点的Bots)', ann=u'去掉File节点的Bots勾选项', c='OCT_mod.OCT_FKSDYDelBot_zwz.OCT_FKSDYDelBot_zwz()', parent='OCT_Mod') 
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('TextureMaterialTool', label=u'arnold透明贴图材质工具', ann=u'arnold透明贴图材质工具', c='OCT_mod.TextureMaterialTool()', parent='OCT_Mod')
    mc.menuItem("ArnoldBox", label=u"arnold代理显示Box(解决模型制作arnld代理卡)", ann=u'arnold代理显示Box...', c="OCT_mod.ArnoldBox()", parent="OCT_Mod")
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('matLib_Tools', label=u'材质质感库', ann=u'材质质感库', to=True, c='OCT_matLib.matLib_Tools()', parent="OCT_Mod")
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('displacementShader', label=u'断开与连接材质贴图(有置换贴图用)', ann=u'断开与连接材质贴图', c='OCT_mod.displacementShader()', parent='OCT_Mod') 
    mc.menuItem('lbTrUIv01', label=u'随机位移、旋转、缩放工具', ann=u'随机位移、旋转、缩放工具', to=True, c='mm.eval("lbTrUIv01;")', parent="OCT_Mod")
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('selectedCreateGroup', label=u'选择的每个物体打组', ann=u'选择的每个物体打组', to=True, c='OCT_mod.selectedCreateGroup()', parent="OCT_Mod")
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('ReductionFace', label=u'减面工具', ann=u'减面工具', to=True, c='OCT_mod.ReductionFace()', parent="OCT_Mod")
    mc.menuItem(d=1, parent="OCT_Mod")
    mc.menuItem('ModecleanupCheck', label=u'模型不规则检测', ann=u'检测模型的非4边面', to=True, c='mm.eval("cleanupCheck;")',parent="OCT_Mod")
    mc.menuItem('SnapToPlane', label=u'物体吸附到平面工具', ann=u'物体吸附到平面工具', to=True, c='OCT_mod.SnapToPlane.SnapToPlane()',parent="OCT_Mod")

    #代理工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_proxys", label=u'代理工具', ann=u'代理工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('Rename', label=u'上传代理前重命名材质贴图名字', ann=u'上传代理前重命名材质贴图名字', c='OCT_proxy.Rename.FProxyRename()', parent="OCT_proxys")
    mc.menuItem('UploadProxy', label=u'上传代理工具', ann=u'上传代理工具', c='OCT_proxy.uploadProxy(1)', parent="OCT_proxys")
    mc.menuItem('UploadProxy_v2', label=u'新上传代理工具', ann=u'新上传代理工具', c='OCT_proxy.uploadProxy(2)', parent="OCT_proxys")
    mc.menuItem('download', label=u'代理工具', ann=u'代理工具', c='OCT_proxy.download()', parent="OCT_proxys")
    mc.menuItem(d=1, parent="OCT_proxys")
    mc.menuItem('ArnoldAssManager', label=u'arnold代理文件管理工具', ann=u'arnold代理文件管理工具', c='mm.eval("ArnoldAssManager;")', parent='OCT_proxys')
    mc.menuItem(d=1, parent="OCT_proxys")
    mc.menuItem('changeProxys', label=u'根据代理库路径的代理转换(根据代理库路径转换VRay、arnold代理、原文件)', ann=u'根据代理库路径的代理转换', c='OCT_proxy.newProxyChange()', parent="OCT_proxys")
    mc.menuItem('SameNameProxyChange', label=u'相同代理名互换(arnold和VRay代理名相似，转换代理库中的代理)', ann=u'相同代理名互换', c='OCT_proxy.SameNameProxyChange()', parent="OCT_proxys")
    mc.menuItem('VRayProxyChangeModel', label=u'VRay代理转Model(代理库中的路劲名相似)', ann=u'VRay代理转Model', c='OCT_proxy.VRayProxyChangeModel()', parent="OCT_proxys")
    mc.menuItem('VRayProxyChangeArnoldProxy', label=u'VRay代理转Arnold代理(代理路径、代理名相同，后缀名不同)', ann=u'VRay代理转Arnold代理', c='OCT_proxy.proxyChanges()', parent="OCT_proxys")
    # mc.menuItem("FindVrayProxyes", label=u'查找VrayMesh的代表物体', ann=u'查找VrayMesh的代表物体', c='OCT_lgt.FindVrayProxys()', parent="OCT_proxys")
    mc.menuItem(d=1, parent="OCT_proxys")
    mc.menuItem(d=1, parent="OCT_proxys")
    mc.menuItem('exPrx4Ins_mi', label=u'替换代理-关联复制(instance)版', ann=u'代理替换工具(可替换关联复制(instance)代理)\n可保持关联复制', c='OCT_proxy.ExchangeProxy4Instance()', parent="OCT_proxys")


    #摄像机工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Camera", label=u'摄像机工具', ann=u'摄像机工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('shakeCamera_zqs', label=u'抖动摄像机(选择相机或物体,执行添加属性控制)...', ann=u'抖动摄像机', c='mm.eval("camShake")', parent='OCT_Camera')
    mc.menuItem('cameraZoom_zzj', label=u'摄像机缩放(偏移和缩放)...', ann=u'摄像机缩放', c='mm.eval("zoomerate")', parent='OCT_Camera')
    mc.menuItem('stereoCamera', label=u'创建环幕摄像机', ann=u'创建环幕摄像机', c='OCT_cam.zwz_CreateStereoCamera.zwz_CreateStereoCamera_menu()', parent='OCT_Camera')
    mc.menuItem('camerasCurves', label=u'创建摄像机视域范围框', ann=u'创建摄像机视域范围框', c='OCT_cam.OCT_CmeraCurves_zwz.OCT_CmeraCurves_zwz()', parent='OCT_Camera')
    mc.menuItem('CreateCamCurve', label=u'创建相机速度动画曲线', ann=u'创建相机速度动画曲线', c='mm.eval("CreateCamCurve_ZZF;")', parent='OCT_Camera')
    mc.menuItem(d=1, parent="OCT_Camera")
    mc.menuItem('MCameraPlane', label=u'多摄像机视域面', ann=u'多摄像机视域面', subMenu=True, to=True, parent='OCT_Camera')
    mc.menuItem('Scalecameras', label=u'调整预览窗口大小(先打开视域窗口按比例缩放)...', ann=u'调整预览窗口大小...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_Window_Scale()', parent='MCameraPlane')
    mc.menuItem('onecameras', label=u'1 View...', ann=u'1_水平视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_1_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('threeameras', label=u'环幕摄像机(自定义)...', ann=u'环幕摄像机(自定义)...', c='OCT_cam.Cam_3_H_Model()', parent='MCameraPlane')
    mc.menuItem('Ring_Cam', label=u'新环幕摄像机(自定义视图数)...', ann=u'新环幕摄像机(自定义视图数)...', c='OCT_cam.Cam_Ring_new()', parent='MCameraPlane')
    mc.menuItem(d=1, parent="MCameraPlane")
    mc.menuItem('two_cameras_SDGT', label=u'2_H View for SDGT...', ann=u'2_垂直视图_圣地古塔...', c='OCT_cam.newCamerasTools("SDGT_Two")', parent='MCameraPlane')
    mc.menuItem(d=1, parent="MCameraPlane")
    mc.menuItem('threeVcameras', label=u'3 V View...', ann=u'3_垂直视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_3_V_Model_Win_menu()', parent='MCameraPlane')   
    mc.menuItem('foureH_T_cameras', label=u'4_H_T View...', ann=u'4_水平视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_4_H_T_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('FKBS_Third', label=u'New 4 View for FKBS(Ball FKBS球幕)...', ann=u'3_视图...', c='OCT_cam.newCamerasTools("FKBS_Four")', parent='MCameraPlane')
    mc.menuItem('fivecamerasAni', label=u'5 View...', ann=u'5_视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_5_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('fivecameras180degrees', label=u'5 View 180度球幕(中间1:1,左右0.5:1,上下1:0.5)', ann = u'5_视图180度球幕', c = 'OCT_cam.OCT_MCameraModel_zwz.Cam_5_180degrees_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('FKBS_Six', label=u'6 View for FKBS(FKBS环幕)...', ann=u'6_视图...', c='OCT_cam.newCamerasTools("FKBS_Six")', parent='MCameraPlane')
    mc.menuItem('CDFKBS_Six', label=u'6 View for CDFKBS...', ann=u'6_视图...', c='OCT_cam.newCamerasTools("CDFKBS")', parent='MCameraPlane')
    mc.menuItem('ninecamerasAni', label=u'9 View(9_视图)...', ann=u'9_视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_9_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('tencamerasAni', label=u'10 View(10_视图)...', ann=u'10_视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_10_Model_Win_menu()', parent='MCameraPlane')
    mc.menuItem('SH_Six', label=u'12 View for SH(6_视图,神话)...', ann=u'12_视图...', c='OCT_cam.newCamerasTools("SH_Six")', parent='MCameraPlane')
    mc.menuItem(d=1, parent="MCameraPlane")
    mc.menuItem('toggleModelOpen', label=u'打开菜单...', ann=u'打开菜单...', c='OCT_cam.newCamerasTools("Open")', parent='MCameraPlane')
    mc.menuItem('toggleModelClose', label=u'关闭菜单...', ann=u'关闭菜单...', c='OCT_cam.newCamerasTools("Close")', parent='MCameraPlane')

    #动画工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Animation", label=u'动画工具', ann=u'动画工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('NewplayBlast', l=u'新版PlayBlast工具...', ann=u'新版PlayBlast工具', c="OCT_generel.NewPlayBlsst_zwz()", parent="OCT_Animation")
    mc.menuItem('playBlast', l=u'PlayBlast工具...', ann=u'PlayBlast工具', c="OCT_generel.playBlast()", parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('poseMan', label=u'姿态快照...', ann=u'姿态快照...', c='mm.eval("poseMan;")', parent='OCT_Animation')
    mc.menuItem('CreatrGeoCache', label=u'批量创建点缓存...', ann=u'批量创建点缓存...', c='OCT_anim.OCT_CreateGeometryCache_zwz.OCT_CreateGeometryCache_Menum_zwz()', parent='OCT_Animation')
    mc.menuItem('cachefilesTools', label=u'缓存管理工具...', ann=u'缓存管理工具...', c='OCT_anim.run_CacheFile_Tools_zwz()', parent='OCT_Animation')
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('Bake_Ani_with_cache', label=u'拷贝带缓存的动画并错开帧数(选择带点缓存的物体,执行复制物体并错开帧)', ann=u'拷贝带缓存的动画并错开帧数...', c='mm.eval("Bake_Animate_With_cache_YH;")', parent='OCT_Animation')
    mc.menuItem('Bake_Camera_all', label=u'Bake选择的摄像机(选选择相机,拷贝相机,Bake相机属性)', ann=u'Bake选择的摄像机...', c='OCT_anim.OCT_BakeCamera()', parent='OCT_Animation')
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem("changeFrameRate", label=u'48帧装换24帧率...', ann=u'48帧装换24帧率...', c='OCT_lgt.changeFrameRate()', parent="OCT_Animation")
    mc.menuItem("DisplayCurrentFrame", label=u'修复HeadUpDisplay无法显示当前帧', ann=u'修复HeadUpDisplay无法显示当前帧', c='OCT_anim.resetHeadsUpCurrentFrame()', parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('tazz_rollrocks', label=u'滚石动画(选择物体,为物体创建旋转X的动画)', ann=u'滚石动画', c='mm.eval("tazz_rollrocks;")', parent='OCT_Animation')
    mc.menuItem('ReferenceToInstance', label=u'参考转成替换(导入替换物体,先选择被替换的参考物体,再选择替换导入的物体)', ann=u'参考转成替换', c='mm.eval("ReferenceToInstance_YH;")', parent='OCT_Animation')
    mc.menuItem('ChangeRefer', label=u'转换参考的几种方式', ann=u'面部表情工具', c='OCT_anim.ChangeReference()', parent='OCT_Animation')
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('Face_Tools_YH', label=u'面部表情工具(导出:先选择曲线,按帧率导出.导入:先选择曲线,按帧率24或48导出)', ann=u'面部表情工具', c='OCT_anim.FaceTools()', parent='OCT_Animation')
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('copyReferenceTool', label=u'拷贝更新参考物体到本机和修改参考的路径', ann=u'拷贝参考物体到本机和修改参考的路径', c='OCT_anim.copyReference()', parent='OCT_Animation')
    mc.menuItem('createAnimCurve', label=u'根据动画路径创建曲线(先选择物体,根据开始、结束、隔帧创建路径动画曲线)', ann=u'根据动画路径创建曲线', c='OCT_anim.createAnimCurve()', parent='OCT_Animation')
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('delMaterialAndFace', label=u'删除材质改lambert(清理材质,所有物体赋予一个lambert)', ann=u'删除材质改lambert', to=True, c='OCT_anim.OCT_delMaterialAndFace()', parent="OCT_Animation")
    mc.menuItem('deleteunUserCacheNode', label=u'删除无用的缓存节点(根据连接节点判读若不是缓存、布料、头发就删除)', ann=u'删除无用的缓存节点', to=True, c='mm.eval("delect_UnuseredCache;")', parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('miarmyGroup', label=u'群集物体打组(选择骨骼组找蒙皮并打组改名,inApply:输入物体新名,outApply:输出物体新名)', ann=u'群集物体打组', to=True, c='OCT_anim.miarmyGroup()', parent="OCT_Animation")
    mc.menuItem('miaryAnimCopy', label=u'群集物体替换拷贝动画(按群集输入输出打组,先选择输入替换的,在选择被替换的)', ann=u'群集物体替换拷贝动画', to=True, c='OCT_anim.miaryAnimCopy()', parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('fix_animation', label=u'修复动画丢失(选择要恢复动画的控制器,相应的动画曲线节点必须存在，没清理)', ann=u'修复动画丢失', to=True, c='OCT_anim.OCT_fix_animation_LXJ.fix_animation()', parent="OCT_Animation")
    mc.menuItem('wind_noises', label=u'风吹动物体的工具(选择物体,必须有houdiniAsset插件)', ann=u'风吹动物体的工具', c='mm.eval("wind_noises;")', parent='OCT_Animation')
    mc.menuItem('IKFK', label=u'IKFK无缝切换', ann=u'IKFK无缝切换', c='mm.eval("IKFK;")', parent='OCT_Animation')
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('ImportExportAnim', label=u'导入导出动画', ann=u'导入导出动画', subMenu=True, to=True, parent='OCT_Animation')
    mc.menuItem('ExportAnimData', label=u'导出动画数据(先列出相关的角色在列表中,选择导出动画数据)', ann=u'导出动画数据', to=True, c='OCT_anim.exportAnimData()', parent="ImportExportAnim")
    mc.menuItem('ImportAnimData', label=u'导入动画数据(先列出角色在列表中,在导入动画数据的缓存,选择相应的角色导入)', ann=u'导入动画数据', to=True, c='OCT_anim.importAnimData()', parent="ImportExportAnim")
    mc.menuItem('LXYRotateWin', label=u'导出物体属性', ann=u'导出物体属性', to=True, c='mm.eval("LXYRotateWin;")', parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('KeyObjSpeedFrame', label=u'创建速度与加速度的曲线', ann=u'创建速度与加速度的曲线', to=True, c='mm.eval("SpeedAttrWindow;")', parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('Bake_Frame', label=u'Bake Frame', ann=u'Bake Frame', to=True, c='OCT_anim.Bake_Frame()', parent="OCT_Animation")
    mc.menuItem('KLJZ_DistanceToScale', label=u'KLJZ DistanceToScale', ann=u'KLJZ DistanceToScale', to=True, c='OCT_anim.kljz_dst()', parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('studiolibrary', label=u'studiolibrary动作库工具', ann=u'studiolibrary动作库工具', to=True, c='OCT_anim.studionLibrarys()', parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem(d=1, parent="OCT_Animation")
    mc.menuItem('abcSgl_mi', label=u'单角色版缓存工具', ann=u'单个角色导入导出缓存', to=True, c='OCT_anim.OCT_abcSglEdition()', parent="OCT_Animation")

    #设置工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Rigging", label=u'设置工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('JointConversion', l=u'骨骼转换(先选骨骼组,再选控制曲线,mc_k属性为动捕骨骼切换)...', ann=u'骨骼转换', c="OCT_rigging.JointConversion()", parent="OCT_Rigging")
    mc.menuItem('modifyJointname', l=u'根据动捕命令规则修改骨骼名...', ann=u'根据动捕命令规则修改骨骼名', c="OCT_rigging.modifyJointname()", parent="OCT_Rigging")
    mc.menuItem('FK_loc', l=u'手脚FK_loc创建(创建loctor,根据规则修改名字)...', ann=u'手脚FK_loc创建', c='mm.eval("FK_loc;")', parent="OCT_Rigging")

    
    #特效工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_VFX", label=u'特效工具', ann=u'特效工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('submitFile', label=u'提交文件至Deadline渲染(特效使用)...', ann=u'提交文件至Deadline渲染(特效使用)...', c='OCT_vfx.submitFile()', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('UVtoPos', label=u'查询物体某UV点世界坐标位置(先选择物体)...', ann=u'查询物体某UV点世界坐标位置...', c='OCT_vfx.uvToPosUI()', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('ExportVrayMesh_zwz1', label=u'从代理文件导出VrayMesh成FBX', ann=u'导出VrayMesh成FBX...', c='OCT_vfx.ExportVrayMeshToFbx(1)', parent='OCT_VFX')
    mc.menuItem('ExportVrayMesh_zwz2', label=u'从Mesh物体导出VrayMesh成FBX', ann=u'导出VrayMesh成FBX...', c='OCT_vfx.ExportVrayMeshToFbx(2)', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('renameSGNodes', label=u'批量修改SG名字', ann=u'批量修改SG名字', c='OCT_vfx.renameSGNodes()', parent='OCT_VFX')
    mc.menuItem('deleteNoSelMesh', label=u'选择物体并导出(选择物体放set组的增、删、改、查、导出的操作)', ann=u'选择物体并导出...', c='OCT_vfx.deleteNoSelMesh()', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('CopyObjAttrbuteToLocator', label=u'拷贝houdini引擎对象属性给locater(先选择物体)', ann=u'拷贝houdini引擎对象属性给locater...', c='OCT_vfx.CopyObjAttrbuteToLocator()', parent='OCT_VFX')
    mc.menuItem('maya_came', label=u'CameraToMaxVrayCamera(maya与max摄像机互通,先选择摄像机创建loctor记录相机属性)', ann=u'CameraToMaxVrayCamera...', c='OCT_vfx.OCT_maya_cam()', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('ModifyMaterial', label=u'转换成选面给材质并改名(先选择物体,修改连接材质的SG节点名字与材质相似)', ann=u'转换成选面给材质并改名...', c='OCT_vfx.ModifyMaterial()', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('ExportImportSGNodes', label=u'特效破碎物体上材质的几种方式', ann=u'特效破碎物体上材质的几种方式...', c='OCT_vfx.ExportImportSGNodes()', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('ReadMaterialInfo', label=u'记录材质信息到txt文档(导出物体信息和物体连接材质信息)', ann=u'记录材质信息到txt文档...', c='OCT_vfx.ReadMaterialInfo()', parent='OCT_VFX')
    mc.menuItem('WriteMaterialInfo', label=u'读取记录的材质信息将材质与物体自动连接物体', ann=u'读取记录的材质信息将材质自动连接物体...', c='OCT_vfx.WriteMaterialInfo()', parent='OCT_VFX')
    mc.menuItem(d=1, parent="OCT_VFX")
    mc.menuItem('deleteNotOpacityMaterial', label=u'删除不带透明通道的材质', ann=u'删除不带透明通道的材质...', c='OCT_vfx.deleteNotOpacityMaterial()', parent='OCT_VFX')
    mc.menuItem('findObjectSmoothness', label=u'判断所选物体是否按3', ann=u'判断所选物体是否按3...', c='OCT_vfx.findObjectSmoothness()', parent='OCT_VFX')
    mc.menuItem('createOcean', label=u'创建、设置海洋平面', ann=u'创建、设置海洋平面...', c='OCT_vfx.createArnoldOcean()', parent='OCT_VFX')


    #灯光工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Light", label=u'灯光工具', ann=u'灯光工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('submitMayaJob_zwz_W', l=u'交接给特效环节工程M:\ALL\\transfer...', ann=u'灯光交接给特效环节工程M:\ALL\\transfer...', c='OCT_generel.submitMayaToDeadline_zwz(6)', parent='OCT_Light')
    mc.menuItem('edit_vrayZDepth', l=u'修改vray ZDepth参数', ann=u'修改vray ZDepth参数', c='OCT_lgt.edit_vrayZDepth()', parent='OCT_Light')
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem('delLink', label=u'删除多余的灯光链接节点', ann=u'删除多余的灯光链接节点', c='mm.eval("IC_LightLinksCleanUp")', parent='OCT_Light')
    mc.menuItem('delUnuseLightDecay', label=u'删除多余的灯光衰减节点', ann=u'删除多余的灯光衰减节点', c='OCT_lgt.deleteUnuseLightDecay()', parent='OCT_Light')
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("ChangeShaderA_YH", label=u'统一改变默认、Vray、arnold标准材质球属性...', ann=u'统一改变默认或者Vray或者arnold标准材质球属性', c='OCT_lgt.ChangeShader_YH()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("ArnoldProduction", label=u'统一改变Arnold模型属性', ann=u'统一改变Arnold模型属性', c='OCT_lgt.ArnoldProduction_YH()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("lightAttrRandom", label=u'灯光属性设置随机值', ann=u'灯光属性设置随机值', c='OCT_lgt.lightAttrRan()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("ChangeAttr_YH", label=u'改变所选灯光的属性(普通灯光、VRay、arnold)', ann=u'改变所选灯光的属性', c='OCT_lgt.ChangeAttr_YH()', parent="OCT_Light")
    mc.menuItem('eyePointLight', l=u'眼神光(选择眼睛模型)', c='OCT_lgt.HYZX_eyeLight()', ann=u'眼神光', parent='OCT_Light')
    mc.menuItem('makemyVolumnLight', l=u'创建假冒的体积光', ann=u'创建假冒的体积光', c='mm.eval("tazz_CreatePointToVolumnLight();")', parent='OCT_Light')
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("arnoldProxyNew", label=u'新检查Arnold代理并拷贝(交接代理文件缓存根据文件缓存从代理库拷贝)', ann=u'新检查Arnold代理并拷贝', c='OCT_lgt.CheckArnoldProxy_YH(2)', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("convertTexFormat", label=u'转换贴图格式(同文件夹贴图名字相同后,缀名不同)', ann=u'转换贴图格式', c='OCT_lgt.ConvertTexFormat_YH()', parent="OCT_Light")
    mc.menuItem("changenNetworkPaths", label=u'改变网路路径与拷贝贴图(${OCTV_PROJECTS}改为//octvision.com/CG,分文件夹拷贝贴图)', ann=u'改变网路路径与拷贝贴图', c='OCT_lgt.changenNetworkPaths()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("tazz_intensity", label=u'灯光闪烁工具(选择灯光，创建闪烁的表达式)', ann=u'灯光闪烁工具', c='mm.eval("tazz_intensity();")', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("sur_Occ_Layers", label=u'MR的OCC拆层工具(换成surfaceShader的材质,带透明通道)', ann=u'MR的OCC拆层工具', c='OCT_lgt.sur_Occ_Layers()', parent="OCT_Light")
    mc.menuItem("Ar_Occ_Layers", label=u'AR的OCC拆层工具(换成aiAmbientOcclusion,带透明通道)', ann=u'AR的OCC拆层工具', c='OCT_lgt.Ar_Occ_Layers()', parent="OCT_Light")
    mc.menuItem("selectTransparency", label=u"选择带透明贴图的物体...", ann=u'选择带透明贴图的物体...', c="OCT_lgt.OCT_SelectTransparency.selectTransparency()", parent="OCT_Light")
    mc.menuItem("giveNewMaterial", label=u"lambert的拆层(换成labert材质,带透明贴图)...", ann=u'lambert的拆层(带透明贴图)...', c="OCT_lgt.giveNewMaterial()", parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("aiPhotomeLightFile_Tools", label=u'灯光aiPhotomeLight贴图管理工具', ann=u'灯光aiPhotomeLight贴图管理工具', c='OCT_lgt.run_PhotometricLightMap_Tools()', parent="OCT_Light")
    mc.menuItem('VRayLightIESShapePath', l=u'修改VRayLightIESShape节点路径...', ann=u'修改VRayLightIESShape节点路径...', c='OCT_generel.VRayLightIESShapePath()', parent='OCT_Light')
    mc.menuItem(d=1, parent="OCT_Light")
    #mc.menuItem("SelectSpotLight", label=u'选择聚光灯', ann=u'选择聚光灯', c='OCT_lgt.SelectSpotLight()', parent="OCT_Light")
    #mc.menuItem("SelectAreaLight", label=u'选择面灯', ann=u'选择面灯', c='OCT_lgt.SelectAreaLight()', parent="OCT_Light")
    #mc.menuItem("selectPointLight", label=u'选择点光源', ann=u'选择点光源', c='OCT_lgt.selectPointLight()', parent="OCT_Light")
    mc.menuItem("SelectTypeLight", label=u'选择某一类型光源', ann=u'选择某一类型光源', c='OCT_lgt.selectTypeLight()', parent="OCT_Light")
    mc.menuItem("changePointLight", label=u'转换成点光源', ann=u'转换成点光源', c='OCT_lgt.changePointLight()', parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem("mergeShadingUI_rhj", label=u'合并材质工具', ann=u'合并材质工具', c='mm.eval("mergeShadingUI();")', parent="OCT_Light")
    
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem('cleanUnusedCameras_zwz', l=u'清除灯光物体中多余的摄像机', c="OCT_generel.cleanUnusedCamera_zwz()", parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem('OCT_MasK_Tool', l=u'遮罩工具(arnold做遮罩,先选择物体)', c="OCT_lgt.OCT_MasK_Tools()", parent="OCT_Light")
    mc.menuItem('OCT_ArnoldStandMasK_Tool', l=u'arnold代理遮罩工具', c="OCT_lgt.arnoldStandInMast()", parent="OCT_Light")
    
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem('lightLibrary', l=u'灯光库', ann=u'灯光库', c="OCT_lgt.lightLibrary()", parent="OCT_Light")
    mc.menuItem(d=1, parent="OCT_Light")
    mc.menuItem('duplicate light link', l=u'复制灯光链接', ann=u'复制灯光链接', c="OCT_lgt.zb_DupLightLink_cmd()", parent="OCT_Light")

    #渲染工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Render", label=u'渲染工具', ann=u'渲染工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('LayerTools', label=u'分层工具...', ann=u'分层工具...', to=True, c='OCT_render.OpenRenderLayerTools()', parent="OCT_Render")
    mc.menuItem("RenderSet_zwz", label=u"渲染面板快速设置...", ann=u'渲染面板快速设置...', c="OCT_generel.OCT_RenderSet_zwz.OCT_RenderSet_zwz_UI()", parent="OCT_Render")
    mc.menuItem("AutoCreateAOV", label=u"自动创建AOV(arnold)", ann=u'自动创建AOV(arnold)...',c="OCT_render.OCT_AutoCreateAOV.AutoCreateAOV().do()", parent="OCT_Render")
    mc.menuItem(d=1, parent="OCT_Render")
    mc.menuItem("resizeImage", l=u"修改图片大小...", ann=u'修改图片大小', c='OCT_render.run_zxy_resizeImage()', parent="OCT_Render")
    mc.menuItem(d=1, parent="OCT_Render")
    mc.menuItem('newRender', label=u'新版拍屏渲染工具...', ann=u'拍屏渲染工具...', c='OCT_render.newPreRender_YH()', parent='OCT_Render')
    mc.menuItem("QuantituRender_zwz", label=u"批量文件拍屏工具...", ann=u'批量文件拍屏工具...', c="OCT_render.OCT_QuantityRender_zwz.OCT_QuantituRender_UI_zwz()", parent="OCT_Render")
    mc.menuItem("FixFrame_zwz", label=u"单文件多任务补帧工具...", ann=u'单文件多任务补帧工具...', c="OCT_render.OCT_SuperFixFram_zwz.SuperFixFream_mmenu_zwz()", parent="OCT_Render")
    mc.menuItem(d=1, parent="OCT_Render")
    mc.menuItem("cameraConnetPlace3d", label=u"手动拆层ZD...(选择相机)", ann=u'手动拆层ZD...(选择相机)', c="OCT_render.cameraConnetPlace3d()", parent="OCT_Render")
    mc.menuItem("cameraConnetPlace3darnold", label=u"arnold类型手动拆层ZD...(选择相机)", ann=u'arnold类型手动拆层ZD...(选择相机)', c="OCT_render.cameraConnetPlace3darnold()", parent="OCT_Render")
    mc.menuItem("cameraConnetPlace3dIMP", label=u"手动拆层IMP...(选择物体)", ann=u'手动拆层IMP...(选择物体)', c="OCT_render.cameraConnetPlace3dImp()", parent="OCT_Render")
    mc.menuItem("changeShaderIMP", label=u"imp连接各种材质(选择物体)", ann=u'imp连接各种材质', c="OCT_render.changeShaderIMP()", parent="OCT_Render")
    mc.menuItem(d=1, parent= "OCT_Render")
    mc.menuItem("OCT_materialChange", label=u"材质转换...", ann=u'材质转换...', c="OCT_render.OCT_materialChanges()", parent="OCT_Render")
    mc.menuItem("OCT_aiMaterialChange", label=u"arnold Standard 转换成 Utility", ann=u'arnold Standard 转换成 Utility', c="OCT_render.aiMatModification()", parent="OCT_Render")
    mc.menuItem(d=1, parent= "OCT_Render")
    mc.menuItem("deldefaultRenderLayer", l=u"清楚多余的DefaultRenderLayer", ann=u'清楚多余的DefaultRenderLayer', c="OCT_generel.delDefaultRenderLayer()", parent="OCT_Render")
    mc.menuItem(d=1, parent= "OCT_Render")
    #mc.menuItem('fixAbcCacheFilePath', l=u'修改Abc缓存节点路径...', ann=u'修改Abc缓存节点路径...', c='OCT_generel.fixAbcCacheFilePath()', parent='OCT_Render')
    mc.menuItem("FTM", l=u"贴图管理工具...", ann=u'贴图管理工具...', c= 'mm.eval("FileTextureManager 0;")', parent="OCT_Render")
    mc.menuItem('cachefilesTools', label=u'cacheFile缓存管理工具...', ann=u'cacheFile缓存管理工具...', c='OCT_anim.run_CacheFile_Tools_zwz()', parent='OCT_Render')
    mc.menuItem('AlembicNodeFile', l=u'abc缓存管理工具...', ann=u'abc缓存管理工具...', c='OCT_render.run_AlembicNodeFile_Tools_YH()', parent='OCT_Render')
    mc.menuItem('YetiCachePath', l=u'修改点Yeti缓存节点路径...', ann=u'修改点Yeti缓存节点路径...', c='OCT_generel.YetiCachePath()', parent='OCT_Render')
    mc.menuItem('YetiFilePath', l=u'修改yeti贴图节点路径...', ann=u'修改yeti贴图节点路径...', c='OCT_generel.YetiFilePath()', parent='OCT_Render')
    mc.menuItem('YetiTexture_Tools', l=u'yeti贴图管理工具...', ann=u'yeti贴图管理工具...', c='OCT_render.run_YetiTexture_Tools()', parent='OCT_Render')
    mc.menuItem('shaveCache_Tools', l=u'shaveCache管理工具...', ann=u'shaveCache管理工具...', c='OCT_render.run_shaveCache_Tools()', parent='OCT_Render')
    mc.menuItem('fixVRmeshFilePath', l=u'修改VRayMes节点路径...', ann=u'修改VRayMes节点路径...', c='OCT_generel.fixVRayMeshFilePath()', parent='OCT_Render')
    mc.menuItem('replaceViewportProxyPath', l=u'修改VRayViewport代理路径...', ann=u'修改VRayViewport代理路径...', c='OCT_render.replaceViewportProxyPath()', parent='OCT_Render')
    mc.menuItem('VRayMeshFile', l=u'VRayMesh的管理工具...', ann=u'VRayMesh的管理工具...', c='OCT_render.run_VRayMeshFile_Tools_YH()', parent='OCT_Render')
    mc.menuItem('fixAiStandInFilePath', l=u'修改aiStandIn节点路径...', ann=u'修改aiStandIn节点路径...', c='OCT_generel.fixaiStandInFilePath()', parent='OCT_Render')
    mc.menuItem('AiStandIn_Tools', l=u'aiStandIn管理工具...', ann=u'aiStandIn管理工具...', c='OCT_render.run_AiStandIn_Tools()', parent='OCT_Render')
    mc.menuItem('CopyYeti', l=u'拷贝yeti缓存和贴图到工程目录下...', ann=u'拷贝yeti缓存和贴图到工程目录下...', c='OCT_generel.CopyYeti()', parent='OCT_Render')
    mc.menuItem(d=1, parent= "OCT_Render")
    mc.menuItem('ClearUseAndDefer', l=u'清理节点和arnold代理延迟加载...', ann=u'清理节点和arnold代理延迟加载...', c='OCT_render.ClearUseRanderDefer()', parent='OCT_Render')
    mc.menuItem('xyzDpthTool', l=u'xyz depth tools..arnold', ann=u'arnold aov 摄像机xyz 深度RGB贴图工具..', c='OCT_render.xyzDpTools()', parent='OCT_Render')
    #VR工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_VR", label=u"VR工具", ann=u'VR工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('CreateAnimationForUnity', label=u'导入数据生成动画(unity中导出的数据)', ann=u'导入数据生成动画', to=True, c='OCT_vr.CreateAnimationForUnity()', parent="OCT_VR")
    mc.menuItem('CreateAnimationForUnity_JGR', label=u'新导入数据生成动画(unity中导出的数据)', ann=u'新导入数据生成动画', to=True, c='OCT_vr.CreateAnimationForUnity_JGR()', parent="OCT_VR")

    #毛发工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Hair", label=u"毛发工具", ann=u'毛发工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem("CVToYeti", label=u"cv线转yeti", ann=u'cv线转yeti', c='mm.eval("CVToYeti")', parent="OCT_Hair")
    mc.menuItem("YetiToCurves", label=u"Yeti转curves", ann=u'Yeti转curves', c='OCT_hair.YetiToCurves()', parent="OCT_Hair")
    mc.menuItem("deleteCurve", label=u"删除曲线", ann=u'删除曲线', c='mm.eval("deleteCurve")', parent="OCT_Hair")
    mc.menuItem("x_bakeShapeWindow", label=u"blend布料(出不带缓存布料用的)", ann=u'blend布料(出不带缓存布料用的)', c='mm.eval("x_bakeShapeWindow")', parent="OCT_Hair")
    mc.menuItem("winGDMain", label=u"设置yeti引导线属性", ann=u'设置yeti引导线属性', c='mm.eval("winGDMain")', parent="OCT_Hair")
    mc.menuItem("subLevelCtrl", label=u"方便创建次级", ann=u'方便创建次级', c='mm.eval("subLevelCtrl")', parent="OCT_Hair")
    mc.menuItem("cut_curve", label=u"面剪线(先选所有曲线，最后选mesh)", ann=u'面剪线(先选所有曲线，最后选mesh)', c='OCT_hair.cut_curve()', parent="OCT_Hair")
    mc.menuItem("nb_cur", label=u"选择模型开口的一圈线创建模型中心曲线", ann=u'选择模型开口的一圈线创建模型中心曲线', c='OCT_hair.nb_cur()', parent="OCT_Hair")
    mc.menuItem("hairballUI", label=u"编辑曲线物体中间生成线", ann=u'编辑曲线物体中间生成线', c='OCT_hair.hairTool()', parent="OCT_Hair")

    # pipeline tools
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Pipeline_mi", label=u'缓存流程', ann=u'缓存流程相关工具', subMenu=True, to=True, parent="OCT_ToolSetMN")

    #旧工具
    mc.menuItem(d=1, parent="OCT_ToolSetMN")
    mc.menuItem("OCT_Old", label=u"旧工具", ann=u'旧工具', subMenu=True, to=True, parent="OCT_ToolSetMN")
    mc.menuItem('submitMayaJob_zwz_sub_comp', l=u'提交文件至Deadline特别版(有服务器权限的灯光组使用)...', ann=u'提交文件至Deadline，仅限合成同事使用', c='OCT_generel.submitMayaToDeadline_zwz(4)', parent='OCT_Old')
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem("MasterAnimtoCache", label=u"根据ms_anim文件生成ms_cache文件", ann=u'根据ms_anim文件生成ms_cache文件', c='mm.eval("octvMsA2Cache")', parent="OCT_Old")
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem("removeNamespace", l=u"清除前缀名工具(查找长名去点':'之前物体名)", ann=u'清楚前缀名', c="OCT_generel.removeNamespace()", parent="OCT_Old")
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem('fixCacheFilePath', l=u'修改点缓存节点路径...', ann=u'修改缓存节点路径...', c='OCT_generel.fixCacheFilePath()', parent='OCT_Old')
    mc.menuItem('CopyCacheFilePath', l=u'拷贝缓存并设置路径...', ann=u'拷贝缓存并设置路径...', c='OCT_generel.CopyCacheFilePath()', parent='OCT_Old')
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem("uniformPathnames", l=u"自动统一贴图路径名(设置工程相对路径)", ann=u'自动统一贴图路径名', c='mm.eval("UniformPathnames;")', parent="OCT_Old")
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem('UVRandomlyPlaced', label=u'UV随机排布...', ann=u'UV随机排布', c='mm.eval("RandomUVToolbox")', parent='OCT_Old')
    mc.menuItem('dupToCurveFlow', label=u'把物体沿曲线铺放', ann=u'把物体沿曲线铺放', c='OCT_mod.dupToCurveFlow()', parent='OCT_Old')
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem('threeHcameras', label=u'3_H_View(有自定义的环幕)...', ann=u'3_水平视图...', c='OCT_cam.OCT_MCameraModel_zwz.Cam_3_H_Model_Win_menu()', parent='OCT_Old')
    mc.menuItem('threeH_cameras_MODOU', label=u'3_H View for TDHJ Or SDGT(有自定义的环幕)...', ann=u'3_水平视图_圣地古塔...', c='OCT_cam.newCamerasTools("MODOU")', parent='OCT_Old')
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem("arnoldProxy", label=u'检查Arnold代理并拷贝(旧的arnold代理库)', ann=u'检查Arnold代理并拷贝', c='OCT_lgt.CheckArnoldProxy_YH(1)', parent="OCT_Old")
    mc.menuItem("VrayArnoldProxyChange", label=u'Vray与Arnold代理转换', ann=u'Vray与Arnold代理转换', c='OCT_lgt.VrayArnoldProxyChange()', parent="OCT_Old")
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem("changeShaveName", label=u'改变shave节点名(shave节点根据缓存的名字“：”改成“_”,maya2016一般不用shave)', ann=u'改变shave节点名', c='OCT_lgt.changeShaveName()', parent="OCT_Old")
    mc.menuItem("updateShaver", label=u'统一改变shave属性', ann=u'统一改变shave属性', c='OCT_lgt.updateShaver()', parent="OCT_Old")
    mc.menuItem(d=1, parent="OCT_Old")
    mc.menuItem('VFXRender', label=u'拍屏渲染工具...', ann=u'拍屏渲染工具...', c='mm.eval("DY_RenderToolsUI_zwz;")', parent='OCT_Old')
     
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
    
    # OCT_UpdateReferenceRemind()
    
    # mc.scriptJob(event=("PostSceneRead",OCT_UpdateReferenceRemind))
    load_ppl_mune_m()
def load_ppl_mune_m():#load pipeline menu item
    import OCT_Pipeline.scripts.Minor.menu_cmds as ppmc
    ppmc.main()
    print("Pipeline menu loaded successful!")
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

# def OCT_deleteMentalray():
#     try:
#         mc.delete('mentalrayGlobals')
#     except:
#         pass
# def OCT_deleteShave():
#     try:
#         mc.delete('shaveGlobals')
#     except:
#         pass  
# def OCT_deleteMentalrayShave():
#     OCT_deleteMentalray()
#     OCT_deleteShave()
