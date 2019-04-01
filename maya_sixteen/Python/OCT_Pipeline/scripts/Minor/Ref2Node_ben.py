#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Ref2Node_ben
__author__ = zhangben 
__mtime__ = 2019/4/1 : 11:27
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import pymel.core as pm
import maya.mel as mel

def Ref2Node():
    refEd = mel.eval('global string $gReferenceEditorPanel;string $a = $gReferenceEditorPanel')
    sel_ref = pm.sceneEditor(refEd, q=True, sr=True)
    allRefs = pm.listReferences()
    ref_nodes = [eaRef.refNode for eaRef in allRefs if eaRef.refNode.name() in sel_ref]
    sel_ref_dict = {}
    for ea_sl_rf in ref_nodes:
        temp_lst = [ea_nd for ea_nd in ea_sl_rf.nodes() if ea_nd.type() == 'transform' and (not ea_nd.getParent(1) or not ea_nd.getParent(1).isReferenced())]
        top_parents = []
        for ea_tmp in temp_lst:
            top_p = get_top_ref(ea_tmp)
            if top_p not in top_parents: top_parents.append(top_p)
        sel_ref_dict[ea_sl_rf] = top_parents
    return sel_ref_dict
def get_top_ref(ref_node):
    n=-1
    getTop = None
    while 1:
        getTop = ref_node.getParent(n)
        if getTop.isReferenced(): break
        n -= 1
    return getTop

def sel_ref_topTrans():
    res = Ref2Node()
    pm.select(res.values())
