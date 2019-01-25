#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm
import shutil,os,re

OCT_PROXYPATH=u'\\\\octvision.com\\cg\\Resource\\Material_Library\\Proxy\\ProxySeed'
OCT_DRIVE = r'\\octvision.com\CG'
class OCT_SameNameProxyChange(object):
	
	def __init__(self):
		pass
		
	def OCT_UploadingProxyUI(self):
		if mc.window("OCT_ChangeProxy",q=True,ex=True):
			mc.deleteUI("OCT_ChangeProxy")
		mc.window("OCT_ChangeProxy",title=u"同一代理名的互换",s=0,w=300,h=200,resizeToFitChildren=1,sizeable=False)
		mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center')
		mc.textFieldGrp('ProxyName',label=u'输入代理文件名:',text='',h=30,editable=True,ct2=('left','left'),cw2=(80,100))
		
		mc.setParent("..")
		mc.rowLayout(numberOfColumns=2,columnWidth2=(100,210),columnAlign2=('left','left'))
		mc.text("newPath",label=u"输入新代理路劲:",h=25)
		mc.text("path",label="",h=25)
		mc.setParent("..")
		mc.rowLayout(numberOfColumns=5,columnWidth5=(25,120,120,10,10),columnAlign5=('center','center','center','center','center'))
		mc.text(l='',vis=0,h=50)
		mc.button(l=u'代理路劲:',w=70,h=25,align='center',c=lambda*args: self.OCT_NewPath())
		mc.button(l=u'OK',w=80,h=25,align='center',c=lambda*args: self.OCT_changeProxyTool())
		mc.button(l=u'Close',width=80,h=25,c=('mc.deleteUI("OCT_ChangeProxy",window=True)'))
		mc.text(l='',vis=0)
		mc.showWindow("OCT_ChangeProxy")
		mc.window('OCT_ChangeProxy', e=True,  wh=[380,120])

	def OCT_NewPath(self):
		getfiles=mc.fileDialog2(fileMode=1,fileFilter="Maya Files (*.ma *.ass)",dialogStyle=2)
		if getfiles:
			mc.text('path',e=True,label=getfiles[0])

	def OCT_changeProxyTool(self):
		#场景中代理名要转换的代理名
		proxyNames=mc.textFieldGrp('ProxyName',q=True,text=True)
		#新替换的代理
		proxyName=proxyNames.split(".")
		#工程目录
		projPath=mc.workspace(fn=True)+"/"
		newPath=mc.text('path',q=True,label=True)
		if newPath.find('z:')>=0:
			newPath=newPath.replace('z:',OCT_DRIVE)

		if newPath.find('Z:')>=0:
			newPath=newPath.replace('Z:',OCT_DRIVE)

		newPath=newPath.replace("/","\\")
		name=newPath.split(".")
		#转换为Vray代理
		if proxyName[1]=="ass" and name[-1]=='ma':
			allArnolds=mc.ls(type="aiStandIn")
			Vrayfirst=""
			for arnolds in allArnolds:
				getArnoldPath=mc.getAttr("%s.dso"%arnolds)
				getArnoldName=os.path.basename(getArnoldPath)

				mc.file(newPath,i=True,type='mayaAscii',ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",pr=True,loadReferenceDepth="all")
				timeTo=mc.listConnections('time1')[-1]
				VrayMeshs=mc.listConnections(timeTo,s=False,d=True)[0]
				if mc.objectType(VrayMeshs)=="VRayMesh":
					fileVrayMeshs=mc.getAttr("%s.fileName"%VrayMeshs)
					fileVrayMesh=fileVrayMeshs.replace("\\","/")
					PathType=projPath+"sourceimages/Vray_DL/"+os.path.basename(fileVrayMeshs)
					if not os.path.isdir(projPath+"sourceimages/Vray_DL"):
						os.makedirs(projPath+"sourceimages/Vray_DL")
					if not os.path.isfile(PathType):
						try:
							shutil.copy2(fileVrayMeshs,projPath+"sourceimages/Vray_DL")
						except:
							print "拷贝贴图出错"
						mc.setAttr("%s.fileName"%VrayMeshs,PathType,type="string")
					else:
						mc.setAttr("%s.fileName"%VrayMeshs,PathType,type="string")

				allFiles=mc.ls(type="file")
				newTexturePath=projPath+"/sourceimages/"+os.path.basename(fileVrayMeshs).split(".")[0]+"_txt"
				
				if not os.path.isdir(newTexturePath):
					os.makedirs(newTexturePath)

				for files in allFiles:
					fileTexPath=mc.getAttr("%s.fileTextureName"%files)
					if os.path.isfile(fileTexPath):
						if projPath not in fileTexPath:
							try:
								shutil.copy2(fileTexPath,newTexturePath)
							except:
								print "拷贝贴图出错"
							newTexPath=newTexturePath+"/"+os.path.basename(fileTexPath)
							mc.setAttr("%s.fileTextureName"%files,newTexPath,type='string')

				arnoldTranNames=mc.listRelatives(arnolds,p=True)[0]
				
				if mc.objectType(arnoldTranNames)=="transform":
					getTranslateArnold=mc.getAttr(arnoldTranNames+".translate")[0]
					getRotateArnold=mc.getAttr(arnoldTranNames+".rotate")[0]
					getScaleArnold=mc.getAttr(arnoldTranNames+".scale")[0]
					timeTo=mc.listConnections('time1')
					
					VrayMeshs=mc.listConnections(timeTo[-1],s=False,d=True)[0]
					if Vrayfirst and Vrayfirst==VrayMeshs:
						VrayMeshs=mc.listConnections(timeTo[-2],s=False,d=True)[0]
					
					allMeshNames=mc.listConnections(VrayMeshs,s=False,d=True)
					for meshs in allMeshNames:
						if mc.objectType(meshs)=="transform":
							Vrayfirst=VrayMeshs
							mc.setAttr('%s.translate'%meshs,getTranslateArnold[0],getTranslateArnold[1],getTranslateArnold[2])
							mc.setAttr('%s.rotate'%meshs,getRotateArnold[0],getRotateArnold[1],getRotateArnold[2])
							mc.setAttr('%s.scale'%meshs,getScaleArnold[0],getScaleArnold[1],getScaleArnold[2])
							mc.delete(arnoldTranNames)
							break

				


		#转换为arnold代理
		elif proxyName[1]=="vrmesh" and name[-1]=='ass':
			allVRayMeshs=mc.ls(type='VRayMesh')
			for vrayMesh in allVRayMeshs:
				getVRayMeshPath=mc.getAttr("%s.fileName"%vrayMesh)
				getVRayMeshName=os.path.basename(getVRayMeshPath)
				imageDir=newPath.split("_AR")[0]
				
				if not os.path.isdir(imageDir):
					imageDir=newPath.split(".")[0]
				if not os.path.isdir(imageDir):
					imageDir=""

				if imageDir:
					if not os.path.isdir(projPath+"/sourceimages/arnoldtex"):
						os.makedirs(projPath+"/sourceimages/arnoldtex")
					try:
						shutil.copy2(newPath,projPath+"/sourceimages/arnoldtex")
					except:
						print "拷贝.vrmesh文件出错"

					fileArnoldPrxy=projPath+"/sourceimages/arnoldtex/"+os.path.basename(newPath)

					mc.file(fileArnoldPrxy,i=True,type="ASS",ra=True,mergeNamespacesOnClash=False,pr=True,loadReferenceDepth="all")
					fileTexturePath=projPath+"/sourceimages/arnoldtex/"+os.path.basename(imageDir)

					myAllMaps=mc.getFileList(filespec=(imageDir+"/*"))

					#拷贝贴图
					if not os.path.isdir(fileTexturePath):
						os.makedirs(fileTexturePath)
					if myAllMaps:
						for maps in myAllMaps:
							try:
								shutil.copy2((imageDir+"/"+maps),fileTexturePath)
							except:
								print(u'拷贝代理文件出错！\n')

					allMeshNames=mc.listConnections(vrayMesh,s=False,d=True)
					for Meshs in allMeshNames:
						if mc.objectType(Meshs)=="transform":
							getTranslateVray=mc.getAttr(Meshs+".translate")[0]
							getRotateVray=mc.getAttr(Meshs+".rotate")[0]
							getScaleVray=mc.getAttr(Meshs+".scale")[0]

							ArnoldTransform=mc.listConnections('ArnoldStandInDefaultLightSet',s=True,d=False)[-1]
							mc.setAttr('%s.translate'%ArnoldTransform,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
							mc.setAttr('%s.rotate'%ArnoldTransform,getRotateVray[0],getRotateVray[1],getRotateVray[2])
							mc.setAttr('%s.scale'%ArnoldTransform,getScaleVray[0],getScaleVray[1],getScaleVray[2])
							mc.delete(Meshs)
							mc.delete(vrayMesh)
							flags=True
						else:
							mc.delete(Meshs)

				else:
					mc.confirmDialog(title=u"提示",message=u"路径下没有相应的贴图文件夹%s"%(os.path.dirname(newPath)))
		


#OCT_SameNameProxyChange().OCT_UploadingProxyUI()
