# coding: utf-8

from __future__ import with_statement #only needed for maya 2008 & 2009

import threading
import sys, os, string, re

import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om

import OCT_RenderSet_zwz
import OCT_Associate_attribute_zwz
import ui_Checkin
import OCT_xGPUCache
import OCT_edit_vrayZDepth_deadline


def renameTexture_temp():
    fileNodeNameList = mc.ls(typ='file')
    if not fileNodeNameList:
        mc.error('No file node on the scence!')

    pathNameList = os.listdir(r'Z:\Themes')

    currentFilePath = mc.file(sn=True,q=True)
    (filePath, fileName) = os.path.split(currentFilePath)
    currentProject_split = fileName.split('_')
    if len(currentProject_split)>1:
        currentProject = currentProject_split[0]
    else:
        mc.error('file name is error!please change!')

    renameDict = {}
    nodeDict = {}

    for fileNodeName in fileNodeNameList:
        fileTexturePath = mc.getAttr('%s.fileTextureName' %fileNodeName)
        if not os.path.isfile(fileTexturePath):
            mc.warning('%s is not exist!' %fileTexturePath)
            continue
        if fileTexturePath in renameDict:
            nodeDict[fileNodeName] = renameDict[fileTexturePath]
            continue
        (filePath, fileName) = os.path.split(fileTexturePath)
        fileName_split = fileName.split('_')
        if fileName_split[0] in pathNameList:
            fileName_split[0] = currentProject
        else:
            fileName_split.insert(0, currentProject)
        newFileName = ('_').join(fileName_split)
        newFilePath = os.path.join(filePath, newFileName)
        
        renameDict[fileTexturePath] = newFilePath
        nodeDict[fileNodeName] = newFilePath

    for oldName, newName in renameDict.items():
        os.rename(oldName, newName)
    for nodeName, newPath in nodeDict.items():
        mc.setAttr('%s.fileTextureName' %nodeName, newPath, type="string")
        
        

def Unload_Plugins():
   import UnloadPlugin
   UnloadPlugin.main()

def NewPlayBlsst_zwz():
    import OCT_QuickPlayAllBlast_zwz
    i = OCT_QuickPlayAllBlast_zwz.QuickPlayAllBlast_C_zwz()
    i.show()

def deleteSelectGroup():
    alls = mc.ls(sl = True)
    if not alls:
        return
    allShapes = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True,tr = True)
    if mc.window("delSelGroup",q=True,exists=True):
        mc.deleteUI("delSelGroup")  
    mc.window("delSelGroup",title=u"提醒",widthHeight=(100,200),sizeable=True)
    t = mc.columnLayout()
    mc.frameLayout('Set',label = u'可能删除下列组，确定要删除！确定：OK, 否：NO',labelAlign = 'top',borderStyle = 'etchedOut',w=280,parent = t)
    uiTextAll = mc.textScrollList('sel', append = alls, aas=True, allowMultiSelection=True, h=100, w =  280, parent=t)
    mc.setParent("..")
    mc.rowLayout('butRow',numberOfColumns = 2,columnWidth2 =(140,140),columnAlign2=('center', 'center'),height =30)
    mc.button( 'okButton',label=u'OK',width =140,command = 'OCT_generel.deleteSelectGroups(%s, %s)'%(allShapes,alls),parent = 'butRow')
    mc.button( 'noButton',label=u'NO',width =140,command = 'mc.deleteUI("delSelGroup",window=True)',parent = 'butRow')
       
    mc.showWindow("delSelGroup") 

def deleteSelectGroups(allShapes, all):
   # all = mc.ls(sl = True)
    # if all:
    #     result = mc.confirmDialog(title = u'提醒', message = u'可能会删除%s组，确定要删除！\n确定：Yes, 否：NO'%all, button = ['Yes', 'No'])
    #     if result == 'No':
    #         return
    
    for i in allShapes:
        lock = mc.lockNode(i, q = True,l= True)
        if lock:
            mc.lockNode(i,l= False)
    mc.delete(all)
    if mc.window("delSelGroup",q=True,exists=True):
        mc.deleteUI("delSelGroup")  

def SetRenderDeepPath():
    import OCT_RenderDeepSetPath
    i=OCT_RenderDeepSetPath.AssetDeadline()
    if i.checkFile(2):
        CopySetPath = OCT_RenderDeepSetPath.SetProjectPath()
        CopySetPath.setPath(i.myUseRender)

def CopyYeti():
    import CopyYetiCacheAndTex
    CopyYetiCacheAndTex.copyYetiCacheAndTex()
    
def references():
    import OCT_ReferenceChange
    i=OCT_ReferenceChange.ReferenceFileChange()
    i.ReferenceFile()
    
#maya2016的arnold代理去掉延迟加载，渲染代理的问题
def UnDeferStandinLoad():
    allAiStandIn = mc.ls(type = "aiStandIn")
    for aiS in allAiStandIn:
        mc.setAttr("%s.deferStandinLoad"%aiS,0)

def deleteUnknown():
    allunknows=mc.ls(type="unknown")
    for unknows in allunknows:
        if mc.objExists(unknows):
            if mc.lockNode(unknows,q=True):
                mc.lockNode(unknows,l=False)
            mc.delete(unknows)

