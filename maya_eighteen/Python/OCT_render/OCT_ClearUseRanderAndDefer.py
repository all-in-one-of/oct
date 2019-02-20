#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm
class OCT_ClearUseRander():
    def __init__(self):
        self.allAiStandIn = ""

    def clearUseRender_UI(self):
        if mc.window(u"clearUseRender_UI", ex = True):
            mc.deleteUI(u"clearUseRender_UI")

        windowRef = mc.window(u"clearUseRender_UI", t = u"渲染问题解决", menuBar = True, widthHeight = [325, 200], resizeToFitChildren = True, sizeable = True)
        mc.formLayout('formLyt', numberOfDivisions=100)
        mc.frameLayout('deferStandinLoad', label=u'更新延迟信息(勾上、取消，点update添加、取消延迟)', labelAlign='top', borderStyle='etchedOut', w=325, parent='formLyt')
        mc.rowLayout(numberOfColumns=2, columnWidth2=(270, 20))
        mc.checkBox("deferS", l = "deferStandinLoad")
        mc.button("UpdateDefer", l = "Update", c = lambda*args:self.UnDeferStandinLoad())
        mc.setParent('..')

        mc.frameLayout(u"clearUseNode", l = u"删除下列无用节点", labelAlign = "center",  borderStyle = 'etchedIn')
        mc.columnLayout('Xml_Type', adjustableColumn=True)
        mc.button("shaveGlobals", l = u"删除shaveGlobals", c = lambda*args:self.OCT_deleteShave())
        mc.button("mentalrayGlobals", l = u"删除mentalrayGlobals", c = lambda*args:self.OCT_deleteMentalray())
        mc.button("mentalrayAndShave", l = u"删除mentalrayGlobals、shaveGlobals", c = lambda*args:self.OCT_deleteMentalrayShave())
        mc.showWindow("clearUseRender_UI")

    def OCT_deleteMentalray(self):
        try:
            mc.delete('mentalrayGlobals')
        except:
            print "not mentalrayGlobals"
            pass
    def OCT_deleteShave(self):
        try:
            
            mc.delete('shaveGlobals')
        except:
            print "not shaveGlobals"
            pass

    def OCT_deleteMentalrayShave(self):
        self.OCT_deleteMentalray()
        self.OCT_deleteShave()

    def UnDeferStandinLoad(self):
        self.allAiStandIn = mc.ls(type = "aiStandIn")
        defer = mc.checkBox("deferS", q= True, v= True)
        if defer:
            for aiS in self.allAiStandIn:
                mc.setAttr("%s.deferStandinLoad"%aiS,1)
        else:
            for aiS in self.allAiStandIn:
                mc.setAttr("%s.deferStandinLoad"%aiS,0)

    

#OCT_ClearUseRander().clearUseRender_UI()