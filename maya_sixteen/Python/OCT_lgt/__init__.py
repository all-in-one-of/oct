#!/usr/bin/env python
# -*- coding: utf-8 -*-



from __future__ import with_statement #only needed for maya 2008 & 2009

import sys, os
import maya.cmds as mc
import maya.mel as mm
import maya.utils
import maya.OpenMaya as om
import string
import math
import OCT_SelectTransparency
import threading
from OCT_aiPhotometricLightMap_Tools import aiPhotomeLightFile_Tools
#import LightLinkTool

# def llCleanUp():
#     mm.eval("IC_LightLinksCleanUp")
#	LightLinkTool.loadUI()

from OCT_edit_vrayZDepth import edit_vrayZDepth


def changePointLight():
    selectObj = mc.ls(sl=True, l=True)
    for lightName in selectObj:
        mc.select(lightName)
        pos_t = mc.xform(q=True, ws=True, t=True)
        mc.delete(lightName)
        mc.pointLight(pos=pos_t, d=2)

def selectTypeLight():
    import OCT_SelectTypeLight
    OCT_SelectTypeLight.main()

def arnoldStandInMast():
    import OCT_ArnoldStandInMast
    i = OCT_ArnoldStandInMast.ArnoldStandInMast()
    i.show()
   
def lightLibrary():
    import OCT_LightLibrary
    path = r'\\octvision.com\CG\Tech\lightLib\ligthIESFile.xml'
    lightLib = OCT_LightLibrary.OCT_LightLibrary(path)
    lightLib.show()

#灯光属性的随机值
def lightAttrRan():
    import OCT_LightAttrRandom
    i = OCT_LightAttrRandom.lightRandom()
    i.show()

#删除多余的灯光衰减节点
def deleteUnuseLightDecay():
    allLightDecay = mc.ls(type = 'aiLightDecay')
    for lgD in allLightDecay:
        con = mc.listConnections(lgD)
        if len(con)<=1 and con[0] == "defaultRenderUtilityList1":
            mc.delete(lgD)
        elif len(con)<1:
            mc.delete(lgD)

def OCT_MasK_Tools():
    import OCT_MasK_Tool
    i = OCT_MasK_Tool.OCT_MasK_Tool()
    i.OCT_MasK_Tool_UI()

#def SelectAreaLight():
#    mc.select(d = True)
#    allAreaLight = mc.ls(type = "areaLight")
#    for area in allAreaLight:
#        trans = mc.listRelatives(area, p = True, f= True)
#        mc.select(trans[0], add = True)
#def selectPointLight():
#    mc.select(d = True)
#    allPointLight = mc.ls(type = "pointLight")
#    for area in allPointLight:
#        trans = mc.listRelatives(area, p = True, f= True)
#        mc.select(trans[0], add = True)

#def SelectSpotLight():
#    mc.select(d = True)
#    allSpotLight = mc.ls(type = "spotLight")
#    for area in allSpotLight:
#        trans = mc.listRelatives(area, p = True, f= True)
#        mc.select(trans[0], add = True)

def run_PhotometricLightMap_Tools():
    if mc.window("LightPathDialog", exists=True):
        mc.deleteUI("LightPathDialog", window=True)
    dialog = aiPhotomeLightFile_Tools()
    t = threading.Thread(None, dialog.show())
    t.start()

def giveNewMaterial():
    import OCT_GiveNewMaterial
    i = OCT_GiveNewMaterial.GetObjectNewMaterial()
    i.getAllMaterial()

def Ar_Occ_Layers():
    import OCT_AR_Occ_Layers
    i=OCT_AR_Occ_Layers.OCT_Ar_Occ_Layers()
    i.LS_All_Material()

def sur_Occ_Layers():
    import OCT_Sur_Occ_Layers
    i=OCT_Sur_Occ_Layers.OCT_Sur_Occ_Layers()
    i.LS_All_Material()

def updateShaver():
    import OCT_UpateShaveAttr
    OCT_UpateShaveAttr.update_Shaver_Attr_UI()

def ChangeShader_YH():
    import OCT_ChangeShaderAttr_YH
    OCT_ChangeShaderAttr_YH.ChangeMayaShderAttr_YH()
    mm.eval("shaderMultiEditOverrideUI()")

#把低摸参考改成高模参考
def ChangeHReference_YH():
    import OCT_ChangeHReference_YH
    i = OCT_ChangeHReference_YH.renameReferenceFile()
    i.renameReferenceFileUI()

#检查arnold非代理文件并拷贝文件
def CheckArnoldProxy_YH(n):
    import OCT_CheckArnoldProxy_YH
    i=OCT_CheckArnoldProxy_YH.checkArnoldProxy_YH()
    if n == 1:
        i.arnoldProxy()
    elif n == 2:
        i.arnoldProxyNew()
        
