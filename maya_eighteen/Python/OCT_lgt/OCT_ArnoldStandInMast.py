#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as mc
class ArnoldStandInMast():
    def __init__(self):
        self.windowSize = (200, 150)
        self.windowName = "ArnoldStandInMast_UI"
        self.allArnoldStandIn = []
        # self.allArnoldStandIn = mc.ls(type = 'aiStandIn')

    def close(self):
        if mc.window(self.windowName, q=True, exists=True):
            mc.deleteUI(self.windowName)

    def show(self):
        self.close()
        win = mc.window(self.windowName,
                        t= u'arnold代理做遮罩',
                        wh=self.windowSize,
                        mnb=False, mxb=False, rtf=True, s=False)
        mc.columnLayout()
        self.select = mc.radioButtonGrp('Target', label='Target:', columnAlign3=('both','left','left',),columnWidth3=(50,90,90), labelArray2=['All In Scene', 'selected'], numberOfRadioButtons=2, sl=1)
        mc.separator()
        mc.rowLayout( numberOfColumns=2, columnWidth2=(310, 75))
        self.Matte = mc.radioButtonGrp('Matte', label='Matte:', columnAlign4=('both','left','left','left'),columnWidth4=(50,90,90, 90), labelArray3=['Mute', 'On', 'Off'], numberOfRadioButtons=3, sl=1)
        self.MatteBt = mc.button(l = 'Update', c = lambda *args:self.setMatteAttr())
        mc.showWindow(win)

    def setMatteAttr(self):
        self.allArnoldStandIn = []
        sel = mc.radioButtonGrp(self.select, q = True, sl = True)
        if sel == 1:
            self.allArnoldStandIn = mc.ls(type = 'aiStandIn')
        else:
            selectObj = mc.ls(sl = True, dag = True,ni = True, shapes = True)
            for obj in selectObj:
                if mc.objectType(obj) == 'aiStandIn':
                    self.allArnoldStandIn.append(obj)

        matte = mc.radioButtonGrp(self.Matte, q = True, sl = True)
        for arnStand in self.allArnoldStandIn:
            if matte == 1:
                mc.setAttr("%s.overrideMatte"%arnStand, 0)
                mc.setAttr("%s.aiMatte"%arnStand, 0)
            elif matte == 2:
                mc.setAttr("%s.overrideMatte"%arnStand, 1)
                mc.setAttr("%s.aiMatte"%arnStand, 1)
            else:
                mc.setAttr("%s.overrideMatte"%arnStand, 1)
                mc.setAttr("%s.aiMatte"%arnStand, 0)


# ArnoldStandInMast().show()

