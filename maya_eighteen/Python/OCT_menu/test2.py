# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
import sys
import string
import os

def CreateMyVRayGammaCorrect_zwz():
    if not mc.objExists('MyVRayGammaCorrect'):
        MyVRGammaCorrect = mc.shadingNode('gammaCorrect', asUtility=True, n='MyVRayGammaCorrect')
        mc.setAttr('%s.gammaX'%MyVRGammaCorrect, 0.454)
        mc.setAttr('%s.gammaY'%MyVRGammaCorrect, 0.454)
        mc.setAttr('%s.gammaZ'%MyVRGammaCorrect, 0.454)
    else:
        MyVRGammaCorrect = 'MyVRayGammaCorrect'
    return MyVRGammaCorrect

#增加Vray的Gammera的模板
def AddGammeraNodeMode(myShader, myAttrAll, myAttrDetail, MyVRGammaCorrect):
    ConnectMode = 0
    myLColorOutV = ''
    #寻找coor链接
    try:
        myLColorOutV = mc.listConnections('%s.%s'%(myShader, myAttrAll), s=True, d=False, plugs=True)[0]
    except:
        pass
    else:
        ConnectMode = 1
    try:
        myLColorOutV = mc.listConnections('%s.%sR'%(myShader, myAttrDetail), s=True, d=False, plugs=True)[0]
    except:
        pass
    else:
        ConnectMode = 2
    #判断是否为hdr贴图，如果是不处理
    fileType = ''
    if ConnectMode != 0:
        conNode = ''
        try:
            conNode = mc.listConnections('%s.%s' % (myShader, myAttrAll))
        except:
            pass
        if conNode:
            if mc.nodeType(conNode) == 'file':
                pathName = mc.getAttr('%s.fileTextureName' % conNode[0])
                fileType = string.lower(os.path.splitext(pathName)[-1])
        #当存在链接、没有链接gammera节点、链接不含有hdr素材
        if myLColorOutV and myLColorOutV.find('GammaCorrect') < 0 and fileType.find('hdr') < 0:
            MyVRGammeNode = mc.duplicate(MyVRGammaCorrect, upstreamNodes=1)[0]
            if ConnectMode == 1:
                mc.disconnectAttr(myLColorOutV, '%s.%s' % (myShader, myAttrAll))
                mc.connectAttr(myLColorOutV, '%s.value' % MyVRGammeNode)
                mc.connectAttr('%s.outValue'%MyVRGammeNode, '%s.%s' % (myShader, myAttrAll))
            elif ConnectMode == 2:
                mc.disconnectAttr(myLColorOutV, '%s.%sR' % (myShader, myAttrDetail))
                mc.connectAttr(myLColorOutV, '%s.valueX' % MyVRGammeNode)
                mc.connectAttr('%s.outValueX' % MyVRGammeNode, '%s.%sR'%(myShader, myAttrDetail))
                try:
                    myLColorOutVG = mc.listConnections('%s.%sG' % (myShader, myAttrDetail), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    mc.disconnectAttr(myLColorOutVG, '%s.%sG' % (myShader, myAttrDetail))
                    mc.connectAttr(myLColorOutVG, '%s.valueY' % MyVRGammeNode)
                    mc.connectAttr('%s.outValueY' % MyVRGammeNode, '%s.%sG'%(myShader, myAttrDetail))
                try:
                    myLColorOutVB = mc.listConnections('%s.%sB' % (myShader, myAttrDetail), s=True, d=False, plugs=True)[0]
                except:
                    pass
                else:
                    mc.disconnectAttr(myLColorOutVB, '%s.%sB' % (myShader, myAttrDetail))
                    mc.connectAttr(myLColorOutVB, '%s.valueZ' % MyVRGammeNode)
                    mc.connectAttr('%s.outValueZ' % MyVRGammeNode, '%s.%sB'%(myShader, myAttrDetail))
    else:
        myColorV = mc.getAttr('%s.%s' % (myShader, myAttrAll))[0]
        if myColorV != (1.0, 1.0, 1.0) and myColorV != (0.0, 0.0, 0.0):
            MyVRGammeNode = mc.duplicate(MyVRGammaCorrect, upstreamNodes=1)[0]
            myColorV = mc.getAttr('%s.%s'% (myShader, myAttrAll))[0]
            mc.setAttr("%s.value" % MyVRGammeNode, myColorV[0], myColorV[1], myColorV[2], type="double3")
            mc.connectAttr('%s.value' % MyVRGammeNode, '%s.%s'% (myShader, myAttrAll))

#在Vray的标准材质、SSS材质、层材质、代理材质中添加Gammera
def VrayShaderAddCorrect(allSelShader,  MyVRGammaCorrect):
    for each in allSelShader:
        mc.select(cl=True)
        try:
            type = mc.nodeType(each)
        except:
            print "None Type object is unsubscriptable"
        else:
            if type == 'layeredShader':
                AllLayerShaderCon = mc.listAttr("%s.inputs" % each, m=True)
                if AllLayerShaderCon:
                    NextLSD = []
                    AllLyaerShaderNode = []
                    for eachLayerCon in AllLayerShaderCon:
                        if eachLayerCon.find('.') < 0:
                            AllLyaerShaderNode.append(eachLayerCon)
                    for eachLayerNode in AllLyaerShaderNode:
                        try:
                            myLColorOutV = mc.listConnections('%s.%s.color'%(each, eachLayerNode), s=True, d=False, plugs=True)[0]
                        except:
                            pass
                        try:
                            myLColorOutV = mc.listConnections('%s.%.colorR'%(each, eachLayerNode), s=True, d=False, plugs=True)[0]
                        except:
                            pass
                        if myLColorOutV:
                            myLConnect = myLColorOutV.split('.')[0]
                            if NextLSD.count('%s' % myLConnect) <= 0:
                                NextLSD.append(myLConnect)
                        if len(NextLSD):
                            VrayShaderAddCorrect(NextLSD, MyVRGammaCorrect)
                elif type == 'VRayMeshMaterial':
                    connectNodes = mc.listConnections(each, c=True, d=False, s=True, scn=True)
                    if connectNodes:
                        NextVMSD = []
                        for tmpCon in connectNodes:
                            if tmpCon.find('shaders') >= 0:
                                tmpVMNode = mc.listConnections(tmpCon)[0]
                                NextVMSD.append(tmpVMNode)
                        VrayShaderAddCorrect(NextVMSD, MyVRGammaCorrect)
            elif type == "VRayMtl":
                #color属性
                myColorAttrAll = 'color'
                myColorAttrDetail = 'diffuseColor'
                AddGammeraNodeMode(each, myColorAttrAll, myColorAttrDetail, MyVRGammaCorrect)
                #反射属性
                mySpeAttrAll = '.reflectionColor'
                mySpeAttrDetail = 'reflectionColor'
                AddGammeraNodeMode(each, mySpeAttrAll, mySpeAttrDetail, MyVRGammaCorrect)
            elif type == "VRayFastSSS2":
                #漫反射属性
                myDiffuseCAttrAll = 'diffuseTex'
                myDiffuseCDetail = 'diffuseTex.diffuseTex'
                AddGammeraNodeMode(each, myDiffuseCAttrAll, myDiffuseCDetail, MyVRGammaCorrect)
                #subfaceColor属性
                mySubSCAttrAll = 'subsurfaceColor'
                mySubSCDetail = 'subsurfaceColor.subsurfaceColor'
                AddGammeraNodeMode(each, mySubSCAttrAll, mySubSCDetail, MyVRGammaCorrect)
                #scatterR属性
                myScaRCAttrAll = 'scatterRadiusColor'
                myScaRCAttrDetail = 'scatterRadiusColor.scatterRadiusColor'
                AddGammeraNodeMode(each, myScaRCAttrAll, myScaRCAttrDetail, MyVRGammaCorrect)

#在HairSystem添加Gammera
def VrayHairsystemAddCorrect(allHairSystems, MyVRGammaCorrect):
    for each in allHairSystems:
        #hairColor属性
        myHairCAttrAll = 'hairColor'
        myHairCAttrDetail = 'hairColor.hairColor'
        AddGammeraNodeMode(each, myHairCAttrAll, myHairCAttrDetail, MyVRGammaCorrect)
        #soecularColor属性
        myHairSAttrAll = 'specularColor'
        myHairSAttrDetail = 'specularColor.specularColor'
        AddGammeraNodeMode(each, myHairSAttrAll, myHairSAttrDetail, MyVRGammaCorrect)
        #haitColorScale属性
        AllHairColorScaleCS = mc.listAttr("%s.hairColorScale" % each, m=True)
        if AllHairColorScaleCS:
            AllHairCNode = []
            for eachLayerCon in AllHairColorScaleCS:
                if eachLayerCon.find('.') < 0:
                    AllHairCNode.append(eachLayerCon)
            for eachHNode in AllHairCNode:
                myTmpAttrAll = '%s.hairColorScale_Color' % eachHNode
                myTmpAttrDetail = '%s.hairColorScale_Color' % eachHNode
                AddGammeraNodeMode(each, myTmpAttrAll, myTmpAttrDetail, MyVRGammaCorrect)

def AssignVRayGamma_zwz():
    allSelShader = mc.ls(mat=True)
    try:
        allSelShader.remove('lambert1')
        allSelShader.remove('particleCloud1')
    except:
        pass
    if len(allSelShader) > 0:
        MyVRGammaCorrect = CreateMyVRayGammaCorrect_zwz()
        VrayShaderAddCorrect(allSelShader, MyVRGammaCorrect)

    allHairSystems = mc.ls(type='hairSystem')
    if len(allHairSystems):
        MyVRGammaCorrect = CreateMyVRayGammaCorrect_zwz()
        VrayHairsystemAddCorrect(allHairSystems, MyVRGammaCorrect)

