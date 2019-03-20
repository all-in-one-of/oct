# -*- coding: utf-8 -*-

import maya.cmds  as cc
import maya.mel   as mm
import pymel.core as pm
import sys

def edit_vrayZDepth():
    k_plugins=cc.pluginInfo(q=1,l=1,listPlugins=1)
    kcode=True

    if 'vrayformaya' in k_plugins:
        try:
            Elements = pm.ls(type='VRayRenderElement')
            for i in Elements:
                if i.hasAttr('vrayClassType'):
                    if i.vrayClassType.get() == 'zdepthChannel':
                        i.vray_depthWhite.set(1.015)
                        i.vray_depthClamp.set(0)

                        if kcode:
                            sys.stdout.write(u'Vray ZDepth参数修改完成!')
                            kcode = False
        except Exception as e:
            print(e)

    else:
        cc.warning(u'没找到vray渲染设置，没进行修改操作。~~')


if __name__ == '__main__':
    edit_vrayZDepth()