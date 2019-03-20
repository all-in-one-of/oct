#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ABC_tmp
__author__ = zhangben 
__mtime__ = 2019/3/19 : 20:50
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import pymel.core as pm
import json
import re
import maya.cmds as mc
import os

if not mc.pluginInfo("AbcImport",q=True,loaded=True):
    mc.loadPlugin('AbcImport',quiet = True)


def wr2f(doCache=True):
    selObj = pm.ls(sl=True)
    new_add = {}
    nmsp = selObj[0].namespace().strip(':')
    for ea in selObj:
        needName = ea.stripNamespace().strip()
        new_add[needName] = ea.longName(stripNamespace=True)
    wsp = pm.workspace.name
    with open(r"{}/{}_caOBjList.json".format(wsp,nmsp), 'w') as f:
        f.write(json.dumps(new_add, indent=4))
    if doCache: mc.AlembicExportSelectionOptions()




def r4f():
    wsp = pm.workspace.name
    singleFilter = "All Files (*.*)"
    res = mc.fileDialog2(fileFilter=singleFilter, dialogStyle=2,fileMode=4)
    readDate = {}
    for af in res:
        ext = os.path.splitext(af)[-1]
        if ext == ".abc": readDate['abc'] = af
        elif ext == '.json': readDate['js'] = af
    with open(readDate['js'], 'r') as f:
        readDate['cclst']= json.load(f)
    return readDate

def list_rdcc_meshs(infor):
    #infor = r4f()
    cc_meshes = infor['cclst']
    readCcMsh = {}
    sel_chr = pm.selected()[0]
    for eaMesh in sel_chr.getChildren(type='mesh',ad=True,ni=True):
        ea_nm = eaMesh.name(stripNamespace=True)
        ea_p = eaMesh.getParent()
        if ea_p.name(stripNamespace=True) in cc_meshes and eaMesh not in readCcMsh: readCcMsh[eaMesh] = ea_p
    pm.select(readCcMsh.values(),r=True)
    return readCcMsh

def im_cache(infor,con_cc_meshes):
    #infor = r4f()
    abc_f = infor['abc']
    #con_cc_meshes = {}
    sel_chr = pm.selected()[0]
    con_objs = [m.longName() for m in con_cc_meshes.values()]
    con_str = " ".join(con_objs)
    mc.AbcImport(abc_f, mode='import', connect = con_str)



    # AlembicImportOptions;
    # performAlembicImport 1 2;
    #
    # AbcImport - mode
    # import
    # -setToStartFrame - debug - connect
    # "yi_45 KOUZI xie_L xie_R yi_48 yi_49 yi_54 yi_50 yi_53 yi_52 polySurface5 L_shoutao R_shoutao kuzi yi_55 sijin_Model head_Model dn_teeth dn_oral up_teeth up_oral tongue R_eye R_eyecon L_eye L_eyecon R_Lash L_Lash leixian_r leixian_l maozi grow_mesh" - createIfNotFound - removeIfNoUpdate
    # "E:/work/FAQ_ALL/cache/alembic/all_exp_abc_003.abc";
    # AbcExport -j "-frameRange 11861 11871 -uvWrite -worldSpace -writeVisibility -dataFormat ogawa -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_45 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:KOUZI -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_L -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_R -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_48 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_49 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_54 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_50 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_53 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_52 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_51|CDMSS_ch001001Moss_l_msAnim:polySurface5 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:L_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:R_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:kuzi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_55 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:sijin_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:head_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:tongue -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:R_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:L_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_r -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_l -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:Yeti|CDMSS_ch001001Moss_l_msAnim:Growmesh|CDMSS_ch001001Moss_l_msAnim:grow_mesh -file E:/work/FAQ_ALL/cache/alembic/all_exp_abc_004.abc";
