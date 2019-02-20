#!/usr/bin/python

# -*- coding: utf-8 -*- 
###================ animation Module Scan Script =======================
import maya.cmds as mc
import maya.mel as mm
import os,re,sys,shutil


def OCT_AllChecks():
	#检查工具格式书写要求
	# 0.检查的函数名称，1.显示在界面上checkBox的名称，2.修改的函数名称，3.自动修正按钮名称，4.可自动修改开关，5.提示标注
	#注：检查工具函数书写要求为检查后如果没有错误则返回空值，否则则返回错误信息,第4项如果可以自动修改的程序则为值1如果只能提供选择
	#等辅助操作而不能进行自动修正时则为0。"Public"的模块不会显示在面板的模块选择栏内，"Public"模块为公用检查函数，即所有模块都会
	#显示并检查"Public"下面的所有选项内容。
	# <== 0 ==>   <==== 1 ====>   <== 2 ==>  <=== 3 ==> <4> <======= 5 =======>
	#[['scanCmd','checkBoxLabel','SolveCmd','SolveLabel',1,'Script instructions'],[],[]....]
	# 0:scan Script command
	# 1:checkBox Label
	# 2:Solve Command
	# 3:Solve Label (Solve Or Select Or Delete)
	# 4:<0> Is Select <1> Solve
	# 5:Script Instructions
    return[
    ['Public',
        ['era_NameSpace(0)',     '名字空间',         'era_NameSpace(1)',        '修正',1,'检查场景中存在的错误名称空间']],
    ['Mod',
        ['erm_DeleteCamera(0)',    'camera',        'erm_DeleteCamera(1)',     '删除',1,'删除多余的摄像机'],
        ['erm_DeleteLight(0)',     '灯光',           'erm_DeleteLight(1)',      '删除',1,'删除灯光'],
        #['erm_TextTuresPath(0)',   '贴图路径',        'erm_TextTuresPath(1)',    '修正',1,'检查贴图的相对路径'],
       	['erm_fileTextures(0)',     '贴图',        	'erm_fileTextures(1)',      '修正/选择/删除',1,'检查贴图格式、路劲、名称等（格式没有修改，路径修改，选择名称错,删除多余）'],     	
        ['erm_Joint(0)',           '骨骼',            'erm_Joint(1)',            '选择',0,'检查是否有骨骼'],
        ['erm_HideObj(0)',         '隐藏物体',         'erm_HideObj(1)',          '选择',0,'检查隐藏的物体'],
        #['erm_fileName(0)',       'file节点及贴图名称','erm_fileName(1)',         '选择',0,'检查file节点及贴图名称只能以字母开头'],
        #['erm_FreezeAttribute(0)', '冻结每个物体',     'erm_FreezeAttribute(1)',  '修正',1,'冻结每个物体(freeze)'],
        ['erm_emptyGroup(0)',      '空组',            'erm_emptyGroup(1)',       '选择',0,'检查是否有空组'],
        ['erm_Intermediate(0)',    'intermediate',    'erm_Intermediate(1)',     '选择',0,'检查Intermediate物体'],
        ['erm_displayLayer(0)',    'displayLayer',    'erm_displayLayer(1)',     '删除',1,'检查是否有多余的层'],
        ['erm_animLayer(0)',       'animLayer',       'erm_animLayer(1)',        '删除',1,'检查是动画层'],
        ['erm_animCurve(0)',       '动画',       	  'erm_animCurve(1)',        '删除',1,'检查是动画节点'],
        ['erm_repeatName(0)',      '重名物体',         'erm_repeatName(1)',       '选择',0,'检查是否有重名物体'],
        ['erm_Histroy(0)',         '历史',             'erm_Histroy(1)',          '选择',0,'检查历史'],
        ['erm_shadingGroup()',     'shadingGroup',     '',                        '',0,'检查每个模型都连接ShadingGroup节点'],
        ['erm_references(0)',      '参考节点',          'erm_references(1)',       '',1,'检查有无参考节点'],
        #['erm_unTexture(0)',       '无用的贴图',        'erm_unTexture(1)',        '删除',1,'检查无用的贴图'],
        ['overrideEnabled(0)',     'Enanle Override',  'overrideEnabled(1)',      '修改',1,'检查Enanle Override是否激活'],
        ['erm_checkHair(0)',       '毛发',              'erm_checkHair(1)',        '选择',0,'检查毛发节点'],
        ['erm_checkDeformers(0)',  '变形器',            'erm_checkDeformers(1)',   '删除',1,'检查变形器'],
        ['erm_unQuickSelect(0)',   '快速选择集',         'erm_unQuickSelect(1)',    '删除',1,'检查快速选择集'],
        ['erm_emptyObj(0)',         '空物体',            'erm_emptyObj(1)',          '选择',0,'检查空物体']],
    ['Rig',
        ],
    ['Animation',
        ['era_CameraView(0)',    'cameraView',     'era_CameraView(1)',    '删除',1,'删除场景中存在的cameraView节点'],
        ['era_UnIntKeys(0)',     '整数帧',          'era_UnIntKeys(1)',     '修正',1,'将场景中的非整数动画帧调整为整数帧'],
        #['era_NameSpace(0)',     '名字空间',         '',                   ''    ,0,'检查场景中存在的错误名称空间'],
        ['era_noRefCams()',      '摄影机',          '',                    ''    ,0,'删除非参考摄影机，一切摄影机都应该引用参考文件'],
        ['era_ListAllLights(0)', '灯光',            'era_ListAllLights(1)', '删除',1,'检查场景中灯光,动画场景中不允许存在任何灯光'],
        ['era_PlaybackOption()', '时间线',          '',                    '',    0,'检查时间线上两端设置是否一致'],
        ['era_DisplayLays(0)',   'Display层',      'era_DisplayLays(1)',   '删除' ,1,'检查除ani_Layer外的所有层'],
        ['era_FileExt()',        '文件后缀',        '',                    '',    0,'检查文件格式是否为mb，是否已保存文件'],
        ['era_FileModify()',     '文件查新',        '',                    '',    0,'检查当前文件是否为保存的最新文件，是否更改'],
        ['era_TopGroups(0)',     '顶级组',          'era_TopGroups(1)',     '修正',1,'查看顶级组数量及顶级组名称'],
        ['era_EmptyAniCurves(0)','动画曲线',        'era_EmptyAniCurves(1)','删除',1,'检查场景中非引用参考的无链接动画曲线'],
        ['era_RenderLayers(0)',  '渲染层',          'era_RenderLayers(1)',  '删除',1,'检查多余渲染层'],
        #['era_emptyGroups(0)',  '空组',            'era_emptyGroups(1)',   '删除',1,'检查场景中空组文件'],
        ['era_CheckHUDs(0)',     'HeadsUpDisplay', 'era_CheckHUDs(1)',     '设置',1,'检查HUD显示数目'],
        ['era_ImagePlanes(0)',   'ImagePlane',     'era_ImagePlanes(1)',   '删除',1,'检查非引用参考文件的ImagePlane(摄影机贴图)文件'],
        ['era_HideMesh(0)',      '隐藏物体',        'era_HideMesh(1)',      '选择',0,'检查非引用参考的隐藏Mesh物体'],
        ['era_RefPath()',        '参考路径',        '',                    '',    0,'检查参考路径是否正确'],
        ['era_FileFormat()',     '文件格式',        '',                    '',    0,'检查保存的文件格式是否符合要求'],
        ['era_ScenePanel(0)',    '多余面板',        'era_ScenePanel(1)',    '清除',1,'检查场景中除主面板外所有其他面板']],
    ['Light',
        ],
    ['Effect',
        ],
        ]
