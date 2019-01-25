#!/usr/bin/env python
# coding=utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import sys
import maya.cmds as mc
import maya.mel as mm
import maya.utils
import maya.OpenMaya as om
import os,re

def renameSGNodes():
    all = mc.ls(type = 'shadingEngine')
    for i in all:
        newName = i.replace(':',"_")
        try:
            mc.rename(i,newName)
        except:
            pass

def submitFile():
    import OCT_SubmitDealine
    i = OCT_SubmitDealine.SubmitDeadline_Vfx()
    i.SubmitDeadline_Vfx_UI()

def createArnoldOcean():
    import OCT_CreateArnoldOCean
    i = OCT_CreateArnoldOCean.CreateArnoldOcean()
    i.CreateArnoldOcean_UI()

def ExportVrayMeshToFbx(mode):
    import ExportVrayMeshToFbx_zwz
    ExportVrayMeshToFbx_zwz.ExportVrayMeshToFbx_ex(mode)

def deleteNoSelMesh():
    import OCT_ExportSelect
    i = OCT_ExportSelect.ExportSelectObj()
    i.SelectExportUI()
   
def ExportImportSGNodes():
    import ExportImportSGNode
    i = ExportImportSGNode.ExportImportSGNode()
    i.ExportImportSGNodeUI()

def OCT_maya_cam():
    import maya_came
    maya_came.maya_came()

def ModifyMaterial():
    import ExportABCCache
    i = ExportABCCache.ExportABCCache()
    i.selectFaceToMaterial()

def ReadMaterialInfo():
    import ExportImportMaterial
    i = ExportImportMaterial.ExportImportMaterial()
    i.ShadingEngine_W()
    
def WriteMaterialInfo():
    import ExportImportMaterial
    i = ExportImportMaterial.ExportImportMaterial()
    i.ShadingEngine_UI()

def uvToPos(_mesh, _u, _v):
    import OCT_vfx
    import OCT_util
    try:
        _dagMesh = OCT_util.nameToDag(_mesh)
    except RuntimeError:
        om.MGlobal.displayWarning(u'场景里没有 %s 物体...' % _mesh)
        return
    
    placeObjType = mc.nodeType(_mesh)
    if placeObjType == 'transform':
        _shape = mc.listRelatives(_mesh,shapes=True)
        
        if _shape[0] == None:
            om.MGlobal.displayWarning(u'所选择的物体没有Shape节点...')
            return
            
        placeObjType = mc.nodeType(_shape[0])
        
        if not placeObjType == 'mesh' and not placeObjType == 'nurbsSurface':
            om.MGlobal.displayWarning(u'只支持Polygon和NURBS,请选择其中一种模型...')
            return
            
    elif not placeObjType == 'mesh' and not placeObjType == 'nurbsSurface':
        om.MGlobal.displayWarning(u'请选择模型...')
        return
    
    _point = om.MPoint()
    
    if placeObjType == 'mesh':
        _meshIt = om.MItMeshPolygon(_dagMesh)
        uv_util = om.MScriptUtil()
        uv_util.createFromDouble(_u,_v)
        uv_ptr = uv_util.asFloat2Ptr()
        _normal = om.MVector()
        while not _meshIt.isDone():
            try:
                _meshIt.getPointAtUV(_point,uv_ptr,om.MSpace.kWorld)
                _meshIt.getNormal(_normal)
                normal = round(_normal.x,4),round(_normal.y,4),round(_normal.z,4)
                #print normal
                point = round(_point.x,4),round(_point.y,4),round(_point.z,4)
                all = point,normal
                return all
            except RuntimeError:
                _meshIt.next()

        if _meshIt.isDone():
            #om.MGlobal.displayInfo(u'没有找到UV点对应的三维世界坐标位置')
            return None
            
    elif placeObjType == 'nurbsSurface':
        try:
            nurbsFn = om.MFnNurbsSurface(_dagMesh)
            nurbsFn.getPointAtParam(_u, _v, _point, om.MSpace.kWorld)
            _normal = nurbsFn.normal(_u, _v, om.MSpace.kWorld)
            normal = round(_normal.x,4),round(_normal.y,4),round(_normal.z,4)
            point = round(_point.x,4),round(_point.y,4),round(_point.z,4)
            all = point,normal
            return all
        except:
            return None


