#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Kits
__author__ = zhangben 
__mtime__ = 2019/4/2 : 9:55
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import os,re,sys
class Kits(object):
    """
    some kits  little procedures are collected here

    """
    def __init__(self):
        pass
    @staticmethod
    def get_dir(path,index=1):
        get_backslash = re.findall(r"\\",path)
        get_slash = re.findall('/',path)
        cur_sep = r'\\' if len(get_backslash)>len(get_slash) else '/'
        pth_abs = os.path.abspath(path)
        pth_spl = pth_abs.split(os.sep)
        spll = len(pth_spl)
        res_pth_spl = []
        id = index*-1
        res_pth_spl = pth_spl[:id]
        res_path_abs = os.sep.join(res_pth_spl)
        return re.sub(repr(os.sep),cur_sep,res_path_abs)