#改变灯光属性
def ChangeAttr_YH():
    import OCT_ChangeLightAttr_YH
    OCT_ChangeLightAttr_YH.ChangeMayaLightAttr_YH()
    mm.eval("changeAttrWithIncrement()")

#材质互换
#def ChangeMaterial_YH():
   # import OCT_MaterialChange_YH
    #i=OCT_MaterialChange_YH.materialChange()
    #i.materialChangeUI()

#arnold圆滑开关批处理
def ArnoldProduction_YH():
    import OCT_ArnoldProduction_YH
    i=OCT_ArnoldProduction_YH.ArnoldProduction()
    i.arnoldProductionUI()
#转换贴图格式
def ConvertTexFormat_YH():
    import OCT_ConvertTexFormat_YH
    i=OCT_ConvertTexFormat_YH.OCT_convertTexFormat()
    i.OCT_convertTexFormatUI()

#vray与arnold代理转换
def VrayArnoldProxyChange():
    import OCT_ProxyChange_YH
    i=OCT_ProxyChange_YH.ProxyChange()
    i.ProxyChangeUI()

def changenNetworkPaths():
    import OCT_ChangePath
    i=OCT_ChangePath.changenNetworkPath()
    i.changenNetworkPathUI()

def changeShaveName():
    import OCT_changeShaveName
    i=OCT_changeShaveName.changeShaveName()
    i.shaveReName()

def FindVrayProxys():
    import OCT_FindVrayProxys
    i=OCT_FindVrayProxys.findVrayProxys()
    i.findVrayProxysUI()

def changeFrameRate():
    import OCT_ChangeFrameRate
    i=OCT_ChangeFrameRate.OCT_ChangeFrameRate()
    i.frameRate()

##########################################################
###  OCT_导材质工具  ###
##########################################################
def OCT_exShader():
    if mc.windowPref("OCT_exShaderWindow",exists=True):
        mc.windowPref("OCT_exShaderWindow",remove=True)

    if mc.window('OCT_exShaderWindow',ex=True):
        mc.deleteUI('OCT_exShaderWindow',window=True)

    mc.window('OCT_exShaderWindow',t=u'OCT_替换材质工具',wh=[200,230],s=False,mnb=False,mxb=False,rtf=True,menuBar=True)
    mc.menu(l=u'帮助',tearOff=False)
    mc.menuItem(l=u'帮助',c='OCT_lgt.exShaderHelp()')
    mc.menuItem(l=u'关于',c='OCT_lgt.exShaderAbout()')
    col = mc.columnLayout(cat=["both",5],rs=5,cw=200,w=200,h=230,cal='center')
    mc.rowLayout(numberOfColumns=1,cw1=200,w=200,h=30,rowAttach=[1,'top',10],\
                 cat=[1,'left',60])
    mc.text('firstLbl',label=u'1.导出材质',font='fixedWidthFont')
    mc.setParent('..')
    mc.radioButtonGrp('expMode',nrb=2,sl=1,l1=u'已选',l2=u'全部',cw2=[75,75],\
                      ct2=['left','left'],co2=[30,30])
    mc.button('expBtn',l=u'导出',c='OCT_lgt.outputShader()')

    mc.rowLayout(numberOfColumns=1,cw1=200,w=200,h=30,rowAttach=[1,'top',10],\
                 cat=[1,'left',10])
    mc.text('secondLbl',label=u'2.打开将要导入材质的模型文件',font='fixedWidthFont')
    mc.setParent('..')
    mc.text('secondMsgLbl',label=u'请确保导出材质所属的模型的名字\n与当前场景的相对应的模型名字一致')


    mc.rowLayout(numberOfColumns=1,cw1=200,w=200,h=30,rowAttach=[1,'top',10],\
                 cat=[1,'left',60])
    mc.text('secondLbl',label=u'3.替换材质',font='fixedWidthFont')
    mc.setParent('..')
    mc.button('impBtn',l=u'替换',c='OCT_lgt.inputShader()')

    mc.showWindow('OCT_exShaderWindow')


