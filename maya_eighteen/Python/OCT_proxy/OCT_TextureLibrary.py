#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm

OCT_ImagePath = r'D:\renhj\matLib_old'

class OCT_TextureLibrary():
    def __init__(self):
        self._windowSize = (600, 600)
        self._windowName = 'textureLib_UI'
        #arnold材质
        self.allArnolds = ''

    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName)

    def show(self):
        self.close()
        win = mc.window(self._windowName, wh = self._windowSize, t = u'材质质感库')
        fll = mc.formLayout()
        tl = mc.treeLister()
        mc.formLayout(fll, e = True, af = ((tl, 'top', 0), (tl, 'left', 0), (tl, 'bottom', 0), (tl, 'right', 0)))
        mc.showWindow(self._windowName)

        #自然物质
        mc.treeLister(tl, e = True, add = (u'自然物质/岩石/', r'', lambda *arg:self.text(0)), numberOfPopupMenus = True, expandToDepth= 500)
        mc.popupMenu("ss",b=3)
        mc.menuItem(l=u"打开maya原文件",c=lambda *arg:self.text(1),parent="ss")
                    
        mc.treeLister(tl, e = True, add = (u'自然物质/山体/', r'', lambda *arg:self.text(1)))
        mc.popupMenu("ss",b=3)
        mc.menuItem(l=u"打开maya原文件",c=lambda *arg:self.text(2),parent="ss")
        mc.treeLister(tl, e = True, add = (u'自然物质/石块/', r'', lambda *arg:self.text(2)))
        mc.treeLister(tl, e = True, add = (u'自然物质/土/', r'', lambda *arg:self.text(3)))
        mc.treeLister(tl, e = True, add = (u'自然物质/沙/', r'', lambda *arg:self.text(4)))

        #人造材
        mc.treeLister(tl, e = True, add = (u'人造材料/砖/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/水泥墙面/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/水泥地面/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/大理石/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/石条(石材)/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/朔料/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/金属/', r'%s\gold.jpg'%OCT_ImagePath, lambda *arg:self.gold()))
        mc.treeLister(tl, e = True, add = (u'人造材料/铬/', r'%s\chrome.jpg'%OCT_ImagePath, lambda *arg:self.chrome())) 
        mc.treeLister(tl, e = True, add = (u'人造材料/玻璃/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/陶器/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/陶瓷/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/蜡/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/木材/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/布料/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'人造材料/书(纸)/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = ( u'人造材料/车漆/', r'%s\carPaint.jpg'%OCT_ImagePath, lambda *arg:self.carPaint()))
        mc.treeLister(tl, e = True, add = (u'人造材料/白炽灯/', r'', lambda *arg:self.text(4)))

        #植物
        mc.treeLister(tl, e = True, add = (u'植物/树叶/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'植物/树干/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'植物/花瓣/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'植物/灌木枝干/', r'', lambda *arg:self.text(4)))

        #液体
        mc.treeLister(tl, e = True, add = (u'液体/水/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'液体/牛奶/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'液体/咖啡/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'液体/油/', r'', lambda *arg:self.text(4)))

        #动物
        mc.treeLister(tl, e = True, add = (u'动物/人类皮肤/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'动物/恐龙皮肤/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'动物/眼球/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'动物/牙齿/', r'', lambda *arg:self.text(4)))
        mc.treeLister(tl, e = True, add = (u'动物/指甲/', r'', lambda *arg:self.text(4)))
       
    def text(self, name):
        print name 
        
    ####################人造材料###################
    #金属
    def gold(self):
        self.allArnolds = mc.ls(type = "aiStandard")
        if self.allArnolds:
            for each in self.allArnolds:
                mc.setAttr('%s.aiEnableMatte'%each, 0)
                mc.setAttr('%s.aiMatteColorR'%each, 0)
                mc.setAttr('%s.aiMatteColorG'%each, 0)
                mc.setAttr('%s.aiMatteColorB'%each, 0)
                mc.setAttr('%s.aiMatteColorA'%each, 0)

                mc.setAttr('%s.Kd'%each, 0.6999999881)
                mc.setAttr('%s.colorR'%each, 0.8309999704)
                mc.setAttr('%s.colorG'%each, 0.4720000029)
                mc.setAttr('%s.colorB'%each, 0)

                mc.setAttr('%s.diffuseRoughness'%each, 0.4269999862)
                mc.setAttr('%s.Ks'%each, 0.7559999824)
                mc.setAttr('%s.KsColorR'%each, 1)
                mc.setAttr('%s.KsColorG'%each, 0.8640000224)
                mc.setAttr('%s.KsColorB'%each, 0.6800000072)
                #mc.setAttr('%s.specularBrdf'%each, 0)
                mc.setAttr('%s.specularRoughness'%each, 0.4390000105)
                mc.setAttr('%s.specularAnisotropy'%each, 0.5)
                mc.setAttr('%s.specularRotation'%each, 0)
                mc.setAttr('%s.Kr'%each, 0)

                mc.setAttr('%s.KrColorR'%each, 1)
                mc.setAttr('%s.KrColorG'%each, 1)
                mc.setAttr('%s.KrColorB'%each, 1)
                mc.setAttr('%s.reflectionExitColorR'%each, 0)
                mc.setAttr('%s.reflectionExitColorG'%each, 0)
                mc.setAttr('%s.reflectionExitColorB'%each, 0)
                mc.setAttr('%s.reflectionExitUseEnvironment'%each, 0)

                mc.setAttr('%s.Kt'%each, 0)
                mc.setAttr('%s.KtColorR'%each, 1)
                mc.setAttr('%s.KtColorG'%each, 1)
                mc.setAttr('%s.KtColorB'%each, 1)
                mc.setAttr('%s.transmittanceR'%each, 1)
                mc.setAttr('%s.transmittanceG'%each, 1)
                mc.setAttr('%s.transmittanceB'%each, 1)
                mc.setAttr('%s.refractionRoughness'%each, 0)
                mc.setAttr('%s.refractionExitColorR'%each, 0)
                mc.setAttr('%s.refractionExitColorG'%each, 0)
                mc.setAttr('%s.refractionExitColorB'%each, 0)
                mc.setAttr('%s.refractionExitUseEnvironment'%each, 0)
                mc.setAttr('%s.IOR'%each, 1)
                mc.setAttr('%s.Kb'%each, 0)
                mc.setAttr('%s.Fresnel'%each, 0)
                mc.setAttr('%s.Krn'%each, 0)
                mc.setAttr('%s.specularFresnel'%each, 1)
                mc.setAttr('%s.Ksn'%each, 1)
                mc.setAttr('%s.FresnelUseIOR'%each, 0)
                mc.setAttr('%s.FresnelAffectDiff'%each, 1)
                mc.setAttr('%s.emission'%each, 0)
                mc.setAttr('%s.emissionColorR'%each, 1)
                mc.setAttr('%s.emissionColorG'%each, 1)
                mc.setAttr('%s.emissionColorB'%each, 1)
                mc.setAttr('%s.directSpecular'%each, 1)
                mc.setAttr('%s.indirectSpecular'%each, 1)
                mc.setAttr('%s.directDiffuse'%each, 1)
                mc.setAttr('%s.indirectDiffuse'%each, 1)
                mc.setAttr('%s.enableGlossyCaustics'%each, 0)
                mc.setAttr('%s.enableReflectiveCaustics'%each, 0)
                mc.setAttr('%s.enableRefractiveCaustics'%each, 0)
                mc.setAttr('%s.enableInternalReflections'%each, 1)

                mc.setAttr('%s.Ksss'%each, 0)
                mc.setAttr('%s.KsssColorR'%each, 1)
                mc.setAttr('%s.KsssColorG'%each, 1)
                mc.setAttr('%s.KsssColorB'%each, 1)
                mc.setAttr('%s.sssRadiusR'%each, 0.1000000015)
                mc.setAttr('%s.sssRadiusG'%each, 0.1000000015)
                mc.setAttr('%s.sssRadiusB'%each, 0.1000000015)
                mc.setAttr('%s.bounceFactor'%each, 1)
                mc.setAttr('%s.opacityR'%each, 1)
                mc.setAttr('%s.opacityG'%each, 1)
                mc.setAttr('%s.opacityB'%each, 1)


    

OCT_TextureLibrary().show()
