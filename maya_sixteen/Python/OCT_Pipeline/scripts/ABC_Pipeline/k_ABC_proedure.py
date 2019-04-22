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
		self.DHgroup = '|DH'
		
	def k_getTargetInfo(self,mode='Group'):
		"""获取场景信息（目标物体、组，导出类型abc、curve，参考信息），导出到当前目录下的json文件里"""
		kresult=[]
		scenesPath = os.path.normpath(os.path.split(cc.file(q=1, sn=1))[0])
		#导出物体的名字规则
		k_re_ch = re.compile(r'^\w+_ch\d+.*')
		k_re_pr = re.compile(r'^\w+_pr\d+.*')
		k_re_geo = re.compile(r'.*:\w*Geo$|.*:\w*Geometry$')
		k_re_cv = re.compile(r'.*:\w*master$')
		k_re_cache = (r'\||:')

		if mode == 'Group':
			if cc.objExists(self.DHgroup):
				try:
					eachTarGroups = cc.listRelatives(self.DHgroup,c=1,f=1)
					#获取GEO组 list
					# eachTars_GeoGroup = [c for i in eachTarGroups for c in cc.listRelatives(i,c=1) if 'Geo' in c]
					for eachTarGroup in eachTarGroups:
						#角色ch
						if k_re_ch.search(cc.ls(eachTarGroup,sn=1)[0]):
							for TarGeoGroups in cc.listRelatives(eachTarGroup,c=1,f=1):
								if k_re_geo.search(TarGeoGroups):
									TarGeoGroup = cc.ls(TarGeoGroups,sn=1)

									dictElement = {'targetObject': TarGeoGroup}
									kresult.append(dictElement)

									dictElement.update({'type': 'abc'})
									dictElement.update({'tarGroupName': eachTarGroup})
									dictElement.update({'targetObject_ln': TarGeoGroups})

									ABCfile = os.path.join(scenesPath,TarGeoGroup[0])
									ABCfile = ABCfile+'.abc'
									#修改ABC文件名
									TarGeoGroup_sub = re.sub(k_re_cache,'_',TarGeoGroup[0])
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


									referencePath_re = referencePath.replace('_anim', '_render')
									dictElement.update({'referencePath_re': referencePath_re})
									referenceNamespace_re = referenceNamespace.replace('_anim', '_render')
									dictElement.update({'referenceNamespace_re': referenceNamespace_re})

						#道具pr
						elif k_re_pr.search(cc.ls(eachTarGroup,sn=1)[0]):
							for TarCvGroups in cc.listRelatives(eachTarGroup, c=1, f=1):
								if k_re_cv.search(TarCvGroups):
									TarCvGroup = cc.ls(TarCvGroups, sn=1)

									dictElement = {'targetObject': TarCvGroup}
									kresult.append(dictElement)

									dictElement.update({'type': 'curve'})
									dictElement.update({'tarGroupName': eachTarGroup})
									dictElement.update({'targetObject_ln': TarCvGroups})

									Animfile = os.path.join(scenesPath, TarCvGroup[0])
									Animfile = Animfile + '.anim'
									# 修改anim文件名
									TarCvGroup_sub = re.sub(k_re_cache, '_', TarCvGroup[0])
									Animfile_sub = os.path.join(scenesPath, TarCvGroup_sub)
									Animfile_sub = Animfile_sub + '.anim'

									dictElement.update({'scenesPath': scenesPath})
									dictElement.update({'Animfile': Animfile})
									dictElement.update({'Animfile_sub': Animfile_sub})



									# 添加reference信息
									referenceRN = cc.referenceQuery(TarCvGroup, referenceNode=1)
									referencePath = cc.referenceQuery(referenceRN, un=1, wcn=1, filename=1)
									referenceNamespace = cc.referenceQuery(referenceRN, namespace=1)

									dictElement.update({'referenceRN': referenceRN})
									dictElement.update({'referencePath': referencePath})
									dictElement.update({'referenceNamespace': referenceNamespace})


									referencePath_re = referencePath.replace('_anim', '_render')
									dictElement.update({'referencePath_re': referencePath_re})
									referenceNamespace_re = referenceNamespace.replace('_anim', '_render')
									dictElement.update({'referenceNamespace_re': referenceNamespace_re})

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

	def k_getJsonInfo(self,mode ='fs'):
		"""获取当前路径下的json文件"""
		if mode=='fs':
			k_abcjson = os.path.normpath(os.path.splitext(cc.file(q=1, sn=1))[0] + '.json')
			k_abcjson = k_abcjson.replace('_fs_','_an_')
			print (k_abcjson)
			TargetInfo = json.loads(open(k_abcjson).read())
			return (TargetInfo)


	def k_expABCInfo(self,startframe,endframe,targetObject,abcFilename,pyCommond=''):
		"""Maya AbcExport 输出参数设置"""
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
		"""导出abc时 加入的python语句"""
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

	def excuteExpAnim(self,kargs):
		#烘焙关键帧
		animfile = kargs['Animfile_sub']
		targetObject = kargs['targetObject']

		startFrame = cc.playbackOptions(q=True, minTime=True)
		endFrame = cc.playbackOptions(q=True, maxTime=True)


		targetObject_trs = []
		targetObject_cvs = cc.ls(targetObject, dag=1, type='nurbsCurve')
		for targetObject_cv in targetObject_cvs:
			targetObject_tr = cc.listRelatives(targetObject_cv, p=1)
			targetObject_trs.append(targetObject_tr[0])

		targetObject_trs = list(set(targetObject_trs))

		cc.bakeResults(targetObject_trs, simulation=1, t=(startFrame, endFrame))
		#cc.bakeResults(targetObject, simulation=1, t=(startFrame, endFrame), hierarchy='below')

		cc.select(targetObject)

		cc.file(animfile, force=1,
				options="precision=8;intValue=17;nodeNames=1;verboseUnits=0;whichRange=1;"
						"options=keys;hierarchy=below;controlPoints=0;shapes=1;helpPictures=0;useChannelBox=1;"
						"copyKeyCmd=-animation objects -option keys -hierarchy below -controlPoints 0 -shape 1",
				type="animExport", pr=1, es=1)

	def excuteImpAnim(self,kargs):

		animfile = kargs['Animfile_sub']

		targetObject = kargs['targetObject']

		cc.select(targetObject)

		cc.file(animfile,i=1,
				options="targetTime=4;copies=1;option=replace;pictures=0;connect=0;",
				type="animImport",iv=1, mnc=0)

		cc.select(cl=1)

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

	def createReference(self,kargs):
		"""根据json信息，创建参考"""
		k_re_DH = re.compile("^\|DH\|")

		if not cc.objExists(self.DHgroup):cc.createNode('transform', n=self.DHgroup)


		referenceNamespace=kargs['referenceNamespace']
		referencePath = kargs['referencePath_re']
		tarGroupName = kargs['tarGroupName']

		tarGroupName_sub = re.sub(k_re_DH, '',tarGroupName)

		k_referenceResolved = cc.file(referencePath,r=1,type='mayaBinary',iv=1,gl=1,
							  shd=('displayLayers','shadingNetworks','renderLayersByName'),mnc=0,
							  options='v=0;',namespace=referenceNamespace)

		try:
			cc.parent(tarGroupName_sub,self.DHgroup)
		except Exception as e:
			print(e)

		return (k_referenceResolved)

	def change_referenceNamespace(self,kargs,ref):
		"""修改参考命名空间"""
		referenceNamespace = kargs['referenceNamespace']
		referenceNamespace_re = kargs['referenceNamespace_re']

		k_namespace = cc.referenceQuery(ref, namespace=1)
		if k_namespace == referenceNamespace:
			try:
				cc.file(ref,e=1,ns=referenceNamespace_re)
			except Exception as e:
				print(e)


	def k_export_cache(self):
		kargs = self.k_getTargetInfo()
		self.Hide_NoPrimaryVisiblility()
		for karg in kargs:
			if karg['type'] == 'abc':
				self.excuteExpABC(karg)
			if karg['type'] == 'curve':
				self.excuteExpAnim(karg)

	def k_import_cache(self):
		#self.changeRefer()
		kargs = self.k_getJsonInfo()
		for karg in kargs:
			k_ref = self.createReference(karg)
			if karg['type'] == 'abc':
				self.excuteImpABC(karg)
				self.connectABC(karg)
			elif karg['type'] == 'curve':
				self.excuteImpAnim(karg)
			self.change_referenceNamespace(karg,k_ref)


	def Hide_NoPrimaryVisiblility(self):
		"""隐藏 primary Visibility状态为不勾选的物体"""
		allMesh = pm.ls(type='mesh', ni=1)
		NoPrimaryVisiblilitys = [a for a in allMesh if not a.primaryVisibility.get()]

		for i in NoPrimaryVisiblilitys:
			#i.visibility.set(0)
			NoPrimaryVisiblilitysTramform = pm.listRelatives(i,p=1)
			NoPrimaryVisiblilitysTramform[0].visibility.set(0)




	def tempwin(self):
		k_class = self
		tempwindow = cc.window()
		templayout = cc.columnLayout(tempwindow, columnAttach=('both', 5), rowSpacing=10, columnWidth=250)
		c = cc.button(label=u'导出abc缓存', command="k_class=k_ABC_procedure()\nk_class.k_export_cache()")
		d = cc.button(label=u'导入abc缓存', command="k_class=k_ABC_procedure()\nk_class.k_import_cache()")

		tempshow = cc.showWindow(tempwindow)




if __name__ == "__main__":

	a=k_ABC_procedure()
	a.tempwin()



