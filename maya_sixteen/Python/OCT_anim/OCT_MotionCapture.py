# *-* coding=utf-8
__author__ = 'yangh'

import maya.cmds as mc
import maya.mel as mm

def motionCapture():
    allSelectObjs = mc.ls(sl = True)
    if len(allSelectObjs) != 2:
        mc.confirmDialog(message = u"请选择两个locator!")
        return
    for obj in allSelectObjs:
        childObj = mc.listRelatives(obj, c=True)[0]
        if mc.objectType(childObj) != "locator":
            mc.confirmDialog(message = u"请选择两个locator!")
            return
    name = mc.createNode("locator")
    parentLocator = mc.listRelatives(name, p=True)[0]
    mc.addAttr(parentLocator, ln="switch", at="double", min=1, max=2, dv=1)
    mc.setAttr("%s.switch"%parentLocator, e=True, keyable=True)

    translateXStr = "%s.translateX = %s.translateX * fmod(%s.switch + 1,2) + %s.translateX * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)
    translateYStr = "%s.translateY = %s.translateY * fmod(%s.switch + 1,2) + %s.translateY * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)
    translateZStr = "%s.translateZ = %s.translateZ * fmod(%s.switch + 1,2) + %s.translateZ * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)

    rotateXStr = "%s.rotateX = %s.rotateX * fmod(%s.switch + 1,2) + %s.rotateX * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)
    rotateYStr = "%s.rotateY = %s.rotateY * fmod(%s.switch + 1,2) + %s.rotateY * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)
    rotateZStr = "%s.rotateZ = %s.rotateZ * fmod(%s.switch + 1,2) + %s.rotateZ * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)

    scaleXStr = "%s.scaleX = %s.scaleX * fmod(%s.switch + 1,2) + %s.scaleX * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)
    scaleYStr = "%s.scaleY = %s.scaleY * fmod(%s.switch + 1,2) + %s.scaleY * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)
    scaleZStr = "%s.scaleZ = %s.scaleZ * fmod(%s.switch + 1,2) + %s.scaleZ * fmod(%s.switch,2);\\n"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)

    visibilityStr = r"%s.visibility = %s.visibility * fmod(%s.switch + 1,2) + %s.visibility * fmod(%s.switch,2);"%(parentLocator,allSelectObjs[0],parentLocator,allSelectObjs[1],parentLocator)

    str = translateXStr + translateYStr + translateZStr + rotateXStr + rotateYStr + rotateZStr + scaleXStr + scaleYStr + scaleZStr + visibilityStr
    print str
    mm.eval('expression  -s  "%s"  -o "" -ae 1 -uc all;'%str)