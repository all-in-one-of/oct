# -*- coding: utf-8 -*-
import maya.cmds as mc
#import maya.OpenMaya as om


def deleteUnknown():
    allunknows=mc.ls(type="unknown")
    for unknows in allunknows:
        if mc.objExists(unknows):
            if mc.lockNode(unknows,q=True):
                mc.lockNode(unknows,l=False)
            try:
                mc.delete(unknows)
            except:
                pass
        
    print 'deleteUnknown() successful...........'