# -*- coding: utf-8 -*-
import maya.cmds as mc


def OCT_FKSDYDelBot_zwz():
    rightN = 0
    errorN = 0
    myAllFiles = mc.ls(type="file", ap=True, l=True)
    for each in myAllFiles:
        try:
            mc.setAttr("%s.useCache" % each, 0)
        except:
            errorN += 1
            pass
        else:
            rightN += 1
    if errorN:
        mc.confirmDialog(title=u'温馨提示：', message=u'有%s个file设置为0失败'%errorN, button=['OK'], defaultButton='Yes', dismissString='No')
    else:
        mc.confirmDialog(title=u'温馨提示：', message=u'   oK！全部设置成功！\n有%s个file设置为0'%rightN, button=['OK'], defaultButton='Yes', dismissString='No')
