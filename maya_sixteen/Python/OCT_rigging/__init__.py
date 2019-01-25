#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om

def JointConversion():
    allSelectObjs = mc.ls(sl = True)
    if len(allSelectObjs) != 2 or mc.objectType(allSelectObjs[0]) != "joint":
        mc.confirmDialog(message = u"请先选择骨骼组，再选择控制的曲线组")
        return

    #拷贝骨骼并且重新命名skin
    mc.select(d = True)
    mc.select(allSelectObjs[0],r = True)
    CopyJointName = mc.duplicate(rr = True)
    mc.parent(CopyJointName, w=True)
    groupNameSkin = mc.rename(CopyJointName, "Root_skin")
    mc.select(d = True)
    mc.select(groupNameSkin,r = True)

    allSelectJoints = mc.ls(sl = True, dag=True,type="joint")
    listJoints = allSelectJoints

    i = 0
    
    while len(listJoints)>0:
        if i == 0:
            newName = listJoints[0].split("|")[-1]
            if newName == groupNameSkin:
                listJoints.remove(listJoints[0])
                continue
            newName = newName + "_skin"
            mc.rename(listJoints[0], newName)
            name = listJoints[0]
            listJoints.remove(listJoints[0])
            for j in range(len(listJoints)):
                if name in listJoints[j]:
                    temName = listJoints[j].replace(name, newName)
                    listJoints[j] = temName
            i=i+1
        else:
            newName = listJoints[0].split("|")[-1]
            if newName == groupNameSkin:
                listJoints.remove(listJoints[0])
                continue
            newName = newName +"_skin"
            mc.rename(listJoints[0], newName)
            name = listJoints[0]
            listJoints.remove(listJoints[0])
            for j in range(len(listJoints)):
                if name in listJoints[j]:
                    temName = listJoints[j].replace(name,newName)
                    listJoints[j] = temName
            i=i+1

    #拷贝骨骼并且重新命名mc骨骼
    mc.select(d = True)
    mc.select(allSelectObjs[0],r = True)
    CopyJointName = mc.duplicate(rr = True)
    mc.parent(CopyJointName, w=True)
    groupNameMC = mc.rename(CopyJointName, "Hips")
    mc.select(d = True)
    mc.select(groupNameMC,r = True)

    allSelectJoints = mc.ls(sl = True, dag=True,type="joint")
    listJoints = allSelectJoints
    print groupNameMC

    i=0
    while len(listJoints)>0:
        if i == 0:
            newName = JointMcName(listJoints[0])
            if not newName:
                listJoints.remove(listJoints[0])
                continue
            #newName = listJoints[0].split("|")[-1]
            #newName = newName+"_skin"
            mc.rename(listJoints[0], newName)
            name = listJoints[0]
            listJoints.remove(listJoints[0])
            for j in range(len(listJoints)):
                if name in listJoints[j]:
                    temName = listJoints[j].replace(name, newName)
                    listJoints[j] = temName
            i=i+1
        else:
            # newName = listJoints[0].split("|")[-1]
            # newName = newName +"_skin"
            newName = JointMcName(listJoints[0])
            if not newName:
                listJoints.remove(listJoints[0])
                continue
            mc.rename(listJoints[0], newName)
            name = listJoints[0]
            listJoints.remove(listJoints[0])
            for j in range(len(listJoints)):
                if name in listJoints[j]:
                    temName = listJoints[j].replace(name,newName)
                    listJoints[j] = temName
            i=i+1

    mc.select(d = True)
    mc.select(groupNameSkin,r = True)
    allSelectPointCons = mc.ls(sl = True, dag=True,type=['pointConstraint', 'parentConstraint', 'orientConstraint', 'tangentConstraint', 'aimConstraint','scaleConstraint'])
    for sel in allSelectPointCons:
        mc.delete(sel)

    mc.select(d = True)
    mc.select(groupNameMC,r = True)
    allSelectPointCons = mc.ls(sl = True, dag=True,type=['pointConstraint', 'parentConstraint', 'orientConstraint', 'tangentConstraint', 'aimConstraint','scaleConstraint'])
    for sel in allSelectPointCons:
        mc.delete(sel)

    mc.select(d=True)
    mc.select(allSelectObjs[0], add = True)
    mc.select(groupNameMC, add = True)
    mc.select(groupNameSkin, add = True)
    parentConstraintName = mc.parentConstraint(mo = True, weight = 1)
    reverseName = mc.shadingNode("reverse", asUtility = True)
    try:
        mc.addAttr(allSelectObjs[1], ln = "mc_k", at = "double", min = 0, max = 1, dv = 0)
        mc.setAttr("%s.mc_k"%allSelectObjs[1], e = True, keyable = True)
    except:
        om.MGlobal.displayError(u'已存在%s.mc_k属性' % allSelectObjs[1])

    groupName1 = groupNameMC.split("|")[-1]
    groupName2 = allSelectObjs[0].split("|")[-1]
    try:
        mc.connectAttr("%s.mc_k"%allSelectObjs[1], "%s.%sW0"%(parentConstraintName[0], groupName2))
        mc.connectAttr("%s.outputX"%reverseName, "%s.%sW1"%(parentConstraintName[0], groupName1))
        mc.connectAttr("%s.mc_k"%allSelectObjs[1], "%s.inputX"%reverseName)
    except:
        om.MGlobal.displayError(u'属性连接出错！')

    parentGroup = mc.listRelatives(allSelectObjs[0], p = True)
    if parentGroup:
        mc.select(d = True)
        mc.select(groupNameSkin, add = True)
        mc.select(parentGroup[0], add = True)
        mc.parent()

    locatorName = mc.createNode('locator')
    locatorNameTran = mc.listRelatives(locatorName, p = True)
    NewLocatorName = mc.rename(locatorNameTran, "Reference")
    mc.select(d=True)
    mc.select(groupNameMC, add = True)
    mc.select(NewLocatorName, add = True)
    mc.parent()

    longName = mc.ls(allSelectObjs[0],long =True)
    if longName:
        buf = longName[0].split("|")
        while '' in buf:
            buf.remove('')
        mc.select(d=True)
        mc.select(NewLocatorName, add = True)
        mc.select(buf[0], add = True)
        mc.parent()

