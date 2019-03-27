# -*- coding: utf-8 -*-
import sys, os
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
import PyQt4.uic as uic
import maya.OpenMayaUI as omu
import maya.OpenMaya as om
import maya.mel as mm
import sip

pyqtPath = '\\\\octvision.com/cg/Tech/maya_sixteen/Lib'
# scriptsPath = 'D:/Work/maya_Scripts/AutoOptimizeScene'
scriptsPath = r'//octvision.com/CG/Tech/maya_sixteen/Python/OCT_check/AutoOptimizeScene'
# scriptsPath = r'D:/MayaSixteenScripts/Python/OCT_check/AutoOptimizeScene'
# if pyqtPath not in sys.path:
# 	sys.path.append (pyqtPath)

import cleanUnusedCamera_zwz
import delDefaultRenderLayer
import deleteUnknown
import delNurbsCurve
import OCT_CheckRefence
import deleteUnuseLightDecay
import deleteUnUseVRayMesh

pyObject = omu.MQtUtil.mainWindow ()
mainWindow = sip.wrapinstance (long (pyObject), QtGui.QWidget)

uiFile = scriptsPath + '/myuis/AutoOptimizeScene.myuis'
print uiFile 
formClass, baseClass = uic.loadUiType (uiFile)

class AutoOptimizeScene (formClass, baseClass) :
	def __init__(self,parent = mainWindow):
		super (AutoOptimizeScene, self).__init__(parent)

		self.setupUi (self)
		self.show ()

		self.uiConfigure ()

	def uiConfigure (self) :
		self.setWindowTitle (u"优化工具集1.0")

		self.pButton_1.clicked.connect (self.executeSelectScript)
		self.pButton_2.clicked.connect (self.close)
		#self.pButton_3.clicked.connect (self.allSelect)

	def executeSelectScript (self):
		scriptsName = []
		executeScripts = self.checkStatus ()
		
		if executeScripts[0] == 2:
			mm.eval('source \"%s/oct_delNameSpace.mel\"' % scriptsPath)
			scriptsName.append(u'删命名空间')
		if executeScripts[1] == 2:
			mm.eval('source \"%s/renameTransForm_muilty_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'解决重名')
		if executeScripts[2] == 2:
			mm.eval('source \"%s/OCT_reLongName.mel\"' % scriptsPath)
			scriptsName.append(u'解决名字过长')
		if executeScripts[3] == 2:
			mm.eval('source \"%s/delete_name_space_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'清前缀')
		if executeScripts[4] == 2:
			mm.eval('source \"%s/deleteMidMeshSafe_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'清midMesh')
		if executeScripts[5] == 2:
			mm.eval('source \"%s/clearNoVertex_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'清无点polygon')
		if executeScripts[6] == 2:
			mm.eval('source \"%s/clearLJ_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'清各种垃圾')
		if executeScripts[7] == 2:
			mm.eval('source \"%s/checkingSmallArea_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'清极小物体')
		if executeScripts[8] == 2:
			delNurbsCurve.delNurbsCurve()
			scriptsName.append(u'清NurbsCurve')
		if executeScripts[9] == 2:
			mm.eval('source \"%s/clearlightLinkerConnections_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'清灯光链接')
		if executeScripts[10] == 2:
			deleteUnknown.deleteUnknown()
			scriptsName.append(u'清unknown')
		if executeScripts[11] == 2:
			OCT_CheckRefence.OCT_CheckRefence().deleteUnusedReference()
			scriptsName.append(u'清Reference')
		if executeScripts[12] == 2:
			mm.eval('source \"%s/deleteUnusedShade.mel\"' % scriptsPath)
			scriptsName.append(u'清多余材质球')
		if executeScripts[13] == 2:
			delDefaultRenderLayer.delDefaultRenderLayer()
			scriptsName.append(u'清多余默认渲染层')
		if executeScripts[14] == 2:
			deleteUnuseLightDecay.deleteUnuseLightDecay()
			scriptsName.append(u'清多余灯光衰减')
		if executeScripts[15] == 2:
			mm.eval('source \"%s/delect_UnuseredCache.mel\"' % scriptsPath)
			scriptsName.append(u'清无用缓存节点')
		if executeScripts[16] == 2:
			cleanUnusedCamera_zwz.cleanUnusedCamera_zwz()
			scriptsName.append(u'清多余相机')
		if executeScripts[17] == 2:
			mm.eval('source \"%s/clearInitialmat_zqs.mel\"' % scriptsPath)
			scriptsName.append(u'清默认材质球')

		if executeScripts[18] == 2:
			mm.eval('source \"%s/OCT_clearPlugin.mel\"' % scriptsPath)
			scriptsName.append(u'清理无用插件')

		if executeScripts[19] == 2:
			deleteUnUseVRayMesh.deleteUnUseVRayMesh()
			scriptsName.append(u'清无用的VRayMesh')


		
		fnum = len(scriptsName)
		print ('一共执行了 %d 个脚本......\n' % fnum).encode("gbk")

		for aaa in scriptsName:
			print (aaa + '\n').encode("gbk")
		

	def checkStatus(self):
		i = 1
		listchecks = []
		while i <21 :
			#a = self.checkBox_1.isChecked()
			sl_checkBox = eval('self.checkBox_'+ str(i) + '.checkState()')
			listchecks.append(sl_checkBox)
			i += 1

		return listchecks


	def allSelect (self):
		#self.checkBox_1.setCheckState(2)
		i = 1
		while i <19 :
			eval('self.checkBox_'+ str(i) + '.setCheckState(2)')
			i += 1


