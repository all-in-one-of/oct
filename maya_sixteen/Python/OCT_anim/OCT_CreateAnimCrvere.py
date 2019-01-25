# -*- coding: utf-8 -*-
import maya.cmds as mc
class createCvere():
    def __init__(self):
        pass
    def createCveres(self):
        AllSelectTran=mc.ls(sl=True)
        if not AllSelectTran:
            mc.confirmDialog(message=u"请选择要创建动画曲线的物体！")
            return
            
        start_frame=mc.textFieldGrp("start",q=True,text=True)
        end_frame=mc.textFieldGrp("end",q=True,text=True)
        missFrame=mc.textFieldGrp("missFrame",q=True,text=True)
        missFrames=""
        if missFrame:
            missFrames=int(missFrame)
        
        if start_frame=="" or end_frame=="":
            mc.confirmDialog(message=u"请输入开始帧和结束帧！")
            return 
        for selectTran in AllSelectTran:
            flag=""
            xforms=""
            i=int(start_frame)
            while True:
                if i>=int(end_frame):
                    mc.currentTime(int(end_frame))
                    break
                mc.currentTime(i)
                tranforn=mc.xform(selectTran,q=True,ws=True,sp=True)
                # if tranforn==xforms:
                #     continue
                # xforms=tranforn
                if flag:
                    mc.curve(flag,a=True,p=(tranforn[0],tranforn[1],tranforn[2]))
                else:
                    flag=mc.curve(p=(tranforn[0],tranforn[1],tranforn[2]))
                if missFrames:
                    i=i+missFrames
                else:
                    i=i+1


    def createCvereUI(self):
        if mc.window("createCvereUI",exists=True):
            mc.deleteUI("createCvereUI")
        win=mc.window("createCvereUI",t=u"根据动画路径创建曲线",w=100,h=200,resizeToFitChildren=1,sizeable=False)
        mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center')
        mc.textFieldGrp("start",label=u"开始帧",editable=True,ct2=('left','left'),cw2=(40,100))
        mc.textFieldGrp("end",label=u"结束帧",editable=True,ct2=('left','left'),cw2=(40,100))
        mc.textFieldGrp("missFrame",label=u"隔  帧",editable=True,ct2=('left','left'),cw2=(40,100))
        mc.setParent("..")
        mc.rowLayout(numberOfColumns=4,columnWidth4=(25,60,60,10),columnAlign4=('center','center','center','center')) 
        mc.text(l='',vis=0)
        mc.button(l='OK',w=40,h=25,backgroundColor = (0.0,0.7,0),align='center',c=lambda*args:self.createCveres())
        mc.button(l='Close',width=40,h=25,backgroundColor = (0.7,0.0,0),c=('mc.deleteUI("createCveres",window=True)'))
        mc.text(l='',vis=0)
        mc.showWindow("createCvereUI") 