def submitMayaToDeadline_zwz(type):
    import OCT_deadline_submit_zwz
    #检查模式
    if type == 1:
        i = OCT_deadline_submit_zwz.AssetDeadline()
        if i.checkFile(1):
            mc.confirmDialog(title=u'温馨提示：', message=u'------恭喜你！------\n------好消息！------\n---工程文件完好！---', button=['OK'], defaultButton='Yes', dismissString='No')
    #检查并拷贝模式
    elif type == 2:
        i = OCT_deadline_submit_zwz.AssetDeadline()
        if i.checkFile(1):
            CopyJob = OCT_deadline_submit_zwz.CopyProject()
            CopyJob.main(1, i.myUseRender)
    #检查、拷贝、上传模式
    elif type == 3:
        usename = os.environ['USERNAME']
        fPath = r'\\octvision.com\cg\Tech\maya_sixteen\Python\OCT_generel\Deadline\Deadline_User.cfg'
        f = file(fPath, 'r')
        infoStr = f.readlines()
        f.close()
        for i in range(len(infoStr)):
            infoStr[i] = infoStr[i][:-2]
        if usename in infoStr:
            i = OCT_deadline_submit_zwz.AssetDeadline()
            if i.checkFile(2):
                if mc.window('hyperShadePanel1Window', q=True, exists=True):
                    mc.deleteUI('hyperShadePanel1Window')
                if mc.window('renderViewWindow', q=True, exists=True):
                    mc.deleteUI('renderViewWindow')
                result = mc.confirmDialog(title=u'温馨提示', message=u'是否暂停提交，检查渲染层是否关闭？\nYes：暂停提交，No:继续提交', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                if result == 'Yes':
                    return
                # effectFile = mc.confirmDialog(title=u'温馨提示', message=u'提交渲染后是否将文件交接给特效环节？\n是 = deadline渲染 + 交接给特效 \n否 = deadline渲染', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                # if effectFile == 'Yes':
                #     CopyJob = OCT_deadline_submit_zwz.CopyProject()
                #     CopyJob.main(5, i.myUseRender)
                #弹窗提示 修改vray ZDepth参数
                OCT_edit_vrayZDepth_deadline.edit_vrayZDepth_deadline()

                i.show()
        else:
            mc.confirmDialog(title=u'温馨提示：', message=u'提交功能仅支持灯光组和后期组使用本工具！', button=['OK'], defaultButton='Yes', dismissString='No')
            sys.stderr.write(u'提交功能仅支持灯光组和后期组使用本工具！')
    elif type == 4:
        usename = os.environ['USERNAME']
        fPath = r'\\octvision.com\cg\Tech\maya_sixteen\Python\OCT_generel\Deadline\Deadline_User.cfg'
        f = file(fPath, 'r')
        infoStr = f.readlines()
        f.close()
        for i in range(len(infoStr)):
            infoStr[i] = infoStr[i][:-2]
        if usename in infoStr:
            i = OCT_deadline_submit_zwz.AssetDeadline()
            if i.checkFile(3):
                i.show()
        else:
            mc.confirmDialog(title=u'温馨提示：', message=u'提交功能仅支持后期组使用本工具！', button=['OK'], defaultButton='Yes', dismissString='No')
            sys.stderr.write(u'提交功能仅支持后期组使用本工具！')
    elif type == 5:
        import OCT_RenderDeepSet
        deep=OCT_RenderDeepSet.OCT_RenderDeepSet()
        deep.OCT_RenderDeepSet_UI()
    elif type == 6:
        i = OCT_deadline_submit_zwz.AssetDeadline()
        if i.checkFile(5):
            CopyJob = OCT_deadline_submit_zwz.CopyProject()
            CopyJob.main(5, i.myUseRender)

    elif type == 7:
        import OCT_deadline_submit_zwz_test
        usename = os.environ['USERNAME']
        fPath = r'\\octvision.com\cg\Tech\maya_sixteen\Python\OCT_generel\Deadline\Deadline_User.cfg'
        f = file(fPath, 'r')
        infoStr = f.readlines()
        f.close()
        for i in range(len(infoStr)):
            infoStr[i] = infoStr[i][:-2]
        if usename in infoStr:
            i = OCT_deadline_submit_zwz_test.AssetDeadline()
            if i.checkFile(2):
                if mc.window('hyperShadePanel1Window', q=True, exists=True):
                    mc.deleteUI('hyperShadePanel1Window')
                if mc.window('renderViewWindow', q=True, exists=True):
                    mc.deleteUI('renderViewWindow')
                result = mc.confirmDialog(title=u'温馨提示', message=u'是否暂停提交，检查渲染层是否关闭？\nYes：暂停提交，No:继续提交', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                if result == 'Yes':
                    return
                # effectFile = mc.confirmDialog(title=u'温馨提示', message=u'提交渲染后是否将文件交接给特效环节？\n是 = deadline渲染 + 交接给特效 \n否 = deadline渲染', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                # if effectFile == 'Yes':
                #     CopyJob = OCT_deadline_submit_zwz.CopyProject()
                #     CopyJob.main(5, i.myUseRender)
                i.show()
        else:
            mc.confirmDialog(title=u'温馨提示：', message=u'提交功能仅支持灯光组和后期组使用本工具！', button=['OK'], defaultButton='Yes', dismissString='No')
            sys.stderr.write(u'提交功能仅支持灯光组和后期组使用本工具！')

def callArnoldTools():
    if not mc.pluginInfo('mtoa.mll', query=True, loaded=True):
        mc.loadPlugin('//octvision.com/CG/Tech/maya_sixteen/modules/solidangle/mtoadeploy/2016/plug-ins/mtoa.mll')
    import customTools_therenderblog
    reload(customTools_therenderblog)
    customTools_therenderblog.UI()

def ReplaceOriginalObject():
    import OCT_ReplaceOriginalObject_zwz
    i = OCT_ReplaceOriginalObject_zwz.ReplaceOriginalObject_zwz()
    i.show()
    
def OpenCloseRenderThumbnailUpdate():
    if mc.window("OpenCloseRenderThumbnailUpdate",ex=True):
        mc.deleteUI("OpenCloseRenderThumbnailUpdate")
    mc.window("OpenCloseRenderThumbnailUpdate",title=u"打开与关闭材质更新",sizeable=False,toolbox=True)
    mc.rowColumnLayout(numberOfColumns=True)
    mc.text(l="")
    mc.text(fn="boldLabelFont",l=u"打开与关闭材质更新")
    mc.text(l="")
    mc.text(l="")
    mc.button(l=u"Open",c="mm.eval('renderThumbnailUpdate true;')",bgc=[0.1,0.6,0.3])
    mc.text(l="")
    mc.button(l=u"Close",c="mm.eval('renderThumbnailUpdate false;')",bgc=[0.1,0.3,0.3])
  
    mc.showWindow('OpenCloseRenderThumbnailUpdate')  

def cleanUnusedCamera_zwz():
    allLight = mc.ls(type='light')
    for myLight in allLight:
        myTLights = mc.listRelatives(myLight, p=True, path=True)
        for myTLight in myTLights:
            myAllSLights = mc.listRelatives(myTLight, c=True, path=True)
            for mySLight in myAllSLights:
                if mc.objectType(mySLight) == 'camera':
                    mc.delete(mySLight)
    om.MGlobal.displayWarning(u'灯光内的无用摄像机已经清理完毕！')


def OCT_Export_Scene_with_Optimize_zwz():
    #重命名动画、素材节点名字
    AllmYRenameObjects = mc.ls(type=['animCurveTA', 'animCurveTL', 'animCurveTU', 'place2dTexture','envBall','bump2d'])
    ALlShader = mc.ls(mat=True,tex=True)
    AllmYRenameObjects += ALlShader
    for each in AllmYRenameObjects:
        AllSplitNs = each.split('_')
        try:
            mc.rename(each, AllSplitNs[-1])
        except:
            try:
                mc.rename(each, '_'.join(AllSplitNs[-2::]))
            except:
                pass
    #删除空层，删除被锁无连接的reference节点
    useDLayers = []
    emptyDLayers = []
    allDLayers = mc.ls(type='displayLayer')
    for Layer in allDLayers:
        if mc.getAttr('%s.identification' % Layer):
            useDLayers.append(Layer)
    for each in useDLayers:
        if not mc.editDisplayLayerMembers(each, q=True, noRecurse=True):
            emptyDLayers.append(each)
    for tmp in emptyDLayers:
        allInfoNodes = mc.listConnections('%s.drawInfo' % tmp, c=True)
        if allInfoNodes:
            for InfoNode in allInfoNodes:
                if mc.nodeType(InfoNode) == 'reference':
                    mc.lockNode(InfoNode, lock=False)
                    mc.delete(InfoNode)
        mc.delete(tmp)
    #删除无子物体，无关联的空组
    deleteList = []
    allTransforms = mc.ls(type='transform')
    if allTransforms:
        for tran in allTransforms:
            if mc.nodeType(tran) == 'transform':
                children = mc.listRelatives(tran, c=True)
                connectNode = mc.listConnections(tran)
                if children is None and connectNode is None:
                    #打印空组的名字
                    print '%s, has no childred or no connected' % (tran)
                    deleteList.append(tran)
    if deleteList:
        try:
            mc.delete(deleteList)
        except:
            pass
    #if mc.ls(sl=True):
    if mc.windowPref('scriptEditorPanel1Window', exists=True):
        mc.windowPref('scriptEditorPanel1Window', remove=True)
    if mc.window('scriptEditorPanel1Window', exists=True):
        mc.deleteUI('scriptEditorPanel1Window', window=True)
    if mc.windowPref('outlinerPanel1Window', exists=True):
        mc.windowPref('outlinerPanel1Window', remove=True)
    if mc.window('outlinerPanel1Window', exists=True):
        mc.deleteUI('outlinerPanel1Window', window=True)
    #显示层
    myDLayers = []
    allDLayers = mc.ls(type='displayLayer')
    for Layer in allDLayers:
        if mc.getAttr('%s.identification' % Layer):
            myDLayers.append(Layer)
    #渲染节点
    allPartitions = mc.ls(type='partition')
    #渲染层
    allMyRLayers = mc.listConnections('renderLayerManager.renderLayerId')
    allMyRLayers.append('renderLayerManager')
    #时间滑条
    if mc.objExists('sceneConfigurationScriptNode'):
        mc.select('sceneConfigurationScriptNode', add=True)
    #选择摄像机
    AllCameras = mc.listCameras()
    #参考节点
    myRfs = mc.ls(type='reference')
    if mc.objExists('defaultLayer'):
        mc.select('defaultLayer', add=True)
    #选择绑定设置的Sets节点
    if mc.objExists('Sets'):
        mc.select('Sets', add=True, ne= True)
    #选择mentalray相关渲染信息
    if mc.objExists('mentalrayGlobals'):
        mc.select('mentalrayGlobals', add=True)
    #选择vray渲染的相关信息
    if mc.objExists('vraySettings'):
        mc.select('vraySettings', add=True)
    #选择Arnold的分层节点
    if mc.pluginInfo('mtoa.mll', query=True, loaded=True):
        try:
            allMyArnoldAOV = mc.ls(type="aiAOV")
        except:
            pass
        else:
            if allMyArnoldAOV:
                mc.select(allMyArnoldAOV, add=True)
        try:
            ArnoldDisplayDriver = mc.ls(type="aiAOVDriver")
        except:
            pass
        else:
            if ArnoldDisplayDriver:
                mc.select(ArnoldDisplayDriver, add=True)
        try:
            defaultArnoldFilter = mc.ls(type="aiAOVFilter")
        except:
            pass
        else:
            if defaultArnoldFilter:
                mc.select(defaultArnoldFilter, add=True)
        try:
            defaultArnoldRenderOptions = mc.ls(type="aiOptions")
        except:
            pass
        else:
            if defaultArnoldRenderOptions:
                mc.select(defaultArnoldRenderOptions, add=True)

    #Vray渲染层
    try:
        allVrayRLs = mc.ls(type='VRayRenderElement')
    except:
        pass
    else:
        if allVrayRLs:
            mc.select(allVrayRLs, add=True)
    if AllCameras:
        mc.select(AllCameras, add=True)
    if myRfs:
        mc.select(myRfs, add=True)
    if myDLayers:
        mc.select(myDLayers, add=True)
    if allPartitions:
        mc.select(allPartitions, add=True)
    if allMyRLayers:
        mc.select(allMyRLayers, add=True)
    mc.select(allDagObjects=True, add=True)
    mc.evalDeferred('mc.ExportSelection();mc.select(cl=True)')
    # else:
    #     mc.confirmDialog(title=u'警告', message=u'请框选outline中所有DAG物体\n(即在勾选‘show DAG Objects Only ’的模式下显示的所有物体)', button=['OK'], defaultButton='Yes', dismissString='No')



def close(uiName):
    mc.deleteUI(uiName, window=1)


'''def checkName():
    allDagObj = mc.ls(dag=1, sn=1)

    sameName = []
    rebuild = {}
    for eachObj in allDagObj:
        _split =  eachObj.split('|')
        #print _split

        rebuild[eachObj] = _split.pop()

    _values = rebuild.values()
    for eachVal in _values:
        _count = _values.count(eachVal)
        if _count > 1:
            sameName.append(eachVal)

            for n in range(_count-1):
                _values.remove(eachVal)

    if len(sameName) > 0:
        mc.select(d=1)
        for k, v in rebuild.iteritems():
            if v in sameName:
                mc.select(k,add=1)
    else:
        sys.stdout.write(u'场景中没有重名物体...')'''


def removeNamespace():
    errorCount = 0
    sys.stdout.write('Remove namespace\n')
    sys.stdout.write('----------------\n')

    for count in range(6):
        buf = mc.ls(long=True)
        for each in buf:
            if mc.objExists(each):
                if not mc.referenceQuery(each, isNodeReferenced=True):
                    eachSV = each.split('|')
                    name = eachSV[len(eachSV)-1]
                    #sp = re.match('[0-9a-zA-Z_]*:',name)
                    sp = mm.eval('match "([0-9a-zA-Z_]*:)+" "%s"' % name)
                    if sp:
                        name = mm.eval('substitute "%s" "%s" ""' % (sp, name))
                        if not mm.eval('catch(`rename "%s" "%s"`)' % (each, name)):
                            if count == 5:
                                errorCount += 1
    sys.stdout.write(u'改名完成，还有%s个物体修改不成功！，如果还没有达到效果请再点一次！' % errorCount)
    '''
    mc.namespace(set=":")
    _root = []
    _root = mc.namespaceInfo(listOnlyNamespaces=True)

    _root.remove("UI")
    _root.remove("shared")

    _avilibleName = []
    if len(_root) > 0:
        for eachRoot in _root:
            mc.namespace(set=':')
            mc.namespace(set=eachRoot)
            _second = mc.namespaceInfo(listOnlyNamespaces=True)
            if _second != None:
                for eachSecond in _second:
                    mc.namespace(set=':')
                    mc.namespace(set=eachSecond)
                    _third = mc.namespaceInfo(listOnlyNamespaces=True)
                    if _third != None:
                        for eachThird in _third:
                            mc.namespace(set=':')
                            mc.namespace(set=eachThird)
                            _fourth = mc.namespaceInfo(listOnlyNamespaces=True)
                            if _fourth != None:
                                for eachFourth in _fourth:
                                    mc.namespace(set=':')
                                    mc.namespace(set=eachFourth)
                                    _containNode = mc.namespaceInfo(dagPath=1,ls=1)
                                    if _containNode != None:
                                        if mc.objExists(_containNode[0]):
                                            isRef = mc.referenceQuery(_containNode[0],inr=1)
                                    else:
                                        isRef = True

                                    if isRef == False:
                                        _avilibleName.append(eachFourth)
                            else:
                                _containNode = mc.namespaceInfo(dagPath=1,ls=1)
                                if _containNode != None:
                                    if mc.objExists(_containNode[0]):
                                        isRef = mc.referenceQuery(_containNode[0],inr=1)
                                else:
                                    isRef = True

                                if isRef == False:
                                    _avilibleName.append(eachThird)
                    else:
                        _containNode = mc.namespaceInfo(dagPath=1,ls=1)
                        if _containNode != None:
                            if mc.objExists(_containNode[0]):
                                isRef = mc.referenceQuery(_containNode[0],inr=1)
                        else:
                            isRef = True

                        if isRef == False:
                            _avilibleName.append(eachSecond)
            else:
                _containNode = mc.namespaceInfo(dagPath=1,ls=1)
                if _containNode != None:
                    if mc.objExists(_containNode[0]):
                        isRef = mc.referenceQuery(_containNode[0],inr=1)
                else:
                    isRef = True

                if isRef == False:
                    _avilibleName.append(eachRoot)

#	print _avilibleName
        mc.namespace(set=':')
        nameCount = len(_avilibleName)

        if mc.window("removeNamespaceUI",exists=1):
            mc.deleteUI("removeNamespaceUI",window=1)

        if mc.windowPref("removeNamespaceUI",exists=True):
            mc.windowPref("removeNamespaceUI",remove=True)

        mc.window("removeNamespaceUI",title="removeNamespace",maximizeButton=0,resizeToFitChildren=1,sizeable=0,wh=[300,150])
        mc.columnLayout(rowSpacing=4)
        mc.rowLayout(numberOfColumns=2, columnWidth2=(200, 100))
        mc.textScrollList("nameList",width=200,numberOfRows=8, allowMultiSelection=True,append=_avilibleName)
        mc.columnLayout(rowSpacing=4,columnAttach=["both",5])
        mc.button("removeBtn",l="Remove Select",c='OCT_generel.rmSelect(0)')
        mc.button("renameBtn",l="Rename",c="OCT_generel.rnSelect()",enable=False)
        mc.button("renameAllBtn",l="Remove All",c='OCT_generel.rmSelect(1)')
        mc.button("closeBtn",l="Close",c='OCT_generel.close("removeNamespaceUI")')
        mc.setParent('..')
        mc.setParent('..')
        mc.showWindow("removeNamespaceUI")'''

def rmSelect(_mode):
    if _mode == 0:
        _sel = mc.textScrollList("nameList",q=1,selectItem=1)
    else:
        _sel = mc.textScrollList("nameList",q=1,allItems=1)

    if _sel == None:
        return

    for eachSel in _sel:
        mc.namespace(set=':')
        allName = [eachSel]
        mc.namespace(set=eachSel)	
        while mc.namespaceInfo(p=1) != ":":
            allName.append(mc.namespaceInfo(p=1))
            parentName = mc.namespaceInfo(p=1)
            mc.namespace(set=':')
            mc.namespace(set=parentName)	

        mc.namespace(set=':')
        for eachName in allName:
            mc.namespace(f=1,mv=(eachName,":"))
            mc.namespace(rm=eachName)

        if mc.namespace(exists=eachSel) == 0:
            sys.stdout.write(u"已经清除%s..." % eachSel)
            mc.textScrollList("nameList",e=1,removeItem=eachSel)

'''			
def rnSelect():
	_sel = mc.textScrollList("nameList",q=True,selectItem=True)
	result = mc.promptDialog(title='Rename Namespace',message='Enter Name:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')

	if result == 'OK':
		text = mc.promptDialog("enterName",query=True, text=True)
	else:
		print u'请输入要更改的名字...'
		return

	mc.namespace(rename=[_sel,text])
	mc.textScrollList("nameList",e=1,removeItem=_sel)
	mc.textScrollList("nameList",e=1,append=text)
'''


def delDefaultRenderLayer():
    layers = mc.ls(exactType='renderLayer')
    count = 0
    pattern = re.compile('^[a-zA-Z0-9_\:-]*defaultRenderLayer$')
    for eachLayer in layers:
        if pattern.match(eachLayer):
            if not eachLayer == 'defaultRenderLayer':
                try:
                    mc.delete(eachLayer)
                except:
                    om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
                else:
                    count += 1
    del pattern
    
    allmylayers = mc.listConnections("renderLayerManager.renderLayerId")
    for layer in layers:
        if not layer in allmylayers:
            try:
                mc.delete(layer)
            except:
                pass
            else:
                count += 1
    om.MGlobal.displayInfo(u'一共清除了%d 个defaultRenderLayer' % count)

def copyTransform():
    if mc.window("IC_copyTransforms",exists=1):
        mc.deleteUI("IC_copyTransforms")

    _winID = mc.window("IC_copyTransforms",title="IC_copyTransforms",wh=[240,240],s=0,mxb=0)
    mc.columnLayout(columnAttach=('both', 5), rowSpacing=5, columnWidth=230)
    _translateCB = mc.checkBoxGrp("tCB",ncb=3,l="Translate",la3=["x","y","z"],cl4=["left","left","left","left"],cw4=[70,50,50,50])
    _rotateCB = mc.checkBoxGrp("rCB",ncb=3,l="Rotate",la3=["x","y","z"],cl4=["left","left","left","left"],cw4=[70,50,50,50])
    _scaleCB = mc.checkBoxGrp("sCB",ncb=3,l="Scale",la3=["x","y","z"],cl4=["left","left","left","left"],cw4=[70,50,50,50])
    _btn1 = mc.button("ok", label= "copy 1 -=> 2",command="OCT_generel.copyIt()")
    mc.showWindow(_winID)

def copyIt():
    _firstObj = mc.ls(sl=1,head=1)
    _secondObj = mc.ls(sl=1,tail=1)
    _translate = ["translateX","translateY","translateZ"]
    _rotate = ["rotateX","rotateY","rotateZ"]
    _scale = ["scaleX","scaleY","scaleZ"]
    _firstError = []
    _secondError = []
    _tCBvalue = []
    _rCBvalue = []
    _sCBvalue = []
    _tCBstatic = []
    _rCBstatic = []
    _sCBstatic = []

    _tCBstatic.append(mc.checkBoxGrp("tCB",q=1,v1=1))
    _tCBstatic.append(mc.checkBoxGrp("tCB",q=1,v2=1))
    _tCBstatic.append(mc.checkBoxGrp("tCB",q=1,v3=1))

    _rCBstatic.append(mc.checkBoxGrp("rCB",q=1,v1=1))
    _rCBstatic.append(mc.checkBoxGrp("rCB",q=1,v2=1))
    _rCBstatic.append(mc.checkBoxGrp("rCB",q=1,v3=1))

    _sCBstatic.append(mc.checkBoxGrp("sCB",q=1,v1=1))
    _sCBstatic.append(mc.checkBoxGrp("sCB",q=1,v2=1))
    _sCBstatic.append(mc.checkBoxGrp("sCB",q=1,v3=1))

    for _x in range(len(_tCBstatic)):
        if _tCBstatic[_x]:
            _tCBvalue.append(_translate[_x])
        if _rCBstatic[_x]:
            _rCBvalue.append(_rotate[_x])
        if _sCBstatic[_x]:
            _sCBvalue.append(_scale[_x])

    if len(_tCBvalue) == 0 and len(_rCBvalue) == 0 and len(_sCBvalue) == 0:
        warn = r'warning "请选择需要复制的属性";'
        mm.mel(warn)
        #mc.warning('请选择需要复制的属性')
        return

    for eachTrans in _translate:
        if mc.attributeQuery(eachTrans,node=_firstObj[0],exists=1) == 0:
            _firstError.append(eachTrans)

        if mc.attributeQuery(eachTrans,node=_secondObj[0],exists=1) == 0:
            _secondError.append(eachTrans)

    for eachRotate in _rotate:
        if mc.attributeQuery(eachRotate,node=_firstObj[0],exists=1) == 0:
            _firstError.append(eachRotate)

        if mc.attributeQuery(eachRotate,node=_secondObj[0],exists=1) == 0:
            _secondError.append(eachRotate)

    for eachScale in _scale:
        if mc.attributeQuery(eachScale,node=_firstObj[0],exists=1) == 0:
            _firstError.append(eachScale)

        if mc.attributeQuery(eachScale,node=_secondObj[0],exists=1) == 0:
            _secondError.append(eachScale)

    allValue = _tCBvalue + _rCBvalue +_sCBvalue
    for x in allValue:
        if _firstError.count(x):
            warn = r'warning "首选物体没有 %s 属性";' % x
            mm.eval(warn)
        #sys.stdout.write(u'首选物体没有 X 属性')
            #mc.warning('首选物体没有 ' x '属性')
            return

        if (_secondError.count(x)):
            warn = r'warning "后选物体没有 %s 属性";' % x
            mm.eval(warn)
            #mc.warning('后选物体没有 ' x '属性')
            return

        _attValue = ''
        _firstAttr = _firstObj[0] + '.' + x
        _secondAttr = _secondObj[0] + '.' + x
        _attValue = mc.getAttr(_secondAttr)
        mc.setAttr(_firstAttr,_attValue)

def changeRefPath():
    promptState = mc.promptDialog(title='Change Reference File Path',message='New Dir:',button=['OK','Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
    if promptState == 'OK':
        dirText = mc.promptDialog(q=True, text=True)

        if os.path.isdir(dirText):
            allRefNode = mc.ls(sl=True, type='reference')
            if not allRefNode:
                allRefNode = mc.ls(type='reference')

            if len(allRefNode) == 0:
                return

            for eachNode in allRefNode:
                try:
                    refNodeName = mc.referenceQuery(eachNode, rfn=True)
                except:
                    continue

                currentFileName = mc.referenceQuery(refNodeName, filename=True)
                baseName = os.path.basename(currentFileName)
                newFullName = os.path.join(dirText, baseName)
                mc.file(newFullName, loadReference=refNodeName)


'''
OCT_Tools/Generel/PlayBlastTool
date:2012-06-15 16:15
auth:ivancheung7@gmail.com
playblast所选择的摄像机
################################### START #############################################
'''
def playBlast():
    filePath = r'C:\OCTTemp\PlayBlast.txt'
    sizeX = 200
    sizeY = 200
    if os.path.isfile(filePath):
        f = file(filePath, 'r')
        infoStr = f.readlines()
        f.close()
        infoStr[0] = infoStr[0][:-2]
        sizeX = int(infoStr[0].split(" ")[0])
        sizeY = int(infoStr[0].split(" ")[1])

    #加载playBlast全局变量
    # mm.eval('global int $octvCrossPB;$octvCrossPB=1;')
    if mc.window('playBlastUI', ex=True):
        mc.deleteUI('playBlastUI')
    allCam = mc.listCameras(p=True)
    pp = mc.workspace(q=True, rd=True)
    mc.window('playBlastUI', t='OCT_playBlastTool', sizeable=True, mxb=False, mnb=False)
    mc.columnLayout(adj=True)
    mc.rowColumnLayout(numberOfColumns=2, columnAttach=((1, 'right', 5)), cw=((1, 50), (2, 240)), rowSpacing=((1, 5), (2, 5)))
    mc.text(l='Format')
    mc.optionMenu('formatOM', l='', w=50, cc=fOptionChanged)
    mc.menuItem(l='avi')
    mc.menuItem(l='jpg')
    mc.text(l='Encoding')
    mc.optionMenu('coding', l='', w=50)
    mc.menuItem(l='MS-CRAM')
    mc.menuItem(l='MS-RLE')
    mc.menuItem(l='MS-YUV')
    mc.menuItem(l='x264vfw')
    mc.text(l='Quality')
    mc.intSliderGrp('qualityIS', field=True, fmn=0, fmx=100, min=0, max=100, v=80, step=1, width=240)
    mc.text(l = 'Preset')
    mc.checkBox('Preset', l=u'180度球幕', v=0)
    mc.text(l = '')
    mc.checkBox('offscreen', l=u'Render offscreen', v=0)
    mc.text(l='Size')
    mc.optionMenu('sizeOM', l='', w=100, cc=sOptionChanged)
    mc.menuItem(l='Custom')
    mc.menuItem(l='From Render Settings')
    mc.menuItem(l='From Window')
    mc.text(l='')
    mc.rowLayout(nc=2, cw2=[50, 50])
    mc.intField('sizeX', v=sizeX, w=50)
    mc.intField('sizeY', v=sizeY, w=50)
    mc.setParent('..')
    mc.text(l='scale')
    mc.floatSliderGrp('scaleFS', field=True, fmn=0.0, fmx=1.0, min=0.0, max=1.0, v=1, width=240, enable=False)
    mc.text(l='F.Padding')
    mc.intSliderGrp('framePaddingIS', field=True, fmn=1, fmx=6, min=1, max=6, v=4, width=240, enable=False)
    mc.text(l='Save Dir')
    mc.textFieldButtonGrp('outputDir', l='', fi=pp, bl='Browser', bc='OCT_generel.doOutputPath()', width=240, cw3=[0, 184, 40], cl3=['left', 'left', 'left'], ct3=['left', 'left', 'left'])
    mc.setParent('..')
    mc.separator(w=290)
    mc.rowLayout(nc=2, w=290, cw2=(50, 240), cal=[1, 'right'], cat=((1, 'both', 4), (2, 'left', 0)))
    mc.text(l='Cameras')
    mc.rowColumnLayout('myCameraRC', nc=3)
    for eachCam in allCam:
        mc.checkBox(eachCam, l=eachCam, v=0)
    mc.setParent('..')
    mc.setParent('..')
    mc.text(l='')
    mc.rowLayout(nc=2, cw2=[145, 145], w=290, cal=((1, 'left'), (2, 'right')), cat=((1, 'right', 5), (2, 'left', 5)))
    mc.button('okBtn', l='PlayBlast', w=60, c='OCT_generel.doPlayBlast()')
    # mc.button('okBtn', l='PlayBlast', w=60, c='doPlayBlast()')
    mc.button('closeBtn', l='Close', w=60, c='mc.deleteUI("playBlastUI")')
    mc.setParent('..')
    mc.showWindow('playBlastUI')
    myCamersRC_W = mc.rowColumnLayout('myCameraRC', q=True, w=True)
    mc.window('playBlastUI', e=True, w=myCamersRC_W+70)

def fOptionChanged(item):
    if item == 'avi':
        mc.optionMenu('coding', e=True, enable=True)
        mc.intSliderGrp('qualityIS', e=True, enable=True)
        mc.intSliderGrp('framePaddingIS', e=True, enable=False)
    else:
        mc.optionMenu('coding', e=True, enable=False)
        mc.intSliderGrp('qualityIS', e=True, enable=False)
        mc.intSliderGrp('framePaddingIS', e=True, enable=True)

def sOptionChanged(item):
    if item == 'Custom':
        mc.floatSliderGrp('scaleFS', e=True, enable=False, v=1.0)
        mc.intField('sizeX', e=True, enable=True)
        mc.intField('sizeY', e=True, enable=True)
    else:
        mc.floatSliderGrp('scaleFS', e=True, enable=True)
        mc.intField('sizeX', e=True, enable=False)
        mc.intField('sizeY', e=True, enable=False)

def doOutputPath():
    pp = mc.textFieldButtonGrp('outputDir', q=True, fileName=True)
    if not os.path.exists(pp):
        pp = ''

    try:
        oPath = mc.fileDialog2(fm=3,ds=2, dir=pp)
        if not oPath == '':
            mc.textFieldButtonGrp('outputDir', e=True, fileName=oPath[0])
    except:
        return

def doPlayBlast():
    if mc.checkBox('offscreen', q=True, v=True):
        mc.optionVar(intValue = ['playblastOffscreen', 1])
    else:
        mc.optionVar(intValue = ['playblastOffscreen', 0])

    format = mc.optionMenu('formatOM', q=True, v=True)
    _coding = mc.optionMenu('coding', q=True, v=True)
    _quality = mc.intSliderGrp('qualityIS', q=True, v=True)
    sizeMode = mc.optionMenu('sizeOM', q=True, sl=True)
    scale = mc.floatSliderGrp('scaleFS', q=True, v=True)
    sizeX = mc.intField('sizeX', q=True, v=True)
    sizeY = mc.intField('sizeY', q=True, v=True)

    filePath = r'C:\OCTTemp\PlayBlast.txt'
    if not os.path.isdir(r'C:\OCTTemp'):
        os.makedirs(r'C:\OCTTemp')
    if os.path.isfile(filePath):
        os.remove(filePath)
    f = open(filePath, 'wt')
    f.write(str(sizeX)+" "+str(sizeY)+"\n")
    f.close()

    fPadding = mc.intSliderGrp('framePaddingIS', q=True, v=True)
    oPath =  mc.textFieldButtonGrp('outputDir', q=True, fileName=True)

    allCam = mc.listCameras(p=True)
    playCam = []
    del playCam[:]
    for eachCam in allCam:
        if mc.checkBox(eachCam, q=True, v=True):
            playCam.append(eachCam)

    if oPath == '' and not os.path.isdir(oPath):
        mc.confirmDialog(m='Please input Save Dir.')
        return

    if len(playCam) == 0:
        mc.confirmDialog(m='Please select least one camera')
        return

    gMainPane = mm.eval('global string $gMainPane;\n$temp = $gMainPane;')
    activePanel = ''
    allPanel = mc.paneLayout(gMainPane, q=True, ca=True)
    for eachPanel in allPanel:
        panelName = mc.getPanel(containing=eachPanel)
        if not panelName == '':
            if mc.getPanel(to=panelName) == 'modelPanel':
                if not mc.control(eachPanel, q=True, io=True):
                    if mc.modelEditor(panelName, q=True, av=True):
                        activePanel = panelName
                        break

    if activePanel == '':
        mc.confirmDialog(m='Please active one ModelPanel \nthen re-click PlayBlast Button')
        return

    if sizeMode == 2:
        sizeX = mc.getAttr('defaultResolution.width')
        sizeY = mc.getAttr('defaultResolution.height')
    elif sizeMode == 3:
        sizeX = 0
        sizeY = 0

    _widthHeight = [sizeX, sizeY]

    _WH = _widthHeight
    pattern1 = re.compile('^(\w+)([DU]{1})$')
    pattern2 = re.compile('^(\w+)([LR]{1})$')

    _percent = scale * 100
    amount = 0
    count = len(playCam)
    per = 100/count
    finish = 0

    mc.progressWindow(t='PlayBlast Status', progress=amount, status=('Finished:0/%d' % count), isInterruptable=True)
    for num, eachCam in enumerate(playCam):
        if mc.checkBox('Preset', q=True, v=True):
            if pattern1.match(eachCam):
                _widthHeight = [_WH[0], _WH[1]/2]
            elif pattern2.match(eachCam):
                _widthHeight = [_WH[0]/2, _WH[1]]
            else:
                _widthHeight = _WH
        mc.lookThru(eachCam, activePanel)        
        # camName = string.replace(eachCam, ':', '_')
        eachFinalCam = eachCam.split(':')[-1]
        fullName = os.path.join(oPath, eachFinalCam)
        if num == 0:
            mm.eval('source buildDisplayMenu.mel')
            v1 = mc.optionVar(q='selectDetailsVisibility')
            v2 = mc.optionVar(q='objectDetailsVisibility')
            v3 = mc.optionVar(q='particleCountVisibility')
            v4 = mc.optionVar(q='polyCountVisibility')
            v5 = mc.optionVar(q='subdDetailsVisibility')
            v6 = mc.optionVar(q='animationDetailsVisibility')
            v7 = mc.optionVar(q='hikDetailsVisibility')
            v8 = mc.optionVar(q='frameRateVisibility')
            v9 = mc.optionVar(q='currentFrameVisibility')
            v10 = mc.optionVar(q='sceneTimecodeVisibility')
            v11 = mc.optionVar(q='currentContainerVisibility')
            v12 = mc.optionVar(q='cameraNamesVisibility')
            v13 = mc.optionVar(q='focalLengthVisibility')
            v14 = mc.optionVar(q='viewAxisVisibility')
            v15 = mc.optionVar(q='userNameVisibility')
            v16 = mc.optionVar(q='fileNameVisibility')
            mm.eval("setObjectDetailsVisibility 0;")
            mm.eval("setParticleCountVisibility 0;")
            mm.eval("setPolyCountVisibility 0;")
            if mc.isTrue("SubdivUIExists"):
                mm.eval("setSubdDetailsVisibility 0;")
            #mm.eval("setSubdDetailsVisibility 0;")
            mm.eval("setAnimationDetailsVisibility 0;")
            mm.eval("setHikDetailsVisibility 0;")
            mm.eval("setFrameRateVisibility 0;")
            mm.eval("setCurrentFrameVisibility %s;" % v9)
            mm.eval("setSceneTimecodeVisibility %s;" % v10)
            mm.eval("setCurrentContainerVisibility 0;")
            mm.eval("setCameraNamesVisibility 0;")
            mm.eval("setFocalLengthVisibility %s;" % v13)
            mm.eval("setViewAxisVisibility 0;")
            mm.eval("setUserNameVisibility %s;" % v15)
            mm.eval("setFileNameVisibility %s;" % v16)
            if format == 'avi':
                audioNames = mc.ls(type = 'audio')
                if audioNames:
                    try:
                        mc.playblast(format='movie', sound = audioNames[0], filename=fullName+'.avi', csd=True, clearCache=False, viewer=False, showOrnaments=True, percent=_percent, quality=_quality, widthHeight=_widthHeight, compression=_coding, fo=True)
                    except:
                        mc.confirmDialog(title=u'温馨提示：', message=u'请先确认是否安装了x64Components软件！', button=['OK'], defaultButton='Yes', dismissString='No')
                        sys.stderr.write(u'请先确认是否安装了x64Components软件！')

                else:
                    try:
                        mc.playblast(format='movie', filename=fullName+'.avi', csd=True, clearCache=False, viewer=False, showOrnaments=True, percent=_percent, quality=_quality, widthHeight=_widthHeight, compression=_coding, fo=True)
                    except:
                        mc.confirmDialog(title=u'温馨提示：', message=u'请先确认是否安装了x64Components软件！', button=['OK'], defaultButton='Yes', dismissString='No')
                        sys.stderr.write(u'请先确认是否安装了x64Components软件！')
            else:
                if not os.path.isdir(fullName):
                    os.makedirs(fullName)
                    fullName = os.path.join(fullName, eachFinalCam)
                mc.playblast(format='iff', filename=fullName, clearCache=False, viewer=False, showOrnaments=True, percent=_percent, quality=_quality, widthHeight=_widthHeight, compression='jpg', fp=fPadding, fo=True)
            mm.eval("setSelectDetailsVisibility %s;" % v1)
            mm.eval("setObjectDetailsVisibility %s;" % v2)
            mm.eval("setParticleCountVisibility %s;" % v3)
            mm.eval("setPolyCountVisibility %s;" % v4)
            if mc.isTrue("SubdivUIExists"):
                mm.eval("setSubdDetailsVisibility %s;" % v5)
            #mm.eval("setSubdDetailsVisibility %s;" % v5)
            mm.eval("setAnimationDetailsVisibility %s;" % v6)
            mm.eval("setHikDetailsVisibility %s;" % v7)
            mm.eval("setFrameRateVisibility %s;" % v8)
            mm.eval("setCurrentFrameVisibility %s;" % v9)
            mm.eval("setSceneTimecodeVisibility %s;" % v10)
            mm.eval("setCurrentContainerVisibility %s;" % v11)
            mm.eval("setCameraNamesVisibility %s;" % v12)
            mm.eval("setFocalLengthVisibility %s;" % v13)
            mm.eval("setViewAxisVisibility %s;" % v14)
            mm.eval("setUserNameVisibility %s;" % v15)
            #mm.eval("setFileNameVisibility %s;" % v16)
        else:
            if format == 'avi':
                audioNames = mc.ls(type = 'audio')
                if audioNames:
                    try:
                        mc.playblast(format='movie', sound = audioNames[0], filename=fullName+'.avi', clearCache=False, viewer=False, showOrnaments=False, percent=_percent, quality=_quality, widthHeight=_widthHeight, compression=_coding, fo=True)
                    except:
                        mc.confirmDialog(title=u'温馨提示：', message=u'请先确认是否安装了x64Components软件！', button=['OK'], defaultButton='Yes', dismissString='No')
                        sys.stderr.write(u'请先确认是否安装了x64Components软件！')
                else:
                    try:
                        mc.playblast(format='movie', filename=fullName+'.avi', clearCache=False, viewer=False, showOrnaments=False, percent=_percent, quality=_quality, widthHeight=_widthHeight, compression=_coding, fo=True)
                    except:
                        mc.confirmDialog(title=u'温馨提示：', message=u'请先确认是否安装了x64Components软件！', button=['OK'], defaultButton='Yes', dismissString='No')
                        sys.stderr.write(u'请先确认是否安装了x64Components软件！')
            else:
                if not os.path.isdir(fullName):
                    os.makedirs(fullName)
                    fullName = os.path.join(fullName, eachFinalCam)
                mc.playblast(format='iff', filename=fullName, clearCache=False, viewer=False, showOrnaments=False, percent=_percent, quality=_quality, widthHeight=_widthHeight, compression='jpg', fp=fPadding, fo=True)
        if mc.progressWindow(q=True, ic=True):
            break
        # if mc.progressWindow(q=True, progress=True) >= 100:
        #     break

        amount += per
        finish += 1

        mc.progressWindow(e=True, progress=amount, status=('Finished:%d/%d' % (finish, count)))
        mc.pause(seconds=0.2)

    mc.progressWindow(e=True,progress=100)
    mc.progressWindow(endProgress=1)

# playBlast()

'''
##################################### END #########################################
OCT_Tools/Generel/PlayBlastTool
'''
def fixCacheFilePath():
    ext = 'xml'
    count = 0
    node = []
    cacheNode = mc.ls(type='cacheFile')
    lenCaches = len(cacheNode)
    dataType = ''
    if lenCaches:
        while True:
            result = mc.promptDialog(t="Enter Cache Dirctroy", m=' Path`s example: D:\work\Test\data', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root = mc.promptDialog(q=True, t=True)
                if os.path.isdir(root):
                    if root[-4::] == "data":
                        dataType = root[-4::]
                    elif root[-9::] == "particles":
                        dataType = root[-9::]
                    else:
                        mc.confirmDialog(m=u'目前只支持data和particles目录下的缓存更改\n请确定新的目录是否在data或者particles下\n\n请重新输入路径')
                        break
                    dataTypeLen = len(dataType)
                    for each in cacheNode:
                        cacheName = mc.getAttr('%s.cacheName' % each)
                        cachePath = mc.getAttr('%s.cachePath' % each)
                        dataAddress = cachePath.find("/%s/" % dataType)
                        newcachePath = cachePath[dataAddress+dataTypeLen+1::]
                        newcachePath = newcachePath.replace("/", "\\")
                        tmp = root+newcachePath
                        newFile = os.path.join(tmp, cacheName) + '.%s' % ext
                        if os.path.isfile(newFile):
                            print newFile
                            count += 1
                            mc.setAttr('%s.cachePath' % each, tmp, type='string')
                        else:
                            node.append(each)
                    if count > 0:
                        print u'一共有%d个缓存节点\n'%lenCaches
                        print u'一共有%d个cacheFile节点缓存路径被替换到%s\n'%(count, root)
                    if count == lenCaches:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成')
                    else:
                        print u'以下的节点缓存节点在新路径找不到:\n'
                        print node
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!\n详细请看脚本编辑器')
                    break
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            else:
                break
    else:
        mc.confirmDialog(m=u'场景里没有cacheFile节点...')


def fixAbcCacheFilePath():
    count = 0
    node = []
    allMyAbcNodes = mc.ls(type='AlembicNode')
    lenCaches = len(allMyAbcNodes)
    dataType = ''
    if lenCaches:
        while True:
            result = mc.promptDialog(t="Enter Cache Dirctroy", m=r' Path`s example: D:\work\Test\cache\alembic', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root = mc.promptDialog(q=True, t=True)
                if os.path.isdir(root):
                    if root[-13::]!= "cache\\alembic":
                        mc.confirmDialog(m=u'目前只支持cache\alembic目录下的缓存更改\n请确定新的目录是否在cache\alembic下\n\n请重新输入路径')
                        break
                    for each in allMyAbcNodes:
                        cacheName = mc.getAttr('%s.abc_File' % each)
                        cacheBaseName = os.path.basename(cacheName)
                        newFile = os.path.join(root, cacheBaseName)
                        if os.path.isfile(newFile):
                            print newFile
                            count += 1
                            mc.setAttr('%s.abc_File'%each, newFile, type='string')
                        else:
                            node.append(each)
                    if count > 0:
                        print u'一共有%d个缓存节点\n'%lenCaches
                        print u'一共有%d个cacheFile节点缓存路径被替换到%s\n'%(count, root)
                    if count == lenCaches:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成!\n\n如果看到动画，请保存文件后再打开即可！！！\n\n')
                    else:
                        print u'以下的节点缓存节点在新路径找不到:\n'
                        print node
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!!!\n详细请看脚本编辑器!!!!\n\n如果看到动画，请保存文件后再打开即可！！！\n\n')
                    break
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            else:
                break
    else:
        mc.confirmDialog(m=u'场景里没有Alembic Cache节点...')

def fixVRayMeshFilePath():
    count = 0
    node = []
    vrProxyNode = mc.ls(type='VRayMesh')
    lenProxyN = len(vrProxyNode)
    if lenProxyN:
        while True:
            result = mc.promptDialog(t="Enter Proxy Dirctroy", m='Path`s example: D:\work\Test\sourceimages', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root = mc.promptDialog(q=True, t=True)
                if os.path.isdir(root):
                    if root[-12::] != "sourceimages":
                        mc.confirmDialog(m=u'目前只支持sourceimages目录下的缓存更改\n请确定新的目录是否在sourceimages下\n\n请重新输入路径!')
                        break
                    for each in vrProxyNode:
                        proxyName = mc.getAttr('%s.fileName' % each)
                        if proxyName:
                            tmp = os.path.split(proxyName)
                            newProxyPath = os.path.join(root, tmp[1])
                            if os.path.isfile(newProxyPath):
                                print each, newProxyPath
                                count += 1
                                mc.setAttr('%s.fileName' % each, newProxyPath, type='string')
                            else:
                                node.append(each)
                    if count > 0:
                        print u'一共有%d个缓存节点\n' % lenProxyN
                        print u'一共有%d个cacheFile节点缓存路径被替换到%s\n' % (count, root)
                    if count == lenProxyN:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成')
                    elif count == 0:
                        mc.confirmDialog(m=u'全部替换不成功 ,请检查该路径是否存在相应的文件')
                    else:
                        print u'以下的节点缓存节点在新路径找不到:\n'
                        print node
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!\n详细请看脚本编辑器')
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            break
    else:
        mc.confirmDialog(m=u'场景里没有VRayMesh节点...')


def fixaiStandInFilePath():
    count = 0
    node = []
    vrProxyNode = mc.ls(type='aiStandIn')
    lenProxyN = len(vrProxyNode)
    if lenProxyN:
        while True:
            result = mc.promptDialog(t="Enter Proxy Dirctroy", m='Path`s example: D:\work\Test\sourceimages', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root = mc.promptDialog(q=True, t=True)
                if os.path.isdir(root):
                    if root[-12::] != "sourceimages":
                        mc.confirmDialog(m=u'目前只支持sourceimages目录下的缓存更改\n请确定新的目录是否在sourceimages下\n\n请重新输入路径!')
                        break
                    for each in vrProxyNode:
                        proxyName = mc.getAttr('%s.dso' % each)
                        if proxyName:
                            #tmp = os.path.split(proxyName)
                            number = proxyName.index('sourceimages')
                            newProxyPath = os.path.join(root[:-12],proxyName[number::])
                            #newProxyPath = os.path.join(root, tmp[1])
                            if os.path.isfile(newProxyPath):
                                print each, newProxyPath
                                count += 1
                                mc.setAttr('%s.dso' % each, newProxyPath, type='string')
                            else:
                                node.append(each)
                    if count > 0:
                        print u'一共有%d个缓存节点\n' % lenProxyN
                        print u'一共有%d个cacheFile节点缓存路径被替换到%s\n' % (count, root)
                    if count == lenProxyN:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成')
                    elif count == 0:
                        mc.confirmDialog(m=u'全部替换不成功 ,请检查该路径是否存在相应的文件')
                    else:
                        print u'以下的节点缓存节点在新路径找不到:\n'
                        print node
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!\n详细请看脚本编辑器')
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            break
    else:
        mc.confirmDialog(m=u'场景里没有aiStandIn节点...')
'''
选择两个物体,把首选的物体关联复制出来,然后把后选物体的位移信息给到复制物体上
'''
# def copyAndMatchTransformWithSecond():
#     sl = om.MSelectionList()
#     om.MGlobal.getActiveSelectionList(sl)
#     if not sl.length() == 2:
#         om.MGlobal.displayError(u'Please select will be copy Proxy Object First, and select Transform Object last...')
#         return

#     firstDag = om.MDagPath()
#     sl.getDagPath(0, firstDag)
#     firstFn = om.MFnDagNode(firstDag)
#     try:
#         instanceName = mc.instance(firstDag.fullPathName())
#     except:
#         om.MGlobal.displayError('Error in Instanceing First Object...')
#         return

#     instanceDag = OCT_util.nameToDag(instanceName[0])
#     instanceFn = om.MFnTransform(instanceDag)

#     lastDag = om.MDagPath()
#     sl.getDagPath(1, lastDag)
#     lastFn = om.MFnTransform(lastDag)
#     lastMatrix = lastFn.transformation()
#     instanceFn.set(lastMatrix)
#     try:
#         om.MGlobal.deleteNode(lastDag.node())
#     except:
#         om.MGlobal.displayWarning('%s node cannot delete...' % lastDag.fullPathName())
#     else:
#         om.MGlobal.displayInfo('Instance And Match Transform Object Work Complete.')


def CopyCacheFilePath():
    ext = 'xml'
    count = 0
    node = []
    cacheNode = mc.ls(type='cacheFile')
    lenCaches = len(cacheNode)
    dataType = ''
    if lenCaches:
        while True:
            result = mc.promptDialog(t="Enter Cache Dirctroy", m=u'请输入拷贝的目标路径,例如D:\work\Test\data:', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root=mc.promptDialog(q=True,t=True)
                if os.path.isdir(root):
                    if root[-4::]=='data':
                        dataType=root[-4::]
                    else:
                        mc.confirmDialog(m=u'目前只支持data目录下的缓存更改\n请确定新的目录是否在data下\n\n请重新输入路径')
                        break
                        
                    dataTypeLen = len(dataType) 
                    for each in cacheNode:
                        cacheName = mc.getAttr('%s.cacheName' % each)
                        cachePath = mc.getAttr('%s.cachePath' % each)
                        dataAddress = cachePath.find("/%s/" % dataType)
                        newcachePath = cachePath[dataAddress+dataTypeLen+1::]
                        newcachePath = newcachePath.replace("/", "\\")
                        tmp=root+newcachePath
                        if not os.path.isdir(tmp):
                            os.makedirs(tmp)
                        
                        if os.path.isfile(cachePath+"/"+cacheName+"."+ext):
                            allFistList=mc.getFileList(folder=cachePath+"/")
                            count += 1
                            for files in allFistList:
                                
                                try:
                                    shutil.copy2(cachePath+"/"+files,tmp+"\\"+files)
                                except:
                                    print "拷贝缓存出错"
                                    
                            mc.setAttr('%s.cachePath' % each, tmp, type='string')
                        else:
                            node.append(each)
                            
                    if count>0:
                        print u"一共有%d个缓存节点\n"%lenCaches
                        print u'一共有%d个cacheFile节点缓存路径被替换到%s\n'%(count, root)
                    if count == lenCaches:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成')
                    else:
                        print u'以下的节点缓存节点在新路径找不到:\n'
                        print node
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!\n详细请看脚本编辑器')
                    break
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            else:
                break
    else:
        mc.confirmDialog(m=u'场景里没有cacheFile节点...')
        
def YetiCachePath():
    allYetiCacheFiles = mc.ls(type='pgYetiMaya')
    lenYetiCache = len(allYetiCacheFiles)
    count = 0
    if lenYetiCache:
        while True:
            result = mc.promptDialog(t="Enter Proxy Dirctroy", m='Path`s example: D:\work\Test\cache', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root = mc.promptDialog(q=True, t=True)
                if os.path.isdir(root):
                    if root[-5::] != "cache":
                        mc.confirmDialog(m=u'目前只支持cache目录下的缓存更改\n请确定新的目录是否在cache下\n\n请重新输入路径!')
                        break
                    for each in allYetiCacheFiles:
                        YetiCacheNodePath = mc.getAttr('%s.cacheFileName' % each)
                        if YetiCacheNodePath:
                            number = YetiCacheNodePath.index('cache')
                            newYetiCacheNodePath = os.path.join(root[:-5],YetiCacheNodePath[number::])
                            newYetiCacheNodePath = newYetiCacheNodePath.replace('\\', '/')
                            count += 1
                            mc.setAttr('%s.cacheFileName' % each, newYetiCacheNodePath, type='string')

                    if count > 0:
                        print u'一共有%d个缓存节点\n' % lenYetiCache
                        print u'一共有%d个pgYetiMaya节点缓存路径被替换到%s\n' % (count, root)
                    if count == lenYetiCache:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成')
                    elif count == 0:
                        mc.confirmDialog(m=u'全部替换不成功 ,请检查该路径是否存在相应的文件')
                    else:
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!\n详细请看脚本编辑器')
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            break     
    else:
        mc.confirmDialog(m=u'场景里没有pgYetiMaya节点...')


def YetiFilePath():
    allYetiCacheFiles = mc.ls(type='pgYetiMaya')
    lenYetiCache = len(allYetiCacheFiles)
    count = 0
    if lenYetiCache:
        while True:
            result = mc.promptDialog(t="Enter Proxy Dirctroy", m='Path`s example: D:\work\Test\sourceimages', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root = mc.promptDialog(q=True, t=True)
                if os.path.isdir(root):
                    if root[-12::] != "sourceimages":
                        mc.confirmDialog(m=u'目前只支持sourceimages目录下的缓存更改\n请确定新的目录是否在sourceimages下\n\n请重新输入路径!')
                        break
                    for each in allYetiCacheFiles:
                        YetiCacheFilePath = mc.getAttr('%s.imageSearchPath' % each)
                        if YetiCacheFilePath:
                            number = YetiCacheFilePath.index('sourceimages')
                            newYetiCacheNodePath = os.path.join(root[:-12],YetiCacheFilePath[number::])
                            newYetiCacheNodePath = newYetiCacheNodePath.replace('\\', '/')
                            count += 1
                            mc.setAttr('%s.imageSearchPath' % each, newYetiCacheNodePath, type='string')

                    if count > 0:
                        print u'一共有%d个缓存节点\n' % lenYetiCache
                        print u'一共有%d个pgYetiMaya节点缓存路径被替换到%s\n' % (count, root)
                    if count == lenYetiCache:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成')
                    elif count == 0:
                        mc.confirmDialog(m=u'全部替换不成功 ,请检查该路径是否存在相应的文件')
                    else:
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!\n详细请看脚本编辑器')
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            break     
    else:
        mc.confirmDialog(m=u'场景里没有pgYetiMaya节点...')

def VRayLightIESShapePath():
    allVRayLightIESShape = mc.ls(type='VRayLightIESShape')

    lenVRayLightIESShape = len(allVRayLightIESShape)
    count = 0
    if lenVRayLightIESShape:
        while True:
            result = mc.promptDialog(t="Enter Proxy Dirctroy", m='Path`s example: D:\work\Test\sourceimages', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
            if result == 'OK':
                root = mc.promptDialog(q=True, t=True)
                if os.path.isdir(root):
                    for each in allVRayLightIESShape:
                        VRayLightIESShapePath = mc.getAttr('%s.iesFile' % each)
                        if VRayLightIESShapePath:
                            LightIESName = os.path.basename(VRayLightIESShapePath)
                            newVRayLightIESShapePath = os.path.join(root,LightIESName)
                            newVRayLightIESShapePath = newVRayLightIESShapePath.replace('\\', '/')
                            count += 1
                            mc.setAttr('%s.iesFile' % each, newVRayLightIESShapePath, type='string')

                    if count > 0:
                        print u'一共有%d个缓存节点\n' % lenVRayLightIESShape
                        print u'一共有%d个VRayLightIESShape节点缓存路径被替换到%s\n' % (count, root)
                    if count == lenVRayLightIESShape:
                        mc.confirmDialog(m=u'所有缓存节点已替换完成')
                    elif count == 0:
                        mc.confirmDialog(m=u'全部替换不成功 ,请检查该路径是否存在相应的文件')
                    else:
                        mc.confirmDialog(m=u'有某些缓存节点在新的路径找不到!\n详细请看脚本编辑器')
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
            break     
    else:
        mc.confirmDialog(m=u'场景里没有VRayLightIESShape节点...')


def delNurbsCurve():
    allNurbsCurve=mc.ls(selection=True, dagObjects=True, ni=True, shapes=True, rq=True)
    if allNurbsCurve:
        for i in allNurbsCurve:
            if mc.objectType(i)=='nurbsCurve':
                mc.delete(i)
    else:
        allNurbsCurve=mc.ls(type='nurbsCurve')
        for i in allNurbsCurve:
            mc.delete(i)
        

