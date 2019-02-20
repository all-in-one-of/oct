# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import math

def setExpForCurve_zwz(cameraShape,curveShape):
    mc.expression(s = u"//获取底片大小\nfloat $chA = %s.horizontalFilmAperture*2.5399999999999999;\nfloat $cvA = %s.verticalFilmAperture*2.5399999999999999;\n//获取偏移值大小\nfloat $chO = %s.horizontalFilmOffset*2.5399999999999999;\nfloat $cvO = %s.verticalFilmOffset*2.5399999999999999;\n//取相应比例值\nfloat $chAOCompare = $chO/$chA;\nfloat $cvAOCompare = $cvO/$cvA;\n//获取摄像机焦距\nfloat $original_f = %s.focalLength/10;\n//获取1MM处的物体距离\nfloat $aovx = atan2($chA/2,$original_f);\nfloat $aovy = atan2($cvA/2,$original_f);\n//计算X轴的左右距离\nfloat $pointBXLV = tan($aovx)*($chAOCompare*2+1);\nfloat $pointBXRV = tan($aovx)*(-$chAOCompare*2+1);\n//计算Y轴的左右距离\nfloat $pointBYUV = tan($aovy)*($cvAOCompare*2+1);\nfloat $pointBYDV = tan($aovy)*(-$cvAOCompare*2+1);\n//编辑9个点的值\n%s.controlPoints[0].xValue = $pointBXLV;\n%s.controlPoints[0].yValue = $pointBYUV;\n%s.controlPoints[0].zValue = -1;\n%s.controlPoints[3].xValue = $pointBXLV;\n%s.controlPoints[3].yValue = $pointBYUV;\n%s.controlPoints[3].zValue = -1;\n\n%s.controlPoints[2].xValue = -$pointBXRV;\n%s.controlPoints[2].yValue = $pointBYUV;\n%s.controlPoints[2].zValue = -1;\n%s.controlPoints[9].xValue = -$pointBXRV;\n%s.controlPoints[9].yValue = $pointBYUV;\n%s.controlPoints[9].zValue = -1;\n \n%s.controlPoints[4].xValue = $pointBXLV;\n%s.controlPoints[4].yValue = -$pointBYDV;\n%s.controlPoints[4].zValue = -1;\n%s.controlPoints[7].xValue = $pointBXLV;\n%s.controlPoints[7].yValue = -$pointBYDV;\n%s.controlPoints[7].zValue = -1;\n \n%s.controlPoints[6].xValue = -$pointBXRV;\n%s.controlPoints[6].yValue = -$pointBYDV;\n%s.controlPoints[6].zValue = -1;\n%s.controlPoints[8].xValue = -$pointBXRV;\n%s.controlPoints[8].yValue = -$pointBYDV;\n%s.controlPoints[8].zValue = -1;\n\n%s.controlPoints[1].xValue = 0;\n%s.controlPoints[1].yValue = 0;\n%s.controlPoints[1].zValue = 0;\n%s.controlPoints[5].xValue = 0;\n%s.controlPoints[5].yValue = 0;\n%s.controlPoints[5].zValue = 0; \n%s.controlPoints[10].xValue = ($pointBXLV-$pointBXRV)/2;\n%s.controlPoints[10].yValue = ($pointBYUV-$pointBYDV)/2;\n%s.controlPoints[10].zValue = -1; \n%s.controlPoints[11].xValue = 0;\n%s.controlPoints[11].yValue = 0;\n%s.controlPoints[11].zValue = 0;" \
                      %(cameraShape,cameraShape,cameraShape,cameraShape,cameraShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape,curveShape), \
                  o='%s'%curveShape,ae=True,uc=all)
def OCT_CmeraCurves_zwz():
    if mc.objExists('allCameraCurves'):
        mc.delete('allCameraCurves')
    mc.confirmDialog( title=u'温馨提示：', message=u'线框只与摄像机关联，未与渲染尺寸关联\n请把渲染尺寸比列匹配摄像机底片比列！', button=['OK'], defaultButton='Yes', dismissString='No')
    allCameras = mc.listCameras( p=True )
    allCameraCurves = []
    for Camera in allCameras:
        cameraShape = mc.listRelatives(Camera,pa=True)
        if cameraShape != None and cameraShape[0] != 'perspShape':
            newCurve = mc.curve(n='%s_curve'%Camera,d = 1,p=[(0,0,0),(0,0,-1),(0,0,-2),(0,0,-3),(0,0,-4),(0,0,-5),(0,0,-6),(0,0,-7),(0,0,-8),(0,0,-9),(0,0,-10),(0,0,-11)])
            curveShape = mc.listRelatives(newCurve)
            setExpForCurve_zwz(str(cameraShape[0]),str(curveShape[0]))
            cameraWs = mc.xform(Camera,q=True,ws=True,t=True)
            cameraWr = mc.xform(Camera,q=True,ws=True,ro=True)
            mc.select(newCurve)
            mc.move(cameraWs[0],cameraWs[1],cameraWs[2],newCurve,r = True)
            mc.xform(newCurve,r=True, ro=(cameraWr[0],cameraWr[1],cameraWr[2]))
            mc.parentConstraint(Camera,newCurve, mo=True,w=True)
            allCameraCurves.append(newCurve)
    mc.group(allCameraCurves,n='allCameraCurves')
    mc.xform('allCameraCurves',r=True, s=(10,10,10))
