#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os 

OCT_ImagePath = r'\\octvision.com\CG\Tech\matLib'

assertText = {u'自然物质':[u'岩石', u'山体', u'石块', u'土', u'沙'],
            u'人造材料':[u'砖', u'水泥墙面', u'水泥地面', u'大理石', u'石条(石材)', u'朔料',u'金属',
            u'玻璃', u'陶器', u'陶瓷', u'蜡', u'木材',  u'布料', u'书(纸)', u'车漆',u'白炽灯', u'食品', u'皮革'],
            u'植物':[u'树叶', u'树干', u'花瓣', u'灌木枝干'],
            u'液体':[u'水', u'牛奶', u'咖啡', u'油'],
            u'动物':[u'人类皮肤', '恐龙皮肤', u'眼球', u'牙齿', u'指甲']}

class OCT_TextureLibrary():
    def __init__(self):
        # #自然物质
        # self.naMatter = {u'自然物质': [u'岩石', u'山体', u'石块', u'土', u'沙']}
        # #人造材料
        # self.artifMaterial = {u'人造材料': [u'砖', u'水泥墙面', u'水泥地面', u'大理石', u'石条(石材)', u'朔料',u'金属',
        #                 u'玻璃', u'陶器', u'陶瓷', u'蜡', u'木材',  u'布料', u'书(纸)', u'车漆',u'白炽灯', u'食品']}
        # #植物
        # self.botany = {u'植物': [u'树叶', u'树干', u'花瓣', u'灌木枝干']}
        # #液体
        # self.liquid = {u'液体': [u'水', u'牛奶', u'咖啡', u'油']}
        # #动物
        # self.animal = {u'动物': [u'人类皮肤', '恐龙皮肤', u'眼球', u'牙齿', u'指甲'}
        self._windowSize = (720, 700)
        self._windowName = 'textureLib_UI'
        #arnold材质
        self.allArnolds = []
    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName)

    def show(self):
        self.close()
        win = mc.window(self._windowName, wh = self._windowSize, t = u'材质质感库', sizeable = False)
        layout = mc.formLayout()
        control = mc.treeView('control', parent = layout, abr = False )

        scroll = mc.scrollLayout('scroll', p = layout)
       
        mc.formLayout(layout,e = True, attachForm = [(control,'top', 2), (control,'left', 2), (control,'bottom', 2),
            (scroll,'top', 2), (scroll,'right', 2), (scroll,'bottom', 2)],
            attachPosition = [(control, 'left', 0, 0), (control, 'right', 0, 25), (scroll, 'left', 0, 25),
            (scroll, 'right', 0, 99)])

        for key in assertText.keys():
            mc.treeView(control, e = True, addItem = (key, ''))
            for typeName in assertText[key]:
                mc.treeView(control, e = True, addItem = (typeName, key))

        mc.treeView(control, e = True, selectCommand = self.selectTreeCallBack)  
        mc.showWindow(win)

        if not mc.pluginInfo('mtoa.mll',q = True,l = True):
            mc.loadPlugin('mtoa.mll')
        
    ##################选择属性裂变执行按钮##############
    def selectTreeCallBack(self, *args):
        #mc.confirmDialog(message = args[0])
        if mc.rowColumnLayout('RowColum', q = True, ex = True):
            mc.deleteUI('RowColum')
        name = mc.treeView('control', q = True, itemSelected = True)
        listRowColum = mc.rowColumnLayout('RowColum', numberOfColumns = 4, p = 'scroll')
        #####################自然物质######################
        if args[0] == u'土' or args[0] == u'自然物质':
            self.iconButton_UI('clay', u'自然物质\土\黏土', u'黏土', 'clay')
        if args[0] == u'岩石' or args[0] == u'自然物质':
            self.iconButton_UI('stone03', u'自然物质\岩石\花岗岩', u'花岗岩', 'stone')

        #####################人造材料######################  
        if args[0] == u'砖' or args[0] == u'人造材料':
            self.iconButton_UI('stone01', u'自然物质\砖\石砖', u'石砖', 'stone')
        if args[0] == u'大理石' or args[0] == u'人造材料':
            self.iconButton_UI('stone02', u'自然物质\大理石\大理石', u'大理石', 'stone')

        if args[0] == u'朔料' or args[0] == u'人造材料':
            self.iconButton_UI('bloon', u'人造材料\朔料\气球', u'气球', 'plastic')
            self.iconButton_UI('mattPlastic', u'人造材料\朔料\哑光塑料', u'哑光塑料', 'plastic')
            self.iconButton_UI('plastic', u'人造材料\朔料\塑料', u'塑料', 'plastic')
            self.iconButton_UI('shinyPlastic', u'人造材料\朔料\闪光塑料', u'闪光塑料', 'plastic')
            self.iconButton_UI('silkMattPlastic', u'人造材料\朔料\丝绸哑光塑料', u'丝绸哑光塑料', 'plastic')
            self.iconButton_UI('softPlastic', u'人造材料\朔料\软塑料', u'软塑料', 'plastic')
            self.iconButton_UI('toyPlastic', u'人造材料\朔料\玩具塑料', u'玩具塑料', 'plastic')
            self.iconButton_UI('rubber01', u'人造材料\朔料\橡胶01', u'橡胶01', 'plastic')
            self.iconButton_UI('rubber02', u'人造材料\朔料\橡胶02', u'橡胶02', 'plastic')
            
        if args[0] == u'金属' or args[0] == u'人造材料':
            self.iconButton_UI('gold', u'人造材料\金属\金', u'金', 'gold')
            self.iconButton_UI('gold01', u'人造材料\金属\金01', u'金01', 'gold')
            self.iconButton_UI('chrome01', u'人造材料\金属\铬01', u'铬01', 'gold')
            self.iconButton_UI('chrome02', u'人造材料\金属\铬02', u'铬02', 'gold')
            self.iconButton_UI('wheelRim', u'人造材料\金属\轮毂', u'轮毂', 'gold')
            self.iconButton_UI('copper01', u'人造材料\金属\铜01', u'铜01', 'gold')
            self.iconButton_UI('copper02', u'人造材料\金属\铜02', u'铜02', 'gold')

        if args[0] == u'玻璃' or args[0] == u'人造材料':
            self.iconButton_UI('glass01', u'人造材料\玻璃\玻璃01', u'玻璃01', 'glass')
            self.iconButton_UI('glass02', u'人造材料\玻璃\玻璃02', u'玻璃02', 'glass')
            self.iconButton_UI('glass03', u'人造材料\玻璃\玻璃03', u'玻璃03', 'glass')
            self.iconButton_UI('glass04', u'人造材料\玻璃\玻璃04', u'玻璃04', 'glass')

        if args[0] == u'陶瓷' or args[0] == u'人造材料':
            self.iconButton_UI('ceramic01', u'人造材料\陶瓷\陶瓷01', u'陶瓷01', 'ceramic')

        if args[0] == u'木材' or args[0] == u'人造材料':
            for i in range(1, 7):
                data = '%02d'%int(i)
                if os.path.isfile(r'%s\wood\wood%s.jpg'%(OCT_ImagePath, data)):
                    self.iconButton_UI('wood%s'%data, u'人造材料\木材\木材%s'%data, u'木材%s'%data, 'wood')

        if args[0] == u'布料' or args[0] == u'人造材料':
            for i in range(1, 15):
                data = '%02d'%int(i)
                if os.path.isfile(r'%s\cloth\cloth%s.jpg'%(OCT_ImagePath, data)):
                    self.iconButton_UI('cloth%s'%data, u'人造材料\布料\布料%s'%data, u'布料%s'%data, 'cloth')

        if args[0] == u'车漆' or args[0] == u'人造材料':
            self.iconButton_UI('carPaint01', u'人造材料\车漆\车漆01', u'车漆01', 'carPaint')
            self.iconButton_UI('metallicCarPaint', u'人造材料\车漆\金属感车漆', u'金属感车漆', 'carPaint')
            
        if args[0] == u'食品' or args[0] == u'人造材料':
            self.iconButton_UI('Chotolate', u'人造材料\食品\巧克力', u'巧克力', 'food')

        if args[0] == u'皮革' or args[0] == u'人造材料':
            self.iconButton_UI('leather01', u'人造材料\皮革\皮革01', u'皮革01', 'leather')
            self.iconButton_UI('leather02', u'人造材料\皮革\皮革02', u'皮革02', 'leather')
            self.iconButton_UI('leather03', u'人造材料\皮革\皮革03', u'皮革03', 'leather')

    ######################图片按钮UI#####################   
    def iconButton_UI(self, types, pathName, iconName, dirname):
        dIconName = '%s(%s).jpg'%(types, iconName)
        dIconPath =  os.path.join(OCT_ImagePath, dirname, dIconName)

        mc.nodeIconButton(types, style = 'iconAndTextVertical', numberOfPopupMenus = True, ann = pathName, image1 = r"%s\%s\%s.jpg"%(OCT_ImagePath, dirname, types), label = iconName, h = 135, w = 135, p = "RowColum", c = lambda *arg:self.AttrCassIfication(types, dIconPath, 0))
        mc.popupMenu(types, parent = types, b = 3 )
        mc.menuItem(l = u'创建', c = lambda *arg:self.AttrCassIfication(types, dIconPath, 1), parent = types)
        mc.menuItem(l = u'设置', c = lambda *arg:self.AttrCassIfication(types, dIconPath, 2), parent = types)

    ##################设置材质属性分类###################
    def AttrCassIfication(self, types, dIconPath, num):
        ########打开图片########
        self.allArnolds = []
        if num == 0:
            os.startfile(dIconPath)
            return
        ########创建材质########
        elif num == 1:
            aiSShader = mc.shadingNode('aiStandard', asShader = True, n = types)
            aiSShaderSG = mc.sets(renderable = True, noSurfaceShader = True, empty = True, name = '%sSG'%aiSShader)
            self.allArnolds.append(aiSShader)
        ######查找arnold材质######
        elif num == 2:
            self.allArnolds = mc.ls(sl = True, type = "aiStandard")
            if not self.allArnolds:
                mc.confirmDialog(message = u'请选择需要设置属性的arnold材质！', button = 'OK')
                return
        #######################人造材料####################### 
        if types == 'bloon' and num != 0:
            self.setBloonAttr()
        elif types == 'mattPlastic' and num != 0:
            self.setMattPlastticAttr()
        elif types == 'toyPlastic' and num != 0:
            self.setToyPlasticAttr()
        elif types == 'shinyPlastic' and num != 0:
            self.setShinyPlasticAttr()
        elif types == 'silkMattPlastic' and num != 0:
            self.setSilkMattPlasticAttr()
        # elif types == 'silkMattPlastic1' and num != 0:
        #     self.setSilkMattPlastic1Attr()
        elif types == 'softPlastic' and num != 0:
            self.setSoftPlasticAttr()
        elif types == 'rubber01' and num != 0:
            self.setRubber01Attr()
        elif types == 'rubber02':
            self.setRubber02Attr()
        elif types == 'gold' and num != 0:
            self.setGoldAttr()
        elif types == 'chrome01' and num != 0 :
            self.setChrome01Attr()
        elif types == 'chrome02' and num != 0:
            self.setChrome02Attr()
        elif types == 'wheelRim' and num != 0:
            self.setWheelRimAttr()
        elif types == 'glass01' and num != 0:
            self.setGalss01Attr()
        elif types == 'ceramic01' and num != 0:
            self.setCeramic01Attr()
        elif types == 'wax' and num != 0:
            self.setWaxAttr()
        elif types == 'carPaint01' and num != 0:
            self.setCarPaint01Attr()
        elif types == 'metallicCarPaint' and num != 0:
            self.setMetallicCarPaintAttr()
        elif types == 'Chotolate' and num != 0:
            self.setChotolateAttr()
        #######################自然物质####################### 
        elif types == 'clay' and num != 0:
            self.setClayAttr()
        else:
            mc.confirmDialog(message = u'目前还没添加属性设置！', button = 'OK')
            return

    ######################设置属性值######################
    def setAttrValue(self, nodeAttr, value):
        try:
            mc.setAttr(nodeAttr, value)
        except:
            pass

    #######################人造材料####################### 
    ######################设置金属性######################
    def setGoldAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                             'FresnelAffectDiff': True,
                             'FresnelUseIOR': False,
                             'IOR': 1.0,
                             'Kb': 0.0,
                             'Kd': 0.699999988079071,
                             'Kr': 0.0,
                             'KrColorB': 1.0,
                             'KrColorG': 1.0,
                             'KrColorR': 1.0,
                             'Krn': 0.0,
                             'Ks': 0.7559999823570251,
                             'KsColorB': 0.6800000071525574,
                             'KsColorG': 0.8640000224113464,
                             'KsColorR': 1.0,
                             'Ksn': 1.0,
                             'Ksss': 0.0,
                             'KsssColorB': 1.0,
                             'KsssColorG': 1.0,
                             'KsssColorR': 1.0,
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
                             'colorG': 0.47200000286102295,
                             'colorR': 0.8309999704360962,
                             'diffuseRoughness': 0.4269999861717224,
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
                             'specularRoughness': 0.4390000104904175,
                             'sssRadiusB': 0.10000000149011612,
                             'sssRadiusG': 0.10000000149011612,
                             'sssRadiusR': 0.10000000149011612,
                             'transmittanceB': 1.0,
                             'transmittanceG': 1.0,
                             'transmittanceR': 1.0} 
         
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    ######################设置气球属性####################
    def setBloonAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                     'FresnelAffectDiff': True,
                     'FresnelUseIOR': False,
                     'IOR': 1.0,
                     'Kb': 1.0,
                     'Kd': 0.699999988079071,
                     'Kr': 0.0,
                     'KrColorB': 1.0,
                     'KrColorG': 1.0,
                     'KrColorR': 1.0,
                     'Krn': 0.0,
                     'Ks': 0.22200000286102295,
                     'KsColorB': 1.0,
                     'KsColorG': 1.0,
                     'KsColorR': 1.0,
                     'Ksn': 0.5559999942779541,
                     'Ksss': 0.4000000059604645,
                     'KsssColorB': 0.9120000004768372,
                     'KsssColorG': 0.7699999809265137,
                     'KsssColorR': 1.0,
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
                     'colorB': 1.0,
                     'colorG': 0.9269999861717224,
                     'colorR': 0.781000018119812,
                     'diffuseRoughness': 0.4230000078678131,
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
                     'specularRoughness': 0.453000009059906,
                     'sssRadiusB': 0.10000000149011612,
                     'sssRadiusG': 0.10000000149011612,
                     'sssRadiusR': 0.10000000149011612,
                     'transmittanceB': 1.0,
                     'transmittanceG': 1.0,
                     'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass
                
    ####################设置哑光朔料属性##################
    def setMattPlastticAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                 'FresnelAffectDiff': True,
                 'FresnelUseIOR': False,
                 'IOR': 1.0,
                 'Kb': 0.0,
                 'Kd': 0.699999988079071,
                 'Kr': 0.0,
                 'KrColorB': 1.0,
                 'KrColorG': 1.0,
                 'KrColorR': 1.0,
                 'Krn': 0.0,
                 'Ks': 0.26499998569488525,
                 'KsColorB': 0.5379999876022339,
                 'KsColorG': 0.5379999876022339,
                 'KsColorR': 0.5379999876022339,
                 'Ksn': 0.0,
                 'Ksss': 0.0,
                 'KsssColorB': 1.0,
                 'KsssColorG': 1.0,
                 'KsssColorR': 1.0,
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
                 'specularFresnel': False,
                 'specularRotation': 0.0,
                 'specularRoughness': 0.5730000138282776,
                 'sssRadiusB': 0.10000000149011612,
                 'sssRadiusG': 0.10000000149011612,
                 'sssRadiusR': 0.10000000149011612,
                 'transmittanceB': 1.0,
                 'transmittanceG': 1.0,
                 'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass
   
    ####################设置玩具朔料属性##################
    def setToyPlasticAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                     'FresnelAffectDiff': True,
                     'FresnelUseIOR': False,
                     'IOR': 1.0,
                     'Kb': 0.0,
                     'Kd': 0.699999988079071,
                     'Kr': 0.0,
                     'KrColorB': 1.0,
                     'KrColorG': 1.0,
                     'KrColorR': 1.0,
                     'Krn': 0.0,
                     'Ks': 0.23999999463558197,
                     'KsColorB': 0.7850000262260437,
                     'KsColorG': 0.7850000262260437,
                     'KsColorR': 0.7850000262260437,
                     'Ksn': 0.675000011920929,
                     'Ksss': 0.10000000149011612,
                     'KsssColorB': 0.32600000500679016,
                     'KsssColorG': 0.5490000247955322,
                     'KsssColorR': 0.2540000081062317,
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
                     'colorB': 0.32600000500679016,
                     'colorG': 0.5389999747276306,
                     'colorR': 0.2639999985694885,
                     'diffuseRoughness': 0.0,
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
                     'specularRoughness': 0.4000000059604645,
                     'sssRadiusB': 0.10000000149011612,
                     'sssRadiusG': 0.10000000149011612,
                     'sssRadiusR': 0.10000000149011612,
                     'transmittanceB': 1.0,
                     'transmittanceG': 1.0,
                     'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    ####################设置闪光朔料属性##################
    def setShinyPlasticAttr(self):
        setAttrValueDir = {}
        setAttrValueDir =  {'Fresnel': False,
                         'FresnelAffectDiff': True,
                         'FresnelUseIOR': False,
                         'IOR': 1.0,
                         'Kb': 0.0,
                         'Kd': 0.699999988079071,
                         'Kr': 0.0,
                         'KrColorB': 1.0,
                         'KrColorG': 1.0,
                         'KrColorR': 1.0,
                         'Krn': 0.0,
                         'Ks': 0.5370000004768372,
                         'KsColorB': 0.6179999709129333,
                         'KsColorG': 0.6179999709129333,
                         'KsColorR': 0.6179999709129333,
                         'Ksn': 0.699999988079071,
                         'Ksss': 0.0,
                         'KsssColorB': 1.0,
                         'KsssColorG': 1.0,
                         'KsssColorR': 1.0,
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
                         'diffuseRoughness': 0.21400000154972076,
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
                         'specularRoughness': 0.3580000102519989,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass
       
    ##################设置丝绸哑光朔料属性################
    def setSilkMattPlasticAttr(self):
        setAttrValueDir = {}
        setAttrValueDir =  {'Fresnel': False,
                         'FresnelAffectDiff': True,
                         'FresnelUseIOR': False,
                         'IOR': 1.0,
                         'Kb': 0.0,
                         'Kd': 0.699999988079071,
                         'Kr': 0.0,
                         'KrColorB': 1.0,
                         'KrColorG': 1.0,
                         'KrColorR': 1.0,
                         'Krn': 0.0,
                         'Ks': 0.7559999823570251,
                         'KsColorB': 1.0,
                         'KsColorG': 1.0,
                         'KsColorR': 1.0,
                         'Ksn': 0.0,
                         'Ksss': 0.0,
                         'KsssColorB': 1.0,
                         'KsssColorG': 1.0,
                         'KsssColorR': 1.0,
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
                         'diffuseRoughness': 1.0,
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
                         'specularFresnel': False,
                         'specularRotation': 0.0,
                         'specularRoughness': 0.7889999747276306,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    ######################设置软塑胶属性###################
    def setSoftPlasticAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                         'FresnelAffectDiff': True,
                         'FresnelUseIOR': False,
                         'IOR': 1.0,
                         'Kb': 0.0,
                         'Kd': 0.699999988079071,
                         'Kr': 0.0,
                         'KrColorB': 1.0,
                         'KrColorG': 1.0,
                         'KrColorR': 1.0,
                         'Krn': 0.0,
                         'Ks': 0.4000000059604645,
                         'KsColorB': 0.26499998569488525,
                         'KsColorG': 0.26499998569488525,
                         'KsColorR': 0.26499998569488525,
                         'Ksn': 0.0,
                         'Ksss': 0.4000000059604645,
                         'KsssColorB': 0.30000001192092896,
                         'KsssColorG': 0.7549999952316284,
                         'KsssColorR': 1.0,
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
                         'colorB': 0.8999999761581421,
                         'colorG': 0.8999999761581421,
                         'colorR': 0.8999999761581421,
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
                         'specularFresnel': False,
                         'specularRotation': 0.0,
                         'specularRoughness': 0.6700000166893005,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0}

        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    ######################设置橡胶01属性###################
    def setRubber01Attr(self):
        setAttrValueDir = {}
        setAttrValueDir =  {'Fresnel': False,
                             'FresnelAffectDiff': True,
                             'FresnelUseIOR': False,
                             'IOR': 1.0,
                             'Kb': 0.800000011920929,
                             'Kd': 0.699999988079071,
                             'Kr': 0.0,
                             'KrColorB': 1.0,
                             'KrColorG': 1.0,
                             'KrColorR': 1.0,
                             'Krn': 0.0,
                             'Ks': 0.6000000238418579,
                             'KsColorB': 0.9268329739570618,
                             'KsColorG': 0.9268329739570618,
                             'KsColorR': 0.9268329739570618,
                             'Ksn': 0.6000000238418579,
                             'Ksss': 1.0,
                             'KsssColorB': 0.38909003138542175,
                             'KsssColorG': 0.6155736446380615,
                             'KsssColorR': 0.9490000009536743,
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
                             'colorB': 0.7699999809265137,
                             'colorG': 0.9093953371047974,
                             'colorR': 1.0,
                             'diffuseRoughness': 0.20000000298023224,
                             'directDiffuse': 1.0,
                             'directSpecular': 1.0,
                             'dispersionAbbe': 0.0,
                             'emission': 0.0,
                             'emissionColorB': 0.9118333458900452,
                             'emissionColorG': 0.7699999809265137,
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
                             'sssRadiusB': 0.8989852666854858,
                             'sssRadiusG': 0.8989852666854858,
                             'sssRadiusR': 1.0,
                             'transmittanceB': 1.0,
                             'transmittanceG': 1.0,
                             'transmittanceR': 1.0} 
 
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    ######################设置橡胶02属性###################
    def setRubber02Attr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                             'FresnelAffectDiff': True,
                             'FresnelUseIOR': False,
                             'IOR': 1.0,
                             'Kb': 1.0,
                             'Kd': 0.699999988079071,
                             'Kr': 0.0,
                             'KrColorB': 1.0,
                             'KrColorG': 1.0,
                             'KrColorR': 1.0,
                             'Krn': 0.0,
                             'Ks': 0.30000001192092896,
                             'KsColorB': 0.9268329739570618,
                             'KsColorG': 0.9268329739570618,
                             'KsColorR': 0.9268329739570618,
                             'Ksn': 0.6000000238418579,
                             'Ksss': 1.0,
                             'KsssColorB': 0.07300001382827759,
                             'KsssColorG': 0.6137499809265137,
                             'KsssColorR': 1.0,
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
                             'colorG': 0.23594999313354492,
                             'colorR': 1.0,
                             'diffuseRoughness': 0.20000000298023224,
                             'directDiffuse': 1.0,
                             'directSpecular': 1.0,
                             'dispersionAbbe': 0.0,
                             'emission': 0.0,
                             'emissionColorB': 0.9118333458900452,
                             'emissionColorG': 0.7699999809265137,
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
                             'sssRadiusB': 0.5,
                             'sssRadiusG': 0.5,
                             'sssRadiusR': 0.5,
                             'transmittanceB': 1.0,
                             'transmittanceG': 1.0,
                             'transmittanceR': 1.0}
        
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass
                                 
    #######################设置铬01属性#####################
    def setChrome01Attr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                         'FresnelAffectDiff': True,
                         'FresnelUseIOR': False,
                         'IOR': 1.0,
                         'Kb': 0.0,
                         'Kd': 0.0,
                         'Kr': 0.0,
                         'KrColorB': 1.0,
                         'KrColorG': 1.0,
                         'KrColorR': 1.0,
                         'Krn': 0.0,
                         'Ks': 1.0,
                         'KsColorB': 1.0,
                         'KsColorG': 1.0,
                         'KsColorR': 1.0,
                         'Ksn': 0.7319999933242798,
                         'Ksss': 0.0,
                         'KsssColorB': 1.0,
                         'KsssColorG': 1.0,
                         'KsssColorR': 1.0,
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
                         'colorB': 1.0,
                         'colorG': 1.0,
                         'colorR': 1.0,
                         'diffuseRoughness': 0.0,
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
                         'specularRoughness': 0.0,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    #######################设置铬1属性#####################
    def setChrome02Attr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
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
                         'Ks': 1.0,
                         'KsColorB': 1.0,
                         'KsColorG': 1.0,
                         'KsColorR': 1.0,
                         'Ksn': 0.7319999933242798,
                         'Ksss': 0.0,
                         'KsssColorB': 1.0,
                         'KsssColorG': 1.0,
                         'KsssColorR': 1.0,
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
                         'colorB': 1.0,
                         'colorG': 1.0,
                         'colorR': 1.0,
                         'diffuseRoughness': 0.0,
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
                         'specularRoughness': 0.0,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0} 
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass
    
    #######################设置轮毂属性#####################
    def setWheelRimAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                         'FresnelAffectDiff': True,
                         'FresnelUseIOR': False,
                         'IOR': 1.0,
                         'Kb': 0.0,
                         'Kd': 0.20000000298023224,
                         'Kr': 0.0,
                         'KrColorB': 1.0,
                         'KrColorG': 1.0,
                         'KrColorR': 1.0,
                         'Krn': 0.0,
                         'Ks': 0.800000011920929,
                         'KsColorB': 1.0,
                         'KsColorG': 1.0,
                         'KsColorR': 1.0,
                         'Ksn': 0.0,
                         'Ksss': 0.5730000138282776,
                         'KsssColorB': 1.0,
                         'KsssColorG': 1.0,
                         'KsssColorR': 1.0,
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
                         'colorB': 0.6710000038146973,
                         'colorG': 0.6710000038146973,
                         'colorR': 0.6710000038146973,
                         'diffuseRoughness': 0.0,
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
                         'specularFresnel': False,
                         'specularRotation': 0.0,
                         'specularRoughness': 0.30000001192092896,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0} 
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    #######################设置玻璃1属性#####################
    def setGalss01Attr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                             'FresnelAffectDiff': True,
                             'FresnelUseIOR': True,
                             'IOR': 1.5,
                             'Kb': 0.0,
                             'Kd': 0.0,
                             'Kr': 0.0,
                             'KrColorB': 1.0,
                             'KrColorG': 1.0,
                             'KrColorR': 1.0,
                             'Krn': 0.0,
                             'Ks': 1.0,
                             'KsColorB': 1.0,
                             'KsColorG': 1.0,
                             'KsColorR': 1.0,
                             'Ksn': 0.0,
                             'Ksss': 0.0,
                             'KsssColorB': 1.0,
                             'KsssColorG': 1.0,
                             'KsssColorR': 1.0,
                             'Kt': 1.0,
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
                             'specularRoughness': 0.0,
                             'sssRadiusB': 0.10000000149011612,
                             'sssRadiusG': 0.10000000149011612,
                             'sssRadiusR': 0.10000000149011612,
                             'transmittanceB': 1.0,
                             'transmittanceG': 1.0,
                             'transmittanceR': 1.0}
       
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    ########################设置陶瓷属性#####################
    def setCeramic01Attr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
                             'FresnelAffectDiff': True,
                             'FresnelUseIOR': False,
                             'IOR': 1.0,
                             'Kb': 0.0,
                             'Kd': 0.699999988079071,
                             'Kr': 0.0,
                             'KrColorB': 1.0,
                             'KrColorG': 1.0,
                             'KrColorR': 1.0,
                             'Krn': 0.0,
                             'Ks': 0.6499999761581421,
                             'KsColorB': 1.0,
                             'KsColorG': 1.0,
                             'KsColorR': 1.0,
                             'Ksn': 0.10000000149011612,
                             'Ksss': 0.30000001192092896,
                             'KsssColorB': 1.0,
                             'KsssColorG': 1.0,
                             'KsssColorR': 1.0,
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
                             'colorB': 1.0,
                             'colorG': 1.0,
                             'colorR': 1.0,
                             'diffuseRoughness': 0.0,
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
                             'specularRoughness': 0.0,
                             'sssRadiusB': 0.10000000149011612,
                             'sssRadiusG': 0.10000000149011612,
                             'sssRadiusR': 0.10000000149011612,
                             'transmittanceB': 1.0,
                             'transmittanceG': 1.0,
                             'transmittanceR': 1.0} 
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass
    #########################设置蜡属性#######################
    def setWaxAttr(self):
         if self.allArnolds:
            for each in self.allArnolds:
                self.setAttrValue('%s.aiEnableMatte'%each, 0)
                self.setAttrValue('%s.aiMatteColorR'%each, 0)
                self.setAttrValue('%s.aiMatteColorG'%each, 0)
                self.setAttrValue('%s.aiMatteColorB'%each, 0)
                self.setAttrValue('%s.aiMatteColorA'%each, 0)

                self.setAttrValue('%s.Kd'%each, 0.3000000119)
                self.setAttrValue('%s.colorR'%each, 0.8999999762)
                self.setAttrValue('%s.colorG'%each, 0.8999999762)
                self.setAttrValue('%s.colorB'%each, 0.8999999762)

                self.setAttrValue('%s.diffuseRoughness'%each, 0.5299999714)
                self.setAttrValue('%s.Ks'%each, 0.5469999909)
                self.setAttrValue('%s.KsColorR'%each, 1)
                self.setAttrValue('%s.KsColorG'%each, 1)
                self.setAttrValue('%s.KsColorB'%each, 1)
                #self.setAttrValue('%s.specularBrdf'%each, 0)
                self.setAttrValue('%s.specularRoughness'%each, 0.6000000238)
                self.setAttrValue('%s.specularAnisotropy'%each, 0.5)
                self.setAttrValue('%s.specularRotation'%each, 0)
                self.setAttrValue('%s.Kr'%each, 0)

                self.setAttrValue('%s.KrColorR'%each, 1)
                self.setAttrValue('%s.KrColorG'%each, 1)
                self.setAttrValue('%s.KrColorB'%each, 1)
                self.setAttrValue('%s.reflectionExitColorR'%each, 0)
                self.setAttrValue('%s.reflectionExitColorG'%each, 0)
                self.setAttrValue('%s.reflectionExitColorB'%each, 0)
                self.setAttrValue('%s.reflectionExitUseEnvironment'%each, 0)

                self.setAttrValue('%s.Kt'%each, 0)
                self.setAttrValue('%s.KtColorR'%each, 1)
                self.setAttrValue('%s.KtColorG'%each, 1)
                self.setAttrValue('%s.KtColorB'%each, 1)
                self.setAttrValue('%s.transmittanceR'%each, 1)
                self.setAttrValue('%s.transmittanceG'%each, 1)
                self.setAttrValue('%s.transmittanceB'%each, 1)
                self.setAttrValue('%s.refractionRoughness'%each, 0)
                self.setAttrValue('%s.refractionExitColorR'%each, 0)
                self.setAttrValue('%s.refractionExitColorG'%each, 0)
                self.setAttrValue('%s.refractionExitColorB'%each, 0)
                self.setAttrValue('%s.refractionExitUseEnvironment'%each, 0)
                self.setAttrValue('%s.IOR'%each, 1)
                self.setAttrValue('%s.Kb'%each, 1)
                self.setAttrValue('%s.Fresnel'%each, 0)
                self.setAttrValue('%s.Krn'%each, 0)
                self.setAttrValue('%s.specularFresnel'%each, 1)
                self.setAttrValue('%s.Ksn'%each, 0)
                self.setAttrValue('%s.FresnelUseIOR'%each, 0)
                self.setAttrValue('%s.FresnelAffectDiff'%each, 1)

                self.setAttrValue('%s.emission'%each, 0)
                self.setAttrValue('%s.emissionColorR'%each, 1)
                self.setAttrValue('%s.emissionColorG'%each, 1)
                self.setAttrValue('%s.emissionColorB'%each, 1)
                self.setAttrValue('%s.directSpecular'%each, 1)
                self.setAttrValue('%s.indirectSpecular'%each, 1)
                self.setAttrValue('%s.directDiffuse'%each, 1)
                self.setAttrValue('%s.indirectDiffuse'%each, 1)
                self.setAttrValue('%s.enableGlossyCaustics'%each, 0)
                self.setAttrValue('%s.enableReflectiveCaustics'%each, 0)
                self.setAttrValue('%s.enableRefractiveCaustics'%each, 0)
                self.setAttrValue('%s.enableInternalReflections'%each, 1)

                self.setAttrValue('%s.Ksss'%each, 0.5730000138)
                self.setAttrValue('%s.KsssColorR'%each, 1)
                self.setAttrValue('%s.KsssColorG'%each, 1)
                self.setAttrValue('%s.KsssColorB'%each, 1)
                self.setAttrValue('%s.sssRadiusR'%each, 0.1000000015)
                self.setAttrValue('%s.sssRadiusG'%each, 0.1000000015)
                self.setAttrValue('%s.sssRadiusB'%each, 0.1000000015)
                self.setAttrValue('%s.bounceFactor'%each, 1)
                self.setAttrValue('%s.opacityR'%each, 1)
                self.setAttrValue('%s.opacityG'%each, 1)
                self.setAttrValue('%s.opacityB'%each, 1)

    #########################设置车漆属性#####################
    def setCarPaint01Attr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': True,
                             'FresnelAffectDiff': True,
                             'FresnelUseIOR': False,
                             'IOR': 1.0,
                             'Kb': 0.0,
                             'Kd': 0.699999988079071,
                             'Kr': 0.0,
                             'KrColorB': 1.0,
                             'KrColorG': 1.0,
                             'KrColorR': 1.0,
                             'Krn': 0.0,
                             'Ks': 1.0,
                             'KsColorB': 1.0,
                             'KsColorG': 1.0,
                             'KsColorR': 1.0,
                             'Ksn': 0.02005000039935112,
                             'Ksss': 0.16300000250339508,
                             'KsssColorB': 0.0,
                             'KsssColorG': 0.0,
                             'KsssColorR': 0.5,
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
                             'colorR': 1.0,
                             'diffuseRoughness': 0.0,
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
                             'specularRoughness': 0.0,
                             'sssRadiusB': 0.10000000149011612,
                             'sssRadiusG': 0.10000000149011612,
                             'sssRadiusR': 0.10000000149011612,
                             'transmittanceB': 1.0,
                             'transmittanceG': 1.0,
                             'transmittanceR': 1.0} 
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    #######################设置金属车漆属性###################
    def setMetallicCarPaintAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': True,
                     'FresnelAffectDiff': True,
                     'FresnelUseIOR': False,
                     'IOR': 1.0,
                     'Kb': 0.0,
                     'Kd': 0.699999988079071,
                     'Kr': 1.0,
                     'KrColorB': 1.0,
                     'KrColorG': 1.0,
                     'KrColorR': 1.0,
                     'Krn': 0.0,
                     'Ks': 0.44999998807907104,
                     'KsColorB': 1.0,
                     'KsColorG': 0.9440000057220459,
                     'KsColorR': 0.5789999961853027,
                     'Ksn': 0.4000000059604645,
                     'Ksss': 0.0,
                     'KsssColorB': 1.0,
                     'KsssColorG': 1.0,
                     'KsssColorR': 1.0,
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
                     'colorB': 1.0,
                     'colorG': 0.4659999907016754,
                     'colorR': 0.20200000703334808,
                     'diffuseRoughness': 0.0,
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
                     'specularRoughness': 0.5899999737739563,
                     'sssRadiusB': 0.10000000149011612,
                     'sssRadiusG': 0.10000000149011612,
                     'sssRadiusR': 0.10000000149011612,
                     'transmittanceB': 1.0,
                     'transmittanceG': 1.0,
                     'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass
    
    ########################设置巧克力属性####################
    def setChotolateAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': True,
                         'FresnelAffectDiff': True,
                         'FresnelUseIOR': False,
                         'IOR': 1.0,
                         'Kb': 0.0,
                         'Kd': 1.0,
                         'Kr': 0.10000000149011612,
                         'KrColorB': 1.0,
                         'KrColorG': 1.0,
                         'KrColorR': 1.0,
                         'Krn': 0.10000000149011612,
                         'Ks': 0.20000000298023224,
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
                         'colorB': 0.21199999749660492,
                         'colorG': 0.27300000190734863,
                         'colorR': 0.38499999046325684,
                         'diffuseRoughness': 0.37599998712539673,
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
                         'specularRoughness': 0.30000001192092896,
                         'sssRadiusB': 0.10000000149011612,
                         'sssRadiusG': 0.10000000149011612,
                         'sssRadiusR': 0.10000000149011612,
                         'transmittanceB': 1.0,
                         'transmittanceG': 1.0,
                         'transmittanceR': 1.0}
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass

    #######################自然物质####################### 
    ###########################黏土#######################
    def setClayAttr(self):
        setAttrValueDir = {}
        setAttrValueDir = {'Fresnel': False,
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
        if self.allArnolds:
            for each in self.allArnolds:
                for key in setAttrValueDir.keys():
                    try:
                        mc.setAttr('%s.%s' % (each, key), setAttrValueDir[key])
                    except:
                        pass 

OCT_TextureLibrary().show()
