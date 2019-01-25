# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import maya.cmds as mc
import os

def FProxyRename():
    RenameNodes = []
    obj = mc.ls(sl=True)
    if obj:
        objShapes = mc.listRelatives(obj,shapes=True)
        objSGs = mc.listConnections(objShapes,d=True,s=False)
        objSGs = list(set(objSGs))
        for objSG in objSGs:
            objShade = mc.listConnections(objSG,d=False,s=True)
            #print objShade
            objShadeTextures = mc.listConnections(objShade[0],d=False,s=True)
            RenameNodes.append(objSG)
            RenameNodes.append(objShade[0])
            if objShadeTextures:
                for objShadeTexture in objShadeTextures:
                    RenameNodes.append(objShadeTexture)
                    ftemp = mc.listConnections(objShadeTexture,d=False,s=True)
                    RenameNodes.append(ftemp[-1])
            else:
                print ("材质球没有贴图.............".encode('cp936'))                
    else:
        mc.confirmDialog(title=u"温馨提示",message=u"请选择一个物体再回来........")
        return
    RenameNodess = list(set(RenameNodes))
    for renameNode in RenameNodess:
        mc.rename(renameNode,"%s_%s" % (obj[0],renameNode))
    num = len(RenameNodess)
    mc.confirmDialog(title=u"温馨提示",message=u"更改完成 %d 个节点........" % num,button="Yes")


# FProxyRename()