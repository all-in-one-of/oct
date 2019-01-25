#!/usr/bin/python
# -*- coding: utf-8 -*- 
import maya.cmds as mc
import maya.mel as mm

class CreateArnoldOcean():
    def __init__(self):
        self._windowSize = (280, 260)
        self._windowName = 'OCT_CreateArnoldOcean_UI'

    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName, window=True)
        if mc.windowPref(self._windowName, q=True, exists=True):
            mc.windowPref(self._windowName, remove=True)

    def CreateArnoldOcean_UI(self):
        self.close()
        win = mc.window(self._windowName, t = u'创建海洋平面效果', menuBar=True, widthHeight=self._windowSize, sizeable=False)
        mc.rowColumnLayout( numberOfColumns=1, columnWidth=(1, 280), columnAlign = (1,'center'))
        mc.button('CreateDefor', l = u'创建水面预览', w = 60, h = 23, c = lambda *args:self.CreateDeformer())
    
        mc.optionMenuGrp('waterType', l = u'水面类型', h = 45)
        mc.menuItem(l = u'湖面')
        mc.menuItem(l = u'海面')
        mc.menuItem(l = u'河面')
        mc.menuItem(l = u'风暴')
        mc.menuItem(l = u'自定义')

        mc.button('setDefor', l = u'设置', h = 23, backgroundColor = (0.9,0.5,0), c = lambda *args:self.setDeformer())
        
        mc.text(l = '')
        mc.separator()
        mc.text(l = '')

        mc.button('CreateArShader', l = u'创建水面ArnoldShader', h = 23, c = lambda*args:self.CreateArnoldShader())
        
        mc.optionMenuGrp('ArnWaterType', l = u'水面类型', h = 45)
        mc.menuItem(l = u'湖面')
        mc.menuItem(l = u'海面')
        mc.menuItem(l = u'河面')
        mc.menuItem(l = u'风暴')
        mc.menuItem(l = u'拷贝预览')
        mc.menuItem(l = u'自定义')

        mc.button('setArnoldShader', l = u'设置', h = 23, backgroundColor = (0.9,0.5,0), c= lambda *args:self.setArnoldShader())

        mc.showWindow(win)

    #创建变形器
    def CreateDeformer(self):
        if not mc.pluginInfo('hotOceanDeformer.mll',q = True,l = True):
            mc.loadPlugin('hotOceanDeformer.mll')
        mc.polyPlane(n = 'OceanPreview', w = 20, h = 20, sx = 150, sy = 150, ax = [0, 1, 0], cuv = 2, ch = 1)
        mc.deformer(type = 'hotOceanDeformer')

    #创建arnold shader
    def CreateArnoldShader(self):
        if not mc.pluginInfo('mtoa.mll',q = True,l = True):
            mc.loadPlugin('mtoa.mll')

        planel = mc.ls(sl = True)
        if not planel:
            mc.confirmDialog(title=u"提示", message=u'请选择polyPlane！')
            return 

        for p in planel:
            try:
                mc.setAttr('%s.aiOpaque'%p, 0)
                mc.setAttr('%s.aiSubdivType'%p, 1)
                mc.setAttr('%s.aiSubdivIterations'%p, 4)
            except:
                pass

        seaShader = mc.shadingNode('aiStandard', asShader = True, n = 'seaShader')
        #seaSG = mc.shadingNode('shadingEngine', asShader = True, n = 'seaSG')
        seaSG = mc.sets(renderable = True, noSurfaceShader = True, empty = True, name = 'seaSG')
        mc.connectAttr('%s.outColor'%seaShader, '%s.surfaceShader'%seaSG, f = True)

        mc.select(planel)
        mc.sets(e = True, forceElement = seaSG)
        
        mc.setAttr('%s.color'%seaShader, 0, 0, 0, type = 'double3')
        mc.setAttr('%s.Kd'%seaShader, 0)
        mc.setAttr('%s.KsColor'%seaShader, 1, 1, 1, type = 'double3')
        mc.setAttr('%s.Ks'%seaShader, 0.5)
        mc.setAttr('%s.specularRoughness'%seaShader, 0)
        mc.setAttr('%s.specularFresnel'%seaShader, 1)
        mc.setAttr('%s.Ksn'%seaShader, 0.45)
        mc.setAttr('%s.Kt'%seaShader, 1)
        mc.setAttr('%s.IOR'%seaShader, 1.33)
        mc.setAttr('%s.opacity'%seaShader, 0.78, 0.78, 0.78, type = 'double3')

        seaDeform = mc.shadingNode('Ocean_Octvision', asShader = True, n = 'Ocean_Octvision')
        disShader = mc.shadingNode('displacementShader', asShader = True, n = 'OceanDisplacement')
        mc.connectAttr('%s.outColor'%seaDeform, '%s.vectorDisplacement'%disShader, f = True)
        mc.connectAttr('%s.displacement'%disShader, '%s.displacementShader'%seaSG, f = True)
        mc.expression(s = '%s.time = 0.5*time;'%seaDeform, o = seaDeform, ae = True, uc = all)

    def setDeformer(self):
        waterType = mc.optionMenuGrp('waterType', q = True, v = True)
        OceanDeformer = mc.ls(type = 'hotOceanDeformer')
        if not OceanDeformer:
            mc.confirmDialog(title=u"提示", message=u'没有找到hotOceanDeformer变形器！')
            return 
        if waterType == u'湖面':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 1)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 10)
                mc.setAttr('%s.windSpeed'%deform, 1.618)
                mc.setAttr('%s.waveHeight'%deform, 0.06)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 2)
                mc.setAttr('%s.windDirection'%deform, 45)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 5)
           
        elif waterType == u'河面':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 2)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 10)
                mc.setAttr('%s.windSpeed'%deform, 1.618)
                mc.setAttr('%s.waveHeight'%deform, 0.08)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 1.5)
                mc.setAttr('%s.windDirection'%deform, 45)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 6.5)

        elif waterType == u'海面':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 1)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 20)
                mc.setAttr('%s.windSpeed'%deform, 3.07)
                mc.setAttr('%s.waveHeight'%deform, 0.3)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 1)
                mc.setAttr('%s.windDirection'%deform, 45)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 6.5)

        elif waterType == u'风暴':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 1)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 100)
                mc.setAttr('%s.windSpeed'%deform, 12.9)
                mc.setAttr('%s.waveHeight'%deform, 5)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 0.7)
                mc.setAttr('%s.windDirection'%deform, 25)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 6.5)
        # elif waterType == u'自定义':
        #     mc.select(OceanDeformer)
        mc.select(OceanDeformer)

    def setArnoldShader(self):
        waterType = mc.optionMenuGrp('ArnWaterType', q = True, v = True)
        OceanDeformer = mc.ls(type = 'Ocean_Octvision')
        if not OceanDeformer:
            mc.confirmDialog(title=u"提示", message=u'没有找到Ocean_Octvision类型节点！')
            return 
        if waterType == u'湖面':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 1)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 10)
                mc.setAttr('%s.windSpeed'%deform, 1.618)
                mc.setAttr('%s.waveHeight'%deform, 0.06)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 2)
                mc.setAttr('%s.windDirection'%deform, 45)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 5)
           
        elif waterType == u'河面':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 2)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 10)
                mc.setAttr('%s.windSpeed'%deform, 1.618)
                mc.setAttr('%s.waveHeight'%deform, 0.08)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 1.5)
                mc.setAttr('%s.windDirection'%deform, 45)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 6.5)

        elif waterType == u'海面':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 1)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 20)
                mc.setAttr('%s.windSpeed'%deform, 3.07)
                mc.setAttr('%s.waveHeight'%deform, 0.3)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 1)
                mc.setAttr('%s.windDirection'%deform, 45)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 6.5)

        elif waterType == u'风暴':
            for deform in OceanDeformer:
                mc.setAttr('%s.globalScale'%deform, 1)
                mc.setAttr('%s.resolution'%deform, 8)
                mc.setAttr('%s.size'%deform, 100)
                mc.setAttr('%s.windSpeed'%deform, 12.9)
                mc.setAttr('%s.waveHeight'%deform, 5)
                mc.setAttr('%s.shortestWave'%deform, 0.001)
                mc.setAttr('%s.choppiness'%deform, 0.7)
                mc.setAttr('%s.windDirection'%deform, 25)
                mc.setAttr('%s.dampReflections'%deform, 0.75)
                mc.setAttr('%s.windAlign'%deform, 6.5)

        elif waterType == u'拷贝预览':
            selOceanDef0r = mc.ls(sl = True, dag = True, s = True, ni = True)
            deforName = ''
            Ocean_OctvisionName = ''
            if len(selOceanDef0r) != 2:
                mc.confirmDialog(title=u"提示", message=u'请先选择连接变形器的面,再选择连接Ocean_Octvision的面')
                return   

            deformer = mc.listConnections('%s.inMesh' % selOceanDef0r[0])
            for defor in deformer:
                if mc.objectType(defor) == 'hotOceanDeformer':
                    deforName = defor

            if not deforName:
                mc.confirmDialog(title=u"提示", message=u'请先选择连接变形器的面,再选择连接Ocean_Octvision的面')
                return


            arnoldSGN = ''

            arnoldSGNames = mc.listConnections('%s.instObjGroups' % selOceanDef0r[1])
            if arnoldSGNames:
                for arnoldSG in arnoldSGNames:
                    if mc.objectType(arnoldSG) == 'shadingEngine':
                        arnoldSGN = arnoldSG

            OceanDisName = ''
            if arnoldSGN:
                OceanDisplacements = mc.listConnections('%s.displacementShader'%arnoldSGN)
                if OceanDisplacements:
                    for disp in OceanDisplacements:
                        if mc.objectType(disp) == 'displacementShader':
                            OceanDisName = disp

            if OceanDisName:
                Ocean_Octvisions = mc.listConnections('%s.vectorDisplacement'%OceanDisName)
                if Ocean_Octvisions:
                    for Ocean in Ocean_Octvisions:
                        if mc.objectType(Ocean) == 'Ocean_Octvision':
                            Ocean_OctvisionName = Ocean
            if not Ocean_OctvisionName:
                mc.confirmDialog(title=u"提示", message=u'请先选择连接变形器的面,再选择连接Ocean_Octvision的面')
                return

            
            globalScale = mc.getAttr('%s.globalScale' % deforName)
            resolution = mc.getAttr('%s.resolution' % deforName)
            size = mc.getAttr('%s.size' % deforName)
            windSpeed = mc.getAttr('%s.windSpeed' % deforName)
            waveHeight = mc.getAttr('%s.waveHeight' % deforName)
            shortestWave = mc.getAttr('%s.shortestWave'% deforName)
            choppiness = mc.getAttr('%s.choppiness'% deforName)
            windDirection = mc.getAttr('%s.windDirection'% deforName)
            dampReflections = mc.getAttr('%s.dampReflections'% deforName)
            windAlign = mc.getAttr('%s.windAlign'% deforName)

            mc.setAttr('%s.globalScale'%Ocean_OctvisionName, globalScale)
            mc.setAttr('%s.resolution'%Ocean_OctvisionName, resolution)
            mc.setAttr('%s.size'%Ocean_OctvisionName, size)
            mc.setAttr('%s.windSpeed'%Ocean_OctvisionName, windSpeed)
            mc.setAttr('%s.waveHeight'%Ocean_OctvisionName, waveHeight)
            mc.setAttr('%s.shortestWave'%Ocean_OctvisionName, shortestWave)
            mc.setAttr('%s.choppiness'%Ocean_OctvisionName, choppiness)
            mc.setAttr('%s.windDirection'%Ocean_OctvisionName, windDirection)
            mc.setAttr('%s.dampReflections'%Ocean_OctvisionName, dampReflections)
            mc.setAttr('%s.windAlign'%Ocean_OctvisionName, windAlign)

        # elif waterType == u'自定义':
        #     mc.select(OceanDeformer)
        mc.select(OceanDeformer)

#CreateArnoldOcean().CreateArnoldOcean_UI()

