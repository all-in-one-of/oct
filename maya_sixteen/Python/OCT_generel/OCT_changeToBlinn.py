#encoding:utf-8
import maya.cmds as cc
import re
class changeToBlinn():
    def __init__(self):
        self.list_Info = [{'type':'alSurface','color':'.diffuseColor','colorStrength':'.diffuseStrength','bump':'.normalCamera','specular':'.specular1Color','opacity':'.opacity'},
                          {'type': 'VRayMtl', 'color': '.color','colorStrength':'.diffuseColorAmount', 'bump': '.bumpMap','specular': '.reflectionColor','opacity':'.opacityMap'},
                          {'type': 'aiStandard', 'color': '.color','colorStrength':'.Kd', 'bump': '.normalCamera', 'specular': '.KsColor','opacity':'.opacity'}
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
            kcolorS = listTypes['colorStrength']
            kbump = listTypes['bump']
            kspecular = listTypes['specular']
            kopacity = listTypes['opacity']


            try:
                k_shaders = cc.ls(type=kType)
                for i in k_shaders:
                    #找指定的连接属性
                    colorT = cc.listConnections(i + kcolor, s=1, d=0,c=1,p=1)
                    colorST = cc.listConnections(i + kcolorS, s=1, d=0, c=1, p=1)
                    normalT = cc.listConnections(i + kbump, s=1, d=0,c=1,p=1)
                    specularT = cc.listConnections(i +kspecular, s=1, d=0, c=1,p=1)
                    opacityT = cc.listConnections(i + kopacity, s=1, d=0, c=1,p=1)

                    colorC = cc.getAttr(i + kcolor)[0]
                    colorSC = cc.getAttr(i + kcolorS)
                    specularC = cc.getAttr(i + kspecular)[0]
                    opacityC = cc.getAttr(i + kopacity)[0]

                    blinncolorSC = colorSC*0.8
                    if kType == 'aiStandard':
                        blinncolorSC = colorSC * (0.8/0.7)


                    # k_SGC = cc.listConnections(i + ('.outColor'), s=0, d=1,p=1)
                    # print (k_SGC)
                    #找SG
                    k_SG = cc.listConnections(i + ('.outColor'), s=0, d=1)
                    #找MESH
                    k_SG_meshs = cc.listConnections(k_SG[0] + ('.dagSetMembers'), s=1, d=1,c=1,p=1)


                    #新建材质球和SG
                    kbilnn_args = self.createBlinn(i)
                    kbilnn = kbilnn_args['kBilnn']
                    kSG = kbilnn_args['kSG']

                    #重连指定属性
                    if colorT:
                        cc.disconnectAttr(colorT[1],colorT[0])
                        cc.connectAttr(colorT[1], (kbilnn + '.color'), f=1)
                    else:cc.setAttr((kbilnn + '.color'), colorC[0], colorC[1], colorC[2], type="double3")
                    if colorST:
                        cc.disconnectAttr(colorST[1],colorST[0])
                        cc.connectAttr(colorST[1], (kbilnn + '.diffuse'), f=1)
                    else:cc.setAttr((kbilnn + '.diffuse'), blinncolorSC)
                    if normalT:
                        cc.disconnectAttr(normalT[1], normalT[0])
                        cc.connectAttr(normalT[1], (kbilnn + '.normalCamera'), f=1)
                    if specularT:
                        cc.disconnectAttr(specularT[1], specularT[0])
                        cc.connectAttr(specularT[1], (kbilnn + '.specularColor'), f=1)
                    else:cc.setAttr((kbilnn + '.specularColor'), specularC[0], specularC[1], specularC[2], type="double3")
                    if opacityT:
                        cc.disconnectAttr(opacityT[1], opacityT[0])
                        cc.connectAttr(opacityT[1], (kbilnn + '.transparency'), f=1)
                    else:cc.setAttr((kbilnn + '.transparency'), abs(opacityC[0]-1), abs(opacityC[1]-1), abs(opacityC[2]-1), type="double3")

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