def outputShader():
    mode = mc.radioButtonGrp('expMode',q=True,select=True)

    selShader = []
    if mode == 1:
        selObj = mc.ls(sl=True,long=True)
        if len(selObj) == 0:
            om.MGlobal.displayWarning(u'请选择要进行导出的模型或者表面材质球...\n')
            return

        for eachObj in selObj:
            if mc.nodeType(eachObj) == 'transform':
                shape = mc.listRelatives(eachObj,shapes=True,f=True)
                if not shape == None:
                    for eachShape in shape:
                        sgList = mc.listConnections(eachShape,type='shadingEngine',source=False,d=True)
                        if not sgList == None:
                            for eachSg in sgList:
                                eachShd = mc.listConnections(eachSg+'.ss',d=True)
                                if not eachShd == None:
                                    if mc.getClassification(mc.nodeType(eachShd[0]),satisfies='shader/surface'):
                                        if selShader.count(eachShd[0]) == 0:
                                            if not eachShd[0] == 'lambert1':
                                                selShader.append(eachShd[0])
            elif mc.getClassification(mc.nodeType(eachObj),satisfies='shader/surface'):
                if selShader.count(eachObj) == 0:
                    if not eachObj == 'lambert1':
                        selShader.append(eachObj)
            else:
                om.MGlobal.displayWarning(u'%s 节点不是此工具操作允许的类型,请选择模型或者表面材质节点,忽略此物体...\n' % eachObj)			
    elif mode == 2:
        allShader = mc.ls(materials=True)
        #allShader.remove(u'lambert1')
        #allShader.remove(u'particleCloud1')
        #allShader.remove(u'shaderGlow1')
        for eachShader in allShader:
            if mc.getClassification(mc.nodeType(eachShader),satisfies='shader/surface'):
                if not eachShader == 'lambert1':
                    selShader.append(eachShader)

    allOutputStr = []
    shd = []
    sg = []


    count = len(selShader)

    if count == 0:
        return

    mc.progressWindow(title=u"导出材质",progress=0,min=0,max=count,status=u"完成:0/%d" % count,isInterruptable=True)

    i = 1
    for eachSel in selShader:
        if mc.progressWindow(query=True,isCancelled=True):
            break

        outputStr = []
        nType = mc.nodeType(eachSel)
        if mc.getClassification(nType,satisfies='shader/surface'):
            parentNode = mc.listConnections(eachSel+'.outColor',s=True)
            if not mc.nodeType(parentNode) == 'shadingEngine':
                i += 1
                continue

            try:
                mc.hyperShade(objects=eachSel)
            except:
                om.MGlobal.displayWarning(u'%s材质获取物体时出错,忽略此节点...\n' % eachSel)
                mc.progressWindow(e=True,progress=i,status=u'完成:%d/%d' % (i,count))
                i += 1
                continue

            objList = mc.ls(sl=True,long=True)
            if len(objList):
                eachSg = mc.listConnections(eachSel+'.outColor',s=True)
                #attr = ['.ss','.ds','.vs']
                #for eachAttr in attr:
                    #subShd = mc.listConnections(eachSg[0]+eachAttr,d=True)

                    #if not subShd == None:
                        #shd.append(subShd[0])

                sg.append(eachSg[0])
                outputStr.append('###\r\n')
                outputStr.append(eachSel+'\r\n')
                for eachObj in objList:
                    outputStr.append(eachObj+'\r\n')

                #if not i == count:
                outputStr.append('\r\n')

            allOutputStr += outputStr
            del outputStr


        mc.progressWindow(e=True,progress=i,status=u'完成:%d/%d' % (i,count))
        i += 1

    mc.progressWindow(endProgress=True)

    tempFolder = os.getenv('TMP')

    outputShaderName = 'OCT_outShader'
    shaderFullPath = os.path.join(tempFolder,outputShaderName+'.mb')
    if not len(sg) == 0:
        mc.select(sg,r=True,ne=True)
        mc.file(shaderFullPath,op="v=0",typ="mayaBinary",pr=True,es=True,f=True)

    outputFileName = 'OCT_outShader.txt'
    fullPath = os.path.join(tempFolder,outputFileName)
    f = file(fullPath,'w')
    f.writelines(allOutputStr)
    f.close()
    del f


def inputShader():
    tempFolder = os.getenv('TMP')

    outputFileName = 'OCT_outShader.txt'
    fullPath = os.path.join(tempFolder,outputFileName)
    if not os.path.isfile(fullPath):
        om.MGlobal.displayError(u'没有找到导出的材质数据...\n')
        return

    try:
        f = file(fullPath,'r')
    except:
        om.MGlobal.displayError(u'打开材质数据时出错...\n')
        return

    found = 0
    obj = []
    shd = ''
    sg = ''
    useNS = 1
    allStr = f.readlines()
    f.close()
    del f

    if len(allStr) < 3:
        om.MGlobal.displayWarning(u'材质数据文件为空,停止导入操作...\n' % obj)
        return

    outputShaderName = 'OCT_outShader'
    shaderFullPath = os.path.join(tempFolder,outputShaderName+'.mb')
    if not os.path.isfile(shaderFullPath):
        om.MGlobal.displayError(u'没有找到导出的材质文件...\n')
        return

    mc.file(shaderFullPath,i=True,type="mayaBinary",ra=True,namespace=outputShaderName,options="v=0",pr=True,loadReferenceDepth="all")
    #try:
        #removeNS(outputShaderName)
    #except:
        #useNS = 1

    count = allStr.count('###\r\n')
    i = 0
    mc.progressWindow(title=u"导入材质",progress=0,min=0,max=count,status=u"完成:0/%d" % count,isInterruptable=True)
    for eachStr in allStr:
        if mc.progressWindow(query=True,isCancelled=True):
            break

        if eachStr == '\r\n':
            found = 0
            i += 1
            if not shd == '' and len(obj) > 0:
                try:
                    mc.select(obj,r=True)
                except:
                    om.MGlobal.displayWarning(u'场景中没有 %s 物体...\n' % obj)
                    continue

                try:
                    mc.sets(e=True,forceElement=sg[0])
                except:
                    om.MGlobal.displayWarning(u'物体附予 %s 材质时出错,忽略此物体...\n' % shd)

            mc.progressWindow(e=True,progress=i,status=u'完成:%d/%d' % (i,count))
            continue

        if eachStr == '###\r\n':
            found = 1
            del obj[:]
            shd = ''
            sg = ''
            continue
        else:
            if found == 1:
                if useNS == 1:
                    shd = outputShaderName + ':' + eachStr[:len(eachStr)-2]
                else:
                    shd = eachStr[:len(eachStr)-2]
                found = 2
                try:
                    sg = mc.listConnections(shd+'.outColor',s=True)
                except:
                    sgName = mc.sets(renderable=True,noSurfaceShader=True,empty=True,name=shd+'SG')
                    mc.connectAttr(shd+'.outColor',sgName+'.surfaceShader',f=True)
                    sg[0] = sgName
                    #om.MGlobal.displayWarning(u'%s 材质没有ShadingGroup节点...' % shd)
            elif found == 2:
                obj.append(eachStr[:len(eachStr)-2])


    removeNS(outputShaderName)
    mc.select(cl=True)
    mc.progressWindow(endProgress=True)


