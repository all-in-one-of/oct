# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import random as rand
import math as math

#此工具运用了Yeti插件
class paint3dContext():
    authType = {
        'default': ('mesh',),
        'source': ('mesh','nurbsSurface', 'locator','aiStandIn'),
        'target': ('mesh',)
    }
    def __init__(self):
        self.windowName = 'paint3dContext_UI'
        self.windowSize = [350, 500]
        self.auth = self.authType['source'] 

        self.targetObj = ''
        self.transform = ''
        self.newPgYetiGroom = ''

        self.obj = {}
        if not mc.pluginInfo('pgYetiMaya.mll',q = True,l = True):
            mc.loadPlugin('pgYetiMaya.mll')

        self.paint3dContext_UI()

    def paint3dContext_UI(self):
        if mc.window(self.windowName, exists=True):
            mc.deleteUI(self.windowName)
        self.uiWin = mc.window(self.windowName, title = self.windowName, wh = self.windowSize, resizeToFitChildren = True, sizeable = False, titleBar = True, minimizeButton = False, maximizeButton = False, menuBar = False, menuBarVisible = False, toolbox = True)
        self.uiTopColumn = mc.columnLayout(adjustableColumn=True, columnAttach=('both', 5))
        self.uiTopForm = mc.formLayout(numberOfDivisions=100)
        self.uiBtnHelp = mc.button(label='Help', command=lambda * args:self.uiButtonCallback("uiBtnHelp", args))
        mc.formLayout(self.uiTopForm, edit=True, attachForm=[(self.uiBtnHelp, 'top', 0), (self.uiBtnHelp, 'left', 0)])
        
        mc.setParent(self.uiTopColumn)

        self.uiSourceFrame = mc.frameLayout(label='Paint Brush', cll=True, collapseCommand=lambda:self.resizeWindow('collapse', 90), expandCommand=lambda:self.resizeWindow('expand', 90), mh=5, mw=5)
        self.uiSourceForm = mc.formLayout(numberOfDivisions=100, width=300)
        self.uiCreateBtn = mc.button(l = u'创建', h = 28, command =lambda * args:self.genericContextCallback('create', args))
        self.uiDeleteBtn = mc.button(l = u'删除', h = 28, command =lambda * args:self.genericContextCallback('delete', args))
        self.uiMoveBtn = mc.button(l = u'移动', h = 28, command =lambda * args:self.genericContextCallback('move', args))
        self.distance = mc.floatSliderGrp( label='Minmum Distance', field=True, minValue = 0, maxValue = 100, fieldMaxValue = 2.0, precision = 2, value = 8, vis = True, w=310, cw=[(1, 95), (2, 95)], changeCommand=lambda * args:self.uiFluxCallback("distance", args))
        self.brushRadius = mc.floatSliderGrp(label='Brush Radius', field = True,minValue = 0, maxValue = 100, fieldMaxValue = 2.0, precision = 2, value = 15, vis = True, w=310, cw=[(1, 95), (2, 95)], changeCommand=lambda * args:self.uiFluxCallback("brushRadius", args))
        mc.formLayout(self.uiSourceForm, edit=True, attachForm=[(self.uiCreateBtn, 'top', 0), (self.uiDeleteBtn, 'top', 0), (self.uiMoveBtn, 'top', 0)], 
                    attachControl=[(self.uiDeleteBtn, 'left', 10, self.uiCreateBtn), (self.uiMoveBtn, 'left', 10, self.uiDeleteBtn), (self.distance, 'top', 10, self.uiCreateBtn),(self.brushRadius, 'top', 10, self.distance)],
                    attachPosition=[(self.uiCreateBtn, 'left', 0, 0), (self.uiCreateBtn, 'right', 0, 30), (self.uiDeleteBtn, 'left', 0, 33), (self.uiDeleteBtn, 'right', 0, 63),(self.uiMoveBtn, 'left', 0, 66), (self.uiMoveBtn, 'right', 0, 99)])
        
        mc.setParent(self.uiTopColumn)


        self.uiTargetFrame = mc.frameLayout(label='Target object', cll=True, collapseCommand=lambda:self.resizeWindow('collapse', 230), expandCommand=lambda:self.resizeWindow('expand', 230), mh=5, mw=5)
        self.uiTargetForm = mc.formLayout(numberOfDivisions=100, width=300)
        self.uiSourceList = mc.textScrollList(numberOfRows=5, allowMultiSelection=True, width=300)
        self.uiSourceBtnAdd = mc.symbolButton(w = 90, h = 18, ann='Add selected object(s) to the list', image='sp3dadd.xpm', command=lambda * args:self.uiListCallback("add", "uiSourceList"))
        self.uiSourceBtnRem = mc.symbolButton(w = 90, h = 18, ann='Remove selected object(s) from the list', image='sp3drem.xpm', command=lambda * args:self.uiListCallback("rem", "uiSourceList"))
        self.uiSourceBtnClr = mc.symbolButton(w = 90, h = 18, ann='Clear the list', image='sp3dclr.xpm', command=lambda * args:self.uiListCallback("clr", "uiSourceList"))
        
        self.duplicate = mc.checkBox(label= u'关联复制', h = 28)
        self.uiScaleCheck = mc.checkBox(label='Scale')
        self.ScaleFieldX = mc.floatFieldGrp(numberOfFields=2, label='Min', extraLabel='Max', cw4=(22, 50, 50, 30), precision=2, co4=(2, 2, 2, 8), v1=1.0, v2=1.0)
       
        self.RotateCheck = mc.checkBox(label='Rotate')
        self.RotateFieldX = mc.floatFieldGrp(numberOfFields=2, label='Min', extraLabel='Max', cw4=(22, 50, 50, 30), precision=2, ct4=('right', 'both', 'both', 'right'), co4=(2, 2, 2, 8))
        self.RotateFieldY = mc.floatFieldGrp(numberOfFields=2, label='Min',  extraLabel='Max', cw4=(22, 50, 50, 30), precision=2, ct4=('right', 'both', 'both', 'right'), co4=(2, 2, 2, 8))
        self.RotateFieldZ = mc.floatFieldGrp(numberOfFields=2, label='Min', extraLabel='Max', cw4=(22, 50, 50, 30), precision=2, ct4=('right', 'both', 'both', 'right'), co4=(2, 2, 2, 8)) 

        self.uiAlign = mc.checkBox(label= u'法线', h = 28)

        self.uiReplaceBtn = mc.button(l = u'替换', h = 28, command =lambda * args:self.replaceCallback('replace', args))

        mc.formLayout(self.uiTargetForm, edit=True, attachForm=[(self.uiSourceList, 'top', 0),(self.uiReplaceBtn, 'left', 0), (self.uiReplaceBtn, 'right', 0), (self.uiReplaceBtn, 'bottom', 0)],
                    attachControl=[(self.uiSourceBtnAdd, 'top', 3, self.uiSourceList), (self.uiSourceBtnRem, 'left', 5, self.uiSourceBtnAdd), (self.uiSourceBtnRem, 'top', 3, self.uiSourceList), (self.uiSourceBtnClr, 'left', 5, self.uiSourceBtnRem), (self.uiSourceBtnClr, 'top', 3, self.uiSourceList),
                    (self.uiAlign, 'top', 10, self.uiSourceBtnAdd), (self.duplicate, 'top', 10, self.uiAlign), (self.uiScaleCheck, 'top', 10, self.duplicate),
                    (self.ScaleFieldX, 'left', 30, self.uiScaleCheck), (self.ScaleFieldX, 'top', 10, self.duplicate), (self.RotateCheck, 'top', 10, self.uiScaleCheck), (self.RotateFieldX, 'left', 30, self.uiScaleCheck),
                    (self.RotateFieldX, 'top', 10, self.uiScaleCheck), (self.RotateFieldY, 'top', 10, self.RotateFieldX), (self.RotateFieldZ, 'top', 10, self.RotateFieldY), (self.RotateFieldY, 'left', 30, self.uiScaleCheck), 
                    (self.RotateFieldZ, 'left', 30, self.uiScaleCheck), (self.uiReplaceBtn, 'top', 20, self.RotateFieldZ)])
       
        mc.setParent(self.uiTopColumn)

        mc.showWindow(self.uiWin)

    #笔刷
    def genericContextCallback(self, *args):
        if ( (mc.upAxis(q=True, axis=True)) == "y" ):
            self.worldUp = om.MVector (0,1,0);
        elif ( (mc.upAxis(q=True, axis=True)) == "z" ):
            self.worldUp = om.MVector (0,0,1);
        else:
            #can't figure out up vector
            mc.confirmDialog(title='Weird stuff happening', message='Not getting any proper info on what the current up vector is. Quitting...')
            sys.exit()

        if args[0] == 'create':
            if not self.pgYetiCreateGroomMesh():
                return
            combContext = mm.eval('pgYetiGroomContext')
            mc.select(self.newPgYetiGroom, r = True)
            mc.setToolTo(combContext)
            mc.setAttr('%s.brushMode'%self.newPgYetiGroom, 2)
            mc.setAttr('%s.populateMode'%self.newPgYetiGroom, 2)
        elif args[0] == 'delete':
            if not self.transform or not mc.objExists(self.transform):
                mc.confirmDialog(message = u'请先点创建按钮！')
                return
            combContext = mm.eval('pgYetiGroomContext')
            mc.select(self.newPgYetiGroom, r = True)
            mc.setToolTo(combContext)
            mc.setAttr('%s.brushMode'%self.newPgYetiGroom, 2)
            mc.setAttr('%s.populateMode'%self.newPgYetiGroom, 1)
        elif args[0] == 'move':
            if not self.transform or not mc.objExists(self.transform):
                mc.confirmDialog(message = u'请先点创建按钮！')
                return
            combContext = mm.eval('pgYetiGroomContext')
            mc.select(self.newPgYetiGroom, r = True)
            mc.setToolTo(combContext)
            mc.setAttr('%s.brushMode'%self.newPgYetiGroom, 0)
            mc.setAttr('%s.toolMode'%self.newPgYetiGroom, 5)

    def replaceCallback(self, *args):
        self.classIf = {}
        if not self.obj:
            mc.confirmDialog(message = u'请添加目标物体放入列表中！')
            return

        duplicateValue = mc.checkBox(self.duplicate, q = True, v = True)
        oldNurbs = mc.ls(type = 'nurbsCurve')
        Scale = []
        RotateX = ''
        RotateY = ''
        RotateZ = ''
       
        if mc.checkBox(self.uiScaleCheck, q = True, v = True):
            Scale = [mc.floatFieldGrp(self.ScaleFieldX, q=True, v1=True), mc.floatFieldGrp(self.ScaleFieldX, q=True, v2=True)]
        if mc.checkBox(self.RotateCheck, q= True, v = True):
            RotateX = [mc.floatFieldGrp(self.RotateFieldX, q=True, v1=True), mc.floatFieldGrp(self.RotateFieldX, q=True, v2=True)]
            RotateY = [mc.floatFieldGrp(self.RotateFieldY, q=True, v1=True), mc.floatFieldGrp(self.RotateFieldY, q=True, v2=True)]
            RotateZ = [mc.floatFieldGrp(self.RotateFieldZ, q=True, v1=True), mc.floatFieldGrp(self.RotateFieldZ, q=True, v2=True)]

        if self.newPgYetiGroom and self.obj:
            mc.pgYetiCommand(self.newPgYetiGroom, convertToCurves = True)
            newNurbs = mc.ls(type = 'nurbsCurve') 
            nurbsObjs = list(set(newNurbs) - set(oldNurbs))
            if nurbsObjs:
                for objs in nurbsObjs:
                    transformNode = mc.listRelatives(objs, p = True)[0]
                    transf = mc.xform('%s.cv[0]'%transformNode, q=True, ws=True, t=True)
                    dkeys = self.obj.keys()
                    dag = self.obj[dkeys[rand.randint(0, len(dkeys) - 1)]]
                    shapeParent = mc.listRelatives(dag, parent = True)
                    if duplicateValue:
                        newObjectDAG = mc.instance(shapeParent[0])
                    else:
                        newObjectDAG = mc.duplicate(shapeParent[0], un=True, ic=True)
                        
                    mc.move(transf[0],transf[1],transf[2], newObjectDAG[0], relative=True) 
                    if mc.checkBox(self.uiAlign, q = True, v = True):
                        self.align(transf, newObjectDAG[0])
                    if Scale:
                        ScaleXYZ = (round(rand.uniform(Scale[0], Scale[1]), 3))
                        mc.scale(ScaleXYZ, ScaleXYZ, ScaleXYZ, newObjectDAG[0], relative=True)
                    if RotateX:
                        randx = (round(rand.uniform(RotateX[0], RotateX[1]), 3))
                        randy = (round(rand.uniform(RotateY[0], RotateY[1]), 3))
                        randz = (round(rand.uniform(RotateZ[0], RotateZ[1]), 3))
                        mc.rotate(randx, randy, randz, newObjectDAG[0], os=True, r=True, rotateXYZ=True)

                    if not dag in self.classIf.keys():
                        self.classIf.update({dag : [newObjectDAG[0]]})
                    else:
                        self.classIf[dag].append(newObjectDAG[0])
                    mc.delete(transformNode)

            mc.delete(self.transform)
            self.transform = ''
            self.newPgYetiGroom = ''

        groupsName = mc.group(empty = True, name = 'group#')
        for key in self.classIf.keys():
            keyName = key.split('|')[-1]
            groupName = mc.group(empty = True, name = keyName)
            mc.parent(self.classIf[key], groupName, relative=True)
            mc.parent(groupName, groupsName, relative=True)

   
    def align(self, transf, dag):
        normal = self.getHitNormal(transf)
        rx, ry, rz = self.getEulerRotationQuaternion(self.worldUp, normal)
        mc.xform(dag, ro=(rx, ry, rz) )

    def getEulerRotationQuaternion(self, upvector, directionvector):
        quat = om.MQuaternion(upvector, directionvector)
        quatAsEuler = om.MEulerRotation()
        quatAsEuler = quat.asEulerRotation()
        return math.degrees(quatAsEuler.x), math.degrees(quatAsEuler.y), math.degrees(quatAsEuler.z)


    def getHitNormal(self, transf):
        targetDAGPath = self.getDAGObject()
        normal = om.MVector()
        fnMesh = om.MFnMesh(targetDAGPath)
        hitPoint = om.MPoint(transf[0], transf[1], transf[2])
        fnMesh.getClosestNormal(hitPoint, normal, om.MSpace.kWorld, None);
        return normal;

    def getDAGObject(self):
        sList = om.MSelectionList()
        meshDP = om.MDagPath()
        om.MGlobal.getSelectionListByName(self.targetObj, sList)
        sList.getDagPath(0,meshDP)
        return meshDP

    #笔刷和距离的控制
    def uiFluxCallback(self, *args):
        if not self.newPgYetiGroom and not mc.objExists(self.newPgYetiGroom):
            mc.confirmDialog(message = u'请先点创建按钮！')
            return
            
        if args[0] == 'distance':
            value = mc.floatSliderGrp(self.distance, q = True, value = True)
            mc.setAttr('%s.minimumStrandDistance'%self.newPgYetiGroom, value)
        elif args[0] == 'brushRadius':
            value = mc.floatSliderGrp(self.brushRadius, q = True, value = True)
            mc.setAttr('%s.brushRadius'%self.newPgYetiGroom, value)

    #创建groom节点
    def pgYetiCreateGroomMesh(self):
        selectedMeshNodes = mc.ls(sl = True, dag = True, ni = True, type = 'mesh')
        if len(selectedMeshNodes) != 1:
            mc.confirmDialog(message = u'请选择一个被种植的物体,再回来！')
            return False
        else:
            self.targetObj = selectedMeshNodes[0]
            connect = mc.listConnections('%s.worldMesh[0]'%self.targetObj, s = False, d = True, shapes = True)
            if connect:
                for con in connect:
                    if mc.objectType(con) == 'pgYetiGroom' and 'paint' in con:
                        self.newPgYetiGroom = con
                        self.transform = mc.listRelatives(con, p = True)[0]
                        return True

            self.transform = mc.createNode('transform', name = 'paint#')
            self.newPgYetiGroom = mc.createNode('pgYetiGroom', name = '%sShape'%self.transform, p = self.transform)
            mc.connectAttr('%s.worldMesh[0]'%selectedMeshNodes[0], '%s.inputGeometry'%self.newPgYetiGroom)
            mc.connectAttr('time1.outTime', '%s.currentTime'%self.newPgYetiGroom)
            value = mc.floatSliderGrp(self.distance, q = True, value = True)
            mc.setAttr('%s.minimumStrandDistance'%self.newPgYetiGroom, value)
            value1 = mc.floatSliderGrp(self.brushRadius, q = True, value = True)
            mc.setAttr('%s.brushRadius'%self.newPgYetiGroom, value1)

            mc.setAttr('%s.initialStrandLength'%self.newPgYetiGroom, 1)
            mc.setAttr('%s.strandSegmentLength'%self.newPgYetiGroom, 1)

            return True

    #添加对象列表中
    def uiListCallback(self, *args):
        mode = args[0]
        textlist = args[1]
        if (mode == 'add'):
            #ADD
            self.auth = self.authType['source'] 
            objselected = mc.ls(selection=True, long = True)
            for obj in objselected:
                objtype = mc.objectType(obj)
                objchild = mc.listRelatives(obj, children=True, shapes=True, f = True)
                if objchild:
                    objchildSplit = objchild[0].split('|')[-1]

                if (objtype in self.auth):
                    if objchildSplit in self.obj:
                        continue
                    self.obj.update({objchildSplit : objchild[0]})
                    mc.textScrollList(self.__dict__[textlist], edit=True, append = objchildSplit)

                elif (objtype == 'transform'):
                    if (len(objchild) <= 2 and mc.nodeType(objchild[0]) in self.auth):
                        if objchildSplit in self.obj:
                            continue
                        self.obj.update({objchildSplit : objchild[0]})
                        mc.textScrollList(self.__dict__[textlist], edit=True, append = objchildSplit)
            
        elif(mode == 'clr'):
            mc.textScrollList(self.__dict__[textlist], edit=True, removeAll=True)
            self.obj.clear()

        elif(mode == 'rem'):
            remlist = mc.textScrollList(self.__dict__[textlist], query=True, selectItem=True)
            if(remlist):
                for remobj in remlist:
                    del self.obj[remobj]
                    mc.textScrollList(self.__dict__[textlist], edit=True, removeItem = remobj);
    
    #将调整窗口的大小，用折叠/展开帧时调整窗口大小。
    def resizeWindow(self, direction, offset):
        if mc.window(self.windowName, exists=True):
            currentSize = mc.window(self.uiWin, query=True, height=True)
            if (direction == 'collapse'):
                currentSize -= offset
            elif (direction == 'expand'):
                currentSize += offset
            elif (direction == 'winui'):
                currentSize = offset
            if(currentSize > 0):
                mc.window(self.uiWin, edit=True, height=currentSize);

    #帮助
    def uiButtonCallback(self, *args):
        mc.confirmDialog(title = 'paint3dContext Help', message = u'此工具运用了Yeti插件！', button='Whatever');
    
# paint3dContext()

