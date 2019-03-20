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
import maya.cmds as mc
import os


def wr2f():
    selObj = pm.ls(sl=True)
    new_add = {}
    nmsp = selObj[0].namespace().strip(':')
    for ea in selObj:
        needName = ea.stripNamespace().strip()
        new_add[needName] = ea.longName(stripNamespace=True)
    wsp = pm.workspace.name
    with open(r"{}/{}_caOBjList.json".format(wsp,nmsp), 'w') as f:
        f.write(json.dumps(new_add, indent=4))
    mc.AlembicExportSelectionOptions()

def r4f():
    wsp = pm.workspace.name
    singleFilter = "All Files (*.*)"
    res = mc.fileDialog2(fileFilter=singleFilter, dialogStyle=2,fileMode=4)
    readDate = {}
    for af in res:
        ext = os.path.splitext(af)[-1]
        if ext == ".abc": readDate['abc'] = af
        elif ext == '.json': readDate['js'] = af
    with open(readDate['js'], 'r') as f:
        readDate['cclst']= json.load(f)
    return readDate

def list_rdcc_meshs():
    infor = r4f()
    cc_meshes = infor['cclst']
    readCcMsh = {}
    sel_chr = pm.selected()[0]
    for eaMesh in sel_chr.getChildren(type='mesh',ad=True,ni=True):
        ea_nm = eaMesh.name(stripNamespace=True)
        ea_p = eaMesh.getParent()
        if ea_p.name(stripNamespace=True) in cc_meshes and eaMesh not in readCcMsh: readCcMsh[eaMesh] = ea_p
    return readCcMsh
