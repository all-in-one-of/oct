# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mm

def update_Shaver_Attr_UI():
	if mc.window("update_Shaver_Attr_UI",ex=True):
		mc.deleteUI("update_Shaver_Attr_UI")
	mc.window("update_Shaver_Attr_UI",title=u"更新shaveHair的属性",tlc=[180,200],wh=[460,350])
	mc.scrollLayout("A",hst=0,vst=8)
	mc.rowLayout("defaultRowLayout",numberOfColumns=1,adjustableColumn=1,columnAttach=([1,"both",0],[2,"both",0]),columnWidth2=[400,300])
	mc.frameLayout(borderStyle="etchedIn",label="Shader Multi Editor")
	mc.columnLayout(adjustableColumn=True,rs=5,cal="left")
	mc.separator()
	mc.radioButtonGrp("selectOrAll",nrb=2,l="Target",labelArray2=['selected','All in Scene'],select=1,cw=([1,60],[2,70]))
	mc.separator()
	mc.floatSliderButtonGrp("rootThickness",pre=3,label=u"毛发根部大小(Root Thckness)",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=([1,160],[2,60],[3,145]),image="navButtonUnconnected.xpm",bc=lambda*args:updateShaverAttr(1,"rootThickness"))
	mc.floatSliderButtonGrp("tipThickness",pre=3,label=u"毛发尖端大小(Tip Thckness)",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=([1,160],[2,60],[3,145]),image="navButtonUnconnected.xpm",bc=lambda*args:updateShaverAttr(1,"tipThickness"))
	mc.floatSliderButtonGrp("specular",pre=3,label=u"高光(Specular)",field=True,buttonLabel="UPDATE",symbolButtonDisplay=False,cw=([1,160],[2,60],[3,145]),image="navButtonUnconnected.xpm",bc=lambda*args:updateShaverAttr(1,"specular"))
	mc.colorSliderButtonGrp('specularTint2',label=u"二次高光(Secondary Specular)",buttonLabel="UPDATE",symbolButtonDisplay=False,cw=([1,160],[2,60],[3,145]),image="navButtonUnconnected.xpm",bc=lambda*args:updateShaverAttr(2,"specularTint2"))
	mc.colorSliderButtonGrp('hairColor',label=u"尖端颜色(Tip Color)",buttonLabel="UPDATE",symbolButtonDisplay=False,cw=([1,160],[2,60],[3,145]),image="navButtonUnconnected.xpm",bc=lambda*args:updateShaverAttr(2,"hairColor"))
	mc.colorSliderButtonGrp('rootColor',label=u"根部颜色（RootColor）",buttonLabel="UPDATE",symbolButtonDisplay=False,cw=([1,160],[2,60],[3,145]),image="navButtonUnconnected.xpm",bc=lambda*args:updateShaverAttr(2,"rootColor"))
	mc.showWindow('update_Shaver_Attr_UI')

def updateShaverAttr(isShave,attr):
	targetShave=""
	selectedOrAll=mc.radioButtonGrp("selectOrAll",q=True,sl=True)
	if selectedOrAll==1:
		targetShave=mc.ls(sl=True)
	else:
		targetShave=mc.ls(type="shaveHair")

	if isShave==1:
		updateAttrValue=mc.floatSliderButtonGrp(attr,q=True,v=True,pre=3)
		for Shave in targetShave:
			mc.setAttr("%s.%s"%(Shave,attr),updateAttrValue)
	elif isShave==2:
		updateAttrColor=mc.colorSliderButtonGrp(attr,q=True,rgb=True)
		for Shave in targetShave:
			mc.setAttr("%s.%s"%(Shave,attr),updateAttrColor[0],updateAttrColor[1],updateAttrColor[2])

#update_Shaver_Attr_UI()