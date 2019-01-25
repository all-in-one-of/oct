# -*- coding: utf-8 -*-

from __future__ import with_statement #only needed for maya 2008 & 2009

import os, OCT_util
import maya.utils
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import string, sys


def makeMenu():
    _gMainWindow = mm.eval("global string $gMainWindow;string $temp = $gMainWindow;")
    #	_gMainWindow = 'MayaWindow'

    mc.setParent(_gMainWindow)
    mc.menu("OCT_ToolSetMN",l="OCT_Tools",tearOff=False,parent=_gMainWindow)

    mc.menuItem("generel",label=u"通用",subMenu=True,to=True,parent="OCT_ToolSetMN")
    mc.menuItem("RenderSet_zwz",label=u"渲染面板设置",c="OCT_generel.OCT_RenderSet_zwz.OCT_RenderSet_zwz_UI()",parent="generel")
    mc.menuItem("rename",label="Rename",c="OCT_generel.reName()",parent="generel")
    mc.menuItem("checkName",label="Check Name",c="OCT_generel.checkName()",parent="generel")
    mc.menuItem("removeNamespace",l=u"清除NameSpace",c="OCT_generel.removeNamespace()",parent="generel")
    mc.menuItem("deldefaultRenderLayer",l=u"清除DefaultRenderLayer",c="OCT_generel.delDefaultRenderLayer()",parent="generel")
    mc.menuItem('changeRefPath', l=u'替换参考文件路径', c="OCT_generel.changeRefPath()", parent="generel")
    mc.menuItem('fixCacheFilePath', l=u'修正CacheFile节点路径', c='OCT_generel.fixCacheFilePath()', parent='generel')

    mc.menuItem(d=1,parent="generel")

    mc.menuItem("FTM",l=u"贴图管理",c="OCT_generel.FTM()",parent="generel")
    mc.menuItem("renderTools",l=u"拍屏渲染工具",c="OCT_generel.renderTools()",parent="generel")

    mc.menuItem(d=1,parent="generel")

    mc.menuItem('copyTransform', l=u'复制位移', c='OCT_generel.copyTransform()',parent='generel')
    mc.menuItem('instanceTransform', l=u'镜像复制并位移到后选物体', c='OCT_generel.copyAndMatchTransformWithSecond()', parent='generel')
    mc.menuItem('playBlast', l=u'PlayBlast工具', c="OCT_generel.playBlast()", parent="generel")

    mc.menuItem(d=1,parent="OCT_ToolSetMN")

    mc.menuItem("anim",label=u'动画',subMenu=True,to=True,parent="OCT_ToolSetMN")

    mc.menuItem(d=1,parent="OCT_ToolSetMN")

    mc.menuItem("mod",label=u'模型',subMenu=True,to=True,parent="OCT_ToolSetMN")
    mc.menuItem('iso',label='Select Multi ISO(NURBS)',c='OCT_mod.calIso()',parent='mod')
    #mc.menuItem('polyTools',label='polyTools',c='OCT_mod.polyTools()',parent='mod')
    mc.menuItem('PlaceOnMesh',label=u'Place Obj on Mesh',c='OCT_mod.placeOnMesh()',parent='mod')
    mc.menuItem('paintGeometry', label=u'Paint Geometry', c='OCT_mod.paintGeo()', parent='mod')
    mc.menuItem('dupToCurveFlow',label=u'Object Follow Curve',c='OCT_mod.dupToCurveFlow()',parent='mod')

    mc.menuItem(d=1,parent="OCT_ToolSetMN")

    mc.menuItem("lgt",label=u'灯光',subMenu=True,to=True,parent="OCT_ToolSetMN")
    mc.menuItem('delLink',label=u'删除灯光连接',c='OCT_lgt.llCleanUp()',parent='lgt')
    #mc.menuItem('makeBat',l=u'生成批处理渲染',c='OCT_lgt.makeBat()',parent='lgt')
    mc.menuItem('smoothTools',l=u'Smooth工具',c='OCT_lgt.smooth()',parent='lgt')
    mc.menuItem('exShaderTools',l=u'替换材质工具',c='OCT_lgt.OCT_exShader()',parent='lgt')
    mc.menuItem('cleanMatTools', l=u'清理材质工具', c='OCT_lgt.cleanMatUI()',parent='lgt')
    mc.menuItem('convertLambertTools', l=u'Phong-=>Lambert', c='OCT_lgt.convertLambert()',parent='lgt')
    mc.menuItem('eyePointLight', l=u'眼神光', c='OCT_lgt.HYZX_eyeLight()', parent='lgt')

    mc.menuItem(d=1,parent="OCT_ToolSetMN")

    mc.menuItem("vfx",label=u'特效',subMenu=True,to=True,parent="OCT_ToolSetMN")
    mc.menuItem('VFXRender',label=u'特效拍屏渲染器',c='OCT_vfx.OCt_DyRender_zwz()',parent='vfx')
    mc.menuItem('UVtoPos',label=u'UV To Position',c='OCT_vfx.uvToPosUI()',parent='vfx')

    mc.menuItem(d=1,parent='OCT_ToolSetMN')

    mc.menuItem('about',label=u'关于',subMenu=True,to=False,parent='OCT_ToolSetMN')
    mc.menuItem('refresh',label=u'刷新',c='OCT_about.refresh()',parent='about')
    mc.menuItem('helpDoc',label=u'帮助',c='OCT_about.helpDoc()',parent='about')
    mc.menuItem('Doc2009',label=u'MAYA2009帮助',c='OCT_about.Maya2009Help()',parent='about')
    mc.menuItem('Doc2012',label=u'MAYA2012帮助',c='OCT_about.Maya2012Help()',parent='about')
    mc.menuItem('Doc2012SDK',label=u'MAYA2012 SDK帮助',c='OCT_about.Maya2012SDK()',parent='about')
    mc.menuItem('feedback',label=u'反馈',c='OCT_about.feedback()',parent='about')
    mc.menuItem('aboutThis',label=u'关于',c='OCT_about.aboutThis()',parent='about')

    mc.menuItem(d=1,parent='OCT_ToolSetMN')
    mc.menuItem('fyxb', label=u'飞越西部工具集', c='OCT_menu.fyxb_UI()', parent='OCT_ToolSetMN')

    mc.menuItem(d=1,parent='OCT_ToolSetMN')
    mc.menuItem('XxbTools', label=u'小锡兵工具集',subMenu=True,to=False,parent='OCT_ToolSetMN')
    mc.menuItem('Xxb_Render',label=u'分层渲染工具',c='OCT_lgt.OCT_TXiaoXiBingTools_zwz.OCT_XiaoXiBingTools_Menum_zwz()',parent='XxbTools')
    mc.menuItem('Xxb_ChangeCameras',label=u'修改摄像机工具',c='OCT_anim.OCT_ChangeXxbOldCameras_zwz.ChangeXxbOldCameras_zwz()',parent='XxbTools')

    mc.menuItem(d=1,parent='OCT_ToolSetMN')
    mc.menuItem('subJob', label=u'提交Deadline渲染', c='OCT_menu.selectServerUI()', parent='OCT_ToolSetMN')

    mc.menuItem(d=1,parent='OCT_ToolSetMN')
    mc.menuItem('setRenderOpt', label=u'渲染设置', c='OCT_menu.setProjRenderOpt_UI()', parent='OCT_ToolSetMN')