def er_Mods():
    return [m[0] for m in OCT_AllChecks()][1:]
def er_TypeChecks(selMod = 'Animation'):
    if selMod in er_Mods():
        return OCT_AllChecks()[0][1:]+([ers[1:] for ers in OCT_AllChecks() if ers[0] == selMod][0])
###************************************************************###
###****************** Public Error Checks *********************###
###****************** Public Error Checks *********************###
###****************** Public Error Checks *********************###
###************************************************************###

###************************************************************###
###****************** Model Error Checks **********************###
###****************** Model Error Checks **********************###
###****************** Model Error Checks **********************###
###************************************************************###

###*************************delete camera**********************###
def erm_DeleteCamera(delCamera=0):
	erm_cam = list(set(mc.ls(mc.listCameras(),v = True)) - set(['front','persp','side','top']))
	erm_ReturnText=''
	if delCamera:
		mc.delete(erm_cam)
	else:
		erm_ReturnText = era_SplitFlag().join(erm_cam)
	return erm_ReturnText

###************************delete light************************###
def erm_DeleteLight(delLight=0):
    lights = mc.ls(lt = True,type=['VRayLightSphereShape','VRayLightIESShape','VRayLightDomeShape','VRayLightRectShape'])
    lightTex = ''
    if lights:
    	if delLight:
    		mc.delete(lights)
    	else:
    		lightTex=era_SplitFlag().join(lights)
   	return lightTex
###***********************textures file form******************###
'''def erm_fileTextures():
	fileText=''
	fileNames=mc.ls(type='file')
	if fileNames:
		for fileName in fileNames:
			imageName=mc.getAttr(fileName+'.ftn')
			the_image=os.path.splitext(imageName)[-1]
			if the_image!='.jpg' and the_image!='.png':
				fileText+= '贴图文件格式错误->'
				fileText +=str(imageName+era_SplitFlag())
			return fileText	
###******************textures relative path********************###
def erm_TextTuresPath(filePath=0):
	fileNames=mc.ls(type='file')
	pathText=''
	fullPath=mc.workspace(expandName='sourceimages')
	if fileNames:
		for fileName in fileNames:
			imageName=mc.getAttr(fileName+'.ftn')
			if not re.match(fullPath,imageName):
				myDir=imageName.split('/')
				if myDir[0]=='sourceimages':
					continue
				if filePath:
					flag=False
					fileImage=''
					path=''	
					fileDir=''				
					for Dir in myDir:
						if Dir=='sourceimages':
							flag=True
						if flag:
							if fileImage=='':
								fileImage=Dir
							else:
								path=path+'/'+Dir
								fileImage=fileImage+'/'+Dir	
								if Dir!=myDir[len(myDir)-1]:
									fileDir=fileDir+'/'+Dir
					if not mc.file((fullPath+fileDir),q=True,exists=True):
						mc.sysFile((fullPath+fileDir),makeDir=True)
					mc.sysFile(imageName,cp=(fullPath+path))
					mc.setAttr((fileName+'.ftn'),fileImage,type="string")
				else:				
					pathText+='贴图文件为绝对路径->'
					pathText+=str(imageName+era_SplitFlag())
	return pathText				
###********************file and textures name*****************###
def erm_fileName(sel=0):
	fileNames=mc.ls(type='file')
	mc.select(d=True)
	if fileNames:
		for fileName in fileNames:
			if not re.match('[A-Za-z]\w*','%s'%fileName):
				if sel:
					mc.select(fileName,add=True)
				else:
					return 'file节点名称必须以字母开头'
			imageName=mc.getAttr(fileName+'.ftn')
			myDir=imageName.split('/')[-1]
			if not re.match('[A-Za-z]\w*','%s'%myDir):
				if sel:
					mc.select(fileName,add=True)
				else:	
					return '贴图名称必须以字母开头'	'''
					
