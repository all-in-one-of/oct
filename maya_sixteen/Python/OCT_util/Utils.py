# coding=utf-8


#　　　　　　　　┏┓　　　┏┓+ +
#　　　　　　　┏┛┻━━━┛┻┓ + +
#　　　　　　　┃　　　　　　　┃ 　
#　　　　　　　┃　　　━　　　┃ ++ + + +
#　　　　　　 ████━████ ┃+
#　　　　　　　┃　　　　　　　┃ +
#　　　　　　　┃　　　┻　　　┃
#　　　　　　　┃　　　　　　　┃ + +
#　　　　　　　┗━┓　　　┏━┛
#　　　　　　　　　┃　　　┃　　　　　　　　　　　
#　　　　　　　　　┃　　　┃ + + + +
#　　　　　　　　　┃　　　┃　　　　神兽威武，心想事成
#　　　　　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
#　　　　　　　　　┃　　　┃              made in fuck
#　　　　　　　　　┃　　　┃　　+　　　　　　　　　
#　　　　　　　　　┃　 　　┗━━━┓ + +
#　　　　　　　　　┃ 　　　　　　　┣┓
#　　　　　　　　　┃ 　　　　　　　┏┛
#　　　　　　　　　┗┓┓┏━┳┓┏┛ + + + +
#　　　　　　　　　　┃┫┫　┃┫┫
#　　　　　　　　　　┗┻┛　┗┻┛+ + + +


#------------------------------
# 常用函数集
#------------------------------

import maya.cmds as mc
import shutil
import os
import re


#--------------------------------------------------------------------------------------
# 函数功能：判断是否是序列贴图
# 函数参数：输入为文件名
# 函数说明：序列贴图命名只能为 fileName.sequence.ext 格式（例如zhangsan.0001.jpg）
#--------------------------------------------------------------------------------------
def IsSequenceFile(fileName):
    # 按‘.’切分，有3个的则为序列贴图
    fileName_Split = fileName.split('.')
    if len(fileName_Split) == 3:
        return 1


#--------------------------------------------------------------------------------------
# 函数功能：返回序列贴图文件名和路径
# 函数参数：带路径的完整文件名，是否是序列
# 函数说明：通过序列的读取及查找序列前部分同样名称的文件来确定文件的完整所有路径
# 返回值为字典，格式为 {文件名称：完整路径}， 如果不是序列则返回空字典
#--------------------------------------------------------------------------------------
def Get_Sequence_File(filePath, isSeq = 1):
    (dirAddr, fileName) = os.path.split(filePath)
    fileDict = {fileName : filePath}  # 需要返回的字典
    
    # 判断文件是否为序列文件
    if not isSeq:
        return fileDict   # 空字典

    # 按'.'切割文件名称
    fileName_Split = fileName.split('.')  # 切割后的变量
    
    # 列出文件夹内所有文件，然后根据序列前的文件名查找所有含此名称的文件数量
    dir_file_num = 0  # 文件夹内包含名称的文件数量
    fileList = os.listdir(dirAddr)
    for name in fileList:
        if name == fileName:
            continue
        if fileName_Split[0] in name:
            name_Split = name.split('.')
            rule = re.match('^\d+$', name_Split[1])
            if rule:
                path = os.path.join(dirAddr, name)
                fileDict[name] = path

    return fileDict


#--------------------------------------------------------------------------------------
# 函数功能：复制序列贴图
# 函数参数：带路径的完整文件名，新路径，复制模式（只有复制和移动2种模式）
# 函数说明：序列贴图命名只能为 fileName.sequence.ext 格式（例如zhangsan.0001.jpg）
# 检查整个场景中的file节点 再检查useFrameExtension或者uvTilingMode属性的值
# 如果是序列则启用， 不是则跳过
# 本函数不做改路径功能，如需改路径可自行添加
# 本函数为辅助 FileTextureManager.mel 这个脚本使用
#--------------------------------------------------------------------------------------
def Copy_Sequence_Texture_File(newDir, mode):
    fileNode_List = mc.ls(typ=('file','psdFileTex','mentalrayTexture'))
    if not os.path.exists(newDir):
        os.makedirs(newDir)
    for fileNode in fileNode_List:
        isSep = 0
        if mc.attributeQuery('useFrameExtension', node = fileNode, ex=True):
           if mc.getAttr('%s.useFrameExtension' %fileNode):
               isSep = 1
        if mc.attributeQuery('uvTilingMode', node = fileNode, ex=True):
           if (mc.getAttr('%s.uvTilingMode' %fileNode) == 3):
               isSep = 1
        if isSep:
            oldFilePath = mc.getAttr('%s.fileTextureName' %fileNode)
            if not os.path.exists(oldFilePath):
                mc.warning('%s is not exist! node %s' %(oldFilePath, fileNode))
                continue
            fileDict = Get_Sequence_File(oldFilePath)
            if mode == 'copy':
                for fileName, filePath in fileDict.items():
                    filePath_new = os.path.join(newDir, fileName)
                    shutil.copy2(filePath, filePath_new)
            elif mode == 'move':
                for fileName, filePath in fileDict.items():
                    filePath_new = os.path.join(newDir, fileName)
                    shutil.move(filePath, filePath_new)

