#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os
import sys
#面板显示图片路径
OCT_ImagePath = r'\\octvision.com\CG\Tech\matLib' 
#源码分类路径
maLibPath = r'\\octvision.com\CG\Tech\maya_sixteen\Python\OCT_matLib'
# maLibPath = r'D:\MayaSixteenScripts\Python\OCT_matLib'
            
assertText = {u'自然物质':[u'岩石', u'山体', u'石块', u'土', u'沙'],
            u'人造材料':[u'砖', u'水泥墙面', u'水泥地面', u'大理石', u'石条(石材)', u'朔料',u'金属',
            u'玻璃', u'陶器', u'陶瓷', u'蜡', u'木材',  u'布料', u'书(纸)', u'车漆',u'白炽灯', u'食品', u'皮革'],
            u'植物':[u'树叶', u'树干', u'花瓣', u'灌木枝干'],
            u'液体':[u'水', u'牛奶', u'咖啡', u'油'],
            u'动物':[u'人类皮肤', u'恐龙皮肤', u'眼球', u'牙齿', u'指甲']}

class OCT_TextureLibrary():
    def __init__(self):
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
        tabs = mc.tabLayout("tabs")
        arnoldScroll = mc.scrollLayout('arnold', p = tabs)
        vrayScroll = mc.scrollLayout('vray', p = tabs)

        mc.formLayout(layout,e = True, attachForm = [(control,'top', 2), (control,'left', 2), (control,'bottom', 2),
            (tabs,'top', 2), (tabs,'right', 2), (tabs,'bottom', 2)],
            attachPosition = [(control, 'left', 0, 0), (control, 'right', 0, 25), (tabs, 'left', 0, 25),
            (tabs, 'right', 0, 99)])

        for key in assertText.keys():
            mc.treeView(control, e = True, addItem = (key, ''))
            for typeName in assertText[key]:
                mc.treeView(control, e = True, addItem = (typeName, key))

        mc.treeView(control, e = True, selectCommand = self.selectTreeCallBack)  
        mc.showWindow(win)

        if not mc.pluginInfo('mtoa.mll',q = True,l = True):
            mc.loadPlugin('mtoa.mll')

        # name = mc.treeView('control', q = True, itemSelected = True)
        # listRowColum = mc.rowColumnLayout('RowColum', numberOfColumns = 4, p = 'scroll')
        # self.iconButton_UI('clay', u'自然物质\土\黏土', u'黏土', 'clay')
        
    ##################选择属性裂变执行按钮##############
    def selectTreeCallBack(self, *args):
        tabsName = mc.tabLayout("tabs",q=True,selectTab=True)
        if tabsName == 'arnold':
            self.setArnoldMat(args[0])
        elif tabsName == 'vray':
            self.setVrayMat(args[0])
    
    ###################设置vray材质质感################
    def setVrayMat(self, args):
        if mc.rowColumnLayout('vrayRow', q = True, ex = True):
            mc.deleteUI('vrayRow')
        name = mc.treeView('control', q = True, itemSelected = True)
        listRowColum = mc.rowColumnLayout('vrayRow', numberOfColumns = 4, p = 'vray')
        
    ##################设置arnold材质质感###############
    def setArnoldMat(self, args):
        if mc.rowColumnLayout('arnoldRow', q = True, ex = True):
            mc.deleteUI('arnoldRow')
        listRowColum = mc.rowColumnLayout('arnoldRow', numberOfColumns = 4, p = 'arnold')
        #####################自然物质######################
        if args == u'土' or args == u'自然物质':
            self.iconButton_UI('clay', u'自然物质\土\黏土', u'黏土', 'clay')
        if args == u'岩石' or args == u'自然物质':
            self.iconButton_UI('stone03', u'自然物质\岩石\花岗岩', u'花岗岩', 'stone')

        #####################人造材料######################  
        if args == u'砖' or args == u'人造材料':
            self.iconButton_UI('stone01', u'自然物质\砖\石砖', u'石砖', 'stone')
        if args == u'大理石' or args == u'人造材料':
            self.iconButton_UI('stone02', u'自然物质\大理石\大理石', u'大理石', 'stone')

        if args == u'朔料' or args == u'人造材料':
            self.iconButton_UI('bloon', u'人造材料\朔料\气球', u'气球', 'plastic')
            self.iconButton_UI('mattPlastic', u'人造材料\朔料\哑光塑料', u'哑光塑料', 'plastic')
            self.iconButton_UI('plastic', u'人造材料\朔料\塑料', u'塑料', 'plastic')
            self.iconButton_UI('shinyPlastic', u'人造材料\朔料\闪光塑料', u'闪光塑料', 'plastic')
            self.iconButton_UI('silkMattPlastic', u'人造材料\朔料\丝绸哑光塑料', u'丝绸哑光塑料', 'plastic')
            self.iconButton_UI('softPlastic', u'人造材料\朔料\软塑料', u'软塑料', 'plastic')
            self.iconButton_UI('toyPlastic', u'人造材料\朔料\玩具塑料', u'玩具塑料', 'plastic')
            self.iconButton_UI('rubber01', u'人造材料\朔料\橡胶01', u'橡胶01', 'plastic')
            self.iconButton_UI('rubber02', u'人造材料\朔料\橡胶02', u'橡胶02', 'plastic')
            
        if args == u'金属' or args == u'人造材料':
            self.iconButton_UI('gold', u'人造材料\金属\金', u'金', 'gold')
            self.iconButton_UI('gold01', u'人造材料\金属\金01', u'金01', 'gold')
            self.iconButton_UI('chrome01', u'人造材料\金属\铬01', u'铬01', 'gold')
            self.iconButton_UI('chrome02', u'人造材料\金属\铬02', u'铬02', 'gold')
            self.iconButton_UI('wheelRim', u'人造材料\金属\轮毂', u'轮毂', 'gold')
            self.iconButton_UI('copper01', u'人造材料\金属\铜01', u'铜01', 'gold')
            self.iconButton_UI('copper02', u'人造材料\金属\铜02', u'铜02', 'gold')

        if args == u'玻璃' or args == u'人造材料':
            self.iconButton_UI('glass01', u'人造材料\玻璃\玻璃01', u'玻璃01', 'glass')
            self.iconButton_UI('glass02', u'人造材料\玻璃\玻璃02', u'玻璃02', 'glass')
            self.iconButton_UI('glass03', u'人造材料\玻璃\玻璃03', u'玻璃03', 'glass')
            self.iconButton_UI('glass04', u'人造材料\玻璃\玻璃04', u'玻璃04', 'glass')

        if args == u'陶瓷' or args == u'人造材料':
            self.iconButton_UI('ceramic01', u'人造材料\陶瓷\陶瓷01', u'陶瓷01', 'ceramic')

        if args == u'木材' or args == u'人造材料':
            for i in range(1, 7):
                data = '%02d'%int(i)
                if os.path.isfile(r'%s\wood\wood%s.jpg'%(OCT_ImagePath, data)):
                    self.iconButton_UI('wood%s'%data, u'人造材料\木材\木材%s'%data, u'木材%s'%data, 'wood')

        if args == u'布料' or args == u'人造材料':
            for i in range(1, 15):
                data = '%02d'%int(i)
                if os.path.isfile(r'%s\cloth\cloth%s.jpg'%(OCT_ImagePath, data)):
                    self.iconButton_UI('cloth%s'%data, u'人造材料\布料\布料%s'%data, u'布料%s'%data, 'cloth')

        if args == u'车漆' or args == u'人造材料':
            self.iconButton_UI('carPaint01', u'人造材料\车漆\车漆01', u'车漆01', 'carPaint')
            self.iconButton_UI('metallicCarPaint', u'人造材料\车漆\金属感车漆', u'金属感车漆', 'carPaint')
            
        if args == u'食品' or args == u'人造材料':
            self.iconButton_UI('Chotolate', u'人造材料\食品\巧克力', u'巧克力', 'food')

        if args == u'皮革' or args == u'人造材料':
            self.iconButton_UI('leather01', u'人造材料\皮革\皮革01', u'皮革01', 'leather')
            self.iconButton_UI('leather02', u'人造材料\皮革\皮革02', u'皮革02', 'leather')
            self.iconButton_UI('leather03', u'人造材料\皮革\皮革03', u'皮革03', 'leather')

    ######################图片按钮UI#####################   
    def iconButton_UI(self, types, pathName, iconName, dirname):
        tabsName = mc.tabLayout("tabs", q=True, selectTab=True)
        dIconName = '%s(%s).jpg'%(types, iconName)
        dIconPath =  os.path.join(OCT_ImagePath, dirname, dIconName)

        mc.nodeIconButton(types, style = 'iconAndTextVertical', numberOfPopupMenus = True, ann = pathName, image1 = r"%s\%s\%s.jpg"%(OCT_ImagePath, dirname, types), label = iconName, h = 135, w = 135, p = '%sRow'%tabsName, c = lambda *arg:self.AttrCassIfication(types, dIconPath, 0))
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
            if maLibPath not in sys.path:
                sys.path.append (maLibPath)
        ######查找arnold材质######
        elif num == 2:
            if maLibPath not in sys.path:
                sys.path.append (maLibPath)
            self.allArnolds = mc.ls(sl = True, type = "aiStandard")
            if not self.allArnolds:
                mc.confirmDialog(message = u'请选择需要设置属性的arnold材质！', button = 'OK')
                return
        #######################人造材料####################### 
        if types == 'stone01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setStone01Attr()

        elif types == 'stone02' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setStone02Attr()

        elif types == 'bloon' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setBloonAttr()
           
        elif types == 'mattPlastic' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setMattPlastticAttr()
            
        elif types == 'toyPlastic' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setToyPlasticAttr()

        elif types == 'shinyPlastic' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setShinyPlasticAttr()
           
        elif types == 'silkMattPlastic' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setSilkMattPlasticAttr()
            
        # elif types == 'silkMattPlastic1' and num != 0:
        #     self.setSilkMattPlastic1Attr()

        elif types == 'softPlastic' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setSoftPlasticAttr()
            
        elif types == 'rubber01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setRubber01Attr()
            
        elif types == 'rubber02'and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setRubber02Attr()

        elif types == 'gold' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setGoldAttr()

        elif types == 'chrome01' and num != 0 :
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setChrome01Attr()
           
        elif types == 'chrome02' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setChrome02Attr()
            
        elif types == 'wheelRim' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setWheelRimAttr()
           
        elif types == 'glass01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setGalss01Attr()
        
        elif types == 'glass02' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setGlass02Attr()

        elif types == 'glass03' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setGlass03Attr()

        elif types == 'glass04' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setGlass04Attr()

        elif types == 'ceramic01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCeramic01Attr()
            
        # elif types == 'wax' and num != 0:
        #     self.setWaxAttr()

        elif types == 'wood01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setWood01Attr()

        elif types == 'wood02' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setWood02Attr()

        elif types == 'wood03' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setWood03Attr()

        elif types == 'wood04' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setWood04Attr()

        elif types == 'wood05' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setWood05Attr()

        elif types == 'wood06' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setWood06Attr()

        elif types == 'cloth01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth01Attr()
        
        elif types == 'cloth02' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth02Attr()

        elif types == 'cloth03' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth03Attr()

        elif types == 'cloth04' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth04Attr()

        elif types == 'cloth05' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth05Attr()

        elif types == 'cloth07' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth07Attr()

        elif types == 'cloth08' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth08Attr()

        elif types == 'cloth09' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth09Attr()

        elif types == 'cloth10' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth10Attr()

        elif types == 'cloth11' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth11Attr()

        elif types == 'cloth12' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth12Attr()

        elif types == 'cloth13' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth13Attr()

        elif types == 'cloth14' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCloth14Attr()

        elif types == 'carPaint01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setCarPaint01Attr()

        elif types == 'metallicCarPaint' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setMetallicCarPaintAttr()
            
        elif types == 'Chotolate' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setChotolateAttr()

        elif types == 'leather01' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setLeather01Attr()

        elif types == 'leather02' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setLeather02Attr()

        elif types == 'leather03' and num != 0:
            from OCT_ArtificialMateral import OCT_ArtificialMateral as matLib
            matLib(self.allArnolds).setLeather03Attr()
            
        #######################自然物质####################### 
        elif types == 'stone03' and num != 0:
            from OCT_NaturalMatter import OCT_NaturalMatter as matLib
            matLib(self.allArnolds).setStone03Attr()

        elif types == 'clay' and num != 0:
            from OCT_NaturalMatter import OCT_NaturalMatter as matLib
            matLib(self.allArnolds).setClayAttr()
            
        else:
            mc.delete(self.allArnolds)
            mc.confirmDialog(message = u'目前还没添加属性设置！', button = 'OK')
            return


# OCT_TextureLibrary().show()
