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
import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om


class Kits4maya(object):
    """
    some kits  little procedures are collected here

    """
    def __init__(self):
        self.rec_refs = []
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
            name_again = Kits4maya.unique_name(new_nm, num, suff)
            return name_again

    def get_ArTx(self,src):#把arnold tx文件加入copy列表
        if not mc.getAttr("defaultRenderGlobals.currentRenderer") =="arnold": return None
        fileSpl = os.path.splitext(src)
        txf_pth = fileSpl[0] + u'.tx'
        if txf_pth == src:return None
        else: return txf_pth

    def recover_ref_mat(self):
        sel_nods = pm.selected()
        sel_refs = [eas.referenceFile() for eas in sel_nods if eas.isReferenced()]
        sel_refs = [sel_refs[n] for n in range(len(sel_refs)) if sel_refs[n] not in sel_refs[:n]]
        need_new_ref_pth = {}
        for ea_ref in sel_refs:
            ref_file = ea_ref.path.strip()
            ref_nsp = ea_ref.namespace
            ref_anew = None
            if ref_file not in need_new_ref_pth:
                ref_anew = pm.createReference(ref_file,namespace='ReMat_{}'.format(ref_nsp))
                need_new_ref_pth[ref_file] = ref_anew
            else:
                ref_anew = need_new_ref_pth[ref_file]
            new_ref_nods = ref_anew.nodes()
            new_ref_nsp = ref_anew.namespace
            bb = new_ref_nods[15]
            faileds = self.failed_nodeplugs(ea_ref)
            for a_cmd in faileds:
                # a_cmd = faileds[1]
                nd = a_cmd['node']
                nd_nm = nd.nodeName(stripNamespace=True)
                nd_plg = a_cmd['plug']

                nd_plg_attr_nm = nd_plg.attrName(longName=True)
                nd_plg_attr_nm_str = '.{}'.format(".".join(nd_plg.name().split('.')[1:]))

                nd_plg_con2 = nd_plg.listConnections(p=True, d=True, s=False)[0]
                nd_plg_con2_nm_str = '.{}'.format(".".join(nd_plg_con2.name().split('.')[1:]))

                nd_plg_conS = nd_plg.listConnections(p=True, c=True)[0]

                newRef_nd = self.nodeTest(ref_anew, nd_nm)
                newRef_attr = newRef_nd.attr(nd_plg_attr_nm)
                # destinate plug
                newRef_plg_con2 = newRef_attr.listConnections(d=True, p=True)
                if not newRef_plg_con2:
                    mc.warning(">>> newRef_attr has no connected!!!!!")
                else:
                    newRef_plg_con2 = newRef_plg_con2[0]
                newRef_plg_con2_node = newRef_plg_con2.node()
                newRef_plg_con2_nm_str = '.{}'.format(".".join(newRef_plg_con2.name().split('.')[1:]))
                newRef_ndAttr = "{}{}".format(newRef_plg_con2_node.name(stripNamespace=True), newRef_plg_con2_nm_str)
                # source plug
                newRef_plg_conS = newRef_attr.listConnections(c=True, p=True)[0]
                newRef_plg_con_attr = [ea_plg for ea_plg in newRef_plg_conS if ea_plg != newRef_plg_con2][0]
                newRef_plg_con_attr_nm_str = '.{}'.format(".".join(newRef_plg_con_attr.name().split('.')[1:]))
                find_targ = self.find_node(ea_ref, newRef_ndAttr)
                if not find_targ: continue
                con2 = find_targ['nd'].attr(find_targ['attr'])
                nd_plg_conS[0] // nd_plg_conS[1]
                nd_plg_conS[0] >> con2
        for ea in need_new_ref_pth:
            need_new_ref_pth[ea].remove

    def nodeTest(self,ref, kwd):
        res = ''
        for ea in (ea for ea in ref.nodes() if re.search('{}$'.format(kwd), ea.name())):
            if not 'isIntermediate' in dir(ea):
                return ea
            else:
                if not ea.isIntermediate(): return ea

    # def failed_nodeplugs(self,ea_ref, melCmd='disconnectAttr', cmdArgs=['-na'], searchKwd='.instObjGroups'):
    #     # ea_ref = refs[1]
    #     # ea_ref_nd = ea_ref
    #     ea_ref.getReferenceEdits()
    #     failed_edts = pm.referenceQuery(ea_ref.refNode, ec=melCmd, es=True, fld=True)
    #     res_lst = []
    #     for eaItem in failed_edts:
    #         if not re.search(searchKwd, eaItem): continue
    #         itm_spl = eaItem.split(' ')
    #         res = {'cmd': melCmd, 'args': cmdArgs, 'node': None, 'plug': None, 'fullCmd': eaItem}
    #         for ea in itm_spl:
    #             if ea in cmdArgs: continue
    #             if re.search(searchKwd, ea):
    #                 src_plg_str = itm_spl[2].strip('\"').strip('\'')
    #                 src_plg = pm.PyNode(src_plg_str)
    #                 res['plug'] = src_plg
    #                 res['node'] = src_plg.node()
    #         res_lst.append(res)
    #     return res_lst

    # nrf_node = pm.selected()[0]
    #
    # # nrf_conSGs = nrf_node.listConnections(c=True,p=True,type='shadingEngine')
    # nrf_asSrc = nrf_node.listConnections(d=True, s=False, p=True, type='shadingEngine', c=True)
    # nrf_asDest = nrf_node.listConnections(d=False, s=True, p=True, type='shadingEngine', c=True)
    #
    # a_con = nrf_asSrc[1]
    #
    # rv = False
    # n_con_src, n_con_targ = (a_con[0], a_con[1]) if not rv else (a_con[1], a_con[0])
    #
    # n_con_src_plg_nm = '.{}'.format(".".join(con_src.name().split('.')[1:]))
    # n_con_targ_plg_nm = '.{}'.format(".".join(con_targ.name().split('.')[1:]))
    #
    # n_con_src_nd = con_src.node()
    # n_con_targ_nd = con_targ.node()
    #
    # o_con_src_nd = find_node(ea_ref, n_con_src.name())

    # def find_node_inRef(self,ref, plg):
    #     # plg = n_con_src
    #     # ref = ea_ref
    #     # pls_spl = plsStr.split('.')
    #     ref_nsp = ref.namespace
    #     plg_nd = plg.node()
    #     ndnm_str = plg_nd.name(stripNamespace=True)
    #     attr_str = '.'.join(plg.name().split('.')[1:])
    #     exacNode = None
    #     exacNode = self.nodeTest(ref, ndnm_str)
    #     if not exacNode:
    #         mc.warning(u"{0}>>>检查参考节点 : {1} 的 名字为 {2} 的 节点是否存在{0}".format(os.linesep, ref.refNode.name(), ndnm_str))
    #         return None
    #     return {'nd': exacNode, 'attr': attr_str}
    # def conectNewRef(o_cn_date, n_ctrl, asDest=True):#
    #     asDest = True
    #     for a_con in o_cn_date:
    #         # a_con = o_cn_asDes[0]
    #         o_cn_src, o_cn_targ = (a_con[1], a_con[0]) if asDest else (a_con[0], a_con[1])
    #         src_nd = o_cn_src.node()
    #         targ_nd = o_cn_targ.node()
    #         targ_nd_udAttr = targ_nd.listAttr(ud=True)
    #         if src_nd.isReferenced() and src_nd.referenceFile() == ea_ref: continue
    #         o_cn_src_nm = o_cn_src.name()
    #         o_cn_targ_nm = o_cn_targ.name()
    #         o_cn_targ_plg_nm = o_cn_targ.attrName(longName=True)
    #         n_plg = None
    #         if o_cn_targ in targ_nd_udAttr:
    #             n_plg = n_ctrl.listAttr(ud=True)[0]
    #         else:
    #             n_plg = n_ctrl.attr(o_cn_targ_plg_nm)
    #         # o_cn_src//o_cn_targ
    #         print(">>>Disconnect =={} ===>>> {}".format(o_cn_src, o_cn_targ))
    #         o_cn_src >> n_plg
    #         print(">>>Connect =={} ===>>> {}".format(o_cn_src, n_plg))
    def find_node(self,ref, plsStr):
        # pls_spl = plsStr.split('.')
        ref_nsp = ref.namespace
        ndnm_str, attr_str = plsStr.split('.')[0], '.'.join(plsStr.split('.')[1:])
        exacNode = None
        if pm.objExists(ndnm_str):
            exacNode = pm.PyNode(ndnm_str)
        else:
            ndnm_str_sht = ndnm_str.split('|')[-1]
            ndnm_str_sht_nspStrip = re.sub('{}:'.format(ref_nsp), '', ndnm_str_sht)
            exacNode = self.nodeTest(ref, ndnm_str_sht_nspStrip)
            if not exacNode:
                mc.warning(u"{0}>>>检查参考节点 : {1} 的 名字为 {2} 的 节点是否存在{0}".format(os.linesep, ref.refNode.name(), ndnm_str))
                return None
        return {'nd': exacNode, 'attr': attr_str}

    def re_ref_tools_ui(self):
        if mc.window("rerefence_win", exists=True, q=True):
            mc.deleteUI("rerefence_win")

        toolWin = pm.window("rerefence_win", t=u"选择要替换参考的物体或参考", w=300)
        m_clm = pm.columnLayout(columnAttach=('both', 5), rowSpacing=20, columnWidth=300, p=toolWin)
        runBt = pm.button('runBt', l=u"替换参考", c= self.re_constraint_GunAndAircraft)
        remBt = pm.button('remBt', l=u"移除原参考", c=self.rm_oldRefs)
        pm.window("rerefence_win",e=True,w=300,h=80)
        toolWin.show()

    def rm_oldRefs(self):
        for eaRef in self.rec_refs:
            eaRef.remove()
    def re_constraint_GunAndAircraft(self):# 重新参考 飞行器和枪，做约束链接
        """
        """
        sel_nods = pm.selected()
        sel_refs = [eas.referenceFile() for eas in sel_nods if eas.isReferenced()]
        sel_refs = [sel_refs[n] for n in range(len(sel_refs)) if sel_refs[n] not in sel_refs[:n]]
        self.rec_refs = sel_refs
        for ea_ref in sel_refs:
            #ea_ref = sel_refs[0]
            ref_top = ea_ref.nodes()[0]
            c_p = ref_top.getParent()
            ref_file = ea_ref.path.strip()
            ref_nsp = ea_ref.namespace
            ref_anew = pm.createReference(ref_file,namespace = ref_nsp)
            n_ref_nsp = ref_anew.namespace
            n_top = ref_anew.nodes()[0]
            n_top.setParent(c_p)
            ls_nTop_cns = ref_top.listConnections(s=True,c=True,d=False,p=True)
            if ls_nTop_cns:
                for ea_cons in ls_nTop_cns:
                    ea_cons =  ls_nTop_cns[0]
                    top_con_srcPlg,top_con_destPlg = ea_cons[1],ea_cons[0]
                    destPlg_nm = top_con_destPlg.attrName()
                    top_con_srcPlg >> n_top.attr(destPlg_nm)
            ctrls = {'pr008001Aircraft':['masterShape','mainShape'],'pr007001StunGun':['MasterShape','MainShape']}
            ea_ctr = re.search('(pr008001Aircraft)|(pr007001StunGun)',ref_nsp).group()
            for ctr_kw in ctrls[ea_ctr]:
                #ctr_kw = ctrls[ea_ctr][1]
                o_ctrl_sh = self.nodeTest(ea_ref,ctr_kw)
                n_ctrl_sh = self.nodeTest(ref_anew,ctr_kw)
                o_ctrl = o_ctrl_sh.getParent()
                n_ctrl = n_ctrl_sh.getParent()
                #pm.select(o_ctrl)
                #pm.select(n_ctrl)
                k_attrs = [ea.attrName(longName=True) for ea in n_ctrl.listAttr(k=True)]
                [n_ctrl.attr(n).set(o_ctrl.attr(n).get()) for n in k_attrs]
                [n_ctrl.attr(n).setKey() for n in k_attrs]
                o_ctrl_beCnstr_attr = o_ctrl.attr('parentInverseMatrix')
                tmp_prcn = o_ctrl_beCnstr_attr.listConnections(d=True,s=False,type='parentConstraint')
                if tmp_prcn:
                    get_PCnstr = [tmp_prcn[n].node() for n in range(len(tmp_prcn)) if tmp_prcn[n].node() not in tmp_prcn[:n]]
                    for ea_cnstr in get_PCnstr:
                        targ_attr = ea_cnstr.attr('target')
                        doCnstr  = [ea[1].node() for ea in targ_attr.listConnections(s=True,d=False,c=True,et=True,t='transform')]
                        doCnstr = [doCnstr[n] for n in range(len(doCnstr)) if doCnstr[n] not in doCnstr[:n]]
                        pm.parentConstraint(doCnstr,n_ctrl,mo=True)
                o_ctrl_asDest = o_ctrl.listConnections(s=True,d=False,p=True,c=True)
                asDest = True
                for a_con in o_ctrl_asDest:
                    #a_con = o_ctrl_asDest[1]
                    o_cn_src, o_cn_targ = (a_con[1], a_con[0]) if asDest else(a_con[0], a_con[1])
                    src_nd = o_cn_src.node()
                    targ_nd = o_cn_targ.node()
                    targ_nd_udAttr = targ_nd.listAttr(ud=True)
                    if src_nd.isReferenced() and src_nd.referenceFile() == ea_ref:continue
                    o_cn_src_nm = o_cn_src.name()
                    o_cn_targ_nm = o_cn_targ.name()
                    o_cn_targ_plg_nm = o_cn_targ.attrName(longName=True)
                    n_plg = None
                    if o_cn_targ in targ_nd_udAttr: n_plg = n_ctrl.listAttr(ud=True)[0]
                    else: n_plg = n_ctrl.attr(o_cn_targ_plg_nm)
                    #o_cn_src//o_cn_targ
                    print(">>>Disconnect =={} ===>>> {}".format(o_cn_src,o_cn_targ))
                    o_cn_src >> n_plg
                    print(">>>Connect =={} ===>>> {}".format(o_cn_src,n_plg))
                o_ctrl_cnstr_attr = o_ctrl.attr('translate')
                o_ctrl_cnstr_other = o_ctrl_cnstr_attr.listConnections(d=True,s=False,type='parentConstraint',et=True)
                if not o_ctrl_cnstr_other: continue
                for ea_cnstr in o_ctrl_cnstr_other:
                    #beCnstr_trans = ea_cnstr.attr('constraintParentInverseMatrix').listConnections(type='transform',et=True)
                    listAll_pls = ea_cnstr.listConnections(d=False,s=True,type='transform',et=True,c=True,p=True)
                    for a_con in listAll_pls:
                        o_src_pls,o_targ_pls = a_con[1],a_con[0]
                        #o_src_pls_nm_f = src_pls.name()
                        o_src_nd = o_src_pls.node()
                        if o_src_nd != o_ctrl: continue
                        o_src_pls_nm = ".".join(o_src_pls.name().split('.')[1:])
                        n_src_pls = n_ctrl.attr(o_src_pls_nm)
                        o_src_pls //  o_targ_pls
                        n_src_pls >> o_targ_pls


