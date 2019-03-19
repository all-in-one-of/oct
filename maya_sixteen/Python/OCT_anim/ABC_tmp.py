#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ABC_tmp
__author__ = zhangben 
__mtime__ = 2019/3/19 : 20:50
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import pymel.core as pm
import json
import re


def wr2f():
    selObj = pm.ls(sl=True)
    new_add = {}
    for ea in selObj:
        needName = ea.stripNamespace().strip()
        new_add[needName] = ea.longName(stripNamespace=True)
    wsp = pm.workspace.name
    with open(r"{}/recorde_meshes.txt".format(wsp), 'w') as f:
        f.write(json.dumps(new_add, indent=4))


def r4f():
    wsp = pm.workspace.name
    readDate = {}
    with open(r"{}/recorde_meshes.txt".format(wsp), 'r') as f:
        readDate = json.load(f)
    allMesh = pm.ls(type='mesh', io=False)
    all_ms_p = []
    for ea in allMesh:
        p = ea.getParent()
        p_nm = p.name(stripNamespace=True)
        if p_nm in readDate and p not in all_ms_p:
            all_ms_p.append(p)
    pm.select(all_ms_p)