def removeNS(str):
    eachSel = str
    mc.namespace(set=':')
    allName = [eachSel]
    mc.namespace(set=eachSel)	
    while mc.namespaceInfo(p=1) != ":":
        parentName = mc.namespaceInfo(p=1)
        allName.append(parentName)
        mc.namespace(set=':')
        mc.namespace(set=parentName)	

    mc.namespace(set=':')
    for eachName in allName:
        mc.namespace(f=1,mv=(eachName,":"))
        mc.namespace(rm=eachName)


def exShaderHelp():
    if mc.windowPref("OCT_exShaderHelpWindow",exists=True):
        mc.windowPref("OCT_exShaderHelpWindow",remove=True)

    if mc.window('OCT_exShaderHelpWindow',ex=True):
        mc.deleteUI('OCT_exShaderHelpWindow',window=True)

    msg = u'使用方法:\n'
    msg += u'1.打开你需要替换的源材质的场景文件.\n'
    msg += u'2.确定是以选择的物体导出还是所有的表面材质导出,以选择的物体导出的话,那请选择将要导出的模型或表面材质.\n'
    msg += u'3.点击导出按钮.\n'
    msg += u'4.打开需要替换的场景文件.\n'
    msg += u'5.确保将要被替换的模型和源模型的名字完全一致,包括层级关系.\n'
    msg += u'6.点击替换按钮.\n'
    msg += u'7.等待完成.\n'
    msg += u'8.请检查是否正确.\n'
    msg += u'注意事项:\n'
    msg += u'1.使用方法第二步里,如果是所有表面材质导出的话,请耐心等候.\n'
    msg += u'2.完成替换后,如果不正确或者出现警告信息,那请重新打开文件,把所有的渲染层删除掉,再替换一次,这是因为文件本身有问题\n'
    msg += u'3.如果还是有问题,请找工具编写者解决.\n'
    msg += u'\n程序:ivancheung7@gmail.com\n'
    mc.window('OCT_exShaderHelpWindow',t=u'帮助',wh=[320,400],s=False)
    mc.columnLayout()
    mc.scrollField(wordWrap=True,editable=False,tx=msg,w=300,h=360,fn='fixedWidthFont')
    mc.showWindow('OCT_exShaderHelpWindow')

def exShaderAbout():
    return
##########################################################


