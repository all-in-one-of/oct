#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = zb_DupLightLink.py
__author__ = zhangben 
__mtime__ = 2019/3/21 : 15:56
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import pymel.core as pm
import json
import os

def write_lightLinks(sourceGrps):
    ws = pm.workspace.name
    out_file = {}
    nmspc = sourceGrps.namespace()
    tmpDir = os.getenv('TMP')
    wf = os.path.abspath(os.path.join(tmpDir, '{}_lightLink.json'.format(nmspc.strip(':'))))
    listAllObject = [ea.getParent() for ea in sourceGrps.listRelatives(ad=True, s=True, ni=True) if not ea.isIntermediate()]
    l_l_dict = {}
    for ea in listAllObject:
        list_lights = pm.lightlink(q=True, object=ea)
        l_l_dict[ea.name(stripNamespace=True)] = list_lights
    with open(wf, 'w') as f:
        f.write(json.dumps(l_l_dict, indent=4))
    out_file[nmspc.strip(':')] = wf
    return out_file
def doLink(targGrp, srcGrpNSP):
    tmpDir = os.getenv('TMP')
    readFile = os.path.abspath(os.path.join(tmpDir, '{}_lightLink.json'.format(srcGrpNSP.strip(':'))))
    readInfo = None
    with open(readFile, 'r') as rf:
        readInfo = json.load(rf)
    listAllObject = [ea.getParent() for ea in targGrp.listRelatives(ad=True, s=True, ni=True) if not ea.isIntermediate()]
    ret_dic = {'linked': [], 'failed': [], 'noLinked': []}
    for eaObj in listAllObject:
        getKey = eaObj.name(stripNamespace=True)
        if getKey not in readInfo:
            ret_dic['failed'].append("Node {} not find in source Select Group".format(eaObj.longName()))
            continue
        ea_l_l = readInfo[getKey]
        if not len(ea_l_l):
            ret_dic['noLinked'].append("WARNING!!!!!:Node {} not find in source Select Group".format(eaObj.longName()))
            continue
        l_tuple = [ealight.name() for ealight in readInfo[getKey]]
        pm.lightlink(object = eaObj, light=l_tuple)
    return ret_dic
def DupLightLink(prnt=False):
    sel_groups = pm.selected()
    if len(sel_groups) !=2: pm.error("Please select 2 group: 1--source character; 2--target group")
    readDate =  write_lightLinks(sel_groups[0])
    result = doLink(sel_groups[1],readDate.keys()[0])
    if not prnt:
        print(u"  一 一 ！！！ 歪歪歪！！ light linked done!!!!")
    for eaRes in result:
        for eaitm in result[eaRes]:
            print (eaRes,eaitm)
