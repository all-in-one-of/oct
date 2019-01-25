# coding=utf-8

import maya.cmds as mc
import maya.mel as mm
import subprocess
import os


# 加载插件
class LoadHoudiniAsset_Polyreduse(object):
    def __init__(self):
        self.checkPlugin()
        self.loadOtlAsset()

    def checkPlugin(self):
        if not mc.pluginInfo('houdiniEngine', q=True, l=True):
            mc.loadPlugin('houdiniEngine.mll')

    def loadOtlAsset(self):
        reply = self.checkAssetNode()
        if reply:
            return
        try:
            mc.houdiniAsset(loadAsset = ["//octvision.com/CG/Tech/Vfx/houdini/otlsformaya/polyreduse tool.otl","Object/reduse_tool"])
        except:
            subprocess.check_output(r'start \\octvision\cg\Tech\maya_sixteen\moudules\houdini_crack\del_HoudiniServer.bat', shell=True)
            subprocess.check_output(r'start \\octvision\cg\Tech\maya_sixteen\moudules\houdini_crack\HoudiniServer.bat', shell=True)

            try:
                mc.houdiniAsset(loadAsset = ["//octvision.com/CG/Tech/Vfx/houdini/otlsformaya/polyreduse tool.otl","Object/reduse_tool"])
            except:
                mc.error(u'houdini 破解失败！请找技术部-傅凯晖！')
        self.checkAssetNode()

    def checkAssetNode(self):
        self.assetNode = self.getAssetNodeName()
        if self.assetNode:
            mc.setAttr("%s.splitGeosByGroup" % self.assetNode, 0)
            return 1
        else:
            return 0

    def getAssetNodeName(self):
        assNodeList = mc.ls(typ = 'houdiniAsset')
        assetNode = ''
        if assNodeList:
            for nodeName in assNodeList:
                filePath = mc.getAttr('%s.otlFilePath' %nodeName)
                if os.path.basename(filePath) == 'polyreduse tool.otl':
                    assetNode = nodeName
                    break
            return assetNode
        else:
            return 0


