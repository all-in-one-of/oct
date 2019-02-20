# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import string, sys

class materialChange(object):
    def __init__(self):
        pass
        
    def disconnectMaterialInfo(self,shaderNode):
        materialInfoNode = self.getMaterialInfo(shaderNode)
        if materialInfoNode == None:
            return

        mc.disconnectAttr(shaderNode + '.message',materialInfoNode + '.material')


    def getMaterialInfo(self,shaderNode):
        connections = mc.listConnections(shaderNode + '.message')
        if connections:
            for each in connections:
                if mc.objectType(each) == 'materialInfo':
                    return each

            return None

    def doReplace(self,origNode, replaceNode):
        origNode = origNode.encode()
        replaceNode = replaceNode.encode()


        origAttrs = mc.listAttr(origNode, scalar=True, multi=True, read=True, visible=True)
        
        replaceAttrs = mc.listAttr(replaceNode, scalar=True, multi=True, read=True, visible=True)
     
        for eachAttr in origAttrs:
            if eachAttr in replaceAttrs:
                value = mc.getAttr(origNode + '.' + eachAttr)
                try:
                    mc.setAttr(replaceNode + '.' + eachAttr,value)
                except:
                    om.MGlobal.displayWarning(u'Error in setting %s.%s attribute...Ignore this attribute!' % (replaceNode,eachAttr))

        origNodeType=mc.nodeType(origNode)
        replaceNodeType=mc.nodeType(replaceNode)

        if replaceNodeType=="aiStandard" and (origNodeType=="blinn" or origNodeType=="lambert" or origNodeType=="phong" or origNodeType=="phongE" or origNodeType=="mia_material" or origNodeType=="mia_material_x" or origNodeType=="anisotropic"):
            try:
                if origNodeType=="mia_material" or origNodeType=="mia_material_x":
                    eachAttr=mc.getAttr(origNode+".diffuse")
                    mc.setAttr(replaceNode+".color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                    eachAttr=mc.getAttr(origNode+".refl_color")
                    mc.setAttr(replaceNode+".KsColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                    
                    eachAttr=mc.getAttr(origNode+".reflectivity")
                    mc.setAttr(replaceNode+".Kr",eachAttr)

                else:
                    eachAttr=mc.getAttr(origNode+".color")
                    mc.setAttr(replaceNode+".color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                    eachAttr=mc.getAttr(origNode+".transparency")
                    mc.setAttr(replaceNode+".opacity",(1-eachAttr[0][0]),(1-eachAttr[0][1]),(1-eachAttr[0][2]),type="double3")

                    #eachAttr=mc.getAttr(origNode+".incandescence")
                    #mc.setAttr(replaceNode+".emissionColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                    if origNodeType=="blinn":
                        eachAttr=mc.getAttr(origNode+".diffuse")
                        mc.setAttr(replaceNode+".Kd",eachAttr)

                        eachAttr=mc.getAttr(origNode+".specularRollOff")
                        mc.setAttr(replaceNode+".specularRoughness",eachAttr)

                        eachAttr=mc.getAttr(origNode+".specularColor")
                        mc.setAttr(replaceNode+".KsColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                        eachAttr=mc.getAttr(origNode+".reflectivity")
                        mc.setAttr(replaceNode+".Kr",eachAttr)

                        eachAttr=mc.getAttr(origNode+".reflectedColor")
                        mc.setAttr(replaceNode+".KtColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                    

            except:
                om.MGlobal.displayWarning(u'Error in setting %s attribute...Ignore this attribute!' % (replaceNode))

        if replaceNodeType=="blinn" and origNodeType=="aiStandard":
            try:
                eachAttr=mc.getAttr(origNode+".color")
                mc.setAttr(replaceNode+".color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                eachAttr=mc.getAttr(origNode+".opacity")
                mc.setAttr(replaceNode+".transparency",(1-eachAttr[0][0]),(1-eachAttr[0][1]),(1-eachAttr[0][2]),type="double3")

                #eachAttr=mc.getAttr(origNode+".emissionColor")
                #mc.setAttr(replaceNode+".incandescence",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                eachAttr=mc.getAttr(origNode+".Kd")
                mc.setAttr(replaceNode+".diffuse",eachAttr)

                eachAttr=mc.getAttr(origNode+".specularRoughness")
                mc.setAttr(replaceNode+".specularRollOff",eachAttr)

                eachAttr=mc.getAttr(origNode+".KsColor")
                mc.setAttr(replaceNode+".specularColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                eachAttr=mc.getAttr(origNode+".Kt")
                mc.setAttr(replaceNode+".reflectivity",eachAttr)

                eachAttr=mc.getAttr(origNode+".KtColor")
                mc.setAttr(replaceNode+".reflectedColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
            except:
                om.MGlobal.displayWarning(u'Error in setting %s attribute...Ignore this attribute!' % (replaceNode))

        if replaceNodeType=="blinn" and origNodeType=="VRayMtl":
            try: 
                eachAttr=mc.getAttr(origNode+".color")
                mc.setAttr(replaceNode+".color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                #eachAttr=mc.getAttr(origNode+".transparency")
                eachAttr=mc.getAttr(origNode+".opacityMap")
                mc.setAttr(replaceNode+".transparency",(1-eachAttr[0][0]),(1-eachAttr[0][1]),(1-eachAttr[0][2]),type="double3")


                #eachAttr=mc.getAttr(origNode+".illumColor")
                #mc.setAttr(replaceNode+".incandescence",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                eachAttr=mc.getAttr(origNode+".diffuseColorAmount")
                mc.setAttr(replaceNode+".diffuse",eachAttr)

                eachAttr=mc.getAttr(origNode+".reflectionColorAmount")
                mc.setAttr(replaceNode+".reflectivity",eachAttr)

                eachAttr=mc.getAttr(origNode+".reflectionColor")
                mc.setAttr(replaceNode+".reflectedColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
            except:
                om.MGlobal.displayWarning(u'Error in setting %s attribute...Ignore this attribute!' % (replaceNode))

        if replaceNodeType=="VRayMtl" and (origNodeType=="blinn" or origNodeType=="lambert" or origNodeType=="phong" or origNodeType=="phongE"or origNodeType=="mia_material" or origNodeType=="mia_material_x" or origNodeType=="anisotropic"):
            try:
                if origNodeType=="mia_material" or origNodeType=="mia_material_x":
                    eachAttr=mc.getAttr(origNode+".diffuse")
                    mc.setAttr(replaceNode+".color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                    #eachAttr=mc.getAttr(origNode+".refl_color")
                    #mc.setAttr(replaceNode+".KsColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                    
                    eachAttr=mc.getAttr(origNode+".reflectivity")
                    mc.setAttr(replaceNode+".reflectionColorAmount",eachAttr)
                else:
                    eachAttr=mc.getAttr(origNode+".color")
                    mc.setAttr(replaceNode+".color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                    eachAttr=mc.getAttr(origNode+".transparency")
                    #mc.setAttr(replaceNode+".transparency",(1-eachAttr[0][0]),(1-eachAttr[0][1]),(1-eachAttr[0][2]),type="double3")
                    mc.setAttr(replaceNode+".opacityMap",(1-eachAttr[0][0]),(1-eachAttr[0][1]),(1-eachAttr[0][2]),type="double3")
                    if origNodeType=="blinn":
                   #eachAttr=mc.getAttr(origNode+".incandescence")
                   # mc.setAttr(replaceNode+".illumColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")

                        eachAttr=mc.getAttr(origNode+".diffuse")
                        mc.setAttr(replaceNode+".diffuseColorAmount",eachAttr)

                        eachAttr=mc.getAttr(origNode+".reflectivity")
                        mc.setAttr(replaceNode+".reflectionColorAmount",eachAttr)

                        eachAttr=mc.getAttr(origNode+".reflectedColor")
                        mc.setAttr(replaceNode+".reflectionColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
            except:
                om.MGlobal.displayWarning(u'Error in setting %s attribute...Ignore this attribute!' % (replaceNode))

                
        binValue = mc.getAttr(origNode + '.binMembership')
        try:
            mc.setAttr(replaceNode + '.binMembership',binValue,type='string')
        except:
            om.MGlobal.displayWarning(u'%s.binMembership attribute not found...ignore!' % origNode)

        connections = mc.listConnections(origNode,s=True,d=False,connections=True,plugs=True)

        if not connections == None:
            for i in range(0,len(connections),2):
                origPlug = connections[i]
                srcPlug = connections[i+1]

                replacePlug = string.replace(origPlug,origNode,replaceNode)
                try:
                    mc.connectAttr(srcPlug,replacePlug)
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (replacePlug,srcPlug))

        connections = mc.listConnections(origNode,s=False,d=True,connections=True,plugs=True)
        if connections:
            for i in range(0,len(connections),2):
                origPlug = connections[i]
                dstPlug = connections[i+1]

                replacePlug = string.replace(origPlug,origNode,replaceNode)

                try:
                    mc.disconnectAttr(origPlug,dstPlug)
                    mc.connectAttr(replacePlug,dstPlug)
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                    
                    
        if replaceNodeType=="aiStandard" and (origNodeType=="blinn" or origNodeType=="lambert" or origNodeType=="phong" or origNodeType=="phongE" or origNodeType=="mia_material" or origNodeType=="mia_material_x" or origNodeType=="anisotropic"):
            connections=mc.listConnections(origNode+".transparency",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".opacity"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            if origNodeType!="mia_material" and origNodeType!="mia_material_x":
                connections=mc.listConnections(origNode+".incandescence",s=True,d=False,connections=True,plugs=True)
                if connections:
                    try:
                        mc.disconnectAttr(connections[1],connections[0])
                        mc.connectAttr(connections[1],(replaceNode+".emissionColor"))
                    except:
                        om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))
                if origNodeType=="blinn":
                    connections=mc.listConnections(origNode+".specularColor",s=True,d=False,connections=True,plugs=True)
                    if connections:
                        try:
                            mc.disconnectAttr(connections[1],connections[0])
                            mc.connectAttr(connections[1],(replaceNode+".KsColor"))
                        except:
                            om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

                    connections=mc.listConnections(origNode+".reflectivity",s=True,d=False,connections=True,plugs=True)
                    if connections:
                        try:
                            mc.disconnectAttr(connections[1],connections[0])
                            mc.connectAttr(connections[1],(replaceNode+".Kt"))
                        except:
                            om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

                    connections=mc.listConnections(origNode+".specularRollOff",s=True,d=False,connections=True,plugs=True)
                    if connections:
                        try:
                            mc.disconnectAttr(connections[1],connections[0])
                            mc.connectAttr(connections[1],(replaceNode+".specularRoughness"))
                        except:
                            om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

                 
        if replaceNodeType=="blinn" and origNodeType=="aiStandard":
            connections=mc.listConnections(origNode+".opacity",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".transparency"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".emissionColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".incandescence"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".KsColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".specularColor"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".Kt",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".reflectivity"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".specularRoughness",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".specularRollOff"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            
        if replaceNodeType=="aiStandard" and origNodeType=="VRayMtl":

            connections=mc.listConnections(origNode+".opacityMap",s=True,d=False,connections=True,plugs=True)
            
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".opacity"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".illumColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".emissionColor"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".reflectionColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".KsColor"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".reflectionColorAmount",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".Kt"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".reflectionGlossiness",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".specularRoughness"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".bumpMap",s=True,d=False,connections=True,plugs=True)        
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".normalCamera"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

          
        if replaceNodeType=="VRayMtl" and origNodeType=="aiStandard":
            connections=mc.listConnections(origNode+".opacity",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".opacityMap"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".emissionColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".illumColor"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".KsColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".reflectionColor"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".Kt",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".reflectionColorAmount"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".specularRoughness",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".reflectionGlossiness"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".normalCamera",s=True,d=False,connections=True,plugs=True)        
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".bumpMap"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))



        if replaceNodeType=="VRayMtl" and (origNodeType=="blinn" or origNodeType=="lambert" or origNodeType=="phong" or origNodeType=="phongE" or origNodeType=="mia_material" or origNodeType=="mia_material_x" or origNodeType=="anisotropic"):
            if origNodeType!="mia_material" and origNodeType!="mia_material_x":
                connections=mc.listConnections(origNode+".incandescence",s=True,d=False,connections=True,plugs=True)
                if connections:
                    try:
                        mc.disconnectAttr(connections[1],connections[0])
                        mc.connectAttr(connections[1],(replaceNode+".illumColor"))
                    except:
                       om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))
                connections=mc.listConnections(origNode+".normalCamera",s=True,d=False,connections=True,plugs=True)
                if connections:
                    try:
                        mc.disconnectAttr(connections[1],connections[0])
                        mc.connectAttr(connections[1],(replaceNode+".bumpMap"))
                    except:
                       om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))
                       
                connections=mc.listConnections(origNode+".transparency",s=True,d=False,connections=True,plugs=True)
                if connections:
                    try:
                        mc.disconnectAttr(connections[1],connections[0])
                        mc.connectAttr(connections[1],(replaceNode+".opacityMap"))
                    except:
                       om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))
                
                if origNodeType=="blinn" :
                    connections=mc.listConnections(origNode+".specularRollOff",s=True,d=False,connections=True,plugs=True)
                    if connections:
                        try:
                            mc.disconnectAttr(connections[1],connections[0])
                            mc.connectAttr(connections[1],(replaceNode+".reflectionGlossiness"))
                        except:
                           om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

                    connections=mc.listConnections(origNode+".specularColor",s=True,d=False,connections=True,plugs=True)
                    if connections:
                        try:
                            mc.disconnectAttr(connections[1],connections[0])
                            mc.connectAttr(connections[1],(replaceNode+".reflectionColor"))
                        except:
                           om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

                    connections=mc.listConnections(origNode+".reflectivity",s=True,d=False,connections=True,plugs=True)
                    if connections:
                        try:
                            mc.disconnectAttr(connections[1],connections[0])
                            mc.connectAttr(connections[1],(replaceNode+".reflectionColorAmount"))
                        except:
                           om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))


        if replaceNodeType=="blinn" and origNodeType=="VRayMtl":
            connections=mc.listConnections(origNode+".illumColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".incandescence"))
                except:
                   om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))
            connections=mc.listConnections(origNode+".bumpMap",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".normalCamera"))
                except:
                   om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".reflectionGlossiness",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".specularRollOff"))
                except:
                   om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".reflectionColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".specularColor"))
                except:
                   om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".reflectionColorAmount",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".reflectivity"))
                except:
                   om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

            connections=mc.listConnections(origNode+".opacityMap",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".transparency"))
                except:
                   om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (connections[1],connections[0]))

         
    def convertBlinn(self):
        changeType = ['phong','phongE']
        if mc.pluginInfo('mtoa', q=True, l=True):
            changeType.append('aiStandard')
        if mc.pluginInfo('vrayformaya', q=True, l=True):
            changeType.append('VRayMtl')
        allPhong = mc.ls(type=changeType)
        replaceNodeType = 'blinn'
        i = 0
        for eachPhong in allPhong:
            replaceNode = mc.createNode(replaceNodeType)

            self.disconnectMaterialInfo(eachPhong)

            self.doReplace(eachPhong, replaceNode)

            cmdStr = 'showEditor %s;\n' % replaceNode

            mm.eval(cmdStr)
            mc.delete(eachPhong)
            i += 1

        print (u'--------========>>>> 一共转换了%d个Phong材质球... <<<<========--------\n' % i)
    def convertVray(self):
        #allPhong = mc.ls(type='blinn')
        allPhongs=[]
        changeType = ['blinn',"lambert","phong","phongE"]
        if mc.pluginInfo('Mayatomr',q=True,loaded=True ):
            changeType.append('mia_material')
            changeType.append('mia_material_x')
        if mc.pluginInfo('mtoa', q=True, l=True):
            changeType.append('aiStandard')

        allPhong = mc.ls(type=changeType)
        for phon in allPhong:
            if mc.listConnections(phon,s=False,d=True)[0]!="initialParticleSE":
                allPhongs.append(phon)
        replaceNodeType = 'VRayMtl'
        i = 0
        for eachPhong in allPhongs:
            replaceNode = mc.createNode(replaceNodeType)

            self.disconnectMaterialInfo(eachPhong)

            self.doReplace(eachPhong, replaceNode)

            cmdStr = 'showEditor %s;\n' % replaceNode

            mm.eval(cmdStr)
            mc.delete(eachPhong)
            i += 1

        print (u'--------========>>>> 一共转换了%d个Phong材质球... <<<<========--------\n' % i)

    def convertArnold(self):
        #allPhong= mc.ls(type='blinn')
        changeType = ['blinn',"lambert","phong","phongE"]
        if mc.pluginInfo('Mayatomr',q=True,loaded=True ):
            changeType.append("mia_material")
            changeType.append("mia_material_x")
        if mc.pluginInfo('vrayformaya', q=True, l=True):
            changeType.append('VRayMtl')


        allPhong = mc.ls(type=changeType)

        #value=mc.radioButtonGrp("selectedOrAll",q=True,sl=True)
        '''if value==2:
            allPhong = mc.ls(type='blinn')
        else:
            allPhong'''
        replaceNodeType = 'aiStandard'
        allPhongs=[]
        for phon in allPhong:
            if mc.listConnections(phon,s=False,d=True)[0]!="initialParticleSE":
                allPhongs.append(phon)
        i = 0
        for eachPhong in allPhongs:
            replaceNode = mc.createNode(replaceNodeType)

            self.disconnectMaterialInfo(eachPhong)

            self.doReplace(eachPhong, replaceNode)

            cmdStr = 'showEditor %s;\n' % replaceNode

            mm.eval(cmdStr)
            mc.delete(eachPhong)
            i += 1

        print (u'--------========>>>> 一共转换了%d个Phong材质球... <<<<========--------\n' % i)



