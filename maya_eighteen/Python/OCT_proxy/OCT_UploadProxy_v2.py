# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import os
import re
import subprocess

OCT_DRIVE = r'\\octvision.com\cg'
CPAU_PATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
REMOTE_USER = r'octvision.com\supermaya'
REMOTE_PWD = 'supermaya'
FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\FastCopy341\FastCopy.exe'

OCT_PROXYPATH = u'\\\\octvision.com\\cg\\Resource\\Material_Library\\Proxy\\ProxySeed'

class OCT_UploadingProxy():
	def __init__(self):
		self.isCheckedSG=[]
		self.isCheckID=0
		#存放所有的SG节点
		self.nodeTypeGain=[]
		self.nodeId=""
		self.customSeedName=''
		self.nodeTypeFile=[]
		#self.NameSeedSList = []
		#self.NameSeedDList = []
	#构建窗口
	def OCT_UploadingProxyUI(self):
		if mc.window("OCT_UploadingProxyUI",q=True,ex=True):
			mc.deleteUI("OCT_UploadingProxyUI")
		mc.window("OCT_UploadingProxyUI",title="OCT_UploadingProxyUI",w=350,h=210,s=0)
		mc.columnLayout()
		mc.rowColumnLayout (numberOfColumns=2,co=[(1,"both",10),(2,"left",10)],columnWidth=[(1,375), (2,50)])
		mc.textFieldGrp('ProxyPath',label=u'代理网络路径 :',text=OCT_PROXYPATH,en=False,h=30,editable=True,ct2=('left','left'),cw2=(100,250))
		mc.checkBox('specifiedPath',label=u'指定路径',v=0,cc=lambda*args: self.specifiedPath())
		mc.setParent("..")

		mc.columnLayout()
		mc.radioButtonGrp('ProxyTypeF',label=u"代理种类 :",la3=["VR","AR",u"原文件"],sl=1,nrb=3,cal=[1,"center"])
		mc.setParent("..")
		mc.rowColumnLayout (numberOfColumns=2,co=[(1,"both",40),(2,"right",20)],columnWidth=[(1,230), (2,230)])
		mc.optionMenu("ProxySeed", label='ProxySeed :',cc=lambda*args: self.customProxySeedName())
		mc.menuItem("p1", label='Flowers' )
		mc.menuItem("p2", label='shrubs' )
		mc.menuItem("p3", label='trees' )
		mc.menuItem("p4", label='Tropical' )
		mc.menuItem("p5", label='vegetable' )
		mc.menuItem("p6", label='vines' )
		mc.menuItem('p7', label='custom' )

		mc.textFieldGrp('customName',label=u'自定义名称 :',text='custom',en=False)
		mc.setParent("..")
		mc.columnLayout(columnAttach=('left', 40), rowSpacing=10, columnWidth=285)
		mc.text("oCTCtrlb",label="",h=25)
		mc.text("oCTCtrlJPG",label="",h=25)
		mc.setParent("..")
		mc.rowLayout(numberOfColumns=6,columnWidth6=(20,100,110,100,100,10),columnAlign6=('center','center','center','center','center','center'))
		mc.text(l='',vis=0)
		mc.button(label=u"效果(.jpg)",w=80,h=25,c=lambda*args: self.OCT_oAttachImageJPG())
		mc.button(label=u"显示(.bmp)",w=80,h=25,c=lambda*args: self.OCT_oAttachImageBMP())
		mc.button(l=u'OK',w=80,h=25,align='center',c=lambda*args: self.OKButtonC())
		mc.button(l=u'Close',width=80,h=25,c=('mc.deleteUI("OCT_UploadingProxyUI",window=True)'))
		mc.text(l='',vis=0)
		mc.showWindow("OCT_UploadingProxyUI")

	def customProxySeedName(self):
		optionMenuValue = mc.optionMenu("ProxySeed",q=True,v=True)
		
		if optionMenuValue == "custom":
			customSeedName = mc.textFieldGrp('customName',q=True,text=True)
			mc.textFieldGrp('customName',e=True,en=True)	
		else:
			mc.textFieldGrp('customName',e=True,en=False)
			customSeedName = optionMenuValue

		return customSeedName

	#设置相关控件禁用
	def specifiedPath(self):
		checkBoxValue = mc.checkBox("specifiedPath",q=True,v=True)
		if checkBoxValue:
			mc.textFieldGrp('ProxyPath',e=True,en=True)
			mc.optionMenu("ProxySeed",e=True,en=False)
		else:
			mc.textFieldGrp('ProxyPath',e=True,en=False)
			mc.optionMenu("ProxySeed",e=True,en=True)

	#判断上传时调用的函数
	def OKButtonC(self):
		checkBoxValue1 = mc.checkBox("specifiedPath",q=True,v=True)
		if checkBoxValue1:
			self.OCT_exportSeedToolOld()
		else:
			self.OCT_exportSeedTool()

	def OCT_oAttachImageBMP(self):
		getfiles=mc.fileDialog2(fileMode=1,fileFilter="Image (*.bmp)",dialogStyle=2)
		if getfiles:
			mc.text("oCTCtrlb",e=True,label=getfiles[0])

	def OCT_oAttachImageJPG(self):
		getfiles=mc.fileDialog2(fileMode=1,fileFilter="Image (*.jpg)",dialogStyle=2)
		if getfiles:
			mc.text("oCTCtrlJPG",e=True,label=getfiles[0])

	def OCT_exportSeedTool(self):
		NameSeedSList = []
		NameSeedDList = []
		ProxySelect = mc.radioButtonGrp("ProxyTypeF",q=True,sl=True)
		
		targetPath=OCT_PROXYPATH+'\\'+self.customProxySeedName()

		if not targetPath:
			mc.confirmDialog(title=u"提示",message=u"请输入正确路径:例如：Z:\Resource\Material_Library\Proxy\ProxySeed\\animal")
			return
		target=targetPath.split("\\")
		proxyType=os.listdir(OCT_PROXYPATH)

		if not target[-1] in proxyType:
			mc.confirmDialog(title=u"提示",message=u"请输入正确路径:例如：Z:\Resource\Material_Library\Proxy\ProxySeed\\animal")
			return
		if targetPath.find('z:') >= 0:
			targetPath=targetPath.replace('z:', OCT_DRIVE)
		elif targetPath.find('Z:') >= 0:
			targetPath=targetPath.replace('Z:', OCT_DRIVE)

		#获取文件名
		filelongName=mc.file(q=True,sn=True)
		fileName=mc.file(q=True,sn=True,shortName=True)
		filelongNames = os.listdir(targetPath)

		for filelongName in filelongNames:
		    NameSeedS = re.findall("[a-z,A-Z]+",filelongName)
		    if NameSeedS[0] not in NameSeedSList:
		        NameSeedSList.append(NameSeedS[0])

		for NameSeedSListF in NameSeedSList:
		    Ftemp = str(NameSeedSListF) + "*\d*"
		    NameSeedNum = []
		    for filelongNamesF in filelongNames:
		        FFtemp = re.match(Ftemp,filelongNamesF)
		        if FFtemp != None:
		            NameSeedNum.append(FFtemp.group(0))

		    NameSeedDList.append(NameSeedNum)
						
		#获取渲染器
		render=mc.getAttr("defaultRenderGlobals.currentRenderer")

		#文件路径
		filePath=mc.workspace(fn=True)+"/scenes/OCT_Proxy/"
		if not os.path.isdir(filePath):
			mc.sysFile(filePath,md=True)

		allSelect=mc.ls(sl=True)
		if not allSelect:
			mc.confirmDialog(title=u"提示",message=u"请选择物体！")
			return
		fileNames = ""
		FfileNames = ""
		if ProxySelect == 3:
			listfile=fileName.split("_")
			if len(listfile)>1:
				FfileNames=listfile[0]
			else:
				FfileNames=fileName.split(".")[0]
		else:
			FfileNames=fileName.split(".")[0]
		#print NameSeedSList
		if FfileNames not in NameSeedSList:
			fileNames = FfileNames + "001"
		else:
			NameSeedSListIndex = NameSeedSList.index(FfileNames)
			NameSeedSListIndexNum = len(NameSeedDList[NameSeedSListIndex]) + 1
			if (NameSeedSListIndexNum < 9):
				fileNames = FfileNames + "00" + str(NameSeedSListIndexNum)
			elif (NameSeedSListIndexNum > 9 and NameSeedSListIndexNum < 99):
				fileNames = FfileNames + "0" + str(NameSeedSListIndexNum)
			else:
				fileNames = FfileNames + str(NameSeedSListIndexNum)

		#解决fileNames自动加序列号的问题	
		#print fileNames
		if ProxySelect == 3:
			mc.file(rename=filePath+fileNames)
		elif ProxySelect == 1:
			mc.file(rename=filePath+fileNames+"_VR")
		elif ProxySelect == 2:
			mc.file(rename=filePath+fileNames+"_AR")

		for T in allSelect:
			#if fileNames!=T:
			#	mc.confirmDialog(title=u"提示",message=u"选择物体组的名字错误应为%s,不能为:%s"%(fileNames,T))
			#	return
			#选择Vray
			if ProxySelect == 1:
				fileNameShort=mc.file(q=True,sn=True,shortName=True)

				self.OCT_UploadingTex(targetPath,T,1)
				rs=mc.file(force=True,prompt=False,save=True,uiConfiguration=False)
				if not rs:
					mc.sysFile((filePath+fileNameShort),delete=True)
					mc.error(u"不能保存文件，请检查是否D：盘空间不足")

				#拷贝原文件
				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					print(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort)
					if os.path.isfile(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort):
						listFileName=fileNameShort+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName):
							
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\scenes\\Backups\\",filespec=(fileNameShort+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileNameShort+"_c"+("%03d"%cver)

						sourceFile=targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break

				#拷贝文件
				if mc.file((filePath+fileNameShort),q=True,ex=True):
					fileVrayProxy=(filePath+fileNameShort).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\scenes"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break

				#代理文件
				fileName_vrmesh=T+"_VR.vrmesh"
				filePath_vrmesh=filePath
				if mc.file((filePath_vrmesh+fileName_vrmesh),q=True,ex=True):
					mc.sysFile((filePath_vrmesh+fileName_vrmesh),delete=True)

				try:
					mm.eval('vrayCreateProxy -createProxyNode -node "%s" -dir "%s" -fname "%s"'%(T,filePath_vrmesh,fileName_vrmesh))
				except:
					om.MGlobal.displayWarning(u'OCT warning : please checking the vray plugin is loading now!')

				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					if os.path.isfile(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+fileName_vrmesh):
						listFileName=fileName_vrmesh+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName):
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\",filespec=(fileName_vrmesh+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileName_vrmesh+"_c"+("%03d" % cver)

						sourceFile=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+fileName_vrmesh
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break

				#拷贝文件
				if mc.file((filePath_vrmesh+fileName_vrmesh),q=True,ex=True):
					fileVrayProxy=(filePath_vrmesh+fileName_vrmesh).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break		

				allVRayMesh=mc.ls(type="VRayMesh")
				
				for vrayMesh in allVRayMesh:
					mc.setAttr("%s.fileName"%vrayMesh,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+fileName_vrmesh),type="string")
					mc.setAttr("%s.showBBoxOnly"%vrayMesh,1)

				if mc.pluginInfo('vrayformaya',q=True,loaded=True):
					#mc.select(T,r=True)
					vrProxyFile=filePath+T+"_VR.ma"
					if mc.file(vrProxyFile,q=True,ex=True):
						mc.sysFile(vrProxyFile,delete=True)

					try:
						mc.file(vrProxyFile,force=True,options="v=0;",ch=True,type="mayaAscii",pr=True,es=True)
					except:
						pass

				print("the exported object is ==>"+filePath_vrmesh+fileName_vrmesh+"\n")

				#拷贝历史文件
				if os.path.isfile(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+T+"_VR.ma"):
					listFileName=T+"_VR.ma"+"_c001"
					if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName):
						
						cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
						if cmd:
							p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break
					else:
						allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\",filespec=(T+"_VR.ma"+"*"))
						lastVerfile=sorted(allBackupsFile)[-1]
						cver=int(lastVerfile.split("_c")[-1])+1
						listFileName=T+"_VR.ma"+"_c"+("%03d"%cver)


					sourceFile=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+T+"_VR.ma"
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
					if cmd:
						p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break

				#拷贝文件

				if mc.file(vrProxyFile,q=True,ex=True):
					fileVrayProxy=vrProxyFile.replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break	

			#选择Arnold
			elif ProxySelect == 2:
				fileNameShort=mc.file(q=True,sn=True,shortName=True)
				self.OCT_UploadingTex(targetPath,T,2)

				rs=mc.file(force=True,prompt=False,save=True,uiConfiguration=False)
				if not rs:
					mc.sysFile((filePath+fileNameShort),delete=True)
					mc.error(u"不能保存文件，请检查是否D：盘空间不足")

				#拷贝原文件
				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break

				else:
					print(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort)
					if os.path.isfile(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort):
						
						listFileName=fileNameShort+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName):
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\scenes\\Backups\\",filespec=(fileNameShort+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileNameShort+"_c"+("%03d"%cver)
							#print listFileName

						sourceFile=targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break


				#拷贝文件
				if mc.file((filePath+fileNameShort),q=True,ex=True):
					fileVrayProxy=(filePath+fileNameShort).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\scenes"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break	

				try:
					mc.setAttr("defaultRenderGlobals.currentRenderer","arnold",type="string")
				except:
					om.MGlobal.displayWarning(u'OCT warning : please check using arnold  as current render\n')
				
				fileName_format=filePath+T+"_AR.ass"

				if mc.file(fileName_format,q=True,ex=True):
					mc.sysFile(fileName_format,delete=True)

				#设置创建代理的路径
				#self.OCT_setArnoldTexPath(fileNames)
				#创建arnold代理
				try:
					mc.setAttr("defaultArnoldRenderOptions.absoluteTexturePaths",0)
				except:
					om.MGlobal.displayWarning(u'OCT warning : please check the arnold render is loaded and using now!')

				if mc.pluginInfo('mtoa.mll',q=True,loaded=True):
					try:
						mc.file(fileName_format,force=True,options="-mask 25;-lightLinks 0;-shadowLinks 0",type="ASS Export",pr=True,es=True)
						print("the exported object is ==> "+fileName_format+"\n")
					except:
						pass
				try:
					mc.setAttr("defaultRenderGlobals.currentRenderer",render,type="string")
				except:
					pass

				#修改arnold代理路径
				self.change_Proxy_Map_Path(fileName_format,T)


				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					print(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\"+T+"_AR.ass")
					if os.path.isfile(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\"+T+"_AR.ass"):
						listFileName=T+"_AR.ass"+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\"+listFileName):
							
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\",filespec=(T+"_AR.ass"+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=T+"_AR.ass"+"_c"+("%03d"%cver)

						sourceFile=targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\"+T+"_AR.ass"
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break


				if mc.file(fileName_format,q=True,ex=True):
					fileArnoldProxy=fileName_format.replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileArnoldProxy,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break

			#上传原文件
			if ProxySelect == 3:
				fileNameShort=mc.file(q=True,sn=True,shortName=True)
				self.OCT_UploadingTex(targetPath,T,3)
				rs=mc.file(force=True,prompt=False,save=True,uiConfiguration=False)
				if not rs:
					mc.sysFile((filePath+fileNameShort),delete=True)
					mc.error(u"不能保存文件，请检查是否D：盘空间不足")

				#拷贝原文件
				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					print(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort)
					if os.path.isfile(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort):
						listFileName=fileNameShort+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName):
							
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\scenes\\Backups\\",filespec=(fileNameShort+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileNameShort+"_c"+("%03d"%cver)

						sourceFile=targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break

				#拷贝文件
				if mc.file((filePath+fileNameShort),q=True,ex=True):
					fileVrayProxy=(filePath+fileNameShort).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\scenes"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break


			#上传按钮的bmp贴图
			oAttachImage=mc.text("oCTCtrlb",q=True,label=True)
			if oAttachImage:
				if oAttachImage.find('z:') >= 0:
					oAttachImage=oAttachImage.replace('z:', OCT_DRIVE)
				elif oAttachImage.find('Z:') >= 0:
					oAttachImage=oAttachImage.replace('Z:', OCT_DRIVE)

				if not os.path.isdir(targetPath+"\\"+fileNames+"\\images"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\images"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
								
				if mc.file(oAttachImage,q=True,ex=True):
					oAttachImage=oAttachImage.replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, oAttachImage,(targetPath+"\\"+fileNames+"\\images"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break
			#上传效果图
			oAttachImageJPG=mc.text("oCTCtrlJPG",q=True,label=True)
			if oAttachImageJPG:
				if oAttachImageJPG.find('z:')>=0:
					oAttachImageJPG=oAttachImageJPG.replace('z:',OCT_DRIVE)
				elif oAttachImageJPG.find('Z:')>=0:
					oAttachImageJPG=oAttachImageJPG.replace('Z:',OCT_DRIVE)
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\images"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNamesJPG+"\\images"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				if mc.file(oAttachImageJPG,q=True,ex=True):
					oAttachImageJPG=oAttachImageJPG.replace("/","\\")
					cmd=r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, oAttachImageJPG,(targetPath+"\\"+fileNames+"\\images"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break

	def OCT_exportSeedToolOld(self):
		NameSeedSList = []
		NameSeedDList = []
		ProxySelect = mc.radioButtonGrp("ProxyTypeF",q=True,sl=True)

		targetPath=mc.textFieldGrp("ProxyPath",q=True,text=True)

		if not targetPath:
			mc.confirmDialog(title=u"提示",message=u"请输入正确路径:例如：Z:\Resource\Material_Library\Proxy\ProxySeed\\animal")
			return
		target=targetPath.split("\\")
		proxyType=os.listdir(OCT_PROXYPATH)

		#print target
		if not target[-1] in proxyType:
			mc.confirmDialog(title=u"提示",message=u"请输入正确路径:例如：Z:\Resource\Material_Library\Proxy\ProxySeed\\animal")
			return
		if targetPath.find('z:') >= 0:
			targetPath=targetPath.replace('z:', OCT_DRIVE)
		elif targetPath.find('Z:') >= 0:
			targetPath=targetPath.replace('Z:', OCT_DRIVE)

		#获取文件名
		filelongName=mc.file(q=True,sn=True)
		fileName=mc.file(q=True,sn=True,shortName=True)

						
		#获取渲染器
		render=mc.getAttr("defaultRenderGlobals.currentRenderer")

		#文件路径
		filePath=mc.workspace(fn=True)+"/scenes/OCT_Proxy/"
		if not os.path.isdir(filePath):
			mc.sysFile(filePath,md=True)

		allSelect=mc.ls(sl=True)
		if not allSelect:
			mc.confirmDialog(title=u"提示",message=u"请选择物体！")
			return
		fileNames=""
		if ProxySelect == 3:
			listfile=fileName.split("_")
			if len(listfile)>1:
				fileNames=listfile[0]
			else:
				fileNames=fileName.split(".")[0]
		else:
			fileNames=fileName.split("_")[0]
		#print fileNames
		if ProxySelect == 3:
			mc.file(rename=filePath+fileNames)
		elif ProxySelect == 1:
			mc.file(rename=filePath+fileNames+"_VR")
		elif ProxySelect == 2:
			mc.file(rename=filePath+fileNames+"_AR")

		for T in allSelect:
			if fileNames!=T:
				mc.confirmDialog(title=u"提示",message=u"选择物体组的名字错误应为%s,不能为:%s"%(fileNames,T))
				return
			#选择Vray
			if ProxySelect == 1:
				fileNameShort=mc.file(q=True,sn=True,shortName=True)

				self.OCT_UploadingTex(targetPath,T,1)
				rs=mc.file(force=True,prompt=False,save=True,uiConfiguration=False)
				if not rs:
					mc.sysFile((filePath+fileNameShort),delete=True)
					mc.error(u"不能保存文件，请检查是否D：盘空间不足")

				#拷贝原文件
				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					print(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort)
					if os.path.isfile(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort):
						listFileName=fileNameShort+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName):
							
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\scenes\\Backups\\",filespec=(fileNameShort+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileNameShort+"_c"+("%03d"%cver)

						sourceFile=targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break

				#拷贝文件
				if mc.file((filePath+fileNameShort),q=True,ex=True):
					fileVrayProxy=(filePath+fileNameShort).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\scenes"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break

				#代理文件
				fileName_vrmesh=T+"_VR.vrmesh"
				filePath_vrmesh=filePath
				if mc.file((filePath_vrmesh+fileName_vrmesh),q=True,ex=True):
					mc.sysFile((filePath_vrmesh+fileName_vrmesh),delete=True)

				try:
					mm.eval('vrayCreateProxy -createProxyNode -node "%s" -dir "%s" -fname "%s"'%(T,filePath_vrmesh,fileName_vrmesh))
				except:
					om.MGlobal.displayWarning(u'OCT warning : please checking the vray plugin is loading now!')

				#fileNames=fileName.split("_")[0]
				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					if os.path.isfile(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+fileName_vrmesh):
						listFileName=fileName_vrmesh+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName):
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\",filespec=(fileName_vrmesh+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileName_vrmesh+"_c"+("%03d"%cver)

						sourceFile=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+fileName_vrmesh
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break

				#拷贝文件
				if mc.file((filePath_vrmesh+fileName_vrmesh),q=True,ex=True):
					fileVrayProxy=(filePath_vrmesh+fileName_vrmesh).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break		

				allVRayMesh=mc.ls(type="VRayMesh")
				
				for vrayMesh in allVRayMesh:
					mc.setAttr("%s.fileName"%vrayMesh,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+fileName_vrmesh),type="string")
					mc.setAttr("%s.showBBoxOnly"%vrayMesh,1)

				if mc.pluginInfo('vrayformaya',q=True,loaded=True):
					#mc.select(T,r=True)
					vrProxyFile=filePath+T+"_VR.ma"
					if mc.file(vrProxyFile,q=True,ex=True):
						mc.sysFile(vrProxyFile,delete=True)

					try:
						mc.file(vrProxyFile,force=True,options="v=0;",ch=True,type="mayaAscii",pr=True,es=True)
					except:
						pass

				print("the exported object is ==>"+filePath_vrmesh+fileName_vrmesh+"\n")

				#拷贝历史文件
				if os.path.isfile(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+T+"_VR.ma"):
					listFileName=T+"_VR.ma"+"_c001"
					if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName):
						
						cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
						if cmd:
							p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break
					else:
						allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\Backups\\",filespec=(T+"_VR.ma"+"*"))
						lastVerfile=sorted(allBackupsFile)[-1]
						cver=int(lastVerfile.split("_c")[-1])+1
						listFileName=T+"_VR.ma"+"_c"+("%03d"%cver)


					sourceFile=targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL\\"+T+"_VR.ma"
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\\sourceimages\\Vray_DL\\Backups\\"+listFileName))
					if cmd:
						p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break

				#拷贝文件

				if mc.file(vrProxyFile,q=True,ex=True):
					fileVrayProxy=vrProxyFile.replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\sourceimages\\Vray_DL"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break	

			#选择Arnold
			elif ProxySelect == 2:
				fileNameShort=mc.file(q=True,sn=True,shortName=True)
				self.OCT_UploadingTex(targetPath,T,2)

				rs=mc.file(force=True,prompt=False,save=True,uiConfiguration=False)
				if not rs:
					mc.sysFile((filePath+fileNameShort),delete=True)
					mc.error(u"不能保存文件，请检查是否D：盘空间不足")

				#拷贝原文件
				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break

				else:
					print(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort)
					if os.path.isfile(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort):
						
						listFileName=fileNameShort+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName):
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\scenes\\Backups\\",filespec=(fileNameShort+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileNameShort+"_c"+("%03d"%cver)
							print listFileName

						sourceFile=targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break


				#拷贝文件
				if mc.file((filePath+fileNameShort),q=True,ex=True):
					fileVrayProxy=(filePath+fileNameShort).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\scenes"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break	

				try:
					mc.setAttr("defaultRenderGlobals.currentRenderer","arnold",type="string")
				except:
					om.MGlobal.displayWarning(u'OCT warning : please check using arnold  as current render\n')
				
				fileName_format=filePath+T+"_AR.ass"

				if mc.file(fileName_format,q=True,ex=True):
					mc.sysFile(fileName_format,delete=True)

				#设置创建代理的路径
				#self.OCT_setArnoldTexPath(fileNames)
				#创建arnold代理
				try:
					mc.setAttr("defaultArnoldRenderOptions.absoluteTexturePaths",0)
				except:
					om.MGlobal.displayWarning(u'OCT warning : please check the arnold render is loaded and using now!')

				if mc.pluginInfo('mtoa.mll',q=True,loaded=True):
					try:
						mc.file(fileName_format,force=True,options="-mask 25;-lightLinks 0;-shadowLinks 0",type="ASS Export",pr=True,es=True)
						print("the exported object is ==> "+fileName_format+"\n")
					except:
						pass
				try:
					mc.setAttr("defaultRenderGlobals.currentRenderer",render,type="string")
				except:
					pass

				#修改arnold代理路径
				self.change_Proxy_Map_Path(fileName_format,T)


				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					print(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\"+T+"_AR.ass")
					if os.path.isfile(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\"+T+"_AR.ass"):
						listFileName=T+"_AR.ass"+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\"+listFileName):
							
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\",filespec=(T+"_AR.ass"+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=T+"_AR.ass"+"_c"+("%03d"%cver)

						sourceFile=targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\"+T+"_AR.ass"
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break


				if mc.file(fileName_format,q=True,ex=True):
					fileArnoldProxy=fileName_format.replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileArnoldProxy,(targetPath+"\\"+fileNames+"\\sourceimages\\arnoldtex"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break

			#上传原文件
			if ProxySelect == 3:
				fileNameShort=mc.file(q=True,sn=True,shortName=True)
				self.OCT_UploadingTex(targetPath,T,3)
				rs=mc.file(force=True,prompt=False,save=True,uiConfiguration=False)
				if not rs:
					mc.sysFile((filePath+fileNameShort),delete=True)
					mc.error(u"不能保存文件，请检查是否D：盘空间不足")

				#拷贝原文件
				#创建文件夹
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				else:
					print(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort)
					if os.path.isfile(targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort):
						listFileName=fileNameShort+"_c001"
						if not os.path.isdir(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName):
							
							cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
							if cmd:
								p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
								while True:
									if not p.poll() is None:
										del p
										break
						else:
							allBackupsFile=mc.getFileList(folder=targetPath+"\\"+fileNames+"\\scenes\\Backups\\",filespec=(fileNameShort+"*"))
							lastVerfile=sorted(allBackupsFile)[-1]
							cver=int(lastVerfile.split("_c")[-1])+1
							listFileName=fileNameShort+"_c"+("%03d"%cver)

						sourceFile=targetPath+"\\"+fileNames+"\\scenes\\"+fileNameShort
						cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceFile,(targetPath+"\\"+fileNames+"\\scenes\\Backups\\"+listFileName))
						if cmd:
							p=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
							while True:
								if not p.poll() is None:
									del p
									break

				#拷贝文件
				if mc.file((filePath+fileNameShort),q=True,ex=True):
					fileVrayProxy=(filePath+fileNameShort).replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, fileVrayProxy,(targetPath+"\\"+fileNames+"\\scenes"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break


			#上传按钮的bmp贴图
			oAttachImage=mc.text("oCTCtrlb",q=True,label=True)
			if oAttachImage:
				if oAttachImage.find('z:') >= 0:
					oAttachImage=oAttachImage.replace('z:', OCT_DRIVE)
				elif oAttachImage.find('Z:') >= 0:
					oAttachImage=oAttachImage.replace('Z:', OCT_DRIVE)

				if not os.path.isdir(targetPath+"\\"+fileNames+"\\images"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNames+"\\images"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
								
				if mc.file(oAttachImage,q=True,ex=True):
					oAttachImage=oAttachImage.replace("/","\\")
					cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, oAttachImage,(targetPath+"\\"+fileNames+"\\images"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break
			#上传效果图
			oAttachImageJPG=mc.text("oCTCtrlJPG",q=True,label=True)
			if oAttachImageJPG:
				if oAttachImageJPG.find('z:')>=0:
					oAttachImageJPG=oAttachImageJPG.replace('z:',OCT_DRIVE)
				elif oAttachImageJPG.find('Z:')>=0:
					oAttachImageJPG=oAttachImageJPG.replace('Z:',OCT_DRIVE)
				if not os.path.isdir(targetPath+"\\"+fileNames+"\\images"):
					cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,(targetPath+"\\"+fileNamesJPG+"\\images"))
					if cmd:
						p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
						while True:
							if not p.poll() is None:
								del p
								break
				if mc.file(oAttachImageJPG,q=True,ex=True):
					oAttachImageJPG=oAttachImageJPG.replace("/","\\")
					cmd=r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, oAttachImageJPG,(targetPath+"\\"+fileNames+"\\images"))
					#cmd = str(cmd).encode("gb2312")
					p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
					while True:
						if not p.poll() is None:
							del p
							break						

	#设置创建代理的贴图路径
	def OCT_setArnoldTexPath(self,fileNames):
		arnoldProxyPath="arnoldtex/"+fileNames+"/"
		print self.nodeTypeFile
		if self.nodeTypeFile:
			for texFileNode in self.nodeTypeFile:
				pathfile=mc.getAttr("%s.fileTextureName"%texFileNode)
				fileTexturePath=arnoldProxyPath+os.path.basename(pathfile)
				mc.setAttr("%s.fileTextureName"%texFileNode,fileTexturePath,type="string")

	#修改arnold代理贴图的路径
	def change_Proxy_Map_Path(self,path,dirName):
		print "change_Proxy_Map_Path"
		try:
			lines=open(path,'r').readlines()
			for i in range(len(lines)):
				if ' filename ' in lines[i]:
					mapPath=lines[i].split(" ")[-1]
					mapName=mapPath.replace("\\","/")
					mapName=mapName.split("/")[-1]
					newPath="\""+"arnoldTex/"+dirName+"/"+mapName
					lines[i]=lines[i].replace(mapPath,newPath)
			open(path,'w').writelines(lines)
		except Exception,e:
			print e

	#贴图
	def OCT_UploadingTex(self,targetPath,T,num):
		#获取型节点
		shape=mc.listRelatives(T,f=True,ad=True,c=True,ni=True,type=["mesh","nurbsSurface"])
		#存放SG节点
		arnoldSG_tempName=[]
		arnoldSG_tempIndex=0
		isCheckedSG=[]
		projPath=mc.workspace(fn=True)+"/"
		if num==1:
			fileName=mc.file(q=True,sn=True,shortName=True).split("_")[0]
			ecoTexPath =targetPath+"/"+fileName+"/sourceimages/"+fileName+"_txt"
		elif num==2:
			fileName=mc.file(q=True,sn=True,shortName=True).split("_")[0]
			fileExt=fileName.split(".")[0]
			ecoTexPath=targetPath+"/"+fileName+"/sourceimages/arnoldtex/"+fileExt
		elif num==3:
			fileName=mc.file(q=True,sn=True,shortName=True).split(".")[0]
			ecoTexPath =targetPath+"/"+fileName+"/sourceimages/"+fileName+"_txt"

		for shapeT in shape:
			#获取型节点连接的SG节点
			SG=mc.listConnections(shapeT,s=False,type="shadingEngine")
			if SG:
				for SGT in SG:
					self.nodeTypeGain=[]
					if not SGT in isCheckedSG:
						#获取所有的file节点在nodeTypeGain组中
						self.OCT_getInputMatNodeArray("file",SGT) 
						isCheckedSG.append(SGT)
				
					#print self.nodeTypeGain
					if self.nodeTypeFile:
						self.nodeTypeFile=self.nodeTypeFile+self.nodeTypeGain
					else:
						self.nodeTypeFile=self.nodeTypeGain

					if self.nodeTypeGain:
						for texFileNodeT in self.nodeTypeGain:
							sourceTex=""
							tex=mc.getAttr("%s.fileTextureName"%texFileNodeT)
							if tex.find('z:') >= 0:
								tex=tex.replace('z:', OCT_DRIVE).replace("\\","/")
							elif tex.find('Z:') >= 0:
								tex=tex.replace('Z:', OCT_DRIVE).replace("\\","/")
							#print tex

							if mc.file((projPath+tex),q=True,ex=True):
								sourceTex=projPath+tex
							elif mc.file(tex,q=True,ex=True):
								sourceTex=tex
							else:
								tokenP=tex.split("/")
								for TT in tokenP:
									if TT==tokenP[-1]:
										sourceTex=sourceTex+TT
									else:
										sourceTex=sourceTex+TT+"/"

							tokenTex=tex.split("/")
							texName=tokenTex[-1]
							tartgetTexPath=ecoTexPath

							if not os.path.isdir(tartgetTexPath):
								mc.sysFile(tartgetTexPath,md=True)
							if mc.file(sourceTex,q=True,ex=True):
								#创建文件夹
								if not os.path.isdir(tartgetTexPath):
									fileVrayProxy=tartgetTexPath.replace("/","\\")
									cmd='%s -u %s -p %s -lwp -c -nowarn -wait -ex "md %s"' %(CPAU_PATH, REMOTE_USER, REMOTE_PWD,fileVrayProxy)

									if cmd:
										p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
										while True:
											if not p.poll() is None:
												del p
												break
								#拷贝文件
								sourceTex=sourceTex.replace("/","\\")
								tartgetTexPath=(tartgetTexPath).replace("/","\\")
								textureName=os.path.basename(sourceTex)
								if not os.path.isfile(tartgetTexPath+"\\"+textureName):
									cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, sourceTex,tartgetTexPath)
									p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
									while True:
										if not p.poll() is None:
											del p
											break

							else:
								mc.confirmDialog(t="OCT error",message=u"%s节点相连接的%s贴图没找到"%(texFileNodeT,sourceTex))
								mc.error(u"%s节点相连接的%s贴图没找到"%(texFileNodeT,sourceTex))

							#print tartgetTexPath
							mc.setAttr("%s.fileTextureName"%texFileNodeT,(tartgetTexPath+"/"+texName),type="string")
							print mc.getAttr("%s.fileTextureName"%texFileNodeT)

	def OCT_getInputMatNodeArray(self,nodeType,checkNode_SG):
		allFiles = mc.ls(type = nodeType)
		for con in allFiles:
			self.nodeTypeGain.append(con)

# OCT_UploadingProxy().OCT_UploadingProxyUI()