class ReductionFaceForHoudini(LoadHoudiniAsset_Polyreduse):
    def __init__(self):
        super(ReductionFaceForHoudini, self).__init__()

    # 窗口
    def showWindow(self):
        if mc.window('ReductionFace_Window', q=True, ex=True):
            mc.deleteUI('ReductionFace_Window')

        mc.window('ReductionFace_Window', t = u'批量减面工具')
        mc.paneLayout('panel_1', configuration='quad')
        mc.button(l = u'开始减面', c = lambda *arge:self.transformationModel(), p = 'panel_1')
        mc.showWindow('ReductionFace_Window')

    # 操作方法
    def transformationModel(self):
        self.getTransform()
        self.setZeroTransform()
        selectObj = mc.ls(sl = True, l = True)
        objDict = self.getObjDict(selectObj)
        if not objDict:
            return 0
        for objName, shapeName in objDict.iteritems():
            self.checkConnectAsset()
            self.connectAsset(objName, shapeName)
            assetObjName = self.checkAssetChildNode()
            if assetObjName[0]:
                objParent = ('|').join(objName.split('|')[:-1])
                if not objParent:
                    mc.parent(assetObjName[1], w = True)
                    nullObjFullName = ('|').join(['',assetObjName[2]])
                else:
                    mc.parent(assetObjName[1], objParent)
                    nullObjFullName = ('|').join([objParent, assetObjName[2]])
                self.deleteModel(objName, nullObjFullName)
            else:
                mc.delete(objName)
        self.setTransform()

    def checkAssetChildNode(self):
        childNode = mc.listRelatives(self.assetNode, c = True, f = True)
        twoChildNode = mc.listRelatives(childNode[0], c = True, f = True)
        shapeNode = mc.listRelatives(twoChildNode[0], s = True, f = True)
        if shapeNode and mc.nodeType(shapeNode[0]) == 'mesh':
            node = twoChildNode[0].split('|')[-1]
            return [1, twoChildNode[0], node]
        else:
            return [0]

    def deleteModel(self, oldName, newName):
        self.checkConnectAsset()
        # 将属性连接替换到新物体上
        self.replaceModel(oldName, newName)
        
        # 删除，改名
        mc.delete(oldName)
        mc.rename(newName, oldName.split('|')[-1])

        mc.flushUndo()
        
    def getTransform(self):
        self.translate = mc.getAttr('%s.translate' %self.assetNode)[0]
        self.rotate = mc.getAttr('%s.rotate' %self.assetNode)[0]
        self.scale = mc.getAttr('%s.scale' %self.assetNode)[0]

    def setTransform(self):
        mc.setAttr('%s.translate' %self.assetNode, self.translate[0], self.translate[1], self.translate[2])
        mc.setAttr('%s.rotate' %self.assetNode, self.rotate[0], self.rotate[1], self.rotate[2])
        mc.setAttr('%s.scale' %self.assetNode, self.scale[0], self.scale[1], self.scale[2])

    def setZeroTransform(self):
        mc.setAttr('%s.translate' %self.assetNode, 0, 0, 0)
        mc.setAttr('%s.rotate' %self.assetNode, 0, 0, 0)
        mc.setAttr('%s.scale' %self.assetNode, 1, 1, 1)

    def replaceModel(self, oldName, newName):
        self.replaceConnectionsAttr(oldName, newName)

        oldShapeName = mc.listRelatives(oldName, s = True, f = True)
        newShapeName = mc.listRelatives(newName, s = True, f = True)
        self.replaceConnectionsAttr(oldShapeName[0], newShapeName[0])

    def replaceConnectionsAttr(self, oldName, newName):
        self.deleteHistory(oldName)
        self.deleteHistory(newName)
        connectionsAttr = mc.listConnections(oldName, p = True, c = True)
        if connectionsAttr:
            for id in xrange(0, len(connectionsAttr), 2):
                nameList = connectionsAttr[id].split('.')
                nameList[0] = newName
                attrName = ('.').join(nameList)
                try:
                    mc.disconnectAttr(connectionsAttr[id], connectionsAttr[id+1])
                    mc.connectAttr('%s.%s' %(newName, attrName), connectionsAttr[id+1], na = True)
                except:
                    mc.warning(u'属性关联错误，%s,%s' % (connectionsAttr[id], connectionsAttr[id+1]))

    def deleteHistory(self, objName):
        mc.select(objName)
        mm.eval('DeleteHistory;')

    def getObjDict(self, objList):
        objDict = {}
        for obj in objList:
            nodeType = mc.nodeType(obj)
            if nodeType == 'mesh':
                transformObj = mc.listRelatives(obj, p = True, f = True)
                objDict[transformObj[0]] = obj
            else:
                shapeObj = mc.listRelatives(obj, s = True, f = True)
                if shapeObj:
                    if mc.nodeType(shapeObj) == 'mesh':
                        objDict[obj] = shapeObj[0]
                else:
                    newObjList = mc.listRelatives(obj, c = True, f = True)
                    if newObjList:
                        newObjDict = self.getObjDict(newObjList)
                        objDict.update(newObjDict)
        return objDict

    def checkConnectAsset(self):
        self.disconnectAsset('%s.input[0].inputGeo' % self.assetNode)
        self.disconnectAsset('%s.input[0].inputTransform' % self.assetNode)

    def connectAsset(self, polyName, polyShapeName):
        mc.connectAttr('%s.outMesh' %polyShapeName, '%s.input[0].inputGeo' % self.assetNode)
        mc.connectAttr('%s.worldMatrix' %polyName, '%s.input[0].inputTransform' % self.assetNode)
        mc.houdiniAsset(syn = '|%s' %self.assetNode)

    def disconnectAsset(self, attrName):
        connectObj = mc.listConnections(attrName, p = True)
        if connectObj:
            mc.disconnectAttr(connectObj[0], attrName)

