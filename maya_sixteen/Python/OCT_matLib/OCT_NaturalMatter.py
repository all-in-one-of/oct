#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
OCT_ImagePath = r'\\octvision.com\CG\Tech\matLib'

##########################自然物质属性设置类#####################
class OCT_NaturalMatter():
    def __init__(self, allArnolds):
        self.setAttrValueDir = {}
        self.nodeAttrConDir = {}
        self.allArnolds = allArnolds
        
    #####################设置arnold材质属性####################
    def setAttrValue(self):
        if self.allArnolds:
            for each in self.allArnolds:
                self.setAttrNodeValue(each)
    #####################设置所有节点属性####################
    def setAttrNodeValue(self, nodeName):
        for key in self.setAttrValueDir.keys():
            try:
                mc.setAttr('%s.%s' % (nodeName, key), self.setAttrValueDir[key])
            except:
                print "%s.%s set value error"%(nodeName, key)

    def nodeAttrCon(self):
        for key in self.nodeAttrConDir.keys():
            for each in self.nodeAttrConDir[key]:
                try:
                    mc.connectAttr('%s'%key, '%s'%each, f = True)
                except:
                    print "The connection between %s and %s is not successful"%(key, each)

    #####################创建file节点#####################
    def CreateFileName(self):
        fileNodeName = mc.shadingNode('file', asTexture = True, isColorManaged = True)
        place2dTexName = mc.shadingNode('place2dTexture', asUtility = True)
        self.nodeAttrConDir = {'%s.coverage'%place2dTexName:['%s.coverage'%fileNodeName], '%s.translateFrame'%place2dTexName:['%s.translateFrame'%fileNodeName],
                            '%s.rotateFrame'%place2dTexName:['%s.rotateFrame'%fileNodeName], '%s.mirrorU'%place2dTexName:['%s.mirrorU'%fileNodeName],
                            '%s.mirrorV'%place2dTexName:['%s.mirrorV'%fileNodeName], '%s.stagger'%place2dTexName:['%s.stagger'%fileNodeName],
                            '%s.wrapU'%place2dTexName: ['%s.wrapU'%fileNodeName], '%s.wrapV'%place2dTexName: ['%s.wrapV'%fileNodeName], 
                            '%s.repeatUV'%place2dTexName: ['%s.repeatUV'%fileNodeName], '%s.offset'%place2dTexName:['%s.offset'%fileNodeName],
                            '%s.rotateUV'%place2dTexName: ['%s.rotateUV'%fileNodeName], '%s.noiseUV'%place2dTexName:['%s.noiseUV'%fileNodeName],
                            '%s.vertexUvOne'%place2dTexName: ['%s.vertexUvOne'%fileNodeName], '%s.vertexUvTwo'%place2dTexName:['%s.vertexUvTwo'%fileNodeName],
                            '%s.vertexUvThree'%place2dTexName:['%s.vertexUvThree'%fileNodeName], '%s.vertexCameraOne'%place2dTexName:['%s.vertexCameraOne'%fileNodeName],
                            '%s.outUV'%place2dTexName:['%s.uv'%fileNodeName], '%s.outUvFilterSize'%place2dTexName: ['%s.uvFilterSize'%fileNodeName]}
        self.nodeAttrCon()
        return fileNodeName, place2dTexName

    ###########################黏土#######################
    def setClayAttr(self):
        self.setAttrValueDir.clear()
        self.setAttrValueDir = {'Fresnel': False,
                         'FresnelAffectDiff': True,
                         'FresnelUseIOR': False,
                         'IOR': 1.0,
                         'Kb': 0.0,
                         'Kd': 1.0,
                         'Kr': 0.0,
                         'KrColorB': 1.0,
                         'KrColorG': 1.0,
                         'KrColorR': 1.0,
                         'Krn': 0.0,
                         'Ks': 0.30000001192092896,
                         'KsColorB': 1.0,
                         'KsColorG': 1.0,
                         'KsColorR': 1.0,
                         'Ksn': 0.125,
                         'Ksss': 0.05000000074505806,
                         'KsssColorB': 0.12200000137090683,
                         'KsssColorG': 0.24699999392032623,
                         'KsssColorR': 0.5920000076293945,
                         'Kt': 0.0,
                         'KtColorB': 1.0,
                         'KtColorG': 1.0,
                         'KtColorR': 1.0,
                         'aiEnableMatte': False,
                         'aiMatteColorA': 0.0,
                         'aiMatteColorB': 0.0,
                         'aiMatteColorG': 0.0,
                         'aiMatteColorR': 0.0,
                         'bounceFactor': 1.0,
                         'colorB': 0.12200000137090683,
                         'colorG': 0.24699999392032623,
                         'colorR': 0.5920000076293945,
                         'diffuseRoughness': 0.5,
                         'directDiffuse': 1.0,
                         'directSpecular': 1.0,
                         'dispersionAbbe': 0.0,
                         'emission': 0.0,
                         'emissionColorB': 1.0,
                         'emissionColorG': 1.0,
                         'emissionColorR': 1.0,
                         'enableGlossyCaustics': False,
                         'enableInternalReflections': True,
                         'enableReflectiveCaustics': False,
                         'enableRefractiveCaustics': False,
                         'indirectDiffuse': 1.0,
                         'indirectSpecular': 1.0,
                         'opacityB': 1.0,
                         'opacityG': 1.0,
                         'opacityR': 1.0,
                         'reflectionExitColorB': 0.0,
                         'reflectionExitColorG': 0.0,
                         'reflectionExitColorR': 0.0,
                         'reflectionExitUseEnvironment': False,
                         'refractionExitColorB': 0.0,
                         'refractionExitColorG': 0.0,
                         'refractionExitColorR': 0.0,
                         'refractionExitUseEnvironment': False,
                         'refractionRoughness': 0.0,
                         'specularAnisotropy': 0.5,
                         'specularDistribution': 1,
                         'specularFresnel': True,
                         'specularRotation': 0.0,
                         'specularRoughness': 0.5,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0}
        self.setAttrValue()
        
    ##########################花岗石######################
    def setStone03Attr(self):
        self.setAttrValueDir.clear()
        self.setAttrValueDir =  {'Fresnel': False,
                                 'FresnelAffectDiff': False,
                                 'FresnelUseIOR': False,
                                 'IOR': 1.0,
                                 'Kb': 0.0,
                                 'Kd': 0.699999988079071,
                                 'Kr': 0.0,
                                 'KrColorB': 1.0,
                                 'KrColorG': 1.0,
                                 'KrColorR': 1.0,
                                 'Krn': 0.10000000149011612,
                                 'Ks': 0.30845770239830017,
                                 'KsColorB': 1.0,
                                 'KsColorG': 1.0,
                                 'KsColorR': 1.0,
                                 'Ksn': 0.10000000149011612,
                                 'Ksss': 0.0,
                                 'KsssColorB': 0.0,
                                 'KsssColorG': 0.0,
                                 'KsssColorR': 0.0,
                                 'Kt': 0.0,
                                 'KtColorB': 1.0,
                                 'KtColorG': 1.0,
                                 'KtColorR': 1.0,
                                 'aiEnableMatte': False,
                                 'aiMatteColorA': 0.0,
                                 'aiMatteColorB': 0.0,
                                 'aiMatteColorG': 0.0,
                                 'aiMatteColorR': 0.0,
                                 'bounceFactor': 1.0,
                                 'colorB': 0.0,
                                 'colorG': 0.0,
                                 'colorR': 0.0,
                                 'diffuseRoughness': 0.0,
                                 'directDiffuse': 1.0,
                                 'directSpecular': 1.5,
                                 'dispersionAbbe': 0.0,
                                 'emission': 0.0,
                                 'emissionColorB': 1.0,
                                 'emissionColorG': 1.0,
                                 'emissionColorR': 1.0,
                                 'enableGlossyCaustics': False,
                                 'enableInternalReflections': False,
                                 'enableReflectiveCaustics': False,
                                 'enableRefractiveCaustics': False,
                                 'indirectDiffuse': 1.0,
                                 'indirectSpecular': 1.0,
                                 'opacityB': 1.0,
                                 'opacityG': 1.0,
                                 'opacityR': 1.0,
                                 'reflectionExitColorB': 0.0,
                                 'reflectionExitColorG': 0.0,
                                 'reflectionExitColorR': 0.0,
                                 'reflectionExitUseEnvironment': True,
                                 'refractionExitColorB': 0.0,
                                 'refractionExitColorG': 0.0,
                                 'refractionExitColorR': 0.0,
                                 'refractionExitUseEnvironment': False,
                                 'refractionRoughness': 0.0,
                                 'specularAnisotropy': 0.5,
                                 'specularDistribution': 1,
                                 'specularFresnel': True,
                                 'specularRotation': 0.0,
                                 'specularRoughness': 0.5273631811141968,
                                 'sssRadiusB': 0.9975398778915405,
                                 'sssRadiusG': 1.0,
                                 'sssRadiusR': 0.9269999861717224,
                                 'transmittanceB': 1.0,
                                 'transmittanceG': 1.0,
                                 'transmittanceR': 1.0}
        self.setAttrValue()
        if self.allArnolds:
            for each in self.allArnolds:
                fileNodeName, place2dTexName = self.CreateFileName()
                self.setAttrValueDir.clear()
                self.setAttrValueDir = {u'aiAutoTx': True,
                                         u'alphaGain': 1.0,
                                         u'alphaIsLuminance': True,
                                         u'alphaOffset': 0.0,
                                         u'colorGainB': 1.0,
                                         u'colorGainG': 1.0,
                                         u'colorGainR': 1.0,
                                         u'colorOffsetB': 0.0,
                                         u'colorOffsetG': 0.0,
                                         u'colorOffsetR': 0.0,
                                         u'defaultColorB': 0.5,
                                         u'defaultColorG': 0.5,
                                         u'defaultColorR': 0.5,
                                         u'exposure': 0.0,
                                         u'frameExtension': 1,
                                         u'frameOffset': 0,
                                         u'invert': False}
                self.setAttrNodeValue(fileNodeName)
                mc.setAttr('%s.fileTextureName'%fileNodeName, r'%s\sourceimages\Stone04.jpg'%OCT_ImagePath, type = 'string')
                self.setAttrValueDir.clear()
                self.setAttrValueDir =  {u'coverageU': 1.0,
                                         u'coverageV': 1.0,
                                         u'mirrorU': False,
                                         u'mirrorV': False,
                                         u'noiseU': 0.0,
                                         u'noiseV': 0.0,
                                         u'offsetU': 0.0,
                                         u'offsetV': 0.0,
                                         u'repeatU': 10.0,
                                         u'repeatV': 10.0,
                                         u'rotateFrame': 0.0,
                                         u'rotateUV': 0.0,
                                         u'stagger': False,
                                         u'translateFrameU': 0.0,
                                         u'translateFrameV': 0.0,
                                         u'wrapU': True,
                                         u'wrapV': True} 
                self.setAttrNodeValue(place2dTexName)

                self.nodeAttrConDir.clear()
                self.nodeAttrConDir = {'%s.outColor'%fileNodeName: ['%s.color'%each]}
                self.nodeAttrCon()

if __name__ == '__main__':
    allArnolds = mc.ls(sl = True, type = "aiStandard")
    matLib = OCT_NaturalMatter(allArnolds)
    matLib.setStone03Attr()