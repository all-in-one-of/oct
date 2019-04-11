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
class Kits(object):
    """
    some kits  little procedures are collected here

    """
    def __init__(self):
        pass
    @staticmethod
    def get_dir(fpth,index=1):#根据 索引值 返回 路径上一层 或上几层
        get_backslash = re.findall(r"\\",fpth)
        get_slash = re.findall('/',fpth)
        cur_sep = r'\\' if len(get_backslash)>len(get_slash) else '/'
        pth_abs = os.path.abspath(fpth)
        pth_spl = pth_abs.split(os.sep)
        spll = len(pth_spl)
        res_pth_spl = []
        id = index*-1
        res_pth_spl = pth_spl[:id]
        res_path_abs = os.sep.join(res_pth_spl)
        return re.sub(repr(os.sep),cur_sep,res_path_abs)

    @staticmethod
    def splitf(fpth,folder):#根据文件夹的名字把路径切割为三段
        get_backslash = re.findall(r"\\", fpth)
        get_slash = re.findall('/', fpth)
        cur_sep = r'\\' if len(get_backslash) > len(get_slash) else '/'
        pth_abs = os.path.abspath(fpth)
        pth_spl = pth_abs.split(os.sep)
        pth_spl_lw = [ea_f.lower() for ea_f in pth_spl]
        if folder.lower() not in pth_spl_lw: return fpth
        id = pth_spl_lw.index(folder.lower())
        forepart = cur_sep.join(pth_spl[:id])
        posterior = cur_sep.join(pth_spl[id + 1:])
        return forepart, folder, posterior,cur_sep



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
