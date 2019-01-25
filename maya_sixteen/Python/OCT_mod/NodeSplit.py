# -*- coding: utf-8 -*-
#!/usr/bin/env python
#同一个代理树把面减了变成高低模，高低模就这样渲染没问题，把高模转底模就有问题。
import maya.cmds as mc
allVRayMesh = mc.ls(type = "VRayMesh")
for VRayMes in allVRayMesh:
    daili = []
    meshNode = mc.listConnections(VRayMes, s = False, d = True, sh = True)
    if not meshNode:
        mc.delete(VRayMes)
    else:
        if len(meshNode)>2:
            i = 1
            for meshN in meshNode:
                if mc.objectType(meshN) == "mesh" or mc.objectType(meshN) == "transform":
                    if i > 1:
                        VRayMeshName = mc.createNode('VRayMesh', name = "VRayMesh%s"%meshN)
                        mc.disconnectAttr("%s.output"%VRayMes,"%s.inMesh"%meshN)
                        mc.connectAttr("%s.output"%VRayMeshName,"%s.inMesh"%meshN)
                        VRayMeshPath = mc.getAttr("%s.fileName2" % VRayMes)
                        mc.setAttr("%s.fileName2"%VRayMeshName, VRayMeshPath, type = "string")
                    i = i + 1
        elif len(meshNode) == 2:
            if mc.objectType(meshNode[0]) == "mesh" or mc.objectType(meshNode[0]) == "transform":
                name = meshNode[0].split("|")[-1]
                trans =mc.listRelatives(name, ap= True)
                if len(trans)>1:
                    daili = trans
                    print daili
                    VRayMeshPath = mc.getAttr("%s.fileName2" % VRayMes)
                    for da in daili:
                        mc.select(d = True)
                        mc.select(da, r = True)
                        newName = mc.duplicate(rr = True, un = True, name = "%snew" %da)
                        shapesName = mc.listRelatives(newName, shapes = True)[0]
                        mc.listConnections(shapesName)
                        newVRayMesh = mc.listConnections(shapesName,s=True,d = False)
                        mc.delete(da)

                    