#########################################################
##UI元素:
##1.列表,可多选,区分相同材质和无用材质
##2.清理材质按钮,合并材质按钮,以材质选择物体按钮
##程序:
##1.列出shadingGroup
##2.列出每个shadingGroup的surface shader
##3.检查surface shader 是否有附属模型
##4.如果没有附属模型的话,从shadingGroup列表中删除并且记录为空材质
##5.以表面材质类别分类
##6.比较shader
##7.如果一样,则记录下来
##
#########################################################    
def cleanMatUI():
    if mc.window('cleanMatUI', exists=True):
        mc.deleteUI('cleanMatUI', window=True)

    if mc.windowPref('cleanMatUI', exists=True):
        mc.windowPref('cleanMatUI', remove=True)

    mc.window('cleanMatUI', t='Clean Material Tool', wh=[520, 272], mnb=True, mxb=True, rtf=True, menuBar=True)
    mc.menu(l=u'帮助',tearOff=False)
    mc.menuItem(l=u'帮助', c='OCT_lgt.cleanMatHelp()')
    mc.menuItem(l=u'关于')
    mc.formLayout('formLyt', numberOfDivisions=100)
    mc.textScrollList('sameList', nr=10, ams=True, h=160, w=148, parent='formLyt', dcc='OCT_lgt.sameList_dcc()')
    mc.textScrollList('unList', nr=10, ams=True, h=160, w=148, parent='formLyt', dcc='OCT_lgt.unList_dcc()')
    mc.button('refBtn', l='Refresh All', w=408, parent='formLyt', c='OCT_lgt.cleanMatCheck("all")')
    mc.button('closeBtn', l='Close', width=408, parent='formLyt', c='mc.deleteUI("cleanMatUI",window=True)')
    mc.columnLayout('sameBtn', cal='center',h=160, rs=30, parent='formLyt')
    mc.button('cleanSel', w=48, l='Clean Sel', parent='sameBtn', c='OCT_lgt.cleanMat("same","sel")')
    mc.button('cleanAll', w=48, l='Clean All', parent='sameBtn', c='OCT_lgt.cleanMat("same","all")')
    mc.button('refresh1', w=48, l='Refresh', parent='sameBtn', c='OCT_lgt.cleanMatCheck("same")')
    mc.columnLayout('unBtn', cal='center',h=160, rs=30, parent='formLyt')
    mc.button('delSel2', l='Del Sel', w=48, parent='unBtn', c='OCT_lgt.cleanMat("unused","sel")')
    mc.button('delAll2', l='Del All', w=48, parent='unBtn', c='OCT_lgt.cleanMat("unused","all")')
    mc.button('refresh2', l='Refresh', w=48, parent='unBtn', c='OCT_lgt.cleanMatCheck("unUsed")')

    mc.formLayout('formLyt', e=True, \
                  attachNone=( ['sameBtn', 'left'], ['refBtn', 'top'], ['closeBtn', 'top'], ['unBtn', 'left'] ), \
                  attachForm=( ['sameList', 'left', 5], ['sameList', 'top', 5], ['sameBtn','top',30], ['unList', 'top', 5], ['unBtn', 'top', 30], ['unBtn', 'right', 5], ['refBtn', 'left', 5], ['refBtn', 'right', 5], ['closeBtn', 'left', 5], ['closeBtn', 'bottom', 5], ['closeBtn', 'right', 5] ), \
                  attachControl=( ['sameList', 'bottom', 5, 'refBtn'], ['sameList', 'right', 5, 'sameBtn'], ['sameBtn', 'bottom', 5, 'refBtn'], ['unList', 'bottom', 5, 'refBtn'], ['unList', 'right', 5, 'unBtn'], ['unBtn', 'bottom', 5, 'refBtn'], ['refBtn', 'bottom', 5, 'closeBtn'] ), \
                  attachPosition=( ['sameBtn', 'right', 5, 50], ['unList', 'left', 0, 50] ) )

    mc.showWindow('cleanMatUI')


def cleanMatCheck(category):
    shaderType = []
    del shaderType[:]

    unusedSG = []
    del unusedSG[:]

    classify = dict()
    classify.clear()

    allSG = mc.ls(type='shadingEngine')

    for eachSG in allSG:
        shader = mc.listConnections(eachSG, d=False, s=True)
        if shader == None:
            continue

        if len(shader):
            for eachShader in shader:
                shaderNodeType = mc.nodeType(eachShader)
                if mc.getClassification(shaderNodeType, satisfies='shader/surface'):
                    mc.hyperShade(objects=eachShader)
                    if not len(mc.ls(sl=True)):
                        unusedSG.append(eachSG)
                    else:
                        if not shaderNodeType in shaderType:
                            shaderType.append(shaderNodeType)

                        if classify.has_key(shaderNodeType):
                            keyValues = classify[shaderNodeType]
                            keyValues.append(eachSG)
                            classify[shaderNodeType] = keyValues
                        else:
                            classify[shaderNodeType] = [eachSG]

                    break
        else:
            print ('%s have no Shader...' % eachSG)

    sameTup = []
    if category == 'same' or category == 'all':
        for k, v in classify.iteritems():
            row = v
            column = v
            #all = v
            for eachRow in row:
                tempSameList = [eachRow]

                for eachColumn in column:
                    if not eachRow == eachColumn:
                        shaderCompare = mc.shadingNetworkCompare(eachRow, eachColumn)
                        if mc.shadingNetworkCompare(shaderCompare,q=True,eq=True):
                            #all.remove(eachColumn)
                            tempSameList.append(eachColumn)

                        mc.shadingNetworkCompare(shaderCompare, delete=True)


                if len(tempSameList) > 1:
                    state = False
                    for eachSame in sameTup:
                        if tempSameList[0] in eachSame:
                            state = True

                    if not state:
                        sameTup.append(tempSameList)

    #print sameTup

    if category == 'unUsed':
        mc.textScrollList('unList', removeAll=True, e=True)
        for eachUn in unusedSG:
            mc.textScrollList('unList', e=True, append=eachUn) 
    elif category == 'same':
        mc.textScrollList('sameList',  removeAll=True, e=True)
        for eachSame in sameTup:
            if len(eachSame):
                for eachSame2 in eachSame:
                    #print eachSame2
                    mc.textScrollList('sameList', e=True, append=eachSame2)

                mc.textScrollList('sameList', e=True, append='')
    else:
        mc.textScrollList('unList', e=True, removeAll=True)
        for eachUn in unusedSG:
            mc.textScrollList('unList', e=True, append=eachUn)

        mc.textScrollList('sameList',  removeAll=True, e=True)
        for eachSame in sameTup:
            if len(eachSame):
                for eachSame2 in eachSame:
                    mc.textScrollList('sameList', e=True, append=eachSame2)

                mc.textScrollList('sameList', e=True, append='')

    mc.select(cl=True)



