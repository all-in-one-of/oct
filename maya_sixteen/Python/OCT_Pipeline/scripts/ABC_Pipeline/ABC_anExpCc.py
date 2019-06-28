#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ABC_anExpCc.py
__author__ = zhangben 
__mtime__ = 2019/5/17 : 20:33
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import maya.cmds as mc
import pymel.core as pm
import os,re
from ..Major import Ppl_scInfo
from ..utility import Kits4maya

def findNodeByName(oneRef,nodeName):
    rfnd = oneRef.refNode
    rf_nmspc = rfnd.associatedNamespace(1)
    #rf_nmspc = oneRef.namespace
    exact_nd_nm = "{}:{}".format(rf_nmspc,nodeName)
    findNode = None
    try:
        findNode = pm.PyNode(exact_nd_nm)
    except:
        return None
    if rfnd.containsNodeExactly(findNode):
        if not findNode.getShape(): return findNode
        else: return None
def an_exp_cc(filterAttr='alembic',exStp=1,ref_mode = True):
    """
    针对当前的流程 提供给maya 批处理完成的 对动画文件输出缓存的 版本
    AbcExport -j "-frameRange 1000 1100 -ro -uvWrite -worldSpace -writeVisibility -dataFormat ogawa -root |basGrp|cube|pCube1 -root |basGrp|ball|pSphere1 -root |basGrp|pPlane1 -file E:/work/JMWC/cache/alembic/aaassss.abc";


    AbcImport -mode replace "E:/work/JMWC/cache/alembic/aaassss.abc";

    AbcImport -mode import -setToStartFrame -connect "SMMXW_ch001001TyrannosaurusRex_h_msAnim:FKBS_ch002001TyrannosaurusRex_zhijia SMMXW_ch001001TyrannosaurusRex_h_msAnim:FKBS_ch002001TyrannosaurusRex_yachi SMMXW_ch001001TyrannosaurusRex_h_msAnim:FKBS_ch002001TyrannosaurusRex_shetou SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_L_01 SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_L_02 SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_L_03 SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_R_01 SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_R_02 SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_R_03 SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_L_01_new SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_L_02_new SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_L_03_new SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_R_01_new SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_R_02_new SMMXW_ch001001TyrannosaurusRex_h_msAnim:ch002001TyrannosaurusRex_eye_R_03_new SMMXW_ch001001TyrannosaurusRex_h_msAnim:FKBS_ch002001TyrannosaurusRex_body SMMXW_ch001001TyrannosaurusRex_h_msAnim:FKBS_ch002001TyrannosaurusRex_kouqiang SMMXW_ch001001TyrannosaurusRex_h_msAnim:FKBS_ch002001TyrannosaurusRex_body_new SMMXW_ch001001TyrannosaurusRex_h_msAnim:face_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:face_base_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:jaw_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:freq_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:neck_dw_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:neck_up_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:sine_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:face_sec_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:L_eye1_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:L_eye2_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:L_eye3_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:R_eye1_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:R_eye2_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:R_eye3_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:face_sec_loc_geo SMMXW_ch001001TyrannosaurusRex_h_msAnim:new_body_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:body_mus_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:body_all_old_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:body_all_bs SMMXW_ch001001TyrannosaurusRex_h_msAnim:Facial_BG_Plane" -createIfNotFound "E:/work/JMWC/cache/alembic/SMMXW_sc09_sh01_ch001001TyrannosaurusRex.abc";

    """
    # shotType = 2 # 默认值是2 ，镜头按场次镜头来划分，备用于切分为3的 模式
    # exStp = 1
    # filterAttr = 'alembic'
    # filterAttr = None
    #parse shot information
    # parse shot information
    STORDATE = {}
    scInfo = Ppl_scInfo.Ppl_scInfo()
    k4m = Kits4maya.Kits4maya()
    if not mc.pluginInfo('KLJZ_dts.py', q=True, l=True):
        mc.loadPlugin("//octvision.com/cg/Tech/maya_sixteen/Plugins/KLJZ_dts.py")
    if not pm.pluginInfo('AbcExport', q=True, l=True):
        pm.loadPlugin('AbcExport')
    if not pm.pluginInfo('AbcImport', q=True, l=True):
        pm.loadPlugin('AbcImport')
    error_msg = {}
    shot_nm_bs = scInfo.scbsnm
    shot_dir = scInfo.cwd_local
    shot_nm_repr_lst = [scInfo.proj,scInfo.ID,scInfo.descr] if scInfo.descr else [scInfo.proj,scInfo.ID]
    shot_nm_repr = '_'.join(shot_nm_repr_lst)
    # wsps_cc_dir = pm.workspace(en='cache')
    # wsps_sc_dir = pm.workspace(en='scenes')
    wsps_sc_dir = shot_dir
    wsps_cc_dir = "{}/cache".format(scInfo.projPath_loc)
    exp_abc_dir = '{}/alembic/'.format(wsps_cc_dir)
    exp_mb_dir = "{}/mayabatchOPT/".format(wsps_sc_dir)
    st_frm = int(pm.playbackOptions(q=True, min=True))
    end_frm = int(pm.playbackOptions(q=True, max=True))
    # for each reference
    proc_grps = pm.selected() if not ref_mode else pm.listReferences()
    # oneRef = proc_grps[-1]
    if not proc_grps:
        proc_grps = get_chprGrp(scInfo.proj)
        ref_mode = False
    if not proc_grps: pm.error(u"程序没有找到需要做缓存的角色或道具组,请检查角色或者道具组的namespace是否正确。")
    for oneRef in proc_grps:
        ref_nsp = oneRef.namespace().strip(':') if not ref_mode else oneRef.namespace
        oneRef_top = None
        if ref_mode:
            oneRef_top = oneRef.nodes()[0]
        else:
            lngnmSpl = oneRef.longName().split('|')
            n = -1
            for m in range(len(lngnmSpl)):
                if re.search(ref_nsp, lngnmSpl[m]):
                    n = m
                    break
            oneRef_top = pm.PyNode('|'.join(lngnmSpl[:n + 1]))
        # ref_f_bsnm = os.path.basename(ref_f)
        # ref_f_nmspl = ref_f_bsnm.split('_')
        ref_f_nmspl = ref_nsp.split('_')
        ref_type = re.search('\w{2}', ref_f_nmspl[1]).group()
        if ref_type not in ['ch','pr']: continue
        reprChar = re.search("[^\d]+[\d]*$", ref_f_nmspl[1], re.I).group()
        ref_No = ''
        if re.search('\d+$', ref_nsp): ref_No = re.search('\d+$', ref_nsp).group()
        ref_repr_Char4cc = "{}{}".format(ref_f_nmspl[1], ref_No)
        ref_repr_Char4mb = "{}{}".format(reprChar, ref_No)
        exp_abc_nm = "{}{}_{}.abc".format(exp_abc_dir, shot_nm_repr, ref_repr_Char4cc)
        exp_mb_nm = "{}{}_{}_cc.mb".format(exp_mb_dir, shot_nm_repr, ref_repr_Char4mb)
        need2cc = None
        if filterAttr:
            if ref_mode:
                need2cc = [e_nd.getParent().longName() for e_nd in oneRef.nodes() if e_nd.type() in [u'mesh'] and e_nd.getParent().hasAttr(filterAttr)]
                if not need2cc:
                    need2cc = [e_nd.getParent().longName() for e_nd in oneRef.nodes() if e_nd.type() in [u'mesh'] and not e_nd.isIntermediate()]
            else:
                need2cc = [e_nd.getParent().longName() for e_nd in oneRef_top.listRelatives(c=True, type='mesh', ad=True, ni=True) if
                           e_nd.getParent().hasAttr(filterAttr)]
                if not need2cc:
                    need2cc = [e_nd.getParent().longName() for e_nd in oneRef_top.listRelatives(c=True, type='mesh', ni=True, ad=True)]
        else:
            if ref_mode:
                need2cc = [e_nd.getParent().longName() for e_nd in oneRef.nodes() if e_nd.type() in [u'mesh'] and not e_nd.isIntermediate()]
            else:
                need2cc = [e_nd.getParent().longName() for e_nd in oneRef_top.listRelatives(c=True, type='mesh', ni=True, ad=True)]
        pm.select(need2cc, r=True)
        # add by zhangben 2019 06 21  老鼠项目，要导出毛发部分
        yetiGrp = None
        if scInfo.proj in ['SLD']:
            if findNodeByName(oneRef, 'yeti'):  yetiGrp = findNodeByName(oneRef, 'yeti')
        need2cc_str = "-root {}".format(' -root '.join(need2cc))
        j_str = "-frameRange {} {} -step {} -uvWrite -writeVisibility -worldSpace {} -f {} -pythonPerFrameCallBack \"print(\\\"...Writing Cache...\\\")\"".format(st_frm, end_frm,
                                                                                                                                             exStp, need2cc_str,
                                                                                                                                             exp_abc_nm)
        try:
            mc.AbcExport(j=j_str)
        except BaseException,e:
            error_msg[oneRef_top.nodeName()] = e.message
        else:
            print(">>>Cache Generated on disk---{}".format(exp_abc_nm))
            if ref_mode:
                oneRef.importContents()
            pm.select(need2cc)
            pm.delete(ch=True)
            if scInfo.proj in ["SLD"]:
                for ea_trn_nm in need2cc:
                    ea_trn = pm.PyNode(ea_trn_nm)
                    ea_mesh = ea_trn.getShape()
                    if ea_mesh.listConnections(type="pgYetiGroom"):continue
                    ea_con_sg = ea_mesh.shadingGroups()
                    k4m.power_disconect(ea_mesh,ea_con_sg)
            chkGrp = []
            for n in oneRef_top.getChildren():
                for m in need2cc:
                    if n.hasChild(m):
                        chkGrp.append(n)
                        break
            for eaGrp in chkGrp:
                if re.search('yeti', eaGrp.name(), re.I): continue
                allTrns = [j for j in eaGrp.getChildren(ad=True, type='transform') if j.nodeType() == 'transform']
                for k in allTrns:
                    if k.listConnections(s=True, d=False,type='constraint'):
                        cons_asTarg = k.listConnections(c=True, p=True, s=True, d=False, type='constraint')
                        for ea_c in cons_asTarg:
                            attrName = ea_c[0].attrName()
                            try:
                                ea_c[1] // ea_c[0]
                                if attrName in ['csx', 'csy', 'csz']: eaGrp.attr(attrName).set(1)
                                else: eaGrp.attr(attrName).set(0)
                            except Exception,e:
                                error_msg[">>>Break Constraint occurs Error on node {}".format(eaGrp.name())]=e.message
            imp_cc_str = ' '.join(need2cc)
            mc.AbcImport(exp_abc_nm, mode="import", setToStartFrame=True, connect=imp_cc_str, createIfNotFound=True)
            pm.select(need2cc, r=True)
            if yetiGrp:
                cons_asSrc = yetiGrp.listConnections(c=True, p=True, d=True, s=False)
                cons_asTarg = yetiGrp.listConnections(c=True, p=True, s=True, d=False)
                if cons_asTarg:
                    for ea_c in cons_asTarg:
                        ea_c[1] // ea_c[0]
                if cons_asSrc:
                    for ea_c in cons_asSrc:
                        ea_c[0] // ea_c[1]
                yetiGrp.attr('visibility').set(1)
                for ea in yetiGrp.listRelatives(ad=True, c=True, type='pgYetiMaya'):
                    ea.getParent().attr('visibility').set(1)
                pm.select(yetiGrp,add=True)
            pm.exportSelected(exp_mb_nm, f=True, options="v=0", type="mayaBinary", pr=True, es=True)
            print("===> MB File exported to :{}{}".format(exp_mb_nm,os.linesep))
    if error_msg != {}:
        for e_error in error_msg:
            print ("\t{}\t{}".format(e_error,error_msg[e_error]))
        mc.warning(">>>There happen some issues while performming task : {} , list the error codes{}".format(shot_nm_bs, os.linesep))
    else:
        print("{0}>>>CACHE EXPORTED!!!!{0}\tCache Start Frame : {1}  Cache End Frame : {2}".format(os.linesep,st_frm,end_frm))

def get_chprGrp(projName):
    re_chprGrp = re.compile("^({0}_ch)|({0}_pr)".format(projName))
    allGrps = [ea for ea in pm.ls(type='transform') if not ea.getShape() and ea.name(stripNamespace=True).lower() == "allanim"]
    chprGrps = [ea for ea in allGrps if re_chprGrp.search(ea.namespace())]
    return chprGrps