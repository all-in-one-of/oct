# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import maya.cmds as mc
import maya.mel as mm
import os 

USERNAME = os.environ['USER']
OCT_FilePath = r'\\file.com\share'

class SubmitDeadline_Vfx():
    def __init__(self):
        #文件名
        self.fileSName = mc.file(q=True, sn=True, shn=True)
        #工程路径
        self.projectPath = mc.workspace(q = True,fn = True)

        self.windowSize = (200, 150)
        self.windowName = 'SubmitDeadline_Vfx_UI'

        self.project = ''
        self.scene = ''
        self.Screen = ''
        self.element = '' 

    #关闭窗口
    def close(self, *args):
        if mc.window(self.windowName, q=True, exists=True):
            mc.deleteUI(self.windowName)

    def SubmitDeadline_Vfx_UI(self):
        if not self.getSubmitData():
            return False

        self.close()
        win = mc.window(self.windowName, t = 'SubmitDeadline_Vfx_UI', wh = self.windowSize, mnb = False, mxb = False, rtf = True, s = False)
        mc.columnLayout(rowSpacing = 2, columnWidth = 50, columnAlign = 'center')   
        mc.textFieldGrp('project', label = u'项目:', text = self.project, editable = True, ct2 = ('left', 'left'), cw2 = (30, 150))
        mc.textFieldGrp('scene', label = u'场景:', text = self.scene, editable = True, ct2 = ('left', 'left'), cw2 = (30, 150))
        mc.textFieldGrp('Screen', label = u'场次:', text = self.Screen, editable = True, ct2 = ('left', 'left'), cw2 = (30, 150))
        mc.textFieldGrp('element', label = u'元素:', text = self.element, editable = True, ct2 = ('left', 'left'), cw2 = (30, 150))
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3, columnAttach3=['both', 'both', 'both'], columnWidth3=[90, 90, 90], columnOffset3=[2, 2, 2], adjustableColumn3=True)
        mc.button('Dayang', l=u'大样', c = lambda *args:self.texturePath(1))
        mc.button('Xiaoyang', l=u'小样', c = lambda *args:self.texturePath(2))
        mc.showWindow(self.windowName)
        
    def getSubmitData(self):
        if not self.fileSName:
            mc.confirmDialog( title=u'温馨提示', message=u'请先保存文件！', button='OK')
            return False
        buf = self.fileSName.split('_')
        if len(buf) >= 5:
            self.project = buf[0]
            self.scene = buf[1]
            self.Screen = buf[2]
            if '.' in buf[4]:
                self.element = buf[4].split('.')[0]
            else:
                self.element = buf[4]

        return True


    def texturePath(self, type):
        imagesPath = ""
        myFileFullName = mc.file(q = True, sn = True)
        print myFileFullName
        self.project = mc.textFieldGrp('project', q = True, text = True)
        self.scene = mc.textFieldGrp('scene', q = True, text = True)
        self.Screen = mc.textFieldGrp('Screen', q = True, text = True)
        self.element = mc.textFieldGrp('element', q = True, text = True)
        if not self.project or not self.scene or not self.Screen or not self.element:
            mc.confirmDialog(title=u'温馨提示', message=u'请输入项目、场景、场次、元素！', button='OK')
            return 

        if type == 1:
            imagesPath = os.path.join(OCT_FilePath, self.project, 'Images', 'Dayang', self.scene, self.Screen, self.element, USERNAME)
            
        elif type == 2:
            imagesPath = os.path.join(OCT_FilePath, self.project, 'Images', 'Xiaoyang', self.scene, self.Screen, self.element, USERNAME)
    
        if imagesPath:
            result = mc.confirmDialog( title=u'温馨提示', message=u'提交渲染的路径：%s\n'%imagesPath, button=['submit', 'cancel'], defaultButton='submit', dismissString='cancel')
            if result == 'submit':
                myfileBaseName = os.path.splitext(self.fileSName)[0]
                mm.eval(r'global string $myFileName = "%s"' % myfileBaseName)
                mm.eval(r'global string $myDeadlineImagesPath = "%s"' % imagesPath.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineSceneFile = "%s"' % myFileFullName.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineProjectPath= "%s"' % self.projectPath.replace('\\', '/'))
                mm.eval('source "SubmitMayaToDeadline_zwz";')
                mm.eval('SubmitMayaToDeadline_zwz')
                              

#SubmitDeadline_Vfx().SubmitDeadline_Vfx_UI()
