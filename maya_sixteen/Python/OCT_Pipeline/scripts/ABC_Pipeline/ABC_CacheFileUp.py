# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import os,subprocess,re,time
import OCT_generel.CopyTxs as cptxs
from PyQt4 import QtGui, QtCore
reload(cptxs)
import octvDB


#直接上传整理后的缓存文件

OCT_PROJ = os.getenv('OCTV_PROJECTS')
OCT_DRIVE = r'\\octvision.com\CG'
RE_USER = r'octvision.com\supermaya'
RE_PWD = 'supermaya'
class ABC_CacheFileUp(QtGui.QDialog):
    percent = QtCore.pyqtSignal('int')
    def __init__(self, parent = None):
        super(ABC_CacheFileUp, self).__init__(parent)
        self.OCTV_TECH = os.getenv('OCTV_TECH') if os.getenv('OCTV_TECH') else '//octvision.com/CG/Tech'
        self.cpauPath = r'%s\bin\CPAU.exe' % os.path.abspath(self.OCTV_TECH)

        self.myFcopyPath = "{}\\bin\\FastCopy341\\FastCopy.exe".format(self.OCTV_TECH).replace("/","\\")

        self.modeDic = {u'cc': 'cache'}
        self.fileName = mc.file(q=True, sn=True)  # 获取文件名
        self.shortName = mc.file(q = True, sn = True, shn = True)
        self.proj = ""         #项目名称
        self.destFolder = ""    #上传目录
        self.upfilename = ""     #上传文件路径
        self.destMapFolder = "" #贴图路径
        self.mode = ''          # 环节描述
        self.videoFile = ""     #视频文件
        self.videoFileType = ['.avi', '.mov']
        self.ext = ""           #扩展名
        self.desc = "test"          #描述字段
        self.worker1 = CopyJobThread(self)
        self.worker2 = CopyJobThread(self)
        self.percent.connect(self.EditProgressWindow)

    def __del__(self):
        del self.worker1,self.worker2

    def EditProgressWindow(self, i):
        mc.progressWindow(edit=True, progress=i)

    def upLoadFile(self):
        self.getFileInfo()
        mc.progressWindow(title=u'上传cache文件', status=u'开始上传', isInterruptable=True)
        self.getAlembicCache()
        self.copyTxsFile()
        self.addVideo()
        self.saveFile()
        mc.progressWindow(endProgress=True)
        self.insertData()

    #获取上传缓存文件的信息
    def getFileInfo(self):
        if not self.fileName:
            mc.error(u"请先保存文件！")

        #获取项目名
        shortName = os.path.basename(self.fileName)
        splitName = os.path.splitext(shortName)
        self.ext = splitName[-1]
        buf = splitName[0].split("_")
        self.proj = buf[0]

        #获取上传路径
        if len(buf)>=4 and len(buf)<= 6:
            if buf[3] in self.modeDic.keys():
                self.upfilename  = buf[0] + "_" + buf[1] + "_" + buf[2] + "_" + buf[3]
                self.mode = self.modeDic[buf[3]]
            elif buf[4] in self.modeDic.keys():
                self.upfilename = buf[0] + "_" + buf[1] + "_" + buf[2] + "_" + buf[3] + "_" + buf[4]
                self.mode = self.modeDic[buf[4]]
            else:
                mc.error(u"文件命名错误，正确的名字格式为：项目名_场景号_镜头号_描述字段(可忽略)_环节_版本(可忽略)，例如 PROJ_sc10_sh02_fight_an_002.mb")

            self.destFolder = "{}/{}/Project/scenes/animation/{}/{}/{}".format(OCT_PROJ, self.proj, buf[1], buf[2],self.mode)
            self.destMapFolder = "{}/{}/Project/sourceimages/animation/{}/{}/maps".format(OCT_PROJ, self.proj, buf[1], buf[2])
            if not os.path.isdir(self.destFolder):
                mc.error(u"找不到对应编号目录，请检查文件名或者联系PA")
            else:
                fList = mc.getFileList(folder = self.destFolder, filespec = "{}*".format(self.upfilename))
                newNum = ""
                if fList:
                    name = os.path.splitext(sorted(fList)[-1])[0]
                    num = int(name[-3:]) + 1
                    newNum = "%03d" % num
                else:
                    newNum = "001"

                self.upfilename = "{}_c{}{}".format(self.upfilename, newNum, self.ext)
        else:
            mc.error(u"文件命名错误，请根据环节正确命名！")

    def addVideo(self):
        #判断是否存在同名的视频文件就上传，无就忽略
        flag = False
        videoName = ""
        for video in self.videoFileType:
            videoName = self.fileName.replace(self.ext, video)
            if os.path.isfile(videoName):
                flag = True
                break
        if flag:
            db = "dbo.filesystem_upload"
            v_ext = os.path.splitext(videoName)[-1]
            buf = self.upfilename.split("_")
            videoFileName = "%s%s"%("_".join(buf[0:-1]), v_ext)
            self.videoFile = os.path.join(self.destFolder, videoFileName).replace("/", "\\")
            videoName = videoName.replace("/", "\\")
            self.getCopyFile(videoName, self.videoFile)

            self.videoFile = self.videoFile.replace("\\", "/")

            octvDB.delTextureDB(db, videoFileName)
            octvDB.insertAnimationDB(db, videoFileName, self.videoFile, self.proj, buf[1], buf[2], '1', "animation", self.mode)

    def saveFile(self):
        localTemp = r"D:\octvTemp"
        if not os.path.isdir(localTemp):
            os.mkdir(localTemp)

        locaoFileName = os.path.join(localTemp, self.upfilename)
        mc.file(rename=locaoFileName)
        try:
            mc.file(force=True, save=True, prompt=False, uiConfiguration = False)
        except:
            mc.error(u"不能保存文件，请检查D：盘是否空间不足")
        time.sleep(1)
        copyData = {locaoFileName:self.destFolder}
        # print copyData
        if self.CopyDataJob(copyData):
            mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData) + 1, status=u"正在上传文件!")
            return True


    #获取abc缓存文件拷贝上传
    def getAlembicCache(self):
        copyData = {}
        errInfo = []
        setData = {}

        destPath = "%s/alembic" % self.destFolder.replace("/scenes/", "/cache/")


        allAlembicNode = mc.ls(type = 'AlembicNode')
        matchPath = "{}/{}/Project/cache".format(OCT_PROJ, self.proj)
        for alembicNode in allAlembicNode:
            if mc.referenceQuery(alembicNode, isNodeReferenced = True):
                continue
            alembicPath = mc.getAttr("{}.abc_File".format(alembicNode))
            if alembicPath.lower().startswith(matchPath.lower()):
                if not alembicPath.lower().startswith(matchPath.replace(OCT_PROJ,"z:/themes/").lower()):
                    destFile = alembicPath.replace(OCT_PROJ, r"Z:/Themes")
                    mc.setAttr("{}.abc_File".format(alembicNode), destFile, type = "string")
                continue
            elif alembicPath.lower().startswith(matchPath.replace(OCT_PROJ,"z:/themes/").lower()):
                continue
            else:
                sourceFilePath = self.myChangeNetPath(alembicPath).replace("/", "\\")
                copyAbcCacheName = os.path.basename(sourceFilePath)
                copyAbcCachePathName = os.path.join(destPath, copyAbcCacheName)
                if os.path.isfile(sourceFilePath) and os.path.isfile(copyAbcCachePathName):
                    testMtime = os.path.getmtime(sourceFilePath)
                    tmpMtime = os.path.getmtime(copyAbcCachePathName)
                    if int(tmpMtime) >= int(testMtime):
                        continue

                if os.path.isfile(sourceFilePath):
                    destPath = destPath.replace("/", "\\")
                    copyData.update({sourceFilePath:destPath})
                    destFile = os.path.join(destPath, os.path.basename(alembicPath))
                    setData.update({alembicNode:destFile})
                else:
                    errInfo.append(alembicPath)
        if errInfo:
            mc.error("%s文件不存在!"%errInfo)
            return False


        if not os.path.isdir(destPath):
            self.getCreateDir(destPath)

        if copyData:
            mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 Alembic caChe 缓存!")
            # print copyData
            self.CopyDataJob(copyData)
            for key in setData.keys():
                mc.setAttr("{}.abc_File".format(key), setData[key], type="string")

    def copyTxsFile(self):
        allFileNode = mc.ls(type = "file")
        copyData = {}
        setData = {}
        for node in allFileNode:
            texFileNameGroup = []
            matchPath = "{}/{}/Project/sourceimages".format(OCT_PROJ, self.proj)
            matchPath = self.myChangeNetPath(matchPath)
            texFirstFilName = mc.getAttr('%s.fileTextureName' % node)
            texFirstFileName = self.myChangeNetPath(texFirstFilName)
            #判断如果上传在服务器上不需要拷贝
            if texFirstFileName.lower().startswith(matchPath.lower()):
                if not texFirstFilName.lower().startswith(matchPath.replace(OCT_PROJ,"z:/themes/").lower()):
                    destFile = texFirstFilName.replace(OCT_PROJ, r"Z:/Themes")
                    mc.setAttr("{}.fileTextureName".format(node), destFile, type = "string")
                continue

            seqFlag = mc.getAttr('%s.useFrameExtension' % node)
            uvSeqFlag = mc.getAttr('%s.uvTilingMode' % node)

            if not seqFlag and uvSeqFlag != 2 and uvSeqFlag != 3:
                texFileNameGroup.append(texFirstFileName)

            elif seqFlag or uvSeqFlag == 3 or uvSeqFlag == 2:
                myTexDirName = os.path.dirname(texFirstFileName)
                myTexBaseName = os.path.basename(texFirstFileName)
                myTexBaseNameSpl = os.path.splitext(myTexBaseName)

                re_isSeq = re.search('_\d+$|\.\d+$|_u\d+$|\.u\d+$|_U\d+$|\.U\d+$', myTexBaseNameSpl[0])
                if not re_isSeq:
                    texFileNameGroup.append(texFirstFileName)
                    WARNmsg = u"=======没有找到序列信息，建议检查序列贴图命名，确保最后是数字序号+贴图格式(\"name.####.ext\"或\"name_####.ext\")======\n" \
                              u"IFFY TEXTURE :    {}".format(texFirstFileName)
                else:
                    myTexFileTopName = re.sub('_\d+$|\.\d+$|_u\d+$|\.u\d+$|_U\d+$|\.U\d+$', '', myTexBaseNameSpl[0])
                    myAllFileName = os.listdir(myTexDirName)
                    for eachDirFileName in myAllFileName:
                        if eachDirFileName.find(myTexFileTopName) >= 0 and re.search('{}(_\d+|\.\d+|_u\d+|\.u\d+|_U\d+$|\.U\d+$)'.format(myTexFileTopName), eachDirFileName):
                            IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                            texFileNameGroup.append(IndexTexName)

            if texFileNameGroup:
                for texFilName in texFileNameGroup:
                    sourceFilePath = self.myChangeNetPath(texFilName).replace("/", "\\")
                    copyFileCacheName = os.path.basename(sourceFilePath)
                    copyFileCachePathName = os.path.join(self.destMapFolder, copyFileCacheName).replace("/","\\")
                    if os.path.isfile(sourceFilePath) and os.path.isfile(copyFileCachePathName):
                        testMtime = os.path.getmtime(sourceFilePath)
                        tmpMtime = os.path.getmtime(copyFileCachePathName)
                        if int(tmpMtime) >= int(testMtime):
                            continue

                    if not texFilName in copyData.keys():
                        destPath = self.destMapFolder.replace("/", "\\")
                        copyData.update({sourceFilePath:destPath})
                    else:
                        continue

                destFileName = os.path.join(self.destMapFolder, os.path.basename(texFirstFileName))
                destFileName = destFileName.replace(OCT_PROJ, r"Z:/Themes")
                setData.update({node:destFileName})

        if copyData:
            mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData) + 1, status=u"正在拷贝相应的 file 贴图!")
            self.CopyDataJob(copyData)

        for key in setData.keys():
            mc.setAttr("{}.fileTextureName".format(key), setData[key], type="string")

    # 拷贝文件
    def getCopyFile(self, filePathName, masterFilePath):
        cmd = r'%s -u %s -p %s -ex  "COPY /Y  %s %s" -lwp -c -nowarn -wait' % (
        self.cpauPath, RE_USER, RE_PWD, filePathName, masterFilePath)
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        while True:
            if not p.poll() is None:
                del p
                break

    # 创建备份文件夹
    def getCreateDir(self, dirBackPath):
        cmd = r'%s -u %s -p %s -ex  "md %s " -lwp -c -nowarn -wait' % (
        self.cpauPath, RE_USER, RE_PWD, dirBackPath)
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        while True:
            if not p.poll() is None:
                del p
                break

    #插入数据库信息
    def insertData(self):
        upUser = os.getenv('username')
        os.path.basename(self.upfilename)
        dirPath = os.path.join(self.destFolder, self.upfilename).replace("\\", "/")
        octvDB.insertDB("animation", self.upfilename, "0", "1", upUser, dirPath, "1", "", self.desc)

    #转换路径
    def myChangeNetPath(self, TempPath):
        if TempPath.find('${OCTV_PROJECTS}') >= 0:
            TempPath = TempPath.replace('${OCTV_PROJECTS}', OCT_PROJ)
        elif TempPath.find('z:') >= 0:
            TempPath = TempPath.replace('z:', OCT_DRIVE)
        elif TempPath.find('Z:') >= 0:
            TempPath = TempPath.replace('Z:', OCT_DRIVE)
        return TempPath

        # 双线程拷贝

    def CopyDataJob(self, myDict):
        i = 0
        for key in myDict.keys():
            if mc.progressWindow(q=True, isCancelled=True):
                while True:
                    if self.worker1.wait() and self.worker2.wait():
                        break
                return False
            mySourceFile = key
            myDestFile = myDict[key]
            if i == 0:
                self.worker1.ready(self.cpauPath, self.myFcopyPath, mySourceFile, myDestFile)
            elif i == 1:
                self.worker2.ready(self.cpauPath, self.myFcopyPath, mySourceFile, myDestFile)
            else:
                while True:
                    if self.worker1.isFinished():
                        self.worker1.ready(self.cpauPath, self.myFcopyPath, mySourceFile, myDestFile)
                        break
                    elif self.worker2.isFinished():
                        self.worker2.ready(self.cpauPath, self.myFcopyPath, mySourceFile, myDestFile)
                        break
            i += 1
            self.percent.emit(i)
        while True:
            if self.worker1.wait() and self.worker2.wait():
                break
        return True


class CopyJobThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(CopyJobThread, self).__init__(parent)
        self.myLocalFlag = False

    def ready(self, CpauPath, FcopyPath, source, dest):
        self.myFcopyPath = FcopyPath
        self.myCpauPath = CpauPath
        self.mySourceFile = source
        self.myDestFile = dest
        self.start()

    def run(self):
        cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE /bufsize=32 \"%s\" /to=\"%s\""' % (
        self.myCpauPath, RE_USER, RE_PWD, self.myFcopyPath, self.mySourceFile, self.myDestFile)
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        while True:
            if not p.poll() is None:
                del p
                break

#ABC_CacheFileUp().upLoadFile()