def erm_fileTextures(sel=0):
	fileText=''
	fileNames=mc.ls(type='file')
	mc.select(d=True)
	if fileNames:
		for fileName in fileNames:
			imageName=mc.getAttr(fileName+'.ftn')
			fullPath=mc.workspace(expandName='sourceimages')	
			if sel:
				#修正贴图路径
				if not re.match(fullPath,imageName):
					myDir=imageName.split('/')
					if myDir[0]!='sourceimages':
						flag=False
						fileImage=''
						path=''	
						fileDir=''				
						for Dir in myDir:
							if Dir=='sourceimages':
								flag=True
							if flag:
								if fileImage=='':
									fileImage=Dir
								else:
									path=path+'/'+Dir
									fileImage=fileImage+'/'+Dir	
									if Dir!=myDir[len(myDir)-1]:
										fileDir=fileDir+'/'+Dir
						if not mc.file((fullPath+fileDir),q=True,exists=True):
							mc.sysFile((fullPath+fileDir),makeDir=True)
						mc.sysFile(imageName,cp=(fullPath+path))
						mc.setAttr((fileName+'.ftn'),fileImage,type="string")
				#选择名字错的贴图				
				myDirs=imageName.split('/')[-1]
				if not re.match('[A-Za-z]\w*','%s'%fileName):
					mc.select(fileName,add=True)
				if not re.match('[A-Za-z]\w*','%s'%myDirs):
					mc.select(fileName,add=True)
				#删除贴图
				shadingEngineNode=mc.listConnections(fileName,s=False)	
				if len(shadingEngineNode)==1:
					mc.delete(fileName)
			else:
				#检查贴图格式
				the_image=os.path.splitext(imageName)[-1]
				if the_image!='.jpg' and the_image!='.png' and the_image!='.JPG' and the_image!='.PNG':
					fileText+= '贴图文件格式错误->'
					fileText +=str(imageName+'\n')
				#检查贴图路径										
				if not re.match(fullPath,imageName):
					myDir=imageName.split('/')
					if myDir[0]!='sourceimages':
						fileText+='贴图文件为绝对路径->'
						fileText+=str(imageName+'\n')
				#检查贴图名称		
				myDirs=imageName.split('/')[-1]
				if not re.match('[A-Za-z]\w*','%s'%fileName):
					fileText+='file节点名称必须以字母开头->'
					fileText+=str(imageName+'\n')		
				if not re.match('[A-Za-z]\w*','%s'%myDirs):
					fileText+='贴图名称必须以字母开头->'
					fileText+=str(imageName+'\n')	
				#检查存在无用的贴图
				shadingEngineNode=mc.listConnections(fileName,s=False)	
				if len(shadingEngineNode)==1:
					fileText+='存在无用的贴图->'
					fileText+=str(fileName+'\n')	
											
	return fileText	
	#print fileText				
#erm_fileTextures(1)							
###*************************list joint************************###
def erm_Joint(sel):
	erm_joint=mc.ls(type='joint')
	if erm_joint:
		if sel:
			mc.select(erm_joint,r=True)
		else:
			return era_SplitFlag().join(erm_joint)	 	
###**********************Freeze Attribute**********************###
'''def erm_FreezeAttribute(freeze=0):
	freezeTransform=''
	allTransform=list(set(mc.ls(tr=True,type='transform'))-set(['front','persp','side','top']))
	for transform in allTransform:
		temp_t=mc.getAttr(transform+'.t')
		temp_r=mc.getAttr(transform+'.r')
		temp_s=mc.getAttr(transform+'.s')
		temp_sh=mc.getAttr(transform+'.sh')
		temp_ra=mc.getAttr(transform+'.ra')
		if temp_t[0]!=(0.0, 0.0, 0.0) or temp_r[0]!=(0.0, 0.0, 0.0) or temp_s[0]!=(1.0, 1.0, 1.0) or temp_sh[0]!=(0.0, 0.0, 0.0) or  temp_ra[0]!=(0.0, 0.0, 0.0):
			if freeze:
				mc.select(transform,add=True)
				mc.makeIdentity(apply=True,t=1,r=1,s=1,n=0)
			else:
				freezeTransform+='物体未冻结->'
				freezeTransform+=str(transform+era_SplitFlag())
	return freezeTransform	'''			
###============= Check Hide Objests ================
def erm_HideObj(selHide = 0):
	allTransform=mc.ls(iv=True,tr=True)
	returnText=[]
	mc.select(d=True)
	for v in allTransform:
		HideMesh=mc.listRelatives(v,c=True,type='mesh')
		if HideMesh:
			if selHide:
				mc.select(v,add=True)
			else:
				returnText.append(v)
	return era_SplitFlag().join(returnText)          
###******************connectctAttr shadingGroup****************###	
def erm_shadingGroup():
	allTransform=list(set(mc.ls(tr=True))-set(['front','persp','side','top']))
	SE=mc.ls(type='shadingEngine')
	wt_dsm=''
	returnText=[]
	for sform in allTransform:
		wt_dsm=''
		obj=mc.listRelatives(sform,ad=True,pa=True,type='shape')
		if obj:
			dagSM=mc.listConnections(obj[0]+'.instObjGroups',s=True,p=True)
			if dagSM==None:
				wt_dsm+='没有连接ShadingGroup节点->'
				wt_dsm+=str(sform+era_SplitFlag())
				returnText.append(wt_dsm)
	for se in SE:
		wt_sfs=''
		xt_sfs=mc.listConnections(se+'.surfaceShader',s=True,p=True)
		if xt_sfs==None:
			wt_sfs+='物体没有连接->'
			wt_sfs+=str(se+'.surfaceShader'+era_SplitFlag())
			returnText.append(wt_sfs)
	return era_SplitFlag().join(returnText)	
							
