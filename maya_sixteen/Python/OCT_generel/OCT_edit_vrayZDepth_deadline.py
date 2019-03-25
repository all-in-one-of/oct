# -*- coding: utf-8 -*-

import maya.cmds  as cc
import maya.mel   as mm
import pymel.core as pm
import sys

def edit_vrayZDepth_deadline():
    k_plugins=cc.pluginInfo(q=1,l=1,listPlugins=1)
    kcode=True
    result='No'


    if 'vrayformaya' in k_plugins:
        try:
            Elements = pm.ls(type='VRayRenderElement')
            for i in Elements:
                if i.hasAttr('vrayClassType'):
                    if i.vrayClassType.get() == 'zdepthChannel':
                        depthWhite=i.vray_depthWhite.get()
                        depthClamp=i.vray_depthClamp.get()

                        if not 1.014 < depthWhite < 1.016 or not depthClamp==0:
                            if kcode:
                                result = cc.confirmDialog(title=u'温馨提示', message=u'是否修改Vray ZDepth参数？\nYes：修改，No:不修改',\
                                                          button=['Yes', 'No'], defaultButton='No', cancelButton='No',\
                                                          dismissString='No')
                                kcode = False

                        if result =='Yes':
                            i.vray_depthWhite.set(1.015)
                            i.vray_depthClamp.set(0)

        except Exception as e:
            print(e)

    else:
        cc.warning(u'没找到vray渲染设置，没进行修改操作。')


if __name__ == '__main__':
    edit_vrayZDepth_deadline()