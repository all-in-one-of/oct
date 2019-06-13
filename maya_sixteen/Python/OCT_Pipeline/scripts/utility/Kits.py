#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Kits
__author__ = zhangben 
__mtime__ = 2019/4/2 : 9:55
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import os,re,sys,time
import subprocess
import string
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
    def monitoringPro(self,pr_name='FastCopy.exe',all=False,holdPrIds=None):## 由进程的名字获取idp
        searchPr_cmd = "tasklist |findstr {}".format(pr_name)
        # cmd = shlex.split(searchPr_cmd)
        # print cmd
        grab_return = []
        p = subprocess.Popen(searchPr_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,shell=True)
        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            # opt = line.decode('cp936').encode(encoding='UTF-8')
            re_id = None
            if line:
                re_id = re.compile("\d+ Console")
                if re_id.search(line):
                    pr_idp = re.search("\d+", re_id.search(line).group()).group()
                    if all: grab_return.append(pr_idp)
                    else:
                        if holdPrIds:
                            if pr_idp not in holdPrIds:
                                grab_return.append(pr_idp)
                        else: grab_return.append(pr_idp)
        return grab_return if len(grab_return) else None

    def killPro(self,pr_name='FastCopy.exe',*holdPrIds): ## 结束指定名字的进程(所有）
        pr_id = self.monitoringPro(pr_name)
        if not pr_id:return
        for ea_pr in pr_id :
            if ea_pr not in holdPrIds:
                # p = psutil.Process(int(ea_pr))
                killPr_cmd = "taskkill /f /pid {}".format(ea_pr)
                p = subprocess.Popen(killPr_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,shell=True)
                while p.poll() is None:
                    line = p.stdout.readline()
                    line = line.strip()
                    opt = line.decode('cp936').encode(encoding='UTF-8')
                    if line:
                        print opt
    def run_subpr(self,per_cmd):# 运行系统命令，获得返回值
        grab_return = []
        p = subprocess.Popen(per_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,shell=True)
        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            opt = line.decode('cp936').encode(encoding='UTF-8')
            if line:
                grab_return.append(opt)
        return grab_return

    def findYourMapDrive(self,slash=None):# 获取映射驱动器盘符 及 路径
        res = self.run_subpr('net use')
        res_dic = {}
        for ea_l in res:
            look4Drv = re.search('[{}]:'.format(string.uppercase), ea_l)
            if look4Drv:
                drv = look4Drv.group()
                tmpSpl = [ea for ea in ea_l.split(' ') if ea.strip()]
                drv_ind = tmpSpl.index(drv)
                adr = tmpSpl[drv_ind + 1]
                if slash: adr = re.sub(r"\\",slash,adr)
                res_dic[drv] = adr
        return res_dic
    def usesep(self,pathStr,invers=False):# 获得路径分隔符
        get_backslash = re.findall(r"\\", pathStr)
        get_slash = re.findall('/', pathStr)
        if not invers: return r'\\' if len(get_backslash) > len(get_slash) else '/'
        else: return r'\\' if len(get_backslash) < len(get_slash) else '/'

    def uniformPath(self,pathStr,rpl):#统一路径分隔符
        re_pth = re.sub(r"\\",rpl,pathStr)
        re_pth = re.sub('/',rpl,re_pth)
        return re_pth

    def filetest(self,filePth,destDir):# determins whether a file needs bo be copied.
        #filePth = new_ea_02
        # print ("CHECK FILE WHETHER EXISTS : {}".format(filePth))
        if not os.path.exists(filePth): return None
        if not os.path.exists(destDir): return True
        txf_mt = time.localtime(os.stat(filePth).st_mtime)
        # print txf_mt
        # print destDir
        fnm = os.path.basename(filePth)
        targ_f_pth = destDir
        if os.path.isdir(destDir):
            targ_f_pth = os.path.abspath(os.path.join(destDir,fnm))
        # print targ_f_pth
        if not os.path.isfile(targ_f_pth): return True
        destf_mt = time.localtime(os.stat(targ_f_pth).st_mtime)
        # print("SOURCE FILE M-Time: {}".format(txf_mt))
        # print("DEST FILE M-Time  : {}".format(destf_mt))
        if txf_mt != destf_mt: return True
        else: return None
    def txAbsPath(self,varPath):#  包含变量的路径 修改为 绝对路径
        useVAR = None
        txfpth = varPath
        if varPath.startswith("${"):
            re_VAR = re.compile("[^${}]+")
            useVAR = re_VAR.search(varPath).group()
        if os.getenv(useVAR):
            txfpth = re.sub("^[$]+{\w+}", os.getenv(useVAR), varPath, re.I)
        return {varPath:txfpth}

    def normalizeTxNm(self,tx_f_bnm): # 规范 命名，让字符串只匹配 字母 数字 下划线 . ：贴图的  basename   如   JP-125-h.JPG
        txf_nm_spl = tx_f_bnm.split('.')
        txf_alter_spl = []
        for eaSpl in txf_nm_spl:
            if re.search('\W+',eaSpl,re.I):
                txf_alter_spl.append(re.sub('\W+', '_', eaSpl,0, re.I))# add replace count 如果不加，则只会替换两个。
            else:
                txf_alter_spl.append(eaSpl)
        return ".".join(txf_alter_spl)

    def findTxSeqs(self,txfile):#获得指定贴图的 序列贴图
        # txfile = aa.attr('fileTextureName').get()
        # txfile = r"Z:/Themes/CDMSS/Project/sourceimages/characters/ch001001Moss/CDMSS_ch001001Moss_head_roughness_1001.jpg"
        path_sep = self.usesep(txfile)
        txFolder = os.path.dirname(txfile)
        tx_bsnm = os.path.basename(txfile)
        tx_bsnm_spl = os.path.splitext(tx_bsnm)
        id_pars_srch = re.search("[_.-]\d*$", tx_bsnm_spl[0])
        if not id_pars_srch:
            iffy_info = "warning(\"the file node {} texture name nonstandard\")".format(txfile)
            return iffy_info
        id_pars = id_pars_srch.group()
        id_nums = re.search('\d+$', id_pars).group()
        # id_sep = re.sub('\d+','',id_pars)
        tx_bsnm_noid = re.sub("{}$".format(id_nums), "", tx_bsnm_spl[0])

        re_srch = re.compile("{}\d+{}".format(tx_bsnm_noid, tx_bsnm_spl[-1]))
        ret_seq = [txfile]
        tmp_list = []
        for ef in os.listdir(txFolder):
            if re_srch.search(ef):
                ef_full = "{}{}{}".format(txFolder, path_sep, ef)
                if ef_full not in ret_seq: tmp_list.append(ef_full)
        tmp_list.sort()
        ret_seq.extend(tmp_list)
        return ret_seq