def UItoCmd():
    _u = mc.floatFieldGrp('uv',q=True,v1=True)
    _v = mc.floatFieldGrp('uv',q=True,v2=True)
    _sel = mc.ls(sl=True,head=1)
    point = uvToPos(_sel[0] ,float(_u) ,float(_v))
    if not point:
        om.MGlobal.displayWarning(u'没有找到UV点对应的三维世界坐标位置!')
        return
    if mc.window("uvToPosUI",exists=1):
        info1 = u'UV为%s,%s的对应坐标为%s,%s,%s' % (_u,_v,point[0][0],point[0][1],point[0][2])
        info2 = u'对应的法线为%s,%s,%s' % (point[1][0],point[1][1],point[1][2])
        mc.text('info1',e=True,l=info1)
        mc.text('info2',e=True,l=info2)
    
def uvToPosUI():
    if mc.windowPref("uvToPosUI",exists=True):
        mc.windowPref("uvToPosUI",remove=True)
        
    if mc.window("uvToPosUI",exists=1):
        mc.deleteUI("uvToPosUI",window=1)
    
    mc.window("uvToPosUI",title="uvToPos",maximizeButton=0,resizeToFitChildren=0,sizeable=1,wh=[365,150])
    mc.columnLayout(rowSpacing=3,columnWidth=350,columnAttach=['both',0],parent='uvToPosUI')
    mc.floatFieldGrp('uv',numberOfFields=2,l='UV',value1=0.0,value2=0.0)
    mc.text('info1',l=ur'选择要查询的物体，输入UV，按Query查询')
    mc.text('info2',l=ur'可以以命令的方式使用，如：OCT_vfx.uvToPos("obj",0.0,0.0)')
    mc.button('btn',l="Query",command='OCT_vfx.UItoCmd()')
    mc.showWindow('uvToPosUI')



# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import maya.cmds as mc
import maya.mel as mm
import os

