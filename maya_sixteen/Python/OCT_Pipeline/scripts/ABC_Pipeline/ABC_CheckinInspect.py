#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = CheckinInspect
__author__ = zhangben 
__mtime__ = 2019/6/13 : 12:35
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import maya.cmds as mc
import pymel.core as pm
import maya.OpenMaya as om
from ..Major import Ppl_scInfo
reload(Ppl_scInfo)
import k_alembicToDatabase as abc2db
import os,re,sys,time,urllib2
# OCT_PROJ = os.getenv('OCTV_PROJECTS')
class CheckinInspect(object):
    """
    checkin asset file or shot file , inspection procedure
    """
    def __init__(self):
        """
        :return:
        """
        # self.chk_db_ip = r"http://192.168.5.20:801"
        # self.chk_db_ip = r"http://pcgr502:801"
        # self.chk_db_ip = r"http://http://192.168.5.20:801"
        self.matchSecDic = {'tx':'rg','rg':'tx'}
        self.chk_dp_ip = "http://192.168.80.200:801"
        self.scInfo = Ppl_scInfo.Ppl_scInfo()
        self.dbop = abc2db.k_alembicToDatabase()
        self.iffyMsg = {}
        print("new checkin mode ---------abc cache pipeline mode")
    def AssetCheck(self,checkTaskBsnm=None):## rg  and tx file checkin  needs inspect alembic meshes  matchable
        if not checkTaskBsnm:
            curTaskBsnm = self.scInfo.scbsnm
            checkTaskBsnm = re.sub(self.scInfo.section,self.matchSecDic[self.scInfo.section],curTaskBsnm)
        chk_addr = "{}/yemojk.aspx?caozuo=ppcx&m={}".format(self.chk_dp_ip,checkTaskBsnm)
        chk_v = urllib2.urlopen(chk_addr).read()
        if chk_v == "NULL" or chk_v == 'False':
            self.dbop.do('upload')
        else:
            chk_r = self.dbop.do('check')
            if len(chk_r):
                om.MGlobal.displayInfo(">>> Asset Match Inspect Get An Error!!!!")
                self.iffyMsg['Match Inspect Error Pleach Check follow Meshes'] = list(chk_r)
            else:
                om.MGlobal.displayInfo(">>> Asset Match Inspect Done!!!!!!")

    def AssetSaveAsMs(self,checkTaskBsnm=None,desc='TD Test'): ## save msAnim  or msRender  file while rg and tx file checkin
        if not checkTaskBsnm: checkTaskBsnm = self.scInfo.scbsnm
        import File_SaveAs as fsa
        SaveAsMaster = fsa.File_SaveAs()
        infoList = SaveAsMaster.file_SaveAs(checkTaskBsnm, self.scInfo.cwd_serv,self.scInfo.mode)
        db = self.scInfo.sectionType
        checkTaskBsnm = infoList[0]
        fstate = "0"
        # master模式类型为7
        ftype = "7"
        upUser = os.getenv('username')
        fpath = infoList[1].replace('\\', '/')
        checkState = "1"
        checkUser = ""
        # 备注信息
        # desc = "test"
        # 插入新文件信息到数据库
        SaveAsMaster.insertData(db, checkTaskBsnm, fstate, ftype, upUser, fpath, checkState, checkUser, desc)
        # 插入备份信息到数据库
        fstate = "1"
        bakname = infoList[2]
        SaveAsMaster.insertData(db, bakname, fstate, ftype, upUser, fpath, checkState, checkUser, desc)
    def checkProjStates(self,PROJ_ROOT_SERV=None):# define a timestamp  , running the functions in this scripts when the projests's create time after the timestamp
        if not PROJ_ROOT_SERV: PROJ_ROOT_SERV = self.scInfo.projRoot_serv
        timestamp = '2017-09-23 21:02'
        proj_c_time = time.strftime('%Y-%m-%d %H:%M',time.localtime(os.stat(PROJ_ROOT_SERV).st_ctime))
        if proj_c_time == timestamp:
           return True
        else:
            return None
    def operate(self,op='check',desc=None):#执行 方法  分类为 check  检测匹配    saveAs  另存 msAnim  msRender
        if op == 'check':
            if not self.scInfo.needMatch: return
            newPpl = self.checkProjStates()
            if not newPpl:return
            self.AssetCheck()
            if self.iffyMsg:
                print ">>>Alembic Cache Pipeline Checkin Inspect Get Error:{}".format(os.linesep)
                for ea_msg in self.iffyMsg:
                    print("\t{}{}".format(ea_msg,os.linesep))
                    for ea_item in self.iffyMsg[ea_msg]:
                        print ea_item
                raise Exception(">>>OOPS! There something wrong!Please check script editor to find more information!")
        if op == 'saveAs':
            self.AssetSaveAsMs(desc=desc)
            # 如果匹配成功，要把数据的 匹配检测开关打开
            set_chk_addr = "{}/yemojk.aspx?caozuo=ppbj&z=1&m={}".format(self.chk_dp_ip, self.scInfo.scbsnm)
            set_chk_v = urllib2.urlopen(set_chk_addr).read()