# -*- coding: utf-8 -*-
#!/usr/bin/env python

import maya.cmds as mc
import maya.mel as mm
import os
import re

class ImportAnimData():
    def __init__(self):
        self.allAnimDataObjs = []
        self.fileName = mc.file(q = True, sn = True)
        # self.animCurves = ""
        # self.fileName = mc.file(q = True, sn = True)
        self.allAnimDataDirt = {}
        self.allCharacterAnim = [] 

    def findAnimDataObj(self):
        self.allAnimDataObjs = []
        #查找所有的曲线
        allShapes = mc.ls(dagObjects=True, ni=True,rq=True, type = "nurbsCurve",l = True)
        for shapes in allShapes:
            tempName = shapes.split("|")
            if len(tempName)>2 and (tempName[-2] == "master" or ":master" in tempName[-2]):
                transfName = mc.listRelatives(shapes, p = True, f = True)[0]
                self.allAnimDataObjs.append(transfName)

        for obj in self.allAnimDataObjs:
            name = ""
            if ":allAnim" in obj:
                name = obj.split(":allAnim")[0]
            else:
                name = obj.split("allAnim")[0]

            names = name.split("|")
            for n in names:
                if "_ch" in n:
                    if not n in self.allAnimDataDirt.keys():
                        self.allAnimDataDirt.update({n: [obj]})
                        self.allCharacterAnim.append(n)
                    else:
                        self.allAnimDataDirt[n].append(obj)
                    break
       
    def ListAnimImportObj_UI(self):
        self.findAnimDataObj()
        path = os.path.dirname(self.fileName)
        if mc.window("ListAnimImportObj_UI",  exists=True):
            mc.deleteUI("ListAnimImportObj_UI", window = True)
        mc.window("ListAnimImportObj_UI", title = u"导入动画数据", menuBar = True, widthHeight = (500, 400), resizeToFitChildren = True, sizeable = True)
        mc.formLayout("formLyt", numberOfDivisions = 100)

        one = mc.columnLayout('First_Set',parent = 'formLyt')
        mc.rowLayout('ImportAddress',numberOfColumns = 2,columnAttach2 = ['left','left'],columnWidth2 = [5,260],columnOffset2 =[2,2],adjustableColumn2 = True,parent = 'First_Set')
        mc.text(label=u'导入数据地址',w = 68,parent = 'ImportAddress')
        mc.textField('ProjectAddress',text = path, width = 400,alwaysInvokeEnterCommandOnReturn= True,parent = 'ImportAddress')
        #mc.button(label =u'选择',width = 50,command = lambda*args: self.ImportAnimDataPath(), backgroundColor = (0.9,0.5,0),annotation =u"请输入数据地址",parent = 'ImportAddress')


        two =mc.frameLayout('AnimDataObj', label = u'列出带动画的物体', labelAlign = 'top', borderStyle = 'etchedOut', w=500, h=400, parent = 'formLyt')
        mc.textScrollList('ListAnimDataObj', append = self.allCharacterAnim, allowMultiSelection=True, h = 300, parent = 'AnimDataObj')

        three = mc.columnLayout('Second_Set',parent = 'formLyt')
        mc.rowLayout('ObjButton',numberOfColumns = 2,columnWidth2 =(250,250),columnAlign2=('center', 'center'),height =30,parent = 'Second_Set')
        mc.button( 'selectObj', label=u'选择列表中的对象导入动画',width = 250,command = lambda*args: self.selectAnimObj(), backgroundColor = (0.9,0.5,0),parent = 'ObjButton')
        mc.button( 'AllSelectObj', label=u'列表中所有的物体导入动画',width =250,command = lambda*args: self.allListAnimData(), backgroundColor = (0.9,0.3,0.3),parent = 'ObjButton')
        
        mc.formLayout("formLyt", e = True,  attachForm=[(one, 'top', 5), (one, 'left', 5), (one, 'right', 5), (two, 'left', 5),  (two, 'right', 5), (three, 'left', 5),(three, 'bottom', 5),(three, 'right', 5)],
            attachControl=[(one, 'bottom', 1, two), (two, 'bottom', 1, three)],
            attachNone=[(three, 'top')],
            attachPosition=[(one, 'left', 0, 0), (one, 'top', 0, 0)])        

        mc.showWindow('ListAnimImportObj_UI')

    # def ImportAnimDataPath(self):
    #     # myImportAnimPath = mc.textField('ProjectAddress', query=True, text=True)
    #     getfiles = mc.fileDialog2(fileMode=1,fileFilter="Maya Files (*.anim)",dialogStyle=2)
    #     if getfiles:
    #         mc.textField('ProjectAddress', e = True,text = getfiles[0])

    def selectAnimObj(self):
        if not mc.pluginInfo("animImportExport.mll", q = True,loaded = True):
            mc.loadPlugin("animImportExport.mll")

        myProjectAddress = mc.textField('ProjectAddress', query=True, text=True)
        if myProjectAddress == "":
            mc.confirmDialog(message = u"请输入导入数据的文件")
            return 

        myProjectAddress  = os.path.normpath(myProjectAddress )
        myProjectAddress  = myProjectAddress  .replace('\\', '/')

        allAnimObj = mc.textScrollList('ListAnimDataObj',query = True,selectItem = True)
        if not allAnimObj:
            mc.confirmDialog(message = u"请选择要导入角色数据的文件")
            return

        UnFileName = []
        for anims in allAnimObj:
            animDataName = "%s/%s.anim"%(myProjectAddress, anims)
            if not os.path.isfile(animDataName):
                UnFileName.append(anims)
                continue
            for key in self.allAnimDataDirt.keys():
                if anims == key:
                    try:
                        mc.select(d = True)
                        mc.select(self.allAnimDataDirt[key])
                        mc.file(animDataName, i = True, type = "animImport", ignoreVersion = True, ra = True, mergeNamespacesOnClash = False, namespace = anims, options = ";targetTime=4;copies=1;option=replace;pictures=0;connect=0;", pr = True)
                    except:
                        UnFileName.append(anims)
                        print(u"导出%s角色动画数据出错！"%key)
        # # print allAnimObj
        if UnFileName:
            mc.confirmDialog(message = u"%s文件导入数据出错！"%UnFileName)
            return
        else:
            mc.confirmDialog(message = u"导入动画数据完成！")
            return

    def allListAnimData(self):
        if not mc.pluginInfo("animImportExport.mll", q = True,loaded = True):
            mc.loadPlugin("animImportExport.mll")

        myProjectAddress = mc.textField('ProjectAddress', query=True, text=True)
        if myProjectAddress == "":
            mc.confirmDialog(message = u"请输入导入数据的文件")
            return 

        myProjectAddress  = os.path.normpath(myProjectAddress )
        myProjectAddress  = myProjectAddress  .replace('\\', '/')

        # allAnimObj = mc.textScrollList('ListAnimDataObj',query = True,selectItem = True)
        # if not allAnimObj:
        #     mc.confirmDialog(message = u"请选择要导入角色数据的文件")
        #     return

        UnFileName = []
        # for anims in allAnimObj:
        #     animDataName = "%s/%s.anim"%(myProjectAddress, anims)
        #     if not os.path.isfile(animDataName):
        #         UnFileName.append(anims)
        #         continue
        for key in self.allAnimDataDirt.keys():
            animDataName = "%s/%s.anim"%(myProjectAddress, key)
            if not os.path.isfile(animDataName):
                UnFileName.append(key)
                continue
            try:
                mc.select(d = True)
                mc.select(self.allAnimDataDirt[key])
                mc.file(animDataName, i = True, type = "animImport", ignoreVersion = True, ra = True, mergeNamespacesOnClash = False, namespace = key, options = ";targetTime=4;copies=1;option=replace;pictures=0;connect=0;", pr = True)
            except:
                UnFileName.append(anims)
                print(u"导出%s角色动画数据出错！"%key)

        # # print allAnimObj
        if UnFileName:
            mc.confirmDialog(message = u"%s文件导入数据出错！"%UnFileName)
            return
        else:
            mc.confirmDialog(message = u"导入动画数据完成！")
            return

#ImportAnimData().ListAnimImportObj_UI()
