# -*- coding: utf-8 -*-
__author__ = 'zhongwzh'
import maya.cmds as mc
import maya.mel as mm
import os
import re
import time

myGeoObject_zwz = []
def OCT_CreateGeometryCache_Menum_zwz():
    global myGeoObject_zwz
    myGeoObject_zwz = []
    if mc.windowPref('OCT_CreateGeometryCache_zwz', exists=True):
        myGeoObject_zwz = []
        mc.windowPref('OCT_CreateGeometryCache_zwz', remove=True)
    if mc.window('OCT_CreateGeometryCache_zwz', exists=True):
        myGeoObject_zwz = []
        mc.deleteUI('OCT_CreateGeometryCache_zwz', window=True)

    mc.window("OCT_CreateGeometryCache_zwz", title=u"OCT_CreateGeometryCache_zwz", menuBar=True, widthHeight=(220, 240), resizeToFitChildren=True, sizeable=True)
    mc.formLayout('formLyt', numberOfDivisions=100)

    one = mc.columnLayout('First_Set', parent='formLyt')
    mc.button('AddObjectToList', label=u'把选择的物体添加到列表中(模式一)', w=220, h=25, command='OCT_anim.OCT_CreateGeometryCache_zwz.AddGroupbySelect_zwz()', backgroundColor=(0.9, 0.5, 0), annotation=u"请框选物体", parent='First_Set')
    mc.button('AddSetToList', label=u'把参考Set里的物体导入列表中（模式二）', w=220, h=25, command='OCT_anim.OCT_CreateGeometryCache_zwz.AddGroupbySets_zwz()', backgroundColor=(0.2, 0.5, 0), parent='First_Set')

    two = mc.frameLayout('Objects_Set', label=u'将以列表中的物体创建GeoChae', labelAlign='top', borderStyle='etchedOut', w=220, h=100, parent='formLyt')
    mc.textScrollList('selectObjects', allowMultiSelection=True, h=70, sc='OCT_anim.OCT_CreateGeometryCache_zwz.lsGeoObjectGroup_zwz()', parent='Objects_Set')

    three = mc.columnLayout('GeoButton_Set', parent='formLyt')
    mc.button('clearObjects', label=u'删除选中列表', width=220, command='OCT_anim.OCT_CreateGeometryCache_zwz.deleteNumList_zwz()', backgroundColor=(0.9, 0.3, 0.3), parent='GeoButton_Set')
    mc.button('CreateGeoCache', label=u'按列表顺序创建物体的Geometry Cache', width=220, h=30, command='OCT_anim.OCT_CreateGeometryCache_zwz.CreateGeometryCache_zwz()', backgroundColor=(0.2, 0.8, 0.3), parent='GeoButton_Set')
    mc.formLayout('formLyt', e=True,
                  attachForm=[(one, 'top', 5), (one, 'left', 15), (two, 'right', 5), (two, 'left', 5), (two, 'top', 55), (three, 'left', 5), (three, 'bottom', 5)],
                  attachControl=[(two, 'bottom', 1, three)],
                  attachNone=[(three, 'top')],
                  attachPosition=[(one, 'left', 2, 1), (one, 'top', 0, 0)])
    mc.showWindow('OCT_CreateGeometryCache_zwz')


def AddGroupbySelect_zwz():
    global myGeoObject_zwz
    usrsName=os.getenv('username')
    mc.button('AddSetToList', e=True, en=False)
    nummyGeo = len(myGeoObject_zwz)
    allMyShapes = []
    allShapes = mc.ls(selection=True, dagObjects=True, shapes=True, ni=True,ap=True)
    numList = mc.textScrollList('selectObjects', q=True, ni=True)
    for Shape in allShapes:
        if nummyGeo:
            for i in range(0, nummyGeo):
                if Shape in myGeoObject_zwz[i]:
                    mc.confirmDialog(title=u'温馨提示', message=u'选择的某个物体已经存在某个组中，请不要重复选择！', button=['OK'], defaultButton='Yes', dismissString='No')
                    return
        ShapeType = mc.nodeType(Shape)
        if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
            allMyShapes.append(Shape)
    if len(allMyShapes) == 0:
        mc.confirmDialog(title=u'温馨提示', message=u'选择的组或者物体不含有模型\n请重新选择！', button=['OK'], defaultButton='Yes', dismissString='No')
    else:
        #解决分开创建物体是会出现同名的物体，上传文件的时候会覆盖
        ISOTIMEFORMAT='%Y%m%d%H%M%S'
        CreateTime=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        mc.textScrollList('selectObjects', e=True, append='ch%sGeoCache%s%s' %(usrsName,numList,CreateTime))
        myGeoObject_zwz.append(allMyShapes)


