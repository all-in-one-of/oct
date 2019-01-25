#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'via_hotKey_debug_Process'    
__author__ = zhangben
__mtime__ = 2018/12/14:16:26
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import sys
sys.path.append(r'F:\Development\OCT\Nuke')

nuke.menu('Nuke').addCommand("","import OTC_convKits_Ben as ck\nreload(ck)\ninck = ck.OTC_convKits()\ninck.SwitchRL()","alt+r")

nuke.menu('Nuke').addCommand("","import py273.OTC_convKits_Ben as ck\nreload(ck)\ninck = ck.OTC_convKits()\ninck.SwitchRL()","alt+r")


nuke.menu("OCT_Nuke_Tools").findItem("New Merge Selected Cameras").setShortcut("alt + m")
nuke.menu("OCT_Nuke_Tools").findItem()
nuke.menu("Nuke").findItem("OCT_Nuke_Tools").findItem("New Merge Selected Cameras").setShortcut("alt+m")


nuke.menu('Nuke').addCommand("","import OCT_newMergCamTool_YH as nmc\nreload(nmc)\ndoSetUp = nmc.newMergeCam()\ndoSetUp.mergeCams_dntg(None,3,\"DNTG\")","ctrl+d")