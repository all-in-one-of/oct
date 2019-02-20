#!/usr/bin/python
# -*- coding: utf-8 -*- 55

import maya.cmds as mc
import re
import os 
class OCT_convertTexFormat():
    def __init__(self):
        pass 
         
    def OCT_convertTex(self):
        er_Info=""
        #转换前的格式
        tga=mc.checkBox('tga',q=True,value=True)
        exr=mc.checkBox('exr',q=True,value=True)
        tx=mc.checkBox('tx',q=True,value=True)
        tiff=mc.checkBox('tiff',q=True,value=True)
        tif=mc.checkBox('tif',q=True,value=True)
        iff=mc.checkBox('iff',q=True,value=True)
        png=mc.checkBox('png',q=True,value=True)
        hdr=mc.checkBox('hdr',q=True,value=True)
        bmp=mc.checkBox('bmp',q=True,value=True)
        jpg=mc.checkBox('jpg',q=True,value=True)
        psd=mc.checkBox('psd',q=True,value=True)
        #转换后的格式
        jpgs=mc.checkBox('jpgs',q=True,value=True)
        tgas=mc.checkBox('tgas',q=True,value=True)
        exrs=mc.checkBox('exrs',q=True,value=True)
        txs=mc.checkBox('txs',q=True,value=True)
        tiffs=mc.checkBox('tiffs',q=True,value=True)
        tifs=mc.checkBox('tifs',q=True,value=True)
        iffs=mc.checkBox('iffs',q=True,value=True)
        pngs=mc.checkBox('pngs',q=True,value=True)
        hdrs=mc.checkBox('hdrs',q=True,value=True)
        bmps=mc.checkBox('bmps',q=True,value=True)
        if jpgs:
            if tgas or exrs or txs or tiffs or tifs or iffs or pngs or hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return 
        elif tgas:
            if exrs or txs or tiffs or tifs or iffs or pngs or hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return 
        elif exrs:
            if txs or tiffs or tifs or iffs or pngs or hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return
        elif txs:
            if tiffs or tifs or iffs or pngs or hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return
        elif tiffs:
            if tifs or iffs or pngs or hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return
        elif tifs:
            if iffs or pngs or hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return
        elif iffs:
            if pngs or hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return
        elif pngs:
            if hdrs or bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return
        elif hdrs:
            if bmps:
                mc.confirmDialog(message=u"转换成的贴图只能选择一项！")
                return


        texFile=mc.ls(type="file")
        for texT in texFile:
            pathName=mc.getAttr("%s.fileTextureName"%texT)
            splits=pathName.split(".")
            if tga and (splits[1]=="tga" or splits[1]=="TGA"):
                if jpgs:
                    self.OCT_outTransparency(texT,splits[0],"jpg")
                #elif tgas:
                #    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif exr and (splits[1]=="exr" or splits[1]=="EXR"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                #elif exrs:
                #    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif tx and (splits[1]=="tx" or splits[1]=="TX"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                #elif txs:
                #    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif tiff and (splits[1]=="tiff" or splits[1]=="TIFF"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                #elif tiffs:
                #    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif tif and (splits[1]=="tif" or splits[1]=="TIF"):
                if jpgs:
                    self.OCT_outTransparency(texT,splits[0],"jpg")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                #elif tifs:
                #    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif iff and (splits[1]=="iff" or splits[1]=="iff"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
               # elif iffs:
                #    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif png and (splits[1]=="png" or splits[1]=="PNG"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                #elif pngs:
               #     mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif hdr and (splits[1]=="HDR" or splits[1]=="hdr"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
               # elif hdrs:
                #    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif bmp and (splits[1]=="BMP" or splits[1]=="bmp"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                elif tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                # elif bmps:
                #     mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")
            elif jpg and (splits[1]=="JPG" or splits[1]=="jpg"):
                # if jpgs:
                #     mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                if tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                # elif bmps:
                #     mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")

            elif psd and (splits[1]=="PSD" or splits[1]=="psd"):
                if jpgs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.jpg"%splits[0],type="string")
                if tgas:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tga"%splits[0],type="string")
                elif exrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.exr"%splits[0],type="string")
                elif txs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tx"%splits[0],type="string")
                elif tiffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tiff"%splits[0],type="string")
                elif tifs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.tif"%splits[0],type="string")
                elif iffs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.iff"%splits[0],type="string")
                elif pngs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.png"%splits[0],type="string")
                elif hdrs:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.hdr"%splits[0],type="string")
                elif bmps:
                    mc.setAttr("%s.fileTextureName"%texT,"%s.bmp"%splits[0],type="string")


    def OCT_outTransparency(self,texT,splits,formats):
        connections=mc.listConnections(texT,s=False,d=True,connections=True,plugs=True)
        srcPlug=""
        if connections:
            for i in range(0,len(connections),2):
                if "outTransparency" in connections[i]:
                    mc.disconnectAttr(connections[i],connections[i+1])
                    srcPlug=connections[i+1]
                    break

        mc.setAttr("%s.fileTextureName"%texT,"%s.%s"%(splits,formats),type="string")
        if srcPlug:
            fileNode=mc.shadingNode('file',asTexture=True)
            mc.connectAttr("%s.outTransparency"%fileNode,srcPlug)
            connection=mc.listConnections(texT,s=True,d=False,connections=True,plugs=True)
            if connection:
                for i in range(0,len(connection),2):
                    fileConnect=connections[i].replace(texT,fileNode)
                    mc.connectAttr(fileConnect,connection[i+1])
            mc.setAttr("%s.fileTextureName"%fileNode,"%s_tran.%s"%(splits,formats),type="string")   


    def OCT_convertTexFormatUI(self):
        if mc.window("OCT_convertTexFormatUI",q=True,exists=True):
            mc.deleteUI("OCT_convertTexFormatUI")
        mc.window("OCT_convertTexFormatUI",title=u"转换贴图格式",w=400,h=200,sizeable=False)
        mc.columnLayout(adjustableColumn=True)
        mc.text(u"=======被 转 换 的 贴 图 格 式=======")
        mc.setParent("..")
        mc.rowColumnLayout(numberOfRows=1,rowHeight=[1,30])
        mc.text(u"贴图格式：")
        mc.checkBox('tga',l="TGA",value=True)
        mc.checkBox('exr',l="EXR",value=True)
        mc.checkBox('tx',l="TX",value=True)
        mc.checkBox('tiff',l="TIFF",value=True)
        mc.checkBox('tif',l="TIF",value=True)
        mc.checkBox('iff',l="IFF",value=True)
        mc.checkBox('png',l="PNG",value=True)
        mc.checkBox('hdr',l="HDR")
        mc.checkBox('bmp',l="BMP")
        mc.checkBox('jpg',l="JPG")
        mc.checkBox('psd',l="PSD")
        mc.setParent("..")
        mc.columnLayout(adjustableColumn=True)
        mc.text(u"=======转 换 成 的 贴 图 格 式=======")
        mc.setParent("..")
        mc.rowColumnLayout(numberOfRows=1,rowHeight=[1,30])
        mc.text(u"贴图格式：")
        mc.checkBox('jpgs',l="JPG",value=True)
        mc.checkBox('tgas',l="TGA")
        mc.checkBox('exrs',l="EXR")
        mc.checkBox('txs',l="TX")
        mc.checkBox('tiffs',l="TIFF")
        mc.checkBox('tifs',l="TIF")
        mc.checkBox('iffs',l="IFF")
        mc.checkBox('pngs',l="PNG")
        mc.checkBox('hdrs',l="HDR")
        mc.checkBox('bmps',l="BMP")
        mc.setParent("..")
        mc.columnLayout(adjustableColumn=True)
        mc.button(l="OK",h=30,c=lambda *args:self.OCT_convertTex())
        #mc.button(l="Close")
        mc.showWindow("OCT_convertTexFormatUI")
            