def fyxb_UI():
    if mc.windowPref('fyxbUI', exists=True):
        mc.windowPref('fyxbUI', remove=True)

    if mc.window('fyxbUI', ex=True):
        mc.deleteUI('fyxbUI', window=True)

    mc.window('fyxbUI', t=u'飞越西部工具集', wh=[294,10], mnb=True, mxb=True, rtf=True)
    mc.columnLayout(rs=5, cal='center')
    mc.frameLayout(bv=True,bs='in',l='Shader',cll=True,li=5,w=294,pcc='OCT_menu.resizeWindow()',pec='OCT_menu.resizeWindow()')
    mc.rowColumnLayout(numberOfRows=1,rowHeight=[1,70])
    mc.symbolButton('red_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_red.xpm', c='OCT_menu.createShader("Red")')
    mc.symbolButton('green_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_green.xpm', c='OCT_menu.createShader("Green")')
    mc.symbolButton('blue_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_blue.xpm', c='OCT_menu.createShader("Blue")')
    mc.symbolButton('white_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_white.xpm', c='OCT_menu.createShader("White")')
    mc.symbolButton('black_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_black.xpm', c='OCT_menu.createShader("Black")')
    mc.symbolButton('lambert_SHD', image=r'\\octvision.com\cg\td\Maya\src\lambert_white.xpm', c='OCT_menu.createShader("Lambert")')
    mc.setParent('..')
    mc.setParent('..')
    mc.frameLayout(bv=True, bs='in', l='Lambert Shader With Transparency', cll=True, li=5, w=294, pcc='OCT_menu.resizeWindow()', pec='OCT_menu.resizeWindow()')
    mc.rowColumnLayout(numberOfRows=1,rowHeight=[1,70])
    mc.symbolButton('red_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_red.xpm', c='OCT_menu.vrshdToLambert_withOpacity("Red")')
    mc.symbolButton('green_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_green.xpm', c='OCT_menu.vrshdToLambert_withOpacity("Green")')
    mc.symbolButton('blue_SHD', image=r'\\octvision.com\cg\td\Maya\src\surfaceShader_blue.xpm', c='OCT_menu.vrshdToLambert_withOpacity("Blue")')
    mc.setParent('..')
    mc.setParent('..')
    mc.frameLayout(bv=True,bs='in',l=u'渲染分层',cll=True,li=5,w=294,pcc='OCT_menu.resizeWindow()',pec='OCT_menu.resizeWindow()')
    mc.rowLayout(nc=2,cw2=[140,140])
    mc.columnLayout(rs=5)
    mc.button(w=140, l=u'OCC', c='OCT_menu.applyLayer("Occ")')
    mc.button(w=140, l=u'Depth', c='OCT_menu.applyLayer("Depth")')
    mc.button(w=140, l=u'Transparency OCC', c='OCT_menu.applyTransOcc()')
    mc.setParent('..')
    mc.setParent('..')
    mc.setParent('..')
    mc.frameLayout(bv=True,bs='in',l=u'渲染预设',cll=True,li=5,w=294,pcc='OCT_menu.resizeWindow()',pec='OCT_menu.resizeWindow()')
    mc.rowLayout(nc=2,cw2=[140,140])
    mc.columnLayout(rs=5)
    mc.button(w=140, l='')
    mc.button(w=140, l='')
    mc.button(w=140, l='')
    mc.setParent('..')
    mc.columnLayout(rs=5)
    mc.button(w=140, l='')
    mc.button(w=140, l='')
    mc.button(w=140, l='')
    mc.setParent('..')
    mc.setParent('..')
    mc.setParent('..')
    mc.frameLayout(bv=True, bs='in',l=u'常用工具',cll=True,li=5,w=294,pcc='OCT_menu.resizeWindow()',pec='OCT_menu.resizeWindow()')
    mc.rowLayout(nc=2, cw2=[140,140])
    mc.columnLayout(rs=5)
    mc.button(w=140, l='Select Multi ISO(NURBS)', c='OCT_mod.calIso()')
    mc.button(w=140, l='Place Object On Mesh', c='OCT_mod.placeOnMesh()')
    mc.button(w=140, l='Object Follow Curve',c='OCT_mod.dupToCurveFlow()')
    mc.button(w=140, l='Paint Geometry',c='OCT_mod.paintGeo()')
    mc.button(w=140, l=u'VR Mat. to Lambert with Transparency', c='OCT_menu.vrshdToLambert_withOpacity("Gray")')
    mc.setParent('..')
    mc.columnLayout(rs=5)
    mc.button(w=140, l=u'PlayBlast工具',c='OCT_generel.playBlast()')
    mc.button(w=140, l=u'拍屏渲染工具',c='OCT_generel.renderTools()')
    mc.button(w=140, l=u'清理材质',c='OCT_lgt.cleanMatUI()')
    mc.button(w=140, l=u'9屏窗口', c='OCT_menu.build_9CamModel()')
    mc.setParent('..')
    mc.setParent('..')
    mc.setParent('..')
    mc.setParent('..')

    mc.showWindow('fyxbUI')

def createShader(shaderType):
    sel = mc.ls(sl=True)

    alpha = [0,0,0]
    type = 'surfaceShader'
    if shaderType == 'Red':
        color = [1,0,0]
    elif shaderType == 'Green':
        color = [0,1,0]
    elif shaderType == 'Blue':
        color = [0,0,1]
    elif shaderType == 'White' or shaderType == 'Lambert':
        color = [1,1,1]
    elif shaderType == 'Black':
        color = [0,0,0]
        alpha = [1,1,1]

    if shaderType == 'Lambert':
        type = 'lambert'

    shaderName = 'SHD_%s' % shaderType

    cmd = 'string $temp = `shadingNode -n %s -asShader %s`;\n' % (shaderName,type)
    finalShdName = mm.eval(cmd)
    sgName = finalShdName + 'SG'
    cmd = 'sets -renderable true -noSurfaceShader true -empty -name %s;\n' % sgName
    finalSGName = mm.eval(cmd)
    mc.connectAttr(finalShdName+'.outColor',finalSGName+'.surfaceShader',f=True)

    if not shaderType == 'Lambert':
        mc.setAttr(finalShdName+'.outColor',color[0],color[1],color[2],type='double3')
        mc.setAttr(finalShdName+'.outMatteOpacity',alpha[0],alpha[1],alpha[2],type='double3')
    else:
        mc.setAttr(finalShdName+'.color',color[0],color[1],color[2],type='double3')

    if not len(sel) == 0:
        mc.select(sel,r=True)
        try:
            mc.hyperShade(assign=finalShdName)
            mc.sets(e=True,forceElement=finalSGName)
        except:
            sys.stderr.write(u'Error assign shader for object...')
            return
    else:
        mc.select(finalShdName,r=True)

def resizeWindow():
    mc.window('fyxbUI',e=True,h=10)

def applyLayer(type):
    sel = mc.ls(sl=True)
    layerName = ''
    newLayer = mc.createRenderLayer(sel, n=type, mc=True, num=1, nr=True)

    if type == 'Occ':
        cmdType = 'occlusion'
    elif type == 'Depth':
        cmdType = 'linearDepth'

    cmd = 'renderLayerBuiltinPreset %s %s;\n' % ( cmdType, newLayer )
    mm.eval(cmd)

