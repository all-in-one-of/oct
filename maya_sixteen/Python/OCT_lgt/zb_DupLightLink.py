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
import os,re
import maya.mel as mel
import maya.cmds as mc
def write_lightLinks(sourceGrps):
    ws = pm.workspace.name
    out_file = {}
    nmspc = sourceGrps.namespace()
    tmpDir = os.getenv('TMP')
    wf = os.path.abspath(os.path.join(tmpDir, '{}_lightLink.json'.format(nmspc.strip(':'))))
    listAllObject = [ea.getParent() for ea in sourceGrps.listRelatives(ad=True, s=True, ni=True,type='mesh') if not ea.isIntermediate()]
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
    listAllObject = [ea.getParent() for ea in targGrp.listRelatives(ad=True, s=True, ni=True,type='mesh') if not ea.isIntermediate()]
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
        l_tuple = [ealight for ealight in readInfo[getKey]]
        pm.lightlink(object = eaObj, light=l_tuple)
    return ret_dic
def DupLightLink(haveRndLayer = False):
    if not haveRndLayer:
        sel_groups = pm.selected()
        if len(sel_groups) !=2: pm.error("Please select 2 group: 1--source character; 2--target group")
        readDate =  write_lightLinks(sel_groups[0])
        result = doLink(sel_groups[1],readDate.keys()[0])
        print(u"  一 一 ！！！ 歪歪歪！！ light linked done!!!!")
        for eaRes in result:
            for eaitm in result[eaRes]:
                print (eaRes,eaitm)
    else:
        sel_obj = pm.selected()
        src_grp = sel_obj[0]
        targ_grp = sel_obj[1]
        allRndL = [eaRl for eaRl in pm.ls(type='renderLayer') if not re.search('defaultrenderlayer', eaRl.name(), re.I)]
        allRndL.extend([eaRl for eaRl in pm.ls(type='renderLayer') if eaRl.name() == 'defaultRenderLayer'])
        for cur_rl in allRndL:
            # cur_rl = allRndL[0]
            cur_rl.setCurrent()

            if cur_rl.inLayer(src_grp) and not cur_rl.inLayer(targ_grp):
                cur_rl.addMembers(targ_grp)
            # list lights linked
            mel.eval("selectLightsIlluminating {}".format(src_grp.name()))
            cur_link_light = pm.selected()
            # cur_link_light_nm = [e_l.name() for e_l in cur_sel_light]
            pm.select(targ_grp, add=True)
            pm.lightlink(make=True, useActiveLights=True, useActiveObjects=True)
            print("=============light linked succeed !!!  in renderLayer {}".format(cur_rl.name()))
        print("All Light Linked to new Character !!!!!!!")