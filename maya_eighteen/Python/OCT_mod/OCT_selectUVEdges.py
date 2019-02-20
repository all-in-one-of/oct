# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import random
class selectUVEdges(object):
    def __init__(self):
        self.finalBorder=[]
        
    def LsUVMap(self):
        Locator_nodes=mc.ls(sl=True,o=True)
        if len(Locator_nodes)!=1:
            mc.confirmDialog(m=u"请选择一个物体！")
            return
        mc.select(Locator_nodes[0],r=True)
        #当前值没有冻结的冻结
        mc.polyNormalPerVertex(ufn=True)
        #选择所有的UV点
        mc.select((Locator_nodes[0]+'.map[*]'),r=True)
        #显示所有修改的部件转变成线
        uvBorder=mc.polyListComponentConversion(te=True,internal=True)
        #查找uvBorder中的线
        uvBorder=mc.ls(uvBorder,fl=True)
        for curEdge in uvBorder:
            edgeUVs=mc.polyListComponentConversion(curEdge,tuv=True)
            edgeUVs=mc.ls(edgeUVs,fl=True)
            if len(edgeUVs)>2:
                self.finalBorder.append(curEdge)
        mc.select(self.finalBorder,r=True)

#selectUVEdges().LsUVMap()