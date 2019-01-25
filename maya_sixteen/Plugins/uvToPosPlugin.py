import maya.OpenMayaMPx as mpx
import sys
import uvToPos

# intialize script plugins
def initializePlugin(mobject):
    mplugin = mpx.MFnPlugin(mobject, "ivancheung7@gmail.com", "1.0", "Any")
    try:
        mplugin.registerCommand( uvToPos.kPluginCmdName, uvToPos.cmdCreator, uvToPos.syntaxCreator)
        sys.stderr.write( "Register command complete: %s\n" % uvToPos.kPluginCmdName )
    except:
        sys.stderr.write("Failed to register command %s \n" % uvToPos.kPluginCmdName)
        raise    


#unitialize script plugins
def uninitializePlugin(mobject):
    mplugin = mpx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(uvToPos.kPluginCmdName)
    except:
        sys.stderr.write("Failed to unregister command %s\n" % uvToPos.kPluginCmdName)
        raise