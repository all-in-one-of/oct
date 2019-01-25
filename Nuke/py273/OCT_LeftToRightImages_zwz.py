# *-* coding: utf-8 *-*

import nuke
import os


def changePath_zwz(readNode):
    oldpath = readNode.knob('file').value()
    baseN = os.path.basename(oldpath).split('.')[0]
    ppList = oldpath.split('/')
    if (ppList[-1].find('camL') >= 0) and (ppList[-2].find('camL') >= 0):
        ppList[-1] = ppList[-1].replace('camL', 'camR')
        ppList[-2] = ppList[-2].replace('camL', 'camR')
        sign = '/'
        newpath = sign.join(ppList)
        return newpath
    elif (ppList[-1].find('cam_L') >= 0) and (ppList[-2].find('cam_L') >= 0):
        ppList[-1] = ppList[-1].replace('cam_L', 'cam_R')
        ppList[-2] = ppList[-2].replace('cam_L', 'cam_R')
        sign = '/'
        newpath = sign.join(ppList)
        return newpath
    elif (ppList[-1].find('camL') >= 0) and (ppList[-2].upper() == 'L'):
        ppList[-1] = ppList[-1].replace('camL', 'camR')
        ppList[-2] = ppList[-2].replace('L', 'R')
        sign = '/'
        newpath = sign.join(ppList)
        return newpath
    elif (ppList[-1].find('cam_L') >= 0) and (ppList[-2].upper() == 'L'):
        ppList[-1] = ppList[-1].replace('cam_L', 'cam_R')
        ppList[-2] = ppList[-2].replace('L', 'R')
        sign = '/'
        newpath = sign.join(ppList)
        return newpath
    else:
        readNode.setSelected(1)
        sign = '/'
        newpath = sign.join(ppList[0:-1])
        return False


def do_LeftToRightImages_zwz():
    ErrorV = 0
    flagR = 0
    nuke.selectAll()
    AllNode = nuke.selectedNodes()
    for donode in AllNode:
        donode.setSelected(0)
    for donode in AllNode:
        if donode.Class() == 'Read':
            flagR += 1
            path = changePath_zwz(donode)
            if path:
                donode.knob('file').setValue(path)
            else:
                ErrorV = 1
    if flagR:
        if ErrorV:
            nuke.message('Warning：\n1、Please check the existence of the right eye frame material\n2、Please check whether the correct naming material (containing camL)')
    else:
        nuke.message('No material!')
