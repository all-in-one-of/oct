# -*- coding: utf-8 -*-
import maya.cmds  as cc

class AutoCreateAOV():
    def __init__(self):
        self.ArnoldDriver = 'defaultArnoldDriver'
        self.ArnoldFilter = 'defaultArnoldFilter'
        self.ArnoldRenderOptions = 'defaultArnoldRenderOptions'
        self.AOVnodes = [{'nodeName': 'k_aiAOV_N', 'aovName': 'N','shader':'','dataType':7,'ArnoldFilter':'closest'},
                         {'nodeName': 'k_aiAOV_P', 'aovName': 'P','shader':'','dataType':8,'ArnoldFilter':'closest'},
                         {'nodeName': 'k_aiAOV_Z', 'aovName': 'Z','shader':'','dataType':4,'ArnoldFilter':'closest'},
                         {'nodeName': 'k_aiAOV_sss', 'aovName': 'sss','shader':'','dataType':5,'ArnoldFilter':''},
                         {'nodeName': 'k_aiAOV_AO', 'aovName': 'AO','shader':'occ','dataType':6,'ArnoldFilter':''},
                         {'nodeName': 'k_aiAOV_rim', 'aovName': 'rim','shader':'rim','dataType':6,'ArnoldFilter':''},
                         {'nodeName': 'k_aiAOV_crypto_asset', 'aovName': 'crypto_asset','shader':'cryptomatteAOV','dataType':5,'ArnoldFilter':''},
                         {'nodeName': 'k_aiAOV_crypto_material', 'aovName': 'crypto_material','shader':'cryptomatteAOV','dataType':5,'ArnoldFilter':''},
                         {'nodeName': 'k_aiAOV_crypto_object', 'aovName': 'crypto_object','shader':'cryptomatteAOV','dataType':5,'ArnoldFilter':''}]

    def k_createAOVnode(self,AOVnode,ArnoldDriver,ArnoldFilter,ArnoldRenderOptions):
        nodeName = AOVnode['nodeName']
        aovName = AOVnode['aovName']
        dataType = AOVnode['dataType']
        Filter = AOVnode['ArnoldFilter']
        shader = AOVnode['shader']

        if cc.objExists(nodeName):
            try:
                cc.delete(nodeName)
                cc.createNode('aiAOV', name=nodeName)
            except Exception as e:
                print (e)
        else:
            cc.createNode('aiAOV',name = nodeName)

        cc.setAttr((nodeName+'.name'),aovName,type = 'string')
        cc.setAttr((nodeName + '.type'), dataType)


        cc.connectAttr(ArnoldDriver+'.message',nodeName+'.outputs[0].driver')

        if Filter:
            FilterNode = self.createFilter((nodeName+'_'+Filter),Filter)
            cc.connectAttr(FilterNode + '.message', nodeName + '.outputs[0].filter')
        else:
            cc.connectAttr(ArnoldFilter+'.message',nodeName+'.outputs[0].filter')

        if shader:
            shaderNode = self.createShader(shader,(nodeName + '_' + shader))
            cc.connectAttr((shaderNode + '.outColor'), (nodeName + '.defaultValue'), f=1)

        if cc.listAttr(ArnoldRenderOptions+'.aovList', multi=1):
            aovlists_size = len(cc.listAttr(ArnoldRenderOptions+'.aovList', multi=1))
            cc.connectAttr(nodeName + '.message', '{0}.aovList[{1}]'.format(ArnoldRenderOptions, aovlists_size))
        else:
            cc.connectAttr(nodeName+'.message','{0}.aovList[{1}]'.format(ArnoldRenderOptions,0))

    def createFilter(self,nodeName,filterType):
        if not cc.objExists(nodeName):
            try:
                FilterNode = cc.createNode('aiAOVFilter', name=nodeName)
                cc.setAttr((FilterNode + ".aiTranslator"), filterType, type='string')
            except Exception as e:
                print (e)

        return (nodeName)

    def createShader(self,type,nodeName):
        if type == 'occ':
            if not cc.objExists(nodeName):
                try:
                    AONode = cc.createNode('aiAmbientOcclusion', name=nodeName)
                    AOSGNode = cc.createNode('shadingEngine', name=(nodeName+'SG'))
                    cc.connectAttr((AONode + '.outColor'),(AOSGNode + '.surfaceShader'),  f=1)

                except Exception as e:
                    print (e)


        if type == 'rim':
            if not cc.objExists(nodeName):
                try:
                    rimNode = cc.createNode('surfaceShader', name=nodeName)
                    rimSGNode = cc.createNode('shadingEngine', name=(nodeName+'SG'))
                    rimRampNode = cc.createNode('ramp', name=(nodeName + '_ramp'))
                    rimInfoNode = cc.createNode('samplerInfo', name=(nodeName + '_samplerInfo'))

                    cc.connectAttr((rimNode + '.outColor'),(rimSGNode + '.surfaceShader'),  f=1)
                    cc.connectAttr((rimRampNode + '.outColor'), (rimNode + '.outColor'), f=1)
                    cc.connectAttr((rimInfoNode + '.facingRatio'), (rimRampNode + '.uCoord'), f=1)
                    cc.connectAttr((rimInfoNode + '.facingRatio'), (rimRampNode + '.vCoord'), f=1)

                    cc.setAttr((rimRampNode + ".colorEntryList[0].position"),0.75)
                    cc.setAttr((rimRampNode + ".colorEntryList[0].color"),0 ,0 ,0,type = 'double3')
                    cc.setAttr((rimRampNode + ".colorEntryList[1].position"), 0)
                    cc.setAttr((rimRampNode + ".colorEntryList[1].color"), 1, 1, 1, type='double3')

                except Exception as e:
                    print (e)


        if type == 'cryptomatteAOV':
            if not cc.objExists(nodeName):
                try:
                    cryptoNode = cc.createNode(type, name=nodeName)
                    cryptoSGNode = cc.createNode('shadingEngine', name=(nodeName+'SG'))
                    cc.connectAttr((cryptoNode + '.outColor'),(cryptoSGNode + '.surfaceShader'),  f=1)

                except Exception as e:
                    print (e)

        return (nodeName)

    def do(self):
        if cc.pluginInfo('mtoa', q=True, l=1):
            for AOVnode in self.AOVnodes:
                self.k_createAOVnode(AOVnode,self.ArnoldDriver,self.ArnoldFilter,self.ArnoldRenderOptions)
        else:
            cc.warning('Had not loaded mtoa plugins!!!')

if __name__ == '__main__':
    a=AutoCreateAOV()
    a.do()