def JointMcName(name):
    oldName = name.split("|")[-1]
    newName = ""
    if oldName == "Spine1_M":
        newName = "Spine"
    elif oldName == "Spine2_M":
        newName = "Spine1"
    elif oldName == "Spine3_M":
        newName = "Spine2"

    elif oldName == "Chest_M":
        newName = "Spine3"

    elif oldName == "Scapula_R":
        newName = "RightShoulder"
    elif oldName == "Shoulder_R":
        newName = "RightArm"
    elif oldName == "ShoulderPart1_R":
        newName = "RightArmRoll"
    elif oldName == "Elbow_R":
        newName = "RightForeArm"
    elif oldName == "ElbowPart1_R":
        newName = "RightForeArmRoll"
    elif oldName == "Wrist_R":
        newName = "RightHand"

    elif oldName == "MiddleFinger1_R":
        newName = "RightHandMiddle1"
    elif oldName == "MiddleFinger2_R":
        newName = "RightHandMiddle2"
    elif oldName == "MiddleFinger3_R":
        newName = "RightHandMiddle3"
    elif oldName == "MiddleFinger4_R":
        newName = "RightHandMiddle4"

    elif oldName == "ThumbFinger1_R":
        newName = "RightHandThumb1"
    elif oldName == "ThumbFinger2_R":
        newName = "RightHandThumb2"
    elif oldName == "ThumbFinger3_R":
        newName = "RightHandThumb3"
    elif oldName == "ThumbFinger4_R":
        newName == "RightHandMiddle4"

    elif oldName == "IndexFinger1_R":
        newName = "RightHandIndex1"
    elif oldName == "IndexFinger2_R":
        newName = "RightHandIndex2"
    elif oldName == "IndexFinger3_R":
        newName = "RightHandIndex3"
    elif oldName == "IndexFinger4_R":
        newName = "RightHandIndex4"

    elif oldName == "PinkyFinger1_R":
        newName = "RightHandPinky1"
    elif oldName == "PinkyFinger2_R":
        newName = "RightHandPinky2"
    elif oldName == "PinkyFinger3_R":
        newName = "RightHandPinky3"
    elif oldName == "PinkyFinger4_R":
        newName = "RightHandPinky4"

    elif oldName == "RingFinger1_R":
        newName = "RightHandRing1"
    elif oldName == "RingFinger2_R":
        newName = "RightHandRing2"
    elif oldName == "RingFinger3_R":
        newName = "RightHandRing3"
    elif oldName == "RingFinger4_R":
        newName = "RightHandRing4"

    elif oldName == "Neck_M":
        newName = "Neck"
    elif oldName == "NeckPart1_M":
        newName = "Neck1"
    elif oldName == "Head_M":
        newName = "Head"

    elif oldName == "Scapula_L":
        newName = "LeftShoulder"
    elif oldName == "Shoulder_L":
        newName = "LeftArm"
    elif oldName == "ShoulderPart1_L":
        newName = "LeftArmRoll"
    elif oldName == "Elbow_L":
        newName = "LeftForeArm"
    elif oldName == "ElbowPart1_L":
        newName = "LeftForeArmRoll"
    elif oldName == "Wrist_L":
        newName = "LeftHand"

    elif oldName == "MiddleFinger1_L":
        newName = "LeftHandMiddle1"
    elif oldName == "MiddleFinger2_L":
        newName = "LeftHandMiddle2"
    elif oldName == "MiddleFinger3_L":
        newName = "LeftHandMiddle3"
    elif oldName == "MiddleFinger4_L":
        newName = "LeftHandMiddle4"

    elif oldName == "ThumbFinger1_L":
        newName = "LeftHandThumb1"
    elif oldName == "ThumbFinger2_L":
        newName = "LeftHandThumb2"
    elif oldName == "ThumbFinger3_L":
        newName = "LeftHandThumb3"
    elif oldName == "ThumbFinger4_L":
        newName == "LeftHandMiddle4"

    elif oldName == "IndexFinger1_L":
        newName = "LeftHandIndex1"
    elif oldName == "IndexFinger2_L":
        newName = "LeftHandIndex2"
    elif oldName == "IndexFinger3_L":
        newName = "LeftHandIndex3"
    elif oldName == "IndexFinger4_L":
        newName = "LeftHandIndex4"

    elif oldName == "PinkyFinger1_L":
        newName = "LeftHandPinky1"
    elif oldName == "PinkyFinger2_L":
        newName = "LeftHandPinky2"
    elif oldName == "PinkyFinger3_L":
        newName = "LeftHandPinky3"
    elif oldName == "PinkyFinger4_L":
        newName = "LeftHandPinky4"

    elif oldName == "RingFinger1_L":
        newName = "LeftHandRing1"
    elif oldName == "RingFinger2_L":
        newName = "LeftHandRing2"
    elif oldName == "RingFinger3_L":
        newName = "LeftHandRing3"
    elif oldName == "RingFinger4_L":
        newName = "LeftHandRing4"

    elif oldName == "Hip_R":
        newName = "RightUpLeg"
    elif oldName == "HipPart1_R":
        newName = "RightUpLegRoll"
    elif oldName == "Knee_R":
        newName = "RightLeg"
    elif oldName == "KneePart1_R":
        newName = "RightLegRoll"
    elif oldName == "Ankle_R":
        newName = "RightFoot"
    elif oldName == "Toes_R":
        newName = "RightToeBase"
    elif oldName == "ToesEnd_R":
        newName = "RightToeEnd"

    elif oldName == "Hip_L":
        newName = "LeftUpLeg"
    elif oldName == "HipPart1_L":
        newName = "LeftUpLegRoll"
    elif oldName == "Knee_L":
        newName = "LeftLeg"
    elif oldName == "KneePart1_L":
        newName = "LeftLegRoll"
    elif oldName == "Ankle_L":
        newName = "LeftFoot"
    elif oldName == "Toes_L":
        newName = "LeftToeBase"
    elif oldName == "ToesEnd_L":
        newName = "LeftToeEnd"
    
    return newName