def AddGroupbySets_zwz():
    global myGeoObject_zwz
    myGeoObject_zwz = []
    mc.textScrollList('selectObjects', e=True, ra=True)
    mc.button('AddObjectToList', e=True, en=False)
    allMySets = []
    myRfs = mc.ls(rf=True, l=True)
    if len(myRfs):
        for myRf in myRfs:
            mySets = []
            myRfNodes = mc.referenceQuery(myRf, nodes=True)
            myChilsRfN = mc.ls(myRfNodes, rf=True)
            if not myChilsRfN:
                myNameSpace = mc.referenceQuery(myRf, namespace=True, shortName=True)
                temp = re.search("_.*", myNameSpace)
                if temp:
                    myNameSpace = temp.group()[1::]
                mySetsTmp = mc.ls(myRfNodes, type='objectSet', l=True)
                for seach in mySetsTmp:
                    if seach.find(':CACHE_OBJS') >= 0:
                        mySets.append(seach)
                #一个参考节点只能有一个set
                numMyset = len(mySets)
                if numMyset == 1:
                    Objects = mc.sets(mySets[0], q=True, no=True)
                    allShapes = mc.ls(Objects, dagObjects=True, shapes=True, ap=True)
                    mySetObjects = []
                    for Shape in allShapes:
                        ShapeType = mc.nodeType(Shape)
                        if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
                            if not mc.getAttr("%s.intermediateObject" % Shape):
                                mySetObjects.append(Shape)
                    tmp = [myNameSpace, mySetObjects]
                    allMySets.append(tmp)
                elif numMyset == 0:
                    mc.confirmDialog(title=u'温馨提示', message=u'%s 参考节点没有命名为CACHE_OBJS的set节点' % myRf, button=['OK'], defaultButton='Yes', dismissString='No')
                    break
                else:
                    mc.confirmDialog(title=u'温馨提示', message=u'%s 一个参考节点只能有一个set' % mySets[0], button=['OK'], defaultButton='Yes', dismissString='No')
                    break
            else:
                mc.confirmDialog(title=u'温馨提示', message=u'%s 含有二次参考的节点\n请处理完再加载!' % myRf, button=['OK'], defaultButton='Yes', dismissString='No')
                break
        #添加cache到列表中
        if len(allMySets) == 0:
            mc.confirmDialog(title=u'温馨提示', message=u'参考节点不含有sets节点', button=['OK'], defaultButton='Yes', dismissString='No')
        else:
            for each in allMySets:
                mc.textScrollList('selectObjects', e=True, append='%s' % each[0])
                myGeoObject_zwz.append(each[1])
    else:
        mc.confirmDialog(title=u'温馨提示', message=u'节点中不含有任何参考节点', button=['OK'], defaultButton='Yes', dismissString='No')


def lsGeoObjectGroup_zwz():
    numLs = mc.textScrollList('selectObjects', q=True, sii=True)
    if numLs:
        for i, each in enumerate(numLs):
            if i == 0:
                mc.select(myGeoObject_zwz[each-1])
            else:
                mc.select(myGeoObject_zwz[each-1], add=True)


