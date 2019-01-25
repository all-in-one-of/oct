# -*- coding: UTF-8 -*-
#拷贝nuke工程文件特效素材到目标盘，除了盘符不一样，其它路径均一样，并另存文件。
import nuke
import nukescripts
import os
import shutil
import ctypes
import platform
import sys
import threading
import time
import subprocess
from os.path import join, getsize

#print "获取文件路径及另存"

OCT_DRIVE = r'\\octvision.com\cg'
CPAU_PATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
REMOTE_USER = r'octvision.com\supermaya'
REMOTE_PWD = 'supermaya'
FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\FastCopy341\FastCopy.exe'


# 获取文件路径及另存

#def __init__(self):
allReadNodes = []
VFXReadNodes = []
copyNode = []

class ModalPanel( nukescripts.PythonPanel ):
    
    def __init__( self ):
        nukescripts.PythonPanel.__init__( self, "请输入目标盘符", "uk.co.thefoundry.FramePanel" )
        self.target_drive = nuke.String_Knob( "target_drive", "targetDrive:" )
        self.addKnob( self.target_drive )
        self.target_drive.setValue('M')
        self.okButton = nuke.Script_Knob( "OK" )
        #self.okButton.setCommand(copy_CompAndSequence())
        self.addKnob( self.okButton )
        self.okButton.setFlag(nuke.STARTLINE)
        self.cancelButton = nuke.Script_Knob( "Cancel" )
        self.addKnob( self.cancelButton )

    def showModalDialog( self ):
        result = nukescripts.PythonPanel.showModalDialog( self )
        if result:
            if len(self.target_drive.getValue()) == 1:
                return self.target_drive.getValue()
            else:
                nuke.message("输入的盘符有误，请检查.....")
                return

def copy_CompAndSequence():
    panelStr = ModalPanel().showModalDialog()
    target_drive = panelStr.upper() + ":"
    comp_dirpath = os.path.dirname(nuke.value("root.name"))
    comp_name = os.path.basename(nuke.value("root.name"))
    old_dirpath = comp_dirpath.split(":")[1]
    bkp_dirpath = target_drive + old_dirpath

    # 获取所以Read节点
    for allNode in nuke.allNodes():
        if allNode.Class() == "Read":
            allReadNodes.append(allNode.name())

        # 获取所以VFXRead节点
    for getNodeFile in allReadNodes:
        readFileInput = nuke.toNode(getNodeFile)["file"].getValue().split("/")
        if "VFX" in readFileInput:
            VFXReadNodes.append(getNodeFile)

        # 获取所以VFXRead节点素材路径
    for VFXReadNode in VFXReadNodes:
        sourceVFXreadFileDir = os.path.dirname(nuke.toNode(VFXReadNode)["file"].getValue())
        sourceVFXreadFileName = os.path.basename(nuke.toNode(VFXReadNode)["file"].getValue())
        source_drive = sourceVFXreadFileDir.split(":")[0]
        sourceVFXreadDir = sourceVFXreadFileDir.split(":")[1]
        targetVFXDir = target_drive + sourceVFXreadDir
        #目标盘为M盘，所以暂时放弃硬盘空间判断。
        #filesize = getdirsize(sourceVFXreadFileDir)
        #disksize = get_free_space_mb(target_drive)

        if not os.path.exists(targetVFXDir):
            os.makedirs(targetVFXDir)
        
        if (source_drive.upper() == "W"):
            source_dir = sourceVFXreadFileDir.replace("/", "\\").replace("W:","\\\\file.com\\share")
        elif (source_drive.upper() == "S"):
            source_dir = sourceVFXreadFileDir.replace("/", "\\").replace("S:","\\\\192.168.90.199\\render90199\\VFX")
        elif (source_drive.upper() == "X"):
            source_dir = sourceVFXreadFileDir.replace("/", "\\").replace("X:","\\\\192.168.80.201\\share\\VFX")
        else:
            source_dir = sourceVFXreadFileDir.replace("/", "\\")
        
        if (ord(panelStr) > 71):   
            target_dir = targetVFXDir.replace("/", "\\").replace("M:","\\\\file2.com\\share")
        else:
            target_dir = targetVFXDir.replace("/", "\\")
        
        if True:
        #if ((disksize - filesize) >= 0):
            cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE \"%s\" /to=\"%s\""' % (CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_SPATH, source_dir,target_dir)
            #threading.Thread(None, copyVFXNukeFile().Destruct(source_dir,target_dir,VFXReadNode)).start()
            if cmd:
                #print "....................a..................."
                p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
                #threading.Thread(None, Destruct(source_dir,target_dir,VFXReadNode)).start()
            while True:
                if not p.poll() is None:
                    del p
                    break
           
        #shutil.copytree(source_dir,target_dir)
            copyNode.append(VFXReadNode)
        else:
           nuke.message('目标硬盘空间不足....')
        
        newSequencePath = targetVFXDir + '/' + sourceVFXreadFileName
        setVFXreadFile = nuke.toNode(VFXReadNode)["file"].setValue(newSequencePath)

    copyNum = str(len(copyNode))
    allNum = str(len(VFXReadNodes))
    nuke.message("成功复制 %s 个节点，共需要复制 %s 个节点。" % (copyNum, allNum))

    #文件另存
    if not os.path.exists(bkp_dirpath):
        os.makedirs(bkp_dirpath)
    #shutil.copytree(comp_dirpath, bkp_dirpath)
    nuke.scriptSaveAs((bkp_dirpath + '/' + comp_name), overwrite=1) 

# 获取序列大小
def getdirsize(dir):
    size = 0L
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size / 1024 / 1024


# 获取磁盘剩余空间
def get_free_space_mb(folder):
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 - 50
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize / 1024 / 1024


def Destruct(sourceDir,targetDir,obj):
    copyDate = getdirsize(targetDir)
    allData = getdirsize(sourceDir)
    task = nuke.ProgressTask("copying......")
    task.setMessage(obj)
    while (copyDate < allData):
        if task.isCancelled():
            nuke.executeInMainThread( nuke.message, args=( "确定中断复制！！！" ) )
            break
        task.setProgress(copyDate / allData * 100)
        time.sleep(1)
        copyDate = copyVFXNukeFile().getdirsize(targetDir)