def applyTransOcc():
    mm.eval('miLoadMayatomr;\n')
    #List Current Selection Obj List
    allSurfaces = mc.ls(type='surfaceShape',long=True)
    sel = mc.ls(sl=True,long=True)
    selSurface = []
    for each in sel:
        if mc.nodeType(each) == 'transform':
            s = mc.listRelatives(each, shapes=True, f=True)
            if not s == None:
                for eachS in s:
                    vaild = mc.getAttr('%s.intermediateObject' % eachS)
                    if vaild == False:
                        if eachS in allSurfaces:
                            selSurface.append(eachS)
                            break
                    else:
                        continue
        elif mc.nodeType(each) == 'mesh' or mc.nodeType(each) == 'nurbsSurface' or mc.nodeType(each) == 'subdiv':
            if each in allSurfaces:
                selSurface.append(each)

    if len(selSurface) == 0:
        om.MGlobal.displayWarning(u'请选择模型...')
        return

    sel = selSurface
    newLayer = mc.createRenderLayer(selSurface, n='Occ', mc=True, num=1, nr=True)
    mc.editRenderLayerGlobals(crl=newLayer)
    cmd = 'renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0";\n'
    mm.eval(cmd)
    mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    mc.setAttr('defaultRenderGlobals.currentRenderer','mentalRay',type='string')

    if not mc.objExists('mentalrayGlobals'):
        mc.createNode('mentalrayGlobals', n='mentalrayGlobals')

    if not mc.objExists('miDefaultOptions'):
        mc.createNode('mentalrayOptions', n='miDefaultOptions')

    if not mc.objExists('mentalrayItemsList'):
        mc.createNode('mentalrayItemsList', n='mentalrayItemsList')

    try:
        cmd = 'connectAttr -f "miDefaultOptions.message" "mentalrayGlobals.options";\nconnectAttr -f "mentalrayGlobals.message" "mentalrayItemsList.globals";\nconnectAttr -f "miDefaultOptions.message" "mentalrayItemsList.options[0]";\n'
        mm.eval(cmd)
    except:
        pass

    mc.editRenderLayerAdjustment('miDefaultOptions.rayTracing')
    mc.setAttr('miDefaultOptions.rayTracing',1)

    mc.editRenderLayerAdjustment('miDefaultOptions.minSamples')
    mc.setAttr('miDefaultOptions.minSamples', 0)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxSamples')
    mc.setAttr('miDefaultOptions.maxSamples',2)

    mc.editRenderLayerAdjustment('miDefaultOptions.filter')
    mc.setAttr('miDefaultOptions.filter',1)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxReflectionRays')
    mc.setAttr('miDefaultOptions.maxReflectionRays',10)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxRefractionRays')
    mc.setAttr('miDefaultOptions.maxRefractionRays',10)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxRayDepth')
    mc.setAttr('miDefaultOptions.maxRayDepth',20)

    mc.editRenderLayerAdjustment('miDefaultOptions.maxShadowRayDepth')
    mc.setAttr('miDefaultOptions.maxShadowRayDepth',2)

    mc.editRenderLayerAdjustment('miDefaultOptions.finalGather')
    mc.setAttr('miDefaultOptions.finalGather',True)

    mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherTraceReflection')
    mc.setAttr('miDefaultOptions.finalGatherTraceReflection',4)

    mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherTraceRefraction')
    mc.setAttr('miDefaultOptions.finalGatherTraceRefraction',4)

    mc.editRenderLayerAdjustment('miDefaultOptions.finalGatherTraceDepth')
    mc.setAttr('miDefaultOptions.finalGatherTraceDepth',8)

    #Define Attr Name And generel Data
    transAttrName = ['transparency','outTransparency']
    specialShd = ['rampShader','layeredShader']
    shaderObj = ''

    #Create Generel SurfaceShader
    shaderName = 'SHD_Occ'
    cmd = 'string $temp = `shadingNode -n %s -asShader "surfaceShader"`;\n' % shaderName
    #Return SurfaceShader Name
    generelSurfaceShd = mm.eval(cmd)
    #Create SG
    sgName = generelSurfaceShd + 'SG'
    cmd = 'sets -renderable true -noSurfaceShader true -empty -name %s;\n' % sgName
    mm.eval(cmd)
    #Connecting SurfaceShader to SG
    mc.connectAttr(generelSurfaceShd+'.outColor',sgName+'.surfaceShader',f=True)
    #Create MR OCC Node
    cmd = 'string $temp = `mrCreateCustomNode -asTexture "" mib_fg_occlusion`;\n'
    #Return Occ Node Name
    occNode = mm.eval(cmd)
    generalOpacity = mc.createNode('mib_opacity')
    mc.connectAttr('%s.outValue' % generalOpacity, '%s.miMaterialShader' % sgName, f=True)
    mc.setAttr('%s.opacity' % generalOpacity, 1, 1, 1, type='double3')
    #Connecting OCC to SurfaceShader
    #mc.connectAttr(occNode+'.outValue',generelSurfaceShd+'.outColor',f=True)

    #For Each Selection Obj
    allShader = []
    for eachSel in sel:
        #Get Each Selection Obj Shape Node
        currentShapes = mc.listRelatives(eachSel, shapes=True, f=True)
        #For Each Shape Node
        if currentShapes == None:
            if not mc.nodeType(eachSel) == 'mesh' and not mc.nodeType(eachSel) == 'nurbsSurface' and not mc.nodeType(eachSel) == 'subdiv':
                continue
            else:
                currentShapes = [eachSel]

        for eachShape in currentShapes:
            #List SG
            allAssignSG = mc.listConnections(eachShape+'.instObjGroups.objectGroups', d=True, s=False)

            if allAssignSG == None:
                allAssignSG = mc.listConnections(eachShape+'.instObjGroups', d=True, s=False)

            for _each in allAssignSG:
                if not _each in allShader:
                    allShader.append(_each)


        mainSG = mc.listConnections(eachShape+'.compInstObjGroups.compObjectGroups', s=False, d=True)
        main = ''
        if not mainSG == None:
            for eachMain in mainSG:
                if mc.nodeType(eachMain) == 'shadingEngine':
                    mainPlug = mc.listConnections(eachShape+'.compInstObjGroups.compObjectGroups', s=False, d=True, p=True)
                    goPlug = mc.listConnections(mainPlug[0],s=True,d=False,p=True)
                    #print goPlug[0], mainPlug[0]
                    try:
                        mc.disconnectAttr(goPlug[0], mainPlug[0])
                    except:
                        sys.stdout.write('ingore disconnect Attr...\n')

                    main = eachMain

    if len(allShader):
        #For each SG
        for eachSG in allShader:
            if mc.nodeType(eachSG) == 'shadingEngine':
                #Get Obj Original surface Shader
                eachShader = mc.listConnections(eachSG+'.surfaceShader', s=True, d=False)

                shdNodeType = mc.nodeType(eachShader[0])
                mc.hyperShade(objects=eachShader[0])
                currentShdObj = mc.ls(sl=True,long=True)

                newShader = generelSurfaceShd
                newSG = sgName
                if not shdNodeType == specialShd[0] and not shdNodeType == specialShd[1]:
                #Check Node Type
                    if mc.getClassification(shdNodeType, satisfies='shader/surface') :
                        hasTrans = 0
                        #Check Original Surface Shader have a Transparency Attribute
                        if mc.attributeQuery(transAttrName[0], n=eachShader[0], ex=True):
                            connectNode = mc.listConnections(eachShader[0]+'.'+transAttrName[0], s=True, d=False, p=True)
                            if not connectNode == None:
                                hasTrans = 1
                        elif mc.attributeQuery(transAttrName[1], n=eachShader[0], ex=True):
                            connectNode = mc.listConnections(eachShader[0]+'.'+transAttrName[1], s=True, d=False, p=True)
                            if not connectNode == None:
                                hasTrans = 2

                        #If no Connect Transparency Attr Then Assgin the GenerelSurfaceShader
                        if (hasTrans == 0):
                            for eachCurrentShdObj in currentShdObj:
                                mc.select(eachCurrentShdObj, r=True)

                                mc.hyperShade(assign=generelSurfaceShd)
                                try:
                                    mc.sets(e=True,forceElement=sgName)
                                except:
                                    om.MGlobal.displayWarning(u'%s模型赋不上材质...' % eachCurrentShdObj)
                                    continue
                        #Else Then Duplicate the generelSurfaceShader to New SurfaceShade and assign to Obj with connect Transparency Node.
                        else:
                            mc.select(cl=True)
                            mc.select(sgName, r=True, ne=True)
                            dupNode = mc.duplicate(upstreamNodes=True)
                            for eachDup in dupNode:
                                if mc.nodeType(eachDup) == 'surfaceShader':
                                    newShader = eachDup

                                if mc.nodeType(eachDup) == 'shadingEngine':
                                    newSG = eachDup

                            if not shdNodeType == specialShd[0] and not shdNodeType == specialShd[1]:
                                dupNode1 = []
                                splitName = string.split(connectNode[0],'.')
                                if not mc.nodeType(splitName[0]) == 'file':
                                    upNode = mc.hyperShade(listUpstreamNodes=splitName[0])

                                    found = False
                                    for eachUp in upNode:
                                        if mc.nodeType(eachUp) == 'file':
                                            mc.select(splitName[0], r=True)
                                            found = True
                                            break

                                    rampNode = mc.createNode('ramp')
                                    mc.removeMultiInstance('%s.colorEntryList[2]' % rampNode,b=True)
                                    mc.removeMultiInstance('%s.colorEntryList[1]' % rampNode,b=True)

                                    opacityNode = mc.createNode('mib_opacity')
                                    mc.setAttr('%s.input' % opacityNode, 1, 1, 1, type='double3')
                                    mc.connectAttr('%s.outValue' % occNode, '%s.input' % opacityNode, f=True)
                                    mc.connectAttr('%s.outValueA' % occNode, '%s.inputA' % opacityNode, f=True)

                                    if found:
                                        print mc.ls(sl=True)
                                        dupNode1 = mc.duplicate(upstreamNodes=True)
                                        print dupNode1

                                        for eachNode in dupNode1:
                                            if mc.nodeType(eachNode) == 'file':
                                                fileNode = eachNode
                                                #texLook = mc.createNode('mib_texture_lookup')
                                                #texRemap = mc.createNode('mib_texture_remap')
                                                #texVec = mc.createNode('mib_texture_vector')

                                                mc.connectAttr('%s.outAlpha' % fileNode, '%s.colorEntryList[0].colorR' % rampNode, f=True)
                                                mc.connectAttr('%s.outAlpha' % fileNode, '%s.colorEntryList[0].colorG' % rampNode, f=True)
                                                mc.connectAttr('%s.outAlpha' % fileNode, '%s.colorEntryList[0].colorB' % rampNode, f=True)

                                                #mc.connectAttr(texVec + '.outValue',texRemap + '.input',f=True)
                                                #mc.connectAttr(texRemap + '.outValue',texLook + '.coord',f=True)
                                                #mc.connectAttr(fileNode + '.message',texLook + '.tex',f=True)

                                                #destPlug = mc.listConnections(fileNode,s=False,d=True,p=True)
                                                #for eachDest in destPlug:
                                                #sourcePlug = mc.listConnections(eachDest,s=True,d=False,p=True)
                                                #plugName = string.split(sourcePlug[0],'.')
                                                #if plugName[1] == 'outColor':
                                                #mc.disconnectAttr(sourcePlug[0],eachDest)
                                                #mc.connectAttr(texLook + '.outValue',eachDest,f=True)
                                                #elif plugName[1] == 'outAlpha':
                                                #mc.disconnectAttr(sourcePlug[0],eachDest)
                                                #mc.connectAttr(texLook + '.outValueA',eachDest,f=True)

                                        #mc.connectAttr(dupNode1[0] + '.outColor',newShader+'.outTransparency',f=True)
                                        mc.connectAttr(occNode+'.outValue',newShader+'.outColor',f=True)
                                    else:
                                        #mc.connectAttr(splitName[0] + '.outColor',newShader+'.outTransparency',f=True)
                                        mc.connectAttr('%s.outAlpha' % splitName[0], '%s.colorEntryList[0].colorR' % rampNode, f=True)
                                        mc.connectAttr('%s.outAlpha' % splitName[0], '%s.colorEntryList[0].colorG' % rampNode, f=True)
                                        mc.connectAttr('%s.outAlpha' % splitName[0], '%s.colorEntryList[0].colorB' % rampNode, f=True)

                                        mc.connectAttr(occNode+'.outValue',newShader+'.outColor',f=True)

                                    mc.connectAttr('%s.outColor' % rampNode, '%s.opacity' % opacityNode, f=True)
                                    mc.connectAttr('%s.outAlpha' % rampNode, '%s.opacityA' % opacityNode, f=True)
                                    mc.connectAttr('%s.outValue' % opacityNode, '%s.miMaterialShader' % newSG, f=True)

                                    if len(currentShdObj):
                                        mc.select(currentShdObj,r=True)
                                    else:
                                        mc.select(eachSel)
                                    mc.hyperShade(assign=newShader)
                                    mc.sets(e=True,forceElement=newSG)
                                else:
                                    rampNode = mc.createNode('ramp')
                                    mc.removeMultiInstance('%s.colorEntryList[2]' % rampNode,b=True)
                                    mc.removeMultiInstance('%s.colorEntryList[1]' % rampNode,b=True)

                                    opacityNode = mc.createNode('mib_opacity')
                                    mc.setAttr('%s.input' % opacityNode, 1, 1, 1, type='double3')
                                    mc.connectAttr('%s.outValue' % occNode, '%s.input' % opacityNode, f=True)
                                    mc.connectAttr('%s.outValueA' % occNode, '%s.inputA' % opacityNode, f=True)
                                    mc.connectAttr('%s.outAlpha' % splitName[0], '%s.colorEntryList[0].colorR' % rampNode, f=True)
                                    mc.connectAttr('%s.outAlpha' % splitName[0], '%s.colorEntryList[0].colorG' % rampNode, f=True)
                                    mc.connectAttr('%s.outAlpha' % splitName[0], '%s.colorEntryList[0].colorB' % rampNode, f=True)
                                    mc.connectAttr('%s.outColor' % rampNode, '%s.opacity' % opacityNode, f=True)
                                    mc.connectAttr('%s.outAlpha' % rampNode, '%s.opacityA' % opacityNode, f=True)
                                    mc.connectAttr('%s.outValue' % opacityNode, '%s.miMaterialShader' % newSG, f=True)
                                    #texLook = mc.createNode('mib_texture_lookup')
                                    #texRemap = mc.createNode('mib_texture_remap')
                                    #texVec = mc.createNode('mib_texture_vector')
                                    #mc.connectAttr(texVec + '.outValue',texRemap + '.input',f=True)
                                    #mc.connectAttr(texRemap + '.outValue',texLook + '.coord',f=True)
                                    #mc.connectAttr(splitName[0] + '.message',texLook + '.tex',f=True)

                                    #destPlug = mc.listConnections(splitName[0],s=False,d=True,p=True)
                                    #for eachDest in destPlug:
                                    #sourcePlug = mc.listConnections(eachDest,s=True,d=False,p=True)
                                    #plugName = string.split(sourcePlug[0],'.')
                                    #if plugName[1] == 'outColor':

                                    #mc.connectAttr(texLook + '.outValue',newShader+'.outTransparency',f=True)
                                    #elif plugName[1] == 'outTransparency' or plugName[1] == 'outAlpha':

                                    #mc.connectAttr(texLook + '.outValue',newShader+'.outTransparency',f=True)

                                    #mc.connectAttr(splitName[0] + '.outColor',newShader+'.outTransparency',f=True)
                                    mc.connectAttr(occNode+'.outValue',newShader+'.outColor',f=True)
                                    if len(currentShdObj):
                                        mc.select(currentShdObj,r=True)
                                    else:
                                        mc.select(eachSel)
                                    mc.hyperShade(assign=newShader)
                                    mc.sets(e=True,forceElement=newSG)

                        mc.setAttr('%s.miExportShadingEngine' % newSG, False)

                        print '======= ' + main + ' == ' + eachSG + ' ======='

                        if eachSG == main:
                            compInstPlug = mc.getAttr(eachShape+'.compInstObjGroups.compObjectGroups',mi=True)
                            if not compInstPlug == None:
                                lastNumbert = compInstPlug.pop()
                                dstPlug = mc.getAttr(newSG+'.dagSetMembers',mi=True)
                                if not dstPlug == None:
                                    lastPlug = dstPlug.pop()+1
                                    mc.getAttr(newSG+'.dagSetMembers[%d]'%(lastPlug))
                                    try:
                                        mc.connectAttr(eachShape+'.compInstObjGroups.compObjectGroups[%d]'%(lastNumbert),newSG+'.dagSetMembers[%d]'%(lastPlug),f=True)
                                    except:
                                        sys.stderr.write('Error connect Attr')
                                        #del newShader
                                        #del newSG
                else:
                    for eachCurrentShdObj in currentShdObj:
                        mc.select(eachCurrentShdObj, r=True)
                        mc.hyperShade(assign=generelSurfaceShd)
                        try:
                            mc.sets(e=True,forceElement=sgName)
                        except:
                            om.MGlobal.displayWarning(u'%s模型赋不上材质...' % eachCurrentShdObj)
                            continue

    mc.select(cl=True)
    mc.connectAttr(occNode+'.outValue',generelSurfaceShd+'.outColor',f=True)
    mc.connectAttr('%s.outValue' % occNode, '%s.input' % generalOpacity, f=True)
    mc.connectAttr('%s.outValueA' % occNode, '%s.inputA' % generalOpacity, f=True)
    mc.setAttr('%s.miExportShadingEngine' % sgName, False)