def cleanMat(which, item):
    if which == 'same':
        controlObj = 'sameList'
    elif which == 'unused':
        controlObj = 'unList'

    if item == 'sel':
        selItem = mc.textScrollList(controlObj, q=True, si=True)

        if selItem == None:
            mc.confirmDialog(t='Warning', m="Please select least one Item's in the left side ScrollList", b='OK')
            return
    elif item == 'all':
        selItem = mc.textScrollList(controlObj,q=True,ai=True)
    if selItem:
        for i in range(selItem.count('')):
            selItem.remove('')

        mc.select(selItem, r=True, ne=True)
        if which == 'same':
            mm.eval('removeDuplicateShadingNetworks(1);\n')
        elif which == 'unused':
            if item == 'sel':
                mm.eval('OCT_MLdeleteUnused;\n')
            else:
                mm.eval('MLdeleteUnused;\n')

        mc.textScrollList(controlObj, e=True, ri=selItem)

    mc.select(cl=True)

def sameList_dcc():
    sel = mc.textScrollList('sameList', q=True, si=True)
    if len(sel) > 0 and len(sel[0]) > 1:
        mc.select(sel,r=True,ne=True)

def unList_dcc():
    sel = mc.textScrollList('unList', q=True, si=True)
    if len(sel) > 0 and len(sel[0]) > 1:
        mc.select(sel,r=True,ne=True)

def cleanMatHelp():
    return


'''
##########################################################################

##########################################################################
##VRAY专用，将所有的Phong材质球转换为Lambert
##Modify DATE:2012/07/06 17:05
##########################################################################

def disconnectMaterialInfo(shaderNode):
    materialInfoNode = getMaterialInfo(shaderNode)
    if materialInfoNode == None:
        return

    mc.disconnectAttr(shaderNode + '.message',materialInfoNode + '.material')


def getMaterialInfo(shaderNode):
    connections = mc.listConnections(shaderNode + '.message')
    for each in connections:
        if mc.objectType(each) == 'materialInfo':
            return each

    return None


def doReplace(origNode, replaceNode):
    origNode = origNode.encode()
    replaceNode = replaceNode.encode()

    origAttrs = mc.listAttr(origNode, scalar=True, multi=True, read=True, visible=True)
    replaceAttrs = mc.listAttr(replaceNode, scalar=True, multi=True, read=True, visible=True)

    for eachAttr in origAttrs:
        if eachAttr in replaceAttrs:
            value = mc.getAttr(origNode + '.' + eachAttr)
            try:
                mc.setAttr(replaceNode + '.' + eachAttr,value)
            except:
                om.MGlobal.displayWarning(u'Error in setting %s.%s attribute...Ignore this attribute!' % (replaceNode,eachAttr))

    binValue = mc.getAttr(origNode + '.binMembership')
    try:
        mc.setAttr(replaceNode + '.binMembership',binValue,type='string')
    except:
        om.MGlobal.displayWarning(u'%s.binMembership attribute not found...ignore!' % origNode)

    connections = mc.listConnections(origNode,s=True,d=False,connections=True,plugs=True)

    if not connections == None:
        for i in range(0,len(connections),2):
            origPlug = connections[i]
            srcPlug = connections[i+1]

            replacePlug = string.replace(origPlug,origNode,replaceNode)
            try:
                mc.connectAttr(srcPlug,replacePlug)
            except:
                om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (replacePlug,srcPlug))

    connections = mc.listConnections(origNode,s=False,d=True,connections=True,plugs=True)

    for i in range(0,len(connections),2):
        origPlug = connections[i]
        dstPlug = connections[i+1]

        replacePlug = string.replace(origPlug,origNode,replaceNode)

        try:
            mc.disconnectAttr(origPlug,dstPlug)
            mc.connectAttr(replacePlug,dstPlug)
        except:
            om.MGlobal.displayWarning(u'Error in connecting %s attribute from %s...' % (dstPlug,replacePlug))


def convertLambert():
    allPhong = mc.ls(type='phong')
    replaceNodeType = 'lambert'
    i = 0
    for eachPhong in allPhong:
        replaceNode = mc.createNode(replaceNodeType)

        disconnectMaterialInfo(eachPhong)

        doReplace(eachPhong, replaceNode)

        cmdStr = 'showEditor %s;\n' % replaceNode

        mm.eval(cmdStr)
        mc.delete(eachPhong)
        i += 1

    print (u'--------========>>>> 一共转换了%d个Phong材质球... <<<<========--------\n' % i)

############################################################################
'''


