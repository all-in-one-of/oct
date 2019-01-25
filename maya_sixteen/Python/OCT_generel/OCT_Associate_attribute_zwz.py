# coding: utf-8

import maya.cmds as mc

def OCT_Associate_attribute_zwz_UI():
    if mc.windowPref('Associate_attribute_zwz', exists=True):
        mc.windowPref('Associate_attribute_zwz', remove=True)
    if mc.window('Associate_attribute_zwz', exists=True):
        mc.deleteUI('Associate_attribute_zwz', window=True)
    mc.window("Associate_attribute_zwz",title = u"属性关联",menuBar = True,widthHeight =(300,358),resizeToFitChildren = True,sizeable = True)
    mc.columnLayout('mainmenu',adjustableColumn = True)
    mc.frameLayout('oneFL',label = u'模糊查找',labelAlign = 'top',borderStyle = 'etchedOut')
    mc.columnLayout('Xml_Type',adjustableColumn = True)
    mc.rowLayout('txRow',numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnWidth3 = [40,180,50],columnOffset3 =[2,2,2])
    mc.text(label='Name:')
    mc.textField('typeCmdText',text = 'name_aa_bb_cc',width = 160,alwaysInvokeEnterCommandOnReturn= True)
    mc.button(label ='Select',width = 60,command = 'OCT_generel.OCT_Associate_attribute_zwz.selectN_zwz()',backgroundColor = (0.9,0.5,0),annotation =u'请输入需要选择物体的名字')
    mc.setParent('mainmenu')
    mc.frameLayout('twoFL',label = u'选择关联物体和被关联的Locator',labelAlign = 'top',borderStyle = 'etchedOut',height = 247)
    mc.columnLayout(rowSpacing = 2,adjustableColumn = True,columnAlign='left')
    mc.radioButtonGrp('Object_Type_zwz',numberOfRadioButtons=2,columnAlign2=("left","left"),columnWidth=(1,50),label="Type:",labelArray2=("Shape","Transform"),columnAttach2=('left','left'), columnAttach=(1,'left',5),select=1)
    mc.rowLayout(numberOfColumns = 2,columnWidth2 = (150,150),columnAlign2=('center', 'center'), columnAttach2 =('both','both'),height =20,adjustableColumn2 = True)
    mc.text(label='Objects(Multiple)')
    mc.text(label='Locator(One)')
    mc.setParent('..')
    mc.rowLayout(numberOfColumns = 2,columnWidth2 = (150,150),columnAlign2=('center','center'), columnAttach2 =('both','both'),height =150,adjustableColumn2 = True)
    mc.textScrollList('selectObject',allowMultiSelection=1, height=150)
    mc.textScrollList('selectLoctor',allowMultiSelection=0,height=150)
    mc.setParent('..')
    mc.rowLayout(numberOfColumns = 4,columnWidth4 =(70,100,70,70),columnAlign4=('center', 'center', 'center', 'center'),height =30,adjustableColumn = True)
    mc.button( 'loadobject',label='Load',width =70,command = 'OCT_generel.OCT_Associate_attribute_zwz.Control_Alist_zwz(1)')
    mc.button( 'clearobject',label='Clear',width =70,command = 'OCT_generel.OCT_Associate_attribute_zwz.Control_Alist_zwz(2)')
    mc.button( 'loadlocator',label='Load',width =70,command = 'OCT_generel.OCT_Associate_attribute_zwz.Control_Alist_zwz(3)')
    mc.button( 'clearlocator',label='Clear',width =70,command = 'OCT_generel.OCT_Associate_attribute_zwz.Control_Alist_zwz(4)')
    mc.setParent('mainmenu')
    mc.frameLayout('threeoFL',label = 'Associate_attribute',labelAlign = 'top',borderStyle = 'etchedOut')
    mc.rowLayout(numberOfColumns = 3,columnAttach3 = ['left','left','left'],columnOffset3 =[2,5,20],columnWidth3=(50,150,10),)
    mc.text(label='Attribute:')
    mc.textField('AddAttr',text = u'别写错，不带点的！',alwaysInvokeEnterCommandOnReturn= True,w=150)
    mc.button(label ='Create',width = 60,command = 'OCT_generel.OCT_Associate_attribute_zwz.Add_Attr_zwz()',backgroundColor = (0.9,0.5,0.5),annotation =u"没写错的话，你就爽歪歪了！")
    mc.showWindow('Associate_attribute_zwz')

