# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
class ArnoldProduction():
    def __init__(self):
        pass
    def ProductionType(self,attr):
        # allObjects=mc.ls(sl=True)
        allObjects = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
        getoptionMenuGrpValue=mc.optionMenuGrp(attr,q=True,v=True)
        for obj in allObjects:
            if getoptionMenuGrpValue=="none":
                mc.setAttr("%s.aiSubdivType"%obj,0)
            elif getoptionMenuGrpValue=="catclart":
                mc.setAttr("%s.aiSubdivType"%obj,1)
            elif getoptionMenuGrpValue=="linear":
                mc.setAttr("%s.aiSubdivType"%obj,2)
            elif getoptionMenuGrpValue=="auto":
                mc.setAttr("%s.aiSubdivAdaptiveMetric"%obj,0)
            elif getoptionMenuGrpValue=="edge_length":
                mc.setAttr("%s.aiSubdivAdaptiveMetric"%obj,1)
            elif getoptionMenuGrpValue=="flatness":
                mc.setAttr("%s.aiSubdivAdaptiveMetric"%obj,2)
            elif getoptionMenuGrpValue=="pin_corners":
                mc.setAttr("%s.aiSubdivUvSmoothing"%obj,0)
            elif getoptionMenuGrpValue=="pin_borders":
                mc.setAttr("%s.aiSubdivUvSmoothing"%obj,1)
            elif getoptionMenuGrpValue=="linears":
                mc.setAttr("%s.aiSubdivUvSmoothing"%obj,2)
            elif getoptionMenuGrpValue=="smooth":
                mc.setAttr("%s.aiSubdivUvSmoothing"%obj,3)
            elif getoptionMenuGrpValue == "mesh_light":
                mc.setAttr("%s.ai_translator"%obj, 'mesh_light', type = 'string')
            elif getoptionMenuGrpValue == "polymesh":
                mc.setAttr("%s.ai_translator"%obj, 'polymesh', type = 'string')
            elif getoptionMenuGrpValue == "procedural":
                mc.setAttr("%s.ai_translator"%obj, 'procedural', type = 'string')
            elif getoptionMenuGrpValue == "constant":
                mc.setAttr('%s.aiDecayType'%obj, 0)
            elif getoptionMenuGrpValue == 'quadratic':
                mc.setAttr('%s.aiDecayType'%obj, 1)
                
                
    def ProductionIterations(self,attr):
        # allObjects=mc.ls(sl=True)
        # print attr
        # updateAttrValue=mc.floatSliderButtonGrp(attr,q=True,v=True)
        # for obj in allObjects:
        #     mc.setAttr("%s.%s"%(obj,attr),updateAttrValue)
        updateAttrValue=mc.floatSliderButtonGrp(attr,q=True,v=True)
        allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
        for obj in allShapes:
            mc.setAttr("%s.%s"%(obj,attr),updateAttrValue)

    def updateArnoldAttrCheckBox(self,attr):
        #allObjects=mc.ls(sl=True)
        allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
        updateAttrValue=mc.checkBox(attr,q=True,v=True)
        for obj in allShapes:
            mc.setAttr("%s.%s"%(obj,attr),updateAttrValue)
        # for obj in allObjects:
        #     print obj
        #     item_shape = mc.listRelatives(obj, s=True)
        #     print item_shape
        #     try:
        #         mc.setAttr("%s.%s"%(item_shape[0],attr),updateAttrValue)
        #     except:
        #         pass
            
    def updateFloatFieldAttr(self, attr):
        allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
        updateAttrValue = mc.floatField(attr,q=True,v=True)
        for obj in allShapes:
            mc.setAttr("%s.%s"%(obj,attr),updateAttrValue)

    def updateColorAttr(self, attr):
        allShapes = mc.ls(selection = True, dagObjects = True, ni = True, shapes = True, rq = True)
        updateAttrValue = mc.colorSliderButtonGrp(attr, q = True, rgb = True)
        for obj in allShapes:
            mc.setAttr('%s.%s'%(obj, attr), updateAttrValue[0], updateAttrValue[1], updateAttrValue[2])

    def arnoldProductionUI(self):
        if mc.window("arnoldProductionUI",ex=True):
            mc.deleteUI("arnoldProductionUI")
        mc.window("arnoldProductionUI",tlc=[180,200],wh=[430,400],menuBar=True,title=u"arnold模型属性修改",sizeable=False)
        mc.scrollLayout("A",hst=0,vst=8)
        mc.columnLayout(adjustableColumn=True)

        mc.rowLayout(nc=2,cw=[(1, 344),(2, 200)])
        mc.checkBox("aiSelfShadows",v=True,label="Self Shadows",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiSelfShadows"))
        mc.setParent("..")
       
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiOpaque",v=True,label="Opaque",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiOpaque"))
        mc.setParent("..")
       
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiVisibleInDiffuse",v=True,label="Visible In Diffuse",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiVisibleInDiffuse"))
        mc.setParent("..")
       

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiVisibleInGlossy",v=True,label="Visible In Glossy",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiVisibleInGlossy"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiExportTangents",v=True,label="Export Tangents",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiExportTangents"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiExportColors",v=True,label="Export Vertex Colors",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiExportColors"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiExportRefPoints",v=True,label="Export Reference Points",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiExportRefPoints"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiExportRefNormals",v=True,label="Export Reference Normals",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiExportRefNormals"))
        mc.setParent("..")
 
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiExportRefTangents",v=True,label="Export Reference Tangents",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiExportRefTangents"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiExportRefTangents",v=True,label="Export Reference Tangents",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiExportRefTangents"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiMatte",v=True,label="Matte",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiMatte"))
        mc.setParent("..")

        mc.separator()

        mc.text("Subdivision")
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.optionMenuGrp("Type",l="Type",h=20)
        mc.menuItem(l="none")
        mc.menuItem(l="catclart")
        mc.menuItem(l="linear")
        mc.button(l="UPDATE",c=lambda *args:self.ProductionType("Type"))
        mc.setParent("..")
        mc.floatSliderButtonGrp("aiSubdivIterations",en=True,pre=0,label="Iterations",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)],min=0,max=10,fieldMaxValue=1,bc=lambda *args:self.ProductionIterations("aiSubdivIterations"))
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.optionMenuGrp("AdaptiveMetric",l="Adaptive Metric",h=20)
        mc.menuItem(l = "auto")
        mc.menuItem(l = "edge_length")
        mc.menuItem(l = "flatness")
        mc.button(l="UPDATE",c=lambda *args:self.ProductionType("AdaptiveMetric"))
        mc.setParent("..")
        mc.floatSliderButtonGrp("aiSubdivPixelError",en=True,pre=3,label="Pixel Error",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)],min=0,max=10,fieldMaxValue=1,bc=lambda *args:self.ProductionIterations("aiSubdivPixelError"))
        
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.optionMenuGrp("aiExportRefTangents",l="UV Smoothing",h=20)
        mc.menuItem(l="pin_corners")
        mc.menuItem(l="pin_borders")
        mc.menuItem(l="linears")
        mc.menuItem(l="smooth")
        mc.button(l="UPDATE",c=lambda *args:self.ProductionType("aiExportRefTangents"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiSubdivSmoothDerivs",v=True,label="SmoothTangents",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiSubdivSmoothDerivs"))
        mc.setParent("..")

        mc.separator()

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.optionMenuGrp("ArnoldTranslatoer",l="Arnold Translatoer",h=20)
        mc.menuItem(l = "mesh_light")
        mc.menuItem(l = "polymesh")
        mc.menuItem(l = "procedural")
        mc.button(l="UPDATE",c=lambda *args:self.ProductionType("ArnoldTranslatoer"))
        mc.setParent("..")

        mc.colorSliderButtonGrp('color', l = 'Color', buttonLabel = 'UPDATE', rgb = [0, 0, 0], symbolButtonDisplay = True, cw = [(1, 80), (2, 50), (3, 180)], bc = lambda *args:self.updateColorAttr('color'))
     
        mc.rowLayout(nc = 3,cw=[(1,46),(2,296),(3,200)])
        mc.text(l = "intensity")
        mc.floatField("intensity", precision = 3)
        mc.button(l= "UPDATE", c=lambda *args:self.updateFloatFieldAttr("intensity"))
        mc.setParent("..")

        mc.floatSliderButtonGrp("aiExposure", en=True, pre=0, min = -5, max = 5, label="aiExposure",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiExposure"))
        
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiUseColorTemperature",v=True,label="Use Color Temperature",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiUseColorTemperature"))
        mc.setParent("..")

        mc.floatSliderButtonGrp("aiColorTemperature", en=True, pre=0, min = 1000, max = 15000, label="Temperature",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiColorTemperature"))
       
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("emitDiffuse",v=True,label="Emit Diffuse",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("emitDiffuse"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("emitSpecular",v=True,label="Emit Specular",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("emitSpecular"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.optionMenuGrp("DecayType",l="Decay Type",h=20)
        mc.menuItem(l = "constant")
        mc.menuItem(l = "quadratic")
        mc.button(l="UPDATE",c=lambda *args:self.ProductionType("DecayType"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("lightVisible",v=True,label="Light Visible",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("lightVisible"))
        mc.setParent("..")

        mc.rowLayout(nc = 3,cw=[(1,46),(2,296),(3,200)])
        mc.text(l = "Samples")
        mc.floatField("aiSamples", precision = 0)
        mc.button(l= "UPDATE", c=lambda *args:self.updateFloatFieldAttr("aiSamples"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiNormalize",v=True,label="Normalize",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiNormalize"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiCastShadows",v=True,label="Cast Shadows",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiCastShadows"))
        mc.setParent("..")

        mc.floatSliderButtonGrp("aiShadowDensity", en=True, pre=3, min = 0, max = 1, label="Shadow Density",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiShadowDensity"))

        mc.colorSliderButtonGrp('aiShadowColor', l = 'Shadow Color', buttonLabel = 'UPDATE', rgb = [0, 0, 0], symbolButtonDisplay = True, cw = [(1, 80), (2, 50), (3, 180)], bc = lambda *args:self.updateColorAttr('aiShadowColor'))
        
        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiAffectVolumetrics",v=True,label="Affect Volumetrics",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiAffectVolumetrics"))
        mc.setParent("..")

        mc.rowLayout(nc=2,cw=[(1,344),(2,200)])
        mc.checkBox("aiCastVolumetricShadows",v=True,label="Cast Volumetric Shadows",align="right")
        mc.button(l="UPDATE",c=lambda *args:self.updateArnoldAttrCheckBox("aiCastVolumetricShadows"))
        mc.setParent("..")

        mc.rowLayout(nc = 3,cw=[(1,86),(2,256),(3,200)])
        mc.text(l = "Volume Samples")
        mc.floatField("aiVolumeSamples", precision = 0)
        mc.button(l= "UPDATE", c=lambda *args:self.updateFloatFieldAttr("aiVolumeSamples"))
        mc.setParent("..")

        mc.floatSliderButtonGrp("aiDiffuse", en=True, pre=3, min = 0, max = 1, label="Diffuse",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiDiffuse"))
        mc.floatSliderButtonGrp('aiSpecular', en = True, pre = 3, min = 0, max = 1, label = 'Specular', field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiSpecular"))
        mc.floatSliderButtonGrp('aiSss', en = True, pre = 3, min = 0, max = 1, label = 'SSS', field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiSss"))
        mc.floatSliderButtonGrp('aiIndirect', en = True, pre = 3, min = 0, max = 1, label = 'Indiret', field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiIndirect"))
        mc.floatSliderButtonGrp('aiVolume', en = True, pre = 3, min = 0, max = 1, label = 'Volume', field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=[(1,130),(2,50)], fieldMaxValue = 1, bc = lambda *args:self.ProductionIterations("aiVolume"))
        
        mc.rowLayout(nc = 3,cw=[(1,66),(2,276),(3,200)])
        mc.text(l = "Max Bounces")
        mc.floatField("aiMaxBounces", precision = 0, value = 999)
        mc.button(l= "UPDATE", c=lambda *args:self.updateFloatFieldAttr("aiMaxBounces"))
        mc.setParent("..")

        mc.showWindow("arnoldProductionUI")

# ArnoldProduction().arnoldProductionUI()
