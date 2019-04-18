#coding:utf-8
import maya.cmds as cc
import json
import os
import maya.mel as mm
import re
import pymel.core as pm

class k_ABC_procedure():
	def __init__(self):
		pass

	def k_getTargetInfo2(self):

		#获取需要输出abc目标的名字
		k_targetObject = '|CDMSS_ch001002MossV2_Hair_h_msAnim:allAnim|CDMSS_ch001002MossV2_Hair_h_msAnim:tou_new'
		#取得abc文件路径名
		k_sn = cc.file(q=1, sn=1)
		scenesPath=os.path.split(k_sn)[0]
		#ABC文件路径
		ABCfile = r'E:\work\Themes\ABC\master\CDMSS_ch001002MossV2_Hair_h_msAnim_tou_new.abc'
		#大组名称
		topGroupName = 'CDMSS_ch001002MossV2_Hair_h_msAnim:allAnim'


		#获取需要输出abc目标的名字
		# 		# k_targetObject2 = '|CDBWG_ch004001XiShi_h_ms_anim1:allAnim|CDBWG_ch004001XiShi_h_ms_anim1:Geo'
		# 		# #取得abc文件路径名
		# 		# k_sn = cc.file(q=1, sn=1)
		# 		# scenesPath2=os.path.split(k_sn)[0]
		# 		# #ABC文件路径
		# 		# ABCfile2 = r'E:\work\Themes\ABC\master\CDBWG_ch004001XiShi_h_ms_anim1_Geo.abc'
		# 		# #大组名称
		# 		# topGroupName2 = 'CDBWG_ch004001XiShi_h_ms_anim1:allAnim'
		# 		#
		# 		# kresult=[{'targetObject':k_targetObject,'scenesPath':scenesPath,\
		# 		# 		 'ABCfile':ABCfile,'topGroupName':topGroupName}, \
		# 		# 		 {'targetObject': k_targetObject2, 'scenesPath': scenesPath2, \
		# 		# 		  'ABCfile': ABCfile2, 'topGroupName': topGroupName2}\
		# 		# 		 ]

		kresult = [{'targetObject': k_targetObject, 'scenesPath': scenesPath, \
							 'ABCfile':ABCfile,'topGroupName':topGroupName}, \
						 ]

		return (kresult)

	def k_getTargetInfo3(self):

		# 获取需要输出abc目标的名字
		k_targetObject = '|CDBWG_ch004001XiShi_h_ms_anim1:allAnim|CDBWG_ch004001XiShi_h_ms_anim1:Geo'
		#取得abc文件路径名
		k_sn = cc.file(q=1, sn=1)
		scenesPath=os.path.split(k_sn)[0]
		#ABC文件路径
		ABCfile = r'E:\work\Themes\ABC\master\CDBWG_ch004001XiShi_h_ms_anim1_Geo.abc'
		#大组名称
		topGroupName = 'CDBWG_ch004001XiShi_h_ms_anim1:allAnim'


		kresult = [{'targetObject': k_targetObject, 'scenesPath': scenesPath, \
							 'ABCfile':ABCfile,'topGroupName':topGroupName}, \
						 ]

		return (kresult)

	def k_getatomInfo(self):
		kresult=[{'groupname':'|CDBWG_ch004001XiShi_h_ms_anim1:allAnim|CDBWG_ch004001XiShi_h_ms_anim1:master',\
				  'atomfile':"E:/work/Themes/ABC/master/ttt.atom"}]

		return (kresult)

	def k_getTargetInfo(self,mode='GeoGroup'):
		kresult=[]
		DHgroup = '|DH'
		scenesPath = os.path.normpath(os.path.split(cc.file(q=1, sn=1))[0])
		#导出物体的名字规则
		k_re = re.compile(r'.*:\w*Geo$|.*:\w*Geometry$')
		abc_re = (r'\||:')

		if mode == 'GeoGroup':
			if cc.objExists(DHgroup):
				try:
					eachTarGroups = cc.listRelatives(DHgroup,c=1,f=1)
					#获取GEO组 list
					# eachTars_GeoGroup = [c for i in eachTarGroups for c in cc.listRelatives(i,c=1) if 'Geo' in c]
					for eachTarGroup in eachTarGroups:
						for TarGeoGroups in cc.listRelatives(eachTarGroup,c=1,f=1):
							if k_re.search(TarGeoGroups):

								TarGeoGroup = cc.ls(TarGeoGroups,sn=1)


								dictElement = {'targetObject': TarGeoGroup}
								kresult.append(dictElement)

								dictElement.update({'tarGroupName': eachTarGroup})
								dictElement.update({'targetObject_ln': TarGeoGroups})

								ABCfile = os.path.join(scenesPath,TarGeoGroup[0])
								ABCfile = ABCfile+'.abc'
								#修改ABC文件名
								TarGeoGroup_sub = re.sub(abc_re,'_',TarGeoGroup[0])
								ABCfile_sub = os.path.join(scenesPath, TarGeoGroup_sub)
								ABCfile_sub = ABCfile_sub + '.abc'

								dictElement.update({'scenesPath': scenesPath})
								dictElement.update({'ABCfile': ABCfile})
								dictElement.update({'ABCfile_sub': ABCfile_sub})

								ABCNodename = TarGeoGroup_sub + '_AlembicNode'
								dictElement.update({'ABCNodename': ABCNodename})

								# 添加reference信息
								referenceRN = cc.referenceQuery(TarGeoGroup, referenceNode=1)
								referencePath = cc.referenceQuery(referenceRN, un=1, wcn=1, filename=1)
								referenceNamespace = cc.referenceQuery(referenceRN, namespace=1)

								dictElement.update({'referenceRN': referenceRN})
								dictElement.update({'referencePath': referencePath})
								dictElement.update({'referenceNamespace': referenceNamespace})

				except Exception as e:
					print (e)
			else:
				cc.error('Cannot found animation group')


			#print kresult

			#导出数据到json
			kresult_json = json.dumps(kresult)

			k_abcjson = os.path.normpath(os.path.splitext(cc.file(q=1, sn=1))[0]+'.json')

			file = open(k_abcjson, 'w')
			file.write(kresult_json)
			file.close()

		return (kresult)

	def k_getJsonInfo(self):
		k_abcjson = os.path.normpath(os.path.splitext(cc.file(q=1, sn=1))[0] + '.json')

		TargetInfo = json.loads(open(k_abcjson).read())
		return (TargetInfo)


	def k_expABCInfo(self,startframe,endframe,targetObject,abcFilename,pyCommond=''):
		"""Maya ABC输出参数"""
		str_root = ""
		for i in targetObject:
			str_root += " -root {0}".format(i)

		k_jobArgs = "-frameRange " \
						 + str(startframe) \
						 + " " \
						 + str(endframe) \
						 + " -uv -wfg -ro -wv -attr k_centerpivot -ws -pythonPerFrameCallback "\
						 + str(pyCommond)\
						 + str(str_root) \
						 + " -file " + str(abcFilename)

		cc.AbcExport(verbose=1,j=k_jobArgs)


	def k_pythonPerFrameCallbackCmd(self,targetObject):
		kcmd ="\"import maya.cmds as cc\\n" \
			  "for i in {0}:\\n" \
			  "    if cc.objExists(i+'.k_centerpivot'):\\n" \
			  "        cc.xform(i, cpc=1)\\n" \
			  "        kpivot = cc.xform(i, q=1, ws=1, rotatePivot=1)\\n" \
			  "        cc.setAttr(i+'.k_centerpivotX', kpivot[0])\\n" \
			  "        cc.setAttr(i+'.k_centerpivotY', kpivot[1])\\n" \
			  "        cc.setAttr(i+'.k_centerpivotZ', kpivot[2])\\n" \
			  "        cc.setKeyframe(i+'.k_centerpivot')\\n\"".format(targetObject)
		return (kcmd)

	def excuteExpABC(self,kargs):
		"""执行输出ABC  #k_centerpivot为写死的属性名 需要导出 两个版本的参考时加入此属性"""
		targetObject = kargs['targetObject']

		abcPath = kargs['ABCfile_sub']
		# 返回动画条的帧数范围
		startFrame = cc.playbackOptions(q=True, minTime=True)
		endFrame = cc.playbackOptions(q=True, maxTime=True)

		#在GEO组下创建记录空间位置的属性
		# try:
		# 	cc.getAttr(targetObject + '.k_centerpivot')
		# except:
		# 	cc.addAttr(targetObject, ln="k_centerpivot", at='double3')
		# 	cc.addAttr(targetObject, ln="k_centerpivotX", at='double', p='k_centerpivot')
		# 	cc.addAttr(targetObject, ln="k_centerpivotY", at='double', p='k_centerpivot')
		# 	cc.addAttr(targetObject, ln="k_centerpivotZ", at='double', p='k_centerpivot')

		self.k_expABCInfo(startFrame,endFrame,targetObject,abcPath,self.k_pythonPerFrameCallbackCmd(targetObject))

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
				rep_unresolveRef=unresolveRef.replace('ms_anim','ms_render')
				cc.file(rep_unresolveRef, loadReference=RNRef)

	def excuteImpABC(self, kargs):
		"""导入ABC缓存"""
		ABCfile = kargs['ABCfile_sub']
		ABCNodename = kargs['ABCNodename']

		if cc.objExists('k_tempGroup'):
			cc.delete('k_tempGroup')
			cc.createNode('transform', n='k_tempGroup')
		else:
			cc.createNode('transform', n='k_tempGroup')

		if cc.objExists(ABCNodename):
			cc.delete(ABCNodename)

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
		topGroupName = kargs['tarGroupName']

		#ABCNodename = os.path.splitext(os.path.basename(ABCfile))[0] + '_AlembicNode'
		ABCNodename = kargs['ABCNodename']

		list_abcShapes = cc.listConnections(ABCNodename, s=0, sh=1, type='mesh')

		if list_abcShapes:
			for abcShape in list_abcShapes:
				singleAbcShapeConnect = cc.listConnections(abcShape, d=0, sh=1, c=1, p=1)

				# abcshape改成meshshape的名字
				kcode = re.compile("^k_tempGroup\|\S*")
				if not kcode.search(singleAbcShapeConnect[0]):
					raise Exception("had not match ParentGroup!")
				connectShape = kcode.search(singleAbcShapeConnect[0]).group()

				ConnectShape = re.sub("^k_tempGroup", topGroupName, connectShape)

				# abc缓存与mesh连接
				try:
					cc.connectAttr(singleAbcShapeConnect[1], ConnectShape, f=1)
				except Exception as e:
					print (e)

		list_abcTranform = cc.listConnections(ABCNodename, s=0, sh=1, scn=1, type='transform')
		if list_abcTranform:
			list_abcTranform = list(set(list_abcTranform))

			for abcTranform in list_abcTranform:
				singleAbcTranformConnect = cc.listConnections(abcTranform, d=0, sh=1, c=1, scn=1, p=1)

				for i in range(len(singleAbcTranformConnect)):
					if i % 2 == 1:
						kcode = re.compile("^k_tempGroup\|\S*")
						if not kcode.search(singleAbcTranformConnect[i - 1]):
							raise Exception("had not match TopGroup!")
						connectShape = kcode.search(singleAbcTranformConnect[i- 1]).group()

						ConnectShape = re.sub("^k_tempGroup", topGroupName, connectShape)

						try:
							cc.connectAttr(singleAbcTranformConnect[i], ConnectShape, f=1)
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
		kargs = self.k_getJsonInfo()
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

	def Hide_NoPrimaryVisiblility(self):
		allMesh = pm.ls(type='mesh', ni=1)
		NoPrimaryVisiblilitys = [a for a in allMesh if not a.primaryVisibility.get()]

		for i in NoPrimaryVisiblilitys:
			#i.visibility.set(0)
			NoPrimaryVisiblilitysTramform = pm.listRelatives(i,allParents=1)
			NoPrimaryVisiblilitysTramform[0].visibility.set(0)




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




