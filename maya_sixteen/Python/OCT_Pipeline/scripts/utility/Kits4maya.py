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
import pymel.core as pm
class Kits4maya(object):
    """
    some kits  little procedures are collected here

    """
    def __init__(self):
        pass
    @staticmethod
    def renameIt(self,obj,newNm,suffix='',cur_num=None):#挺有用的重命名工具
        if not cur_num: cur_num = 0
        new_nm_str  = "{}{}".format(newNm,cur_num)
        new_nm_str = re.sub("_0{}$".format(suffix),'_',new_nm_str)
        if pm.objExists(new_nm_str):
            cur_num +=1
            self.renameIt(obj,newNm,cur_num)
        else:
            obj.rename(newNm,ignoreShape=True)
    @staticmethod
    def unique_name(oldName, num=None, suff='_'):# 找到唯一命名
        if not pm.objExists(oldName): return oldName
        if not num: num = 0
        nm_noSuf = re.sub('\d*{}$'.format(suff), '', oldName)
        new_nm = "{}{}{}".format(nm_noSuf, num, suff)
        new_nm = re.sub('0{}$'.format(suff), '{}'.format(suff), new_nm)
        if not pm.objExists(new_nm):
            return new_nm
        else:
            num += 1
            name_again = Kits.unique_name(new_nm, num, suff)
            return name_again
