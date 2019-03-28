#!/usr/bin/python
# -*- coding: utf-8 -*- 

import maya.cmds as mc
import os
import Rename

def uploadProxy(num):
	allName=["wangyq","qiaol","zengzhf","yangh"]
	Name=os.getenv('username')
	if Name in allName:
		if num == 1:
			import OCT_UploadProxy
			i=OCT_UploadProxy.OCT_UploadingProxy()
			i.OCT_UploadingProxyUI()
		elif num == 2:
			import OCT_UploadProxy_v2
			i = OCT_UploadProxy_v2.OCT_UploadingProxy()
			i.OCT_UploadingProxyUI()
	else:
		mc.confirmDialog(title=u"提示",message=u"上传代理仅提供模型的王毅强和乔玲")
		return
		
def download():
	import OCT_DownloadProxy
	OCT_DownloadProxy.OCT_DownloadProxyUI()


def newProxyChange():
	import OCT_ProxyChange
	i=OCT_ProxyChange.OCT_ProxyChange_YH()
	i.OCT_ProxyChangeUI()
	
def SameNameProxyChange():
	import OCT_SameNameProxyChange
	i=OCT_SameNameProxyChange.OCT_SameNameProxyChange()
	i.OCT_UploadingProxyUI()
	
def VRayProxyChangeModel():
	import OCT_VRayProxyChangeModel
	i=OCT_VRayProxyChangeModel.OCT_VRayProxyChangeModel()
	i.VRayChangeModel()

def proxyChanges():
	import OCT_ALLVRayProxyChangeArnoldProxy
	OCT_ALLVRayProxyChangeArnoldProxy.proxyChange()

def ExchangeProxy4Instance():
	import OCT_ExchangeProxy_v1 as oep
	if (mc.window('exchProxyWin', exists=True, q=True)):
		mc.deleteUI('exchProxyWin')
	inWin = oep.OCT_ExchangeProxy()
	inWin.show()
	inWin.raise_()