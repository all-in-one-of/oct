import maya.cmds as mc


def bake_Frame():
    info = {}
    min = int(mc.playbackOptions(q=True, min=True))
    max = int(mc.playbackOptions(q=True, max=True))
    selectObj = mc.ls(sl=True)
    mc.select(cl=True)
    if not selectObj:
        mc.error('please select obj')

    for timeNum in xrange(min,max+1):
        mc.currentTime(timeNum)
        for objName in selectObj:
            mc.select(objName)
            world_translate = mc.xform(q=True, ws=True, t=True)
            world_rotate = mc.xform(q=True, ws=True, ro=True)
            world_scale = mc.xform(q=True, ws=True, s=True)
            if objName in info:
                info[objName].update({timeNum:[world_translate, world_rotate, world_scale]})
            else:
                info[objName] = ({timeNum:[world_translate, world_rotate, world_scale]})
            

    for frameNum in xrange(min,max+1):
        for objName in info:
            attrName_t = '%s.translate' %(objName)
            attrName_ro = '%s.rotate' %(objName)
            attrName_sc = '%s.scale' %(objName)
        
            mc.currentTime(frameNum)
        
            mc.setAttr(attrName_t, info[objName][frameNum][0][0], info[objName][frameNum][0][1], info[objName][frameNum][0][2])
            mc.setAttr(attrName_ro, info[objName][frameNum][1][0], info[objName][frameNum][1][1], info[objName][frameNum][1][2])
            mc.setAttr(attrName_sc, info[objName][frameNum][2][0], info[objName][frameNum][2][1], info[objName][frameNum][2][2])
        
            mc.setKeyframe(objName)
