#!/usr/bin/env python
# coding=utf-8

import maya.cmds as cmds
def maya_came():
    cmds.cycleCheck (e=0)
    stm=cmds.playbackOptions( q=True,minTime=True) 
    etm=cmds.playbackOptions( q=True,maxTime=True)
    timRg=etm-stm+1
    cames=cmds.ls( sl=True )
    cmds.polyCube(name='locS_') 
    cmds.delete('locS_*')

    localS=[]

    for i in cames:
        loco1=cmds.spaceLocator(name=i)
        loco1New=cmds.rename('locS_'+loco1[0])
        cmds.addAttr( longName='FlimOffset', attributeType='double2' )
        cmds.addAttr( longName='XX', attributeType='double', parent='FlimOffset' )
        cmds.addAttr( longName='YY', attributeType='double', parent='FlimOffset' )
        cmds.addAttr( longName='focal', attributeType='float' )
        cmds.addAttr( longName='view', attributeType='float' )
        cmds.addAttr( longName='hF', attributeType='float' )
        cmds.addAttr( longName='ox', attributeType='float' )
        cmds.addAttr( longName='oy', attributeType='float' )
        localS.append(loco1New)




    for i2 in range(0,int(timRg+1),1):
        cons=0
        for i3 in cames:
            cmds.select(i3)
            caT=cmds.xform(q=1,ws=1,t=1)
            caR=cmds.xform(q=1,ws=1,ro=1)
            hfa=cmds.camera(i3, q=True,  hfa=True)
            vfa=cmds.camera(i3, q=True,  vfa=True)
            hfo=cmds.camera(i3, q=True,  hfo=True)
            vfo=cmds.camera(i3, q=True,  vfo=True)
            horHo=hfo/hfa 
            vorHo=vfo/hfa
            cFL = cmds.camera(cames[cons], q=True, fl=True)
            view = cmds.camera(cames[cons], q=True, hfv=True)
            hfa = cmds.camera(cames[cons], q=True, hfa=True)
            cmds.setAttr(localS[cons]+'.XX', (horHo*-1) )
            cmds.setAttr(localS[cons]+'.YY', (vorHo*-1) )
            cmds.setAttr(localS[cons]+'.focal',cFL)
            cmds.setAttr(localS[cons]+'.view',view)
            cmds.setAttr(localS[cons]+'.hF',hfa)
            cmds.setAttr(localS[cons]+'.ox',hfo)
            cmds.setAttr(localS[cons]+'.oy',vfo)
            cmds.setAttr(localS[cons]+'.tx',caT[0])
            cmds.setAttr(localS[cons]+'.ty',caT[1])
            cmds.setAttr(localS[cons]+'.tz',caT[2])
            cmds.setAttr(localS[cons]+'.rx',caR[0])
            cmds.setAttr(localS[cons]+'.ry',caR[1])
            cmds.setAttr(localS[cons]+'.rz',caR[2])
            cmds.setKeyframe(localS[cons], at='XX')
            cmds.setKeyframe(localS[cons], at='YY' )
            cmds.setKeyframe(localS[cons], at='focal' )
            cmds.setKeyframe(localS[cons], at='view' )
            cmds.setKeyframe(localS[cons], at='hF' )
            cmds.setKeyframe(localS[cons], at='ox' )
            cmds.setKeyframe(localS[cons], at='oy' )
            cmds.setKeyframe(localS[cons], at='rz' )
            cmds.setKeyframe(localS[cons], at='tx' )
            cmds.setKeyframe(localS[cons], at='ty' )
            cmds.setKeyframe(localS[cons], at='tz' )
            cmds.setKeyframe(localS[cons], at='rx' )
            cmds.setKeyframe(localS[cons], at='ry' )
            cmds.setKeyframe(localS[cons], at='rz' )
            cons=cons+1
        cmds.currentTime(stm+i2)
    cmds.currentTime(stm)          