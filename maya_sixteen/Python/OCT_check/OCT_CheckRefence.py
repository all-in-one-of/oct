# -*- coding: utf-8 -*-
#!/usr/local/bin/python

__author__ = 'yangh'

import maya.cmds as mc

class OCT_CheckRefence():
    def __init__(self):
        self.allUnusedReference = []

    #检查无用的参拷节点
    def checkReference(self):
        allReference = mc.ls(type = "reference")
        mc.select(d = True)
        for ref in allReference:
            num = mc.lockNode(ref, q = True, l = True)
            if not num[0]:
                if self.allUnusedReference:
                    if not ref in self.allUnusedReference:
                        mc.select(ref, add = True)
                        self.allUnusedReference.append(ref)
                else:
                    mc.select(ref, add = True)
                    self.allUnusedReference.append(ref)

            try:
                reference = mc.referenceQuery(ref, filename=True)
            except:
                if self.allUnusedReference:
                    if not ref in self.allUnusedReference:
                        mc.select(ref, add = True)
                        self.allUnusedReference.append(ref)
                else:
                    mc.select(ref, add=True)
                    self.allUnusedReference.append(ref)


        if self.allUnusedReference:
            messages = u"选择了无用的参考节点，并列出如下:"
            for unused in self.allUnusedReference:
                messages = messages + unused + " "
            mc.confirmDialog(message=messages)
            print messages
        else:
            mc.confirmDialog(message=u"没有发现无用的参考节点！")
            return

    #清楚无用的参考节点
    def deleteUnusedReference(self):
        self.checkReference()
        flag = False
        for unusedRefence in self.allUnusedReference:
            num = mc.lockNode(unusedRefence, q = True, l = True)
            if num[0]:
                mc.lockNode(unusedRefence, l = False)
            mc.delete(unusedRefence)
            print u"删除的参考节点%s"%unusedRefence
            flag = True
        
        if flag:
            mc.confirmDialog(message = u"清理无用的参考节点完成！")
            return 
        else:
            mc.confirmDialog(message = u"没有清楚无用的节点！")
            return 
