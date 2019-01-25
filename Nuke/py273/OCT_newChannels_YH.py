# -*- coding: utf-8 -*-
import nuke, re, os, nukescripts.utils
import random
def warnMsg(msg):
    nuke.message(msg)

class newCreateChannels():
    def __init__(self):
        self.numSelect = 0
        '''self.num = {"LD":7, "DL":7, "D":8, "RD":9, "DR":9, "L":4, "M":5, "R":6, "LU":1, "UL":1, "U":2, "RU":3, "UR":3,\
            "F_LD":13, "F_DL":13, "F_D":14, "F_RD":15, "F_DR":15, "F_L":7, "F_M":8, "F_R":9, "F_LU":1, "F_UL":1, "F_U":2, "F_RU":3, "F_UR":3,\
            "B_LD":16, "B_DL":16, "B_D":17, "B_RD":18, "B_DR":18, "B_L":10, "B_M":11, "B_R":12, "B_LU":4, "B_UL":4, "B_U":5, "B_RU":6, "B_UR":6}'''

        self.num = {'1_A':1,'1_B':2,'1_C':3,'1_D':4,'2_A':5,'2_B':6,'2_C':7,'2_D':8,'3_A':9,'3_B':10,'3_C':11,'3_D':12}

    def checkFile(self, readNode):
        #改变节点的路径符号
        f = readNode.knob('file').value().replace('\\','/')
        #print f
        if not f:
            warnMsg('warning File')
            return

        #basn是摄像机名、pa是路径名、pplist是路径分割后的列表
        baseN = os.path.basename(f).split('.')[0]
        pa = os.path.dirname(f)
        ppList = pa.split('/')
        backDropStr = ''

        #如果存在路径，设置backDropStr名为摄像机名，pp为摄像机名
        if not pa:
            warnMsg('warning pp')
            return
        else:
            if len(ppList):
                pp = ppList.pop()

        #判断是否有摄像机名
        if not baseN:
            warnMsg('warning baseName')
            return

        #正则表达式规则：字幕和数字类型，包含有DLMRU其中2个字幕，并且有后缀名
        pattern1 = re.compile('^(\w+)([ABCDEF]{1})$')
        pattern2 = re.compile('^(\w+)([ABCDEF]{2})$')
        pattern3 = re.compile('^(\w+)([1-9$_ABCDEF]{4})$')
        m = None
        #pp、baseN可能是摄像机名，在这两个中匹配，匹配出一个或者两个的
        nameType = None
        myCameraGroup = [pp, baseN]

        for i in myCameraGroup:
            if self.numSelect <= 3:
                m = pattern2.match(i)
                if m == None:
                    m = pattern1.match(i)
                    if m == None:
                        continue
            else:
                m = pattern3.match(i)
                if m == None:
                    m = pattern2.match(i)
                    if m == None:
                        m = pattern1.match(i)
                        if m == None:
                            continue
            if m:
                nameType = myCameraGroup.index(i)
                break
        #如果存在路径，设置backDropStr名为摄像机名，pp为摄像机名
        if not nameType  is None:
            if nameType == 0:
                if len(ppList) and pp:
                    backDropStr = ppList.pop()
            else:
                backDropStr = pp

        #如果有找到匹配的，把那个摄像机保存到result中
        result = None
        if m is not None:
            try:
                result = m.groups()[1]
            except:
                result = -1
        #返回那个摄像机M,
        return [result, backDropStr]

    def setSelecteNone(self):
        #如果有选择的节点，去掉选择
        allmySelectedNodes = nuke.selectedNodes()
        if allmySelectedNodes:
            for mySelectedNode in allmySelectedNodes:
                mySelectedNode.setSelected(False)

    # 界面
    def channelsUI(self):
        #获取选择的节点
        _source=nuke.selectedNodes('Read')

        if len(_source)==0:
            nuke.message("No Read Nodes Selected...")
            return 
        _bd_1=''
        if len(nuke.selectedNodes('BackdropNode')):
            _bd_1=nuke.selectedNodes('BackdropNode')[0]
            #_bd_1.setSelected(False)
        else:
            nuke.message("No BackdropNode Nodes Selected...")
            return 
        _node=_source[0]
        #查找节点的通道
        channels=_node.channels()
        #print channels
        layers = list( set([c.split('.')[0] for c in channels]))
        #print layers
        layers.sort()
        p=nuke.Panel('Merge Selected Cameras and Create Channels')
        for layer in layers:
            p.addBooleanCheckBox(layer,False)
     
        if not p.show():
            return 
       
        #原来选择的BackdropNode的X轴的位置
        _bd_X=_bd_1.xpos()
       
        #获取所选择的Read节点
        for layer in layers:
            if p.value(layer):
                self.mergeCamera(layer, _source,_bd_X)

        
        
    def mergeCamera(self,layer,_source,_bd_X):
        #获取选择了多少个Read节点
        self.numSelect=len(_source)
        _contactSheet,_constant,_bd='','',''
        _contactSheet_1,_constant_1,_backDropStr='','',''
       
        #存放选择素材节点的字典
        _sortedCam = {}
        #搜索所选的内容
        if len(nuke.selectedNodes('ContactSheet')):
            _contactSheet=nuke.selectedNodes('ContactSheet')[0] 
            _contactSheet.setSelected(False)
            #获取选择的constactSheet信息
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
            nuke.message("No BackdropNode Nodes Selected...")

        #获取BackdropNode的的大小
        _bd_w=_bd.knob('bdwidth').value()
        _bd_h=_bd.knob('bdheight').value()

        #获取BackdropNode的大小
        _bd_pos=[_bd.xpos(),_bd.ypos()]

        #以第一个素材为例，定义素材的格式_w _h
        #相对于nuke的节点大小_bbox,节点的位置_pos
        _node=_source[0]
        #素材大小
        _w=_node.knob('format').value().width()
        _h=_node.knob('format').value().height()
        
        #素材屏幕大小
        _bbox=[_node.screenWidth(),_node.screenHeight()]
        
        _pos=[_node.xpos(),_node.ypos()]
     
         #判断素材的格式是否为EXR
        myfileFlagEXR =False
        #for each in _source:
         #   myfilwName=each['file'].value()
          #  myfileNameType=os.path.splitext(myfileName)[1]


        myfileName = _source[0]['file'].value()
        myfileNameType = os.path.splitext(myfileName)[1]
        if myfileNameType:
            if myfileNameType.find('exr')>=0:
                myfileFlagEXR = True
        #常见节点，并设置它的坐标为第一个素材的节点的位置
        if not myfileFlagEXR:
            return
        _dot_bd=nuke.nodes.Dot()
        _dot_bd.setXYpos(_bd_pos[0]+int(_bd_w),_bd_pos[1]+int(_bd_h))

        '''if self.numSelect <= 9:
            _pattern = ((-1, -2), (-0, -2), (1, -2), \
                        (-1, -1), (0, -1), (1, -1), \
                        (-1, 0), (0, 0), (1, 0))
        else:
            _pattern = ((-3, -2), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), \
                        (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1), \
                        (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0))'''
        if self.numSelect==6:
            _pattern=((-2,-2),(-1,-2),(0,-2),(1,-2),\
                (-2,-1),(-1,-1),(0,-1),(1,-1),\
                (-2,0),(-1,0),(0,0),(1,0))

             #查找输出尺寸
        # _format = nuke.knob("format").split()
        #当方格为空时创建方格，并设置它的位置
        
        #if _contactSheet == "":
        #if self.numSelect <= 9: 
        #_sheetNode_1 = nuke.nodes.ContactSheet(width=_w*3,height=_h*3,roworder='TopBottom')
        #_sheetNode_1.setInput(0,_contactSheet)
        if const_split:
            starframes=_contactSheet.knob('startframe').value()
            endframes=_contactSheet.knob('endframe').value()
            _contactSheet_1 = nuke.nodes.ContactSheet(width=conts_width,height=conts_height,rows=conts_w,columns=conts_h,roworder=conts_row,colorder=const_color,splitinputs=True,startframe=starframes,endframe=endframes).name()
        else:
            _contactSheet_1 = nuke.nodes.ContactSheet(width=conts_width,height=conts_height,rows=conts_w,columns=conts_h,roworder=conts_row,colorder=const_color,splitinputs=False).name()  

       # if self.numSelect <= 9: 
          #$  _contactSheet_1 = nuke.nodes.ContactSheet(width=_w*3,height=_h*3,rows=3,columns=3,roworder='TopBottom').name()
        #else:
           # _contactSheet_1 = nuke.nodes.ContactSheet(width=_w*6,height=_h*3,rows=3,columns=6,roworder='TopBottom').name()

        _node_1 = nuke.toNode(_contactSheet_1)



         #在所有的尺寸格式中，寻找跟素材一样样式，在创建黑板，并设置位置
       # if _constant == "":
        _allFormat = nuke.formats()
        for _eachFormat in _allFormat:
           if _eachFormat.width() == _w and _eachFormat.height() == _h:
                    #创建黑板
                    #_constant = nuke.nodes.Constant(format=_eachFormat.name()).name()
                _constant_1= nuke.nodes.Constant(format=_eachFormat.name()).name()
                   
                _node_1 = nuke.toNode(_constant_1)
            
                    
        #在每个素材中记录摄像机，且记录背板的名字
        for each in _source:
            camStr = self.checkFile(each)
            if camStr:
                _sortedCam[camStr[0]] = each 
                #print each
                if not _backDropStr:
                    _backDropStr = camStr[1]
            else:
                each.setSelected(False)

        _sheetNode_1= nuke.toNode(_contactSheet_1)

      
        _conNode_1 = nuke.toNode(_constant_1)

        #连接方格和黑板
       # if self.numSelect <= 9:
           # for _x in range(9):
             #   _sheetNode_1.setInput(_x, _conNode_1)
     #   else:
        for _x in range(18):
             _sheetNode_1.setInput(_x, _conNode_1)
               # _sheetNode_2.setInput(_x, _conNode_2)

    
        myii = 0
        newMyShuffle_clone=[]
        #newMyShuffle_clone1=[]
        for _k, _v in _sortedCam.iteritems():
           # print _k
            _sourceNode = _v
            #查找摄像机相对应的方格通道，链接，并调整位置
            if _k[0] == "_":
                myKey = _k[1::]
                #print myKey
            else:
                myKey = _k
            #print myKey
            #当时exr时，添加shuffle通道节点
            
            _pick = _pattern[self.num[myKey]-1]
    
            if not myfileFlagEXR:
                _sheetNode_1.setInput(self.num[myKey]-1,_sourceNode)

                #_sourceNode.setSelected(1)
            else:
                if myii == 0:
                    #创建管道
                    myShuffle_1 =nuke.nodes.Shuffle()
                   
                    myShuffle_1['in'].setValue(layer)
                    myShuffle_1['hide_input'].setValue(True)
                 
                    #管道与Read节点连接
                    myShuffle_1.setInput(0,_sourceNode)
                    #方格与管道连接
                    _sheetNode_1.setInput(self.num[myKey]-1,myShuffle_1)
                    #设置管道的位置
                   # _node.screenWidth()
                   # _node.screenHeight()
                    myS_w=_sourceNode.xpos()-_bd_X
                    myS_h=_sourceNode.ypos()
                    myShuffle_1.setXYpos(_dot_bd.xpos()+myS_w+10,myS_h)
                   #'''if self.numSelect==5:
                      #  myShuffle_1.setXYpos(_bbox[0]*_pick[0]+_dot_bd.xpos()+2*_bbox[0],_bbox[1]*_pick[1]+_dot_bd.ypos()-_bbox[1])
                   # else:
                       # myShuffle_1.setXYpos(_bbox[0]*_pick[0]+_dot_bd.xpos()+4*_bbox[0],_bbox[1]*_pick[1]+_dot_bd.ypos()-_bbox[1])'''
                else:
                    self.setSelecteNone()
                    newMyShuffle_1 = nuke.clone(myShuffle_1)
                    newMyShuffle_1.setInput(0, _sourceNode)
                    _sheetNode_1.setInput(self.num[myKey]-1, newMyShuffle_1)

                    myS_w=_sourceNode.xpos()-_bd_X
                    myS_h=_sourceNode.ypos()
                    newMyShuffle_1.setXYpos(_dot_bd.xpos()+myS_w+10,int(myS_h))

                   #''' if self.numSelect==5:
                      #  newMyShuffle_1.setXYpos(_bbox[0]*_pick[0]+_dot_bd.xpos()+2*_bbox[0],_bbox[1]*_pick[1]+_dot_bd.ypos()-_bbox[1])
                   # else:
                     #   newMyShuffle_1.setXYpos(_bbox[0]*_pick[0]+_dot_bd.xpos()+4*_bbox[0],_bbox[1]*_pick[1]+_dot_bd.ypos()-_bbox[1])   '''   

                    newMyShuffle_clone.append(newMyShuffle_1)
                    
            
            myii = myii + 1
        

        for each in _source:
            each.setSelected(0)
        #创建背板，并设置名字，
        cs_w=_contactSheet.xpos()-_bd.xpos()
        cs_h=_contactSheet.ypos()
        _sheetNode_1.setXYpos(_dot_bd.xpos()+cs_w+10,cs_h)
        #_sheetNode_1.setInput(0,_contactSheet)

        const_w=_constant.xpos()-_bd.xpos()
        const_h=_constant.ypos()
        _conNode_1.setXYpos(_dot_bd.xpos()+const_w+10,const_h)

        '''if self.numSelect==5:
            _sheetNode_1.setXYpos(_dot_bd.xpos()+2*_bbox[0],_dot_bd.ypos()-20)
        else:
            _sheetNode_1.setXYpos(_dot_bd.xpos()+4*_bbox[0]-_bbox[0]/2,_dot_bd.ypos()-20)
        if self.numSelect ==5:
            _conNode_1.setXYpos(_dot_bd.xpos()+3*_bbox[0],_dot_bd.ypos()-_bbox[1])
          
        else:
            _conNode_1.setXYpos(_dot_bd.xpos()+_bbox[0]*6,_dot_bd.ypos()-_bbox[1])'''
       

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
    
        bd_1 = nukescripts.autoBackdrop()
        bd_1.knob('label').setValue(_backDropStr+'_'+layer)
        myOldbdHeight_1 = bd_1.knob('bdheight').value()
        myOldbdWidth_1=bd_1.knob('bdwidth').value()
        bd_1.knob('bdheight').setValue(myOldbdHeight_1+15) 
        bd_1.knob('bdwidth').setValue(myOldbdWidth_1+50) 
        bd_1.setSelected(True)


