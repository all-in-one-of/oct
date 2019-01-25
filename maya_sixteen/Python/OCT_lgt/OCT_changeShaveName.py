# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os
class changeShaveName():
    def __init__(self):
        pass
    def shaveReName(self):
        noShaveCacheFiles = []
        allOnlyShaveShapes = []
        PROJECT_PATH = mm.eval('getenv "OCTV_PROJECTS"')
        OCT_DRIVE = r'\\octvision.com\cg'
        allShaveShapes = mc.ls(type='shaveHair')
        for eachShape in allShaveShapes:
            allOnlyShaveShapes.append(eachShape.split("|")[-1])
            
        allOnlyShaveShapes = list(set(allOnlyShaveShapes))
        if len(allShaveShapes) > len(allOnlyShaveShapes):
            mc.warning(u"毛发Shave的shapes节点有重名的，将导致同名的Shave使用同一个缓存！")
        myshaveGlobals = "shaveGlobals"
            
        allOnlyShaveShapes = list(set(allOnlyShaveShapes))
        myshaveGlobals = "shaveGlobals"
        if allShaveShapes and myshaveGlobals:
            shavePath = mc.getAttr("%s.tmpDir" % myshaveGlobals)
            if shavePath:
                if shavePath.find('${OCTV_PROJECTS}') >= 0:
                    shavePath = shavePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                elif shavePath.find('z:') >= 0:
                    shavePath = shavePath.replace('z:', OCT_DRIVE)
                elif shavePath.find('Z:') >= 0:
                    shavePath = shavePath.replace('Z:', OCT_DRIVE)
                if not os.path.isdir(shavePath):
                    proPath = mc.workspace(q=True, rd=True)
                    shavePath = os.path.normpath(os.path.join(proPath, shavePath))
                if shavePath.find('z:') >= 0:
                    shavePath = shavePath.replace('z:', OCT_DRIVE)
                elif shavePath.find('Z:') >= 0:
                    shavePath = shavePath.replace('Z:', OCT_DRIVE)
                if os.path.isdir(shavePath):
                    allSahveDirs = os.listdir(shavePath)
                    if allSahveDirs:
                        shaveNames = []
                        for eachDir in allSahveDirs:
                            shaveNames.append(eachDir.split(".")[0])
                        shaveNames = list(set(shaveNames))
                        for eachShape in allShaveShapes:
                            if mc.reference( eachShape,isNodeReferenced=True):
                                mc.confirmDialog(message=u"请先导入参考的文件！")
                                return
                            myName=""
                            if ":" in eachShape.split("|")[-1]:
                                shaveNames=eachShape.replace(":","_")
                                myName=mc.rename(eachShape,shaveNames)
                                eachTran=mc.listRelatives(myName, f=True, p=True)[0]
                                pathTran=eachTran.split("|")
                                if ":" in pathTran[-1]:
                                    tranName=pathTran[-1].replace(":","_")
                                    myName=mc.rename(pathTran[-1],tranName)
                            else:
                                noShaveCacheFiles.append(myshaveGlobals) 
                        
        if not noShaveCacheFiles:
            mc.confirmDialog(message=u"修改shave的名字成功！")
            return
            


