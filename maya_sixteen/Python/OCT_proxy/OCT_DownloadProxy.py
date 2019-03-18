# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import maya.cmds as mc
import maya.mel as mm
import os,re
import shutil

OCT_PROXYPATH=u'\\\\octvision.com\\cg\\Resource\\Material_Library\\Proxy\\ProxySeed'

#图片160*120


def OCT_DownloadProxyUI():
	proxyType=[]
	proxyType=[eaDir for eaDir in os.listdir(OCT_PROXYPATH) if os.path.isdir(os.path.join(OCT_PROXYPATH,eaDir))]
	if mc.window("OCT_ProxySeed",q=True,exists=True):
		mc.deleteUI("OCT_ProxySeed")
	mc.window("OCT_ProxySeed",title=u"代理库工具",widthHeight=(490,730),sizeable=False)
	form=mc.formLayout()
	tabs=mc.tabLayout("tabs")
	mc.formLayout(form,edit=True,attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
	if proxyType:
		for proxy in proxyType:
			mc.scrollLayout(proxy,p=tabs)
			mc.rowColumnLayout(proxy,numberOfColumns=3)
			PathType=OCT_PROXYPATH+"\\"+proxy
			path=os.listdir(PathType)
			if path:
				for j in range(len(path)):
					iconFile=PathType+"\\"+path[j]+"\\images\\"+path[j]+".bmp"
					mc.nodeIconButton(path[j],style='iconAndTextVertical', numberOfPopupMenus=True,image=iconFile,label=path[j],h=130,w=160,p=proxy,c='OCT_proxy.OCT_DownloadProxy.Opendir(%d)'%j)
					mc.popupMenu(path[j],parent=path[j],b=3)
					mc.menuItem(l=u"打开maya原文件",c='OCT_proxy.OCT_DownloadProxy.OpenMaya(%d)'%j,parent=path[j])
					mc.menuItem(l=u"打开maya_Vray原文件",c='OCT_proxy.OCT_DownloadProxy.OpenMayaVray(%d)'%j,parent=path[j])
					mc.menuItem(l=u"打开maya_Arnold原文件",c='OCT_proxy.OCT_DownloadProxy.OpenMayaArnold(%d)'%j,parent=path[j])
					mc.menuItem(l=u"导入Vray代理文件",c='OCT_proxy.OCT_DownloadProxy.ImportVray(%d)'%j,parent=path[j])
					mc.menuItem(l=u"导入Arnold代理文件",c='OCT_proxy.OCT_DownloadProxy.importArnold(%d)'%j,parent=path[j])
				mc.setParent("..")
			mc.setParent("..")

	mc.showWindow("OCT_ProxySeed")

def Opendir(j):
	tabsName=mc.tabLayout("tabs",q=True,selectTab=True)
	path=os.listdir(OCT_PROXYPATH+"\\"+tabsName)
	dirPath=OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]
	os.startfile(dirPath)

def OpenMaya(j):
	result = mc.confirmDialog(title=u"提示", message = u'是否需要打开maya原文件!\nYes打开, NO不打开', b = ['Yes', 'NO'])
	if result == 'NO':
		return
	tabsName=mc.tabLayout("tabs",q=True,selectTab=True)
	path=os.listdir(OCT_PROXYPATH+"\\"+tabsName)
	PathType=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\scenes\\"+path[j]+".mb").replace("\\","/")
	if os.path.isfile(PathType):
		mc.file(PathType,f=True,options="v=0;",typ="mayaBinary",o=True)
	else:
		messages=u"网络路径没有%s文件"%PathType
		mc.confirmDialog(title=u"警告",message=messages)
		return

def OpenMayaVray(j):
	result = mc.confirmDialog(title=u"提示", message = u'是否需要打开MayaVray原文件!\nYes打开, NO不打开', b = ['Yes', 'NO'])
	if result == 'NO':
		return
	tabsName=mc.tabLayout("tabs",q=True,selectTab=True)
	path=os.listdir(OCT_PROXYPATH+"\\"+tabsName)
	PathType=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\scenes\\"+path[j]+"_VR.mb").replace("\\","/")
	if os.path.isfile(PathType):
		mc.file(PathType,f=True,options="v=0;",typ="mayaBinary",o=True)
	else:
		messages=u"网络路径没有%s文件"%PathType
		mc.confirmDialog(title=u"警告",message=messages)
		return

def OpenMayaArnold(j):
	result = mc.confirmDialog(title=u"提示", message = u'是否需要打开MayaArnold原文件!\nYes打开, NO不打开', b = ['Yes', 'NO'])
	if result == 'NO':
		return
	tabsName=mc.tabLayout("tabs",q=True,selectTab=True)
	path=os.listdir(OCT_PROXYPATH+"\\"+tabsName)
	PathType=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\scenes\\"+path[j]+"_AR.mb").replace("\\","/")
	if os.path.isfile(PathType):
		mc.file(PathType,f=True,options="v=0;",typ="mayaBinary",o=True)
	else:
		messages=u"网络路径没有%s文件"%PathType
		mc.confirmDialog(title=u"警告",message=messages)
		return
