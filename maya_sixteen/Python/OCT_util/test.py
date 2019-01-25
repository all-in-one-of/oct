import os
import subprocess
import maya.cmds as mc
import time

CPAU_PATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\fCopy'
REMOTE_USER = r'octvision.com\supermaya'
REMOTE_PWD = 'supermaya'
PROJECT_PATH = mm.eval('getenv "OCTV_PROJECTS"')
SERVE_PATH = r'\\192.168.80.205'
USERNAME = os.environ['COMPUTERNAME']
NEWPROJECT_NAME = 'New_Project'
MAYAFILE_NAME = 'MayaFiles'
FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\fCopy\FastCopy.exe'




#拷贝命令
def myCopyFile(temp_file, remote_dir):
    cmd = r'%s -u %s -p %s -ex "%s /force_close /no_confirm_del /force_start=FALSE /cmd=sync \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_FPATH, temp_file, remote_dir)
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
    p.communicate()
    while True:
        if not subprocess.Popen.poll(p) is None:
            del p
            break
        else:
            pass

def fileCountIn(dir):
    return sum([len(files) for root, dirs, files in os.walk(dir)])


def getCopyPath():
    FCOPY_SPATH_BN = os.path.basename(FCOPY_SPATH)
    FCOPY_SPATH_DN = os.path.dirname(FCOPY_SPATH)
    FCOPY_LPATH_DN = r'D:\Program Files (x86)\fCopy'
    if os.path.isdir(FCOPY_LPATH_DN):
        if fileCountIn(FCOPY_SPATH_DN) != fileCountIn(FCOPY_LPATH_DN):
            shutil.copyfile(FCOPY_SPATH_DN, FCOPY_LPATH_DN)
            time.sleep(5)
    else:
        myCopyFile(FCOPY_SPATH_DN, FCOPY_LPATH_DN)
        time.sleep(5)
    return os.path.join(FCOPY_LPATH_DN, FCOPY_SPATH_BN)

#创建文件夹命令
def myCreateFolder(address):
    cmd = r'%s -u %s -p %s -ex "md %s" -c' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, address)
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
    p.communicate()
    while True:
        if not subprocess.Popen.poll(p) is None:
            del p
            break
        else:
            time.sleep(1)

#拷贝命令
def myCopyFile(temp_file, remote_dir):
    temp_file = os.path.abspath(temp_file)
    remote_dir = os.path.abspath(remote_dir)
    cmd = r'%s -u %s -p %s -ex "%s /force_close /no_confirm_del /force_start=FALSE /cmd=sync \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, temp_file, remote_dir)
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
    p.communicate()
    while True:
        if not subprocess.Popen.poll(p) is None:
            del p
            break
        else:
            time.sleep(1)


#创建相应场景
def myCreateScenes():
    fileSName = mc.file(q=True, sn=True, shn=True)
    fileSNameSplit = fileSName.split('_')
    serveProject = os.path.join(SERVE_PATH, MAYAFILE_NAME, fileSNameSplit[0], fileSNameSplit[1], fileSNameSplit[2])
    if not os.path.isdir(serveProject):
        myCreateFolder(serveProject)
        exampleProject = os.path.join(SERVE_PATH, MAYAFILE_NAME, NEWPROJECT_NAME)
        myCopyFile(exampleProject, serveProject)
    return serveProject

#拷贝单个文件
def myCopyOneFile(temp_file, remote_dir, type_file):
    temp_file = os.path.abspath(temp_file)
    remote_dir = os.path.abspath(remote_dir)
    Tnum = len(type_file)
    FNum = temp_file.find(type_file)
    Cfinal_file = remote_dir+temp_file[(FNum+Tnum)::]
    if os.path.isfile(Cfinal_file):
        temp_file_date = os.path.getmtime(temp_file)
        Cfinal_file_date = os.path.getmtime(Cfinal_file)
        if temp_file_date == Cfinal_file_date:
            return Cfinal_file
    CNum = Cfinal_file.rfind('\\')
    CCopy_file = Cfinal_file[:CNum]
    myCopyFile(temp_file, CCopy_file)
    return Cfinal_file

#拷贝所有file节点的文件并改变节点
def myCopyType_Files(serveProject):
    type_file = 'sourceimages'
    serFileName = os.path.join(serveProject, type_file)
    allfiles = mc.ls(type='file')
    folderType = []
    if allfiles:
        for eachfile in allfiles:
            try:
                texFileName = mc.getAttr('%s.fileTextureName' % eachfile)
            except:
                pass
            else:
                if texFileName.find('${OCTV_PROJECTS}') >= 0:
                    texFileName = texFileName.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                texFileName = os.path.normpath(texFileName)
                texFileNameRL = []
                texFileNameL = texFileName.split('\\')
                texFileNameRL += texFileNameL
                texFileNameRL.reverse()
                indexType = texFileNameRL.index('sourceimages')
                serLastFileName = '\\'.join(texFileNameL[-indexType::])
                serFinalFilePath = os.path.join(serFileName, serLastFileName)
                if texFileName != serFinalFilePath:
                    #在type_file子文件下的文件
                    if indexType > 1:
                        if texFileNameRL[indexType-1] in folderType:
                            pass
                        else:
                            #获取拷贝的文件夹
                            folderType.append(texFileNameRL[indexType-1])
                            folderCD = '\\'.join(texFileNameL[:-indexType+1])
                            serFileFPath = os.path.join(serFileName, texFileNameRL[indexType-1])
                            if folderCD!=serFileFPath:
                                myCopyFile(folderCD, serFileFPath)
                    #在type_file根目录下文件下的文件
                    else:
                        myCopyOneFile(texFileName, serFileName, type_file)
                    #设置路径
                    mc.setAttr('%s.fileTextureName' % eachfile, serFinalFilePath, type='string')

