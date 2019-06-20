#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'Pc_obtScInfor'    
__author__ = zhangben
__mtime__ = 2018/12/6:17:26
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import maya.cmds as mc
import pymel.core as pm
import re,os

OCT_PROJ = os.getenv('OCTV_PROJECTS')
class Ppl_scInfo(object):
    u"""
    获取镜头文件信息
        self.proj = None               #项目名称
        self.ID = None                 #文件ID   shot：（集数） 场次 镜头  asset: 资产identity
        self.projRoot_serv = None      #项目在服务器上的root目录
        self.projPath_serv = None      # 项目工程目录（数据库）
        self.projPath_loc = None       # 本地工程路径
        self.cwd_local = None          # 当前文件存储路径
        self.cwd_serv = None           # 文件服务器存储路径
        self.sectionPart = None        # 文件类别  asset  / shot
        self.section = None            # 环节 缩写 mo tx rg ef lg etc...
        self.mode = ''                 # 环节描述
        # self.destFolder = None       # checkin　目录
        self.shotType = 2              # 镜头场次分类方式 默认是2

        #===asset file informations
        # self.assetId = None           #资产ID

        self.assetPrec = None           #资产精度描述  precision : h l
        self.category = None            #资产类型 #  asset  which one dose the assets belongs to,in character,props and set
        self.needMatch = False          #资产文件是 是否需要 匹配检测
        #==========read file information===================
        self.scnm = sceneFile if sceneFile else pm.sceneName()
        self.scbsnm = os.path.basename(self.scnm)
        self.obtScInfo()
    """
    def __init__(self,sceneFile=None):
        self.modeDic = {u'mo': 'model', u'tx': 'texture', u'rg': 'rigging', u'ms': 'master', u'an':'anim',u'sm':'simulation',u'ef':'effect',u'lg':'lighting',u'rn':'rendering',u'cc':'cache'}
        # self.modeFolder = {u'mo':'model',u'tx':'texture',r'rg':'rigging',u'ms':'master','shot':'animation',u'an':'anim',u'cc':'cache',u'ef':'effect'}
        self.sort = {'asset':{'ch':'characters','pr':'props','se':'sets'},'shot':{'ep':'anim','sc':'anim'}}
        self.sectionDic = {'ch':'asset','pr':'asset','se':'asset','ep':'shot','sc':'shot'}
        self.shtypDic = {'ep':3,'sc':2}
        #self.precisionDic = {u'lo':'l'}
        self.proj = None               #项目名称
        self.ID = None             #文件ID   shot：（集数） 场次 镜头  asset: 资产identity
        self.projRoot_serv = None   #项目在服务器上的root目录
        self.projPath_serv = None  # 项目工程目录（数据库）
        self.projPath_loc = None  # 本地工程路径
        self.cwd_local = None  # 当前文件存储路径
        self.cwd_serv = None  # 文件服务器存储路径
        self.sectionPart = None  # 文件类别  asset  / shot
        self.section = None  # 环节 缩写 mo tx rg ef lg etc...
        self.mode = ''  # 环节描述
        # self.destFolder = None  # checkin　目录
        self.shotType = 2  # 镜头场次分类方式 默认是2

        #===asset file informations
        # self.assetId = None              #资产ID

        self.assetPrec = None            #资产精度描述  precision : h l
        self.category = None           #资产类型 #  asset  which one dose the assets belongs to,in character,props and set
        self.needMatch = False         #资产文件是 是否需要 匹配检测
        #==========read file information===================
        self.scnm = sceneFile if sceneFile else pm.sceneName()
        self.scbsnm = os.path.basename(self.scnm)
        self.obtScInfo()
    def obtScInfo(self):#获取信息的函数 并赋值
        # scnm = pm.sceneName()
        # print scnm
        scbsnm = self.scnm.basename()
        bsnm_spl = os.path.splitext(scbsnm)[0].split(u'_')
        # print bsnm_spl
        self.proj = bsnm_spl[0]
        self.projRoot_serv = "{}/{}".format(OCT_PROJ,self.proj)
        self.projPath_serv = "{}/Project".format(self.projRoot_serv)
        # print bsnm_spl[1][:2]
        self.projPath_loc = pm.workspace.getPath()
        self.cwd_local = pm.workspace.getcwd()
        id_pref = bsnm_spl[1][:2]
        self.sectionPart = self.sectionDic[id_pref]
        self.category = self.sort[self.sectionPart][id_pref]
        if  self.sectionPart == 'asset':
            self.ID = bsnm_spl[1]
            # print assId
            self.section = bsnm_spl[3]
            try:
                self.mode = self.modeDic[self.section]
            except Exception,e:
                print(e.message)
            self.assetPrec = bsnm_spl[2]
            self.cwd_serv = '{}/scene/{}/{}/{}'.format(self.projPath_serv, self.sort[self.sectionPart][id_pref], self.ID, self.mode)
            if self.category in ['character'] and self.section in [u'tx',u'rg']: self.needMatch = True
        else:
            self.shotType = self.shtypDic[self.category]