###********************Check EmptyGroup************************###
def erm_emptyGroup(sel=0):
	#start = mc.timerX()
	unused=[]
	associatedNodes=mm.eval("stringArrayRemoveDuplicates(`referenceQuery -topReference -editNodes -editCommand parent`)")
	xforms=mc.ls(transforms=True,leaf=True)
	for obj in xforms:
		fullPath=mc.ls(obj,l=True)
		if fullPath[0] not in associatedNodes:
			childrenNodes=mc.listRelatives(obj,c=True)
			if childrenNodes==None:
				if mc.objectType(obj)=='transform' and (not mc.referenceQuery(obj,inr=True)):
					conn=mc.listConnections(obj)
					if conn==None:
						unused.append(obj) 
					elif ((len(conn)==1) and (mc.objectType(conn[0])=='displayLayer')):
						unused.append(obj)
					elif (len(conn)==1) and (mc.objectType(conn[0])=='renderLayer'):
						unused.append(obj) 
	if sel:
		mc.select(d=True)
		if unused:	
			mc.select(unused,r=True)
			#totalTime = mc.timerX(startTime=start)
			#print "Total time: ", totalTime
		else:
			#totalTime = mc.timerX(startTime=start)
			#print "Total time: ", totalTime
			return unused
	else:
		#totalTime = mc.timerX(startTime=start)
		#print "Total time: ", totalTime
		return ','.join(unused)	
erm_emptyGroup(1)
###*********************Intermediate obj***********************###	
def erm_Intermediate(sel=0):
	ios=mc.ls(io=True,type=['mesh','nurbsSurface'])
	if sel:
		mc.select(ios,r=True)
	else:
		return era_SplitFlag().join(ios)	
###**********************check displayLayer********************###
def erm_displayLayer(solve=0):
	allLayers=mc.ls(type='displayLayer')
	extraLayerName=[]
	if solve:
		for layer in allLayers:
			if layer not in ['defaultLayer','mod_hide']:
				mc.delete(layer)
	else:
		for layer in allLayers:
			if layer not in ['defaultLayer','mod_hide']:
				extraLayerName.append(layer)
	return era_SplitFlag().join(extraLayerName)
###********************check animLayer*************************###		
def erm_animLayer(solve=0):
	allLayers=mc.ls(type='animLayer')
	if solve:
		if allLayers:
			mc.delete(allLayers)
	else:
		return era_SplitFlag().join(allLayers) 
###***********************check animCrve***********************###
def erm_animCurve(solve=0):
	allAnimCurves=mc.ls(type=['animCurveTL','animCurveTA','animCurveTU','animCurveTT','animLayer'])
	if solve:
		if allAnimCurves:
			mc.delete(allAnimCurves)
	else:
		return era_SplitFlag().join(allAnimCurves) 	
###*********************check repeatName***********************###
def erm_repeatName(solve=0):
	#start = mc.timerX()
	checkObjs=list(set(mc.ls(type=['transform','nurbsCurve',]))-set(mc.listCameras()))
	returnText=[]
	for checkobj in checkObjs:
		if '|' in checkobj:			
			returnText.append(checkobj)
		print len(returnText)	
	if solve:
		if returnText:
			mc.select(returnText,r=True)
			#totalTime = mc.timerX(startTime=start)
			#print "Total time: ", totalTime

		else:
			#totalTime = mc.timerX(startTime=start)
			#print "Total time: ", totalTime
			return returnText
	else:
		#totalTime = mc.timerX(startTime=start)
		#print "Total time: ", totalTime
		return ",".join(returnText)	
###**********************check history************************###
def erm_Histroy(sel=0):
	returnText=''
	fileName=mc.file(q=True,sn=True)
	nodeTypeArray=['groupId','parentConstraint','time','expression','timeToUnitConversion','shadingEngine','switch_apple']
	allObjs=mc.ls(tr=True)
	for obj in allObjs:
		getHistorys=mc.listHistory(obj,pdo=True)
		if getHistorys!=None:		
			for getHistory in getHistorys:
				nodeTypes=mc.nodeType(getHistory)
				if nodeTypes not in nodeTypeArray:
					returnText+=obj+'->'+getHistory+'\n'	
					if sel:
						mc.select(obj,add=True)		
	return returnText
###**********************check references**********************###
def erm_references(ref=0):
	referencesNode=mc.ls(type='reference')
	if referencesNode:
		if ref:
			for node in referencesNode:
				cmds.lockNode(node,lock=False )
				mc.delete(node)
		else:
			return era_SplitFlag().join(returnText)
###**********************check unTextureFile*******************###
'''def erm_unTexture(sel=0):
	allFileNode=mc.ls(type='file')
	allRefFileNode=mc.ls(rn=True,type='file')	
	notRefFileNode=list(set(allFileNode)-set(allRefFileNode))
	for noteRef in notRefFileNode:
		fileImageName=mc.getAttr(noteRef+'.fileTextureName')
		shadingEngineNode=mc.listConnections(noteRef,s=False)
		if len(shadingEngineNode)==1:
			if sel:
				mc.delete(noteRef)
			else:
				return "存在无用的贴图"'''
###**********************check overrideEnabled*****************###
def overrideEnabled(sel=0):
	allMesh=list(set(mc.ls(tr=True,type='mesh'))-set(['front','persp','side','top']))
	returnText=''
	if sel:
		for mesh in allMesh:
			overrideE=mc.getAttr(mesh+'.overrideEnabled')
			if overrideE:
				mc.setAttr((mesh+'.overrideEnabled'),0)
	else:
		for mesh in allMesh:
			overrideE=mc.getAttr(mesh+'.overrideEnabled')
			if overrideE:
				return '不能激活 Enanle Override选项'

