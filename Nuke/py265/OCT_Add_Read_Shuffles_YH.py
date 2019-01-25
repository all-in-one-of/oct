# *-* coding: utf-8 *-*

import nuke, re, os, nukescripts.utils

def warnMsg(msg):
    nuke.message(msg)

class createChannels():
    def __init__(self):
        self.numSelect=0
        self.flag=False

    #如果有选择的节点，去掉选择
    def setSelecteNone(self):
        allmySelectedNodes=nuke.selectedNodes()
        if allmySelectedNodes:
            for mySelectedNode in allmySelectedNodes:
                mySelectedNode.setSelected(False)

    #界面            
    def channelsUI(self):
        #获取选择的节点
        _source=nuke.selectedNodes('Read')
        #是否选择了素材
        if len(_source)==0:
            nuke.message("No Read Nodes Selected...")
            return

        _bd_1=''
        #先选择BackdropNode
        if len(nuke.selectedNodes('BackdropNode')):
            _bd_1=nuke.selectedNodes('BackdropNode')[0]
        else:
            nuke.message('No BackdropNode Nodes Selected ...')
            return

        _node=_source[0]
        #查找节点的通道
        channels=_node.channels()
        layers=list(set([c.split('.')[0] for c in channels]))
        layers.sort()
        p=nuke.Panel('Merge Selected Cameras and Create Channels')
        for layer in layers:
            p.addBooleanCheckBox(layer, False)

        if not p.show():
            return

        #获取原来选择的BackdropNode的X轴的位置
        _bd_X=_bd_1.xpos()
        backDropStr=nuke.selectedNodes('BackdropNode')[0]

        #获取所选择的Read节点
        for layer in layers:
            if p.value(layer):
                self.mergeCamera(layer, _source, _bd_X,backDropStr)

    #创建相机通道并合并
    def mergeCamera(self,layer,_source,_bd_X,backDropStr):
        #获取选择的Read节点的个数
        self.numSelect=len(_source)
        #所选择的_contactSheet方格 _constant黑板 _backDropStr背板
        _contactSheet,_constant,_bd='','',''
        #新创建的_contactSheet方格 _constant黑板 _backDropStr背板
        _contactSheet_1,_constant_1,_backDropStr='','',''
        #保存的摄像机字典
        _sortedCam = {}
        _backDropStr=backDropStr.knob('label').value()
        #获取所选择的contactSheet方格 _constant黑板 _backDropStr背板中的信息
        if len(nuke.selectedNodes('ContactSheet')):
            _contactSheet=nuke.selectedNodes('ContactSheet')[0]
            _contactSheet.setSelected(False)
            #获取所选择的ContactSheet的信息
            conts_w=_contactSheet.knob('rows').value()
            conts_h=_contactSheet.knob('columns').value()
            conts_row=_contactSheet.knob('roworder').value()
            conts_width=_contactSheet.knob('width').value()
            conts_height=_contactSheet.knob('height').value()
            const_color=_contactSheet.knob('colorder').value()
            const_split=_contactSheet.knob('splitinputs').value()

        if len(nuke.selectedNodes('Constant')):
            _constant=nuke.selectedNodes('Constant')[0]
            _constant.setSelected(False)

        if len(nuke.selectedNodes('BackdropNode')):
            _bd=nuke.selectedNodes('BackdropNode')[0]
            _bd.setSelected(False)
        else:
            nuke.message('No BackdropNode Nodes Selected...')
            return

        #判断是否选择了Shuffle
        if len(nuke.selectedNodes('Shuffle')):
            self.flag=True
        else:
            self.flag=False


        #获取BackdropNode的大小
        _bd_w=_bd.knob('bdwidth').value()
        _bd_h=_bd.knob('bdheight').value()

        #获取BackdropNode的位置
        _bd_pos=[_bd.xpos(),_bd.ypos()]
        #以第一个素材为例，定义素材的格式_w,_h
        _node=_source[0]
        #素材大小
        _w=_node.knob('format').value().width()
        _h=_node.knob('format').value().height()

        #素材屏幕大小
        _bbox=[_node.screenWidth(),_node.screenHeight()]
        _pos=[_node.xpos(),_node.ypos()]

        #判断素材的格式是否为EXR
        myfileFlagEXR=False

        myfileName=_source[0]['file'].value()    
        myfileNameType = os.path.splitext(myfileName)[1]
        if myfileNameType:
            if myfileNameType.find('exr')>=0:
                myfileFlagEXR=True


        #常见节点，并设置它的坐标为第一个素材的节点的位置
        if not myfileFlagEXR:
            return

        _dot_bd=nuke.nodes.Dot()
        _dot_bd.setXYpos(_bd_pos[0]+int(_bd_w),_bd_pos[1]+int(_bd_h))

        if const_split:
            starframes=_contactSheet.knob('startframe').value()
            endframes=_contactSheet.knob('endframe').value()
            _contactSheet_1 = nuke.nodes.ContactSheet(width=conts_width,height=conts_height,rows=conts_w,columns=conts_h,roworder=conts_row,colorder=const_color,splitinputs=True,startframe=starframes,endframe=endframes).name()
        else:
            _contactSheet_1 = nuke.nodes.ContactSheet(width=conts_width,height=conts_height,rows=conts_w,columns=conts_h,roworder=conts_row,colorder=const_color,splitinputs=False).name()  

        _node_1 = nuke.toNode(_contactSheet_1)

        #在所有的尺寸格式中，寻找跟素材一样的样式，在创建黑板，并设置位置
        _allFormat = nuke.formats()
        for _eachFormat in _allFormat:
               if _eachFormat.width()==_w and _eachFormat.height()==_h:
                   _constant_1=nuke.nodes.Constant(format=_eachFormat.name()).name()
                   _node_1=nuke.toNode(_constant_1)
        
        _sheetNode_1= nuke.toNode(_contactSheet_1)
        _conNode_1=nuke.toNode(_constant_1)

        for _x in range(18):
            _sheetNode_1.setInput(_x,_conNode_1)

        mii=0
        newMyShuffle_clone=[]
        for each in  _source:
            if mii==0:
                #创建管道
                myShuffle_1=nuke.nodes.Shuffle()

                myShuffle_1['in'].setValue(layer)
                myShuffle_1['hide_input'].setValue(True)
                for i in range(18):
                    if self.flag:
                        if _contactSheet.input(i).input(0)==each:
                            myShuffle_1.setInput(0,each)
                            #方格与管道连接
                            _sheetNode_1.setInput(i,myShuffle_1)
                            #设置管道的位置
                            myS_w=each.xpos()-_bd_X
                            myS_h=each.ypos()
                            myShuffle_1.setXYpos(_dot_bd.xpos()+myS_w+10,myS_h)
                            break
                    else:
                        if _contactSheet.input(i)==each:
                            #管道与Read节点连接
                            myShuffle_1.setInput(0,each)
                            #方格与管道连接
                            _sheetNode_1.setInput(i,myShuffle_1)
                            #设置管道的位置
                            myS_w=each.xpos()-_bd_X
                            myS_h=each.ypos()
                            myShuffle_1.setXYpos(_dot_bd.xpos()+myS_w+10,myS_h)
                            break
            else:
                self.setSelecteNone()
                newMyShuffle_1 = nuke.clone(myShuffle_1)
                for i in range(18):
                    if self.flag:
                        if _contactSheet.input(i).input(0)==each:
                            newMyShuffle_1.setInput(0, each)
                            _sheetNode_1.setInput(i, newMyShuffle_1)
                            myS_w=each.xpos()-_bd_X
                            myS_h=each.ypos()
                            newMyShuffle_1.setXYpos(_dot_bd.xpos()+myS_w+10,int(myS_h))
                            newMyShuffle_clone.append(newMyShuffle_1)
                            break  
                    else:
                        if _contactSheet.input(i)==each:
                            newMyShuffle_1.setInput(0, each)
                            _sheetNode_1.setInput(i, newMyShuffle_1)
                            myS_w=each.xpos()-_bd_X
                            myS_h=each.ypos()
                            newMyShuffle_1.setXYpos(_dot_bd.xpos()+myS_w+10,int(myS_h))
                            newMyShuffle_clone.append(newMyShuffle_1)
                            break

            mii=mii+1
        for each in _source:
            each.setSelected(False)

        #创建背板，并设置名字，
        cs_w=_contactSheet.xpos()-_bd.xpos()
        cs_h=_contactSheet.ypos()
        _sheetNode_1.setXYpos(_dot_bd.xpos()+cs_w+10,cs_h)
        #_sheetNode_1.setInput(0,_contactSheet)

        const_w=_constant.xpos()-_bd.xpos()
        const_h=_constant.ypos()
        _conNode_1.setXYpos(_dot_bd.xpos()+const_w+10,const_h)

        #删除黑板
        conUsed = _conNode_1.dependent()
       # print conUsed

        if not conUsed:
            nuke.delete(_conNode_1)
        else:
            _conNode_1.setSelected(1)

        nuke.delete(_dot_bd)

        for shuffle in newMyShuffle_clone:
            shuffle.setSelected(True)
        _sheetNode_1.setSelected(True)
       
        _conNode_1.setSelected(True)
        myShuffle_1.setSelected(True)
        newMyShuffle_1.setSelected(True)

        myOldbdWidth_1=backDropStr.knob('bdwidth').value()
        myOldbdHeight_1=backDropStr.knob('bdheight').value()
        bd_1 = nukescripts.autoBackdrop()
        bd_1.knob('label').setValue(_backDropStr+'_'+layer)

        #myOldbdHeight_1 = bd_1.knob('bdheight').value()
        #myOldbdWidth_1=bd_1.knob('bdwidth').value()
        bd_1.knob('bdheight').setValue(myOldbdHeight_1) 
        bd_1.knob('bdwidth').setValue(myOldbdWidth_1) 
      
        bd_1.setSelected(True)
# b=createChannels()   

# b.channelsUI()