def build_9CamModel():
    if mc.windowPref('Cam9_Model_Win',ex=True):
        mc.windowPref('Cam9_Model_Win',remove=True)

    if mc.window('Cam9_Model_Win',ex=True):
        mc.deleteUI('Cam9_Model_Win',window=True)

    if mc.modelPanel('LU_panel', ex=True):
        mc.deleteUI('LU_panel', panel=True)

    if mc.modelPanel('U_panel', ex=True):
        mc.deleteUI('U_panel', panel=True)

    if mc.modelPanel('RU_panel', ex=True):
        mc.deleteUI('RU_panel', panel=True)

    if mc.modelPanel('L_panel', ex=True):
        mc.deleteUI('L_panel', panel=True)

    if mc.modelPanel('M_panel', ex=True):
        mc.deleteUI('M_panel', panel=True)

    if mc.modelPanel('R_panel', ex=True):
        mc.deleteUI('R_panel', panel=True)

    if mc.modelPanel('LD_panel', ex=True):
        mc.deleteUI('LD_panel', panel=True)

    if mc.modelPanel('D_panel', ex=True):
        mc.deleteUI('D_panel', panel=True)

    if mc.modelPanel('RD_panel', ex=True):
        mc.deleteUI('RD_panel', panel=True)

    mc.window('Cam9_Model_Win', t='OCT_9CamModel', wh=[1068,940],sizeable=True, rtf=True)
    mc.rowLayout('row1',nc=4,cw4=[300,300,300,100])
    mc.columnLayout('column1',w=300,h=900,parent='row1')
    mc.paneLayout('pane1', w=300, h=1, configuration='single', p='column1', aft=0, st=1)
    mc.paneLayout('pane2', w=300, h=300, configuration='single', p='column1', aft=0, st=1)
    mc.paneLayout('pane3', w=300, h=1, configuration='single', p='column1', aft=0, st=1)

    mc.columnLayout('column2',w=300,h=900,parent='row1')
    mc.paneLayout('pane4', w=300, h=1, configuration='single', p='column2', aft=0, st=1)
    mc.paneLayout('pane5', w=300, h=300, configuration='single', p='column2', aft=0, st=1)
    mc.paneLayout('pane6', w=300, h=1, configuration='single', p='column2', aft=0, st=1)

    mc.columnLayout('column3',w=300,h=900,parent='row1')
    mc.paneLayout('pane7', w=300, h=1, configuration='single', p='column3', aft=0, st=1)
    mc.paneLayout('pane8', w=300, h=300, configuration='single', p='column3', aft=0, st=1)
    mc.paneLayout('pane9', w=300, h=1, configuration='single', p='column3', aft=0, st=1)

    mc.columnLayout('column4', w=150, h=900, parent='row1', cw=150, adj=True, cal='left', cat=['left',1])
    mc.columnLayout('column5', w=150, h=1, parent='column4', cw=150)
    mc.columnLayout('column6', w=150, h=300, parent='column4', cw=150, adj=False, cal='left', rs=5)
    mc.text(l='', parent='column6')
    mc.text(l='', parent='column6')
    mc.text(l='', parent='column6')
    mc.text(l='', parent='column6')
    mc.radioButtonGrp('mode', nrb=3, vr=True, l='Mode', labelArray3=['3 Cameras', '5 Cameras', '9 Cameras'], sl=1, cw2=[40,110], \
                      parent='column6', on1='OCT_menu.cam9_changeViews(3)', on2='OCT_menu.cam9_changeViews(5)', on3='OCT_menu.cam9_changeViews(9)')
    mc.columnLayout('column7', w=150, h=1, parent='column4', cw=150)

    mc.window('Cam9_Model_Win', e=True, wh=[1035,341])

    mc.showWindow('Cam9_Model_Win')

    cam9_changeViews(3)