class VRayBlendTolayeredShader(object):
    def __init__(self):
        pass

    def deleteVRayMeshMaterial(self):
        allVRayMeshMaterial=mc.ls(type="VRayMeshMaterial")
        for VRayMeshMaterials in allVRayMeshMaterial:
            allMesh=mc.listConnections("%s.outColor"%VRayMeshMaterials,s=False,d=True,plugs=True)
            mc.delete(allMesh[0])
            mc.delete(VRayMeshMaterials)
        mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')

    def VRayMtl2SidedToAiUtility(self):
        allVRayMtl2Sided=mc.ls(type="VRayMtl2Sided")
        for VRayMtl2Sided in allVRayMtl2Sided:
            aiUtility=mc.shadingNode("aiUtility",asShader=True)
            mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(aiUtility+"SG"))
            mc.connectAttr((aiUtility+".outColor"),(aiUtility+"SG.surfaceShader"),force=True)
            conditions=mc.shadingNode("condition",asShader=True)
            try:
                mc.connectAttr(("%s.outColor"%conditions),("%s.color"%aiUtility),f=True)
            except:
                pass
            mc.hyperShade(objects=VRayMtl2Sided)
            mc.hyperShade(assign=aiUtility)
            samplerInfo=mc.shadingNode("samplerInfo",asShader=True)
            try:
                mc.connectAttr(("%s.flippedNormal"%samplerInfo),("%s.firstTerm"%conditions),f=True)
            except:
                pass
            connection=mc.listConnections(VRayMtl2Sided,s=True,d=False,connections=True,plugs=True)
            if connection and len(connection)>=4:
                mc.connectAttr(connection[1],("%s.colorIfTrue"%conditions),f=True)
                mc.connectAttr(connection[3],("%s.colorIfFalse"%conditions),f=True)
            elif connection and len(connection)>=4:
                mc.connectAttr(connection[1],("%s.colorIfTrue"%conditions),f=True)
            mc.delete(VRayMtl2Sided)
        mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");') 


    def VRayBlendMtlTolayeredShader(self):
        materialChange().convertArnold()
        allVRayBlend=mc.ls(type='VRayBlendMtl')
        for VRayBlend in allVRayBlend:
            #求原链接的节点
            connections=mc.listConnections(VRayBlend,s=True,d=False,connections=True,plugs=True)
            #创建layeredShader节点
            layeredShader=mc.shadingNode("layeredShader",asShader=True)
            mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=(layeredShader+"SG"))
            mc.connectAttr((layeredShader+".outColor"),(layeredShader+"SG.surfaceShader"),force=True)
            listMaterial=[]
            if not connections==None:
                number=len(connections)
                numbers=number
                i=1
                while(number):
                    if "coat_material" in connections[number-2]:
                        try:
                            mc.connectAttr(connections[number-1],"%s.inputs[%d].color"%(layeredShader,i))
                            value=mc.getAttr(VRayBlend+".blend_amount_"+str(i-1))
                            values=list(value[0])
                            mc.setAttr(("%s.inputs[%d].transparency"%(layeredShader,i)),values[0],values[1],values[2])
                        except:
                            om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.inputs[%d].color' % (connections[number-1],layeredShader,i))
                        
                        i+=1
                        listMaterial.append(connections[number-1])
                    number-=2  
                k=1
                for j in range(0,numbers,2):
                    if "blend_amount" in connections[j]:
                        blends=connections[j+1].replace("outColor","outTransparency")
                        try:
                            mc.connectAttr(blends,"%s.inputs[%d].transparency"%(layeredShader,k))
                        except:
                            om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.inputs[%d].color' %(blends,layeredShader,k)) 
                        k+=1
                    if "base_material" in connections[j]:
                        blends=connections[j+1].replace("outColor","outTransparency") 
                        try:
                            mc.connectAttr(blends,"%s.inputs[%d].transparency"%(layeredShader,i))
                            mc.connectAttr(connections[j+1],"%s.inputs[%d].color"%(layeredShader,i)) 
                        except:
                            om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.inputs[%d].color' %(blends,layeredShader,i)) 
                        listMaterial.append(connections[j+1])

            try:
                connections=mc.listConnections((VRayBlend+".outColor"),s=False,d=True,connections=True,plugs=True)
            except:
                pass

            if connections:
                if mc.objectType(connections[1].split(".")[0])=="shadingEngine":
                    mc.hyperShade(objects=connections[0].split(".")[0])
                    mc.hyperShade(assign=layeredShader)
                    mc.delete(connections[0].split(".")[0])
                    continue

                outColor=connections[1].replace("base_material","bumpMap") 
                connects=mc.listConnections(outColor,s=True,d=False,connections=True,plugs=True)
                
                fileStr=connects[1].replace("outColor","outAlpha") 
                bump=mc.shadingNode("bump2d",asUtility=True)
                try:
                    mc.connectAttr(fileStr,(bump+".bumpValue"))
                except:
                    om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.bumpValue' %(fileStr,bump)) 
                     
                for Material in listMaterial:
                    Mater=Material.split(".")[0]
                    try:
                        mc.connectAttr((bump+".outNormal"),(Mater+".normalCamera"))
                    except:
                        om.MGlobal.displayWarning(u'Error %s.outNormal already has an incoming connection from %s.normalCamera' %(Mater,Mater))
                        
                objs=connections[1].split(".")[0]
                
                if mc.getAttr(objs+".bumpMapType")==0:
                    mc.setAttr(bump+".bumpInterp",0)
                else:
                    mc.setAttr(bump+".bumpInterp",1)
                
                
                mc.hyperShade(objects=objs)
                mc.hyperShade(assign=layeredShader)
                mc.delete(objs)
                mc.delete(connections[0].split(".")[0])

        allVRayBump=mc.ls(type='VRayBumpMtl')
        for VRayBump in allVRayBump:
            flag=False
            objects=""
            connections=mc.listConnections(VRayBump,s=True,d=False,connections=True,plugs=True)
            if connections:
                for con in range(0,len(connections),2):
                    objs=connections[con+1].split(".")[0]
                    if mc.objectType(objs)=="aiStandard":
                        objects=objs
                        flag=True
                        break
            if flag:
               connects=mc.listConnections(VRayBump+".bumpMap",s=True,d=False,connections=True,plugs=True)
               if connects:
                    fileStr=connects[1].replace("outColor","outAlpha")
                    bump=mc.shadingNode("bump2d",asUtility=True)
                    try:
                        mc.connectAttr(fileStr,(bump+".bumpValue"))
                    except:
                        om.MGlobal.displayWarning(u'Error %s already has an incoming connection from %s.bumpValue' %(fileStr,bump))
                    try:
                        mc.connectAttr((bump+".outNormal"),(objects+".normalCamera"))
                    except:
                        om.MGlobal.displayWarning(u'Error %s.outNormal already has an incoming connection from %s.normalCamera' %(Mater,Mater)) 
               if mc.getAttr(VRayBump+".bumpMapType")==0:
                   mc.setAttr(bump+".bumpInterp",0)
               else:
                   mc.setAttr(bump+".bumpInterp",1)
                    
               mc.hyperShade(objects=VRayBump)
               mc.hyperShade(assign=objects)
               #mc.delete(VRayBump)
               mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')