###**********************check blendShape**********************###	
def erm_BlendShape(sel=0):
	blendShapeNode=mc.ls(type='blendShape')
	if blendShapeNode:
		if sel:
			mc.delete(blendSN)	
		else:
			return 	era_SplitFlag().join(returnText)
			
###**********************check hair****************************###
def erm_checkHair(sel=0):
	allHairs=mc.ls(type='hairSystem')
	if allHairs:
		if sel:
			for allHair in allHairs:
				p_Hair=mc.listRelatives(allHair,p=True,ap=True,pa=True)
				if p_Hair!=None:
					mc.select(p_Hair,add=True)
		else:
			return '存在毛发节点'
			
###*********************check Deformers************************###
def erm_checkDeformers(defor=0):
	returnText=[]
	allDeformers=mc.ls(type=['ffd','wrap','cluster','softMod','nonLinear','sculpt','jiggle'])
	if allDeformers:
		if defor:
			mc.delete(allDeformers)
		else:
			return era_SplitFlag().join(returnText)
	
###*********************check quick select*********************###
def erm_unQuickSelect(sel=0):
	returnText=''	
	AllQuickSelect=list(set(mc.ls(sets=True))-set(mc.ls(type='shadingEngine'))-set(['defaultLightSet','defaultObjectSet']))
	if AllQuickSelect:
		if sel:
			mc.delete(AllQuickSelect)
		else:
			returnText='存在快速选择集->'
			returnText+=str(era_SplitFlag().join(AllQuickSelect))
	return returnText	
###***********************emptry obj***************************###
def erm_emptyObj(sel=0):
	returnText=[]
	allMeshObj=mc.ls(type='mesh',noIntermediate=True,long=True)
	for MeshObj in allMeshObj:
		checkVertex=mc.polyEvaluate(MeshObj,vertex=True)
		checkFace=mc.polyEvaluate(MeshObj,f=True)
		if checkVertex<3 or checkFace==0:
			returnText.append(MeshObj)
	if sel:
		if returnText:
			mc.select(returnText,r=True)
		else:
			return returnText
	else:
		return ','.join(returnText)
		
###************************************************************###
###****************** Rigging Error Checks ********************###
###****************** Rigging Error Checks ********************###
###****************** Rigging Error Checks ********************###
###************************************************************###

###************************************************************###
###******************Animation Error Checks********************###
###******************Animation Error Checks********************###
###******************Animation Error Checks********************###
###************************************************************###
def era_SplitFlag():
    return ' , '
###=============   cameraView   ===============================
def era_CameraView(cameraViewDel = 0):
    era_CameraViews = mc.ls(type = 'cameraView')
    era_ReturnText = ''
    if cameraViewDel:
        mc.delete(era_CameraViews)
    else:
        era_ReturnText = era_SplitFlag().join(era_CameraViews)
    return era_ReturnText
###=============   unInteger Keys   ===============================
def era_UnIntKeys(integer = 0): 
    import re
    retTx = ''
    re_objs = []
    objs = mc.ls(tr = True,v = True,ut = True)
    for obj in objs:
        i = 0
        keys = mc.keyframe(obj,q = True,timeChange = True)
        if keys:
            for key in keys:
                if not re.match('^[-0-9]+.[0]*$','%s'%key):
                    retTx += obj + era_SplitFlag()
                    re_objs.append(obj)
                    break
    if re_objs and integer:
        mc.snapKey(re_objs)
    else:
        return retTx
###=============   List Name Space ================
def era_NameSpace(delNameSpace = 0):
    nameSpaces = list(set(mc.namespaceInfo(lon = True,r = True,sn = True)) - set(['UI','shared']) - set([mc.referenceQuery(r,ns = True,shn = True) for r in mc.ls(rf = True)]))
    print nameSpaces
    if nameSpaces:
        if delNameSpace:
            num = 0
            while(True):
                ns = list(set(mc.namespaceInfo(lon = True,r = True,sn = True)) - set(['UI','shared']) - set([mc.referenceQuery(r,ns = True,shn = True) for r in mc.ls(rf = True)]))
                if not ns:
                    break
                for n in ns:
                    if num > 10000:
                        return '脚本运行错误，请联系技术部人员解决。'
                    try:
                        mc.namespace( f = True,mv=[n,':'] )
                        mc.namespace( f = True,rm=n )
                    except RuntimeError:
                        num +=1
                        continue
                if num > 10000:
                    return '脚本运行错误，请联系技术部人员解决。'
        else:
            return era_SplitFlag().join(nameSpaces)
###=============   List No Reference Cameras ================
def era_noRefCams():
    camText = ''
    cams = list(set(mc.ls(mc.listCameras(),v = True)) - set(['front','persp','side','top']))
    if cams:
        return str(era_SplitFlag().join(cams))
###=============  List All Lights ================
def era_ListAllLights(delLight = 0):
    lights = mc.ls(lt = True)
    lightTex = ''
    if lights:
        for light in lights:
            if not mc.referenceQuery(light,inr = True):
                if delLight:
                    mc.delete(light)
                else:
                    lightTex += light + era_SplitFlag()
    return lightTex
###=============  PlaybackOption ================
def era_PlaybackOption():
    min = mc.playbackOptions(q = True,min = True)
    max = mc.playbackOptions(q = True,max = True)
    ast = mc.playbackOptions(q = True,ast = True)
    aet = mc.playbackOptions(q = True,aet = True)
    if min != ast or max != aet:
        return '时间滑块设置不一致。'
