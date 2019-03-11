#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'OTC_convenientKits_Ben'    
__author__ = zhangben
__mtime__ = 2018/12/14:11:41
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re,os
import nuke

class OTC_convenientKits(object):
    def __init__(self):
        self.dict_rl = {'r':'l','R':'L','l':'r','L':'R','Right':'Left','Left':'Right'}


    def SwitchRL(self,readNodes=None):

        if readNodes == None:  readNodes = nuke.selectedNodes()
        if len(readNodes) == 0:
            readNodes = nuke.allNodes("Read")
        un_replace_nodes = []
        bd_modified = []
        for eard in readNodes:
            # eard = readNodes[0]
            stuffPath = eard.knob("file").getValue()
            cam_name = re.search('cam[\w_]*(r|l)', stuffPath, re.I).group()
            camOriant = re.search('(r|l)$', cam_name, re.I).group()
            cam_name_new = re.sub(camOriant, self.dict_rl[camOriant], cam_name)
            stuffPaht_new = re.sub(cam_name, cam_name_new, stuffPath)
            stuffPaht_new_2 = stuffPaht_new + "abc.exe"
            if not os.path.isdir(os.path.split(stuffPaht_new)[0]):
                un_replace_nodes.append(eard)
                continue
            eard.knob("file").setValue(stuffPaht_new)
            bd_node = self.getBackdropNodes(eard)
            if len(bd_node) == 0: continue
            self.refresh_drp(bd_node[0], bd_node[0] not in bd_modified)
            bd_modified.append(bd_node[0])
        if len(un_replace_nodes) != 0:
            allmySelectedNodes = nuke.selectedNodes()
            if len(allmySelectedNodes):
                for mySelectedNode in allmySelectedNodes:
                    mySelectedNode.setSelected(False)
            warStr = "The following Nodes cant switch OPPOSITE Stuffs:\n"
            for each_un in un_replace_nodes:
                warStr += "{}\n".format(each_un.name())
                each_un.setSelected(True)
            print warStr


    def getBackdropNodes(self,node):
        allBDs = nuke.allNodes('BackdropNode')
        nodeBackdrops = []
        # store original selection
        originalSelection = nuke.selectedNodes()
        for bd in allBDs:
            # clear original selection:
            for n in nuke.allNodes():
                n.setSelected(False)
            # select backdrop nodes
            bd.selectNodes()
            # store new selection
            bdNodes = nuke.selectedNodes()
            if node in bdNodes:
                nodeBackdrops.append(bd)
        # restore previous selection
        for n in nuke.allNodes():
            n.setSelected(n in originalSelection)

        return nodeBackdrops

    def refresh_drp(self, bd, toggle=True):  # =====modify  backdrop nodes title and name to obbside camera
        if not toggle: return None
        bd_nm = bd.name()
        bd_label = bd.knob("label").getValue()
        re_orientation = re.compile('(Right)|(Left)')
        bd_nm_new = bd_nm
        bd_label_new = bd_label
        if re_orientation.search(bd_nm):
            or_str = re_orientation.search(bd_nm).group()
            bd_nm_new = re.sub(or_str, self.dict_rl[or_str], bd_nm)
        if re_orientation.search(bd_label):
            or_str = re_orientation.search(bd_label).group()
            bd_label_new = re.sub(or_str, self.dict_rl[or_str], bd_label)
        bd.setName(bd_nm_new)
        bd.knob("label").setValue(bd_label_new)

