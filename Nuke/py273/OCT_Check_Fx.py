# *-* coding: utf-8 *-*
import nuke, re, os, nukescripts.utils

#特效生成节点

class OCT_Check_fx(object):
    def __init__(self):
        self.allSelectNode = ""

    #去掉所有所选择的点
    def setSelecteNone(self):
        allmySelectedNodes = nuke.selectedNodes()
        if allmySelectedNodes:
            for mySelectedNode in allmySelectedNodes:
                mySelectedNode.setSelected(False)

    def check_Fx(self):
        #查找所有的节点
        self.allSelectNode = nuke.selectedNodes()
        for slNode in self.allSelectNode:
            _bbox = [slNode.screenWidth(), slNode.screenHeight()]

            myDot = nuke.nodes.Dot()
            myDot.setInput(0, slNode)

            myDot.setXYpos(slNode.xpos() + _bbox[1]/2, slNode.ypos()+ _bbox[1]/2*3)

            myShuffle = nuke.nodes.Shuffle()
            myShuffle.setInput(0, myDot)
            myShuffle['red'].setValue(6)
            myShuffle['green'].setValue(6)
            myShuffle['blue'].setValue(6)
            myShuffle['alpha'].setValue(6)

            myShuffle.setXYpos(slNode.xpos() + _bbox[1]/2*3, slNode.ypos()+ _bbox[1]/2*3)

            myGrade = nuke.nodes.Grade()
            myGrade['white'].setValue(0.3)
            myGrade.setInput(0, myShuffle)

            myGrade.setXYpos(slNode.xpos(), slNode.ypos()+ _bbox[1]*2)

            myMerge = nuke.nodes.Merge()
            myMerge.setInput(1, myDot)
            myMerge.setInput(0, myGrade)

            myMerge.setXYpos(slNode.xpos() - _bbox[1]/2*3, slNode.ypos()+ _bbox[1]/2*3)

            self.setSelecteNone()

            myDot.setSelected(True)
            myShuffle.setSelected(True)
            myGrade.setSelected(True)
            myMerge.setSelected(True)

            nuke.collapseToGroup()

#OCT_Check_fx().check_Fx()