def deleteNumList_zwz():
    numLs = mc.textScrollList('selectObjects', q=True, sii=True)
    if numLs:
        numList = mc.textScrollList('selectObjects', q=True, ni=True)
        j = 0
        for each in numLs:
            myGeoObject_zwz.remove(myGeoObject_zwz[each-j-1])
            if mc.button('AddSetToList', q=True, en=True):
                mc.textScrollList('selectObjects', e=True, rii=each-j)
            if mc.button('AddObjectToList', q=True, en=True):
                mc.textScrollList('selectObjects', e=True, ra=True)
                if numList >= 2:
                    for i in range(len(myGeoObject_zwz)):
                        mc.textScrollList('selectObjects', e=True, append='chMyGeoCache%s' % i)
            j = j+1
        mc.select(cl=True)


def CreateGeometryCache_zwz():
    myStartFrameV = mc.playbackOptions(q=True, min=True)
    myEndFrameV = mc.playbackOptions(q=True, max=True)
    num_myGeoObject_zwz = len(myGeoObject_zwz)
    #获取激活视面
    if num_myGeoObject_zwz:
        mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
        activePlane = ''
        i = 1
        while(i):
            try:
                tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
            except:
                pass
            else:
                if tmp:
                    activePlane = 'modelPanel%d' % i
                    break
            i += 1
        mc.modelEditor(activePlane, e=True, polymeshes=False, nurbsSurfaces=False)
        myfileName = mc.file(q=True, sn=True, shortName=True).split('.')[0]
        mydataName = mc.workspace(en='data/%s/' % myfileName)
        ErrorObjects = []
        amount = 0
        mc.progressWindow(title=u'动画缓存创建,一共有%s个' % num_myGeoObject_zwz, progress=amount, status='chMyGeoCache', min=0, max=num_myGeoObject_zwz, isInterruptable=True)
        allcacheNames = mc.textScrollList('selectObjects', q=True, ai=True)
        for i, each in enumerate(myGeoObject_zwz):
            if len(each):
                cacheName = allcacheNames[i]
                mc.progressWindow(e=True, status=u'第%s个: %s' % (i, cacheName), progress=i)
                mc.select(cl=True)
                mc.select(myGeoObject_zwz[i], r=True)
                mm.eval("SelectIsolate;")
                j = 1
                while(True):
                    if os.path.isdir(mydataName+cacheName):
                        if os.path.isdir(mydataName+cacheName+'_'+'%s' % j):
                            j = j+1
                        else:
                            cacheName = cacheName+'_'+'%s' % j
                            break
                    else:
                        break
                cacheFiles = mc.cacheFile(r=True, sch=True, dtf=True, fm='OneFilePerFrame', spm=1, smr=1, directory=mydataName + cacheName, fileName=cacheName, st=myStartFrameV, et=myEndFrameV, points=each)
                if mc.progressWindow(q=True, isCancelled=True) or mc.progressWindow(q=True, progress=True) > num_myGeoObject_zwz:
                    mc.progressWindow(endProgress=True)
                    mc.confirmDialog(title=u'温馨提示', message=u'到第%s个: %s就停了' % (i, cacheName), button=['OK'], defaultButton='Yes', dismissString='No')
                    return
                mc.delete(each, ch=True)
                myswichNode = []
                myswichList = []
                myNewcacheObjects = []
                switchText = ''
                for peach in each:
                    try:
                        switch = mm.eval('createHistorySwitch("%s", false)' % peach)
                    except:
                        ErrorObjects.append(peach)
                        print peach
                    else:
                        myNewcacheObjects.append(peach)
                        myswichNode.append(switch)
                        switchText = '%s.inp[0]' % switch
                        myswichList.append(switchText)
                mc.cacheFile(f=cacheName, directory=mydataName+cacheName, cnm=myNewcacheObjects, ia=myswichList, attachFile=True)
                for seach in myswichNode:
                    mc.setAttr('%s.playFromCache' % seach, 1)
                mc.select(cl=True)
        mc.progressWindow(endProgress=True)
        mc.isolateSelect(activePlane, state=False)
        mc.modelEditor(activePlane, e=True, polymeshes=True, nurbsSurfaces=True)
        if ErrorObjects:
            print (u'以下shapes不能创建缓存:\n %s' % ErrorObjects)
        print u'全部创建完成'