class materialChangeBlinnMia_material_x(object):
    def __init__(self):
        pass
        
    def disconnectMaterialInfo(self,shaderNode):
        materialInfoNode = self.getMaterialInfo(shaderNode)
        if materialInfoNode == None:
            return

        mc.disconnectAttr(shaderNode + '.message',materialInfoNode + '.material')


    def getMaterialInfo(self,shaderNode):
        connections = mc.listConnections(shaderNode + '.message')
        if connections:
            for each in connections:
                if mc.objectType(each) == 'materialInfo':
                    return each

            return None

    def doReplace(self,origNode, replaceNode):
        origNode = origNode.encode()
        replaceNode = replaceNode.encode()
        
        origAttrs = mc.listAttr(origNode, scalar=True, multi=True, read=True, visible=True)
   
        replaceAttrs = mc.listAttr(replaceNode, scalar=True, multi=True, read=True, visible=True)
        
        for eachAttr in origAttrs:
            if eachAttr in replaceAttrs:
                value = mc.getAttr(origNode + '.' + eachAttr)
                try:
                    mc.setAttr(replaceNode + '.' + eachAttr,value)
                except:
                    om.MGlobal.displayWarning(u'Error in setting %s.%s attribute...Ignore this attribute!' % (replaceNode,eachAttr))

        origNodeType=mc.nodeType(origNode)
        replaceNodeType=mc.nodeType(replaceNode)
        if replaceNodeType=="blinn" and (origNodeType=="mia_material_x" or origNodeType=="mia_material"):
            try:
                eachAttr=mc.getAttr(origNode+".diffuse")
                mc.setAttr(replaceNode+".color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                
                eachAttr=mc.getAttr(origNode+".additional_color")
                mc.setAttr(replaceNode+".incandescence",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                
                eachAttr=mc.getAttr(origNode+".refl_color")
                mc.setAttr(replaceNode+".specularColor",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
            except:
                om.MGlobal.displayWarning(u'Error in setting %s attribute...Ignore this attribute!' % (replaceNode)) 
                
              
        if replaceNodeType=="mia_material_x" and origNodeType=="blinn":
            try:
                eachAttr=mc.getAttr(origNode+".color")
                mc.setAttr(replaceNode+".diffuse",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                
                eachAttr=mc.getAttr(origNode+".incandescence")
                mc.setAttr(replaceNode+".additional_color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
                
                eachAttr=mc.getAttr(origNode+".specularColor")
                mc.setAttr(replaceNode+".refl_color",eachAttr[0][0],eachAttr[0][1],eachAttr[0][2],type="double3")
            except:
                om.MGlobal.displayWarning(u'Error in setting %s attribute...Ignore this attribute!' % (replaceNode)) 

                
        binValue = mc.getAttr(origNode + '.binMembership')
        try:
            mc.setAttr(replaceNode + '.binMembership',binValue,type='string')
        except:
            om.MGlobal.displayWarning(u'%s.binMembership attribute not found...ignore!' % origNode)

        connections = mc.listConnections(origNode,s=True,d=False,connections=True,plugs=True)

        if not connections == None:
            for i in range(0,len(connections),2):
                origPlug = connections[i]
                srcPlug = connections[i+1]

                replacePlug = string.replace(origPlug,origNode,replaceNode)
                try:
                    mc.connectAttr(srcPlug,replacePlug)
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (replacePlug,srcPlug))

        connections = mc.listConnections(origNode,s=False,d=True,connections=True,plugs=True)
        if connections:
            for i in range(0,len(connections),2):
                origPlug = connections[i]
                dstPlug = connections[i+1]

                replacePlug = string.replace(origPlug,origNode,replaceNode)

                try:
                    mc.disconnectAttr(origPlug,dstPlug)
                    mc.connectAttr(replacePlug,dstPlug)
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                    
                    
        if replaceNodeType=="blinn" and (origNodeType=="mia_material_x" or origNodeType=="mia_material"):
            connections=mc.listConnections(origNode+".diffuse",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".color"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
  
            connections=mc.listConnections(origNode+".cutout_opacity",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    dest=connections[1].replace("outAlpha","outTransparency")
                    mc.connectAttr(dest,(replaceNode+".transparency"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                    
            connections=mc.listConnections(origNode+".additional_color",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".incandescence"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
           
            connections=mc.listConnections(origNode+".refl_color",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".specularColor"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))

            connections=mc.listConnections(origNode+".refl_gloss",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".specularRollOff"))
                    #dest=connections[1].replace("outColor","outAlpha")
                    #mc.connectAttr(dest,(replaceNode+".refl_colorA"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                    
            if origNodeType=="mia_material_x":
                connections=mc.listConnections(origNode+".overall_bump",s=True,d=False,connections=True,plugs=True)
                if connections:
                    try:
                        mc.disconnectAttr(connections[1],connections[0])
                        mc.connectAttr(connections[1],(replaceNode+".normalCamera"))
                    except:
                        om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                
                    
        if replaceNodeType=="mia_material_x" and origNodeType=="blinn":
            connections=mc.listConnections(origNode+".color",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".diffuse"))
                    dest=connections[1].replace("outColor","outAlpha")
                    mc.connectAttr(dest,(replaceNode+".diffuseA"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                    
            connections=mc.listConnections(origNode+".transparency",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    dest=connections[1].replace("outTransparency","outAlpha")
                    mc.connectAttr(dest,(replaceNode+".cutout_opacity"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                    
            connections=mc.listConnections(origNode+".incandescence",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".additional_color"))
                    dest=connections[1].replace("outColor","outAlpha")
                    mc.connectAttr(dest,(replaceNode+".additional_colorA"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                     
            connections=mc.listConnections(origNode+".specularColor",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".refl_color"))
                    dest=connections[1].replace("outColor","outAlpha")
                    mc.connectAttr(dest,(replaceNode+".refl_colorA"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))

            connections=mc.listConnections(origNode+".specularRollOff",s=True,d=False,connections=True,plugs=True)
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".refl_gloss"))
                    #dest=connections[1].replace("outColor","outAlpha")
                    #mc.connectAttr(dest,(replaceNode+".refl_colorA"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))


            connections=mc.listConnections(origNode+".normalCamera",s=True,d=False,connections=True,plugs=True)       
            if connections:
                try:
                    mc.disconnectAttr(connections[1],connections[0])
                    mc.connectAttr(connections[1],(replaceNode+".overall_bump"))
                except:
                    om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))
                
                              
                    
    def convertBlinn(self):
        allPhong = mc.ls(type=['mia_material_x','mia_material'])
        replaceNodeType = 'blinn'
        i = 0
        for eachPhong in allPhong:
            connections=mc.listConnections(eachPhong,s=False,d=True,connections=True,plugs=True)
            connectSG=""
            listShape=[]
            if connections:
                for con in connections:
                    if "SG.miMaterialShader" in con:
                        connectSG=con
                        break
                if  connectSG:
                    shapesSG=connectSG.split(".")[0]
                    connections=mc.listConnections(shapesSG,s=True,d=False,connections=True,plugs=True)
                   
                    for cons in connections:
                        if "instObjGroups" in cons:
                            objGroups=cons.split(".")[0]
                            listShape.append(objGroups)

            replaceNode = mc.createNode(replaceNodeType)

            self.disconnectMaterialInfo(eachPhong)

            self.doReplace(eachPhong, replaceNode)

            mc.select(d=True)
            for shap in listShape:
                mc.select(shap,r=True)
                mc.hyperShade(assign=replaceNode)

            cmdStr = 'showEditor %s;\n' % replaceNode

            mm.eval(cmdStr)
            mc.delete(eachPhong)
            i += 1
            
    def convertMia_material_x(self):
        allPhong = mc.ls(type='blinn')
        replaceNodeType = 'mia_material_x'
        if not mc.pluginInfo('Mayatomr',q=True,loaded=True ):
            mc.confirmDialog(message=u"没有加载Mayatomr！")
            return
        i = 0
        for eachPhong in allPhong:
            connections=mc.listConnections(eachPhong,s=False,d=True,connections=True,plugs=True)
            connectSG=""
            listShape=[]
            if connections:
                for con in connections:
                    if "SG.surfaceShader" in con:
                        connectSG=con
                        break
                if  connectSG:
                    shapesSG=connectSG.split(".")[0]
                    connections=mc.listConnections(shapesSG,s=True,d=False,connections=True,plugs=True)
                   
                    for cons in connections:
                        if "instObjGroups" in cons:
                            objGroups=cons.split(".")[0]
                            listShape.append(objGroups)

            replaceNode = mc.createNode(replaceNodeType)

            self.disconnectMaterialInfo(eachPhong)

            self.doReplace(eachPhong, replaceNode)

            mc.select(d=True)
            for shap in listShape:
                mc.select(shap,r=True)
                mc.hyperShade(assign=replaceNode)
                    
            cmdStr = 'showEditor %s;\n' % replaceNode

            mm.eval(cmdStr)
            mc.delete(eachPhong)
            i += 1
            
            
def OCT_materialChangeUI():
    if mc.window('OCT_materialChangeUI', exists=True):
        mc.deleteUI('OCT_materialChangeUI', window=True)

    mc.window("OCT_materialChangeUI", title=u"材质互换", menuBar=True, widthHeight=(260, 150), resizeToFitChildren=True, sizeable=True)
    mc.columnLayout('mainmenu', adjustableColumn=True) 
    mc.text(u"各 种 材 质 的 互 换",h=40,backgroundColor=(0.4, 0.3, 0.1))           
    mc.button(label='VRayMtl', w=60, h=30, command='OCT_render.OCT_materialChange.materialChange().convertVray()', backgroundColor=(0.5, 0.3, 0.51))
    mc.button(label='aiStandard', w=60, h=30, command='OCT_render.OCT_materialChange.materialChange().convertArnold()', backgroundColor=(0.5, 0.3, 0.55))
    mc.button(label='blinn', w=60, h=30, command='OCT_render.OCT_materialChange.materialChange().convertBlinn()', backgroundColor=(0.5, 0.3, 0.59))
    mc.button(label='VRayBlendTolayeredShader', w=150, h=30, command='OCT_render.OCT_materialChange.VRayBlendTolayeredShader().VRayBlendMtlTolayeredShader()', backgroundColor=(0.4, 0.5, 0.5))
    mc.button(label='DeleteVRayMeshMaterial', w=150, h=30, command='OCT_render.OCT_materialChange.VRayBlendTolayeredShader().deleteVRayMeshMaterial()', backgroundColor=(0.4, 0.5, 0.5))
    mc.button(label='VRayMtl2SidedToAiUtility', w=150, h=30, command='OCT_render.OCT_materialChange.VRayBlendTolayeredShader().VRayMtl2SidedToAiUtility()', backgroundColor=(0.4, 0.5, 0.5))

    mc.button(label='Mia_material_x To Blinn', w=150, h=30, command='OCT_render.OCT_materialChange.materialChangeBlinnMia_material_x().convertBlinn()', backgroundColor=(0.4, 0.4, 0.3))
    mc.button(label='Blinn To Mia_material_x', w=150, h=30, command='OCT_render.OCT_materialChange.materialChangeBlinnMia_material_x().convertMia_material_x()', backgroundColor=(0.4, 0.4, 0.4))
    mc.showWindow("OCT_materialChangeUI")
               