###============= Check DisplayLayers ================
def era_DisplayLays(delLays = 0):
    disPlayLays = mc.ls(type = 'displayLayer')
    lays = ''
    for disPlayLay in disPlayLays:
        if not re.match('\w+:defaultLayer|ani_Layer|ani_TX|defaultLayer|\w+:\w+',disPlayLay):
            if delLays:
                mc.delete(disPlayLay)
            else:
                lays += disPlayLay + era_SplitFlag()
    return lays
###============= Check File Format ================            
def era_FileExt():
    fileFormat = mc.file(q = True,sn = True)
    if fileFormat:
        if os.path.splitext(fileFormat)[1][1:] != 'mb':
            return '文件后缀格式不正确。'
    else:
        return '文件未保存。'
###============= File anyModified ================
def era_FileModify():
    if mc.file(q = True,sn = True) and os.path.isfile(mc.file(q = True,sn = True)):
        if mc.file(q = True,amf = True):
            return '文件在保存后有更改，请重新保存文件。'
    else:
        return '文件未保存或文件不存在，请重新保存文件。'
###============= Check TopGroup ================
def era_TopGroups(modifyGroups = 0):
    topGroupTex = ''
    allGroups = mc.ls(assemblies = True)
    allCams = mc.listRelatives(mc.ls(ca = True),p = True)
    tops = list(set(allGroups)-set(allCams))
    if not tops:
        return '场景无物体，请确认场景正确后检查！'
    topGroups = [g for g in tops if not mc.listRelatives(g,c = True,s = True)]
    if len(tops) != 1:
        if not 'DH' in topGroups:
            if modifyGroups:
                mc.group(tops,n = 'DH')
                mc.select(cl = True)
            else:
                topGroupTex += '顶级组数量错误且没有DH顶级组。-> '
                topGroupTex += str(era_SplitFlag().join(tops))
        else:
            if modifyGroups:
                tops.remove('DH')
                mc.parent(tops,'DH')
                mc.select(cl = True)
            else:
                tops.remove('DH')
                topGroupTex += '存在多余顶级组。-> '
                topGroupTex += str(era_SplitFlag().join(tops))
    else:
        if not mc.listRelatives(tops[0],c = True,s = True):
            if tops[0] != 'DH':
                if modifyGroups:
                    mc.rename(tops[0],'DH')
                    mc.select(cl = True)
                else:
                    topGroupTex += '顶级组名称错误。-> '
                    topGroupTex += str(era_SplitFlag().join(tops))
        else:
            if modifyGroups:
                mc.group(tops,n = 'DH')
                mc.select(cl = True)
            else:
                topGroupTex += '顶级组不能是物体。-> '
                topGroupTex += str(era_SplitFlag().join(tops))
    return topGroupTex
###============= Check Empty Animation Curves ================
def era_EmptyAniCurves(delAniCurves = 0):
    emptyAniCurvesTex = ''
    aniCurves = mc.ls(type = ['animCurveTU','animCurveTA','animCurveTL','animCurveUL'])
    for aniCurve in aniCurves:
        if not mc.referenceQuery(aniCurve,inr = True) and not mc.listConnections(aniCurve,c = True):
            if delAniCurves:
                mc.delete(aniCurve)
            else:
                emptyAniCurvesTex += aniCurve + era_SplitFlag()
    return emptyAniCurvesTex
###============= Check RenderLayers ================
def era_RenderLayers(delRenderLay = 0):
    renderLayers = mc.ls(type = 'renderLayer')
    renLayerTex = ''
    for renderLayer in renderLayers:
        if not re.match('\w+:defaultRenderLayer|defaultRenderLayer|\w+:\w+',renderLayer):
            print renderLayer
            print delRenderLay
            if delRenderLay:
                mc.delete(renderLayer)
            else:
                renLayerTex += renderLayer + era_SplitFlag()
    return renLayerTex
'''
###============= Check Empty Group ================
def era_emptyGroups(delEmptyGroup = 0):
    trans = mc.ls(tr = True,type = 'transform',g = True)
    if 'Hips_parentConstraint1' in trans:
        print 'ddd'
    topGrps = mc.ls(assemblies = True)
    emptyTex = ''
    for tran in trans:
        if not mc.referenceQuery(tran,inr = True) and not mc.listRelatives(tran,c = True):
            if not tran in topGrps and tran != 'DH':
                if delEmptyGroup:
                    mc.delete(tran)
                else:
                    emptyTex += tran + era_SplitFlag()
    return emptyTex
'''
###============= Check HUD ================
def era_CheckHUDs(unDis = 0):
    '''disHUDs = ['HUDCameraNames','HUDHQCameraNames','HUDFrameRate','HUDCurrentFrame','HUDIKSolverState',
               #'HUDCurrentCharacter','HUDPlaybackSpeed','HUDFocalLength','HUDSceneTimecode','HUDViewAxis']
    dis = [i for i in mc.headsUpDisplay(q = True,lh = True) if mc.headsUpDisplay(i,q = True,vis = True) and not i in disHUDs]
    noDis = [i for i in disHUDs if not mc.headsUpDisplay(i,q = True,vis = True)]
    if dis or noDis:
        if UnDis:
            for d in dis:
                mc.headsUpDisplay(d,e = True,vis = False)
            for n in noDis:
                mc.headsUpDisplay(n,e = True,vis = True)
        else:
            return era_SplitFlag().join(dis) + era_SplitFlag().join(noDis)'''
    era_Huds = [i for i in mc.headsUpDisplay(q = True,lh = True) if mc.headsUpDisplay(i,q = True,vis = True)]
    if era_Huds:
        if unDis:
            for era_Hud in era_Huds:
                mc.headsUpDisplay(era_Hud,e = True,vis = False)
        else:
            return era_SplitFlag().join(era_Huds)
