# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import random
class setUV(object):
    def __init__(self):
        pass
    def setUVUI(self):
        Locator_nodes=mc.ls(sl=True,fl=True)
        if Locator_nodes:
            #选择物体
            mc.select(Locator_nodes[0],r=True)
            #查询所有的点
            totalf=mc.polyEvaluate(v=True)
            #查询有多少个UV（多少片叶子）
            num=mc.polyEvaluate(shell=True)
            
            toUV=mc.polyEditUV("%s.map[%d]"%(Locator_nodes[0],totalf),q=True)
            setScaleU=0.33/toUV[0]
            setScaleV=0.33/toUV[1]
            mm.eval('doMenuComponentSelection("%s", "puv");'%Locator_nodes[0])
           
            for i in range(totalf):
                pointUV=mc.polyEditUV("%s.map[%d]"%(Locator_nodes[0],(i+1)),q=True)
                if pointUV[0]==toUV[0] and pointUV[1]==toUV[1]:
                    print pointUV
                    mc.select(d=False)
                    mc.select("%s.map[%d]"%(Locator_nodes[0],i+1),r=True)
                    #选择每片叶子的所有点
                    mc.polySelectConstraint(sh=True,bo=False,m=2)
                    ranInt=random.randint(1,9)
                    if ranInt==1:
                        mc.polyEditUV(u=0, v=0, scaleU=setScaleU, scaleV=setScaleV)
                    elif ranInt==2:
                        mc.polyEditUV(u=0, v=0.33, scaleU=setScaleU, scaleV=setScaleV)
                    elif ranInt==3:
                        mc.polyEditUV(u=0, v=0.66, scaleU=setScaleU, scaleV=setScaleV) 
                    elif ranInt==4:
                        mc.polyEditUV(u=0.33, v=0, scaleU=setScaleU, scaleV=setScaleV)
                    elif ranInt==5:
                        mc.polyEditUV(u=0.33, v=0.33, scaleU=setScaleU, scaleV=setScaleV)
                    elif ranInt==6:
                        mc.polyEditUV(u=0.33, v=0.66, scaleU=setScaleU, scaleV=setScaleV) 
                    elif ranInt==7:
                        mc.polyEditUV(u=0.66, v=0, scaleU=setScaleU, scaleV=setScaleV) 
                    elif ranInt==8:
                        mc.polyEditUV(u=0.66, v=0.33, scaleU=setScaleU, scaleV=setScaleV)  
                    elif ranInt==9:
                        mc.polyEditUV(u=0.66, v=0.66, scaleU=setScaleU, scaleV=setScaleV)  
                else:
                    continue
            mm.eval('maintainActiveChangeSelectMode %s;'%Locator_nodes[0])

            
