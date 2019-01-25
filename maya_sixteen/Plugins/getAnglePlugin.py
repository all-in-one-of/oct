import maya.OpenMayaMPx as mpx
import sys
import getAngle

def initializePlugin(mobject):
    mplugin = mpx.MFnPlugin(mobject, 'ivancheung7@gmail.com','1.0','Any')
    try:
        mplugin.registerCommand(getAngle.kPluginCmdName, getAngle.cmdCreator, getAngle.syntaxCreator)
        sys.stderr.write('Register command complete: %s\n' % getAngle.kPluginCmdName)
    except:
        sys.stderr.write('Failed to register command %s \n' % getAngle.kPluginCmdName)
        raise
    
def uninitializePlugin(mobject):
    mplugin = mpx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(getAngle.kPluginCmdName)
    except:
        sys.stderr.write('Failed to unregister command %s \n' % getAngle.kPluginCmdName)
        raise
