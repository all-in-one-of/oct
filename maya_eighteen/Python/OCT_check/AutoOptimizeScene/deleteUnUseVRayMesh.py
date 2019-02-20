#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om
#删除多余的VRayMesh节点
def deleteUnUseVRayMesh():
    count = 0
    allVRayMeshs = mc.ls(type = 'VRayMesh')
    if allVRayMeshs:
        for VRayM in allVRayMeshs:
            cons = mc.listConnections(VRayM, s =False, d = True, shapes = True)
            flag = True
            if cons:
                for con in cons:
                    if mc.objectType(con) == 'mesh':
                        flag = False
                if flag:
                    try:
                        mc.delete(VRayM)
                    except:
                        om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
                    else:
                        count = count + 1
            else:
                try:
                    mc.delete(VRayM)
                except:
                    om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
                else:
                    count = count + 1
    print"delete VRayMesh node number is %s"%count

