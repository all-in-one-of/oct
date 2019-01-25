#!/usr/bin/env python
# coding=utf-8
import maya.cmds as mc
import maya.mel as mm
import os

class ExportSelectObj():
    def __init__(self):
        self.allSelObj = ""
        if mc.objExists("OCT_SelObjSet"):
            mc.delete("OCT_SelObjSet")

    # def selObjSet(self, *args):
    #     self.allSelObj = ""
    #     self.allSelObj = mc.ls(sl = True)
    #     if mc.objExists("OCT_SelObjSet"):
    #         mc.sets(cl="OCT_SelObjSet")
    #         mc.sets(add="OCT_SelObjSet")
    #     else:
    #         mc.sets(n="OCT_SelObjSet")
    #     mc.select(self.allSelObj)
    #     mc.sets(add="OCT_SelObjSet")

    def isolateSelects(self, *args):
        if not self.allSelObj:
            mc.confirmDialog(title='Confirm', message=u'请选择中物体添加到OCT_SelObjSet')
            return

        activePlane = ""
        i = 1
        while(i):
            try:
                tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
            except:
                pass
            else:
                if tmp:
                    activePlane = 'modelPanel%d' % i
                    break
            i+=1
        if activePlane == "":
            mc.confirmDialog(message = u"请在点击主显示窗口",button = u"重新选择")
            return

        mc.select(d = True)
        #print self.allSelObj
        for objs in self.allSelObj:
            mc.select(objs,add = True)
        if mc.isolateSelect(activePlane, q = True, state = True):
            mm.eval("enableIsolateSelect %s false;"%activePlane)
        else:
            mm.eval("enableIsolateSelect %s true;"%activePlane)

    def SelectExport(self, *args):
        if not self.allSelObj:
            mc.confirmDialog(title='Confirm', message=u'请选择中物体添加到OCT_SelObjSet')
            return

        if mc.window("OCT_SelObjSetUI",exists=True):
            mc.deleteUI("OCT_SelObjSetUI",window=True)
        mc.window("OCT_SelObjSetUI", title="OCT_SelObjSetUI",maximizeButton=0,resizeToFitChildren=0,sizeable=1,wh=[355,120])
        mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center',h=70)
        mc.rowLayout(numberOfColumns=2,columnWidth2=(300,60),h=60)
        mc.textFieldGrp('newPath',label='New Path:',text='',editable=True,ct2=('left','left'),cw2=(55,305))
        mc.button("btn4",l="borrow",c = self.borrow)
        mc.setParent("..")
        mc.columnLayout(rowSpacing=5)
        mc.rowLayout(numberOfColumns=3,columnWidth3=(110,110,110),h=30)
        mc.button("btn1", l = u'1、导出到当前目录', w = 120, c = self.CurrentDirExport)
        mc.button("btn2", l = u'2、导出到指定目录', w = 120, c = self.DirExport)
        mc.button("btn3", l = u'3、取消', w = 120, c = 'mc.deleteUI("OCT_SelObjSetUI",window=True)')
        mc.showWindow('OCT_SelObjSetUI')
        # fileName = mc.file(q=True, sn=True)
        # fileName = os.path.splitext(fileName)[0]
        # fileName = fileName + "_deleted"

        # mc.select(d = True)
        # for objs in self.allSelObj:
        #     mc.select(objs,add = True)

        # mc.file(fileName,force= True,options = "v=0;",typ = "mayaBinary",pr = True,es = True)

    def borrow(self, *args):
        getDitr = mc.fileDialog2(caption = "Browse Asset Library", okCaption = "Open", fileMode = 3)
        if getDitr:
            mc.textFieldGrp("newPath",edit= True, text=getDitr[0])

    def DirExport(self, *args):
        newPath=mc.textFieldGrp('newPath',q=True,text=True)
        if os.path.isdir(newPath):
            fileName = mc.file(q=True, sn=True,shn = True)
            fileName = os.path.splitext(fileName)[0]
            fileName = fileName + "_deleted"
            serFilePath = os.path.join(newPath,fileName)

            mc.select(d = True)
            for objs in self.allSelObj:
                mc.select(objs,add = True)
            mc.file(serFilePath,force= True,options = "v=0;",typ = "mayaBinary",pr = True,es = True)
        else:
            mc.confirmDialog(message = u"此目录不存在！",button = u"重新填写")
            return

    def CurrentDirExport(self, *args):
        fileName = mc.file(q=True, sn=True)
        fileName = os.path.splitext(fileName)[0]
        fileName = fileName + "_deleted"

        mc.select(d = True)
        for objs in self.allSelObj:
            mc.select(objs,add = True)

        mc.file(fileName,force= True,options = "v=0;",typ = "mayaBinary",pr = True,es = True)


    def selectAddObj(self, *args):
        selObj = mc.ls(sl = True)
        if self.allSelObj:
            for sel in selObj:
                if not sel in self.allSelObj:
                    self.allSelObj.append(sel)
        else:
            self.allSelObj = selObj


        if mc.objExists("OCT_SelObjSet"):
            mc.sets(cl="OCT_SelObjSet")
            mc.sets(add="OCT_SelObjSet")
        else:
            mc.sets(n="OCT_SelObjSet")
        mc.select(self.allSelObj)
        mc.sets(add="OCT_SelObjSet")

        # if not mc.objExists("OCT_SelObjSet"):
        #     mc.confirmDialog(message = u"OCT_SelObjSet节点不存在")
        #     return
        # selecAdd = mc.ls(sl = True)
        # for sel in selecAdd:
        #     if not sel in self.allSelObj:
        #         self.allSelObj.append(sel) 
    
        # mc.select(d = True)
        # mc.delete("OCT_SelObjSet")
        # mc.sets(n="OCT_SelObjSet")
        # mc.select(self.allSelObj)
        # mc.sets(add="OCT_SelObjSet")

    def removeSelectObj(self, *args):
        if not mc.objExists("OCT_SelObjSet"):
            mc.confirmDialog(message = u"OCT_SelObjSet节点不存在")
            return

        selectAdd = mc.ls(sl = True)
        for sel in selectAdd:
            if sel in self.allSelObj:
               self.allSelObj.remove(sel)

        mc.select(d = True)  
        mc.delete("OCT_SelObjSet")
        mc.sets(n = "OCT_SelObjSet")
        mc.select(self.allSelObj)
        mc.sets(add="OCT_SelObjSet")

    def SelectExportUI(self):
        if mc.window("SelectExportUI",exists=True):
            mc.deleteUI("SelectExportUI",window=True)
        mc.window("SelectExportUI", title="SelectExportUI",maximizeButton=0,resizeToFitChildren=0,sizeable=1,wh=[355,150])
        mc.columnLayout(rowSpacing=3,columnWidth=350,columnAttach=['both',0],parent='SelectExportUI')
        mc.text(l="")
        mc.button('addObj',l=u"选择物体添加到OCT_SelObjectSet",command=self.selectAddObj)
        mc.text(l="")
        mc.button('removeObj',l=u"选择OCT_SelObjectSet下的物体移除sets",command=self.removeSelectObj)
        mc.text(l="")
        mc.button('btn1',l=u"切换显示隐藏OCT_SelObjSet下物体",command=self.isolateSelects)
        mc.text(l="")
        mc.button('Export',l=u"导出OCT_SelObjSet物体",command=self.SelectExport)
        mc.showWindow('SelectExportUI')


#ExportSelectObj().SelectExportUI()
