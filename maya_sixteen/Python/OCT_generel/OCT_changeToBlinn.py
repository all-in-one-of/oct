#encoding:utf-8
import maya.cmds as cc
import re
class changeToBlinn():
    def __init__(self):
        self.list_Info = [{'type':'alSurface','color':'.diffuseColor','bump':'.normalCamera','specular':'.specular1Color','opacity':'.opacity'},
                          {'type': 'VRayMtl', 'color': '.color', 'bump': '.bumpMap','specular': '.reflectionColor','opacity':'.opacityMap'},
                          {'type': 'aiStandard', 'color': '.color', 'bump': '.normalCamera', 'specular': '.KsColor','opacity':'.opacity'}
                          ]


    def createBlinn(self,kname):
        kBilnn = cc.shadingNode('blinn',name=(kname+'_blinn'),asShader=1)
        kSG = cc.sets(renderable=1,noSurfaceShader=1,empty=1,name=(kname+'_SG'))
        cc.connectAttr((kBilnn+'.outColor'),(kSG+'.surfaceShader'),f=1)
        return ({'kBilnn':kBilnn,'kSG':kSG})

    def do(self):
        #re_SG = re.compile(r"(.*)(.dagSetMembers\[\d+\])$")
        for listTypes in self.list_Info:
            kType = listTypes['type']
            kcolor = listTypes['color']
            kbump = listTypes['bump']
            kspecular = listTypes['specular']
            kopacity = listTypes['opacity']


            try:
                k_shaders = cc.ls(type=kType)
                for i in k_shaders:
                    #找指定的连接属性
                    diffC = cc.listConnections(i + kcolor, s=1, d=0,c=1,p=1)
                    normalC = cc.listConnections(i + kbump, s=1, d=0,c=1,p=1)
                    specularC = cc.listConnections(i +kspecular, s=1, d=0, c=1,p=1)
                    opacityC = cc.listConnections(i + kopacity, s=1, d=0, c=1,p=1)


                    # k_SGC = cc.listConnections(i + ('.outColor'), s=0, d=1,p=1)
                    # print (k_SGC)
                    #找SG
                    k_SG = cc.listConnections(i + ('.outColor'), s=0, d=1)
                    #找MESH
                    k_SG_meshs = cc.listConnections(k_SG[0] + ('.dagSetMembers'), s=1, d=1,c=1,p=1)


                    if diffC or normalC or specularC or opacityC:
                        #新建材质球和SG
                        kbilnn_args = self.createBlinn(i)
                        kbilnn = kbilnn_args['kBilnn']
                        kSG = kbilnn_args['kSG']

                        #重连指定属性
                        if diffC:
                            cc.disconnectAttr(diffC[1],diffC[0])
                            cc.connectAttr(diffC[1], (kbilnn + '.color'), f=1)
                        if normalC:
                            cc.disconnectAttr(normalC[1], normalC[0])
                            cc.connectAttr(normalC[1], (kbilnn + '.normalCamera'), f=1)
                        if specularC:
                            cc.disconnectAttr(specularC[1], specularC[0])
                            cc.connectAttr(specularC[1], (kbilnn + '.specularColor'), f=1)
                        if opacityC:
                            cc.disconnectAttr(opacityC[1], opacityC[0])
                            cc.connectAttr(opacityC[1], (kbilnn + '.transparency'), f=1)

                        #重连mesh
                        for i in range(len(k_SG_meshs)):
                            if not i % 2 ==0:
                                new_kSG=k_SG_meshs[i - 1].replace(k_SG[0],kSG)
                                cc.disconnectAttr(k_SG_meshs[i], k_SG_meshs[i - 1])
                                cc.connectAttr(k_SG_meshs[i],new_kSG,f=1)

            except Exception as e:
                print (e)


if __name__ =='__main__':
    a=changeToBlinn()
    a.do()