def ImportVray(j):
	tabsName=mc.tabLayout("tabs",q=True,selectTab=True)
	filePath=mc.workspace(fn=True)+"/sourceimages/Vray_DL"
	path=os.listdir(OCT_PROXYPATH+"\\"+tabsName)
	if not os.path.isdir(filePath):
		os.makedirs(filePath)
	PathType=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\sourceimages\\Vray_DL\\"+path[j]+"_VR.vrmesh").replace("\\","/")
	PathVray=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\sourceimages\\Vray_DL\\"+path[j]+"_VR.ma").replace("\\","/")
	if os.path.isfile(PathType):
		try:
			shutil.copy2(PathType,filePath)
		except:
			print "拷贝.vrmesh文件出错"
		'''try:
			shutil.copy2(PathVray,filePath)
		except:
			print "拷贝.ma文件出错"'''
		
		mc.file(PathVray,i=True,type='mayaAscii',ra=True,mergeNamespacesOnClash=False,options="v=0;p=17;f=0",pr=True,loadReferenceDepth="all")
		allVrayMeshs=mc.ls(type="VRayMesh")

		if allVrayMeshs:
			for VrayMeshs in allVrayMeshs:
				fileVrayMeshs=mc.getAttr("%s.fileName"%VrayMeshs)
				fileVrayMesh=fileVrayMeshs.replace("\\","/")
				print fileVrayMesh
				print PathType
				if fileVrayMesh==PathType:
					mc.setAttr("%s.fileName"%VrayMeshs,filePath+"/"+path[j]+"_VR.vrmesh",type="string")
					break

		allFiles=mc.ls(type="file")
		OldTexturePath=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\sourceimages\\"+path[j]+"_txt").replace("\\","/")
		imageVRayDir=zwGetAssetType()
		newTexturePath=""
		if imageVRayDir:
			newTexturePath=mc.workspace(fn=True)+"/sourceimages/"+imageVRayDir
		else:
			newTexturePath=mc.workspace(fn=True)+"/sourceimages/"+path[j]+"_txt"

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
		
	else:
		messages=u"网络路径没有%s文件"%PathType
		mc.confirmDialog(title=u"警告",message=messages)
		return

def importArnold(j):
	tabsName=mc.tabLayout("tabs",q=True,selectTab=True)
	path=os.listdir(OCT_PROXYPATH+"\\"+tabsName)
	PathType=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\sourceimages\\arnoldtex\\"+path[j]+"_AR.ass").replace("\\","/")
	if os.path.isfile(PathType):
		filePath=mc.workspace(fn=True)+"/sourceimages/arnoldtex"
		if not os.path.isdir(filePath):
			os.makedirs(filePath)
		try:
			shutil.copy2(PathType,filePath)
		except:
			print "拷贝出错"

		fileArnoldPrxy=filePath+"/"+path[j]+"_AR.ass"
		if os.path.isfile(fileArnoldPrxy):
			mc.file(fileArnoldPrxy,i=True,type="ASS",ra=True,mergeNamespacesOnClash=False,pr=True,loadReferenceDepth="all")

		PathType=(OCT_PROXYPATH+"\\"+tabsName+"\\"+path[j]+"\\sourceimages\\arnoldtex\\"+path[j]).replace("\\","/")
		myAllMaps=mc.getFileList(filespec=(PathType+"/*"))

		fileTexturePath=mc.workspace(fn=True)+"/sourceimages/arnoldtex/"+path[j]

		if not os.path.isdir(fileTexturePath):
			os.makedirs(fileTexturePath)
		if myAllMaps:
			for maps in myAllMaps:
				try:
					shutil.copy2((PathType+"/"+maps),fileTexturePath)
				except:
					print(u'拷贝代理文件出错！\n')

	else:
		messages=u"网络路径没有%s文件"%PathType
		mc.confirmDialog(title=u"警告",message=messages)
		return


#前期文件类型:道具、场景、角色、相机
def zwGetAssetType():
    asset_type=""
    shortName=mc.file(q=True,sn=True,shortName=True)
    path=shortName.lower()
    pattern1=re.compile('^[^_]+_pr')
    pattern2=re.compile('^[^_]+_se')
    pattern3=re.compile('^[^_]+_ch')
    pr= pattern1.match(path)
    #pr.group()
    se=pattern2.match(path)
    ch=pattern3.match(path)

    if pr:
        asset_type="props"
    elif se:
        asset_type="sets"
    elif ch:
        asset_type="characters"

    return asset_type