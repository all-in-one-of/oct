#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import maya.mel as mm
import shutil,os,re

OCT_PROXYPATH=u'\\\\octvision.com\\cg\\Resource\\Material_Library\\Proxy\\ProxySeed'

class OCT_ProxyChange_YH():
	def __init__(self):
		pass

	def OCT_ProxyChangeUI(self):
		if mc.window("OCT_ProxyChangeUI",q=True,exists=True):
			mc.deleteUI("OCT_ProxyChangeUI")
		mc.window("OCT_ProxyChangeUI",title=u"转换代理",widthHeight=(490,730),sizeable=False)
		mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center') 
		mc.radioButtonGrp('Options',columnAlign3=('left','left','left'),columnWidth3=(90,80,80),numberOfRadioButtons=2,label=u'选择:',labelArray2=('All','Select'),sl=1,enable=True,h=35)
		mc.setParent('..')
		mc.columnLayout()
		mc.text(label="")
		mc.button('delVray',label=u'清除多余的VrayMesh',w=120,h=30,c=lambda*args: self.deleteVrayMesh())
		mc.text(label="")
		mc.setParent('..')
		mc.rowLayout(numberOfColumns=4,columnWidth4=(90,100,100,100))
		mc.button('vray',label='VRayMesh',w=70,h=30,c=lambda*args: self.ChangeVray())
		mc.button('arnold',label='Arnold',w=70,h=30,c=lambda*args: self.ChangeArnold())
		mc.button('model',label='Model',w=70,h=30,c=lambda*args: self.changeModel())
		mc.showWindow('OCT_ProxyChangeUI')
		mc.window("OCT_ProxyChangeUI",e=True,widthHeight=(270,130))

	def deleteVrayMesh(self):
		allVRayMeshs=mc.ls(type="VRayMesh")
		allNoMeshVray=[]
		for vrayMeshs in allVRayMeshs:
		    allMeshs=mc.listConnections("%s.output"%vrayMeshs,s=False,d=True)
		    if not allMeshs:
		        allNoMeshVray.append(vrayMeshs)
		 
		for NoMeshVaray in allNoMeshVray:
		    allConnectVrayMesh=mc.listConnections(NoMeshVaray)
		    if allConnectVrayMesh:
		        for meshs in allConnectVrayMesh:
		           timeMesh=mc.listConnections(meshs)[0]
		           if timeMesh and mc.objectType(timeMesh)!="time":
		               mc.delete(timeMesh) 
		        if NoMeshVaray:
		            mc.delete(meshs)  

	#转成模型的
	def changeModel(self):
		Option=mc.radioButtonGrp('Options',q=True,sl=True)
		if Option==1:
			#Vray
			#获取所有的VRayMesh节点
			allVrayMesh=mc.ls(type='VRayMesh')
			proxyType=os.listdir(OCT_PROXYPATH)
			#贴图路径
			sourceTex=""
			#获取文件的工作空间
			projPath=mc.workspace(fn=True)+"/"
			#网路路径上不存在对应代理节点
			infoVray=""
			infoArnold=""
			infoModel=""
			for vrayMesh in allVrayMesh:
				getVRayMeshPath=mc.getAttr('%s.fileName'%vrayMesh)
				getVRayMeshName=os.path.basename(getVRayMeshPath)
				VrayDirName=getVRayMeshName.split("_")[0]
				print "文件夹："
				print VrayDirName
				#原模型文件的文件夹
				ModelDir=""
				myVRayMeshName=""
				#获场景中存在的代理在网络那个路径上面
				for types in proxyType:
					myVRayMeshName=OCT_PROXYPATH+"\\"+types+"\\"+VrayDirName+"\\sourceimages\\Vray_DL\\"+getVRayMeshName
					if os.path.isfile(myVRayMeshName):
						ModelDir=OCT_PROXYPATH+"\\"+types+"\\"+VrayDirName+"\\scenes\\"
						break
					else:
						continue

				#网路路径存在vrayMesh节点
				if ModelDir:
					ModelName=ModelDir+VrayDirName+".mb"
					if os.path.isfile(ModelName):
						#导入模型的节点名
						modesName=""
						name=VrayDirName+"_"+VrayDirName
						allTrans=mc.ls(type="transform")
						if name in allTrans:
							modesName=name

						mc.file(ModelName,i=True,type="mayaBinary",ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",loadReferenceDepth="all")
						num=0
						nums=0
						if not modesName:
							for trans in allTrans:
								if "|" not in trans and modesName in trans:
									try:
										tranName=trans.replace(name,"")
										nums=int(tranName) 
									except:
										pass
								if num<=nums:
									modesName=trans
									num=nums

						allMeshNames=mc.listConnections(vrayMesh,s=False,d=True)
						for Meshs in allMeshNames:
							if mc.objectType(Meshs)=="transform":
								getTranslateVray=mc.getAttr(Meshs+".translate")[0]
								getRotateVray=mc.getAttr(Meshs+".rotate")[0]
								getScaleVray=mc.getAttr(Meshs+".scale")[0]

								mc.setAttr('%s.translate'%modesName,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
								mc.setAttr('%s.rotate'%modesName,getRotateVray[0],getRotateVray[1],getRotateVray[2])
								mc.setAttr('%s.scale'%modesName,getScaleVray[0],getScaleVray[1],getScaleVray[2])
								mc.delete(Meshs)
								mc.delete(vrayMesh)
							else:
								mc.delete(Meshs)

					else:
						infoModel=vrayMesh+","+ModelName+"\n"
				else:
					infoVray=vrayMesh+","+myVRayMeshName+"\n"

			#arnold
			allArnoldProxys=mc.ls(type="aiStandIn")
			for arnoldProxys in allArnoldProxys:
				getArnoldPath=mc.getAttr("%s.dso"%arnoldProxys)
				getArnoldName=os.path.basename(getArnoldPath)
				ArnoldDirName=getArnoldName.split("_")[0]
				print "文件夹："
				print getArnoldName
				#原模型文件的文件夹
				ModelDir=""
				myArnoldName=""
				for types in proxyType:
					ModelDir
					#查找anrold代理是否存在
					myArnoldName=OCT_PROXYPATH+"\\"+types+"\\"+ArnoldDirName+"\\sourceimages\\arnoldtex\\"+getArnoldName
					if os.path.isfile(myArnoldName):
						ModelDir=OCT_PROXYPATH+"\\"+types+"\\"+ArnoldDirName+"\\scenes\\"
						break
					else:
						continue

				if ModelDir:
					ModelName=ModelDir+ArnoldDirName+".mb"
					if os.path.isfile(ModelName):
						#导入模型的节点名
						modesName=""
						name=ArnoldDirName+"_"+ArnoldDirName
						allTrans=mc.ls(type="transform")
						if name in allTrans:
							modesName=name

						mc.file(ModelName,i=True,type="mayaBinary",ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",loadReferenceDepth="all")
						num=0
						nums=0
						if not modesName:
							for trans in allTrans:
								if "|" not in trans and modesName in trans:
									try:
										tranName=trans.replace(name,"")
										nums=int(tranName) 
									except:
										pass
								if num<=nums:
									modesName=trans
									num=nums
						if modesName:
							arnoldTranNames=mc.listRelatives(arnoldProxys,p=True)[0]
							if mc.objectType(arnoldTranNames)=="transform":
								getTranslateArnold=mc.getAttr(arnoldTranNames+".translate")[0]
								getRotateArnold=mc.getAttr(arnoldTranNames+".rotate")[0]
								getScaleArnold=mc.getAttr(arnoldTranNames+".scale")[0]

								mc.setAttr('%s.translate'%modesName,getTranslateArnold[0],getTranslateArnold[1],getTranslateArnold[2])
								mc.setAttr('%s.rotate'%modesName,getRotateArnold[0],getRotateArnold[1],getRotateArnold[2])
								mc.setAttr('%s.scale'%modesName,getScaleArnold[0],getScaleArnold[1],getScaleArnold[2])
								mc.delete(arnoldTranNames)
					else:
						infoModel=arnoldProxys+","+ModelName+"\n"
				else:
					infoArnold=arnoldProxys+","+myArnoldName+"\n"
			if infoModel:
				mc.confirmDialog(title=u"提示",message=u"场景中存在的代理网路路劲没有对应的原模型文件,查看编辑窗口。")
				print "下列是场景中存在的代理网路路劲没有对应的原模型文件:"
				print infoModel
				return
			if infoArnold:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Arnold代理网路路劲没有对应的Arnold代理,查看编辑窗口")
				print "下列是场场景中存在Arnold代理网路路劲没有对应的Arnold代理:"
				print infoArnold
				return

			if infoVray:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Vray代理网路路劲没有对应的Vray代理,查看编辑窗口")
				print "下列是场场景中存在Vray代理网路路劲没有对应的Vray代理:"
				print infoVray
				return

		elif Option==2:
			allSelect=mc.ls(sl=True)
			allArnold={}
			allVrayMesh={}
			for sel in allSelect:
				Meshs=mc.listRelatives(sel,c=True)[0]
				if mc.objectType(Meshs)=='aiStandIn':
					allArnold.update({sel:Meshs})
				else:
					VraMeshs=mc.listConnections(Meshs,s=True,d=False)[0]
					if mc.objectType(VraMeshs)=='VRayMesh':
						allVrayMesh.update({sel:VraMeshs})

		
			proxyType=os.listdir(OCT_PROXYPATH)
			#贴图路径
			sourceTex=""
			#获取文件的工作空间
			projPath=mc.workspace(fn=True)+"/"
			#网路路径上不存在对应代理节点
			infoVray=""
			infoArnold=""
			infoModel=""

			for mesh in allVrayMesh.keys():
				getVRayMeshPath=mc.getAttr('%s.fileName'%allVrayMesh[mesh])
				getVRayMeshName=os.path.basename(getVRayMeshPath)
				VrayDirName=getVRayMeshName.split("_")[0]
				print "文件夹："
				print VrayDirName
				#原模型文件的文件夹
				ModelDir=""
				myVRayMeshName=""
				#获场景中存在的代理在网络那个路径上面
				for types in proxyType:
					myVRayMeshName=OCT_PROXYPATH+"\\"+types+"\\"+VrayDirName+"\\sourceimages\\Vray_DL\\"+getVRayMeshName
					if os.path.isfile(myVRayMeshName):
						ModelDir=OCT_PROXYPATH+"\\"+types+"\\"+VrayDirName+"\\scenes\\"
						break
					else:
						continue

				#网路路径存在vrayMesh节点
				if ModelDir:
					ModelName=ModelDir+VrayDirName+".mb"
					if os.path.isfile(ModelName):
						#导入模型的节点名
						modesName=""
						name=VrayDirName+"_"+VrayDirName
						allTrans=mc.ls(type="transform")
						if name in allTrans:
							modesName=name

						mc.file(ModelName,i=True,type="mayaBinary",ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",loadReferenceDepth="all")
						num=0
						nums=0
						if not modesName:
							for trans in allTrans:
								if "|" not in trans and modesName in trans:
									try:
										tranName=trans.replace(name,"")
										nums=int(tranName) 
									except:
										pass
								if num<=nums:
									modesName=trans
									num=nums

						
						getTranslateVray=mc.getAttr(mesh+".translate")[0]
						getRotateVray=mc.getAttr(mesh+".rotate")[0]
						getScaleVray=mc.getAttr(mesh+".scale")[0]

						mc.setAttr('%s.translate'%modesName,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
						mc.setAttr('%s.rotate'%modesName,getRotateVray[0],getRotateVray[1],getRotateVray[2])
						mc.setAttr('%s.scale'%modesName,getScaleVray[0],getScaleVray[1],getScaleVray[2])
						mc.delete(mesh)
						mc.delete(allVrayMesh[mesh])
							
					else:
						infoModel=allVrayMesh[mesh]+","+ModelName+"\n"
				else:
					infoVray=allVrayMesh[mesh]+","+myVRayMeshName+"\n"

			#arnold
			for arnolds in allArnold.keys():
				getArnoldPath=mc.getAttr("%s.dso"%allArnold[arnolds])
				getArnoldName=os.path.basename(getArnoldPath)
				ArnoldDirName=getArnoldName.split("_")[0]
				print "文件夹："
				print getArnoldName
				#原模型文件的文件夹
				ModelDir=""
				myArnoldName=""
				for types in proxyType:
					ModelDir
					#查找anrold代理是否存在
					myArnoldName=OCT_PROXYPATH+"\\"+types+"\\"+ArnoldDirName+"\\sourceimages\\arnoldtex\\"+getArnoldName
					if os.path.isfile(myArnoldName):
						ModelDir=OCT_PROXYPATH+"\\"+types+"\\"+ArnoldDirName+"\\scenes\\"
						break
					else:
						continue

				if ModelDir:
					ModelName=ModelDir+ArnoldDirName+".mb"
					if os.path.isfile(ModelName):
						#导入模型的节点名
						modesName=""
						name=ArnoldDirName+"_"+ArnoldDirName
						allTrans=mc.ls(type="transform")
						if name in allTrans:
							modesName=name

						mc.file(ModelName,i=True,type="mayaBinary",ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",loadReferenceDepth="all")
						num=0
						nums=0
						if not modesName:
							for trans in allTrans:
								if "|" not in trans and modesName in trans:
									try:
										tranName=trans.replace(name,"")
										nums=int(tranName) 
									except:
										pass
								if num<=nums:
									modesName=trans
									num=nums
					
						getTranslateArnold=mc.getAttr(arnolds+".translate")[0]
						getRotateArnold=mc.getAttr(arnolds+".rotate")[0]
						getScaleArnold=mc.getAttr(arnolds+".scale")[0]

						mc.setAttr('%s.translate'%modesName,getTranslateArnold[0],getTranslateArnold[1],getTranslateArnold[2])
						mc.setAttr('%s.rotate'%modesName,getRotateArnold[0],getRotateArnold[1],getRotateArnold[2])
						mc.setAttr('%s.scale'%modesName,getScaleArnold[0],getScaleArnold[1],getScaleArnold[2])
						mc.delete(arnolds)
					else:
						infoModel=allArnold[arnolds]+","+ModelName+"\n"
				else:
					infoArnold=allArnold[arnolds]+","+myArnoldName+"\n"
			if infoModel:
				mc.confirmDialog(title=u"提示",message=u"场景中存在的代理网路路劲没有对应的原模型文件,查看编辑窗口。")
				print "下列是场景中存在的代理网路路劲没有对应的原模型文件:"
				print infoModel
				return
			if infoArnold:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Arnold代理网路路劲没有对应的Arnold代理,查看编辑窗口")
				print "下列是场场景中存在Arnold代理网路路劲没有对应的Arnold代理:"
				print infoArnold
				return

			if infoVray:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Vray代理网路路劲没有对应的Vray代理,查看编辑窗口")
				print "下列是场场景中存在Vray代理网路路劲没有对应的Vray代理:"
				print infoVray
				return


	def ChangeArnold(self):
		Option=mc.radioButtonGrp('Options',q=True,sl=True)
		infoVray=""
		infoArnold=""
		infoModel=""

		if Option==1:
			allVrayMesh=mc.ls(type='VRayMesh')
			proxyType=os.listdir(OCT_PROXYPATH)
			#贴图路径
			sourceTex=""
			#项目路径
			projPath=mc.workspace(fn=True)+"/"
			infoVray=""
			infoArnold=""
			for vrayMesh in allVrayMesh:
				getVRayMeshPath=mc.getAttr('%s.fileName'%vrayMesh)
				getVRayMeshName=os.path.basename(getVRayMeshPath)
				dirName=getVRayMeshName.split("_")[0]
				print "文件夹："
				print dirName
				arnoldDir=""
				myVRayMeshName=""
				oldTexPath=""
				for types in proxyType:
					myVRayMeshName=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\Vray_DL\\"+getVRayMeshName
					oldTexPath=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\arnoldtex\\"+dirName
					if os.path.isfile(myVRayMeshName):
						arnoldDir=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\arnoldtex\\"
						break
					else:
						continue

				if arnoldDir:
					myArnoldName=arnoldDir+dirName+"_AR.ass"
					if os.path.isfile(myArnoldName):
						if not os.path.isdir(projPath+"/sourceimages/arnoldtex"):
							os.makedirs(projPath+"/sourceimages/arnoldtex")
						try:
							shutil.copy2(myArnoldName,projPath+"/sourceimages/arnoldtex")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/arnoldtex/"+dirName+"_AR.ass"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(fileArnoldPrxy,i=True,type="ASS",ra=True,mergeNamespacesOnClash=False,pr=True,loadReferenceDepth="all")

						fileTexturePath=projPath+"/sourceimages/arnoldtex/"+dirName

						myAllMaps=mc.getFileList(filespec=(oldTexPath+"/*"))

						#拷贝贴图
						if not os.path.isdir(fileTexturePath):
							os.makedirs(fileTexturePath)
						if myAllMaps:
							for maps in myAllMaps:
								try:
									shutil.copy2((oldTexPath+"/"+maps),fileTexturePath)
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
						infoVray=vrayMesh+","+myArnoldName+"\n"
				else:
					infoArnold=vrayMesh+","+getVRayMeshPath+"\n"

			allTran=mc.ls(type="transform")
			allTrans=[]
			for T in allTran:
				if not mc.listRelatives(T,p=True):
					allTrans.append(T)
			for trans in allTrans:
				arnoldDir=""
				#贴图路径
				oldTexPath=""
				transName=""
				flagss=False
				if "|" not in trans and "_" in trans:
					transName=trans.split("_")
					if transName[0] in transName[1]:
						for types in proxyType:
							myModelName=OCT_PROXYPATH+"\\"+types+"\\"+transName[0]+"\\scenes\\"+transName[0]+".mb"
							oldTexPath=OCT_PROXYPATH+"\\"+types+"\\"+transName[0]+"\\sourceimages\\arnoldtex\\"+transName[0]
							if os.path.isfile(myModelName):
								arnoldDir=OCT_PROXYPATH+"\\"+types+"\\"+transName[0]+"\\sourceimages\\arnoldtex\\"
								break
							else:
								continue
				if arnoldDir:
					myArnoldName=arnoldDir+transName[0]+"_AR.ass"
					if os.path.isfile(myArnoldName):
						if not os.path.isdir(projPath+"/sourceimages/arnoldtex"):
							os.makedirs(projPath+"/sourceimages/arnoldtex")
						try:
							shutil.copy2(myArnoldName,projPath+"/sourceimages/arnoldtex")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/arnoldtex/"+transName[0]+"_AR.ass"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(fileArnoldPrxy,i=True,type="ASS",ra=True,mergeNamespacesOnClash=False,pr=True,loadReferenceDepth="all")

						fileTexturePath=projPath+"/sourceimages/arnoldtex/"+transName[0]

						myAllMaps=mc.getFileList(filespec=(oldTexPath+"/*"))

						#拷贝贴图
						if not os.path.isdir(fileTexturePath):
							os.makedirs(fileTexturePath)
						if myAllMaps:
							for maps in myAllMaps:
								try:
									shutil.copy2((oldTexPath+"/"+maps),fileTexturePath)
								except:
									print(u'拷贝代理文件出错！\n')

						
						getTranslateVray=mc.getAttr(trans+".translate")[0]
						getRotateVray=mc.getAttr(trans+".rotate")[0]
						getScaleVray=mc.getAttr(trans+".scale")[0]

						ArnoldTransform=mc.listConnections('ArnoldStandInDefaultLightSet',s=True,d=False)[-1]
						mc.setAttr('%s.translate'%ArnoldTransform,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
						mc.setAttr('%s.rotate'%ArnoldTransform,getRotateVray[0],getRotateVray[1],getRotateVray[2])
						mc.setAttr('%s.scale'%ArnoldTransform,getScaleVray[0],getScaleVray[1],getScaleVray[2])
						mc.delete(trans)
						
					else:
						infoVray=trans+","+myArnoldName+"\n"

			if infoArnold:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Vray代理或模型网路路劲没有对应的arnold代理文件,查看编辑窗口。")
				print "下列是场景中存在Vray代理或模型网路路劲没有对应的arnold代理文件:"
				print infoArnold
				return
			if infoVray:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Vray代理网路路劲没有对应的Vray代理文件,查看编辑窗口。")
				print "下列是场景中存在Vray代理网路路劲没有对应的Vary代理文件:"
				print infoVray
				return

		elif Option==2:
			allSelect=mc.ls(sl=True)
			allVrayMesh={}
			allModel={}
			for sel in allSelect:
				Meshs=mc.listRelatives(sel,c=True)[0]
				if Meshs:
					VraMeshs=mc.listConnections(Meshs,s=True,d=False)
					if VraMeshs and mc.objectType(VraMeshs[0])=='VRayMesh':
						allVrayMesh.update({sel:VraMeshs[0]})
					else:
						if "|" not in sel and "_" in sel:
							transName=sel.split('_')
							if transName[0] in transName[1]:
								allModel.update({sel:transName[0]})
				else:
					if "|" not in sel and "_" in sel:
						transName=sel.split('_')
						if transName[0] in transName[1]:
							allModel.update({sel:transName[0]})

			print allVrayMesh
			print allModel
			proxyType=os.listdir(OCT_PROXYPATH)
			#贴图路径
			sourceTex=""
			#项目路径
			projPath=mc.workspace(fn=True)+"/"
			infoVray=""
			infoArnold=""
			for vrayMesh in allVrayMesh.keys():
				getVRayMeshPath=mc.getAttr('%s.fileName'%allVrayMesh[vrayMesh])
				getVRayMeshName=os.path.basename(getVRayMeshPath)
				dirName=getVRayMeshName.split("_")[0]
				print "文件夹："
				print dirName
				arnoldDir=""
				myVRayMeshName=""
				oldTexPath=""
				for types in proxyType:
					myVRayMeshName=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\Vray_DL\\"+getVRayMeshName
					oldTexPath=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\arnoldtex\\"+dirName
					if os.path.isfile(myVRayMeshName):
						arnoldDir=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\arnoldtex\\"
						break
					else:
						continue

				if arnoldDir:
					myArnoldName=arnoldDir+dirName+"_AR.ass"
					if os.path.isfile(myArnoldName):
						if not os.path.isdir(projPath+"/sourceimages/arnoldtex"):
							os.makedirs(projPath+"/sourceimages/arnoldtex")
						try:
							shutil.copy2(myArnoldName,projPath+"/sourceimages/arnoldtex")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/arnoldtex/"+dirName+"_AR.ass"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(fileArnoldPrxy,i=True,type="ASS",ra=True,mergeNamespacesOnClash=False,pr=True,loadReferenceDepth="all")

						fileTexturePath=projPath+"/sourceimages/arnoldtex/"+dirName

						myAllMaps=mc.getFileList(filespec=(oldTexPath+"/*"))

						#拷贝贴图
						if not os.path.isdir(fileTexturePath):
							os.makedirs(fileTexturePath)
						if myAllMaps:
							for maps in myAllMaps:
								try:
									shutil.copy2((oldTexPath+"/"+maps),fileTexturePath)
								except:
									print(u'拷贝代理文件出错！\n')

						
						getTranslateVray=mc.getAttr(vrayMesh+".translate")[0]
						getRotateVray=mc.getAttr(vrayMesh+".rotate")[0]
						getScaleVray=mc.getAttr(vrayMesh+".scale")[0]

						ArnoldTransform=mc.listConnections('ArnoldStandInDefaultLightSet',s=True,d=False)[-1]
						mc.setAttr('%s.translate'%ArnoldTransform,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
						mc.setAttr('%s.rotate'%ArnoldTransform,getRotateVray[0],getRotateVray[1],getRotateVray[2])
						mc.setAttr('%s.scale'%ArnoldTransform,getScaleVray[0],getScaleVray[1],getScaleVray[2])
						mc.delete(vrayMesh)
						
					else:
						infoVray=allVrayMesh[vrayMesh]+","+myArnoldName+"\n"
				else:
					infoArnold=allVrayMesh[vrayMesh]+","+getVRayMeshPath+"\n"

			for trans in allModel.keys():
				arnoldDir=""
				#贴图路径
				oldTexPath=""
				transName=""
				for types in proxyType:
					myModelName=OCT_PROXYPATH+"\\"+types+"\\"+allModel[trans]+"\\scenes\\"+allModel[trans]+".mb"
					oldTexPath=OCT_PROXYPATH+"\\"+types+"\\"+allModel[trans]+"\\sourceimages\\arnoldtex\\"+allModel[trans]
					if os.path.isfile(myModelName):
						arnoldDir=OCT_PROXYPATH+"\\"+types+"\\"+allModel[trans]+"\\sourceimages\\arnoldtex\\"
						break
					else:
						continue
				if arnoldDir:
					myArnoldName=arnoldDir+allModel[trans]+"_AR.ass"
					if os.path.isfile(myArnoldName):
						if not os.path.isdir(projPath+"/sourceimages/arnoldtex"):
							os.makedirs(projPath+"/sourceimages/arnoldtex")
						try:
							shutil.copy2(myArnoldName,projPath+"/sourceimages/arnoldtex")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/arnoldtex/"+allModel[trans]+"_AR.ass"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(fileArnoldPrxy,i=True,type="ASS",ra=True,mergeNamespacesOnClash=False,pr=True,loadReferenceDepth="all")

						fileTexturePath=projPath+"/sourceimages/arnoldtex/"+allModel[trans]

						myAllMaps=mc.getFileList(filespec=(oldTexPath+"/*"))

						#拷贝贴图
						if not os.path.isdir(fileTexturePath):
							os.makedirs(fileTexturePath)
						if myAllMaps:
							for maps in myAllMaps:
								try:
									shutil.copy2((oldTexPath+"/"+maps),fileTexturePath)
								except:
									print(u'拷贝代理文件出错！\n')

						
						getTranslateVray=mc.getAttr(trans+".translate")[0]
						getRotateVray=mc.getAttr(trans+".rotate")[0]
						getScaleVray=mc.getAttr(trans+".scale")[0]

						ArnoldTransform=mc.listConnections('ArnoldStandInDefaultLightSet',s=True,d=False)[-1]
						mc.setAttr('%s.translate'%ArnoldTransform,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
						mc.setAttr('%s.rotate'%ArnoldTransform,getRotateVray[0],getRotateVray[1],getRotateVray[2])
						mc.setAttr('%s.scale'%ArnoldTransform,getScaleVray[0],getScaleVray[1],getScaleVray[2])
						mc.delete(trans)
						
					else:
						infoVray=trans+","+myArnoldName+"\n"
				else:
					infoModel=trans+","+myArnoldName+"\n"
			if infoArnold:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Vray代理或模型网路路劲没有对应的arnold代理文件,查看编辑窗口。")
				print "下列是场景中存在Vray代理或模型网路路劲没有对应的arnold代理文件:"
				print infoArnold
				return
			if infoVray:
				mc.confirmDialog(title=u"提示",message=u"场景中存在Vray代理网路路劲没有对应的Vray代理文件,查看编辑窗口。")
				print "下列是场景中存在Vray代理网路路劲没有对应的Vary代理文件:"
				print infoVray
				return

			if infoModel:
				mc.confirmDialog(title=u"提示",message=u"场景中存在模型网路路劲没有对应的模型文件,查看编辑窗口。")
				print "下列是场景中存在模型网路路劲没有对应的模型文件:"
				print infoVray
				return

	#Vray
	def ChangeVray(self):
		Option=mc.radioButtonGrp('Options',q=True,sl=True)
		infoVray=""
		infoArnold=""
		infoModel=""
		if Option==1:
			allArnoldProxys=mc.ls(type="aiStandIn")
			proxyType=os.listdir(OCT_PROXYPATH)
			#贴图路径
			sourceTex=""

			infoVray=""
			infoArnold=""
			#项目路径
			projPath=mc.workspace(fn=True)+"/"
			for arnoldProxys in allArnoldProxys:
				getArnoldPath=mc.getAttr("%s.dso"%arnoldProxys)
				getArnoldName=os.path.basename(getArnoldPath)
				dirName=getArnoldName.split("_")[0]
				print "文件夹："
				print dirName
				myArnoldName=""
				VrayDir=""
				OldTexturePath=""
				for types in proxyType:
					#查找anrold代理是否存在
					myArnoldName=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\arnoldtex\\"+getArnoldName
					OldTexturePath=(OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\"+dirName+"_txt").replace("\\","/")
					if os.path.isfile(myArnoldName):
						VrayDir=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\Vray_DL\\"
						break
					else:
						continue

				#查找网路路径下的Vray代理
				if VrayDir:
					myVRayMeshName=VrayDir+dirName+"_VR.vrmesh"
					PathVray=(VrayDir+dirName+"_VR.ma").replace("\\","/")
					if os.path.isfile(myVRayMeshName) and os.path.isfile(PathVray):
						if not os.path.isdir(projPath+"/sourceimages/Vray_DL"):
							os.makedirs(projPath+"/sourceimages/Vray_DL")
						try:
							shutil.copy2(myVRayMeshName,projPath+"/sourceimages/Vray_DL")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/Vray_DL/"+dirName+"_VR.vrmesh"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(PathVray,i=True,type='mayaAscii',ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",pr=True,loadReferenceDepth="all")

						PathType=myVRayMeshName.replace("\\","/")

						timeTo=mc.listConnections('time1')[-1]
						VrayMeshs=mc.listConnections(timeTo,s=False,d=True)[0]
						if mc.objectType(VrayMeshs)=="VRayMesh":
							fileVrayMeshs=mc.getAttr("%s.fileName"%VrayMeshs)
							fileVrayMesh=fileVrayMeshs.replace("\\","/")
							if fileVrayMesh==PathType:
								mc.setAttr("%s.fileName"%VrayMeshs,fileArnoldPrxy,type="string")


						allFiles=mc.ls(type="file")
						newTexturePath=projPath+"/sourceimages/"+dirName+"_txt"
						if not os.path.isdir(newTexturePath):
							os.makedirs(newTexturePath)

						for files in allFiles:
							fileTexPath=mc.getAttr("%s.fileTextureName"%files)
							if OldTexturePath in fileTexPath:
								if os.path.isfile(fileTexPath):
									try:
										shutil.copy2(fileTexPath,newTexturePath)
									except:
										print "拷贝贴图出错"
									newTexPath=newTexturePath+"/"+os.path.basename(fileTexPath)
									mc.setAttr("%s.fileTextureName"%files,newTexPath,type='string')

						arnoldTranNames=mc.listRelatives(arnoldProxys,p=True)[0]
						if mc.objectType(arnoldTranNames)=="transform":
							getTranslateArnold=mc.getAttr(arnoldTranNames+".translate")[0]
							getRotateArnold=mc.getAttr(arnoldTranNames+".rotate")[0]
							getScaleArnold=mc.getAttr(arnoldTranNames+".scale")[0]

							allMeshNames=mc.listConnections(VrayMeshs,s=False,d=True)
							for meshs in allMeshNames:
								if mc.objectType(meshs)=="transform":
									mc.setAttr('%s.translate'%meshs,getTranslateArnold[0],getTranslateArnold[1],getTranslateArnold[2])
									mc.setAttr('%s.rotate'%meshs,getRotateArnold[0],getRotateArnold[1],getRotateArnold[2])
									mc.setAttr('%s.scale'%meshs,getScaleArnold[0],getScaleArnold[1],getScaleArnold[2])
									mc.delete(arnoldTranNames)
									break
					else:
						infoVray=arnoldProxys+","+myVRayMeshName+","+PathVray+"\n"
				else:
					infoArnold=arnoldProxys+","+myArnoldName+"\n"

			allTran=mc.ls(type="transform")
			allTrans=[]
			for T in allTran:
				if not mc.listRelatives(T,p=True):
					allTrans.append(T)
			for trans in allTrans:
				VrayDir=""
				#贴图路径
				OldTexturePath=""
				transName=""
				if "|" not in trans and "_" in trans:
					transName=trans.split("_")
					if transName[0] in transName[1]:
						for types in proxyType:
							myModelName=OCT_PROXYPATH+"\\"+types+"\\"+transName[0]+"\\scenes\\"+transName[0]+".mb"
							OldTexturePath=(OCT_PROXYPATH+"\\"+types+"\\"+transName[0]+"\\sourceimages\\"+transName[0]+"_txt").replace("\\","/")
							if os.path.isfile(myModelName):
								VrayDir=OCT_PROXYPATH+"\\"+types+"\\"+transName[0]+"\\sourceimages\\Vray_DL\\"
								break
							else:
								continue
				if VrayDir:
					myVRayMeshName=VrayDir+transName[0]+"_VR.vrmesh"
					PathVray=(VrayDir+transName[0]+"_VR.ma").replace("\\","/")
					if os.path.isfile(myVRayMeshName) and os.path.isfile(PathVray):
						if not os.path.isdir(projPath+"/sourceimages/Vray_DL"):
							os.makedirs(projPath+"/sourceimages/Vray_DL")
						try:
							shutil.copy2(myVRayMeshName,projPath+"/sourceimages/Vray_DL")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/Vray_DL/"+transName[0]+"_VR.vrmesh"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(PathVray,i=True,type='mayaAscii',ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",pr=True,loadReferenceDepth="all")

						PathType=myVRayMeshName.replace("\\","/")

						timeTo=mc.listConnections('time1')[-1]
						VrayMeshs=mc.listConnections(timeTo,s=False,d=True)[0]
						if mc.objectType(VrayMeshs)=="VRayMesh":
							fileVrayMeshs=mc.getAttr("%s.fileName"%VrayMeshs)
							fileVrayMesh=fileVrayMeshs.replace("\\","/")
							if fileVrayMesh==PathType:
								mc.setAttr("%s.fileName"%VrayMeshs,fileArnoldPrxy,type="string")
								

						allFiles=mc.ls(type="file")
						newTexturePath=projPath+"/sourceimages/"+transName[0]+"_txt"
						if not os.path.isdir(newTexturePath):
							os.makedirs(newTexturePath)

						for files in allFiles:
							fileTexPath=mc.getAttr("%s.fileTextureName"%files)
							if OldTexturePath in fileTexPath:
								if os.path.isfile(fileTexPath):
									try:
										shutil.copy2(fileTexPath,newTexturePath)
									except:
										print "拷贝贴图出错"
									newTexPath=newTexturePath+"/"+os.path.basename(fileTexPath)
									mc.setAttr("%s.fileTextureName"%files,newTexPath,type='string')

						getTranslateVray=mc.getAttr(trans+".translate")[0]
						getRotateVray=mc.getAttr(trans+".rotate")[0]
						getScaleVray=mc.getAttr(trans+".scale")[0]

						allMeshNames=mc.listConnections(VrayMeshs,s=False,d=True)
						for meshs in allMeshNames:
							if mc.objectType(meshs)=="transform":
								mc.setAttr('%s.translate'%meshs,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
								mc.setAttr('%s.rotate'%meshs,getRotateVray[0],getRotateVray[1],getRotateVray[2])
								mc.setAttr('%s.scale'%meshs,getScaleVray[0],getScaleVray[1],getScaleVray[2])
								mc.delete(trans)
								break

					else:
						infoVray=trans+","+myVRayMeshName+","+PathVray+"\n"
				
			if infoArnold:
				mc.confirmDialog(title=u"提示",message=u"场景中存在arnold代理网路路劲没有对应的arnold代理,查看编辑窗口。")
				print "下列是场景中存在arnold代理网路路劲没有对应的arnold代理:"
				print infoArnold
				return
			if infoVray:
				mc.confirmDialog(title=u"提示",message=u"场景中存在arnold代理网路路劲没有对应的Vray代理或.ma代理文件,查看编辑窗口。")
				print "下列是场景中存在arnold代理网路路劲没有对应的Vray代理或.ma代理文件:"
				print infoVray
				return

		elif Option==2:
			allSelect=mc.ls(sl=True)
			allArnold={}
			allModel={}
			for sel in allSelect:
				Meshs=mc.listRelatives(sel,c=True)[0]
				if mc.objectType(Meshs)=='aiStandIn':
					allArnold.update({sel:Meshs})
				else:
					if "|" not in sel and "_" in sel:
						transName=sel.split('_')
						if transName[0] in transName[1]:
							allModel.update({sel:transName[0]})

			proxyType=os.listdir(OCT_PROXYPATH)
			#贴图路径
			sourceTex=""
			infoVray=""
			infoArnold=""
			#项目路径
			projPath=mc.workspace(fn=True)+"/"
			for arnolds in allArnold.keys():
				getArnoldPath=mc.getAttr("%s.dso"%allArnold[arnolds])
				getArnoldName=os.path.basename(getArnoldPath)
				dirName=getArnoldName.split("_")[0]
				print "文件夹："
				print dirName
				myArnoldName=""
				VrayDir=""
				OldTexturePath=""
				for types in proxyType:
					#查找anrold代理是否存在
					myArnoldName=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\arnoldtex\\"+getArnoldName
					OldTexturePath=(OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\"+dirName+"_txt").replace("\\","/")
					if os.path.isfile(myArnoldName):
						VrayDir=OCT_PROXYPATH+"\\"+types+"\\"+dirName+"\\sourceimages\\Vray_DL\\"
						break
					else:
						continue

				#查找网路路径下的Vray代理
				if VrayDir:
					myVRayMeshName=VrayDir+dirName+"_VR.vrmesh"
					PathVray=(VrayDir+dirName+"_VR.ma").replace("\\","/")
					if os.path.isfile(myVRayMeshName) and os.path.isfile(PathVray):
						if not os.path.isdir(projPath+"/sourceimages/Vray_DL"):
							os.makedirs(projPath+"/sourceimages/Vray_DL")
						try:
							shutil.copy2(myVRayMeshName,projPath+"/sourceimages/Vray_DL")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/Vray_DL/"+dirName+"_VR.vrmesh"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(PathVray,i=True,type='mayaAscii',ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",pr=True,loadReferenceDepth="all")

						PathType=myVRayMeshName.replace("\\","/")

						timeTo=mc.listConnections('time1')[-1]
						VrayMeshs=mc.listConnections(timeTo,s=False,d=True)[0]
						if mc.objectType(VrayMeshs)=="VRayMesh":
							fileVrayMeshs=mc.getAttr("%s.fileName"%VrayMeshs)
							fileVrayMesh=fileVrayMeshs.replace("\\","/")
							if fileVrayMesh==PathType:
								mc.setAttr("%s.fileName"%VrayMeshs,fileArnoldPrxy,type="string")


						allFiles=mc.ls(type="file")
						newTexturePath=projPath+"/sourceimages/"+dirName+"_txt"
						if not os.path.isdir(newTexturePath):
							os.makedirs(newTexturePath)

						for files in allFiles:
							fileTexPath=mc.getAttr("%s.fileTextureName"%files)
							if OldTexturePath in fileTexPath:
								if os.path.isfile(fileTexPath):
									try:
										shutil.copy2(fileTexPath,newTexturePath)
									except:
										print "拷贝贴图出错"
									newTexPath=newTexturePath+"/"+os.path.basename(fileTexPath)
									mc.setAttr("%s.fileTextureName"%files,newTexPath,type='string')

						
						getTranslateArnold=mc.getAttr(arnolds+".translate")[0]
						getRotateArnold=mc.getAttr(arnolds+".rotate")[0]
						getScaleArnold=mc.getAttr(arnolds+".scale")[0]

						allMeshNames=mc.listConnections(VrayMeshs,s=False,d=True)
						for meshs in allMeshNames:
							if mc.objectType(meshs)=="transform":
								mc.setAttr('%s.translate'%meshs,getTranslateArnold[0],getTranslateArnold[1],getTranslateArnold[2])
								mc.setAttr('%s.rotate'%meshs,getRotateArnold[0],getRotateArnold[1],getRotateArnold[2])
								mc.setAttr('%s.scale'%meshs,getScaleArnold[0],getScaleArnold[1],getScaleArnold[2])
								mc.delete(arnolds)
								break
					else:
						infoVray=allArnold[arnolds]+","+myVRayMeshName+","+PathVray+"\n"
				else:
					infoArnold=allArnold[arnolds]+","+myArnoldName+"\n"


			allTrans=mc.ls(type="transform")
			for trans in allModel.keys():
				VrayDir=""
				#贴图路径
				OldTexturePath=""
				transName=""
				for types in proxyType:
					myModelName=OCT_PROXYPATH+"\\"+types+"\\"+allModel[trans]+"\\scenes\\"+allModel[trans]+".mb"
					OldTexturePath=(OCT_PROXYPATH+"\\"+types+"\\"+allModel[trans]+"\\sourceimages\\"+allModel[trans]+"_txt").replace("\\","/")
					if os.path.isfile(myModelName):
						VrayDir=OCT_PROXYPATH+"\\"+types+"\\"+allModel[trans]+"\\sourceimages\\Vray_DL\\"
						break
					else:
						continue
				if VrayDir:
					myVRayMeshName=VrayDir+allModel[trans]+"_VR.vrmesh"
					PathVray=(VrayDir+allModel[trans]+"_VR.ma").replace("\\","/")
					if os.path.isfile(myVRayMeshName) and os.path.isfile(PathVray):
						if not os.path.isdir(projPath+"/sourceimages/Vray_DL"):
							os.makedirs(projPath+"/sourceimages/Vray_DL")
						try:
							shutil.copy2(myVRayMeshName,projPath+"/sourceimages/Vray_DL")
						except:
							print "拷贝.vrmesh文件出错"

						fileArnoldPrxy=projPath+"/sourceimages/Vray_DL/"+allModel[trans]+"_VR.vrmesh"
						if os.path.isfile(fileArnoldPrxy):
							mc.file(PathVray,i=True,type='mayaAscii',ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",pr=True,loadReferenceDepth="all")

						PathType=myVRayMeshName.replace("\\","/")

						timeTo=mc.listConnections('time1')[-1]
						VrayMeshs=mc.listConnections(timeTo,s=False,d=True)[0]
						if mc.objectType(VrayMeshs)=="VRayMesh":
							fileVrayMeshs=mc.getAttr("%s.fileName"%VrayMeshs)
							fileVrayMesh=fileVrayMeshs.replace("\\","/")
							if fileVrayMesh==PathType:
								mc.setAttr("%s.fileName"%VrayMeshs,fileArnoldPrxy,type="string")
								

						allFiles=mc.ls(type="file")
						newTexturePath=projPath+"/sourceimages/"+allModel[trans]+"_txt"
						if not os.path.isdir(newTexturePath):
							os.makedirs(newTexturePath)

						for files in allFiles:
							fileTexPath=mc.getAttr("%s.fileTextureName"%files)
							if OldTexturePath in fileTexPath:
								if os.path.isfile(fileTexPath):
									try:
										shutil.copy2(fileTexPath,newTexturePath)
									except:
										print "拷贝贴图出错"
									newTexPath=newTexturePath+"/"+os.path.basename(fileTexPath)
									mc.setAttr("%s.fileTextureName"%files,newTexPath,type='string')

						getTranslateVray=mc.getAttr(trans+".translate")[0]
						getRotateVray=mc.getAttr(trans+".rotate")[0]
						getScaleVray=mc.getAttr(trans+".scale")[0]

						allMeshNames=mc.listConnections(VrayMeshs,s=False,d=True)
						for meshs in allMeshNames:
							if mc.objectType(meshs)=="transform":
								mc.setAttr('%s.translate'%meshs,getTranslateVray[0],getTranslateVray[1],getTranslateVray[2])
								mc.setAttr('%s.rotate'%meshs,getRotateVray[0],getRotateVray[1],getRotateVray[2])
								mc.setAttr('%s.scale'%meshs,getScaleVray[0],getScaleVray[1],getScaleVray[2])
								mc.delete(trans)
								break

					else:
						infoVray=trans+","+myVRayMeshName+","+PathVray+"\n"
				
			if infoArnold:
				mc.confirmDialog(title=u"提示",message=u"场景中存在arnold代理网路路劲没有对应的arnold代理,查看编辑窗口。")
				print "下列是场景中存在arnold代理网路路劲没有对应的arnold代理:"
				print infoArnold
				return
			if infoVray:
				mc.confirmDialog(title=u"提示",message=u"场景中存在arnold代理网路路劲没有对应的Vray代理或.ma代理文件,查看编辑窗口。")
				print "下列是场景中存在arnold代理网路路劲没有对应的Vray代理或.ma代理文件:"
				print infoVray
				return



#OCT_ProxyChange_YH().OCT_ProxyChangeUI()