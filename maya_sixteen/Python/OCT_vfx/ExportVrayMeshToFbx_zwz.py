#!/usr/bin/env python
# coding=utf-8
import maya.cmds as mc
import maya.mel as mm
import os


def ExportVrayMeshToFbx_ex(mode):
    myPlaneChangeFlag = False
    myactivePlane = ''
    i = 1
    while(i):
        try:
            tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
        except:
            pass
        else:
            if tmp:
                myactivePlane = 'modelPanel%d' % i
                break
        i += 1
    myActivePlaneV = mc.modelEditor(myactivePlane, q=True, da=True)
    if myActivePlaneV != "boundingBox":
        #mc.modelEditor(myactivePlane, e=True, da='boundingBox')
        myPlaneChangeFlag = True
    myAllVrayPath = []
    try:
        allVrayMeshs = mc.ls(type="VRayMesh")
    except:
        mc.warning(u'没有VrayMesh缓存')
    else:
        if allVrayMeshs:
            #判断如果有文件不存在退出
            for myVrayMesh in allVrayMeshs:
                myeachName = mc.getAttr('%s.fileName' % myVrayMesh)
                if not os.path.isfile(myeachName):
                    mc.confirmDialog(title=u'温馨提示', message=u'代理物体指定的路径找不到相应文件！', button=['OK'], defaultButton='Yes', dismissString='No')
                    #return False
            if not mc.pluginInfo('fbxmaya', query=True, loaded=True):
                mc.loadPlugin("fbxmaya")
            numAllVrayMeshs = len(allVrayMeshs)
            mc.progressWindow(title=u'正在导出VrayMesh为FBX到Data中！\n    请耐心等待', progress=0, status=u'即将开始', min=0, max=numAllVrayMeshs, isInterruptable=True)
            tmp = mc.workspace("FBX export", query=True, renderTypeEntry=True)
            myDataPath = mc.workspace(expandName=tmp)
            allMyVrayMeshs = []
            for i, myVrayMesh in enumerate(allVrayMeshs):
                # print u"正在导出第 %s 个，总共有 %s 个VrayMesh代理文件" % (i, numAllVrayMeshs)
                myVrayPath = mc.getAttr('%s.fileName' % myVrayMesh)
                myVrayMeshTran = ''
                VrayMeshCons = mc.listConnections(myVrayMesh)
                if VrayMeshCons:
                    for eachCon in VrayMeshCons:
                        if mc.nodeType(eachCon) == "transform":
                            myVrayMeshTran = eachCon
                            break
                if myVrayPath in myAllVrayPath:
                    continue
                elif myVrayMeshTran == '':
                    continue
                else:
                    myAllVrayPath.append(myVrayPath)
                    allMyVrayMeshs.append(myVrayMesh)
            if allMyVrayMeshs:
                for myVrayMesh in allMyVrayMeshs:
                    myVrayPath = mc.getAttr('%s.fileName' % myVrayMesh)
                    mc.setAttr("%s.reassignShaders" % myVrayMesh, 1)
                    myBaseName = os.path.basename(myVrayPath)
                    myFileName = os.path.splitext(myBaseName)[0]
                    myNerMeshTr = ""
                    if mode == 1:
                        mm.eval("vray restoreMesh %s;" % myVrayMesh)
                        myNewMeshShape = mc.ls(sl=True)
                        myNerMeshTr = mc.listRelatives(myNewMeshShape[0], f=True, p=True)[0]
                        mc.setAttr("%s.tx" % myNerMeshTr, 0)
                        mc.setAttr("%s.ty" % myNerMeshTr, 0)
                        mc.setAttr("%s.tz" % myNerMeshTr, 0)
                    elif mode == 2:
                        #print mode
                        BoxChangeFlag = False
                        MeshChangeFlag = False
                        myVrayMeshTran = ""
                        BoxFlag = mc.getAttr("%s.showBBoxOnly" % myVrayMesh)
                        MeshFlag = mc.getAttr("%s.showWholeMesh" % myVrayMesh)
                        if BoxFlag:
                            mc.setAttr("%s.showBBoxOnly" % myVrayMesh, 0)
                            BoxChangeFlag = True
                        if not MeshFlag:
                            mc.setAttr("%s.showWholeMesh" % myVrayMesh, 1)
                            MeshChangeFlag = True
                        #print myVrayMesh
                        VrayMeshCons = mc.listConnections(myVrayMesh)
                        if VrayMeshCons:
                            for eachCon in VrayMeshCons:
                                if mc.nodeType(eachCon) == "transform":
                                    myVrayMeshTran = eachCon
                                    break
                        if myVrayMeshTran:
                            myVrayMeshDTran = mc.duplicate(myVrayMeshTran, rr=True)
                            try:
                                myVrayMeshNew = mc.parent(myVrayMeshDTran, w=True)
                            except:
                                myVrayMeshNew = myVrayMeshDTran
                            myNerMeshTr = mc.ls(myVrayMeshNew, l=True)
                            if MeshChangeFlag:
                                mc.setAttr("%s.showWholeMesh" % myVrayMesh, MeshFlag)
                            if BoxChangeFlag:
                                mc.setAttr("%s.showBBoxOnly" % myVrayMesh, BoxFlag)
                    if myNerMeshTr:
                        myFileFullName = os.path.join(myDataPath, myFileName+".fbx")
                        myFileFullName = os.path.normpath(myFileFullName)
                        myNerMeshTr = mc.rename(myNerMeshTr, myFileName)
                        mc.select(myNerMeshTr)
                        mc.file(myFileFullName, force=True, options="v=0", type="FBX export", pr=True, es=True)
                        mc.delete(myNerMeshTr)
                        mc.progressWindow(edit=True, progress=i+1)
                        if mc.progressWindow(q=True, isCancelled=True):
                            break
            mc.progressWindow(endProgress=True)
            os.startfile(myDataPath)
        else:
            mc.warning(u'没有VrayMesh缓存')
    if myPlaneChangeFlag:
        mc.modelEditor(myactivePlane, e=True, da=myActivePlaneV)    