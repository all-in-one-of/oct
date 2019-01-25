# *-* coding: utf-8 *-*
import nuke,re,os,nukescripts.utils


class newMergeCam():
    def __init__(self):
        self.mode=1
        self.numSelect=0
        self.num={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}

        #self.num={'A':1,'B':2,'C':3,'1_A':1,'1_B':2,'1_C':3,'2_A':4,'2_B':5,'2_C':6,'3_A':7,'3_B':8,'3_C':9}
        self.num6={'1_A':1,'1_B':2,'1_C':3,'1_D':4,'2_A':5,'2_B':6,'2_C':7,'2_D':8,'3_A':9,'3_B':10,'3_C':11,'3_D':12}
    
    def checkFile(self,readNode):
        #改变节点路径的符号
        f=readNode.knob('file').value().replace('\\','/')
        if not f:
            warnMsg('warning File')   
        #basn是摄像机名、pa是路径名、pplist是路径分割后的列表
        baseN=os.path.basename(f).split('.')[0]
        pa=os.path.dirname(f)
        ppList=pa.split('/')
        backDropStr=''

        #如果存在路径，设置backDropStr名为摄像机名，pp为摄像机名
        if not pa:
            nuke.message('warning')
            return
        else:
            if len(ppList):
                pp=ppList.pop()
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
        #返回那个摄像机,
        return [result, backDropStr]
      

    #去掉所有所选择的点
    def setSelecteNone(self):
        allmySelectedNodes = nuke.selectedNodes()
        if allmySelectedNodes:
            for mySelectedNode in allmySelectedNodes:
                mySelectedNode.setSelected(False)


    def mergeCamera(self, flag, mymodel):
        self.mode=mymodel

        #选择所有的节点
        _source=nuke.selectedNodes('Read')
        self.numSelect=len(_source)
        #定义_contactSheet方格 _constant黑板 _backDropStr背板、保存的摄像机字典
        _contactSheet, _constant, _backDropStr = '', '', ''
        _sortedCam={}

        #搜索所选的内容
        if len(nuke.selectedNodes('ContactSheet')):
            _contactSheet=nuke.selectedNodes('ContactSheet')[0]
        if len(nuke.selectedNodes('Constant')):
            _constant=nuke.selectedNodes('Constant')[0]

        if len(_source)==0:
            nuke.message('No Read Nodes Selected...')
            return
        if len(_source)!=flag:
            nuke.message('\xe4\xbd\xa0\xe6\x89\x80\xe9\x80\x89\xe6\x8b\xa9\xe7\x9a\x84\xe7\xb4\xa0\xe6\x9d\x90\xe4\xb8\xaa\xe6\x95\xb0\xe4\xb8\x8e\xe4\xbd\xa0\xe9\x80\x89\xe6\x8b\xa9\xe7\x9a\x84\xe5\x90\x88\xe5\xb9\xb6\xe9\x80\x89\xe9\xa1\xb9\xe4\xb8\x8d\xe7\x9b\xb8\xe5\x90\x8c')
            return

        #以所选的第一个素材为例，定义素材的格式_w _h
        _node=_source[0]
        #获取第一个素材在nuke中的位置
        _w=_node.knob('format').value().width()
  
        _h=_node.knob('format').value().height()

        #获取第一个素材的大小
        _bbox=[_node.screenWidth(),_node.screenHeight()]
        _pos=[_node.xpos(),_node.ypos()]

        #常见点节点，并设置它的坐标为第一个素材的节点位置
        _dot=nuke.nodes.Dot()
        _dot.setXYpos(_pos[0],_pos[1])

        _pattern=''
        if self.numSelect<=3:
            _pattern=((-1,0),(0,0),(1,0))

        elif self.numSelect==6:
            _pattern=((-2,-2),(-1,-2),(0,-2),(1,-2),\
                (-2,-1),(-1,-1),(0,-1),(1,-1),\
                (-2,0),(-1,0),(0,0),(1,0))

        #当方格为空时，并设置它的坐标为第一个素材的节点位置
        if _contactSheet=="":
            if self.numSelect<=3:
                _contactSheet=nuke.nodes.ContactSheet(width=_w*3,height=_h*1,rows=1,columns=3,roworder='TopButtom').name()
            elif self.numSelect==6:
                _contactSheet=nuke.nodes.ContactSheet(width=_w*4,height=_h*3,rows=3,columns=4,roworder='TopButtom').name()

            _node=nuke.toNode(_contactSheet)
            _node=_node.setXYpos(_dot.xpos()+_bbox[0]*0,_dot.ypos()+_bbox[1]*2)

        #在所有的尺寸格式中，寻找跟素材一样样式，在创建黑板，并设置位置
        if _constant=="":
            _allFormat=nuke.formats()
            for _eachFormat in _allFormat:
                if _eachFormat.width()==_w and _eachFormat.height()==_h:
                    _constant=nuke.nodes.Constant(format=_eachFormat.name()).name()
                    _node=nuke.toNode(_constant)
                   


        #在每个素材中记录摄像机，并记录黑板的名字
        for each in _source:
            camStr=self.checkFile(each)
            if camStr:
                _sortedCam[camStr[0]]=each
                if not _backDropStr:
                    _backDropStr=camStr[1]
                else:
                    each.setSelected(False)
        _sheeNode=nuke.toNode(_contactSheet)
        _conNode=nuke.toNode(_constant)


        #根据所选的素材的个数创建ContactSheet和Constant连接的线
        if self.numSelect==3:
            for _x in range(9):
                _sheeNode.setInput(_x,_conNode)
        else:
            for _x in range(18):
                _sheeNode.setInput(_x,_conNode)
        #判断素材的格式
        myfileFlagEXR=False
        #查询第一个素材的路径
        myfileName=_source[0]['file'].value()
        #获取素材的格式
        myfileNameType=os.path.splitext(myfileName)[1]
        if myfileNameType:
            if myfileNameType.find('exr')>=0:
                myfileFlagEXR = True

        myii=0
        for _k,_v in _sortedCam.iteritems():
            _sourceNode=_v
            #查找摄像机对应的方格通道，链接，并调整位置
            if _k[0]=="_":
                myKey=_k[1::]
            else:
                myKey=_k

            #当时exr时，添加shuffle通道节点
            if self.mode==1:
                if self.numSelect==3:
                    _sheeNode.setInput(self.num[myKey]-1,_sourceNode)
                    _pick=_pattern[self.num[myKey]-1]
                    #设置素材的在nuke中的位置
                    _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                elif self.numSelect==6:
                    _sheeNode.setInput(self.num6[myKey]-1,_sourceNode)
                    _pick=_pattern[self.num6[myKey]-1]
                    _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())

            #当时exr时，根据需要添加shuffle通道节点
            elif self.mode==2:
                if self.numSelect==3:
                    _pick=_pattern[self.num[myKey]-1]
                    _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                    if not myfileFlagEXR:
                        _sheeNode.setInput(self.num[myKey]-1,_sourceNode)
                        _sourceNode.setSelected(1)
                    else:
                        if myii==0:
                            myShuffle=nuke.nodes.Shuffle()
                            myShuffle.setInput(0,_sourceNode)
                            _sheeNode.setInput(self.num[myKey]-1,myShuffle)
                            myShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                        else:
                            self.setSelecteNone()
                            newMyShuffle=nuke.clone(myShuffle)
                            newMyShuffle.setInput(0,_sourceNode)
                            _sheeNode.setInput(self.num[myKey]-1,newMyShuffle)
                            newMyShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())

                elif self.numSelect==6:
                    _pick=_pattern[self.num6[myKey]-1]
                    _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                    if not myfileFlagEXR:
                        _sheeNode.setInput(self.num6[myKey]-1,_sourceNode)
                        _sourceNode.setSelected(1)
                    else:
                        if myii==0:
                            myShuffle=nuke.nodes.Shuffle()
                            myShuffle.setInput(0,_sourceNode)
                            _sheeNode.setInput(self.num6[myKey]-1,myShuffle)
                            myShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                        else:
                            self.setSelecteNone()
                            newMyShuffle=nuke.clone(myShuffle)
                            newMyShuffle.setInput(0,_sourceNode)
                            _sheeNode.setInput(self.num6[myKey]-1,newMyShuffle)
                            newMyShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())

            myii=myii+1
        _sheeNode.setSelected(1)

        for each in _source:
            each.setSelected(1)
        if self.numSelect==3:
            _sheeNode.setXYpos(_dot.xpos()+_bbox[0]*0,_dot.ypos()+_bbox[1]*2-30)
            _conNode.setXYpos(_dot.xpos()+_bbox[0]*1,_dot.ypos()+_bbox[1]*1-10) 

        elif self.numSelect==6:
            _sheeNode.setXYpos(_dot.xpos()+_bbox[0]*0-45,_dot.ypos()+_bbox[1]*1)
            _conNode.setXYpos(_dot.xpos()+10,_dot.ypos()+10)   

        #if self.numSelect==3:
            #_conNode.setXYpos(_dot.xpos()+_bbox[0]*1,_dot.ypos()+_bbox[1]*1-10)   

        #删除黑板
        conUsed=_conNode.dependent()

        if not conUsed:
            nuke.delete(_conNode)
        else:
            _conNode.setSelected(1)

        nuke.delete(_dot)
        bd=nukescripts.autoBackdrop()
        bd.knob('label').setValue(_backDropStr)
        myOldbdHeight = bd.knob('bdheight').value()
        bd.knob('bdheight').setValue(myOldbdHeight+15)
    #=============add by zhangben  2018.12.12 =========== for DNTG ===========merge 3 cameras=====
    def mergeCams_dntg(self, sourceSels, flag, FileName):
        _dot = nuke.nodes.Dot()
        sourceSels = sorted(sourceSels, key=lambda eaNd: self.checkFile(eaNd, FileName)[0])

        left_edge = min(eand.xpos() for eand in sourceSels)
        right_edge = max(eand.xpos() for eand in sourceSels)

        top_edge = min(eand.ypos() for eand in sourceSels)
        bottom_edge = max(eand.ypos() for eand in sourceSels)

        _sortedCam = {}
        # cleare select
        for i in sourceSels:
            i['selected'].setValue(False)

        transData = {"A": {"translate": [0, 0]}, "B": {"translate": [2286, 1028.5]}, "C": {"translate": [4572, 0]}}
        centerData = [1143, 4343.5]

        merge_inputPlugs = {0: 1, 1: 3, 2: 4}

        x_pos_v = left_edge

        transLst = []
        for each in sourceSels:
            # each['selected'].setValue(True)
            camStr = self.checkFile(each, FileName)
            if not camStr: nuke.error("sutff name promeblem")
            _bkdrpStr = "cam{}".format(camStr[0])

            each.setXYpos(x_pos_v, top_edge)
            ea_w = each.screenWidth()
            ea_h = each.screenHeight()

            ea_left = each.xpos()
            ea_right = ea_left + ea_w

            ea_top = each.ypos()
            ea_bottom = ea_top - ea_h

            #   each.setSelected(1)

            bdrp = nuke.nodes.BackdropNode(xpos=ea_left - 15, bdwidth=ea_w + 30, ypos=ea_top - 35, bdheight=ea_h + 70,
                                           tile_color=int((random.random() * (16 - 10))) + 10, note_font_size=42)
            bdrp.setName(camStr[0])
            bdrp.knob("label").setValue(_bkdrpStr)

            trnsnd = nuke.nodes.Transform()
            trnsnd['translate'].setValue([transData[camStr[0]].values()[0][0], transData[camStr[0]].values()[0][1]])
            trnsnd['center'].setValue([centerData[0], centerData[1]])
            trnsnd.setXYpos(ea_left, ea_bottom + 250)
            trnsnd.setInput(0, each)
            transLst.append(trnsnd)

            each.setYpos(each.ypos() + 30)
            x_pos_v += (ea_w + 33)

        MergeNode = nuke.nodes.Merge2()
        MergeNode.setXYpos(transLst[1].xpos(), transLst[1].ypos() + 80)
        for n in range(len(transLst)):
            MergeNode.setInput(merge_inputPlugs[n], transLst[n])

        _setFormat = [eafmt for eafmt in nuke.formats() if eafmt.width() == 6858]
        _constant = nuke.nodes.Constant(format=_setFormat[0].name())

        _constant.setXYpos((MergeNode.xpos() + 200), MergeNode.ypos() - 50)
        _constant.knob("channels").setValue("rgb")
        MergeNode.setInput(0, _constant)

    #合并选择相机的界面
    def mergeSelectCamUI(self,model):
        p=nuke.Panel('Merg Select Cam Tools')
        p.setWidth(100)
        p.addBooleanCheckBox('TDHJ Merg 3 Cam',False)
        p.addBooleanCheckBox('CPSP Merg 6 Cam', False)
        p.addBooleanCheckBox('Merg 5 Cam',False)
        p.addBooleanCheckBox('Merg 9 Cam',False)
        p.addBooleanCheckBox('Merg 10 Cam',False)
        p.addBooleanCheckBox('Merg 18 Cam',False)


        p.addButton('Cancel')
        p.addButton('OK')
        result=p.show()
        flag=''
        if p.value('TDHJ Merg 3 Cam'):
            if flag=='':
                flag=3
            else:
                nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
                return 

        if p.value('Merg 5 Cam'):
            if flag=='':
                flag=5
            else:
                nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
                return

        if p.value('Merg 9 Cam'):
            if flag=='':
                flag=9
            else:
                nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
                return 

        if p.value('Merg 10 Cam'):
            if flag=='':
                flag=10
            else:
                nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
                return
           
        if p.value('Merg 18 Cam'):
            if flag=='':
                flag=18
            else:
                nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
                return 

        if p.value('CPSP Merg 6 Cam'):
            if flag=='':
                flag=6
            else:
                nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
                return
       
        if flag:
            self.mergeCamera(flag,model)
            return 