#拷贝所有data节点的文件并改变节点
def myCopy_Data(serveProject):
    type_file = 'data'
    serFileName = os.path.join(serveProject, type_file)
    #是否已经拷贝过文件的标志
    folderType = []
    copDatayflg = False
    allCacheFiles = mc.ls(type='cacheFile')
    if allCacheFiles:
        for eachfile in allCacheFiles:
            try:
                cachePath = mc.getAttr('%s.cachePath' % eachfile)
            except:
                pass
            else:
                if cachePath.find('${OCTV_PROJECTS}') >= 0:
                    cachePath = cachePath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                #当前缓存节点的位置
                cachePath = os.path.normpath(cachePath)
                cachePathS = cachePath.split('\\')
                indexType = cachePathS.index('data')
                lenCache = len(cachePathS)
                serLastCacheName = '\\'.join(cachePathS[indexType+1::])
                #当前缓存节点的服务器地址
                serFinalCachePath = os.path.join(serFileName, serLastCacheName)
                #当前工程缓存的缓存位置
                localCachePath = '\\'.join(cachePathS[:indexType+1])
                if cachePath != serFinalCachePath:
                    if indexType+1 < lenCache:
                        #在type_file子文件下的文件
                        if cachePathS[indexType+1] in folderType:
                            pass
                        else:
                            #获取拷贝的文件夹
                            folderType.append(cachePathS[indexType+1])
                            serFileFPath = os.path.join(serFileName, cachePathS[indexType+1])
                            if cachePath != serFileFPath:
                                myCopyFile(cachePath, serFileFPath)
                    else:
                        if not copDatayflg:
                            mylistDir = os.listdir(localCachePath)
                            for everydir in mylistDir:
                                myDirpath = os.path.join(dir, everydir)
                                if os.path.isfile(myDirpath):
                                    myCopyFile(myDirpath, serFileName)
                            copDatayflg = True
                    mc.setAttr('%s.cachePath' % eachfile, serFileFPath, type='string')


#拷贝某些贴图节点的文件
def myCopy_OtherImages(myShape, mtAttr, serveProject):
    print myShape
    myFilepath = mc.getAttr('%s.%s' % (myShape, mtAttr))
    type_file = 'sourceimages'
    serFileName = os.path.join(serveProject, type_file)
    print myFilepath
    if myFilepath.find('${OCTV_PROJECTS}') >= 0:
        myFilepath = myFilepath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
    #获取文件名
    myFileBaseName = os.path.basename(myFilepath)
    myFinalName = os.path.join(serFileName, myFileBaseName)
    myFilepath = os.path.abspath(myFilepath)
    myFinalName = os.path.abspath(myFinalName)
    if myFilepath.find(myFinalName) < 0:
        myCopyFile(myFilepath, serFileName)
    print '%s.%s' % (myShape, mtAttr),myFinalName
    mc.setAttr('%s.%s' % (myShape, mtAttr), myFinalName, type='string')


def myCopy_ShapeImages(serveProject):
    #检查mentalrayIblShape节点的贴图
    allMrIbShapes = mc.ls(type='mentalrayIblShape')
    if allMrIbShapes:
        msAttr = 'texture'
        for MrSeach in allMrIbShapes:
            myCopy_OtherImages(MrSeach, msAttr, serveProject)
    #检查mentalrayTexture节点的贴图
    allMrTxShapes = mc.ls(type='mentalrayTexture')
    if allMrTxShapes:
        mtAttr = 'fileTextureName'
        for MrTeach in allMrTxShapes:
            if not myCopy_OtherImages(MrTeach, mtAttr, serveProject):
                break
    #检查摄像机投影贴图
    allCaImShapes = mc.ls(type='imagePlane')
    if allCaImShapes:
        ciAttr = 'imageName'
        for CaIeach in allCaImShapes:
            if not myCopy_OtherImages(CaIeach, ciAttr, serveProject):
                break


def main():
    serveProject = myCreateScenes()
    myCopyType_Files(serveProject)
    myCopy_Data(serveProject)
    myCopy_ShapeImages(serveProject)


FCOPY_SPATH = getCopyPath()
main()


