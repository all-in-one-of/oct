# *-* coding: utf-8 *-*
import nuke

def ChckFileOnnet_uui():
    numMyP = 0
    flagR = 0
    nuke.selectAll()
    AllNode = nuke.selectedNodes()
    for donode in AllNode:
        donode.setSelected(0)
    for donode in AllNode:
        if donode.Class() == 'Read':
            flagR += 1
            path = donode.knob('file').value()
            pathLow = path.lower()
            if not(pathLow.find("//192.168") >= 0 or pathLow.find("z:/") >= 0 or pathLow.find("w:/") >= 0 or pathLow.find("//octvision/cg") >= 0 or pathLow.find("//octvision.com/cg") >= 0):
                donode.setSelected(1)
                numMyP += 1
    if flagR:
        if numMyP > 0:
            nuke.message('There are     %s    material in local\nAll local materials had been selected!' % numMyP)
        else:
            nuke.message('OK! \nAll material in SkyDrive')
    else:
        nuke.message('No material!')
