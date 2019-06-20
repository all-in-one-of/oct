#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'pk_rnmtools_auto'    
__author__ = zhangben
__mtime__ = 2018/12/6:11:28
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''
import re
import pymel.core as pm
import maya.cmds as mc
import copy
from ..Major import Ppl_pubCheck
reload(Ppl_pubCheck)
from ..Major import Ppl_scInfo
reload(Ppl_scInfo)
from ..utility import Kits4maya
reload(Kits4maya)
# scinf = pc.major.Pc_scInfo.Pc_scInfo()
# reload(ppc)
# chk = ppc.Pc_pubCheck()
# chk.checkDonotNodeCleanBase()
# scinf = psi.Pc_scInfo()
# Pre_regNaming_fix('MSH__', 'MSH_')
# Pre_regNaming()
"I'm a rename tool"

def Pre_regNaming(sel_MODEL=None,topSel=False):#=========rename selecte group and children's  name =======main proc
    if not sel_MODEL: sel_MODEL = pm.selected()[0]
    if not sel_MODEL.getParent() : topSel =True
    # sel_nm_analysis = get_name_membs(sel_MODEL.name())
    # p_side = sel_nm_analysis['sd']
    # getAll_trans = sel_MODEL.listRelatives(ad=True, c=True, type='transform')
    # for each in getAll_trans:
    #     ea_nm = new_names(each,pk_sid = p_side)
    #     if ea_nm: each.rename(ea_nm)
    # for each in getAll_trans:
    #     fix_suffix_num(each)
    # sel_MODEL.rename(new_names(sel_MODEL))
    renm_grp(sel_MODEL)
    if sel_MODEL.getParent(): #topSel = True
        print(u'========regularizeed nodes name ==================')
        return None
    if sel_MODEL.name != u'MSH_all':
        sel_MODEL.rename(u'MSH_all')
    if not pm.objExists(u'MODEL'): pm.group(em=True,w=True,n=u'MODEL')
    sel_MODEL.setParent(u'MODEL')
    if not pm.objExists(u'MSH_geo'):
        geoGrp = pm.group(em=True,w=True,n=u'MSH_geo')
        geoGrp.setParent(u'MSH_all')
    if not pm.objExists(u'MSH_outfig'):
        outfitGrp = pm.group(em=True,w=True,n=u'MSH_outfit')
        outfitGrp.setParent(u'MSH_all')
    fix_ch_side()
def renm_grp(SEL_GRP):
    grp_side_flg = pick_side_desc(SEL_GRP.name())
    print("========   {}".format(grp_side_flg))
    if grp_side_flg:
        p_side = get_name_membs(SEL_GRP.name())['sd']
        GET_CH = SEL_GRP.getChildren(c=True,type='transform',ad=True)
        for each in GET_CH:
            ea_nm = new_names(each, pk_sid=p_side)
            if ea_nm: each.rename(ea_nm)
        for each in GET_CH:
            fix_suffix_num(each)
        SEL_GRP.rename(new_names(SEL_GRP))
        fix_suffix_num(SEL_GRP)
        return None
    GET_CH = SEL_GRP.getChildren(c=True,type='transform')
    #cp_all = copy.deepcopy(GET_CH)
    for ea_ch in GET_CH:#ea_ch = GET_CH[0]
        side_flg = pick_side_desc(ea_ch.name())
        if side_flg:
            grndch = ea_ch.getChildren(c=True,type='transform',ad=True)
            if len(grndch):
                sel_nm_analysis = get_name_membs(ea_ch.name())
                p_side = sel_nm_analysis['sd']
                for each in grndch:
                    ea_nm = new_names(each,pk_sid = p_side)
                    if ea_nm: each.rename(ea_nm)
                for each in grndch:
                    fix_suffix_num(each)
            else:
                ea_ch.rename(new_names(ea_ch))
                fix_suffix_num(ea_ch)
            ea_ch.rename(new_names(ea_ch))
            fix_suffix_num(ea_ch)
        else:
            grndch = ea_ch.getChildren(c=True,type='transform',ad=True)
            if not (len(grndch)):
                ea_ch.rename(new_names(ea_ch))
                fix_suffix_num(ea_ch)
            else:  renm_grp(ea_ch)
    SEL_GRP.rename(new_names(SEL_GRP))
    # fix_suffix_num(SEL_GRP)
def ls_ch_side_flg(SEL_GRP):
    """
    列出指定物体的子物体并分类：

    :param SEL_GRP:
    :return: 返回字典 所有的
    """
    SEL_GRP_CH  = SEL_GRP.listRelatives(ad=True,c=True,type='transform')
    pick_side_grp = {}
    grndchs = []
    for ea_ch in SEL_GRP_CH:
        if pick_side_desc(ea_ch.name()):
            get_grnch  = ea_ch.listRelatives(ad=True,c=True,type='transform')
            if len(get_grnch):
                pick_side_grp[ea_ch] = ea_ch.listRelatives(ad=True,c=True,type='transform')
                grndchs.extend(get_grnch)
            else:
                pick_side_grp[ea_ch] = None
    for ea_ch in SEL_GRP_CH:
        if ea_ch not in grndchs and ea_ch not in pick_side_grp: pick_side_grp[ea_ch] = None
    return pick_side_grp

