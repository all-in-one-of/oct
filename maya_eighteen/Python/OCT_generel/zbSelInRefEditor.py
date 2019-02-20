#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = zbSelInRefEditor.py
__author__ = zhangben 
__mtime__ = 2019/2/16 : 16:33
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

import pymel.core as pm
import maya.mel as mel
import maya.cmds as mc

def getRefNodes(selObjs):
    """
        via selected objects get the reference nodes
    """
    res = []
    for ea in selObjs:
        if not ea.isReferenced():
            return None
        f_ref = ea.referenceFile()
        #ref_path = f_ref.path.strip()
        #ref_nd = ref_file.refNode.name()
        res.append(f_ref)
    return res

def selectInReferenceEditor():
    """
    SELECTE THE FIRST reference in the referenceEditor related to the current seclection
    """
    # get glbal name of the reference editor panel from mel
    gReferenceEditorPanel = mel.eval("$temp_1 = $gReferenceEditorPanel")
    #get all referenced files names
    all_ref_f = pm.listReferences()
    refNode  = getRefNodes(pm.selected())
    if refNode:
        index = all_ref_f.index(refNode[0])
    pm.sceneEditor(gReferenceEditorPanel,si = index,e=True)