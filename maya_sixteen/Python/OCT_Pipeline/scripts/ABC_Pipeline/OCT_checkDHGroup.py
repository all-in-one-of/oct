#coding:utf-8
import maya.cmds as cc
import re

def checkDHGroup():
    DHgroup  = '|DH'
    BGgroup  = '|BG'
    CAMgroup = '|CAM'

    k_re_ch = re.compile(r'^\w+_ch\d+.*')
    k_re_pr = re.compile(r'^\w+_pr\d+.*')

    ErrorMessage = []
    ErrorObjs     = []

    if cc.objExists(DHgroup):
        SubGroups = cc.listRelatives(DHgroup, c=1, f=1)
        for SubGroup in SubGroups:
            # 角色ch
            if cc.ls(SubGroup, sn=1)[0] == 'CHR':
                eachTarGroups = cc.listRelatives(SubGroup, c=1, f=1)
                for eachTarGroup in eachTarGroups:
                    if not k_re_ch.search(cc.ls(eachTarGroup, sn=1)[0]):
                        ErrorObjs.append(cc.ls(eachTarGroup, sn=1)[0])
            # 道具pr
            elif cc.ls(SubGroup, sn=1)[0] == 'PROP':
                eachTarGroups = cc.listRelatives(SubGroup, c=1, f=1)
                for eachTarGroup in eachTarGroups:
                    if not k_re_pr.search(cc.ls(eachTarGroup, sn=1)[0]):
                        ErrorObjs.append(cc.ls(eachTarGroup, sn=1)[0])

            else:
                ErrorMessage.append(u'有不符合规定的组命名在 DH 组里面，不符合规定的组名称为 {}'.format(SubGroup))

    else:
        ErrorMessage.append(u'没有 DH 组')

    if not cc.objExists(BGgroup) : ErrorMessage.append(u'没有 BG 组')
    if not cc.objExists(CAMgroup): ErrorMessage.append(u'没有 CAM 组')

    ErrorMessage = list(set(ErrorMessage))
    ErrorObjs     = list(set(ErrorObjs))
    for ErrorObj in ErrorObjs:
        ErrorMessage.append(u'有错误格式的组命名，错误的组名称为 {}'.format(ErrorObj))

    return ErrorMessage

if __name__ == '__main__':
    a=checkDHGroup()
    for i in a:
        print i