def cam9_changeViews(mode):
    if mode == 3:
        if mc.modelPanel('LU_panel', ex=True):
            mc.deleteUI('LU_panel', panel=True)
        if mc.modelPanel('U_panel', ex=True):
            mc.deleteUI('U_panel', panel=True)
        if mc.modelPanel('RU_panel', ex=True):
            mc.deleteUI('RU_panel', panel=True)
        if mc.modelPanel('LD_panel', ex=True):
            mc.deleteUI('LD_panel', panel=True)
        if mc.modelPanel('D_panel', ex=True):
            mc.deleteUI('D_panel', panel=True)
        if mc.modelPanel('RD_panel', ex=True):
            mc.deleteUI('RD_panel', panel=True)
        if mc.modelPanel('L_panel', ex=True) == False:
            mc.modelPanel('L_panel', camera='testL', mbv=False, l='L', p='pane2')
        if mc.modelPanel('M_panel', ex=True) == False:
            mc.modelPanel('M_panel', camera='testM', mbv=False, l='M', p='pane5')
        if mc.modelPanel('R_panel', ex=True) == False:
            mc.modelPanel('R_panel', camera='testR', mbv=False, l='R', p='pane8')

        mc.paneLayout('pane1', e=True, h=1)
        mc.paneLayout('pane3', e=True, h=1)
        mc.paneLayout('pane4', e=True, h=1)
        mc.paneLayout('pane6', e=True, h=1)
        mc.paneLayout('pane7', e=True, h=1)
        mc.paneLayout('pane9', e=True, h=1)
        mc.columnLayout('column5', e=True, h=1)
        mc.columnLayout('column7', e=True, h=1)

        mc.modelEditor('L_panel',e=True,hud=False)
        mc.modelEditor('L_panel',e=True,dtx=True)
        mc.modelEditor('L_panel',e=True,ca=False)
        mc.modelPanel('L_panel',e=True,mbv=False)
        mc.modelEditor('M_panel',e=True,hud=False)
        mc.modelEditor('M_panel',e=True,dtx=True)
        mc.modelEditor('M_panel',e=True,ca=False)
        mc.modelPanel('M_panel',e=True,mbv=False)
        mc.modelEditor('R_panel',e=True,hud=False)
        mc.modelEditor('R_panel',e=True,dtx=True)
        mc.modelEditor('R_panel',e=True,ca=False)
        mc.modelPanel('R_panel',e=True,mbv=False)
        mc.window('Cam9_Model_Win', e=True, wh=[1032, 341])
    elif mode == 5:
        if mc.modelPanel('LU_panel', ex=True):
            mc.deleteUI('LU_panel', panel=True)
        if mc.modelPanel('RU_panel', ex=True):
            mc.deleteUI('RU_panel', panel=True)
        if mc.modelPanel('LD_panel', ex=True):
            mc.deleteUI('LD_panel', panel=True)
        if mc.modelPanel('RD_panel', ex=True):
            mc.deleteUI('RD_panel', panel=True)
        if mc.modelPanel('D_panel', ex=True) == False:
            mc.modelPanel('D_panel', camera='testD', mbv=False, l='D', p='pane6')
        if mc.modelPanel('L_panel', ex=True) == False:
            mc.modelPanel('L_panel', camera='testL', mbv=False, l='L', p='pane2')
        if mc.modelPanel('M_panel', ex=True) == False:
            mc.modelPanel('M_panel', camera='testM', mbv=False, l='M', p='pane5')
        if mc.modelPanel('R_panel', ex=True) == False:
            mc.modelPanel('R_panel', camera='testR', mbv=False, l='R', p='pane8')
        if mc.modelPanel('U_panel', ex=True) == False:
            mc.modelPanel('U_panel', camera='testU', mbv=False, l='U', p='pane4')

        mc.paneLayout('pane1', e=True, h=300)
        mc.paneLayout('pane3', e=True, h=300)
        mc.paneLayout('pane4', e=True, h=300)
        mc.paneLayout('pane6', e=True, h=300)
        mc.paneLayout('pane7', e=True, h=300)
        mc.paneLayout('pane9', e=True, h=300)
        mc.columnLayout('column5', e=True, h=300)
        mc.columnLayout('column7', e=True, h=300)

        mc.modelEditor('L_panel',e=True,hud=False)
        mc.modelEditor('L_panel',e=True,dtx=True)
        mc.modelEditor('L_panel',e=True,ca=False)
        mc.modelPanel('L_panel',e=True,mbv=False)
        mc.modelEditor('M_panel',e=True,hud=False)
        mc.modelEditor('M_panel',e=True,dtx=True)
        mc.modelEditor('M_panel',e=True,ca=False)
        mc.modelPanel('M_panel',e=True,mbv=False)
        mc.modelEditor('R_panel',e=True,hud=False)
        mc.modelEditor('R_panel',e=True,dtx=True)
        mc.modelEditor('R_panel',e=True,ca=False)
        mc.modelPanel('R_panel',e=True,mbv=False)
        mc.modelEditor('U_panel',e=True,hud=False)
        mc.modelEditor('U_panel',e=True,dtx=True)
        mc.modelEditor('U_panel',e=True,ca=False)
        mc.modelPanel('U_panel',e=True,mbv=False)
        mc.modelEditor('D_panel',e=True,hud=False)
        mc.modelEditor('D_panel',e=True,dtx=True)
        mc.modelEditor('D_panel',e=True,ca=False)
        mc.modelPanel('D_panel',e=True,mbv=False)
        mc.window('Cam9_Model_Win', e=True, wh=[1032, 938])
    elif mode == 9:
        if mc.modelPanel('D_panel', ex=True) == False:
            mc.modelPanel('D_panel', camera='testD', mbv=False, l='D', p='pane6')
        if mc.modelPanel('L_panel', ex=True) == False:
            mc.modelPanel('L_panel', camera='testL', mbv=False, l='L', p='pane2')
        if mc.modelPanel('M_panel', ex=True) == False:
            mc.modelPanel('M_panel', camera='testM', mbv=False, l='M', p='pane5')
        if mc.modelPanel('R_panel', ex=True) == False:
            mc.modelPanel('R_panel', camera='testR', mbv=False, l='R', p='pane8')
        if mc.modelPanel('U_panel', ex=True) == False:
            mc.modelPanel('U_panel', camera='testU', mbv=False, l='U', p='pane4')
        if mc.modelPanel('LU_panel', ex=True) == False:
            mc.modelPanel('LU_panel', camera='testLU', mbv=False, l='LU', p='pane1')
        if mc.modelPanel('LD_panel', ex=True) == False:
            mc.modelPanel('LD_panel', camera='testLD', mbv=False, l='LD', p='pane3')
        if mc.modelPanel('RU_panel', ex=True) == False:
            mc.modelPanel('RU_panel', camera='testRU', mbv=False, l='RU', p='pane7')
        if mc.modelPanel('RD_panel', ex=True) == False:
            mc.modelPanel('RD_panel', camera='testRD', mbv=False, l='RD', p='pane9')

        mc.paneLayout('pane1', e=True, h=300)
        mc.paneLayout('pane3', e=True, h=300)
        mc.paneLayout('pane4', e=True, h=300)
        mc.paneLayout('pane6', e=True, h=300)
        mc.paneLayout('pane7', e=True, h=300)
        mc.paneLayout('pane9', e=True, h=300)
        mc.columnLayout('column5', e=True, h=300)
        mc.columnLayout('column7', e=True, h=300)

        mc.modelEditor('L_panel',e=True,hud=False)
        mc.modelEditor('L_panel',e=True,dtx=True)
        mc.modelEditor('L_panel',e=True,ca=False)
        mc.modelPanel('L_panel',e=True,mbv=False)
        mc.modelEditor('M_panel',e=True,hud=False)
        mc.modelEditor('M_panel',e=True,dtx=True)
        mc.modelEditor('M_panel',e=True,ca=False)
        mc.modelPanel('M_panel',e=True,mbv=False)
        mc.modelEditor('R_panel',e=True,hud=False)
        mc.modelEditor('R_panel',e=True,dtx=True)
        mc.modelEditor('R_panel',e=True,ca=False)
        mc.modelPanel('R_panel',e=True,mbv=False)
        mc.modelEditor('U_panel',e=True,hud=False)
        mc.modelEditor('U_panel',e=True,dtx=True)
        mc.modelEditor('U_panel',e=True,ca=False)
        mc.modelPanel('U_panel',e=True,mbv=False)
        mc.modelEditor('D_panel',e=True,hud=False)
        mc.modelEditor('D_panel',e=True,dtx=True)
        mc.modelEditor('D_panel',e=True,ca=False)
        mc.modelPanel('D_panel',e=True,mbv=False)
        mc.modelEditor('LU_panel',e=True,hud=False)
        mc.modelEditor('LU_panel',e=True,dtx=True)
        mc.modelEditor('LU_panel',e=True,ca=False)
        mc.modelPanel('LU_panel',e=True,mbv=False)
        mc.modelEditor('RU_panel',e=True,hud=False)
        mc.modelEditor('RU_panel',e=True,dtx=True)
        mc.modelEditor('RU_panel',e=True,ca=False)
        mc.modelPanel('RU_panel',e=True,mbv=False)
        mc.modelEditor('LD_panel',e=True,hud=False)
        mc.modelEditor('LD_panel',e=True,dtx=True)
        mc.modelEditor('LD_panel',e=True,ca=False)
        mc.modelPanel('LD_panel',e=True,mbv=False)
        mc.modelEditor('RD_panel',e=True,hud=False)
        mc.modelEditor('RD_panel',e=True,dtx=True)
        mc.modelEditor('RD_panel',e=True,ca=False)
        mc.modelPanel('RD_panel',e=True,mbv=False)
        mc.window('Cam9_Model_Win', e=True, wh=[1032, 938])