def HYZX_eyeLight():
    import OCT_util
    sl = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(sl)

    if sl.isEmpty():
        om.MGlobal.displayWarning(u'请选择眼睛模型...')
        return

    allLinker = mc.ls(type='lightLinker')
    if not allLinker:
        om.MGlobal.displayError(u'当前场景里不存在LightLinker节点...')
        return

    linker = OCT_util.nameToNode(allLinker[0])
    linkerFn = om.MFnDependencyNode(linker)
    linkPlug = linkerFn.findPlug('link')

    i = 0
    slIt = om.MItSelectionList(sl)

    while not slIt.isDone():
        eachDag = om.MDagPath()
        slIt.getDagPath(eachDag)
        dagName = eachDag.fullPathName()
        try:
            s, t = OCT_util.getShapeNameAndType(dagName)
        except:
            om.MGlobal.displayWarning(u'%s节点无Shape节点, 跳过操作...' % dagName)
            slIt.next()
            continue

        if not t == 'kMesh' and not t == 'kSubdiv' and not t == 'kNurbsSurface':
            om.MGlobal.displayWarning(u'%s节点为非模型物体, 跳过操作....' % dagName)
            slIt.next()
            continue

        # Get the Shape DagPath from current selected object
        shapeDag = OCT_util.nameToDag(s)
        shapeFn = om.MFnDagNode(shapeDag)

        inMeshPlug = shapeFn.findPlug('inMesh')
        if inMeshPlug.isConnected():
            inMeshSource = om.MPlugArray()
            inMeshPlug.connectedTo(inMeshSource, True, False)
            if inMeshSource[0].node().apiTypeStr() == 'kPolySmoothFacet':
                smoothFn = om.MFnDependencyNode(inMeshSource[0].node())
                smoothPlug = smoothFn.findPlug('inputPolymesh')
                inMeshSource = om.MPlugArray()
                smoothPlug.connectedTo(inMeshSource, True, False)
            
            if inMeshSource[0].node().apiTypeStr() == 'kSkinClusterFilter':
                inMeshFn = om.MFnDependencyNode(inMeshSource[0].node())
                worldMatrixPlug = inMeshFn.findPlug('matrix')
                for i in range(0, worldMatrixPlug.numElements()):
                    worldMatrixElement = worldMatrixPlug.elementByPhysicalIndex(i)
                    if worldMatrixElement.isConnected():
                        jointArray = om.MPlugArray()
                        worldMatrixElement.connectedTo(jointArray, True, False)
                        if jointArray[0].node().apiTypeStr() == 'kJoint':
                            eyeJointRootObj = jointArray[0].node()
                            om.MGlobal.select(eyeJointRootObj, om.MGlobal.kReplaceList)
                            jointObj = mc.ls(sl=True, ap=True)
                            jointDag = OCT_util.nameToDag(jointObj[0])
                            mtx = om.MMatrix.identity
                            transMatrix = om.MTransformationMatrix(jointDag.exclusiveMatrix())
                            # Get Scale
                            scaleUtil = om.MScriptUtil()
                            scaleUtil.createFromDouble(0.0, 0.0, 0.0)
                            scalePtr = scaleUtil.asDoublePtr()
                            transMatrix.getScale(scalePtr, om.MSpace.kWorld)
                            # Get scale
                            scaleX = scaleUtil.getDoubleArrayItem(scalePtr, 0)
                            scaleY = scaleUtil.getDoubleArrayItem(scalePtr, 1)
                            scaleZ = scaleUtil.getDoubleArrayItem(scalePtr, 2)

                            # obj Transform Fn
                            transformFn = om.MFnTransform(jointDag)
                            # get Original Rotation
                            quat = om.MQuaternion()
                            transformFn.getRotation(quat, om.MSpace.kWorld)
                            er = quat.asEulerRotation()
                            meshFn = om.MFnTransform(eachDag)
                            newBB = meshFn.boundingBox()
                            bbCenter = newBB.center()
                            thisMtx = eachDag.exclusiveMatrix()
                            bbCenter *= thisMtx
                            bbWidth = newBB.width()
                            bbHeight = newBB.height()
                            bbDepth = newBB.depth()
                            # offsetZ = bbWidth / 6.00 * scaleX
                            offsetZ = bbWidth / 1.00 * scaleX # alter by zhangben 20190522  alter eyelight position
                            offsetY = bbHeight / 6.00 * scaleY
                            offsetX = (math.sqrt(bbWidth * bbWidth + bbDepth * bbDepth) / 2 + math.sqrt(bbHeight * bbHeight + bbDepth * bbDepth) / 2) * 0.35 * scaleZ
                            # Transform the original BB Center to the Current BB Center: MPoint = MPoint * MMatrix
                            bbCenter *= mtx

                            dagName = jointObj[0]
                        else:
                            continue
                    else:
                        continue
            else:
                slIt.next()
                continue
        else:
            # Get Select Obj worldMatrix
            mtx = eachDag.inclusiveMatrix()
            # Get TransformationMatrix from worldMatrix
            transMatrix = om.MTransformationMatrix(eachDag.exclusiveMatrix())
            # Get Scale
            scaleUtil = om.MScriptUtil()
            scaleUtil.createFromDouble(0.0, 0.0, 0.0)
            scalePtr = scaleUtil.asDoublePtr()
            transMatrix.getScale(scalePtr, om.MSpace.kWorld)
            # Get scale
            scaleX = scaleUtil.getDoubleArrayItem(scalePtr, 0)
            scaleY = scaleUtil.getDoubleArrayItem(scalePtr, 1)
            scaleZ = scaleUtil.getDoubleArrayItem(scalePtr, 2)

            # obj Transform Fn
            transformFn = om.MFnTransform(eachDag)
            # get Original Rotation
            quat = om.MQuaternion()
            transformFn.getRotation(quat, om.MSpace.kWorld)
            er = quat.asEulerRotation()

            # Get the BoundingBox from current selected object
            newBB = transformFn.boundingBox()

            bbCenter = newBB.center()
