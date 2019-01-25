#!/usr/bin/env python
# coding=utf-8
import maya.cmds as mc


def DelUnuseUvSets_zxy():
    selected = mc.ls(sl=True, ap=True)
    if selected:
        for eachSelected in selected:
            shape = mc.listRelatives(eachSelected, s=True, f=True)
            if shape is None:
                continue
            for eachShape in shape:
                if mc.getAttr(eachShape+'.intermediateObject') is False and mc.nodeType(eachShape) == 'mesh':
                    try:
                        all_uv_set = mc.polyUVSet(eachShape, q=True, auv=True)
                        for each in all_uv_set:
                            if not each == 'map1':
                                mc.polyUVSet(d=True, uvs=each)
                    except:
                        continue
        mc.confirmDialog(message=u"已清理完毕！", button="OK")
    else:
        mc.confirmDialog(message=u"请选择需要清理的模型！", button="OK")
