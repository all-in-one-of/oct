# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os

if mc.windowPref('ReplaceOriginalObject_zwz', exists=True):
    mc.windowPref('ReplaceOriginalObject_zwz', remove=True)
if mc.window('ReplaceOriginalObject_zwz', exists=True):
    mc.deleteUI('ReplaceOriginalObject_zwz', window=True)
allCameras = mc.listCameras(p=True)
myStartFrameV = mc.getAttr("defaultRenderGlobals.startFrame")
myEndFrameV = mc.getAttr("defaultRenderGlobals.endFrame")
myRenderwidth = mc.getAttr("defaultResolution.width")
myRenderheight = mc.getAttr("defaultResolution.height")

mc.window("ReplaceOriginalObject_zwz",title = u"OCT_ReplaceOriginalObject_zwz",menuBar = True,widthHeight =(350,340),resizeToFitChildren = True,sizeable = True)

mc.formLayout('formLyt', numberOfDivisions=100)

one = mc.radioButtonGrp('modelOption_Radio',label=u'模式:',labelArray2=[u'创建', u'修复'], numberOfRadioButtons=2,columnAlign=[1,'left'],columnAlign2=['left','left'], cw3=[45, 75, 90], sl = 1, bgc=(0.2,0.8,0.3), cc='modelOption()', parent = 'formLyt')

two_one = mc.frameLayout('Replace_objects',label = u'被替代物体',labelAlign = 'top',borderStyle = 'etchedOut', en=True,  parent='formLyt')
two_one_one = mc.textScrollList('Replace_objects_text', allowMultiSelection=True,parent = 'Replace_objects')
mc.button('Replace_AB', label =u'加载',command = '', backgroundColor = (0.9,0.5,0))
mc.button('Replace_CB', label =u'清除',command = '', backgroundColor = (0.2,0.8,0.3))

two_two =mc.frameLayout('Instancer_objects',label = u'替代的源物体',labelAlign = 'top',borderStyle = 'etchedOut',w=100,h=100,parent = 'formLyt')
mc.textScrollList('Instancer_objects_text', allowMultiSelection=True,parent = 'Instancer_objects')
mc.button(label =u'加载',command = '', backgroundColor = (0.9,0.5,0))
mc.button(label =u'清除',command = '', backgroundColor = (0.2,0.8,0.3))

two_three =mc.frameLayout('myLocators',label = u'Locators',labelAlign = 'top',borderStyle = 'etchedOut',parent = 'formLyt')
mc.textScrollList('myLocators_text', allowMultiSelection=True,parent = 'myLocators')
mc.button(label =u'加载',command = '', backgroundColor = (0.9,0.5,0))
mc.button(label =u'清除',command = '', backgroundColor = (0.2,0.8,0.3))

two_four = mc.frameLayout('myParticles',label = u'Particles',labelAlign = 'top',borderStyle = 'etchedOut', en=False, parent = 'formLyt')
mc.textScrollList('myParticles_text', allowMultiSelection=True,parent = 'myParticles')
mc.button('myParticles_AB', label =u'加载',command = '', backgroundColor = (0.267, 0.267, 0.267))
mc.button('myParticles_CB', label =u'清除',command = '', backgroundColor = (0.267, 0.267, 0.267))

three = mc.textFieldGrp('Instancer_objects_name', label='替换物体的组名', text = 'test',cw2=[85, 250], cal=[1, 'left'], parent = 'formLyt')

four = mc.frameLayout('NoAnModel',label = u'静态模式(无动画)',labelAlign = 'top',borderStyle = 'etchedOut',parent = 'formLyt')
mc.rowLayout('NoAnModel_row',numberOfColumns = 3,columnAttach3 = ['left','left','left'], columnWidth3 = [80,180,35], columnOffset3 =[2,2,2], parent = 'NoAnModel')
mc.text(label=u'关联复制:',parent = 'NoAnModel_row')
mc.button('NoAnModel_ICB', label=u'创建', w=130, command='', backgroundColor = (0.2,0.8,0.3))