def Pre_regNaming_fix(pattern,repl,pos=False,ignCap = False,topSel=False):
    sel_MODEL = pm.selected()[0]
    getAll_trans = sel_MODEL.listRelatives(ad=True, c=True, type='transform')
    if not sel_MODEL: sel_MODEL = pm.selected()[0]
    for each in getAll_trans:
        # print ("will rename ======{}".format(each.name()))
        ea_nm = new_names(each)
        # print ea_nm
        if not ea_nm:continue
        # print("run line no  46==============")
        ea_nm = fix_modeName(pattern,repl,ea_nm,ignCap,pos)
        each.rename(ea_nm)
        # print('run line no   49 ======{}========='.format(each.name()))
    for each in getAll_trans:
        fix_suffix_num(each)
        # print ('======Rename object:{}================'.format(each.name()))
    sel_MODEL.rename(fix_modeName(pattern,repl,sel_MODEL.nodeName(),ignCap,pos))
    if not topSel:
        print(u'========regularizeed nodes name ==================')
        return None
    if sel_MODEL.name != u'MSH_all':
        sel_MODEL.rename(u'MSH_all')
    if not pm.objExists(u'MODEL'): pm.group(em=True,w=True,n=u'MODEL')
    sel_MODEL.setParent(u'MODEL')
    if not pm.objExists(u'MSH_geo'):
        geoGrp = pm.group(em=True,w=True,n=u'MSH_geo')
        geoGrp.setParent(u'MSH_all')
    if not pm.objExists(u'MSH_outfig'):
        outfitGrp = pm.group(em=True,w=True,n=u'MSH_outfit')
        outfitGrp.setParent(u'MSH_all')




def fix_modeName(pattern,repl,ndname,pos=False,ignCap = False):### sepecified a pattern replace source name
    newnm = None
    if pos == 'suffix':
        if ignCap:
            newnm = re.sub(u'{}$'.format(pattern),repl,ndname,re.I)
        else:
            newnm = re.sub(u'{}$'.format(pattern),repl,ndname)
    elif pos == 'prefix':
        if ignCap:
            newnm = re.sub(u'^{}'.format(pattern),repl,ndname,re.I)
        else:
            newnm = re.sub(u'^{}'.format(pattern),repl,ndname)
    else:
        if ignCap:
            newnm = re.sub(u'{}'.format(pattern),repl,ndname, re.I)
        else:
            newnm = re.sub(u'{}'.format(pattern),repl,ndname)
    return newnm

def fix_suffix_num(rnnode):#fix  "xxx_20"====> "xxx20_"
    ndname = rnnode.name()
    mod_idnm_search = re.search(u'_[\d]+$', ndname)
    if mod_idnm_search:
        suf_str = mod_idnm_search.group()
        idnm = re.search(u'\d+', mod_idnm_search.group()).group()
        rnnode.rename(re.sub(suf_str, u'_{}_'.format(idnm), ndname))

def new_names(nodeObj, prifix=u'MSH', suffix=u'_',precision= None, pk_sid = None):# return the new name string
    if not precision:
        scInf = Ppl_scInfo.Ppl_scInfo()
        precision = scInf.assetPrec
    # nodeObj = each
    nm_str = nodeObj.nodeName()
    nm_dic = get_name_membs(nm_str,pk_sid)
    # print nm_dic
    new_name_dict = {}
    if nm_dic['nm'] in [u'MSH_all',u'MSH_geo',u'MSH_outfit']: return None
    if nm_dic['nm'].startswith('MSH_'):
        nmsplt = nodeObj.nodeName().split('_')
        prifix = nmsplt[0]
        nm_dic['sd'] = nmsplt[1]
        precision = nmsplt[2]
        nm_dic['nm'] = '_'.join(nmsplt[3:])
    if not nodeObj.getShape():
        suffix = None
    new_name_dict = {'pr': prifix, 'prec': precision, 'nm': nm_dic['nm'], 'side': nm_dic['sd'], 'id': nm_dic['id']}
    new_name_list = [new_name_dict['pr']]
    for each in ['side', 'prec', 'nm', 'id']:
        # each = 'nm'
        if new_name_dict[each]:
            if each == 'nm':
                name_base = re.search(u'[\w]*[^0-9]+', new_name_dict['nm'], re.I).group()
                # name_base = re.sub(u'[_]+$',u'',name_base)
                name_base = re.sub(u'[\d_]+$', u'', name_base)
                if name_base.startswith('_'): name_base = re.sub('^_', '', name_base)
                new_name_list.append(name_base)
            elif each == 'id':
                suffix = None
                new_name_list.append(new_name_dict[each])
            else:  # each = 'nm'
                new_name_list.append(new_name_dict[each])
    new_name_list[-1] = re.sub(u'[_]+$', u'', new_name_list[-1])
    finally_nm = "_".join(new_name_list)
    if suffix and nodeObj.getShape():
        finally_nm += '_'
    final_nm = Kits4maya.Kits4maya.unique_name(finally_nm, suff=suffix)


    return final_nm
