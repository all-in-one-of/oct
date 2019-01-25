# *-* coding=utf-8
__author__ = 'yangh'
import maya.cmds as mc
import string

class OCT_MiaryCopyAnim():
    def __init__(self):
        self.allSelectedGroup = ""
        self.allInputList = []
        self.allInputJointList = []
        self.allOutputJointList = []

    def miaryCopyAnim(self):
        self.allSelectedGroup = mc.ls(sl = True, l = True)
        result = mc.confirmDialog(title=u'提示', message=u'请先选择输入组在选择输出组！', button=['Yes','NO'], defaultButton='Yes', dismissString='No')
        if result == 'NO':
            return
        inputGroup = ""
        outputGroup = []
        if len(self.allSelectedGroup) == 2:
            inputGroup = mc.listRelatives(self.allSelectedGroup[0], c = True, f =True)[0]
            outputGroup = mc.listRelatives(self.allSelectedGroup[1], c = True, f =True)
        else:
            inputGroup = self.allSelectedGroup[0]
            outputGroup = self.allSelectedGroup[1:]

        numObj = len(outputGroup)
        for i in range(numObj):
            if i == numObj-1:
                outputName = mc.listRelatives(outputGroup[i], c = True, f =True)
                outputJoint = ""
                for name in outputName:
                    if mc.objectType(name) == 'joint':
                        outputJoint = name
                if outputJoint:
                    self.allOutputJointList.append(outputJoint)
                else:
                    mc.confirmDialog(title=u'警告', message=u'%s组下面没有joint组，请重新检查再替换'%outputGroup[i], button='OK', defaultButton='Yes', dismissString='No')
                    return
                inputName = mc.listRelatives(inputGroup, c = True, f =True)
                inputJoint = ""
                for name in inputName:
                    if mc.objectType(name) == 'joint':
                        inputJoint = name
                if inputJoint:
                    self.allInputJointList.append(inputJoint)
                else:
                    mc.confirmDialog(title=u'警告', message=u'%s组下面没有joint组，请重新检查再替换'%outputGroup[i], button='OK',  defaultButton='Yes', dismissString='No')
                    return
                break

            mc.select(d = True)
            mc.select(inputGroup)
            inputDupName = mc.duplicate(rr = True, renameChildren=True, un =True)
            self.allInputList.append(inputDupName[0])

            outputName = mc.listRelatives(outputGroup[i], c = True)
            outputJoint = ""
            for name in outputName:
                if mc.objectType(name) == 'joint':
                    outputJoint = name
            if outputJoint:
                self.allOutputJointList.append(outputJoint)
            else:
                mc.confirmDialog(title=u'警告', message=u'%s组下面没有joint组，请重新检查再替换'%outputGroup[i], button='OK', defaultButton='Yes', dismissString='No')
                return

            inputName = mc.listRelatives(inputDupName[0], c = True)
            inputJoint = ""
            for name in inputName:
                if mc.objectType(name) == 'joint':
                    inputJoint = name
            if inputJoint:
                self.allInputJointList.append(inputJoint)
            else:
                mc.confirmDialog(title=u'警告', message=u'%s组下面没有joint组，请重新检查再替换'%outputGroup[i], button='OK', defaultButton='Yes', dismissString='No')
                return
        print self.allOutputJointList
        print self.allInputJointList

        for i in range(len(self.allOutputJointList)):
            #output骨骼的层级关系
            mc.select(d = True)
            mc.select(self.allOutputJointList[i], r = True)
            JointOutDict = {}
            outJointChilds = mc.ls(sl = True, dagObjects = True,type='joint',l=True)

            mc.select(d = True)
            mc.select(self.allInputJointList[i], r = True)
            JointInDict = {}
            inJointChilds = mc.ls(sl = True, dagObjects = True,type='joint',l=True)
            if len(outJointChilds) != len(inJointChilds):
                mc.confirmDialog(title=u'警告', message=u'%s和%s组的骨骼子集不相等，骨骼数量错误，请检查！'%(self.allOutputJointList[i], self.allInputJointList[i]), button='OK', defaultButton='Yes', dismissString='No')
                print(u'%s和%s组的骨骼子集不相等，骨骼数量错误，请检查！'%(self.allOutputJointList[i], self.allInputJointList[i]))
                return
            for j in range(len(outJointChilds)):
                number = len(outJointChilds[j].split('|'))
                number1 = len(inJointChilds[j].split('|'))
                if number != number1:
                    mc.confirmDialog(title=u'警告', message=u'%s和%s层级不相同！'%(outJointChilds[j], inJointChilds[j]), button='OK', defaultButton='Yes', dismissString='No')
                    print(u'%s和%s层级不相同！'%(outJointChilds[j], inJointChilds[j]))
                    return
                animCurves = mc.listConnections(outJointChilds[j], s=True, d=False, plugs = True)
                if animCurves:
                    if not number in JointOutDict.keys():
                        JointOutDict.update({number : [outJointChilds[j]]})
                        JointInDict.update({number : [inJointChilds[j]]})
                    else:
                        JointOutDict[number].append(outJointChilds[j])
                        JointInDict[number].append(inJointChilds[j])

            for j in JointOutDict.keys():
                for k in range(len(JointOutDict[j])):
                    animCurves = mc.listConnections(JointOutDict[j][k], s=True, d=False, connections = True, plugs = True)
                    for anim in range(0, len(animCurves), 2):
                        if '.output' in animCurves[anim+1]:
                            # print "guge"
                            print animCurves[anim+1]
                            print animCurves[anim]
                            mc.disconnectAttr(animCurves[anim+1], animCurves[anim])
                            origPlug = animCurves[anim]
                            srcPlug = animCurves[anim+1]
                            replacePlug ='%s.%s'%(JointInDict[j][k], origPlug.split('.')[-1])

                            # print "xinxx"
                            # print origPlug
                            # print srcPlug
                            # print replacePlug
                            # print "fffff"
                            mc.connectAttr(srcPlug, replacePlug, f=True)

        if len(self.allSelectedGroup) == 2:
            mc.delete(self.allSelectedGroup[1])
            mc.rename(self.allSelectedGroup[0],self.allSelectedGroup[1])
            mc.confirmDialog(title=u'提示', message=u'替换完成！', button='OK')
        else:
            mc.delete(outputGroup)
            mc.confirmDialog(title=u'提示', message=u'替换完成！', button='OK')

#OCT_MiaryCopyAnim().miaryCopyAnim()