import maya.OpenMaya as om
import maya.OpenMayaMPx as mpx
import sys, math

kPluginCmdName = 'IC_getAngle'

kOrignalFlag = '-o'
kOrignalLongFlag = '-orignal'
kTargetFlag = '-t'
kTargetLongFlag = '-target'


class getAngle(mpx.MPxCommand):
    def __init__(self):
        mpx.MPxCommand.__init__(self)
    
    def doIt(self, args):
        argData = om.MArgDatabase(self.syntax(), args)
        if argData.isFlagSet(kOrignalFlag):
            origName = argData.flagArgumentString(kOrignalFlag, 0)
        else:
            om.MGlobal.displayError('Flag -orignal/-o must be specfied.')
            return
        
        if argData.isFlagSet(kTargetFlag):
            targetName = argData.flagArgumentString(kTargetFlag, 0)
        else:
            om.MGlobal.displayError('Flag -target/t must be specfied.')
            return
        
        try:
            thisObj = nameToDag(origName)
        except:
            om.MGlobal.displayError('%s object not found...' % origName)
            raise
        
        try:
            targetObj = nameToDag(targetName)
        except:
            om.MGlobal.displayError('%s object not found...' % targetObj)
            raise
        
        thisFnTrans = om.MFnTransform(thisObj)
        targetFnTrans = om.MFnTransform(targetObj)
        
        frontVec = om.MVector(0.0, 0.0, -1.0)

        thisVec = thisFnTrans.getTranslation(om.MSpace.kWorld)
        thisRotQuat = om.MQuaternion()
        thisFnTrans.getRotation(thisRotQuat, om.MSpace.kWorld)
        invertRot = thisRotQuat.inverse()
        
        rotThis = thisVec.rotateBy(invertRot)
        #afterRot = frontVec.rotateBy(thisRotQuat)
        
        targetVec = targetFnTrans.getTranslation(om.MSpace.kWorld)
        rotTarget = targetVec.rotateBy(invertRot)
        
        #if thisVec.x == 0.0 and thisVec.y == 0.0 and thisVec.z == 0.0:
            #thisVec = om.MVector(0.0, 0.0, -1.0)
        
        if rotTarget.x == 0.0 and rotTarget.y == 0.0 and rotTarget.z == 0.0:
            rotTarget = om.MVector(0.0, 0.0, -1.0)
        
        #thisVec = om.MVector(ox, oy, oz)
        
        #convert targetVec world space to the thisVec object space
        convertVec = rotTarget - rotThis
        
        if frontVec == convertVec:
            mpx.MPxCommand.clearResult()
            _result = om.MDoubleArray()
            _result.append(0.0)
            _result.append(0.0)
            _result.append(0.0)
            mpx.MPxCommand.setResult(_result)
        
        #length
        convertLength = convertVec.length()
        scaleVec = frontVec * convertLength
        agl = scaleVec.angle(convertVec)
        tempVec = scaleVec.rotateBy(om.MVector.kYaxis, agl)
        if tempVec.isEquivalent(convertVec,0.01):
            rotY = round(math.degrees(agl), 8)
        else:
            rotY = round(math.degrees(agl*-1), 8)

        #convert radians angle to degrees angle
        rotX = round(0.0, 8)
        #rotY = round(math.degrees(erVector.y), 8)
        rotZ = round(0.0, 8)
        
        _result = om.MDoubleArray()
        _result.append(rotX)
        _result.append(rotY)
        _result.append(rotZ)
        
        mpx.MPxCommand.clearResult()
        mpx.MPxCommand.setResult(_result)
      

def cmdCreator():
    return mpx.asMPxPtr(getAngle())


def syntaxCreator():
    syntax = om.MSyntax()
    syntax.addFlag(kOrignalFlag, kOrignalLongFlag, om.MSyntax.kString)
    syntax.addFlag(kTargetFlag, kTargetLongFlag, om.MSyntax.kString)
    return syntax


def nameToDag(name):
    selectionList = om.MSelectionList()
    selectionList.add(name)
    path = om.MDagPath()
    selectionList.getDagPath(0, path)
    return path