def vrshdToLambert_withOpacity(c):
    color = None
    amb = None
    if c == 'Gray':
        color = [0.5, 0.5, 0.5]
        amb = [0.0, 0.0, 0.0]
    elif c == 'Red':
        color = [1, 0, 0]
        amb = color
    elif c == 'Green':
        color = [0, 1, 0]
        amb = color
    elif c == 'Blue':
        color = [0, 0, 1]
        amb = color

    mc.hyperShade(smn=True)
    allSelShader = mc.ls(sl=True)

    vrShd = []
    del vrShd[:]
    defaultShd = []
    del defaultShd[:]

    for each in allSelShader:
        if mc.nodeType(each) == 'VRayMtl':
            vrShd.append(each)
        elif mc.nodeType(each) == 'lambert' or mc.nodeType(each) == 'blinn' \
            or mc.nodeType(each) == 'phong' or mc.nodeType(each) == 'phongE' \
            or mc.nodeType(each) == 'surfaceShader':
            defaultShd.append(each)


            #	if mc.pluginInfo('vrayformaya',q=True,l=True):
            #		vrShd = mc.ls(type='VRayMtl')
            #		if vrShd == None:
            #			vrShd = []
            #	else:
            #		vrShd = []

    newLbtShd = []
    #	lmbtShd = mc.ls(type='lambert')
    mc.select(cl=True)

    i = 1
    for each in vrShd:
        mc.hyperShade(objects=each)
        sdObj = mc.ls(sl=True)

        if len(sdObj):
            shaderName = 'VR_To_Lbrt%d_%s' % (i, c)
            cmd = 'string $temp = `shadingNode -n %s -asShader "lambert"`;\n' % shaderName

            lambertShd = mm.eval(cmd)

            sgName = lambertShd + 'SG'
            cmd = 'sets -renderable true -noSurfaceShader true -empty -name %s;\n' % sgName
            sgName = mm.eval(cmd)

            mc.connectAttr(lambertShd + '.outColor',sgName+'.surfaceShader',f=True)

            try:
                opacityPath = mc.listConnections('%s.opacityMap' % each, s=True, d=False, plugs=True)
            except:
                sys.stdout.write('%s Shader Opacity Attribute have not connecting Anything...' % each)
            else:
                if not opacityPath == None:
                    opacityNode = opacityPath[0].split('.')[0]
                    opacityAttr = opacityPath[0].split('.')[1]
                    mc.setAttr('%s.alphaIsLuminance' % opacityNode, True)

                    if mc.attributeQuery('invert', node=opacityNode, ex=True):
                        mc.setAttr('%s.invert' % opacityNode, True)
                        mc.connectAttr(opacityPath[0], '%s.transparency' % lambertShd, f=True)
                    if mc.attributeQuery('outAlpha', node=opacityNode, ex=True):
                        mc.connectAttr('%s.outAlpha' % opacityNode, '%s.transparencyR' % lambertShd, f=True)
                        mc.connectAttr('%s.outAlpha' % opacityNode, '%s.transparencyG' % lambertShd, f=True)
                        mc.connectAttr('%s.outAlpha' % opacityNode, '%s.transparencyB' % lambertShd, f=True)
                    else:
                        reverseNode = mc.createNode('reverse')
                        child = mc.attributeQuery(opacityAttr, node=opacityNode, nc=True)
                        if not child == None:
                            if child == 3:
                                mc.connectAttr(opacityPath[0], '%s.input' % reverseNode, f=True)
                        else:
                            opacityR = mc.listConnections('%s.opacityMapR' % each, d=False, s=True, plugs=True)
                            opacityG = mc.listConnections('%s.opacityMapG' % each, d=False, s=True, plugs=True)
                            opacityB = mc.listConnections('%s.opacityMapB' % each, d=False, s=True, plugs=True)
                            try:
                                mc.connectAttr('%s' % opacityR, '%s.inputX' % reverseNode, f=True)
                            except:
                                om.MGlobal.displayWarning(u'%s材质球没有连接opacityMapR属性' % (each))
                            try:
                                mc.connectAttr('%s' % opacityG, '%s.inputY' % reverseNode, f=True)
                            except:
                                om.MGlobal.displayWarning(u'%s材质球没有连接opacityMapG属性' % (each))
                            try:
                                mc.connectAttr('%s' % opacityB, '%s.inputZ' % reverseNode, f=True)
                            except:
                                om.MGlobal.displayWarning(u'%s材质球没有连接opacityMapB属性' % (each))

                        mc.connectAttr('%s.output' % reverseNode, '%s.transparency' % lambertShd, f=True)

            mc.setAttr('%s.color' % lambertShd, color[0], color[1], color[2], type='double3')
            mc.setAttr('%s.ambientColor' % lambertShd, amb[0], amb[1], amb[2], type='double3')
            mc.setAttr('%s.diffuse' % lambertShd, 1)
            mc.select(sdObj, r=True)
            try:
                mc.hyperShade(assign=lambertShd)
                mc.sets(e=True,forceElement=sgName)
            except:
                sys.stdout.write('%s Object error in assign Shader' % sdObj)

            newLbtShd.append(lambertShd)
            i += 1

    i = 1
    for each in defaultShd:
        type = mc.nodeType(each)
        if type == 'surfaceShader':
            transAttr = 'outTransparency'
        else:
            transAttr = 'transparency'

        mc.hyperShade(objects=each)
        sdObj = mc.ls(sl=True)

        if len(sdObj):
            shaderName = 'Lbrt_To_Lbrt%d_%s' % (i, c)
            cmd = 'string $temp = `shadingNode -n %s -asShader "lambert"`;\n' % shaderName

            lambertShd = mm.eval(cmd)

            sgName = lambertShd + 'SG'
            cmd = 'sets -renderable true -noSurfaceShader true -empty -name %s;\n' % sgName
            sgName = mm.eval(cmd)

            mc.connectAttr(lambertShd + '.outColor',sgName+'.surfaceShader',f=True)

            try:
                transPath = mc.listConnections('%s.%s' % (each, transAttr), s=True, d=False,plugs=True)
            except:
                sys.stdout.write('%s Shader Transparency Attribute have not connecting Anything...' % each)
            else:
                if not transPath == None:
                    transNode = transPath[0].split('.')[0]
                    transAttr = transPath[0].split('.')[1]
                    mc.setAttr('%s.alphaIsLuminance' % transNode, True)

                    mc.connectAttr(transPath[0], '%s.transparency' % lambertShd, f=True)

            mc.select(sdObj, r=True)
            mc.setAttr('%s.color' % lambertShd, color[0], color[1], color[2], type='double3')
            mc.setAttr('%s.ambientColor' % lambertShd, amb[0], amb[1], amb[2], type='double3')
            mc.setAttr('%s.diffuse' % lambertShd, 1)
            try:
                mc.hyperShade(assign=lambertShd)
                mc.sets(e=True,forceElement=sgName)
            except:
                sys.stdout.write('%s Object assign Shader cause Error...' % sdObj)

            newLbtShd.append(lambertShd)
            i += 1
    '''
    if len(newLbtShd):
    mc.select(newLbtShd, r=True)
    mm.eval('removeDuplicateShadingNetworks(1);\n')
    '''
    mc.select(cl=True)

