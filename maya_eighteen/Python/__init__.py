#!/usr/bin/env python
# coding=utf-8

import os
import string
import re
import sys
import math
import maya.utils
import maya.utils as mu
import maya.cmds as mc
import maya.mel as mm
import pymel as pm
import maya.OpenMaya as om

try:
    sys.path.append(r'\\octvision.com\cg\Tech\maya_sixteen\Lib')
    from PyQt4 import QtCore, QtGui
    import maya.OpenMayaUI as mui
    import sip
except:
    om.MGlobal.displayError(u'加载界面时出现异常2,请联系管理员.')

import OCT_about
import OCT_anim
import OCT_cam
import OCT_generel
import OCT_lgt
import OCT_render
import OCT_menu
import OCT_mod
import OCT_util
import OCT_vfx
import OCT_check
import OCT_proxy
import OCT_vr
import OCT_hair
import OCT_matLib
import OCT_animImEx
import OCT_rigging
import Themes
import OCT_Projects
