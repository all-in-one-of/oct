import maya.cmds as mc
import os
import sys


def octvGetCurrentProject(shortNameList):
    projectName = ''
    #判断按个区域：深圳
    OFFICE_LOCATION = mm.eval('getenv "STUDIO_LOCATION"')
    OCTV_PROJECTS = mm.eval('getenv "OCTV_PROJECTS"')
    octvProjects = os.listdir(OCTV_PROJECTS)
    if OFFICE_LOCATION:
        myproject = shortNameList[0]
        if myproject:
            for item in octvProjects:
                if item.upper() == myproject.upper():
                    projectName = item
    return projectName


def zwGetAssetType(shortNameList):
    typePath = ''
    if shortNameList[1][:2].lower() == 'sc':
        typePath = 'animation'
    elif shortNameList[1][:2].lower() == 'ch':
        typePath = 'characters'
    elif shortNameList[1][:2].lower() == 'pr':
        typePath = 'props'
    elif shortNameList[1][:2].lower() == 'se':
        typePath = 'sets'
    return typePath


def zwGetMode(shortNameList):
    model = ''
    if 'mo' in shortNameList:
        model = 'model'
    elif 'msAnim' in shortNameList or 'msCache' in shortNameList:
        model = 'master'
    elif 'rg' in shortNameList:
        model = 'rigging'
    elif 'mt' in shortNameList:
        model = 'morph'
    elif 'al' in shortNameList:
        model = 'action'
    elif 'dy' in shortNameList:
        model = 'dynamic'
    elif 'tx' in shortNameList:
        model = 'texture'
    elif 'ly' in shortNameList:
        model = 'layout'
    elif 'an' in shortNameList:
        model = 'anim'
    elif 'sm' in shortNameList:
        model = 'simulation'
    elif 'cd' in shortNameList:
        model = 'crowd'
    elif 'cc' in shortNameList:
        model = 'cache'
    elif 'fx' in shortNameList:
        model = 'effect'
    elif 'rd' in shortNameList:
        model = 'render'
    return model

if __name__ == "__main__":
    #获取项目目录
    OCTV_PROJECTS = mm.eval('getenv "OCTV_PROJECTS"')
    fileName = mc.file(q=True, sn=True)
    shortName = mc.file(q=True, sn=True, shn=True)
    shortNameList = shortName.split('_')
    #上传后的文件名
    upfileName = ''
    #上传目录
    destFolder = ''
    #上传贴图目录
    destMapFolder = ''

    if fileName:
        result = mc.confirmDialog(message=u"Checkin之前必须存盘，是否确定继续？", button=["Yes", "No"], defaultButton='Yes', cancelButton='No', dismissString='No')
        if result == "No":
            pass
            #return
    else:
        mc.error(u'请先保存文件')

    project = octvGetCurrentProject(shortNameList)
    if not project:
        mc.error(u"文件名不匹配运行中项目")
        # return
    asset_type = zwGetAssetType(shortNameList)
    mode = zwGetMode(shortNameList)
    buf = []
    #判别Asset文件类型
    numShortName = len(shortNameList)
    if asset_type == "characters" or asset_type == "props" or asset_type == "sets":
        if (numShortName == 4 or numShortName == 5) and mode:
            idName = shortNameList[1]
            upfilename = shortNameList[0]+'_'+shortNameList[1]+'_'+shortNameList[2]+'_'+shortNameList[3]
            destFolder = '%s/%s/Project/scenes/%s/%s/%s' % (OCTV_PROJECTS, project, asset_type, idName, mode)
            destMapFolder = '%s/%s/Project/sourceImages/%s/%s' % (OCTV_PROJECTS, project, asset_type, idName)
        else:
            mc.error(u"文件命名错误，正确的名字格式为：项目名_编号名_h/l_环节名_版本(可忽略)，例如 JMWC_ch001001GirlSmall_h_rg_001.mb")
    else:
        #判别当为Animation文件时
        if mode:
            if (numShortName >= 4 or numShortName <= 6) and mode:
                sceneNum = shortNameList[1]
                shortNum = shortNameList[2]
                ext = os.path.splitext(shortNameList[-1])[-1]
                testName = shortNameList[3]
                if testName[:2] == 'ly' or testName[:2] == 'an' or testName[:2] == 'sm' or testName[:2] == 'cd' or testName[:2] == 'cc' or testName[:2] == 'fx' or testName[:2] == 'rd':
                    upfileName = '%s_%s_%s_%s' % (shortNameList[0], shortNameList[1], shortNameList[2], shortNameList[3])
                else:
                    testName = shortNameList[4]
                    if testName[:2] == 'ly' or testName[:2] == 'an' or testName[:2] == 'sm' or testName[:2] == 'cd' or testName[:2] == 'cc' or testName[:2] == 'fx' or testName[:2] == 'rd':
                        upfileName = '%s_%s_%s_%s_%s' % (shortNameList[0], shortNameList[1], shortNameList[2], shortNameList[3], shortNameList[4])
                    else:
                        mc.error(u"文件命名错误，正确的名字格式为：项目名_场景号_镜头号_描述字段_环节_版本(可忽略)，例如 JMWC_sc10_sh02_fight_an_002.mb")
                destFolder = '%s/%s/Project/scenes/animation/%s/%s/%s' % (OCTV_PROJECTS, project, sceneNum, shortNum, mode)
                fList = os.listdir(r'%s' % destFolder)
                numfList = len(fList)
                if numfList:
                    newver = numfList + 1
                    padding = 3
                    newNum = "%.3d" % (newver)
                    upfilename = '%s_c%s%s' % (upfileName, newNum, ext)
                else:
                    upfilename = '%s_c001%s' % (upfileName, ext)
                    #打印上传文件名字
                print '\nupfilename:%s' % upfilename
                destMapFolder = '%s/%s/Project/sourceimages/animation/%s/%s/maps' % (OCTV_PROJECTS, project, sceneNum, shortNum)
            else:
                mc.error(u"文件命名错误，正确的名字格式为：项目名_场景号_镜头号_描述字段(可忽略)_环节_版本(可忽略)，例如 JMWC_sc10_sh02_fight_an_002.mb")
        else:
            mc.error(u"文件命名错误，请根据环节正确命名后再Checkin")
    if not os.path.isdir(destFolder):
        mc.error(u"找不到对应编号目录，请检查文件名或联系PA")
    if not os.path.isdir(destMapFolder):
        mc.error(u"找不到对应编号目录，请检查文件名或联系PA")