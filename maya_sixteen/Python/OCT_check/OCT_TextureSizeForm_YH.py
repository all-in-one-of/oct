#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import re
import os 
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class checkTextureSize():
    def __init__(self):
        self.mySizeDict = {}

    def textureSize(self):
        er_Info=""
        self.mySizeDict.clear()
        mc.textScrollList("textureSize", e = True, ra = True)
        max = mc.intFieldGrp('maxs',q=True,value1=True)
        fileNames = mc.ls(type="file")
        if fileNames:
            for fileName in fileNames:
                imageName = mc.getAttr(fileName+".ftn")
                if imageName:
                    ImageoutSizeX = mc.getAttr(fileName+".outSizeX")
                    ImageoutSizeY = mc.getAttr(fileName+".outSizeY")
                    if ImageoutSizeX>max or ImageoutSizeY>max:
                    #    er_Info += imageName + u"分辨率为("+ str(ImageoutSizeX)+","+str(ImageoutSizeY)+u")\n"
                    #else:
                        er_Info = imageName + u"分辨率为("+ str(ImageoutSizeX)+","+str(ImageoutSizeY)+u")\n"
                        er_Info = er_Info.strip()
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureSize",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureSize"))
                        else:
                            self.mySizeDict[er_Info].append(fileName)     
            #mc.scrollField('textureSize', e = True, text=er_Info)                 

    def selectListTexture(self, textureSize):
        selectTexture = mc.textScrollList(textureSize, q = True, selectItem = True)
        selectList = []
        mc.select(d = True)
        for sel in selectTexture:
            for files in self.mySizeDict[sel]:
                selectList.append(files)
        mc.select(selectList)

    def textureForm(self):
        self.mySizeDict.clear()
        er_Info=""
        jpg=mc.checkBox('jpg',q=True,value=True)
        hdr=mc.checkBox('hdr',q=True,value=True)
        tx=mc.checkBox('tx',q=True,value=True)
        tiff=mc.checkBox('tiff',q=True,value=True)
        iff=mc.checkBox('iff',q=True,value=True)
        png=mc.checkBox('png',q=True,value=True)
        tga=mc.checkBox('tga',q=True,value=True)
        bmp=mc.checkBox('bmp',q=True,value=True)
        
        mc.textScrollList("textureForm", e = True, ra = True)

        fileNames=mc.ls(type="file")
        if fileNames:
            for fileName in fileNames:
                imageName=mc.getAttr(fileName+".ftn")
                form=os.path.splitext(imageName)
                print form[-1]
                if not jpg:
                    if form[-1]=='.jpg' or form[-1]=='.JPG' or form[-1]=='.jpeg' or form[-1]=='.JPEG':
                        #er_Info+=imageName+u'图片格式为(jpg、jpeg)\n'
                        er_Info = imageName+u'图片格式为(jpg、jpeg)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName)  
                        continue
                if not hdr:
                    if form[-1]=='.hdr' or form[-1]=='.HDR':
                        er_Info=imageName+u'图片格式为(hdr)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName)  
                        continue
                
                if not tx:
                    if form[-1]=='.tx' or form[-1]=='.TX':
                        er_Info=imageName+u'图片格式为(tx)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName) 
                        continue
                if not tiff:
                    if form[-1]=='.tif' or form[-1]=='.TIF':
                        er_Info=imageName+u'图片格式为(tif)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName) 
                        continue   
                if not iff:
                    if form[-1]=='.iff' or form[-1]=='.IFF':
                        er_Info=imageName+u'图片格式为(iff)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName) 
                        continue
                if not png:
                    print form[-1]
                    if form[-1]=='.png' or form[-1]=='.PNG':
                        er_Info=imageName+u'图片格式为(png)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName) 
                        continue
                if not tga:
                    if form[-1]=='.tga' or form[-1]=='.TGA':
                        er_Info=imageName+u'图片格式为(tga)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName) 
                        continue
                if not bmp:
                    if form[-1]=='.bmp' or form[-1]=='.BMP':
                        er_Info=imageName+u'图片格式为(bmp)\n'
                        if not er_Info in self.mySizeDict.keys():
                            self.mySizeDict.update({er_Info : [fileName]})
                            mc.textScrollList("textureForm",e = True,append = er_Info, sc = lambda *args:self.selectListTexture("textureForm"))          
                        else:
                            self.mySizeDict[er_Info].append(fileName) 
                        continue
            #mc.scrollField('textureForm', e = True, text=er_Info)


    def checkTextureSizeFormUI(self):
        if mc.window("TextureSizeForm",q=True,exists=True):
            mc.deleteUI("TextureSizeForm")
        mc.window("TextureSizeForm",title="TextureSizeForm",w=100,h=200,sizeable=False)
        mc.rowColumnLayout ("WinColumnLayout",numberOfColumns=1,rowSpacing=[1,1])
        mc.intFieldGrp("maxs",numberOfFields=1,label='max', value1=4096)
        mc.setParent("..")
        uiTextSCameras = mc.textScrollList('textureSize', aas=True, allowMultiSelection=True, p="WinColumnLayout")
        #mc.textScrollList("textureSize",w=400,h=180,bgc=(0.3,0.3,0.3))
        #mc.scrollField('textureSize',p="WinColumnLayout",ed =False, wordWrap=True, text='')
        mc.separator(p = 'WinColumnLayout',st = 'none')
        #mc.rowColumnLayout("SelectList", p = "WinColumnLayout", numberOfColumns=2)
        mc.button(p = 'WinColumnLayout', l = u"检查贴图分辨率", h=30, w = 200, c = lambda *args:self.textureSize())
        #mc.button(p = 'SelectList', l = u"选择贴图", h=30, w = 200)
        mc.setParent("..")
        mc.rowColumnLayout(numberOfRows=1,rowHeight=[1,30], p = "WinColumnLayout")
        mc.text(u"贴图格式：")
        mc.checkBox('jpg',l="JPG",value=True)
        mc.checkBox('hdr',l="HDR",value=True)
        mc.checkBox('tx',l="TX",value=True)
        mc.checkBox('tiff',l="TIF")
        mc.checkBox('iff',l="IFF")
        mc.checkBox('png',l="PNG")
        mc.checkBox('tga',l="TGA")
        mc.checkBox('bmp',l="BMP")
        #mc.scrollField('textureForm',p="WinColumnLayout",ed =False, wordWrap=True, text='')
        uiTextSCameras = mc.textScrollList('textureForm', aas=True, allowMultiSelection=True, p="WinColumnLayout")
        mc.separator(p='WinColumnLayout',st = 'none')
        mc.button(p='WinColumnLayout',l=u"检查贴图的格式",h=30,c=lambda *args:self.textureForm())
        mc.showWindow("TextureSizeForm")


#checkTextureSize().checkTextureSizeFormUI()

