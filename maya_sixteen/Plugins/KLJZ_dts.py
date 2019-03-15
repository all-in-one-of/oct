# coding=utf-8

#---------------------------------------------
# 针对KLJZ项目制作的插件
# 随着离相机越近，物体越小
#---------------------------------------------

import DistanceToScale_Node as distanceNode
import maya.OpenMayaMPx as mpx

# initiallize the script plug-in
def initializePlugin(mobject):
    mplugin = mpx.MFnPlugin(mobject)
    try:
        mplugin.registerNode(distanceNode.kPluginNodeTypeName, distanceNode.dstNodeId, distanceNode.nodeCreator, distanceNode.nodeInitialize)
    except:
        sys.stderr.write('Failed to register node: %s' %kPluginNodeTypeName)
        raise


# uninitiallize the script plug-in
def uninitializePlugin(mobject):
    mplugin = mpx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode(distanceNode.dstNodeId)
    except:
        sys.stderr.write('Failed to unregister node: %s' %kPluginNodeTypeName)
        raise