def selectServerUI():
    if mc.windowPref("ServerUI",exists=True):
        mc.windowPref("ServerUI",remove=True)

    if mc.window('ServerUI', ex=True):
        mc.deleteUI('ServerUI', window=True)

    mc.window('ServerUI', t='DeadLine@octvision.com', wh=[414, 200], mnb=False, mxb=False, rtf=True, s=False)
    mc.columnLayout('col1', w=414, cat=['both',0], cw=414)
    mc.rowLayout('row1', w=414, cw2=[110, 304], nc=2, p='col1')
    mc.frameLayout('frame1', l="Servers List", borderStyle='in', w=110, h=170, p='row1')
    mc.columnLayout('col2', rs=5, p='frame1')
    mc.radioCollection()
    mc.radioButton('one', l='#1', onc='OCT_menu.selectServer1()', p='col2')
    mc.radioButton('two', l='#2', onc='OCT_menu.selectServer2()', p='col2')
    mc.radioButton('three', l='#3', onc='OCT_menu.selectServer3()', p='col2')
    mc.radioButton('four', l='#4', onc='OCT_menu.selectServer4()', p='col2')
    mc.setParent('..')
    mc.frameLayout('frame2', l="Server Info", borderStyle='in', w=304, h=170, p='row1')
    mc.columnLayout('col3', rs=5, p='frame2')
    mc.scrollField('serverInfo', w=296, h=146, tx='', ww=True, ed=False, p='col3')
    mc.columnLayout('col4', w=414, cat=['both',3], p='col1', cw=414)
    mc.button('slButton', l='Select', c='OCT_menu.selectServer()', p='col4', en=False, w=100)
    mc.button('cancelButton', l='Cancel', c='mc.deleteUI("ServerUI",window=True)', p='col4', w=100)
    mc.showWindow('ServerUI')

