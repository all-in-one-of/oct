#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Ppl_checkT_asset
__author__ = zhangben 
__mtime__ = 2019/4/1 : 18:24
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import shutil
# from PySide import QtGui,QtCore,QtUiTools
from PyQt4 import QtGui,QtCore,uic
import logging
import maya.OpenMayaUI as mui
import inspect,sys,os,copy,re
import maya.mel as mel
import maya.cmds as mc
import pymel.core as pm
from types import FunctionType
import sip
from ..utility import Kits
reload(Kits)
from ..past import sk_checkTools,sk_sceneTools,sk_smoothSet
reload(sk_checkTools)
reload(sk_sceneTools)
reload(sk_smoothSet)
import Ppl_pubCheck as ppc
reload(ppc)
import Ppl_scInfo as psinf
reload(psinf)
from ..Minor import SetSmoothLevelTools_ui,Ppl_rnmtools_auto,Ppl_check
reload(SetSmoothLevelTools_ui)
reload(Ppl_rnmtools_auto)
reload(Ppl_check)
from ..Major import Ppl_scInfo
reload(Ppl_scInfo)
SCRIPT_LOC = os.path.split(__file__)[0]
PROJ_DIR = os.getenv('OCTV_PROJECTS')
class Ppl_assetT_main(QtGui.QMainWindow):
    def __init__(self):#load ui  show it
        """
        前期检测整理工具集
        """
        ppl_UI = os.path.join(Kits.Kits.get_dir(SCRIPT_LOC, 2), r'media\ppl_assetTool.ui')
        # MayaMain = shiboken.wrapInstance(long(mui.MQtUtil.mainWindow()), QtGui.QWidget)
        MayaMain = sip.wrapinstance(long(mui.MQtUtil.mainWindow()), QtGui.QWidget)
        super(Ppl_assetT_main,self).__init__(MayaMain)
        #=======program MEL path ====================
        self.mel_dir = os.path.join(Kits.Kits.get_dir(SCRIPT_LOC, 1),'MEL')
        #=======relative modules======================
        self.skchk = sk_checkTools.sk_checkTools()
        self.sksct = sk_sceneTools.sk_sceneTools()
        self.sksmth = sk_smoothSet.sk_smoothSet()
        self.scInfo = Ppl_scInfo.Ppl_scInfo()
        self.pplchk = Ppl_check.Ppl_check()
        # main window load/settings
        self.ui = self.loadUiWidget(ppl_UI,self)
        self.ui.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
        self.ui.destroyed.connect(self.cmd_onExitCode)
        self.ui.move(200,400)
        self.buttonsList = [ea_bt.objectName() for ea_bt in self.ui.findChildren(QtGui.QPushButton) if re.search('_bt[_]*',str(ea_bt.objectName()))]
        # self.cbxDict = [ea_chbx.objectName() for ea_chbx in self.ui.findChildren(QtGui.QCheckBox) if re.search('_chk',str(ea_chbx.objectName()))]
        self.cbxDict = dict([[ea_chbx.objectName(),ea_chbx] for ea_chbx in self.ui.findChildren(QtGui.QCheckBox) if re.search('_cbx',str(ea_chbx.objectName())) and not ea_chbx.setChecked(True)])
        self.ui.plsAbcAttr_tidy_bt.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.plsAbcAttr_tidy_bt.customContextMenuRequested.connect(self.addAttrPopMenu)
        self.ui.show()

        self.makeConnections()
        # === about porjects information
        self.k = Kits.Kits()
        ALL_PROJ_ABBRS = os.listdir(PROJ_DIR)
        sc_shn = os.path.basename(pm.sceneName())
        self.proj_abbr = re.search("^[^_]+", os.path.splitext(sc_shn)[0]).group() if sc_shn else None

        #some attribute
        self._addAttr = 'add'
        self.topGrpDic = {'tx':'CHR','rg':'CHR','mo':'MODEL'}
        self.iify_infor = []
        # self.attr_op = {True: 'add', None: 'delete'}

        self.addToolTips()
        self.setLabelClr()
        # self.setAllChkbxOn()
    def makeConnections(self): # connect buttons to fucntions
        for each_bt in self.buttonsList:
            _fuction = None
            if re.search("_regchk_bt",each_bt):
                fndbtn = self.ui.findChildren(QtGui.QPushButton, each_bt)[0] # find button object
                fndbtn.clicked.connect(lambda state, x=each_bt:self.call_pplchk(x))
            else:
                _fuction = getattr(self, "cmd_{}".format(each_bt)) if "cmd_{}".format(each_bt) in self.__class__.__dict__ else self._somFunc
                self.ui.findChildren(QtGui.QPushButton, each_bt)[0].clicked.connect(_fuction)
    def addToolTips(self): # add tools tip for each button
        for each_bt in self.buttonsList:
            fndbtn = self.ui.findChildren(QtGui.QPushButton, each_bt)[0]  # find button object
            tipStr = None
            if re.search("_regchk_bt", each_bt):
                infor_spl = each_bt.split("_regchk_bt")
                func_name = 'autoRun' if infor_spl[0] == 'all' else infor_spl[0]

                exCmd = "tipStr = self.pplchk.{}.__doc__".format(func_name)
                exec (exCmd)
                if tipStr:  fndbtn.setToolTip(u"{}".format(tipStr))
            # elif re.search("(_tidy_bt)|(_chk_bt)",each_bt):
            else:
                # print each_bt
                func_name = "cmd_{}".format(each_bt)
                exCmd = "tipStr = self.{}.__doc__".format(func_name)
                try:
                    exec(exCmd)
                except Exception,e:
                    print e.message
                if tipStr: fndbtn.setToolTip(u"{}".format(tipStr))
    # def setAllChkbxOn(self):
    #     for each_cbxnm in self.cbxDict:
    #         each_cbx = self.ui.findChildren(QtGui.QCheckBox, each_cbxnm)[0]
    #         each_cbx.setChecked(True)
    def setLabelClr(self):# 设置button  letter color  ,this is a obsolete function
        clrCode = "rgb(71,220,145)"
        for each_bt in self.buttonsList:
            _fuction = None
            if re.search("indiv[\w]+_regchk_bt",each_bt,re.I):
                fndbtn = self.ui.findChildren(QtGui.QPushButton, each_bt)[0]  # find button object
                labStr =  ur"{}".format(str(fndbtn.toolTip()))
                # labStr_n = u"<span style = \"font-size:12pt;color:#49d5d1;\"> {} </span>".format(labStr)
                labStr_n = u"<pre><span style = \"color:black\"> {} </span></pre>".format(labStr)  # richtext  remain linesep etc,need add <pre> </pre>
                # print labStr_n
                # fndbtn.setText(labStr_n)
                # fndbtn.setStyleSheet("""QToolTip{
                #                     background-color:black
                #                     color：rgb(50,250,255)
                #                     border:black solid 1px
                #                     }""")
                # fndbtn.setStyleSheet("color: {};QToolTip{border:0px solid black;background-color: black}".format(clrCode))
                fndbtn.setStyleSheet("color: {}".format(clrCode))
                # fndbtn.setStyleSheet("")
                fndbtn.setToolTip(labStr_n)
        self.ui.tiplab.setStyleSheet("color: {}".format(clrCode))
    def addAttrPopMenu(self,point):# add  attribute popmenu config
        self.popMenu = QtGui.QMenu(self.ui)
        ac_add = QtGui.QAction('add',self.ui)
        ac_add.setObjectName('act_add')
        # ac_add.triggered.connect(lambda x=True:self.cmd_addAttrPopMenu(x))
        self.popMenu.addAction(ac_add)
        ac_del = QtGui.QAction('delete',self.ui)
        ac_del.setObjectName('act_delete')
        # ac_del.triggered.connect(lambda  x= None:self.cmd_addAttrPopMenu(x))
        self.popMenu.addAction(ac_del)
        self.popMenu.triggered[QtGui.QAction].connect(self.cmd_addAttrPopMenu)
        self.popMenu.exec_(self.ui.plsAbcAttr_tidy_bt.mapToGlobal(point))
    def cmd_addAttrPopMenu(self,q):# add attribute popmumen connect fuction
        op = re.sub('act_',"",str(q.objectName()))
        bluetx = "<span> <font color=#55ff00> {}</font> </span>".format(op)
        self.ui.opLab.setText(bluetx)
        # self._addAttr = bool(1 - self._addAttr)
        self._addAttr = op
    #=========↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   connected functions ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓========================================
    def cmd_onExitCode(self):
        sys.stdout.write("You closed the demo ui !!\n")
    def _somFunc(self):
        print("some function return what a F~~")
    #  call tools buttons commands =================================
    def cmd_rnmT_bt(self):#重命名工具
        """
        >>一款比较强大的重命名工具点开来瞧瞧~~
        """
        src_mel = os.path.abspath(os.path.join(self.mel_dir, 'Quick_rename_tool.mel'))
        src_mel = re.sub(r'\\','/',src_mel)
        mel.eval("source \"{}\"".format(src_mel))
        mel.eval("Quick_rename_tool()")

    def cmd_alterTxsPrf_bt(self):#修改贴图前缀匹配当前项目
        u"""
        >>  根据maya文件名获取项目缩写，修改所有贴图前缀为项目缩写
                         同时修改 - 空格 等不规范字符
        """
        mod = {'RENAME OLD':'rn','COPIED FOR NEW':'cp'}
        result = mc.promptDialog(title='Texture Prefix',message='Enter Prefix:',button=['COPIED FOR NEW','RENAME OLD','Cancel'],defaultButton='OK',
                                 cancelButton='Cancel',
                                 dismissString='Cancel',text = self.proj_abbr)
        if result in mod: self.proj_abbr = mc.promptDialog(query=True, text=True)
        else:return
        ALL_PROJ_ABBRS = os.listdir(PROJ_DIR)
        alterFs = pm.selected(type='file')
        if not alterFs: alterFs = pm.ls(type='file')
        cur_proj_wsp = pm.workspace(fn=True, q=True)
        cur_src_dir = "{}/sourceimages/".format(cur_proj_wsp)
        all_cnt = len(alterFs)
        renmed_txs_cnt = 0
        prg_num = (renmed_txs_cnt+1 / float(all_cnt)) * 100
        cpProgressWin = mc.progressWindow(title="Add Prefix", progress=prg_num, status="PROGRESS : {}%".format(prg_num), isInterruptable=True,
                                          min=0, max=100)
        res_error_str = ""
        modifiedTex = {}
        for eaf in alterFs:
            get_txfpths = []
            txfpth_01 = eaf.attr('fileTextureName').get()
            if txfpth_01.startswith("${"):
                txfpth_01 = self.k.txAbsPath(txfpth_01).values()[0]
            get_txfpths.append(txfpth_01)
            if_tx_file = self.get_ArTx(txfpth_01)
            if if_tx_file and os.path.isfile(if_tx_file): get_txfpths.append(if_tx_file)
            if eaf.attr('uvTilingMode').get() == 3 or eaf.attr('useFrameExtension').get():
                seqs = self.k.findTxSeqs(txfpth_01)
                if isinstance(seqs, str):
                    res_error_str += u'{0}>>>请检查 file节点 {1:<32} 的序列贴图是否存在或命名是否正确：\t{2} {0}'.format(os.linesep, eaf.nodeName(),txfpth_01)
                else:
                    get_txfpths.extend(seqs[1:])
                if if_tx_file and os.path.isfile(if_tx_file):
                    tx_seqs = self.k.findTxSeqs(if_tx_file)
                    if isinstance(tx_seqs, str):
                        res_error_str += u'{0}>>>请检查 file节点 {1:<32} 的序列贴图是否存在或命名是否正确：\t{2} {0}'.format(os.linesep, eaf.nodeName(), if_tx_file)
                    else:
                        get_txfpths.extend(tx_seqs[1:])
            print "node name {}".format(eaf.nodeName())
            for txfpth in get_txfpths:
                print " textrue file : {} " .format(txfpth)
                set_attr_value = True
                if get_txfpths.index(txfpth): set_attr_value = False
                txf_nm = os.path.basename(txfpth)
                txf_prj_abbr = re.search("^[^_]+", txf_nm).group()
                # if txf_prj_abbr == self.proj_abbr: continueW
                txf_dir = re.sub(txf_nm, '', txfpth)

                if not txf_dir == cur_src_dir and mod[result]=='cp':
                    txf_dir = cur_src_dir
                new_txf_nm = None
                if txf_prj_abbr in ALL_PROJ_ABBRS:
                    txf_nm_norm = self.k.normalizeTxNm(txf_nm)
                    new_txf_nm = re.sub(txf_prj_abbr, self.proj_abbr, txf_nm_norm)
                else :
                    new_txf_nm = '{}_{}'.format(self.proj_abbr,self.k.normalizeTxNm(txf_nm))
                new_txf_pth = "{}{}".format(txf_dir, new_txf_nm)
                if txfpth in modifiedTex:
                    eaf.attr('fileTextureName').set(new_txf_pth)
                    continue
                if self.k.filetest(txfpth,new_txf_pth):
                    # print(">>>--{}{}>>>---{}".format(txfpth,os.linesep,new_txf_pth))
                    if mod[result] =='cp':
                        try:
                            shutil.copy2(txfpth,new_txf_pth)
                            if set_attr_value:
                                eaf.attr('fileTextureName').set(new_txf_pth)
                            modifiedTex[txfpth] = new_txf_pth
                        except:
                            print("sorce image: {1}{0}target image: {2}".format(os.linesep, txfpth, new_txf_pth))
                            mc.progressWindow(cpProgressWin, endProgress=1)
                            res_error_str += u'{0}>>>请检查 file节点 {1:<32} 的贴图是否存在或命名是否正确：\t{2} >>>> new name : {3} {0}'.format(os.linesep,eaf.nodeName(),txfpth,new_txf_pth)

                    elif mod[result] =='rn':
                        try:
                            eaf.attr('fileTextureName').set("")

                            os.rename(txfpth,new_txf_pth)
                            if set_attr_value:
                                eaf.attr('fileTextureName').set(new_txf_pth)
                            modifiedTex[txfpth] = new_txf_pth
                        except Exception,e:
                            print e.message
                            res_error_str += u'{0}>>>请检查 file节点 {1:<32} 的贴图 路径的写入权限:{2:<32} ：\t{}{0}'.format(os.linesep, eaf.nodeName(), txf_dir)
                            mc.progressWindow(cpProgressWin, endProgress=1)
                    renmed_txs_cnt +=1
                    self.ref_pr_bar(renmed_txs_cnt+1,all_cnt,cpProgressWin)
                    # print(u">>>请检查 当前工程的sourceimages文件夹 是否存在并且有写入权限")
                else:
                    if os.path.exists(new_txf_pth):
                        if set_attr_value: eaf.attr('fileTextureName').set(new_txf_pth)
                        renmed_txs_cnt += 1
                        self.ref_pr_bar(renmed_txs_cnt + 1, all_cnt, cpProgressWin)
        mc.progressWindow(cpProgressWin, endProgress=1)
        print(u">>> 本次操作修改了 {} 张贴图前缀 匹配了当前文件 项目 缩写 : {} ".format(renmed_txs_cnt,self.proj_abbr))
        if res_error_str:
            print (res_error_str)
            mc.warning(res_error_str)
    def cmd_smoothSetT_bt(self): # smooth set 设置工具
        u"""
        >>smooth 级别设置工具
        """
        # global appName
        MayaMainWin = sip.wrapinstance(long(mui.MQtUtil.mainWindow()), QtGui.QWidget)
        findWin = MayaMainWin.findChild(QtGui.QWidget, 'SetSmoothLevelWin')
        if findWin: findWin.close()
        SetSmoothLevelTools_ui.main_my()
    #  call fuction buttons commands ================================
    # 根据名字选择
    def cmd_selByNm_bt(self):
        u"""
        >>根据名字选择
        """
        srcStr = self.ui.pick_sel_l.text()
        ls_objs = pm.ls(str(srcStr))
        pm.select(ls_objs)
    # 自动重命名
    def cmd_nm_tidy_bt(self):
        u"""
        >>规范化命名 : mo 文件： outliner 创建 MODEL组|MSH_all|MSH_geo/MSH_outfit
                               所有子级别节点，添加 规范化的前缀 后缀 根据 模型当前名字 自动规范化命名
                      rg 文件： outliner 还会创建  RIG   DEFORMER  FX 组，

                     请 各位artist 整理相应节点到相应组下
        """
        Ppl_rnmtools_auto.Pre_regNaming()
    # 添加后缀 _
    def cmd_suff_tidy_bt(self):
        u"""
        >>添加后缀 _
        """
        self.skchk.checkRenameMSHPosfix()
    # 检查 namespace
    def cmd_chkNmsp(self):
        u"""
        >>检查 namespace
        """
        self.skchk.checkModelDetailsWarning("nsCheck")
    # namespace工具
    def cmd_nmsp_tidy_bt(self):
        u"""
        >>namespace工具
        """
        src_mel = os.path.abspath(os.path.join(self.mel_dir,'common_namespaceTools.mel'))
        src_mel = re.sub(r'\\', '/', src_mel)
        mel.eval("source \"{}\"".format(src_mel))
        mel.eval("common_namespaceTools")
    # 清理多余的显示层
    def cmd_dsly_tidy_bt(self):
        u"""
        >>清理多余的显示层
        """
        self.sksct.checkCleanDisplayLayers()
        print("DisplayLayer Tidied!!!")
    # delete empty group
    def cmd_emgrp_tidy_bt(self):
        u"""
        >>删除空组 mo，tx 文件 清楚所有空组
        """
        emptGrp = None
        if self.scInfo.section == 'mo':
            emptGrp = [n for n in pm.ls(type='transform') if not n.getChildren(ad=True)]
        else:
            emptGrp = [n for n in pm.PyNode('MODEL').listRelatives(ad=True, type='transform') if not n.getChildren(ad=True)]
        pm.delete(emptGrp)
    #添加 ct_an 标记 标记物体输出动画
    def cmd_anlab_tidy_bt(self):
        u"""
        >>添加 ct_an 标记 标记物体输出动画
        """
        self.skchk.checkCTANSignAdd()
    def cmd_set_tidy_bt(self):# 自动标记set组
        u"""
        自动标记set组
        """
        self.sksct.checkCacheSetAdd()
        self.sksct.checkTransAnimSetAdd()
        self.sksct.sk_sceneCacheAnimSetConfig("Cache", "ZM")
        self.sksct.sk_sceneCacheAnimSetConfig("Anim", "ZM")
    def cmd_plsAbcAttr_tidy_bt(self):
        u"""
        >>添加或删除alembic属性 ：参与渲染以及毛发的生长体模型，
                              需要输出缓存必须添加alembic
                              并且这些模型只能在MODEL组或FX组下
        """

        # bluetx.append("add")
        # bluetx.append("</span>")
        # addStr = QtCore.QString("abc")
        # font = QtGui.QFont()
        # font
        # addStr.setStyleSheet("color:red")
        self.customAttr('alembic',self._addAttr)

    def cmd_rmun_tidy_bt(self):
        u"""
        >>清除unknown,unused 节点，海龟渲染等相关节点
        
        """
        pchk = ppc.Ppl_pubCheck()
        pchk.checkDonotNodeCleanBase()
    #===================check panel commands=======================================
    def cmd_ref_chk_bt(self):#检查参考
        u"""
        >>检查参考
        """
        self.skchk.checkModelDetailsWarning("refCheck")
    def cmd_nmsp_chk_bt(self):#检查namespace
        u"""
        >>#检查namespace
        """
        self.skchk.checkModelDetailsWarning("nsCheck")
    def cmd_nm_chk_bt(self):#检查命名
        u"""
        >>检查命名
        """
        self.skchk.checkModelDetailsWarning("MSHCheck")
    def cmd_fnm_chk_bt(self):#检查面数
        u"""
        >>检查面数
        """
        self.skchk.checkModelDetailsWarning("faceCheck")
    def cmd_ins_chk_bt(self):#检查instance
        u"""
        >>检查instance
        """
        self.skchk.checkModelDetailsWarning("insCheck")
    def cmd_sm_chk_bt(self):  # 检查smooth
        u"""
        >>检查smooth
        """
        self.skchk.checkModelDetailsWarning("moothCheck")
    def cmd_flg_chk_bt(self):  # 检测属性标记
        u"""
        >>检测属性标记
        """
        self.skchk.checkModelDetailsWarning("signCheck")
    def cmd_tautonymy_chk_bt(self):  # 检查 transform 同名
        u"""
        >>检查 transform 同名
        """
        self.skchk.checkModelDetailsWarning("sameTransformCheck")
    def cmd_tautonymyShp_chk_bt(self): # 检查 shape同名
        u"""
        >>检查 shape同名
        """
        self.skchk.checkModelDetailsWarning("sameShapeCheck")
    def cmd_tautonymyMsh_chk_bt(self): # 检查 mesh 同名
        u"""
        >>检查 mesh 同名
        """
        self.skchk.checkModelDetailsWarning("sameShapeNodeCheck")
    def cmd_smthSet_chk_bt(self): # 检查smooth set
        self.skchk.checkModelDetailsWarning("smoothSet")
    def cmd_prxTr_chk_bt(self): # 检查proxy 位移
        u"""
        >>检查proxy 位移
        """
        self.skchk.checkModelDetailsWarning("proxyInfo")
    def cmd_rndSta_chk_bt(self):#检查 render state
        u"""
        >>检查 render state
        """
        self.skchk.checkModelDetailsWarning("renderState")
    def cmd_selSmth_tidy_bt(self):#选取物体smooth
        u"""
        >>选取物体smooth
        """
        self.sksmth.smoothSetDoSmooth(useSmoothSet = 1,selMode = 1)
    def cmd_txsnm_chk_bt(self):#check 贴图命名
        u"""
        >>check 贴图命名 :  项目缩写为 前缀， 使用 数字 0-9 字母a-zA-Z 下划线 _  点.
                           贴图文件命名及路径中 回避 中文
                           贴图文件命名及路径中 不能有  空格 - () 等 特殊字符
        """
        chk_labels = {'noExists': u'贴图不存在', 'iffyName': u'贴图命名 应由 (字母/数字/_/.) 组成', 'seqIffyName': u'序列贴图序号存在异常 正常为 ***.0001.jpg', 'prefIffyName':
            u'贴图前缀与当前任务不匹配'}
        res = self.chk_txf_name()
        if not res: return
        olnps = [ea for ea in pm.lsUI(panels=True) if ea.type() == 'ToutlinerEditor']
        if olnps:
            mc.outlinerEditor(olnps[0].name(), showSetMembers=True, e=True)
        res_str = u'>>>请检查列出的file节点 贴图命名 所描述的错误{}'.format(os.linesep)
        ck_cnt = 0
        res_total_sets = None
        if pm.objExists('Check_Error_information_Sets'):
            res_total_sets = pm.PyNode('Check_Error_information_Sets')
            [pm.delete(ea_sets) for ea_sets in res_total_sets.listConnections()]
        res_total_sets = pm.sets(name='Check_Error_information_Sets',em=True)
        for ea_ck_lb in chk_labels:
            if res[ea_ck_lb]:
                res_sets = pm.sets(name="CheckRes_{}".format(ea_ck_lb))
                res_total_sets.add(res_sets.name())
                res_str += u'\t{}{}'.format(chk_labels[ea_ck_lb], os.linesep)
                for ea_fn in res[ea_ck_lb]:
                    res_sets.add(ea_fn.name())
                    res_str += u"\t\t>>>File Node >> {:<32}\t>>>Texture File>>  {:<120}\t 异常部分: {}{}".format(ea_fn.name(), res[ea_ck_lb][
                        ea_fn].keys()[
                        0],res[ea_ck_lb][ea_fn].values()[0], os.linesep)
                ck_cnt +=1
        if ck_cnt: print res_str
        else: print(u">>>没有贴图节点被check")
    #add to asset file regularity check
    def call_pplchk(self,infor):
        # print("Call Pipeline Check.........")
        # print btn.objectName()
        infor_spl = str(infor).split("_regchk_bt")
        func_name = infor_spl[0]
        if infor_spl[1]:
            argvs_lst = []
            for n in infor_spl[1:][0].split('_'):
                if not n:continue
                if re.search("^[\d]+$",n): argvs_lst.append(n)
                else:argvs_lst.append("\"{}\"".format(n))
            argvs = ",".join(argvs_lst)
            cmd = "self.pplchk.autoRun(\'{},{}\')".format(func_name,argvs)
            print cmd
            exec(cmd)
        else:
            self.pplchk.autoRun(func_name)
    def cmd_allReg_chk_bt(self):
        u"""
        >>执行检查   被勾选的项
        
        """
        allFncs = dict([[x,y] for x,y in self.__class__.__dict__.items()])
        # for x, y in allFncs:
        #     if re.search('_check_all_\d', x) and type(y) == FunctionType and cbxs["{}_regchk_chk".format(x)].checkState() == 2:
        #         # print x
        #         chkAll_prc.append(x)
        #     elif re.search('_check_indiv_', x) and type(y) == FunctionType and cbxs["{}_regchk_chk".format(x)].checkState() == 2:
        #         chkIndiv_prc.append(x)
        # chkAll_prc.sort()
        # self.pplchk.autoRun('all')
        # print self.cbxDict
        # print allFncs
        for ecbx in self.cbxDict:
            # print(self.cbxDict[ecbx].checkState())
            if self.cbxDict[ecbx].checkState()==2 and not re.search("_regchk_",ecbx):
                fnc_nm = "cmd_{}".format(re.sub("_cbx$","_bt",str(ecbx)))
                if fnc_nm in allFncs:
                    exc_cmd = "self.{}()".format(fnc_nm)
                    exec(exc_cmd)


        # allcbx = dict([[str(eacbx.objectName()), eacbx] for eacbx in .findChildren(self.ui.QCheckBox) if re.search("_chk$", eacbx.objectName())])
        # allcbx = dict(self.cbxDict)

    # def cmd_all_1_grpName_regchk_bt(self):
    #     fram = inspect.currentframe()
    #     infor = inspect.getframeinfo(fram).function
    #     func_name = re.sub('cmd_','_check_',infor)
    #     self.pplchk.autoRun(func_name)
    #     # self.pplchk._check_all_1_grpName()
    # def cmd_unfrz_regchk_bt(self):
    #     fram = inspect.currentframe()
    #     infor = inspect.getframeinfo(fram).function
    #     func_name = re.sub('cmd_', '_check_', infor)
    #     self.pplchk.autoRun(func_name)
    def cmd_all_chk_bt(self):
        print("\n".join(self.buttonsList))

    # smoothSetDoSmooth(useSmoothSet = 1,selMode = 1)

    #=========↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑    connected functions  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑========================================

    def loadUiWidget(self,uifilename, parent=None): # load ui file
        """import ui file"""
        # loader = QtUiTools.QUiLoader()
        # uifile = QtCore.QFile(uifilename)
        # uifile.open(QtCore.QFile.ReadOnly)
        # ui = loader.load(uifile, parent)
        # uifile.close()
        uic.properties.logger.setLevel(logging.WARNING)
        uic.uiparser.logger.setLevel(logging.WARNING)
        ui = uic.loadUi(uifilename,parent)
        return ui
    def nonUniqueObjects(self): # a function list all taotunymy object
        all_nds = pm.ls()
        non_uniques = {}
        temp_nm_dic = {}
        for ea_nd in all_nds:
            ndTyp = ea_nd.type()
            ndShtNm = ea_nd.name()
            ndLngNm = ea_nd.longName()
            if ndShtNm not in temp_nm_dic:
                temp_nm_dic[ndShtNm] = {ndTyp: [ea_nd]}
            else:
                if ndShtNm not in non_uniques:
                    cp_date = copy.deepcopy(temp_nm_dic[ndShtNm])
                    non_uniques[ndShtNm] = cp_date
                    if ndTyp in non_uniques[ndShtNm]:
                        non_uniques[ndShtNm].append(ea_nd)
                    else:
                        non_uniques[ndShtNm][ndTyp] = [ea_nd]
                else:
                    if ndTyp in non_uniques[ndShtNm]:
                        non_uniques[ndShtNm].append(ea_nd)
                    else:
                        non_uniques[ndShtNm][ndTyp] = [ea_nd]

    def chk_txf_name(self,proj_abbr=None):  # texture file name check
        u"""
        >> 检测贴图命名
        :param proj_abbr:
        
        """
        if not proj_abbr:  # project abbreviation
            fileName_shn = mc.file(q=True, sn=True, shn=True)
            proj_abbr = re.search('^[^_]*', fileName_shn).group()
            if proj_abbr == fileName_shn: proj_abbr == None
        lsfils = pm.ls(type='file')
        checkRes = {'noExists': {}, 'iffyName': {}, 'seqIffyName': {}, 'prefIffyName': {}}
        hasIffy = None
        for eaf in lsfils:
            txfpth = eaf.attr('fileTextureName').get()
            useVAR = None
            txfpth_var = None
            if txfpth.startswith("${"):
                re_VAR = re.compile("[^${}]+",re.I)
                useVAR = re_VAR.search(txfpth).group()
                if os.getenv(useVAR):
                    txfpth_var = txfpth
                    txfpth = re.sub("^[$]+{\w+}", os.getenv(useVAR), txfpth, re.I)

            txf_nm = os.path.basename(txfpth)
            txf_prf = re.search("^[^_]+", txf_nm).group()
            # check texture file prefix match project abbreviation
            if proj_abbr and proj_abbr != txf_prf:
                hasIffy = True
                checkRes['prefIffyName'][eaf] = {txfpth:txf_prf}
            # check file whether exists
            if not os.path.isfile(txfpth):
                hasIffy = True
                checkRes['noExists'][eaf] = {txfpth:txfpth_var}
            # check file name whether
            re_iffynm = re.compile("[^\w_/{}:.]+".format(os.sep), re.I)
            ckres = re_iffynm.findall(txfpth)
            if len(ckres):
                hasIffy = True
                checkRes['iffyName'][eaf] = {txfpth: ckres}
            # check sequence texture
            if eaf.attr('useFrameExtension').get() or eaf.attr('uvTilingMode').get() == 3:
                tx_spl = os.path.splitext(txf_nm)
                re_seq = re.compile('[._]+\d+$', re.I)
                if not re_seq.search(tx_spl[0]):
                    re_seq_comp = re.compile('[^_.]+$', re.I)
                    if re_seq_comp.search(tx_spl[0]):
                        hasIffy = True
                        checkRes['seqIffyName'][eaf] = {txfpth: re_seq_comp.findall(tx_spl[0])}
                    else:
                        hasIffy = True
                        checkRes['seqIffyName'][eaf] = {txfpth: [tx_spl[0]]}
                else:
                    match_seq = re_seq.search(tx_spl[0]).group()
                    print match_seq
                    re_illegal_seq = re.compile('[._]')
                    redundant_sep = re_illegal_seq.findall(match_seq)[:-1]
                    if redundant_sep:
                        hasIffy = True
                        checkRes['seqIffyName'][eaf] = {txfpth: redundant_sep}

        if hasIffy : return checkRes
        else: return None

    def ref_pr_bar(self,cur_cp_num, exec_count, cpProgressWin):# 更新进度条
        prg_num_tmp = (cur_cp_num / float(exec_count)) * 100
        mc.progressWindow(cpProgressWin, e=True, progress=prg_num_tmp, status="Copy perform: {}%".format(prg_num_tmp))

    def get_ArTx(self,src):#把arnold tx文件加入copy列表
        if not mc.getAttr("defaultRenderGlobals.currentRenderer") =="arnold": return None
        fileSpl = os.path.splitext(src)
        txf_pth = fileSpl[0] + u'.tx'
        if txf_pth == src:return None
        else: return txf_pth

    def customAttr(self,attrName='GD', operation='add',attrV=1):
        SEL_OBJS = pm.selected()
        OBJS = []
        for ea_sel in SEL_OBJS:
            for ea in ea_sel.listRelatives(ad=True, c=True, type='mesh', ni=True):
                trns = ea.getParent()
                if ea not in OBJS:
                    OBJS.append(ea)
                    if operation == 'add':
                        if trns.hasAttr(attrName):
                            pm.deleteAttr(trns, at=attrName)
                        pm.addAttr(trns, ln=attrName, at='double', dv=1, k=1)
                        trns.attr(attrName).set(attrV)
                    elif operation == 'delete':
                        if trns.hasAttr(attrName): pm.deleteAttr(trns, at=attrName)
            for ea in ea_sel.listRelatives(ad=True,c=True,type='light',ni=True):
                if ea not in OBJS:
                    OBJS.append(ea)
                    trns_l = ea.getParent()
                    if operation == 'add':
                        if trns_l.hasAttr(attrName):
                            pm.deleteAttr(trns_l, at=attrName)
                        pm.addAttr(trns_l, ln=attrName, at='double', dv=1, k=1)
                        trns.attr(attrName).set(attrV)
                    elif operation == 'delete':
                        if trns_l.hasAttr(attrName): pm.deleteAttr(trns_l, at=attrName)




# def call_it():
#     if not mc.window('ppl_asset_win',exists=True):
#         win = Ppl_assetT_main()
#     else:
#         sys.stdout.write("Tools is already open!\n")

    #win.showUI()