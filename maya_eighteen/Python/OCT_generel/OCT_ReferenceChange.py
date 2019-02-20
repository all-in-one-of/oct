#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm
import os

OCT_DRIVE = r'\\octvision.com\CG'

class ReferenceFileChange():
	def __init__(self):
		pass
	def ReferenceFile(self):
		if mc.window("ReferenceFileUI",q=True,ex=True):
			mc.deleteUI("ReferenceFileUI")
		mc.window("ReferenceFileUI",title=u"转换参考文件",w=500,h=200,sizeable=False)
		mc.columnLayout()
		mc.text("")
		mc.setParent('..')
		mc.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 90), (2, 500)])
		mc.button('old',label=u'原参考文件路径:',w=80,h=30,c=lambda*args: self.oldReferencePath(1))
		mc.text("oldPath",align='left',label="",w=400)
		mc.button('new',label=u'新参考文件路径:',w=80,h=30,c=lambda*args: self.oldReferencePath(2))
		mc.text("newPath",align='left',label="",w=400)
		mc.setParent("..")
		
		#mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center')
		#mc.textFieldGrp('newPath',label=u'新参考文件路径:',text='',h=25,editable=True,ct2=('left','left'),cw2=(90,400))
		#mc.setParent("..")
		mc.rowLayout(numberOfColumns=4,columnWidth4=(120,120,220,200),columnAlign4=('center','center','center','center'))
		mc.text(l='',vis=0)
		mc.button(l=u'OK',w=80,h=30,align='center',c=lambda*args: self.ReferenceFiles())
		mc.button(l=u'Close',width=80,h=30,c=('mc.deleteUI("ReferenceFileUI",window=True)'))
		mc.text(l='',vis=0)
		mc.showWindow("ReferenceFileUI")

	def oldReferencePath(self,j):
		path=mc.fileDialog2(fileMode=1,fileFilter="Maya Files (*.mb)",dialogStyle=2)
		if path:
			if j==1:
				mc.text('oldPath',e=True,label=path[0])
			elif j==2:
				mc.text('newPath',e=True,label=path[0])



	def ReferenceFiles(self):
		oldPath=mc.text('oldPath',q=True,label=True)
		newPath=mc.text('newPath',q=True,label=True)
		if not oldPath or not newPath:
			mc.confirmDialog(title=u"提示",message=u'请输入路径例如:Z:\Themes\FKBS\Project\scenes\characters\ch001001Allosaurus\master\FKBS_ch001001Allosaurus_h_msAnim.mb')
			return
		if oldPath.find('z:')>=0:
			oldPath=oldPath.replace('z:',OCT_DRIVE)

		if oldPath.find('Z:')>=0:
			oldPath=oldPath.replace('Z:',OCT_DRIVE)

		if newPath.find('z:')>=0:
			newPath=newPath.replace('z:',OCT_DRIVE)

		if newPath.find('Z:')>=0:
			newPath=newPath.replace('Z:',OCT_DRIVE)

		#if not os.path.isfile(oldPath):
			#mc.confirmDialog(title=u"提示",message=u'请输入正确文件路径例如:Z:\Themes\FKBS\Project\scenes\characters\ch001001Allosaurus\master\FKBS_ch001001Allosaurus_h_msAnim.mb')
			#return

		if not os.path.isfile(newPath):
			mc.confirmDialog(title=u"提示",message=u'请输入正确文件路径例如:Z:\Themes\FKBS\Project\scenes\characters\ch001001Allosaurus\master\FKBS_ch001001Allosaurus_h_msAnim.mb')
			return

		oldPath=oldPath.replace('\\','/')
		newPath=newPath.replace('\\','/')
		#print oldPath
		#print newPath
		allReferenceFiles=mc.file(q=True,reference=True)
		for refer in allReferenceFiles:
			refer=refer.split('{')[0]
			if oldPath==refer:
				referenceNode=mc.file(refer,q=True,referenceNode=True)
				mc.file(newPath,loadReference=referenceNode)

#ReferenceFileChange().ReferenceFile()