def CopyObjAttrbuteToLocator():
    ObjectDirt = {}
    locatorObject = []
    #拷贝物体属性locator上，在输出到houdini
    objs = mc.ls(sl = True)
    fileName = mc.file(q = True, sn = True)
    filePath = os.path.dirname(fileName)
    if not mc.pluginInfo("fbxmaya.mll", q = True, loaded = True):
        mc.loadPlugin( 'fbxmaya.mll' )

    for obj in objs:
        addNoises = mc.listConnections(obj, s= True,d =False, p = True, c = True)
        if addNoises:
            for i in range(len(addNoises)/2):
                if ".outMesh" in addNoises[i*2+1]:
                    meshObj = addNoises[i*2+1].split(".outMesh")
                    #print "%s\r\n"%meshObj
                    if meshObj:
                        tansf = mc.listRelatives(meshObj[0], p = True)[0]
                        mc.select(d = True)
                        mc.select(tansf)
                        #导出物体
                        objPath = "%s/%s" % (filePath,tansf)
                        mc.file(objPath, force = True, options = "", type = "FBX export", pr = True, es = True)
                        Object = addNoises[i*2].split("[")
                        num = Object[1].split("]")
                        ObjectDirt.update({num[0]:meshObj[0]})
            print ObjectDirt

        #创建locator
        myName = mc.spaceLocator(p = (0,0,0), n = "%s_Loc" % obj)
        if addNoises:
            for key in ObjectDirt.keys():
                if int(key) >= 0 and int(key) < 3:
                    num1 = int(key)+1
                    mc.addAttr(myName[0], ln = ("Object%sSet"%str(num1)), dt = "string")
                    mc.setAttr("%s.Object%sSet"%(myName[0],str(num1)), e = True, keyable = True)
                    mc.setAttr("%s.Object%sSet"%(myName[0],str(num1)), ObjectDirt[key], type="string")
                elif int(key) >= 3 and int(key) < 6:
                    num1 = int(key)-2
                    mc.addAttr(myName[0], ln = ("StaticObject%sSet"%str(num1)), dt = "string")
                    mc.setAttr("%s.StaticObject%sSet"%(myName[0],str(num1)), e = True, keyable = True)
                    mc.setAttr("%s.StaticObject%sSet"%(myName[0],str(num1)), ObjectDirt[key], type="string")
                elif int(key) >= 6 and int(key) <11:
                    num1 = int(key)-5
                    mc.addAttr(myName[0], ln = ("wingman%sSet"%str(num1)), dt = "string")
                    mc.setAttr("%s.wingman%sSet"%(myName[0],str(num1)), e = True, keyable = True)
                    mc.setAttr("%s.wingman%sSet"%(myName[0],str(num1)), ObjectDirt[key], type="string")

            object1Edit = mc.getAttr("%s.houdiniAssetParm_objpath1"%obj)
            if object1Edit:
                mc.addAttr(myName[0], ln = "Object1Edit", dt = "string")
                mc.setAttr("%s.Object1Edit"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.Object1Edit"%myName[0], object1Edit, type="string") 

            object2Edit = mc.getAttr("%s.houdiniAssetParm_objpath2"%obj)
            if object2Edit:
                mc.addAttr(myName[0], ln = "Object2Edit", dt = "string")
                mc.setAttr("%s.Object2Edit"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.Object2Edit"%myName[0], object2Edit, type="string")

            object3Edit = mc.getAttr("%s.houdiniAssetParm_objpath3"%obj)
            if object2Edit:
                mc.addAttr(myName[0], ln = "Object3Edit", dt = "string")
                mc.setAttr("%s.Object3Edit"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.Object3Edit"%myName[0], object3Edit, type="string")

            parm_view_pivo = mc.getAttr("%s.houdiniAssetParm_view_pivot"%obj)
            mc.addAttr(myName[0], ln = "view_pivot", at = "bool")
            mc.setAttr("%s.view_pivot"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.view_pivot"%myName[0], parm_view_pivo)

            Pivot_Position = mc.getAttr("%s.houdiniAssetParm_Pivot_Position"%obj)
            mc.addAttr(myName[0], ln = "Pivot_Position", en = "Top:Bottom", at = "enum")
            mc.setAttr("%s.Pivot_Position"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Pivot_Position"%myName[0], Pivot_Position)

            Pivot__tuple0 = mc.getAttr("%s.houdiniAssetParm_Translate_Pivot__tuple0"%obj)
            Pivot__tuple1 = mc.getAttr("%s.houdiniAssetParm_Translate_Pivot__tuple1"%obj)
            Pivot__tuple2 = mc.getAttr("%s.houdiniAssetParm_Translate_Pivot__tuple2"%obj)
            mc.addAttr(myName[0], ln = "Translate_Pivot", at = "double3")
            mc.addAttr(myName[0], ln = "Translate_PivotX", at = "double", p = "Translate_Pivot")
            mc.addAttr(myName[0], ln = "Translate_PivotY", at = "double", p = "Translate_Pivot")
            mc.addAttr(myName[0], ln = "Translate_PivotZ", at = "double", p = "Translate_Pivot")
            mc.setAttr("%s.Translate_Pivot"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Translate_PivotX"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Translate_PivotY"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Translate_PivotZ"%myName[0], e = True, keyable = True)

            mc.setAttr("%s.Translate_PivotX"%myName[0], Pivot__tuple0)
            mc.setAttr("%s.Translate_PivotY"%myName[0], Pivot__tuple1)
            mc.setAttr("%s.Translate_PivotZ"%myName[0], Pivot__tuple2)

            Parm_freq0 = mc.getAttr("%s.houdiniAssetParm_freq__tuple0"%obj)
            Parm_freq1 = mc.getAttr("%s.houdiniAssetParm_freq__tuple1"%obj)
            Parm_freq2 = mc.getAttr("%s.houdiniAssetParm_freq__tuple2"%obj)
            mc.addAttr(myName[0], ln = "Frequency", at = "double3")
            mc.addAttr(myName[0], ln = "FrequencyX", at = "double", p = "Frequency")
            mc.addAttr(myName[0], ln = "FrequencyY", at = "double", p = "Frequency")
            mc.addAttr(myName[0], ln = "FrequencyZ", at = "double", p = "Frequency")
            mc.setAttr("%s.Frequency"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.FrequencyX"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.FrequencyY"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.FrequencyZ"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.FrequencyX"%myName[0], Parm_freq0)
            mc.setAttr("%s.FrequencyY"%myName[0], Parm_freq1)
            mc.setAttr("%s.FrequencyZ"%myName[0], Parm_freq2)

            offset0 = mc.getAttr("%s.houdiniAssetParm_offset__tuple0"%obj)
            offset1 = mc.getAttr("%s.houdiniAssetParm_offset__tuple1"%obj)
            offset2 = mc.getAttr("%s.houdiniAssetParm_offset__tuple2"%obj)
            mc.addAttr(myName[0], ln = "Offset", at = "double3")
            mc.addAttr(myName[0], ln = "OffsetX", at = "double", p = "Offset")
            mc.addAttr(myName[0], ln = "OffsetY", at = "double", p = "Offset")
            mc.addAttr(myName[0], ln = "OffsetZ", at = "double", p = "Offset")
            mc.setAttr("%s.Offset"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.OffsetX"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.OffsetY"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.OffsetZ"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.OffsetX"%myName[0], offset0)
            mc.setAttr("%s.OffsetY"%myName[0], offset1)
            mc.setAttr("%s.OffsetZ"%myName[0], offset2)

            Parm_rough = mc.getAttr("%s.houdiniAssetParm_rough"%obj)
            mc.addAttr(myName[0], ln = "Roughness", at = "double", min = 0, max = 1, dv = Parm_rough)
            mc.setAttr("%s.Roughness"%myName[0], e = True, keyable = True)

            noisetype = mc.getAttr("%s.houdiniAssetParm_noisetype"%obj)
            mc.addAttr(myName[0], ln = "noiseType", en = "Perlin:Simplex", at = "enum")
            mc.setAttr("%s.noiseType"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.noiseType"%myName[0], noisetype)


            Direction0 = mc.getAttr("%s.houdiniAssetParm_Direction__tuple0"%obj)
            Direction1 = mc.getAttr("%s.houdiniAssetParm_Direction__tuple1"%obj)
            Direction2 = mc.getAttr("%s.houdiniAssetParm_Direction__tuple2"%obj)
            mc.addAttr(myName[0], ln = "Direction", at = "double3")
            mc.addAttr(myName[0], ln = "DirectionX", at = "double", p = "Direction")
            mc.addAttr(myName[0], ln = "DirectionY", at = "double", p = "Direction")
            mc.addAttr(myName[0], ln = "DirectionZ", at = "double", p = "Direction")
            mc.setAttr("%s.Direction"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.DirectionX"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.DirectionY"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.DirectionZ"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.DirectionX"%myName[0], Direction0)
            mc.setAttr("%s.DirectionY"%myName[0], Direction1)
            mc.setAttr("%s.DirectionZ"%myName[0], Direction2)

            speed = mc.getAttr("%s.houdiniAssetParm_Speed"%obj)
            mc.addAttr(myName[0], ln = "Speed", at = "double", min = 0, max = 2, dv = speed)
            mc.setAttr("%s.Speed"%myName[0], e = True, keyable = True)

            scale = mc.getAttr("%s.houdiniAssetParm_scale2"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_scale2", nn = "scale", at = "double", min = 0, max = 10, dv = scale)
            mc.setAttr("%s.houdiniAssetParm_scale2"%myName[0], e = True, keyable = True)

            Amplitude_For_Direction = mc.getAttr("%s.houdiniAssetParm_Amplitude_For_Direction"%obj)
            mc.addAttr(myName[0], ln = "Amplitude_For_Direction", at = "double", min = 0, max = 50, dv = Amplitude_For_Direction)
            mc.setAttr("%s.Amplitude_For_Direction"%myName[0], e = True, keyable = True)

            Amplitude_For_No_Direction = mc.getAttr("%s.houdiniAssetParm_Amplitude_For_No_Direction"%obj)
            mc.addAttr(myName[0], ln = "Amplitude_For_No_Direction", at = "double", min = 0, max = 50, dv = Amplitude_For_No_Direction)
            mc.setAttr("%s.Amplitude_For_No_Direction"%myName[0], e = True, keyable = True)

            #deform
            Minimum_Value_In_Source_Range = mc.getAttr("%s.houdiniAssetParm_srcmin"%obj)
            mc.addAttr(myName[0], ln = "Minimum_Value_In_Source_Range", at = "double", dv = Minimum_Value_In_Source_Range)
            mc.setAttr("%s.Minimum_Value_In_Source_Range"%myName[0], e = True, keyable = True)

            Maximum_Value_In_Source_Range = mc.getAttr("%s.houdiniAssetParm_srcmax"%obj)
            mc.addAttr(myName[0], ln = "Maximum_Value_In_Source_Range", at = "double", min = 0, max = 50, dv = Maximum_Value_In_Source_Range)
            mc.setAttr("%s.Maximum_Value_In_Source_Range"%myName[0], e = True, keyable = True)


            Noise_Effect_Direction0 = mc.getAttr("%s.houdiniAssetParm_Noise_Effect_Direction__tuple0"%obj)
            Noise_Effect_Direction1 = mc.getAttr("%s.houdiniAssetParm_Noise_Effect_Direction__tuple1"%obj)
            Noise_Effect_Direction2 = mc.getAttr("%s.houdiniAssetParm_Noise_Effect_Direction__tuple2"%obj)
            mc.addAttr(myName[0], ln = "Noise_Effect_Direction", at = "double3")
            mc.addAttr(myName[0], ln = "Noise_Effect_DirectionX", at = "double", p = "Noise_Effect_Direction")
            mc.addAttr(myName[0], ln = "Noise_Effect_DirectionY", at = "double", p = "Noise_Effect_Direction")
            mc.addAttr(myName[0], ln = "Noise_Effect_DirectionZ", at = "double", p = "Noise_Effect_Direction")
            mc.setAttr("%s.Noise_Effect_Direction"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Noise_Effect_DirectionX"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Noise_Effect_DirectionY"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Noise_Effect_DirectionZ"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.Noise_Effect_DirectionX"%myName[0], Noise_Effect_Direction0)
            mc.setAttr("%s.Noise_Effect_DirectionY"%myName[0], Noise_Effect_Direction1)
            mc.setAttr("%s.Noise_Effect_DirectionZ"%myName[0], Noise_Effect_Direction2)

            Parm_freq4_0 = mc.getAttr("%s.houdiniAssetParm_freq4__tuple0"%obj)
            Parm_freq4_1 = mc.getAttr("%s.houdiniAssetParm_freq4__tuple1"%obj)
            Parm_freq4_2 = mc.getAttr("%s.houdiniAssetParm_freq4__tuple2"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_freq", nn = "Frequency", at = "double3")
            mc.addAttr(myName[0], ln = "houdiniAssetParm_freqX", at = "double", p = "houdiniAssetParm_freq")
            mc.addAttr(myName[0], ln = "houdiniAssetParm_freqY", at = "double", p = "houdiniAssetParm_freq")
            mc.addAttr(myName[0], ln = "houdiniAssetParm_freqZ", at = "double", p = "houdiniAssetParm_freq")
            mc.setAttr("%s.houdiniAssetParm_freq"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_freqX"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_freqY"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_freqZ"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_freqX"%myName[0], Parm_freq4_0)
            mc.setAttr("%s.houdiniAssetParm_freqY"%myName[0], Parm_freq4_1)
            mc.setAttr("%s.houdiniAssetParm_freqZ"%myName[0], Parm_freq4_2)

            Parm_offset4_0 = mc.getAttr("%s.houdiniAssetParm_offset4__tuple0"%obj)
            Parm_offset4_1 = mc.getAttr("%s.houdiniAssetParm_offset4__tuple1"%obj)
            Parm_offset4_2 = mc.getAttr("%s.houdiniAssetParm_offset4__tuple2"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_offset4", nn = "offset", at = "double3")
            mc.addAttr(myName[0], ln = "houdiniAssetParm_offset4X", at = "double", p = "houdiniAssetParm_offset4")
            mc.addAttr(myName[0], ln = "houdiniAssetParm_offset4Y", at = "double", p = "houdiniAssetParm_offset4")
            mc.addAttr(myName[0], ln = "houdiniAssetParm_offset4Z", at = "double", p = "houdiniAssetParm_offset4")
            mc.setAttr("%s.houdiniAssetParm_offset4"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_offset4X"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_offset4Y"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_offset4Z"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_offset4X"%myName[0], Parm_offset4_0)
            mc.setAttr("%s.houdiniAssetParm_offset4Y"%myName[0], Parm_offset4_1)
            mc.setAttr("%s.houdiniAssetParm_offset4Z"%myName[0], Parm_offset4_2)

            Amplitude = mc.getAttr("%s.houdiniAssetParm_amp"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_amp", nn = "Amplitude", at = "double", min = -1, max = 1, dv = Amplitude)
            mc.setAttr("%s.houdiniAssetParm_amp"%myName[0], e = True, keyable = True)

            Parm_rough2 = mc.getAttr("%s.houdiniAssetParm_rough2"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_rough2", nn = "Roughness", at = "double", min = 0, max = 1, dv = Parm_rough2)
            mc.setAttr("%s.houdiniAssetParm_rough2"%myName[0], e = True, keyable = True)

            flowrate2 = mc.getAttr("%s.houdiniAssetParm_flowrate2"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_flowrate2", nn = "Flow_Rate", at = "double", min = -1, max = 1, dv = flowrate2)
            mc.setAttr("%s.houdiniAssetParm_flowrate2"%myName[0], e = True, keyable = True)

            #static Object
            StaticObject1 = mc.getAttr("%s.houdiniAssetParm_Static_Object_1"%obj)
            if StaticObject1:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_Static_Object_1", nn ="Static_Object_1", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_Static_Object_1"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_Static_Object_1"%myName[0], StaticObject1, type="string") 

            StaticObject2 = mc.getAttr("%s.houdiniAssetParm_Static_Object_2"%obj)
            if StaticObject2:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_Static_Object_2", nn ="Static_Object_2", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_Static_Object_2"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_Static_Object_2"%myName[0], StaticObject2, type="string") 

            StaticObject3 = mc.getAttr("%s.houdiniAssetParm_Static_Object_3"%obj)
            if StaticObject3:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_Static_Object_3", nn ="Static_Object_3", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_Static_Object_3"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_Static_Object_3"%myName[0], StaticObject3, type="string") 

            Parm_radius = mc.getAttr("%s.houdiniAssetParm_radius"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_radius", nn = "search_radius", at = "double", min = 0, max = 10000, dv = Parm_radius)
            mc.setAttr("%s.houdiniAssetParm_radius"%myName[0], e = True, keyable = True)

            Distance = mc.getAttr("%s.houdiniAssetParm_Distance"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_Distance", nn = "Distance", at = "double", min = 0, max = 10000, dv = Distance)
            mc.setAttr("%s.houdiniAssetParm_Distance"%myName[0], e = True, keyable = True)
            
            #wingman
            Parm_type = mc.getAttr("%s.houdiniAssetParm_type"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_type", nn = "type", en = "none:rotate:rotate and deform", at = "enum")
            mc.setAttr("%s.houdiniAssetParm_type"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.houdiniAssetParm_type"%myName[0], Parm_type)

            wingman1 = mc.getAttr("%s.houdiniAssetParm_wingman1"%obj)
            if wingman1:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_wingman1", nn ="wingman1", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_wingman1"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_wingman1"%myName[0], wingman1, type="string") 

            wingman2 = mc.getAttr("%s.houdiniAssetParm_wingman2"%obj)
            if wingman2:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_wingman2", nn ="wingman2", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_wingman2"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_wingman2"%myName[0], wingman2, type="string")

            wingman3 = mc.getAttr("%s.houdiniAssetParm_wingman3"%obj)
            if wingman3:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_wingman3", nn ="wingman3", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_wingman3"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_wingman3"%myName[0], wingman3, type="string") 

            wingman4 = mc.getAttr("%s.houdiniAssetParm_wingman3"%obj)
            if wingman4:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_wingman4", nn ="wingman4", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_wingman4"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_wingman4"%myName[0], wingman4, type="string") 

            wingman5 = mc.getAttr("%s.houdiniAssetParm_wingman5"%obj)
            if wingman5:
                mc.addAttr(myName[0], ln = "houdiniAssetParm_wingman5", nn ="wingman5", dt = "string")
                mc.setAttr("%s.houdiniAssetParm_wingman5"%myName[0], e = True, keyable = True)
                mc.setAttr("%s.houdiniAssetParm_wingman5"%myName[0], wingman5, type="string") 

            Parm_radius2 = mc.getAttr("%s.houdiniAssetParm_radius2"%obj)
            mc.addAttr(myName[0], ln = "houdiniAssetParm_radius2", nn = "Radius for deform", at = "double", min = 0, max = 10000, dv = Parm_radius2)
            mc.setAttr("%s.houdiniAssetParm_radius2"%myName[0], e = True, keyable = True)
            
            assetName = mc.getAttr("%s.assetName"%obj)
            mc.addAttr(myName[0], ln = "assetName", nn="Asset_Type", dt = "string")
            mc.setAttr("%s.assetName"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.assetName"%myName[0], assetName, type="string")

            otlFilePath = mc.getAttr("%s.otlFilePath"%obj)
            mc.addAttr(myName[0], ln = "otlFilePath", nn="File_Path", dt = "string")
            mc.setAttr("%s.otlFilePath"%myName[0], e = True, keyable = True)
            mc.setAttr("%s.otlFilePath"%myName[0], otlFilePath, type="string")

            trans = mc.getAttr("%s.translate"%obj)[0]
            mc.setAttr("%s.translate"%myName[0], trans[0], trans[1], trans[2], type="double3")

            rotate = mc.getAttr("%s.rotate"%obj)[0]
            mc.setAttr("%s.rotate"%myName[0], rotate[0], rotate[1], rotate[2], type="double3")

            scale = mc.getAttr("%s.scale"%obj)[0]
            mc.setAttr("%s.scale"%myName[0], scale[0], scale[1], scale[2], type="double3")

            shearXY = mc.getAttr("%s.shearXY"%obj)
            mc.setAttr("%s.shearXY"%myName[0], shearXY)

            shearXZ = mc.getAttr("%s.shearXZ"%obj)
            mc.setAttr("%s.shearXZ"%myName[0], shearXZ)

            shearYZ = mc.getAttr("%s.shearYZ"%obj)
            mc.setAttr("%s.shearYZ"%myName[0], shearYZ)

        locatorObject.append(myName)
    mc.select(d = True)
    for loc in locatorObject:
        mc.select(loc, add = True)

    objPath = os.path.splitext(fileName)[0]+"_loc"
    mc.file(objPath, force = True, options = "", type = "FBX export", pr = True, es = True)

#CopyObjAttrbuteToLocator()



# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import string

def deleteNotOpacityMaterial():
    allShape=[]
    allMaterial = mc.ls(type=['blinn','lambert','phong','phongE','surfaceShader','aiStandard','VRayMtl'])
    for mater in allMaterial:
        transpImage=""
        try:
            transpImage=mc.listConnections("%s.transparency"%mater,s=True,d=False,plugs=True)
        except:
            pass
        if not transpImage:
            try:
                transpImage=mc.listConnections("%s.opacity"%mater,s=True,d=False,plugs=True)
            except:
                pass
        if not transpImage:
            try:
                transpImage=mc.listConnections("%s.outTransparency"%mater,s=True,d=False,plugs=True)
            except:
                pass
        if not transpImage:
            try:
                transpImage=mc.listConnections("%s.opacityMap"%mater,s=True,d=False,plugs=True)
            except:
                pass
        if not transpImage:
            if "lambert1" != mater:
                mc.delete(mater)

#判断maya物体是否按3
def findObjectSmoothness():
    allMeshs = []
    allSmoothness = []

    allSelObj = mc.ls(sl = True, dag = True, shapes = True)
    if not allSelObj:
        mc.confirmDialog(message = u"请选择物体！")
        return
    for obj in allSelObj:
        if mc.objectType(obj) == "mesh":
            allMeshs.append(obj)

    if allMeshs:
        for meshs in allMeshs:
            displaySms = mc.displaySmoothness(meshs,q= True, polygonObject = True)
            if displaySms:
                if displaySms[0] == 3:
                    allSmoothness.append(meshs)
               

    if allSmoothness:
        res = mc.confirmDialog(message = u"下列是所选物体按3的%s\n是否需要Smoothness\n 是 = Yes,否 = No\n"%allSmoothness, button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
        if res == 'Yes':
            for sm in allSmoothness:
                mc.polySmooth(sm, suv =1, dv = 2, ps = 0.1, ro = 1)
        else: 
            return
    
