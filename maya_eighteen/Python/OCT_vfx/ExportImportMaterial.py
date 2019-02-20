# -*- coding: utf-8 -*-
#!/usr/bin/env python

import maya.cmds as mc
import maya.mel as mm
import os
import time
import re

#导入导出材质连接信息，保证物体名相同。
class ExportImportMaterial():
    
    def __init__(self):
        self.fileSName = mc.file(q=True, sn=True)

        self.myDirct = {}

    def ShadingEngine_W(self):
        fileName = os.path.splitext(self.fileSName)
        temp = r"%s.txt"%fileName[0]
        fileId = open(temp, 'w')

        shadingGrp = mc.ls(type = "shadingEngine")
        if shadingGrp:
            for shading in shadingGrp:
                objs = mc.sets(shading, q = True)
                if objs:
                    name = mc.listConnections("%s.surfaceShader"%shading, s = True, d= True)
                    if name == "lambert1":
                        mc.confirmDialog(message = u'请不要把物体连接到lambert1材质上！')
                        return
                    for obj in objs:
                       # buf = mc.ls(obj, long = True)
                        buf = mc.ls(obj)
                        try:
                            fileId.write("%s\t%s\r\n"%(name[0],buf[0]))
                        except:
                            print "写入文件出错";
                        
        fileId.close()
        time.sleep(1)
        mc.confirmDialog(message = u"数据读取完成！")
        return

#ExportImportMaterial().ShadingEngine_W()


    def ShadingEngine_UI(self):
        if mc.window('Read_shadingEngine', exists=True):
            mc.deleteUI('Read_shadingEngine', window=True)
        getWindow=mc.window('Read_shadingEngine',wh=(300,100),resizeToFitChildren=1,sizeable=True)  
        mc.formLayout('formLyt', numberOfDivisions=100)
        one = mc.columnLayout('First_Set',parent = 'formLyt')
        mc.text(l = "", h =30,parent = 'First_Set')
        mc.rowLayout('materialPath',numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnWidth3 = [5,260,35],columnOffset3 =[2,2,2],adjustableColumn3 = True,parent = 'First_Set')
        mc.text(label=u'材质文件路径(mb)：',w = 75, h = 30, parent = 'materialPath')
        mc.textField('materialAddress',text = '',width = 250, h = 30, alwaysInvokeEnterCommandOnReturn= True,parent = 'materialPath')
        mc.button(label =u'选择路径', width = 50, h = 30, command =lambda*args: self.getPath() , annotation =u"请材质文件路径", parent = 'materialPath')
        
        mc.rowLayout('materialInfo',numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnWidth3 = [5,260,35],columnOffset3 =[2,2,2],adjustableColumn3 = True,parent = 'First_Set')
        mc.text(label=u'材质信息路径(txt)：',w = 75, h = 30, parent = 'materialInfo')
        mc.textField('materialInfoAddress',text = '',width = 250, h = 30, alwaysInvokeEnterCommandOnReturn= True,parent = 'materialInfo')
        mc.button(label =u'选择路径', width = 50, h = 30, c = lambda*args: self.getInfoPath())
        
        mc.text(l = "", h =30, parent = 'First_Set')
        mc.rowLayout(numberOfColumns=4,columnWidth4=(80,120,120,20),columnAlign4=('center','center','center','center'), parent = 'First_Set')
        mc.text(l='',vis=0)
        mc.button(l='OK',w=80,h=30, align='center',c=lambda*args: self.ShadingEngine_R())
        mc.button(l='Close',width=80,h=30,c=('mc.deleteUI(\"'+getWindow+'\",window=True)'))
        mc.text(l='',vis=0)
        mc.setParent('..')
        mc.showWindow(getWindow)


    def getPath(self):
        path = mc.fileDialog2(fileMode = True, fileFilter = "mayaBinary(*.mb)")
        mc.textField("materialAddress", e = True, text = path[0])

    def getInfoPath(self):
        path = mc.fileDialog2(fileMode = True, fileFilter = "txt(*.txt)")
        mc.textField("materialInfoAddress", e = True, text = path[0])

    def ShadingEngine_R(self):
        materialAddress = mc.textField("materialAddress", q = True, text = True)
        materialInfoAddress = mc.textField("materialInfoAddress", q = True, text = True)
        if not os.path.isfile(materialAddress):
            mc.confirmDialog(message = u'文件不存在！')
            return
        if not os.path.isfile(materialInfoAddress):
            mc.confirmDialog(message = u'文件不存在！')
            return
        path = os.path.splitext(materialAddress)
        pathName = os.path.basename(path[0])
        mc.file(materialAddress, i = True, type = "mayaBinary", ignoreVersion = True, ra = True, mergeNamespacesOnClash = False, namespace = pathName, options = "v=0;", pr = True)

        f = file(materialInfoAddress, 'r')
        infoStr = f.readlines()
        f.close()
        self.myDirct.clear()
        for i in range(len(infoStr)):
            infoStr[i] = infoStr[i][:-2]
            # print infoStr[i]
            name = infoStr[i].split('\t')
            shaingGrp = name[0]
            if not shaingGrp in self.myDirct.keys():
                self.myDirct.update({shaingGrp:[name[1]]})
            else:
                self.myDirct[shaingGrp].append(name[1])
        
        allMats = mc.ls(mat = True)
        for key in self.myDirct.keys():
            materialName = ""
            shade = key.split(":")[-1]
            for mat in allMats:
                pattern1 = re.compile('^(\w+)(:%s)$'%shade)
                m = pattern1.match(mat)
                if not m:
                    pattern2 = re.compile('^(\w+):(\w+)(:%s)$'%shade)
                    m = pattern2.match(mat)
                if m:
                    materialName = m.group()
                    continue

            if mc.objExists(materialName):
                nameSG = mc.sets(renderable= True, noSurfaceShader = True, empty = True, name = (materialName+"SG"))
                mc.connectAttr("%s.outColor"%materialName, "%s.surfaceShader"%nameSG, f = True)
               
                for meshs in self.myDirct[key]:
                    if mc.objExists(meshs):
                        mc.sets(meshs, e = True, forceElement = nameSG)
                    else:
                        name = "_".join(meshs.split("_")[0:-1])
                        listName = mc.ls("%s*"%name)
                        mc.sets(listName[0], e = True, forceElement = nameSG)

        mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
        time.sleep(1)
        mc.confirmDialog(message = u"材质连接完成！")
        return

#ExportImportMaterial().ShadingEngine_UI()
