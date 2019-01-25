#!/usr/bin/env python
# coding=utf-8
import os
import sys
import shutil

import maya.cmds as mc
import maya.mel as mm


class AssetDeadline():
    def __init__(self):
        #UI
        self._windowSize = (400, 350)
        self._windowName = "DeadlineSubmitUI"
        self._assetRadio = ""
        self._outputFiled = ""
        self._okButton = ""
        self._deadlineSereveIp = ""
        self._fileName = ""
        self._ProjectPath = ""
        self._ProjectName = ""

    def close(self, *args):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName)

    def show(self, *args):
        self.close()

        #make the window
        win = mc.window(self._windowName,
                        t='DeadlineSubmitUI_zwz',
                        wh=self._windowSize,
                        mnb=False, mxb=False, rtf=True, s=True)
        form = mc.formLayout(numberOfDivisions=100)
        one = mc.columnLayout('row1', p=form)
        mc.frameLayout('form', l="Servers List", h=20, borderStyle='out', p='row1')
        mc.columnLayout('row2', p='row1', rs=20)
        selectRadio = mc.radioCollection(p='row2')
        mc.radioButton('one', l=u'#1 (211池)', onc=self.selectServer, p='row2')
        mc.radioButton('two', l=u'#2 (222池)', onc=self.selectServer, p='row2')
        mc.radioButton('three', l=u'#3 (223池)', onc=self.selectServer, p='row2')
        mc.radioButton('four', l=u'#4 (224池)', onc=self.selectServer, p='row2')
        mc.radioButton('five', l=u'#5 (73池)', onc=self.selectServer, p='row2')
        two_one = mc.frameLayout('frame2', l="Server Info", h=20, borderStyle='out', p=form)
        two_two = mc.scrollField('serverInfo', tx='', ww=True, ed=False, p=form)
        three_one = mc.button('slButton', l='Submint', c=self.copyFile, p=form, en=False, bgc=[0, 0.7, 0], w=100)
        three_two = mc.button('cancelButton', l='Cancel', c=self.close, p=form, w=100)

        mc.formLayout(form, edit=True,
                      attachForm=[(one, 'left', 5), (two_one, 'right', 5), (two_two, 'right', 5), (one, 'top', 5), (two_one, 'top', 5), (three_one, 'left', 5), (three_one, 'right', 5), (three_two, 'left', 5), (three_two, 'right', 5), (three_two, 'bottom', 5)],
                      attachControl=[(two_one, 'left', 1, one), (two_two, 'left', 1, one), (two_two, 'top', 1, two_one), (one, 'bottom', 1, three_one), (two_two, 'bottom', 1, three_one), (three_one, 'bottom', 1, three_two)],
                      attachNone=[(three_one, 'top')],
                      )

        self._windowName = win
        self._assetRadio = selectRadio
        self._outputFiled = two_two
        self._okButton = three_one

        mc.showWindow(win)

    def selectServer(self, *args):
        mc.waitCursor(state=True)
        selectOption = mc.radioCollection(self._assetRadio, q=True, sl=True)
        if selectOption == 'one':
            self._deadlineSereveIp = r'//192.168.80.211'
        elif selectOption == 'two':
            self._deadlineSereveIp = r'//192.168.80.222'
        elif selectOption == 'three':
            self._deadlineSereveIp = r'//192.168.80.223'
        elif selectOption == 'four':
            self._deadlineSereveIp = r'//192.168.80.224'
        elif selectOption == 'five':
            self._deadlineSereveIp = r'//192.168.6.73'
        path = os.getenv('PATH').split(';')
        addr = ''
        for eachPath in path:
            if 'Deadline/bin' in eachPath:
                addr = eachPath
                if os.path.isfile('%s/deadlinecommand.exe' % addr):
                    break
        if addr == '':
            mc.confirmDialog(title=u'温馨提示：', message=u'找不到Deadline客户端安装目录,请安装Deadline客户端.', button=['OK'], defaultButton='Yes', dismissString='No')
            sys.stderr.write(u'找不到Deadline客户端安装目录,请安装Deadline客户端.')
        else:
            try:
                str = os.popen(r'"%s/deadlinecommand.exe" -ChangeRepository %s/DeadlineRepository' % (addr, self._deadlineSereveIp)).read()
            except:
                sys.stderr.write(u'设定Deadline服务器时出错,请检查网络连接或权限.')
            else:
                try:
                    str = os.popen(r'"%s/deadlinecommand.exe" -executescript //octvision.com/cg/td/APP/RenderFarm/getServerInfo.py' % addr).read()
                except:
                    mc.confirmDialog(title=u'温馨提示：', message=u'获取Deadline的信息失败，请联系技术管理员！', button=['OK'], defaultButton='Yes', dismissString='No')
                    sys.stderr.write('Error getting Server Info')
                else:
                    mc.scrollField(self._outputFiled, e=True, tx=str)
                    mc.button(self._okButton, e=True, en=True)
        mc.waitCursor(state=False)

    def checkFile(self):
        projectPath = mm.eval('getenv "OCTV_PROJECTS"')
        #检查文件目录,当正确时分解出工程目录名，项目名
        fileLongName = mc.file(q=True, sn=True)
        if fileLongName:
            fileLongName = os.path.normpath(fileLongName)
            fileLongName = fileLongName.replace('\\', '/')
            fileSN = fileLongName.split('/')
            while '' in fileSN:
                fileSN.remove('')
            if not (((fileSN[0].lower() == 'z:' or fileSN[0] == '192.168.80.200') and fileSN[1].lower() == 'themes' and fileSN[3].lower() == 'project') or (fileSN[0].lower() == 'octvision.com' and fileSN[2].lower() == 'themes' and fileSN[4].lower() == 'project')):
                mc.confirmDialog(title=u'警告', message=u'只限Check in后的文件提交后台渲染!\n\n来吧....\n让Check in来的更猛烈些吧！', button=['OK'], defaultButton='Yes', dismissString='No')
                return False
            else:
                #传递工程名字
                if fileSN[0].lower() == 'z:':
                    self._ProjectPath = r'%s/%s/%s/%s' % (fileSN[0], fileSN[1], fileSN[2], fileSN[3])
                    self._ProjectName = fileSN[2]
                elif fileSN[0] == '192.168.80.200':
                    self._ProjectPath = r'//%s/%s/%s/%s' % (fileSN[0], fileSN[1], fileSN[2], fileSN[3])
                    self._ProjectName = fileSN[2]
                elif fileSN[0] == 'octvision.com':
                    self._ProjectPath = r'//%s/%s/%s/%s/%s' % (fileSN[0], fileSN[1], fileSN[2], fileSN[3], fileSN[4])
                    self._ProjectName = fileSN[3]
                self._fileName = fileLongName
        else:
            mc.confirmDialog(title=u'警告', message=u'文件名为空！\n只限Check in后的文件提交后台渲染!\n\n来吧....\n让Check in来的更猛烈些吧！', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        #检查贴图路径
        noTexFiles = []
        ErrorTexPaths = []
        allTexFiles = mc.ls(type='file')
        if allTexFiles:
            for texFile in allTexFiles:
                try:
                    texFileName = mc.getAttr('%s.fileTextureName' % texFile)
                except:
                    pass
                else:
                    if texFileName.find('${OCTV_PROJECTS}') >= 0:
                        texFileName = texFileName.replace('${OCTV_PROJECTS}', projectPath)
                    texFileName = os.path.normpath(texFileName)
                    texFileName = texFileName.replace('\\', '/')
                    texFileSN = texFileName.split('/')
                    while '' in texFileSN:
                        texFileSN.remove('')
                    if not os.path.isfile(texFileName):
                        noTexFiles.append(texFile)
                    else:
                        if not (((texFileSN[0].lower() == 'z:' or texFileSN[0] == '192.168.80.200') and texFileSN[1].lower() == 'themes') or (texFileSN[0].lower() == 'octvision.com' and texFileSN[2].lower() == 'themes')):
                            ErrorTexPaths.append(texFile)
        self.outPutSets(noTexFiles, 'sortNo_TexFiles_sets')
        self.outPutSets(ErrorTexPaths, 'sortErrorPath_TexFiles_sets')

        #检查缓存路径
        noCacheFiles = []
        ErrorCachePaths = []
        allCacheFiles = mc.ls(type='cacheFile')
        if allCacheFiles:
            for cacheFile in allCacheFiles:
                try:
                    cachePath = mc.getAttr('%s.cachePath' % cacheFile)
                except:
                    pass
                else:
                    cacheName = mc.getAttr('%s.cacheName' % cacheFile)
                    cacheFilePath = os.path.join(cachePath, cacheName) + '.xml'
                    if cacheFilePath.find('${OCTV_PROJECTS}') >= 0:
                        cacheFilePath = cacheFilePath.replace('${OCTV_PROJECTS}', projectPath)
                    cacheFilePath = os.path.normpath(cacheFilePath)
                    cacheFilePath = cacheFilePath.replace('\\', '/')
                    cacheFileSN = cacheFilePath.split('/')
                    while '' in cacheFileSN:
                        cacheFileSN.remove('')
                    if not os.path.isfile(cacheFilePath):
                        noCacheFiles.append(cacheFile)
                    else:
                        if not (((cacheFileSN[0].lower() == 'z:' or cacheFileSN[0] == '192.168.80.200') and cacheFileSN[1].lower() == 'themes') or (cacheFileSN[0].lower() == 'octvision.com' and cacheFileSN[2].lower() == 'themes')):
                            ErrorCachePaths.append(cacheFile)
        self.outPutSets(noCacheFiles, 'sortNo_CacheFiles_sets')
        self.outPutSets(ErrorCachePaths, 'sortErrorPath_CacheFiles_sets')

        #检查代理路径
        noProxyFiles = []
        ErrorProxyPaths = []
        try:
            allVrProxys = mc.ls(type='VRayMesh')
        except:
            pass
        else:
            if allVrProxys:
                for vrProxy in allVrProxys:
                    try:
                        vrProxyFileName = mc.getAttr('%s.fileName' % vrProxy)
                    except:
                        pass
                    else:
                        if vrProxyFileName.find('${OCTV_PROJECTS}') >= 0:
                            vrProxyFileName = vrProxyFileName.replace('${OCTV_PROJECTS}', projectPath)
                        vrProxySN = vrProxyFileName.split('/')
                        while '' in vrProxySN:
                            vrProxySN.remove('')
                        if not os.path.isfile(vrProxyFileName):
                            noProxyFiles.append(vrProxy)
                        else:
                            if not (((vrProxySN[0].lower() == 'z:' or vrProxySN[0] == '192.168.80.200') and vrProxySN[1].lower() == 'themes') or (vrProxySN[0].lower() == 'octvision.com' and vrProxySN[2].lower() == 'themes')):
                                ErrorProxyPaths.append(vrProxy)
        self.outPutSets(noProxyFiles, 'sortNo_ProxyFiles_sets')
        self.outPutSets(ErrorProxyPaths, 'sortErrorPath_ProxyFiles_sets')

        #输出错误
        ErrorText = u''
        numnoTexFiles = len(noTexFiles)
        numErrorTexPaths = len(ErrorTexPaths)
        numNoCacheFiles = len(noCacheFiles)
        numErrorCachePaths = len(ErrorCachePaths)
        numNoProxyFiles = len(noProxyFiles)
        numErrorProxyPaths = len(ErrorProxyPaths)
        if numnoTexFiles+numNoCacheFiles+numNoProxyFiles > 0:
            ErrorText += u'文件存在以下错误：\n错误1: 在输入的路径下，相应文件并不存在!\n有以类型的节点:\n\n'
            if numnoTexFiles:
                ErrorText += u'有 %s 个贴图file文件,并存在"sortNo_TexFiles_sets"的sets节点下\n' % numnoTexFiles
            if numNoCacheFiles:
                ErrorText += u'有 %s 个缓存cacheFile文件,并存在"sortNo_CacheFiles_sets"的sets节点下\n' % numNoCacheFiles
            if numNoProxyFiles:
                ErrorText += u'有 %s 个代理cacheFile文件,并存在"sortNo_ProxyFiles_sets"的sets节点下\n' % numNoProxyFiles
            ErrorText += u'\n\n'
        if numErrorTexPaths+numErrorCachePaths+numErrorProxyPaths > 0:
            if not ErrorText:
                ErrorText += u'文件存在以下错误：\n'
            ErrorText += u'错误2: 输入的路径不符合规范!\n有以下类型的节点:\n\n'
            if numErrorTexPaths:
                ErrorText += u'有 %s 个贴图file文件,并存在"sortErrorPath_TexFiles_sets"的sets节点下\n' % numErrorTexPaths
            if numErrorCachePaths:
                ErrorText += u'有 %s 个缓存cacheFile文件,并存在"sortErrorPath_CacheFiles_sets"的sets节点下\n' % numErrorCachePaths
            if numErrorProxyPaths:
                ErrorText += u'有 %s 个代理cacheFile文件,并存在"sortErrorPath_ProxyFiles_sets"的sets节点下\n' % numErrorProxyPaths
            ErrorText += u'\n'
            ErrorText += u'路径的开头地址应该是以下几种：\n1、${OCTV_PROJECTS} \n2、\\192.168.80.200\Themes \n3、Z:\Themes'
        if ErrorText:
            print ErrorText
            mc.confirmDialog(title=u'警告', message=u'%s' % ErrorText, button=['OK'], defaultButton='Yes', dismissString='No')
            return False
        print ErrorText
        return True

    def outPutSets(self, nodes, name):
        if nodes:
            mc.select(nodes)
            if mc.objExists(name):
                mc.sets(cl=name)
                mc.sets(add=name)
            else:
                mc.sets(n=name)
        else:
            if mc.objExists(name):
                mc.delete(name)

    def copyFile(self, *args):
        #设置工程目录
        mm.eval('setProject "%s"' % self._ProjectPath)
        #建立相应文件夹
        saveFileSereveIp = ''
        userName = os.environ['USER']
        sceneFileName = mc.file(q=True, shn=True, sn=True)
        tempName = os.path.splitext(sceneFileName)
        fileName = tempName[0]
        fileType = tempName[1]
        if self._deadlineSereveIp == r'//192.168.80.211':
            saveFileSereveIp = r'//192.168.80.221'
        elif self._deadlineSereveIp == r'//192.168.80.222':
            saveFileSereveIp = r'//192.168.80.222'
        elif self._deadlineSereveIp == r'//192.168.80.223':
            saveFileSereveIp = r'//192.168.80.223'
        elif self._deadlineSereveIp == r'//192.168.80.224':
            saveFileSereveIp = r'//192.168.80.224'
        elif self._deadlineSereveIp == r'//192.168.6.73':
            saveFileSereveIp = r'//192.168.6.73'
        #建立maya文件夹
        saveMayaPath = os.path.join(saveFileSereveIp, 'MayaFiles', userName, self._ProjectName)
        saveMayaPath = os.path.normpath(saveMayaPath)
        saveMayaPath = saveMayaPath.replace('\\', '/')
        if not os.path.isdir(saveMayaPath):
            os.makedirs(saveMayaPath)
        #判断是否存在旧的文件
        existServerFile = r'%s/%s' % (saveMayaPath, sceneFileName)
        if os.path.isfile(existServerFile):
            delTick = mc.confirmDialog(title=u'警告:', message=u'在 %s 下\n已存在%s文件\n\n请问是否覆盖原文件' % (saveMayaPath, sceneFileName), button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
            if delTick == 'Yes':
                os.remove(existServerFile)
            else:
                return False
        #maya另存文件
        myTyprName = 'mayaBinary'
        if fileType.find('mb') >= 0:
            myTyprName = 'mayaBinary'
        else:
            myTyprName = 'mayaAscii'
        mc.file(rename=existServerFile)
        mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
        #建立素材文件夹
        saveFilePath = os.path.join(saveFileSereveIp, 'Images', userName, self._ProjectName, fileName)
        saveFilePath = os.path.normpath(saveFilePath)
        saveFilePath = saveFilePath.replace('\\', '/')
        if not os.path.isdir(saveFilePath):
            os.makedirs(saveFilePath)
        mm.eval('global string $myDeadlineImagesPath = "%s"' % saveFilePath)
        for txt in sys.path:
            txt = os.path.normpath(txt)
            if os.path.isfile(r'%s\scripts\SubmitMayaToDeadline.mel' % txt):
                txtTemp = r'%s\scripts\SubmitMayaToDeadline.mel' % txt
                txtTemp = os.path.normpath(txtTemp)
                txtTemp = txtTemp.replace('\\', '/')
                mm.eval('source "%s"' % txtTemp)
        mc.evalDeferred("mm.eval('SubmitJobToDeadline')")





def show():
    i = AssetDeadline()
    # if i.checkFile():
    #     i.show()
    i.show()
    return i

show()