"""
def get_name_membs(nm_str,pk_sid=None): # return a dict, contains the new name needs membership
    new_name_dict = {}
    if not pk_sid:  pk_sid = pick_side_desc(nm_str)
    new_name_dict['nm'] = nm_str
    new_name_dict['id'] = None
    if isinstance(pk_sid,unicode) or isinstance(pk_sid,str):
        new_name_dict['sd'] = pk_sid
    elif isinstance(pk_sid,dict):
        re_nm_str = re.compile(pk_sid.values()[0].keys()[0])
        nm_str_n = re_nm_str.sub('_', nm_str)
        new_name_dict['sd'] = pk_sid.keys()[0]
        new_name_dict['nm'] = nm_str_n
        new_name_dict['id'] = pk_sid.values()[0].values()[0]
    else:
        new_name_dict['sd'] = u'c'
    return new_name_dict
"""
def get_name_membs(nm_str,pk_sid=None): # return a dict, contains the new name needs membership
    new_name_dict = {}
    pk_sid_dic = pick_side_desc(nm_str)
    if isinstance(pk_sid,unicode) or isinstance(pk_sid,str):
        new_name_dict['sd'] = pk_sid
    if pk_sid_dic:
        used_sid = pk_sid_dic.values()[0].keys()[0]
        nm_str_n = re.sub(used_sid,'',nm_str)
        nm_str_spl = nm_str.split(used_sid)
        if nm_str_spl[0] == 'MSH' and re.search('^MSH_', nm_str):
            nm_str_n = '_'.join(nm_str.split('_')[3:])
        if pk_sid : new_name_dict['sd'] = pk_sid
        else:
            new_name_dict['sd'] = pk_sid_dic.keys()[0]
        new_name_dict['nm'] = nm_str_n
        new_name_dict['id'] = pk_sid_dic.values()[0].values()[0]
    else:
        new_name_dict['sd'] = u'c'
        new_name_dict['nm'] = nm_str
        new_name_dict['id'] = None
    return new_name_dict


def pick_side_desc(nameStr): # on the basis of current mode's name,obtain model object on wich side including : r,l ,c
    re_pick_side = re.compile('(_|\s)[r|l][0-9]*[_]?', re.I)
    if not re_pick_side.search(nameStr):
        re_pick_side = re.compile("^[rl][0-9]*[_]?", re.I)
        if not re_pick_side.search(nameStr):
            re_pick_side = re.compile('[R|L]_')
            if not re_pick_side.search(nameStr): return None
    re_side = re.compile(u'r|l', re.I)
    re_num = re.compile(u'[0-9]+')
    side_dict = {}
    side_desc = ''
    mod_num = None
    side_desc = re_pick_side.search(nameStr).group()
    side_str = re_side.search(side_desc).group().lower()
    if re_num.search(side_desc):
        mod_num = re_num.search(side_desc).group()
    side_desc_dict = {side_desc: mod_num}
    side_dict[side_str] = side_desc_dict
    return side_dict


def get_side(selGrp):
    find_side = re.search('MSH_(r|l)_', selGrp.name(), re.I)
    if find_side:
        side = re.search('[^(MSH)_]', find_side.group(), re.I).group()
        return side


def fix_ch_side():
    SEL_GRP = None
    if pm.selected():
        SEL_GRP = pm.selected()[0]
    else:
        SEL_GRP = pm.PyNode('MODEL')
    ch_grps = []
    for c in SEL_GRP.listRelatives(type='transform', ad=True, c=True):
        for c2 in c.getChildren():
            if c2.type() != 'transform':
                continue
            else:
                if c not in ch_grps: ch_grps.append(c)
    if not ch_grps:
        ch_grps = [SEL_GRP]
    for grp in ch_grps:
        if not get_side(grp): continue
        side = get_side(grp)
        for e in grp.getChildren():
            add_suff = None
            eNM = e.name()
            eNM_noSuff = eNM
            if e not in ch_grps:
                add_suff = True
                eNM_noSuff = eNM.strip('_')
            nmspl = eNM_noSuff.split('_')
            new_nm_str = '{}_{}_{}_{}'.format(nmspl[0], side, nmspl[2], nmspl[-1])
            if add_suff: new_nm_str += '_'
            e.rename(new_nm_str)
