# -*- coding: utf-8 -*-

import maya.cmds as mc
import random
import maya.OpenMaya as om

class lightRandom ():
    def __init__(self):
        self._windowSize = (350, 140)
        self._windowName = 'lightRandom_UI'

        self.lightTypeList = ['ambientLight', 'directionalLight', 'pointLight', 'spotLight', 'areaLight', 
                        'volumeLight', 'aiAreaLight', 'aiSkyDomeLight', 'aiPhotometricLight', 'VRayLightSphereShape',
                        'VRayLightDomeShape', 'VRayLightRectShape', 'VRayLightIESShape']
    
    def closeWin(self, myWinName):
        if mc.window(myWinName, q=True, exists=True):
            mc.deleteUI(myWinName, window=True)
        if mc.windowPref(myWinName, q=True, exists=True):
            mc.windowPref(myWinName, remove=True)

    def show(self):
        #删除以往的窗口
        self.closeWin(self._windowName)
        #创建窗口
        win = mc.window(self._windowName, title=u"lightRandom_UI", menuBar=True, widthHeight=(350, 140), resizeToFitChildren=True, sizeable=True)
        mc.formLayout('formLyt', numberOfDivisions=100)

        one = mc.columnLayout('First_Set', parent='formLyt')

        mc.rowLayout('oneRow', numberOfColumns=5, columnAttach5=['left', 'left', 'left', 'left', 'left'], columnWidth5=[5, 48, 60, 80, 40], columnOffset5=[2, 2, 10, 15, 24], adjustableColumn5=True, parent='First_Set')
        mc.text(label=u'Min:', w=58, parent='oneRow')
        mc.textField('minIntensity', text='', width=60, alwaysInvokeEnterCommandOnReturn=True, parent='oneRow')
        mc.text(label=u'Max:', w=58, parent='oneRow')
        mc.textField('maxIntensity', text='', width=60, alwaysInvokeEnterCommandOnReturn=True, parent='oneRow')
        mc.button(label=u'intensity', width=60, command=lambda*args:self.randomIntensity('intensity', 'minIntensity', 'maxIntensity'), parent='oneRow')

        mc.rowLayout('twoRow', numberOfColumns=5, columnAttach5=['left', 'left', 'left', 'left', 'left'], columnWidth5=[5, 48, 60, 80, 40], columnOffset5=[2, 2, 10, 15, 24], adjustableColumn5=True, parent='First_Set')
        mc.text(label=u'Min:', w=58, parent='twoRow')
        mc.textField('minExposure', text='', width=60, alwaysInvokeEnterCommandOnReturn=True, parent='twoRow')
        mc.text(label=u'Max:', w=58, parent='twoRow')
        mc.textField('maxExposure', text='', width=60, alwaysInvokeEnterCommandOnReturn=True, parent='twoRow')
        mc.button(label=u'Exposure', width=60, command=lambda*args:self.randomIntensity('aiExposure', 'minExposure', 'maxExposure'), parent='twoRow')

        mc.showWindow(win)

    def randomIntensity(self, attr, minStr, maxStr):
        allSelectObj = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True)
        minIntensity = mc.textField(minStr, q = True, text = True)
        maxIntensity = mc.textField(maxStr, q = True, text = True)
        if minIntensity == '' and maxIntensity == '':
            mc.confirmDialog(title=u'温馨提示', message=u'请输入%s的min和max！'%attr, button='OK', defaultButton='Yes', dismissString='No')
            return False

        minF = float(minIntensity)
        maxF = float(maxIntensity)

        for obj in allSelectObj:
            if mc.objectType(obj) in self.lightTypeList:
                oldIntensity = mc.getAttr('%s.%s'%(obj, attr))

                newIntensity = random.uniform(oldIntensity*(1-minF/100), oldIntensity*(1+maxF/100))
                try:
                    mc.setAttr('%s.%s'%(obj, attr), newIntensity)
                except:
                    om.MGlobal.displayWarning(u'%s.%s属性设置错误！'%(obj, attr))

    # def randomExposure(self, *args):
    #     allSelectObj = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True)
    #     minExposure = mc.textField('minExposure', q = True, text = True)
    #     maxExposure = mc.textField('maxExposure', q = True, text = True)
    #     if minExposure == '' and maxExposure == '':
    #         mc.confirmDialog(title=u'温馨提示', message=u'请输入intensity的min和max！', button='OK', defaultButton='Yes', dismissString='No')
    #         return False

    #     minF = float(minExposure)
    #     maxF = float(maxExposure)

    #     for obj in allSelectObj:
    #         if mc.objectType(obj) in self.lightTypeList:
    #             newExposure = random.uniform(minF, maxF)
    #             try:
    #                 mc.setAttr('%s.aiExposure'%obj,newExposure)
    #             except:
    #                 om.MGlobal.displayWarning(u'%s.aiExposure属性设置错误！'%obj)

#lightRandom().show()
