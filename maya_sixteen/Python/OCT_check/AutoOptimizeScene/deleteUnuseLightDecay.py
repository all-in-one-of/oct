#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import maya.cmds as mc
import string
import math
import threading

#删除多余的灯光衰减节点
def deleteUnuseLightDecay():
    allLightDecay = mc.ls(type = 'aiLightDecay')
    for lgD in allLightDecay:
        con = mc.listConnections(lgD)
        if len(con)<=1 and con[0] == "defaultRenderUtilityList1":
            mc.delete(lgD)
        elif len(con)<1:
            mc.delete(lgD)

    print ("删除多余的灯光衰减节点..................".encode("gbk"))