def selectServer1():
    mc.waitCursor(state=True)
    path = os.getenv('PATH').split(';')
    addr = ''
    for eachPath in path:
        if 'Deadline/bin' in eachPath:
            addr = eachPath
            if os.path.isfile('%s/deadlinecommand.exe' % addr):
                break

    if addr == '':
        sys.stderr.write(u'找不到Deadline客户端安装目录,请安装Deadline客户端.')

    try:
        str = os.popen(r'"%s/deadlinecommand.exe" -ChangeRepository \\192.168.80.211\DeadlineRepository' % addr).read()
    except:
        sys.stderr.write(u'设定Deadline服务器时出错,请检查网络连接或权限.')
    else:
        try:
            str = os.popen(r'"%s/deadlinecommand.exe" -executescript \\octvision.com\cg\td\APP\RenderFarm\getServerInfo.py' % addr).read()
        except:
            sys.stderr.write('Error getting Server Info')
        else:
            mc.scrollField('serverInfo', e=True, tx=str)
            mc.button('slButton', e=True, en=True)

    mc.waitCursor(state=False)

def selectServer2():
    mc.waitCursor(state=True)
    path = os.getenv('PATH').split(';')
    addr = ''
    for eachPath in path:
        if 'Deadline/bin' in eachPath:
            addr = eachPath
            if os.path.isfile('%s/deadlinecommand.exe' % addr):
                break

    if addr == '':
        sys.stderr.write(u'找不到Deadline客户端安装目录,请安装Deadline客户端.\n')

    try:
        str = os.popen(r'"%s/deadlinecommand.exe" -ChangeRepository \\192.168.80.212\DeadlineRepository' % addr).read()
    except:
        sys.stderr.write(u'设定Deadline服务器时出错,请检查网络连接或权限.\n')
    else:
        try:
            str = os.popen(r'"%s/deadlinecommand.exe" -executescript \\octvision.com\cg\td\APP\RenderFarm\getServerInfo.py' % addr).read()
        except:
            sys.stderr.write('Error getting Server Info')
        else:
            mc.scrollField('serverInfo', e=True, tx=str)
            mc.button('slButton', e=True, en=True)

    mc.waitCursor(state=False)

def selectServer3():
    mc.waitCursor(state=True)
    path = os.getenv('PATH').split(';')
    addr = ''
    for eachPath in path:
        if 'Deadline/bin' in eachPath:
            addr = eachPath
            if os.path.isfile('%s/deadlinecommand.exe' % addr):
                break

    if addr == '':
        sys.stderr.write(u'找不到Deadline客户端安装目录,请安装Deadline客户端.\n')

    try:
        str = os.popen(r'"%s/deadlinecommand.exe" -ChangeRepository \\192.168.80.213\DeadlineRepository' % addr).read()
    except:
        sys.stderr.write(u'设定Deadline服务器时出错,请检查网络连接或权限.\n')
    else:
        try:
            str = os.popen(r'"%s/deadlinecommand.exe" -executescript \\octvision.com\cg\td\APP\RenderFarm\getServerInfo.py' % addr).read()
        except:
            sys.stderr.write('Error getting Server Info')
        else:
            mc.scrollField('serverInfo', e=True, tx=str)
            mc.button('slButton', e=True, en=True)

    mc.waitCursor(state=False)

def selectServer4():
    mc.waitCursor(state=True)
    path = os.getenv('PATH').split(';')
    addr = ''
    for eachPath in path:
        if 'Deadline/bin' in eachPath:
            addr = eachPath
            if os.path.isfile('%s/deadlinecommand.exe' % addr):
                break

    if addr == '':
        sys.stderr.write(u'找不到Deadline客户端安装目录,请安装Deadline客户端.\n')

    try:
        str = os.popen(r'"%s/deadlinecommand.exe" -ChangeRepository \\192.168.80.214\DeadlineRepository' % addr).read()
    except:
        sys.stderr.write(u'设定Deadline服务器时出错,请检查网络连接或权限.\n')
    else:
        try:
            str = os.popen(r'"%s/deadlinecommand.exe" -executescript \\octvision.com\cg\td\APP\RenderFarm\getServerInfo.py' % addr).read()
        except:
            sys.stderr.write('Error getting Server Info')
        else:
            mc.scrollField('serverInfo', e=True, tx=str)
            mc.button('slButton', e=True, en=True)

    mc.waitCursor(state=False)

def executeScript():
    try:
        str = os.popen(r'"deadlinecommand.exe" -ExecuteScript \\octvision.com\cg\td\APP\RenderFarm\MayaSubmission.py').read()
    except:
        pass
    else:
        sys.stdout.write(str)

def selectServer():
    ftpAddress = ''
    folder = ''
    v, b = mc.about(v=True).split(' ')
    version = 'Maya' + v

    if mc.radioButton('one', q=True, sl=True):
        ftpAddress = '192.168.80.221'
        folder = 'RenderFiles1'

    if mc.radioButton('two', q=True, sl=True):
        ftpAddress = '192.168.80.222'
        folder = 'RenderFiles2'

    if mc.radioButton('three', q=True, sl=True):
        ftpAddress = '192.168.80.223'
        folder = 'RenderFiles3'

    if mc.radioButton('four', q=True, sl=True):
        ftpAddress = '192.168.80.224'
        folder = 'RenderFiles4'

    try:
        import OCT_DL_uploadFile
        upload = OCT_DL_uploadFile.OCT_DL_uploadFile(ftpAddress, 21, folder, version)
    except:
        pass
    else:
        if mc.window('ServerUI', ex=True):
            mc.deleteUI('ServerUI', window=True)

        mc.waitCursor(state=True)
        upload.doUpload()
        del upload
        sys.stdout.write('Please wait for initialize submit a job script...')
        executeScript()
        mc.waitCursor(state=False)

def setProjRenderOpt_UI():
    if mc.windowPref("setProjRenderOpt_UI",exists=True):
        mc.windowPref("setProjRenderOpt_UI",remove=True)

    if mc.window('setProjRenderOpt_UI', ex=True):
        mc.deleteUI('setProjRenderOpt_UI', window=True)

    mc.window('setProjRenderOpt_UI', t=u'应用渲染设置', wh=[200, 80], mnb=False, mxb=False, rtf=True, s=False)
    mc.columnLayout(w=200, cat=['both',5], cw=200)
    mc.rowLayout(nc=2, h=80, cw2=[120,80], rat=[1,'both',5])
    mc.optionMenu(label=u'项目')
    mc.menuItem(label=u'请选择')
    mc.menuItem(label=u'飞越西部')
    mc.button('setOpt', l='Setup',w=60, c='OCT_menu.setProjRenderOpt()')
    mc.setParent('..')
    mc.showWindow('setProjRenderOpt_UI')

def setProjRenderOpt():
    if not mc.objExists('defaultResolution'):
        om.MGlobal.displayError(u'找不到defaultResolution节点...')
        return

    if not mc.objExists('defaultRenderGlobals'):
        om.MGlobal.displayError(u'找不到defaultRenderGlobals节点...')
        return

    selectionList = om.MSelectionList()
    selectionList.add('defaultResolution')
    r = om.MObject()
    selectionList.getDependNode( 0, r )

    rFn = om.MFnDependencyNode(r)
    attr = ['deviceAspectRatio']
    for each in attr:
        plug = rFn.findPlug(each)
        if not mc.getAttr('defaultResolution.%s' % each) == 1:
            if plug.isLocked():
                plug.setLocked(False)

            mc.setAttr('defaultResolution.%s' % each,1)

        if not plug.isLocked():
            plug.setLocked(True)
            #        plug.setLocked(False)

    selectionList = om.MSelectionList()
    selectionList.add('defaultRenderGlobals')
    g = om.MObject()
    selectionList.getDependNode(0, g)

    gFn = om.MFnDependencyNode(g)
    mc.setAttr('defaultRenderGlobals.imageFilePrefix','<Scene>',type='string')
    mc.setAttr('defaultRenderGlobals.animation',True)
    mc.setAttr('defaultRenderGlobals.putFrameBeforeExt',True)
    mc.setAttr('defaultRenderGlobals.outFormatControl',False)
    mc.setAttr('defaultRenderGlobals.periodInExt',True)
    padding = gFn.findPlug('extensionPadding')
    if not padding.isLocked():
        mc.setAttr('defaultRenderGlobals.extensionPadding',4)
        padding.setLocked(True)