#			thisMtx = eachDag.exclusiveMatrix()
#			bbCenter *= thisMtx
            bbWidth = newBB.width()
            bbHeight = newBB.height()
            bbDepth = newBB.depth()
            offsetX = bbWidth / -6.00 * scaleX
            offsetY = bbHeight / 6.00 * scaleY
            offsetZ = (math.sqrt(bbWidth * bbWidth + bbDepth * bbDepth) / 2 + math.sqrt(bbHeight * bbHeight + bbDepth * bbDepth) / 2) * 0.35 * scaleZ
            # Transform the original BB Center to the Current BB Center: MPoint = MPoint * MMatrix
            bbCenter *= mtx

        dagFn = om.MFnDagNode()
        # Create PointLight Shape
        lightName = mc.shadingNode('pointLight', asLight=True)
        lightName = mc.rename(lightName, 'eyeLight01')
        # Get Light DagPath with lightName
        lightTrans = OCT_util.nameToDag(lightName)
        # Get LightShape DagPath From lightTrans extend to shape
        lightShape = om.MDagPath(lightTrans)
        lightShape.extendToShape()

        lightTransFn = om.MFnTransform(lightTrans)
        lightTransFn.setTranslation(om.MVector(bbCenter), om.MSpace.kTransform)
        lightTransFn.setRotation(er)
        lightTransFn.translateBy(om.MVector(offsetX, offsetY, offsetZ), om.MSpace.kObject)

        lightFn = om.MFnLight(lightShape)
        lightFn.setIntensity(2.0)
        emitPlug = lightFn.findPlug('emitDiffuse')
        emitPlug.setBool(False)

        sMsgPlug = shapeFn.findPlug('message')
        lightMsgPlug = lightFn.findPlug('message')

        modifier = om.MDagModifier()
        plugArray = om.MPlugArray()
        lightSetPlug = lightTransFn.findPlug('instObjGroups').elementByLogicalIndex(0)
        lightSetPlug.connectedTo(plugArray, False, True)
        if plugArray.length():
            try:
                modifier.disconnect(lightSetPlug, plugArray[0])
            except:
                om.MGlobal.displayWarning('%s does not connected to %s...,ingore it.' % (lightSetPlug.info(), plugArray[0].info()))

        while True:
            currentPlug = linkPlug.elementByLogicalIndex(i)
            if i == linkPlug.evaluateNumElements():
                getAttrName = currentPlug.info()
#					mc.getAttr(getAttrName)
                modifier.connect(lightMsgPlug, currentPlug.child(0))
                modifier.connect(sMsgPlug, currentPlug.child(1))
                modifier.doIt()
                break

            if currentPlug.child(0).isConnected() or currentPlug.child(1).isConnected():
                i += 1
            else:
                modifier.connect(lightMsgPlug, currentPlug.child(0))
                modifier.connect(sMsgPlug, currentPlug.child(1))
                modifier.doIt()
                break

        mc.parentConstraint(dagName, lightTrans.fullPathName(), mo=True, weight=1.0)
        del modifier

        slIt.next()

def zb_DupLightLink_cmd():
    res = mc.confirmDialog(t=u"复制灯光链接",message=u'1 先选择有灯光链接的原角色组\n2 再选择没有灯光链接的新角色组',button=['copy','No'])
    if res == 'copy':
        import OCT_lgt.zb_DupLightLink as dupll
        dupll.DupLightLink()