###============= Check ImagePlanes ================
def era_ImagePlanes(delIP = 0):
    ipTex = ''
    ips = mc.ls(type = 'imagePlane')
    for ip in ips:
        if not mc.referenceQuery(ip,inr = True):
            if delIP:
                mc.delete(ip)
            else:
                ipTex += ip + era_SplitFlag()
    return ipTex
###============= Check Hide Mesh Objests ================
def era_HideMesh(selHid = 0):
    allHideMesh = [v for v in mc.ls(iv = True,tr = True) if not mc.referenceQuery(v,inr = True) and mc.listRelatives(v,c = True,type = 'mesh')]
    if allHideMesh:
        if selHid:
            mc.select(allHideMesh,r = True)
        else:
            return era_SplitFlag().join(allHideMesh)
###============= Check Reference Path ================
def era_RefPath():
    rePathTex = ''
    paths = mc.file(q = True,r = True)
    for path in paths:
        if path[:2] == 'O:' or path[:2] == 'o:':
            continue
        else:
            rePathTex += path + era_SplitFlag()
    return rePathTex
###============= Check File Format ================
def era_FileFormat():
    fileName = os.path.basename(mc.file(q = True,sn = True))
    if fileName:
        if not (re.match('^an_sc\d{3}_\d{3}\.mb$',fileName) or re.match('^an_sc\d+_\d+\_\d+.mb$',fileName)):
            return '所保存文件格式不对，请更正格式后重新检查。'
    else:
        return '文件未保存，请先按指定格式保存文件后再检查。'
###============= Check Other Panels ================
def era_ScenePanel(delPanel = 0):
    defaultPanel = 'modelPanel4'
    currentPanel = mc.getPanel(wf = True)
    panels = mc.getPanel(vis = True)
    if 'scriptEditorPanel1' in panels:
        panels.remove('scriptEditorPanel1')
    if panels != [defaultPanel]:
        if delPanel:
            if defaultPanel in panels:
                panels.remove(defaultPanel)
                mc.deleteUI(panels)
            else:
                if not len(panels)==1:
                    mc.deleteUI(panels[1:])
                mc.panel(defaultPanel,e = True,rp = panels[0])
        else:
            return era_SplitFlag().join(panels)
            
###************************************************************###
###****************** Error Checks Window *********************###
###****************** Error Checks Window *********************###
###****************** Error Checks Window *********************###
###************************************************************###
###============== changeMods ======================
def er_changeMods():
    changeModule = mc.optionMenu('Er_Mods_OM',q = True,v = True)
    er_MIs(slmod = changeModule)
    mc.scrollField('er_ErrorInfos_SF', e =True,text='' )
    mc.button('erSolveAll_Button',e = True,en = False)

def er_checkBoxSel(status = 0):
    print 'rrrr'
    currentMod = mc.optionMenu('Er_Mods_OM',q = True,v = True)
    rowlays = mc.scrollLayout('Er_CheckSL',q = True,ca = True)
    ern = 0
    for rowlay in rowlays:
        if not status == 2:
            mc.checkBox('%s_checkBox'%rowlay,e = True,v = status)
        elif status == 2:
            if mc.iconTextButton('%s_icon'%rowlay,q = True, image1=True) == 'check_Wrong.png':
                mc.checkBox('%s_checkBox'%rowlay,e = True,v = 1)
            else:
                mc.checkBox('%s_checkBox'%rowlay,e = True,v = 0)
        ern += 1

###============== Check List Buttons ======================
def er_MIs(slmod = 'Animation'):
    bs = mc.scrollLayout('Er_CheckSL',q = True,ca = True)
    if bs:
        mc.deleteUI(bs)
    #slmod = mc.optionMenu('yy_Er_Mods_OM',q = True,v = True)
    num = 0
    er_Checks = er_TypeChecks(slmod)
    if er_Checks:
        for er_Check in er_Checks:
            er_LayoutLabel = er_Check[0].split('(')[0]
            mc.rowLayout(er_LayoutLabel,p = 'Er_CheckSL',h = 30,nc = 4,cw4 = [50,80,200,100],co4 = [0,10,20,20],cl4 = ['right','center','center','center'],ct4 = ['right','both','both','both'])
            mc.iconTextButton('%s_icon'%er_LayoutLabel,style='iconOnly', image1='check_Right.png', vis = False,label='')
            if er_Check[2] and er_Check[3]:
                mc.button('%s_solve'%er_LayoutLabel,en = False,w = 50,vis = True,l = er_Check[3],c = 'er_Solves(solName = [%s])'%er_Check)
            else:
                mc.button('%s_solve'%er_LayoutLabel,en = False,w = 50,vis = False,l = '')
            mc.checkBox('%s_checkBox'%er_LayoutLabel,l = er_Check[1],ann = er_Check[5],v = 1)
            mc.button('%s_checkButton'%er_LayoutLabel,w = 50, l = '检查', c = 'er_CheckCmd(checkName =[%s])'%er_Check)
            print er_Check
            mc.setParent('..')
