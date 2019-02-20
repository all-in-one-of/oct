# -*- coding: utf-8 -*-
#!/usr/bin/env python

import maya.cmds as mc
import maya.mel as mm

class ExportABCCache():

    def __init__(self):
        self.allSelectObject = mc.ls(sl = True)
        self.myList = []
        self.myRename = []
        self.allShader = []

    def selectFaceToMaterial(self):
        #print self.allSelectObject
        self.myList = []
        if self.allSelectObject:
            for obj in self.allSelectObject:
                childObj = mc.listRelatives(obj, c= True)
                if mc.objectType(childObj[0]) != "mesh":
                    continue
                
                # print childObj
                # print "\n"
               
                shding = mc.listConnections(childObj[0], s= False, d= True)
                #print shding
                
                tempName = []
                for sh in shding:
                    if mc.objectType(sh) == "shadingEngine" and sh not in tempName:
                        tempName.append(sh)

                #判断是是否为选面给物体，若为真，修改SG节点的名字和材质名字相关联，若为假，保存数据创建新的材质
                if len(tempName) == 1:
                    if not tempName[0] in self.myList:
                        self.myList.append(tempName[0])
                else:
                    for shad in tempName:
                        if not shad in self.myList:
                            materialName = mc.listConnections("%s.surfaceShader"%shad,s = True, d = False)
                            try:
                                mc.rename(shad,materialName[0]+"_fxSG")
                            except:
                                print "检查%sSG节点，是否是默认材质！"%shad
                            

        self.myList = list(set(self.myList))
       

        if self.myList:
            for shade in self.myList:
                materialName = mc.listConnections("%s.surfaceShader"%shade,s = True, d = False)

                name = mc.shadingNode("blinn", asShader = True, name = "%s_fx"%materialName)
                nameSG = mc.sets(renderable = True, noSurfaceShader = True, empty = True, name = "%sSG"%name)
                mc.connectAttr("%s.outColor"%name, "%s.surfaceShader"%nameSG)

                meshNames = mc.sets(shade, q = True)
                for meshN in meshNames:
                    mc.select(d= True)
                    try:
                        mc.select(meshN, r = True)
                    except:
                        mc.confirmDialog(message = u"%s节点是否为combine物体没请历史！"%meshN)
                        return
                    
                    mm.eval("ConvertSelectionToFaces;")
                    mc.sets(e = True, forceElement = nameSG)
                try:
                    mc.delete(shade)
                except:
                    pass
        mm.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
        mc.confirmDialog(message = u"选面给材质设置完成！")
        return

               

#ExportABCCache().selectFaceToMaterial()
