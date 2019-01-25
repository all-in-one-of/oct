# coding=utf-8

import maya.cmds as mc
import shutil
import os


class ReplaceVRayViewport(object):
    def __init__(self):
        pass

    def showWindow(self):
        if mc.window('ReplaceVRayViewport_Window', q=True, ex=True):
            mc.deleteUI('ReplaceVRayViewport_Window')

        mc.window('ReplaceVRayViewport_Window', t = u'VRay Viewport proxy路径替换')
        form = mc.formLayout(numberOfDivisions=100)
        
        row_1 = mc.rowLayout(numberOfColumns = 2, columnAlign = (2, 'right'), columnAttach=[(1, 'left', 0), (2, 'right', 0)], adj = 1)
        self.text = mc.text(l = u'VRay Viewport proxy 个数为: 0', al = 'left')
        self.checkBox = mc.checkBox(l = u'自动复制', v = True)
        mc.setParent('..')
        
        self.textFieldGrp = mc.textFieldGrp(label=u'路径：', text='', columnWidth = [1,50], adjustableColumn = 2)
        
        row_2 = mc.rowLayout(numberOfColumns = 2, columnAttach = [(1, 'both', 0), (2, 'both', 0)], adj = 1)
        start_B = mc.button(l = u'开始替换', c = lambda *arge:self.replacePath())
        updata_B = mc.button(l = u'更新', c = lambda *arge:self.updataUI())
        mc.setParent('..')

        mc.formLayout( form, edit=True,
                      attachForm=[(row_1, 'top', 5),
                                  (row_1, 'left', 5),
                                  (row_1, 'right', 5),

                                  (self.textFieldGrp, 'left', 5),
                                  (self.textFieldGrp, 'right', 5),
                                  
                                  (row_2, 'left', 5),
                                  (row_2, 'right', 5),
                                  (row_2, 'bottom', 5),],
                      attachControl=[(row_1, 'bottom', 5, self.textFieldGrp),
                                     (self.textFieldGrp, 'bottom', 5, row_2)])
        
        self.updataUI()
        mc.showWindow( 'ReplaceVRayViewport_Window' )

    def getText(self):
        text = mc.textFieldGrp(self.textFieldGrp, q = True, tx = True)
        if os.path.isdir(text):
            return text
        else:
            mc.error(u'填写的文件路径错误，请重新填写')

    def replacePath(self):
        newPath = self.getText()
        if not self.proxyAttr:
            return
        for attrName, filePath in self.proxyAttr.iteritems():
            fileName = os.path.basename(filePath)
            fullPath = os.path.join(newPath, fileName)
            if os.path.exists(fullPath):
                mc.setAttr(attrName, fullPath, type = 'string')
            else:
                if mc.checkBox(self.checkBox, q = True, v = True):
                    self.autoCopy(filePath, fullPath, attrName)
                else:
                    mc.warning(u'%s 中，替换的路径不存在!' % attrName)

    def autoCopy(self, sourcePath, targetPath, attrName):
        try:
            shutil.copy(sourcePath, targetPath)
            mc.setAttr(attrName, targetPath, type = 'string')
        except:
            mc.warning(u'%s自动复制失败，请手动复制' % sourcePath)

    def getProxyNum(self):
        vrayNodeList = mc.ls(typ = 'VRayMesh')
        num = 0
        self.proxyAttr = {}
        if not vrayNodeList:
            return num
        for node in vrayNodeList:
            filePath = mc.getAttr('%s.overrideFileName' %node)
            if filePath and os.path.isfile(filePath):
                num += 1
                self.proxyAttr['%s.overrideFileName' %node] = filePath
        return num

    def updataUI(self):
        num = self.getProxyNum()
        mc.text(self.text, e = True, l = u'VRay Viewport proxy 个数为: %s' % str(num))
