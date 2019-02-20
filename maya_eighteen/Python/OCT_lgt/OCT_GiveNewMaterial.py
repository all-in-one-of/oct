# -*- coding: utf-8 -*-


import maya.cmds as mc
import string
import maya.OpenMaya as om

#给物体赋labert材质并带有透明贴图
class GetObjectNewMaterial():

    def __init__(self):
        self.allShadingEngine = ""
        self.allMaterial = []
        self.defaultMaterial = ""
        self.notTransparency = []

    def getAllMaterial(self):
        self.allShadingEngine = mc.ls(type = "shadingEngine")
        for shading in self.allShadingEngine:
            if shading != "initialParticleSE" and shading != "initialShadingGroup":
                conn = mc.listConnections("%s.surfaceShader"%shading)
                if conn:
                    self.allMaterial.append(conn[0])
            elif shading == "initialShadingGroup":
                conn = mc.listConnections("%s.surfaceShader"%shading)
                self.defaultMaterial = conn[0]

        self.lambertShader()

    def lambertShader(self):
        #所有材质判断是否带透明贴图，换材质
        for mater in self.allMaterial:
            transp = ""
            try:
                transp = mc.listConnections("%s.transparency"%mater, s = True, d = False, plugs = True)[0]
            except:
                pass
            try:
                transp = mc.listConnections("%s.opacity"%mater, s = True, d = False, plugs =True)[0]
            except:
                pass
            try:
                transp = mc.listConnections("%s.opacityMap"%mater, s = True, d = True, plugs =True)[0]
            except:
                pass

            if transp:
                try:
                    mc.disconnectAttr(transp,"%s.transparency"%mater)
                except:
                    pass
                try:
                    mc.disconnectAttr(transp,"%s.opacity"%mater)
                except:
                    pass
                try:
                    mc.disconnectAttr(transp,"%s.opacityMap"%mater)
                except:
                    pass
                print transp
                print
                lambertShader = mc.shadingNode("lambert", asShader=True)
                tran=transp.split(".")[0]
                mc.connectAttr("%s.outColor"%tran, "%s.transparency"%lambertShader, f=True)

                connections = mc.listConnections(mater, s = False, d =True, connections = True, plugs = True)
                if connections:
                    for i in range(0,len(connections),2):
                        origPlug = connections[i]
                        dstPlug = connections[i+1]
                        replacePlug = string.replace(origPlug, mater, lambertShader)
                        try:
                            mc.disconnectAttr(origPlug, dstPlug)
                            mc.connectAttr(replacePlug, dstPlug)
                        except:
                            om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug, replacePlug))
            else:
                self.notTransparency.append(mater)
        #不带透明贴图的材质
        if self.notTransparency:
            lambertShader = mc.shadingNode("lambert", asShader=True)
            for mater in self.notTransparency:
                connections = mc.listConnections(mater, s = False, d =True, connections = True, plugs = True)
                if connections:
                    for i in range(0, len(connections), 2):
                        origPlug = connections[i]
                        dstPlug = connections[i+1]
                        replacePlug = string.replace(origPlug, mater, lambertShader)
            
                        try:
                            mc.disconnectAttr(origPlug, dstPlug)
                            mc.connectAttr(replacePlug, dstPlug)
                        except:
                            om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))

        if self.defaultMaterial:
            lambertShader = mc.shadingNode("lambert",asShader=True)
            lambertShaderSG=mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(lambertShader+"SG"))
            try:
                mc.hyperShade(objects=self.defaultMaterial)
                mc.hyperShade(assign=lambertShader)
            except:
                pass