five = mc.frameLayout('AnModel',label = u'动态模式(动画)',labelAlign = 'top',borderStyle = 'etchedOut',parent = 'formLyt')
mc.rowLayout('AnModel_In_row',numberOfColumns = 3,columnAttach3 = ['left','left','left'], columnWidth3 = [80,180,35], columnOffset3 =[2,2,2], parent = 'AnModel')
mc.text(label=u'关联复制:',parent = 'AnModel_In_row')
mc.button('AnModel_ICB', label=u'创建', w=130, command='', backgroundColor = (0.2,0.8,0.3))
mc.rowLayout('AnModel_Pr_row',numberOfColumns = 4,columnAttach4 = ['left','left','left','left'], columnWidth4 = [80,180,180,35], columnOffset4 =[2,2,2,2], parent = 'AnModel')
mc.text(label=u'粒子替代:',parent = 'AnModel_Pr_row')
mc.button('AnModel_PCB', label=u'创建', w=130, command='', backgroundColor = (0.2, 0.8, 0.3))
mc.button('AnModel_PMB', label=u'修复', w=130, command='', en=False, backgroundColor = (0.267, 0.267, 0.267))

mc.formLayout('formLyt', e=True,
              attachForm=[(two_one, 'left', 0), (four, 'left', 0), (five, 'left', 0), (two_four, 'right', 0), (four, 'right', 0), (five, 'right', 0), (two_one, 'top', 20), (two_two, 'top', 20), (two_three, 'top', 20), (two_four, 'top', 20), (five, 'bottom', 5)],
              attachControl=[(two_one, 'bottom', 1, three), (two_two, 'bottom', 1, three), (two_three, 'bottom', 1, three), (two_four, 'bottom', 1, three), (three, 'bottom', 1, four), (four, 'bottom', 1, five)],
              attachNone=[],
              attachPosition=[(two_one, 'right', 0, 25), (two_two, 'left', 0, 25), (two_two, 'right', 0, 50), (two_three, 'left', 0, 50), (two_three, 'right', 0, 75), (two_four, 'left', 0, 75), (two_four, 'right', 0, 100)])

mc.showWindow('ReplaceOriginalObject_zwz')

def modelOption():
    modelOptionV = mc.radioButtonGrp('modelOption_Radio', q=True, sl=True)
    if modelOptionV == 1:
        mc.frameLayout('Replace_objects', e=True, en=True)
        mc.frameLayout('myParticles', e=True, en=False)
        mc.button('Replace_AB', e=True, en=True, backgroundColor = (0.9,0.5,0))
        mc.button('Replace_CB', e=True, en=True, backgroundColor = (0.2, 0.8, 0.3))
        mc.button('myParticles_AB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))
        mc.button('myParticles_CB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))
        mc.button('NoAnModel_ICB', e=True, en=True, backgroundColor = (0.2, 0.8, 0.3))
        mc.button('AnModel_ICB', e=True, en=True, backgroundColor = (0.2, 0.8, 0.3))
        mc.button('AnModel_PCB', e=True, en=True, backgroundColor = (0.2, 0.8, 0.3))
        mc.button('AnModel_PMB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))

    elif modelOptionV == 2:
        mc.frameLayout('Replace_objects', e=True, en=False)
        mc.frameLayout('myParticles', e=True, en=True)
        mc.button('Replace_AB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))
        mc.button('Replace_CB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))
        mc.button('myParticles_AB', e=True, en=True, backgroundColor = (0.9,0.5,0))
        mc.button('myParticles_CB', e=True, en=True, backgroundColor = (0.2, 0.8, 0.3))
        mc.button('NoAnModel_ICB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))
        mc.button('AnModel_ICB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))
        mc.button('AnModel_PCB', e=True, en=False, backgroundColor = (0.267, 0.267, 0.267))
        mc.button('AnModel_PMB', e=True, en=True, backgroundColor = (0.2, 0.8, 0.3))