###============== Check Cmds ======================
def er_CheckCmd(checkName =[]):
    che_mod = mc.optionMenu('Er_Mods_OM',q = True,v = True)
    #mc.button('erSolveAll_Button',e = True,en = False)
    if checkName:
        checkList = checkName
        mc.checkBox('%s_checkBox'%checkName[0][0].split('(')[0],e = True,v = 1)
    else:
        checkList = er_TypeChecks(selMod = che_mod)
    er_Info = ''
    if checkList:
        mc.button('er_OnlySelErrorButton',e = True,en = True)
    else:
        return
        
    for checkCmd in checkList:
        checkLab = checkCmd[0].split('(')[0]
        er_Teturn = ''
        #mc.iconTextButton('%s_icon'%checkLab,e = True,vis = False)
        #mc.button('%s_solve'%checkLab,e = True,en = False)
        if checkCmd[0]:
            if mc.checkBox('%s_checkBox'%checkLab,q = True,v = True):
                try:
                    exec('er_Teturn = %s'%checkCmd[0])
                except RuntimeError:
                    mc.scrollField('er_ErrorInfos_SF', e = True, text='警告：%s 检查程序在运行时出现错误，请及时联系技术人员解决。'%str(checkLab))
                    continue
                if er_Teturn:
                    er_Info += '============ < %s > 错误信息: ===========\n>>> %s\n'%(checkCmd[1],str(er_Teturn))
                    mc.iconTextButton('%s_icon'%checkLab,e = True, image1='check_Wrong.png', vis = True)
                    mc.button('%s_solve'%checkLab,e = True,en = True)
                    if checkCmd[4]:
                        mc.button('erSolveAll_Button',e = True,en = True)
                else:
                    mc.iconTextButton('%s_icon'%checkLab,e = True, image1='check_Right.png', vis = True)
            else:
                mc.iconTextButton('%s_icon'%checkLab,e = True,vis = False)
    mc.scrollField('er_ErrorInfos_SF', e = True, text=er_Info )
    
    
###============== Solves ======================    
def er_Solves(solName = []):
    sol_Mod = mc.optionMenu('Er_Mods_OM',q = True,v = True)
    sol_checkAll = []
    allSolves = [sol for sol in er_TypeChecks(selMod = sol_Mod) if sol[2] and sol[4]]
    if solName:
        sol_checkAll = solName
    else:
        sol_checkAll = allSolves
    #print 'te'
    for sol_solveCmd in sol_checkAll:
        solLayoutName = sol_solveCmd[0].split('(')[0]
        sol_Icon = mc.iconTextButton('%s_icon'%solLayoutName,q = True, image1=True)
        sol_checkBox = mc.checkBox('%s_checkBox'%solLayoutName,q = True,v = True)
        sol_solveButton = mc.button('%s_solve'%solLayoutName,q = True,en = True)
        #print sol_Icon,'***\n****',sol_solveButton,'***\n****',sol_checkBox,'***\n****'
        if (sol_Icon == 'check_Wrong.png' and sol_solveButton and sol_checkBox):
            print sol_solveCmd
            try:
                exec('er_Solvetu = %s'%sol_solveCmd[2])
                mc.iconTextButton('%s_icon'%solLayoutName,e = True, image1='check_Right.png')
                mc.button('%s_solve'%solLayoutName,e = True,en = False)
            except RuntimeError:
                mc.scrollField('er_ErrorInfos_SF', e = True, text='警告：%s 检查程序在运行时出现错误，请及时联系技术人员解决。'%str(solLayoutName))
                continue



def er_window(selMo = 'animation'):
    er_winName = 'checkError_Window'
    wh = [500,740]
    if(mc.window(er_winName,q = True,ex = True)):
        mc.deleteUI(er_winName)
    mc.window(er_winName,wh = wh,t = '文件检查窗口',mb = True,s = True)
    mc.menu(l = '帮助')
    mc.menuItem(l = '使用帮助')
    mc.menuItem(l = '关于软件',c = '')
    mc.columnLayout('er_WinColumnLayout',w = wh[0],cat = ['both',10],rs = 10,adj = True)
    #mc.text(l = '文件提交检查工具')
    mc.image(i = '/check01.jpg')
    mc.separator()
    mc.optionMenu('Er_Mods_OM',l='模块：   ',cc ='er_changeMods()')
    for mod in er_Mods():
        mc.menuItem(p = 'Er_Mods_OM',l= mod)
    #if selMo in er_Mods():
        #mc.optionMenu('yy_Er_Mods_OM',e = True,v = selMo)
    #mc.optionMenu('yy_Er_Mods_OM',e = True,v = erMod)
    mc.scrollLayout('Er_CheckSL',p = 'er_WinColumnLayout',w = wh[0]-30,h = wh[1]/3)
    mc.setParent('..')
    cw = wh[0]/4 -7
    mc.rowLayout(w = wh[0],nc = 4,cw4 = [cw,cw,cw,cw],co4 = [10,10,10,10],cl4 = ['center','center','center','center'],ct4 = ['both','both','both','both'])
    mc.button(w = 80,h = 28,l = '选择全部',c = 'er_checkBoxSel(1)')
    mc.button(w = 80,h = 28,l = '去除全部',c = 'er_checkBoxSel(0)')
    mc.button('er_OnlySelErrorButton',w = 80,h = 28,l = '只选错误项',en = False,c = 'er_checkBoxSel(2)')
    mc.button('erSolveAll_Button',w = 80,h = 28,l = '修正所有',en = False, c = 'er_Solves()')
    mc.setParent('..')
    mc.button(p = 'er_WinColumnLayout',h = 50,l = '开始检查',c = 'er_CheckCmd()')
    mc.separator(p = 'er_WinColumnLayout',st ='in')
    mc.text(p = 'er_WinColumnLayout',l = '错误信息')
    mc.scrollField('er_ErrorInfos_SF',p = 'er_WinColumnLayout', ed =False, wordWrap=True, text='' )
    mc.separator(p = 'er_WinColumnLayout',st = 'none')
    mc.setParent('..')
    mc.showWindow(er_winName)
    mc.window(er_winName,e = True,wh = wh)
    if er_Mods():
        er_changeMods()
er_window()