# AbcExport -j "-frameRange 11861 11871 -stripNamespaces -uvWrite -worldSpace -writeVisibility -dataFormat ogawa -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_45 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:KOUZI -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_L -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:xie1|CDMSS_ch001001Moss_l_msAnim:xie_R -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_48 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_49 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_54 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_50 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_53 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_52 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_51|CDMSS_ch001001Moss_l_msAnim:polySurface5 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:L_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:R_shoutao -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:kuzi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:yi_55 -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:CDMSS_ch001002MossV2_h_mo2|CDMSS_ch001001Moss_l_msAnim:yi|CDMSS_ch001001Moss_l_msAnim:sijin_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:head_Model -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:dn_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_teeth -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:up_oral -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:kouqiang|CDMSS_ch001001Moss_l_msAnim:tongue -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eye_grp|CDMSS_ch001001Moss_l_msAnim:R_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eye_grp|CDMSS_ch001001Moss_l_msAnim:L_eyecon -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:R_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:Head_G|CDMSS_ch001001Moss_l_msAnim:L_Lash -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_r -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi_maofa_g|CDMSS_ch001001Moss_l_msAnim:leixian_l -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:tou_new|CDMSS_ch001001Moss_l_msAnim:maozi -root |DH|chr|CDMSS_ch001001Moss_l_msAnim:allAnim|CDMSS_ch001001Moss_l_msAnim:Yeti|CDMSS_ch001001Moss_l_msAnim:Growmesh|CDMSS_ch001001Moss_l_msAnim:grow_mesh -file E:/work/FAQ_ALL/cache/alembic/all_exp_abc_005.abc";
# AbcImport -mode import -setToStartFrame -debug -connect "CDMSS_ch001002MossV2_Hair_h_msAnim:yi_45 CDMSS_ch001002MossV2_Hair_h_msAnim:KOUZI CDMSS_ch001002MossV2_Hair_h_msAnim:up_oral CDMSS_ch001002MossV2_Hair_h_msAnim:yi_54 CDMSS_ch001002MossV2_Hair_h_msAnim:L_eye CDMSS_ch001002MossV2_Hair_h_msAnim:L_shoutao CDMSS_ch001002MossV2_Hair_h_msAnim:leixian_r CDMSS_ch001002MossV2_Hair_h_msAnim:R_Lash CDMSS_ch001002MossV2_Hair_h_msAnim:up_teeth CDMSS_ch001002MossV2_Hair_h_msAnim:yi_50 CDMSS_ch001002MossV2_Hair_h_msAnim:maozi CDMSS_ch001002MossV2_Hair_h_msAnim:kuzi CDMSS_ch001002MossV2_Hair_h_msAnim:leixian_l CDMSS_ch001002MossV2_Hair_h_msAnim:xie_L CDMSS_ch001002MossV2_Hair_h_msAnim:dn_teeth CDMSS_ch001002MossV2_Hair_h_msAnim:yi_55 CDMSS_ch001002MossV2_Hair_h_msAnim:sijin_Model CDMSS_ch001002MossV2_Hair_h_msAnim:yi_53 CDMSS_ch001002MossV2_Hair_h_msAnim:L_eyecon CDMSS_ch001002MossV2_Hair_h_msAnim:R_eyecon CDMSS_ch001002MossV2_Hair_h_msAnim:head_Model CDMSS_ch001002MossV2_Hair_h_msAnim:polySurface5 CDMSS_ch001002MossV2_Hair_h_msAnim:tongue CDMSS_ch001002MossV2_Hair_h_msAnim:R_shoutao CDMSS_ch001002MossV2_Hair_h_msAnim:grow_mesh CDMSS_ch001002MossV2_Hair_h_msAnim:yi_49 CDMSS_ch001002MossV2_Hair_h_msAnim:R_eye CDMSS_ch001002MossV2_Hair_h_msAnim:yi_48 CDMSS_ch001002MossV2_Hair_h_msAnim:L_Lash CDMSS_ch001002MossV2_Hair_h_msAnim:dn_oral CDMSS_ch001002MossV2_Hair_h_msAnim:xie_R CDMSS_ch001002MossV2_Hair_h_msAnim:yi_52" -createIfNotFound -removeIfNoUpdate "E:/work/FAQ_ALL/cache/alembic/all_exp_abc_001.abc";

if __name__ == "__main__":
#先运行 下面两行代码
    import OCT_anim.ABC_tmp as abct
    reload(abct)

    # ===== 动画师 输出 缓存 和 记录 选择模型信息文件 执行下面一行代码
    abct.wr2f()
    # ==== 运行之后，会在 当前工程目录 路径 下 有一个 .json 格式的文件，这个文件是记录 选择的模型的
    # 把输出的缓存 和这个 json 文件 一并 提供给 美术师
    #===================================================================================================================
    """
    =====灯光美术师 选择要读取缓存的模型的组(要import，因为在两个leixia模型的设置并不全是rig蒙皮
    
    一共三行代码 逐行运行 选择到 当前角色读取缓存的模型，要进行解锁和删除历史操作
    """
    # 第一步 选择缓存 和记录模型信息的文件 导入相关信息
    info = abct.r4f()
    # 第二步 确保已选择要读取缓存的角色的大组(是该角色的大组）根据动画师记录的信息程序会选择相应的模型
    con_cc_objs = abct.list_rdcc_meshs(info)
    # 第三部，对当前选择的模型进行，清历史，解锁通道栏translate属性，
    # 第四部 运行下面脚本
    abct.im_cache(info, con_cc_objs)