#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm
import os

OCT_DRIVE = r'\\octvision.com\CG'

class ChangeReference():

    def __init__(self):
        #查找所有的物体
        self.allReference = ""
        
    def changeRef_UI(self):
        if mc.window(u"ChangeRef_UI", ex = True):
            mc.deleteUI(u"ChangeRef_UI")

        windowRef = mc.window(u"ChangeRef_UI", t = u"Change Reference Path", menuBar = True, widthHeight = [350, 400], resizeToFitChildren = True, sizeable = True)
        mc.formLayout('formLyt', numberOfDivisions=400)
        mc.columnLayout('Xml_Type', adjustableColumn=True)

        mc.radioButtonGrp("RefOption", columnAlign3=('left','left','left'), columnWidth3=(100,100,100), numberOfRadioButtons = 2, label = u"Ref Option:", labelArray2 = [u"All", "Select"], sl=1, enable=True)
        
        mc.frameLayout(u"ReplacePath", l = u"替换参考路径", labelAlign = "center",  borderStyle = 'etchedIn' )
        mc.rowLayout(numberOfColumns = 3, columnWidth3 = (40, 260, 80), adjustableColumn = 2, columnAlign=(1, 'left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
        mc.text(l = u"输入路径:")
        mc.textField("replacePath")
        mc.button("replaceOK", l = "OK", command = lambda*args: self.replaceRefPath())
        mc.setParent("..")

        mc.frameLayout(u"ChangePath", l = u"批量转换同一文件", labelAlign = "center",  borderStyle = 'etchedIn')
        mc.rowLayout(numberOfColumns = 4, columnWidth4 = (40, 220, 80, 80), adjustableColumn = 3, columnAlign=(1, 'left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0), (4, 'both', 0)])
        mc.text(l = u"原路径：")
        mc.textField('oldPath', editable = False)
        mc.button("Option1", l = u"Option", c = lambda*args: self.ReferencePathChange(1))
        mc.text(l = "")
        mc.setParent("..")
        mc.rowLayout(numberOfColumns = 4, columnWidth4 = (40, 220, 80, 80),adjustableColumn = 3, columnAlign=(1, 'left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0), (4, 'both', 0)])
        mc.text(l = u"新路径：")
        mc.textField('newPath', editable = False)
        mc.button("Option2", l = u"Option", c = lambda*args: self.ReferencePathChange(2))
        mc.button("ChangePathOK", l = u"OK", c = lambda*args: self.referenceFiles())
        mc.setParent("..")

        mc.frameLayout(u"ChangeHMLPath", l = u"高中低模转换", labelAlign = "center",  borderStyle = 'etchedIn')
        mc.rowLayout(numberOfColumns = 3, columnWidth3 = (150, 150, 150), adjustableColumn = 2, columnAlign=(1, 'left'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)])
        mc.button("L", l = "L", c = lambda*args:self.renameReferenceFileL())
        mc.button("M", l = "M", c = lambda*args:self.renameReferenceFileM())
        mc.button("H", l = "H", c = lambda*args:self.renameReferenceFileH())
        mc.setParent("..")

        mc.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 220), (2, 220)])
        mc.button("texTomsAnim", l = u"_h_msNoTex转换成_h_msAnim", c = lambda*args:self.renameReferenceFileNoTex())
        mc.button("msAnimToTex", l = u"_h_msAnim转换成_h_msNoTex", c = lambda*args:self.renameReferenceFileAnim())

        mc.button("mc_msAnimToh_msAnim", l = u"_mc_msAnim转换成_h_msAnim", c = lambda*args:self.renameReferencemc_AnimChangeToh_Anim())
        mc.button("h_msAnimTomc_msAnim", l = u"_h_msAnim转换成_mc_msAnim", c = lambda*args:self.renameReferenceh_AnimChangeTomc_Anim())

        mc.button("txTomsAnim", l = u"_tx转换成_msAnim", c = lambda*args:self.Reference_texToMaster())
        mc.button("rgTomsAnim", l = u"_rg转换成_msAnim", c = lambda*args:self.Reference_rigToMaster())
        mc.showWindow(u"ChangeRef_UI")

    #替换路径，输入路径转换成目标目录下的相同文件
    def replaceRefPath(self):
        allDirNotFile = []

        dirText = mc.textField("replacePath", q = True, text = True)
        if not os.path.isdir(dirText):
            mc.confirmDialog(message = u"请输入正确路径！")
            return

        selRad = mc.radioButtonGrp("RefOption", q = True, sl = True)
        if selRad == 1:
            self.allReference = mc.file(q=True,reference=True)
        else:
            #查找选择的参考文件
            _gReferenceEditorPanel = mm.eval("global string $gReferenceEditorPanel;string $temp = $gReferenceEditorPanel;")
            
            try:
                self.allReference = mc.sceneEditor(_gReferenceEditorPanel, q = True, selectItem = True)
            except:
                mc.confirmDialog(message = u"请打开参考编辑界面,并选择要替换的参考")
                return

        if self.allReference:
            for eachRef in self.allReference:
                eachRef = eachRef.split('{')[0]
                baseName = os.path.basename(eachRef)
                newFullName = os.path.join(dirText, baseName)
                if os.path.isfile(newFullName):
                    referenceNode = mc.file(eachRef, q=True, referenceNode=True)
                    mc.file(newFullName, loadReference=referenceNode)
                else:
                    allDirNotFile.append(baseName)

        if allDirNotFile:
            mc.confirmDialog(message = u"目标文件夹中不存在%s"%baseName)
            return
            #print u"目标文件夹中不存在%s"%baseName

    #参考同一个文件转换，把旧参考换成新的参考
    def ReferencePathChange(self, j):
        path = mc.fileDialog2(fileMode=1, fileFilter="Maya Files (*.mb)", dialogStyle=2)
        if path:
            if j==1:
                mc.textField('oldPath', e = True, text = path[0])
            elif j==2:
                mc.textField('newPath', e = True, text = path[0])

    def referenceFiles(self):
        oldPath = mc.textField('oldPath', q = True, text = True)
        newPath = mc.textField('newPath', q = True, text = True)

        if not oldPath or not newPath:
            mc.confirmDialog(title = u"提示", message = u"请按Option按钮选择正确的路径!")
            return
        if oldPath.find('z:')>=0:
            oldPath = oldPath.replace('z:', OCT_DRIVE)

        if oldPath.find('Z:')>=0:
            oldPath = oldPath.replace('Z:',OCT_DRIVE)

        if newPath.find('z:')>=0:
            newPath = newPath.replace('z:',OCT_DRIVE)

        if newPath.find('Z:')>=0:
            newPath = newPath.replace('Z:',OCT_DRIVE)

        if not os.path.isfile(newPath):
            mc.confirmDialog(title=u"提示",message=u'请输入正确文件路径例如:Z:\Themes\FKBS\Project\scenes\characters\ch001001Allosaurus\master\FKBS_ch001001Allosaurus_h_msAnim.mb')
            return

        oldPath = oldPath.replace('\\', '/')
        newPath = newPath.replace('\\', '/')
        #print oldPath
        #print newPath
        allReferenceFiles = mc.file(q=True, reference=True)
        for refer in allReferenceFiles:
            refer = refer.split('{')[0]
            if oldPath == refer:
                referenceNode = mc.file(refer, q=True, referenceNode=True)
                mc.file(newPath, loadReference = referenceNode)


    #高中低模转换
    def changeReferenceFiles(self, *args):
        self.allReference = []
        referenceOptions = mc.radioButtonGrp("RefOption", q = True, sl = True)
        if referenceOptions == 1:
            self.allReference = mc.file(q = True, reference = True)
        else:
            _gReferenceEditorPanel = mm.eval("global string $gReferenceEditorPanel;string $temp = $gReferenceEditorPanel;")
            try:
                self.allReference = mc.sceneEditor(_gReferenceEditorPanel, q = True, selectItem = True)
            except:
                mc.confirmDialog(message = u"请打开参考编辑界面,并选择要替换的参考")
                return

    #高、中模转换成低模
    def renameReferenceFileL(self):
        self.changeReferenceFiles()
        for referenceFile in self.allReference:
            fileName = referenceFile.split("/")
            buf = fileName[-1].split("_")
            Name=""
            Names=""
            if 'h' in buf or 'm' in buf:
                flag = False
                if buf[2] == 'h' or buf[2] == 'm':
                    Name = buf[0] + "_" + buf[1] + "_l_" + buf[3]
                    Names = buf[0] + "_" + buf[1] + "_l_msAnim.mb"
                    flag = True

                elif buf[3] == 'h' or buf[3] == 'm':
                    Name = buf[0] + "_" + buf[1] + "_" + buf[2] + "_l_" + buf[4]
                    Names = buf[0] + "_" + buf[1] + "_" + buf[2] + "_l_msAnim.mb"

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print os.path.isfile(fileNames)
                    if os.path.isfile(fileNames):
                        referenceNode=mc.file(referenceFile,q=True,referenceNode=True)
                        mc.file(descfile,loadReference=referenceNode)

    #高、低模转换成中模
    def renameReferenceFileM(self):
        self.changeReferenceFiles()
        for referenceFile in self.allReference:
            fileName = referenceFile.split("/")
            buf = fileName[-1].split("_")
            Name=""
            Names=""
            if 'l' in buf or 'h' in buf:
                flag = False
                if buf[2] == 'l' or buf[2] == 'h':
                    Name = buf[0] + "_" + buf[1] + "_m_" + buf[3]
                    Names = buf[0] + "_" + buf[1] + "_m_msAnim.mb"
                    flag = True

                elif buf[3] == 'l' or buf[2] == 'h':
                    Name = buf[0] + "_" + buf[1] + "_" + buf[2] + "_m_" + buf[4]
                    Names = buf[0] + "_" + buf[1] + "_" + buf[2] + "_m_msAnim.mb"
                    flag = True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print os.path.isfile(fileNames)
                    if os.path.isfile(fileNames):
                        referenceNode=mc.file(referenceFile,q=True,referenceNode=True)
                        mc.file(descfile,loadReference=referenceNode)

    #中、低模转换成高模
    def renameReferenceFileH(self):
        self.changeReferenceFiles()
        for referenceFile in self.allReference:
            fileName = referenceFile.split("/")
            buf = fileName[-1].split("_")
            Name = ""
            Names = ""
            if 'l' in buf or 'm' in buf:
                flag=False
                if buf[2] == 'l' or buf[2] == 'm':
                    Name = buf[0] + '_' + buf[1] + '_h_' + buf[3]
                    Names = buf[0] + '_' + buf[1] + '_h_msAnim.mb'
                    flag = True

                elif buf[3]== 'l' or buf[3] == 'm':
                    Name = buf[0] + "_" + buf[1] + "_" + buf[2] + "_h_" + buf[4]
                    Names = buf[0] + "_" + buf[1] + "_" + buf[2] + "_h_msAnim.mb"
                    flag=True

                if flag:
                    descfile='/'.join(fileName[0:-1])+"/"+Name
                    #srcFile='/'.join(fileName[0:-1])+"/"+srcName
                    fileNames='/'.join(fileName[0:-1])+'/'+Names
                    #print os.path.isfile(fileNames)
                    if os.path.isfile(fileNames):
                        referenceNode = mc.file(referenceFile, q = True, referenceNode = True)
                        mc.file(descfile, loadReference = referenceNode)

    def renameReferenceFileNoTex(self):
        self.changeReferenceFiles()
        for ReferenceFile in self.allReference:
            if "_h_msNoTex" in ReferenceFile:
                referFile = mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName = os.path.dirname(ReferenceFile)+"/"+referFile
                fileName = pathFileName.replace("_h_msNoTex","_h_msAnim")
                if os.path.isfile(fileName):
                    referenceNode = mc.file(ReferenceFile, q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def renameReferenceFileAnim(self):
        self.changeReferenceFiles()
        for ReferenceFile in self.allReference:
            if "_h_msAnim" in ReferenceFile:
                referFile=mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName=os.path.dirname(ReferenceFile)+"/"+referFile
                fileName=pathFileName.replace("_h_msAnim","_h_msNoTex")
                if os.path.isfile(fileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def renameReferencemc_AnimChangeToh_Anim(self):
        self.changeReferenceFiles()
        for ReferenceFile in self.allReference:
            if "_mc_msAnim" in ReferenceFile:
                referFile=mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName=os.path.dirname(ReferenceFile)+"/"+referFile
                fileName=pathFileName.replace("_mc_msAnim","_h_msAnim")
                if os.path.isfile(fileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def renameReferenceh_AnimChangeTomc_Anim(self):
        self.changeReferenceFiles()
        for ReferenceFile in self.allReference:
            if "_h_msAnim" in ReferenceFile:
                referFile=mc.referenceQuery(ReferenceFile,withoutCopyNumber=True,shortName=True,filename=True)
                pathFileName=os.path.dirname(ReferenceFile)+"/"+referFile
                fileName=pathFileName.replace("_h_msAnim","_mc_msAnim")
                if os.path.isfile(fileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(fileName,loadReference=referenceNode)

    def Reference_texToMaster(self):
        self.changeReferenceFiles()
        for ReferenceFile in self.allReference:
            referenList=ReferenceFile.split("/")
            if referenList[-2]=="texture":
                referenceName=referenList[-1].replace("_tx.","_msAnim.")
                referenceName=referenceName.split("{")[0]
                pathFileName="/".join(referenList[0:-2])+"/master/"+referenceName
                if os.path.isfile(pathFileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(pathFileName,loadReference=referenceNode)

    def Reference_rigToMaster(self):
        self.changeReferenceFiles()
        for ReferenceFile in self.allReference:
            referenList=ReferenceFile.split("/")
            if referenList[-2]=="rigging":
                referenceName=referenList[-1].replace("_rg.","_msAnim.")
                referenceName=referenceName.split("{")[0]
                pathFileName="/".join(referenList[0:-2])+"/master/"+referenceName
                if os.path.isfile(pathFileName):
                    referenceNode=mc.file(ReferenceFile,q=True,referenceNode=True)
                    mc.file(pathFileName,loadReference=referenceNode)

#ChangeReference().changeRef_UI()