def selectN_zwz():
    mc.select(cl=True)
    typeCmd = mc.textField('typeCmdText', query=1, text=1)
    # buffer = typeCmd.split("_")
    # numSplit = len(buffer)
    # mySelectN = 0
    # if numSplit ==1:
    #     try:
    #         mc.select("*" + buffer[0]+ "*")
    #     except:
    #         pass
    # if numSplit ==2:
    #     try:
    #         mc.select("*" + buffer[0]+ "*" + buffer[1]+ "*")
    #     except:
    #         pass
    # if numSplit ==3:
    #     try:
    #         mc.select("*" + buffer[0]+ "*" + buffer[2]+ "*")
    #     except:
    #         pass
    # if numSplit ==4:
    #     try:
    #         mc.select("*" + buffer[0]+ "*" + buffer[3]+ "*")
    #     except:
    #         pass
    try:
        mc.select("*" + typeCmd + "*")
    except:
        pass
    mc.select('*Shape*', d=True)
    mySelectN = len(mc.ls(sl=True))
    if mySelectN:
        mc.confirmDialog(title='warning', message=u'已选择了%s个含有%s字符名字的物体' % (mySelectN,typeCmd), button='OK', defaultButton='OK')
    else:
        mc.confirmDialog(title='warning', message=u'0个物体的名字含有%s字符' % typeCmd, button='OK', defaultButton='OK')

def Control_Alist_zwz(n):
    select_o = ''
    if n==1:
        select_o = mc.ls(selection=True)
        if len(select_o)>0:
            mc.textScrollList('selectObject',edit = True,removeAll = True)
            mc.textScrollList('selectObject',edit = True,append = select_o)
        else:
            mc.confirmDialog( title='warning', message=u'请至少选择一个物体!', button='OK', defaultButton='OK' )
    if n==2:
        mc.textScrollList('selectObject',edit = True,removeAll = True)

    if n==3:
        select_o = mc.ls(selection=True)
        if len(select_o)>0 and len(select_o)<2:
            mc.textScrollList('selectLoctor',edit = True,removeAll = True)
            mc.textScrollList('selectLoctor',edit = True,append = select_o)
        else:
            mc.confirmDialog( title='warning', message=u'请仅选择一个Locator!', button='OK', defaultButton='OK' )
    if n==4:
        mc.textScrollList('selectLoctor',edit = True,removeAll = True)

def Add_Attr_zwz():
    numType = mc.radioButtonGrp('Object_Type_zwz',query = True,select=True)-1
    selected_Os = mc.textScrollList('selectObject',query = True,allItems= True)
    selected_Ls = mc.textScrollList('selectLoctor',query = True,allItems= True)
    mytext = mc.textField('AddAttr',query = True,tx = True)
    if not selected_Os or not selected_Ls:
        mc.confirmDialog( title='warning', message=u'列表不能为空!', button='OK', defaultButton='OK')
    if numType:
        try:
            valueData = mc.getAttr(selected_Os[0]+'.'+mytext)
        except:
            mc.confirmDialog( title='warning', message=u'物体不含有此属性!', button='OK', defaultButton='OK')
            return
    else:
        buffer = mc.listRelatives(selected_Os[0],shapes=True,path = True)
        try:
            valueData =  mc.getAttr(buffer[0]+'.'+mytext)
        except:
            mc.confirmDialog( title='warning', message=u'物体的Shape不含有此属性!', button='OK', defaultButton='OK')
            return
    mc.addAttr(selected_Ls[0],longName ='my_' + mytext,attributeType = 'double',defaultValue = valueData)
    mc.setAttr(selected_Ls[0] + '.my_' + mytext,edit = True,keyable = True)
    if numType:
        for selected_O in selected_Os:
            try:
                mc.connectAttr(selected_Ls[0] + '.my_' + mytext,selected_O+'.' + mytext,force = True)
            except:
                pass
    else:
        for selected_O in selected_Os:
            buffer = mc.listRelatives(selected_O,shapes=True,path = True)
            try:
                mc.connectAttr(selected_Ls[0] + '.my_' + mytext,buffer[0] +'.' + mytext,force = True)
            except:
                pass
    mc.select(selected_Ls)
    mc.confirmDialog( title='warning', message=u'Locator已关联物体的%s属性'%mytext, button='OK', defaultButton='OK')