#修改骨骼的名字
def modifyJointname():
    allSelectObjs = mc.ls(sl = True)
    if len(allSelectObjs) != 1 or mc.objectType(allSelectObjs[0]) != "joint":
        mc.confirmDialog(message = u"请先选择骨骼组")
        return

    mc.select(d = True)
    mc.select(allSelectObjs[0],r = True)
    CopyJointName = mc.duplicate(rr = True)
    mc.parent(CopyJointName, w=True)

    JointName = mc.rename(CopyJointName, "Hips")
    mc.select(d = True)
    mc.select(JointName,r = True)
    allSelectJoints = mc.ls(sl = True, dag=True,type="joint")
    listJoints = allSelectJoints

    mc.select(d = True)
    mc.select(JointName,r = True)
    allSelectPointCons = mc.ls(sl = True, dag=True,type=['pointConstraint', 'parentConstraint', 'orientConstraint', 'tangentConstraint', 'aimConstraint','scaleConstraint'])
    for sel in allSelectPointCons:
        mc.delete(sel)

    i = 0
    while len(listJoints)>0:
        if i == 0:
            newName = JointMcName(listJoints[0])
            if not newName:
                listJoints.remove(listJoints[0])
                continue
            #newName = listJoints[0].split("|")[-1]
            #newName = newName+"_skin"
            mc.rename(listJoints[0], newName)
            name = listJoints[0]
            listJoints.remove(listJoints[0])
            for j in range(len(listJoints)):
                if name in listJoints[j]:
                    temName = listJoints[j].replace(name, newName)
                    listJoints[j] = temName
            i=i+1
        else:
            # newName = listJoints[0].split("|")[-1]
            # newName = newName +"_skin"
            newName = JointMcName(listJoints[0])
            if not newName:
                listJoints.remove(listJoints[0])
                continue
            mc.rename(listJoints[0], newName)
            name = listJoints[0]
            listJoints.remove(listJoints[0])
            for j in range(len(listJoints)):
                if name in listJoints[j]:
                    temName = listJoints[j].replace(name,newName)
                    listJoints[j] = temName
            i=i+1

    parentGroup = mc.listRelatives(JointName, p = True)

    locatorName = mc.createNode('locator')
    locatorNameTran = mc.listRelatives(locatorName, p = True)
    NewLocatorName = mc.rename(locatorNameTran, "Reference")
    mc.select(d=True)
    mc.select(JointName, add = True)
    mc.select(NewLocatorName, add = True)
    mc.parent()

    if parentGroup:
        mc.select(d = True)
        mc.select(NewLocatorName, add = True)
        mc.select(parentGroup[0], add = True)
        mc.parent()

    longName = mc.ls(allSelectObjs[0],long =True)
    if longName:
        buf = longName[0].split("|")
        while '' in buf:
            buf.remove('')
        mc.select(d=True)
        mc.select(NewLocatorName, add = True)
        mc.select(buf[0], add = True)
        mc.parent()
        
#modifyJointname()
#JointConversion()
