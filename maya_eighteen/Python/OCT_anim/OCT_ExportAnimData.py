# -*- coding: utf-8 -*-
#!/usr/bin/env python

import maya.cmds as mc
import maya.mel as mm
import os,re

class ExportAnimData():
    def __init__(self):
        self.allAnimDataObjs = []
        self.animCurves = ""
        self.fileName = mc.file(q = True, sn = True)
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
        if not self.allAnimDataObjs:
            mc.confirmDialog(message = u"场景中没有到相应的角色！")
            return

        # #获取所有的动画曲线
        # self.animCurves = mc.ls(type = "animCurve")
        # allAnimData = []
        # for animCurve in self.animCurves:
        #     connections = mc.listConnections(animCurve, s = True, d = False)
        #     #排除去驱动关键帧
        #     if not connections: 
        #         keyframeCount = mc.keyframe(animCurve, q = True, keyframeCount = True)
        #         if keyframeCount:
        #             #获取有动画数据的物体的长名
        #             animDataObj = mc.listConnections(animCurve, s = False, d = True)
        #             if animDataObj:
        #                 animDataName = mc.ls(animDataObj[0], l = True)
        #                 if mc.objectType(animDataName[0]) == "reference":
        #                     continue
        #                 else:
        #                     allAnimData.append(animDataName[0])

        # if allAnimData:
        #     self.allAnimDataObjs = list(set(allAnimData))

        #带动画的物体分类，
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


    def ListAnimDataObj_UI(self):
        self.findAnimDataObj()
        if mc.window("ListAnimDataObj_UI",  exists=True):
            mc.deleteUI("ListAnimDataObj_UI", window = True)
        mc.window("ListAnimDataObj_UI", title = u"导出动画数据", menuBar = True, widthHeight = (500, 400), resizeToFitChildren = True, sizeable = True)
        mc.formLayout("formLyt", numberOfDivisions = 100)
        one =mc.frameLayout('AnimDataObj', label = u'列出带动画的物体', labelAlign = 'top', borderStyle = 'etchedOut', w=500, h=400, parent = 'formLyt')
        mc.textScrollList('ListAnimDataObj', append = self.allCharacterAnim, allowMultiSelection=True, h = 300, parent = 'AnimDataObj')

        two = mc.columnLayout('Second_Set',parent = 'formLyt')
        mc.rowLayout('ObjButton',numberOfColumns = 2,columnWidth2 =(250,250),columnAlign2=('center', 'center'),height =30,parent = 'Second_Set')
        mc.button( 'selectObj',label=u'选择列表中的对象导出动画',width = 250,command = lambda*args: self.selectAnimObj(), backgroundColor = (0.9,0.5,0),parent = 'ObjButton')
        mc.button( 'AllSelectObj',label=u'列表中所有的物体导出动画',width =250,command = lambda*args: self.allListAnimData(), backgroundColor = (0.9,0.3,0.3),parent = 'ObjButton')
        
        mc.formLayout("formLyt", e = True,  attachForm=[(one, 'top', 5), (one, 'left', 5), (one, 'right', 5), (two, 'left', 5), (two, 'bottom', 5), (two, 'right', 5)],
            attachControl=[(one, 'bottom', 1, two)],
            attachNone=[(two, 'top')],
            attachPosition=[(one, 'left', 0, 0), (one, 'top', 0, 0)])        

        mc.showWindow('ListAnimDataObj_UI')

    def selectAnimObj(self):
        if not mc.pluginInfo("animImportExport.mll", q = True,loaded = True):
            mc.loadPlugin("animImportExport.mll")

        filePath = os.path.dirname(self.fileName)
        # fileN = os.path.basename(self.fileName)
        # fileNames = os.path.splitext(fileN)[0] +"_anim"

        animDataName = ""

        # PathAnimFile = mc.getFileList(folder = "%s/"%filePath, filespec = "%s*"%fileNames)
        # if PathAnimFile:
        #     PathAnimFiles = sorted(PathAnimFile)
        #     m = re.findall(r'(\w*[0-9]+)\w*',PathAnimFiles[-1])
        #     num = int(m[0][-3:len(m[0])])+1
        #     nums = '%03d' % num
        #     animDataName = "%s/%s%s"%(filePath, m[0][0:-3], nums)
        # else:
        #     animDataName = "%s/%s_c001.anim"%(filePath, fileNames)

        allAnimObj = mc.textScrollList('ListAnimDataObj',query = True,selectItem = True)
        if not allAnimObj:
            mc.confirmDialog(message = u"请先选择列表中要导出动画数据的角色！")
            return

        allAnimDataName = [] 
        for anims in allAnimObj:
            for key in self.allAnimDataDirt.keys(): 
                if anims == key:
                    
                    animDataName = "%s/%s.anim"%(filePath, key)
                    try:
                        mc.select(d = True)
                        mc.select(self.allAnimDataDirt[key])
                        name = mc.file(animDataName, force = True, options = "precision=8;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1", typ = "animExport", pr = True, es = True)
                        print name 
                        allAnimDataName.append(animDataName)
                    except:
                        print(u"导出%s角色动画数据出错！"%key)
                    

        mc.confirmDialog(message = u"导出动画数据存在%s文件中"%allAnimDataName)
        return

    def allListAnimData(self):
        if not mc.pluginInfo("animImportExport.mll", q = True,loaded = True):
            mc.loadPlugin("animImportExport.mll")

        filePath = os.path.dirname(self.fileName)
        
        allAnimDataName = [] 
        #for anims in allAnimObj:
        for key in self.allAnimDataDirt.keys():

            animDataName = "%s/%s.anim"%(filePath, key)
            try:
                mc.select(d = True)
                mc.select(self.allAnimDataDirt[key])
                name = mc.file(animDataName, force = True, options = "precision=8;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;range=0:10;options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=0;copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1", typ = "animExport", pr = True, es = True)
               # print name 
                allAnimDataName.append(animDataName)
            except:
                print(u"导出%s角色动画数据出错！"%key)

        mc.confirmDialog(message = u"导出动画数据存在%s文件中"%allAnimDataName)
        return
        

#ExportAnimData().ListAnimDataObj_UI()

