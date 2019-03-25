#coding:utf-8
import maya.cmds as cc
import json
import os
import maya.mel as mm
import re

class k_ABC_procedure():
	def __init__(self):
		pass

	def k_getTargetInfo(self):

		#获取需要输出abc目标的名字
		k_targetObject = '|CDBWG_ch004001XiShi_h_ms_anim:allAnim|CDBWG_ch004001XiShi_h_ms_anim:Geo'
		#取得abc文件路径名
		k_sn = cc.file(q=1, sn=1)
		scenesPath=os.path.split(k_sn)[0]
		#ABC文件路径
		ABCfile = r'E:\work\Themes\ABC\master\CDBWG_ch004001XiShi_h_ms_anim_Geo.abc'
		#大组名称
		topGroupName = 'CDBWG_ch004001XiShi_h_ms_anim:allAnim'


		#获取需要输出abc目标的名字
		k_targetObject2 = '|CDBWG_ch004001XiShi_h_ms_anim1:allAnim|CDBWG_ch004001XiShi_h_ms_anim1:Geo'
		#取得abc文件路径名
		k_sn = cc.file(q=1, sn=1)
		scenesPath2=os.path.split(k_sn)[0]
		#ABC文件路径
		ABCfile2 = r'E:\work\Themes\ABC\master\CDBWG_ch004001XiShi_h_ms_anim1_Geo.abc'
		#大组名称
		topGroupName2 = 'CDBWG_ch004001XiShi_h_ms_anim1:allAnim'

		kresult=[{'targetObject':k_targetObject,'scenesPath':scenesPath,\
				 'ABCfile':ABCfile,'topGroupName':topGroupName}, \
				 {'targetObject': k_targetObject2, 'scenesPath': scenesPath2, \
				  'ABCfile': ABCfile2, 'topGroupName': topGroupName2}\
				 ]



		return (kresult)

	def k_getatomInfo(self):
		kresult=[{'groupname':'|CDBWG_ch004001XiShi_h_ms_anim1:allAnim|CDBWG_ch004001XiShi_h_ms_anim1:master',\
				  'atomfile':"E:/work/Themes/ABC/master/ttt.atom"}]

		return (kresult)

	def k_expABCInfo(self,startframe,endframe,targetObject,abcFilename,attr=''):
		"""Maya ABC输出参数"""
		k_jobArgs = "-frameRange " \
						 + str(startframe) \
						 + " " \
						 + str(endframe) \
						 + " -uvWrite -worldSpace -root " \
						 + str(targetObject) \
						 + " " \
						 + "-file" + " " + str(abcFilename)

		cc.AbcExport(verbose=1,j=k_jobArgs)

	def excuteExpABC(self,kargs):
		"""执行输出ABC"""
		targetObject = kargs['targetObject']
		scenesPath = kargs['scenesPath']

		# 返回动画条的帧数范围
		startFrame = cc.playbackOptions(q=True, minTime=True)
		endFrame = cc.playbackOptions(q=True, maxTime=True)


		k_abcFilename=targetObject.split('|')[-1]
		if ':' in k_abcFilename:
			k_abcFilename=k_abcFilename.replace(":","_")
		abcPath = os.path.join(scenesPath,k_abcFilename)
		abcPath = abcPath+'.abc'
		print abcPath
		self.k_expABCInfo(startFrame,endFrame,targetObject,abcPath)

	def changeRefer(self):
		"""换参考，将无材质带绑定的参考换成 有材质无绑定的参考"""
		reflist = cc.file(q=True, reference=1)
		for resolveRef in reflist:
			if cc.referenceQuery(resolveRef, isLoaded=1):
				print (resolveRef)
				unresolveRef = cc.referenceQuery(resolveRef, un=1, wcn=1, filename=1)
				print (unresolveRef)
				RNRef = cc.referenceQuery(resolveRef, referenceNode=1)
				print (RNRef)
				rep_unresolveRef=unresolveRef.replace('anim','render')
				cc.file(rep_unresolveRef, loadReference=RNRef)

	def excuteImpABC(self, kargs):
		"""导入ABC缓存"""
		ABCfile = kargs['ABCfile']

		if cc.objExists('k_tempGroup'):
			cc.delete('k_tempGroup')
			cc.createNode('transform', n='k_tempGroup')
		else:
			cc.createNode('transform', n='k_tempGroup')

		cc.AbcImport(ABCfile, mode='import', reparent='k_tempGroup')

	def expanim(self,kargs):
		cc.select(kargs['groupname'], r=1, hierarchy=1)
		atomfile = kargs['atomfile']

		cc.file(atomfile, force=1,\
				options="precision=8;\
				statics=1;baked=0;sdk=0;constraint=0;animLayers=0;selected=childrenToo;\
				whichRange=2;hierarchy=none;controlPoints=1;useChannelBox=2;options=keys;\
				copyKeyCmd=-animation objects \
				-option keys -hierarchy none -controlPoints 1 ", \
				type="atomExport", pr=1, es=1)


		print('export successful!')
		cc.select(cl=1)

	def impanim(self,kargs):
		cc.select(kargs['groupname'], r=1, hierarchy=1)
		atomfile = kargs['atomfile']

		melstr = 'file -import -type "atomImport"  \
	    -options "targetTime=3;option=insert;match=hierarchy;selected=childrenToo;" \
	    "%s";' % (atomfile)

		mm.eval(melstr)

		print('import successful!')



	def connectABC(self,kargs):
		"""ABC缓存连接到 有材质无绑定的mesh上（仅限mesh）"""
		ABCfile = kargs['ABCfile']
		topGroupName = kargs['topGroupName']

		# CDBWG_ch004001XiShi_h_ms_anim_Geo_AlembicNode
		ABCNodename = os.path.splitext(os.path.basename(ABCfile))[0] + '_AlembicNode'
		# print(ABCNodename)

		list_abcShapes = cc.listConnections(ABCNodename, s=0, sh=1, type='mesh')
		for abcShape in list_abcShapes:
			singleAbcShapeConnect = cc.listConnections(abcShape, d=0, sh=1, c=1, p=1)
			# print(singleAbcShapeConnect)
			# abcshape改成meshshape的名字
			kcode = re.compile("^k_tempGroup\|\S*")
			if not kcode.search(singleAbcShapeConnect[0]):
				raise Exception("had not match TopGroup!")
			connectShape = kcode.search(singleAbcShapeConnect[0]).group()

			ConnectShape = re.sub("^k_tempGroup", topGroupName, connectShape)

			# abc缓存与mesh连接
			try:
				cc.connectAttr(singleAbcShapeConnect[1], ConnectShape, f=1)
			except Exception as e:
				print (e)

		try:
			cc.delete('k_tempGroup')
		except Exception as e:
			print (e)


	def k_export_abc(self):
		kargs = self.k_getTargetInfo()
		for karg in kargs:
			self.excuteExpABC(karg)

	def k_import_abc(self):
		self.changeRefer()
		kargs = self.k_getTargetInfo()
		for karg in kargs:
			self.excuteImpABC(karg)
			self.connectABC(karg)

	def k_export_atom(self):
		kargs = self.k_getatomInfo()
		for karg in kargs:
			self.expanim(karg)

	def k_import_atom(self):
		kargs = self.k_getatomInfo()
		for karg in kargs:
			self.impanim(karg)

	def tempwin(self):
		k_class = self
		tempwindow = cc.window()
		templayout = cc.columnLayout(tempwindow, columnAttach=('both', 5), rowSpacing=10, columnWidth=250)
		a = cc.button(label=u'保存ani版本', command="k_class=k_ABC_procedure()\nk_class.k_save_ani()")
		b = cc.button(label=u'保存render版本', command="k_class=k_ABC_procedure()\nk_class.k_save_render()")
		c = cc.button(label=u'导出abc缓存', command="k_class=k_ABC_procedure()\nk_class.k_export_abc()")
		d = cc.button(label=u'导入abc缓存', command="k_class=k_ABC_procedure()\nk_class.k_import_abc()")
		e = cc.button(label=u'导出atom缓存', command="k_class=k_ABC_procedure()\nk_class.k_export_atom()")
		f = cc.button(label=u'导入atom缓存', command="k_class=k_ABC_procedure()\nk_class.k_import_atom()")
		tempshow = cc.showWindow(tempwindow)


if __name__ == "__main__":
	a=k_ABC_procedure()
	a.tempwin()

