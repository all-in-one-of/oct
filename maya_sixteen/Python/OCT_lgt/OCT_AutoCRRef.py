#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = AutoCRRef
__author__ = zhangben 
__mtime__ = 2019/5/14 : 9:25
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
创建参考路径下的所有文件，选择同名文件的最后一个版本

"""
import pymel.core as pm
import maya.cmds as mc
import re,os
def autoCreateRef():
    searchDir = mc.fileDialog2(fm=3, okc=u'确定路径', ds=2, rf=False)
    if not searchDir: return
    LIST_Files = {}
    for root, dirs, files in os.walk(searchDir[0]):
        for eaf in files:
            if os.path.splitext(eaf)[-1] == '.mb':
                fn_noExt = os.path.splitext(eaf)[0]
                re_ed = re.compile('_[a-z]*\d+$', re.I)
                fn_noEdt = fn_noExt
                if re_ed.search(fn_noExt):
                    edt = re_ed.search(fn_noExt).group()
                    fn_noEdt = re.sub(edt, "", fn_noExt)
                if fn_noEdt not in LIST_Files:
                    LIST_Files[fn_noEdt] = {fn_noEdt: [root, eaf]}
                else:
                    LIST_Files[fn_noEdt][fn_noExt] = [root, eaf]

    Need_Files = []
    for ea in LIST_Files:
        k_list = LIST_Files[ea].keys()
        k_list.sort()
        Need_Files.append(LIST_Files[ea][k_list[-1]])
    for ea in Need_Files:
        nms = '_'.join(ea[1].split('_')[:2])
        ref_dir = os.path.abspath(os.path.join(ea[0], ea[1]))
        pm.createReference(ref_dir, namespace=nms)