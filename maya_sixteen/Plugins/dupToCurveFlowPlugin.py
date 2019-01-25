import maya.OpenMayaMPx as mpx
import sys
import dupToCurveFlow

def initializePlugin(mobject):
	mplugin = mpx.MFnPlugin(mobject,'ivancheung7@gmail.com','1.0','Any')
	try:
		mplugin.registerNode(dupToCurveFlow.kPluginNodeTypeName,dupToCurveFlow.kPluginNodeId,dupToCurveFlow.nodeCreator,dupToCurveFlow.nodeInitializer,mpx.MPxNode.kDependNode)
	except:
		sys.stderr.write('failed to register node: %s' % dupToCurveFlow.kPluginNodeTypeName)
		raise
		
def uninitializePlugin(mobject):
	mplugin = mpx.MFnPlugin(mobject)
	try:
		mplugin.deregisterNode(dupToCurveFlow.kPluginNodeId)
	except:
		sys.stderr.write('Failed to register node: %s' % dupToCurveFlow.kPluginNodeTypeName)
		raise