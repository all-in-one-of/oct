# coding=utf-8

import maya.cmds as mc

def displacementToScale():
    if not mc.pluginInfo('KLJZ_dts', q=True, l=True):
        mc.loadPlugin('KLJZ_dts.py')

    objSelect = mc.ls(sl=True)
    if len(objSelect)!=2:
        mc.error(u'请选择2个物体')
    dts_node = mc.createNode('KLJZ_dts')
    for x in xrange(2):
        if not mc.attributeQuery('worldMatrix', n=objSelect[x], ex=True):
            mc.error(u'选择的物体没有worldMatrix属性')
        pointMatrixNode = mc.createNode('pointMatrixMult')
        mc.connectAttr('%s.worldMatrix[0]' %objSelect[x],  '%s.inMatrix' % pointMatrixNode, force=True)
        mc.connectAttr( '%s.output' %pointMatrixNode, '%s.obj%s' %(dts_node,str(x+1)), force=True)

    mc.setAttr('%s.coefficient' % dts_node, -0.00423781, 0.12412153, 0.09117381)

    mc.connectAttr('%s.value' %dts_node, '%s.scaleX' %objSelect[1], f=True)
    mc.connectAttr('%s.value' %dts_node, '%s.scaleY' %objSelect[1], f=True)
    mc.connectAttr('%s.value' %dts_node, '%s.scaleZ' %objSelect[1], f=True)
