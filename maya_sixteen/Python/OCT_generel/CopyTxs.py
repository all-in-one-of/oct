#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = CopyTexture_exec_zb
__author__ = zhangben
__mtime__ = 2019/4/24 : 15:49
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import os,re,sys,subprocess,shlex,time
from OCT_Pipeline.scripts.utility import Kits
reload(Kits)
import maya.mel as mel
import maya.cmds as mc
import string
class CopyTxs(object):
    """
    重构copy texture file 可接受mel 传递的参数  也可以 直接传 参数调用
    """
    def __init__(self,copyMode,var_fileNods,var_copyTxsList,var_destDir,my_f_nm):
        """
        将接受从mel 传递过来的mel 变量名字作为参数，程序 在mel中执行。
        ##$rs = `zwSysFilePartial "fcopy" $REC_TXS_BY_NODE $destFolder 0 $runBatfile`;
        :param var_fileNods: '$ALL_FILE_NODES'  --- 所有的file 节点
        :param var_copyTxsList: $REC_TXS_BY_NODE[]; --- 按节点方式 记录 ：每个node 关联的贴图们 写在一起 为一条 fastCopy 命令的参数
        :param var_destDir:  目标文件夹
        :param my_f_nm:  当前maya文件的名字 或者 要通过CPAU 执行的bat 文件的路径
        :return:
        """
        print("{}ENTER NEW COPY MODE -------------------------------------".format(os.linesep))
        # ==========返回值:
        self.resultStr = None
        # === process argumets
        self.allFileNodes = [re.sub("\"", "", ea_item) for ea_item in mel.eval("global string {0}[];string $tmp_list[] = {0}".format(var_fileNods))] if isinstance(var_fileNods,str) else var_fileNods
        # for ea in self.allFileNodes: print ea
        self.recTxsList = [re.sub("\"", "", ea_item) for ea_item in mel.eval("global string {0}[];string $tmp_list2[] = {0}".format(var_copyTxsList))] if isinstance(var_copyTxsList,str) else var_copyTxsList
        # filesLst_read = mel.eval("global string {0}[];string $tmp_list2[] = {0}".format(var_copyTxsList))
        # for ea_item in filesLst_read:
        #     print ea_item
        self.in_txs_num = len(self.recTxsList)
        if not self.in_txs_num:
            self.resultStr = "{0}>>> No Textrue need copy???!!!{0}".format(os.linesep)
            print(self.resultStr)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # print(len(self.recTxsList))
        # for ea in self.recTxsList:
        #     print ea
        #     print("~~~~~~~~~~~~~~~~~~~~~~")
        # raise Exception("TDTEst0")
        self.destDir = mel.eval("string $tmp_str = {}".format(var_destDir)) if var_destDir.startswith('$') else var_destDir
        self.my_f_nm = mel.eval("string $tmp_str = {}".format(my_f_nm)) if my_f_nm.startswith('$') else os.path.splitext(my_f_nm)[0]
        self.copyMode = copyMode
        # === parse and declare variables
        self.OCTV_TECH = os.getenv('OCTV_TECH') if os.getenv('COTV_TEHC') else '//octvision.com/CG/Tech'
        self.invokepath = '{}/bin/CPAU.exe -u octvision\supermaya -p supermaya -ex '.format(self.OCTV_TECH)
        self.k = Kits.Kits()
        sysTmpDir = os.getenv("TEMP")
        #执行的CPAY 要运行的bat file
        self.ex_batFile = os.path.abspath(os.path.join(sysTmpDir,'{}.bat'.format(self.my_f_nm)))
        #记录bat 执行进度的 计数文件
        self.rec_cptimes_f = os.path.abspath(os.path.join(os.path.dirname(self.ex_batFile), "{}.recf".format(os.path.splitext(os.path.basename(self.ex_batFile))[0])))
        print("=========rec copy time file======================")
        print self.rec_cptimes_f
        #程序要调用的 系统命令 CAPU.exe  user : supermaya   execute  bat file
        self.exec_cmd = "{}{}".format(self.invokepath, self.ex_batFile)
        #获取当前系统的映射驱动器 盘符及路径
        self.mapDrive = self.k.findYourMapDrive()
        #要写入bat文件的 单行命令 template 目前只有fastcopy 模式， 以后可以添加其他方法，置入对应字典的 键与值
        wr_cmd_str_fcp = "{}\\bin\\FastCopy341\\FastCopy.exe /force_close /cmd=sync -nowarn -wait &COPY_FILES_PERGRP& /to=\"{}\"{}".format(os.path.abspath(self.OCTV_TECH),os.path.abspath(self.destDir),os.linesep)
        self.wr2f_cmd = {'fastCopy':wr_cmd_str_fcp}
        # 一些计数变量 用来监测copy 进程的完成情况
        self.colect_allTxs = []
        self.txs_info_dict = {}
        self.copy_count = 0
        self.tidy_lst = []
        self.exec_count = 0
        self.tidyFiles()

    def copytxs(self):#copy
        if not self.wr_bat(): return self.resultStr
        print("\n:::::RUN COMMAND::::\n")
        print("{}".format(self.exec_cmd))
        EXEC_COPY = self.k.run_subpr(self.exec_cmd)
        cp_stTm = time.ctime()
        cp_endTm = time.ctime()
        print(">>> START COPY AT :{}{}".format(cp_stTm, os.linesep))
        runingFcpy = self.k.monitoringPro('FastCopy.exe')
        new_fcp_pr = None
        copy_time = 1
        prg_num = (copy_time / float(self.exec_count)) * 100
        cpProgressWin = mc.progressWindow(title="Copy Textrues", progress=prg_num, status="Copy perform: {}%".format(prg_num), isInterruptable=True)
        while True:
            print"\t>>> ENTER MONITORING!!!!!!!!!!!!!!:{}{}".format(copy_time,os.linesep)
            cur_cp_num = self.check_copyTimes()
            if cur_cp_num != copy_time:
                self.ref_pr_bar(cur_cp_num, self.exec_count, cpProgressWin)
            runingFcpy_2 = self.k.monitoringPro('FastCopy.exe')
            if runingFcpy_2 == runingFcpy:
                if self.check_copyTimes() < self.exec_count + 1:
                    print(">>>.... THE SYSTEM WORK HARD AT COPYING......PLEASE WAIT  >>>>>>>>>>>\n")
                    time.sleep(3)
                    continue
            fcp_pr = self.k.monitoringPro('FastCopy.exe', 0, runingFcpy)
            if not fcp_pr:
                time.sleep(3)
                fcp_pr_2 = self.k.monitoringPro('FastCopy.exe', 0, runingFcpy)
                if not fcp_pr_2:
                    if self.check_copyTimes() == self.exec_count + 1:
                        print(">>> COPY OPERATION DONE!!!!!!\n")
                        cp_endTm = time.ctime()
                        print(">>> END TIME: {}{}".format(cp_endTm,os.linesep))
                        mc.progressWindow(cpProgressWin, endProgress=1)
                        break
                    else:
                        mc.warning("\t>>> COPY DONS'T PERFORM!!!PLEASE CHECK TEXTURES IN DESTINATION\n")
                        mc.progressWindow(cpProgressWin, endProgress=1)
                        mc.error("\t>>> COPYE TERMINATIONED AT TIME ::::: {}/{} \n".format(cur_cp_num, self.exec_count))
                        break
                else:
                    new_fcp_pr = fcp_pr_2
            else:
                if fcp_pr == new_fcp_pr:
                    if self.check_copyTimes() < self.exec_count + 1:
                        print(">>>.... THE SYSTEM WORK HARD AT COPYING......PLEASE WAIT  >>>>>>>>>>>\n")
                    else:
                        print(">>> COPY OPERATION DONE!!!!!!\n")
                        cp_endTm = time.ctime()
                        print(">>> END TIME: {}".format(cp_endTm))
                        mc.progressWindow(cpProgressWin, endProgress=1)
                        break
                else:
                    new_fcp_pr = fcp_pr
                    # print("COPY TIME IS::: {}\n".format(copy_time))
                copy_time = cur_cp_num
                    # time.sleep(1.5)
            # mc.progressWindow(cpProgressWin, endProgress=1)
        if self.copy_count < self.in_txs_num:
            self.resultStr = u">>>!!!ATTENTION PLEASE>>>!!!! 本次只更新了 [ {} ] 张贴图中的 [{}] 张贴图".format(self.in_txs_num,self.copy_count)
            print(self.resultStr)
        else:
            self.resultStr =u">>>共上传了 [{}]  张贴图".format(self.copy_count)
            print(self.resultStr)
        return self.resultStr
        # raise Exception('td test check')
    def tidyFiles(self,txNumPerGrp=20):#重新整理copy texutre files 每 txNumPerGrp 个贴图分为一组
        # print("L125: Tidy need copy texture {}  files".format(len(self.recTxsList)))
        iffy_txs = {}
        for ea in self.recTxsList:
            # ea= recTxsList[16] # ea= recTxsList[5]
            # print(">>>=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # print ea
            ea_spl = ea.split(' ')
            tmp_list = []
            idx = self.recTxsList.index(ea)
            f_nd = self.allFileNodes[idx]
            for ea_02 in ea_spl:
                endChar = None
                if re.search("\w\\\\\\\\", ea_02): endChar = re.sub("\\\\\\\\", "", re.search("\w\\\\\\\\", ea_02).group())
                new_ea_02 = re.sub("\w\\\\\\\\", "{}\\\\".format(endChar), ea_02)
                # print("\nCHECK texture: {} \n".format(new_ea_02))
                if not os.path.isfile(new_ea_02):
                    iffy_txs[iffy_txs] = new_ea_02
                    continue
                if new_ea_02 not in tmp_list: tmp_list.append(new_ea_02)
                if new_ea_02 not in self.colect_allTxs and self.filetest(new_ea_02, self.destDir): self.colect_allTxs.append(new_ea_02)
                else: print("\ttexture eixists on server : {}".format(new_ea_02))
                # print("\n==={}\n".format(new_ea_02))
                new_ea_02_txf = self.get_ArTx(new_ea_02)
                if new_ea_02_txf:
                    # print new_ea_02_txf
                    if new_ea_02_txf not in tmp_list: tmp_list.append(new_ea_02_txf)
                    if new_ea_02_txf not in self.colect_allTxs and self.filetest(new_ea_02_txf, self.destDir): self.colect_allTxs.append(new_ea_02_txf)
                    else: print("\ttexture eixists on server : {}".format(new_ea_02_txf))
            self.txs_info_dict[f_nd] = tmp_list
        if len(iffy_txs):
            erro_msg = u">>>请检查 下列file 节点 的 贴图命名{}".format(os.linesep)
            for ea in iffy_txs:
                ea_str = "{}{}{}".format(ea,iffy_txs[ea],os.linesep)
                erro_msg += ea_str
            erro_msg += u">>>程序列出贴 贴图命名可能存在异常 的file 节点 及 贴图名字，请打开脚本编辑器查看{}".format(os.linesep)
            mc.error(erro_msg)
        self.copy_count = len(self.colect_allTxs)
        self.tidy_lst = [self.colect_allTxs[x:x + txNumPerGrp] for x in range(0, self.copy_count, txNumPerGrp)]
        self.exec_count = len(self.tidy_lst)
        # raise Exception("TD CHECK")
    def get_ArTx(self,src):#把arnold tx文件加入copy列表
        if not mc.getAttr("defaultRenderGlobals.currentRenderer") =="arnold": return None
        fileSpl = os.path.splitext(src)
        return re.sub(fileSpl[-1],'.tx',src)

    def wr_bat(self):#生成相关文件
        # print("COPY EXECU COMMAND NUMBER : {}".format(self.exec_count))
        if not self.exec_count:
            print("{0}>>>ALL TEXTRUE FILES EXISTS! COPY UNNECESSARY{0}".format(os.linesep))
            self.resultStr = u">>>!!!ATTENTION PLEASE>>>!!!! 本次上传没有贴图更新！！！！！".format(os.linesep)
            return None
        print("rec_cptimes_f :::::{}".format(self.rec_cptimes_f))
        if os.path.isfile(self.rec_cptimes_f): os.remove(self.rec_cptimes_f)
        with open(self.rec_cptimes_f, 'w') as f_cptm:
            f_cptm.write('0')
        print("write counter DONE!!!!")
        if os.path.isfile(self.ex_batFile): os.remove(self.ex_batFile)
        for ea_grp in self.tidy_lst:
            tmp_wr_str = ""
            exec_idx = self.tidy_lst.index(ea_grp)
            with open(self.ex_batFile, 'a') as f:
                rec_cp_tm_str = "echo \"{}\">{}{}".format(exec_idx + 1, self.rec_cptimes_f, os.linesep)
                f.write(rec_cp_tm_str)
                for ea_it in ea_grp:
                    tmp = "{!r}".format(ea_it).split("'")[1]
                    tmp_wr_str += "\"{}\" ".format(tmp)
                # print('------------------------------------')
                # print tmp_wr_str
                # print('-------222222------------------------')
                wrStr = re.sub('&COPY_FILES_PERGRP&',tmp_wr_str,self.wr2f_cmd[self.copyMode])
                # print wrStr
                f.write(wrStr)
                if exec_idx == self.exec_count - 1:
                    rec_cp_tm_str = "echo \"{}\">{}{}".format(exec_idx + 2, self.rec_cptimes_f, os.linesep)
                    f.write(rec_cp_tm_str)
        return True
    def check_copyTimes(self):
        res = 0
        with open(self.rec_cptimes_f, 'r') as f_cptm:
            res = int(re.search('\d+', f_cptm.readlines()[0]).group())
        return res

    def ref_pr_bar(self,cur_cp_num, exec_count, cpProgressWin):# 更新进度条
        prg_num_tmp = (cur_cp_num / float(exec_count)) * 100
        mc.progressWindow(cpProgressWin, e=True, progress=prg_num_tmp, status="Copy perform: {}%".format(prg_num_tmp))

    def filetest(self,filePth,destDir):# determins whether a file needs bo be copied.
        #filePth = new_ea_02
        # print ("CHECK FILE WHETHER EXISTS : {}".format(filePth))
        txf_mt = time.localtime(os.stat(filePth).st_mtime)
        # print txf_mt
        # print destDir
        fnm = os.path.basename(filePth)
        targ_f_pth = os.path.abspath(os.path.join(destDir,fnm))
        # print targ_f_pth
        if not os.path.isfile(targ_f_pth): return True
        destf_mt = time.localtime(os.stat(targ_f_pth).st_mtime)
        # print("SOURCE FILE M-Time: {}".format(txf_mt))
        # print("DEST FILE M-Time  : {}".format(destf_mt))
        if txf_mt != destf_mt: return True
        else: return None

























import sys
# import win32wnet
# print(win32wnet.WNetGetUniversalName('z:',1))





# if __name__ == "__main__":
    # a  = monitoringPro('maya.exe')
    # killPro('maya.exe')