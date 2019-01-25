# *-* coding: utf-8 *-*
import nuke,re,os,nukescripts.utils
class FKBSMergCamLeftRight():
    def __init__(self):
        self.mode=1
        self.num={'L_1_A':1, 'L_1_B':2, 'L_1_C':3, 'R_1_E':4, 'R_1_F':5, 'R_1_G':6, 'R_1_A':7, 'R_1_B':8, 'R_1_C':9, 'L_1_E':10, 'L_1_F':11, 'L_1_G':12}

    def checkFile(self, readNode):
        #改变节点的路径符号
        f = readNode.knob('file').value().replace('\\','/')
        if not f:
            nuke.message('warning File')
            return

        #basn是摄像机名、pa是路径名、pplist是路径分割后的列表
        baseN = os.path.basename(f).split('.')[0]
        pa = os.path.dirname(f)
        ppList = pa.split('/')
        backDropStr = ''

        #如果存在路径，设置backDropStr名为摄像机名，pp为摄像机名
        if not pa:
            nuke.message('warning pp')
            return
        else:
            if len(ppList):
                pp = ppList.pop()

        #判断是否有摄像机名
        if not baseN:
            nuke.message('warning baseName')
            return

        #正则表达式规则：字幕和数字类型，包含有DLMRU其中2个字幕，并且有后缀名
        pattern = re.compile('^(\w+)([LR1-9$_ABCDEFG]{5})$')
        m = None
        #pp、baseN可能是摄像机名，在这两个中匹配，匹配出一个或者两个的
        nameType = None
        myCameraGroup = [pp, baseN]
        for i in myCameraGroup:
            m = pattern.match(i)
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
        allmySelectedNodes = nuke.selectedNodes()
        if allmySelectedNodes:
            for mySelectedNode in allmySelectedNodes:
                mySelectedNode.setSelected(False)

    def FKBSMergCam(self, mode):
        self.mode = mode
        #选择所有的节点
        _source=nuke.selectedNodes('Read')
        self.numSelect = len(_source)
        #定义_contactSheet方格 _constant黑板 _backDropStr背板、保存的摄像机字典
        _contactSheet, _constant, _backDropStr,_contactSheet1, _constant1, _backDropStr1= '', '', '', '', '', ''
        _sortedCam = {}
        #搜索所选的内容
        if len(nuke.selectedNodes('ContactSheet')):
            nuke.message('ContactSheet Nodes Not Can Selected...')
            return
        if len(nuke.selectedNodes('Constant')):
            nuke.message('ContactSheet Nodes Not Can Selected...')
            return
        if len(_source)==0:
            nuke.message('No Read Nodes Selected...')
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
        _dot = nuke.nodes.Dot()
        _dot.setXYpos(_pos[0],_pos[1])
        
        _pattern=((-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0))


        _contactSheet = nuke.nodes.ContactSheet(width=_w*self.numSelect/2,height=_h,rows=1,columns=self.numSelect/2,roworder='TopBottom').name()

        _contactSheet1 = nuke.nodes.ContactSheet(width=_w*self.numSelect/2,height=_h,rows=1,columns=self.numSelect/2,roworder='TopBottom').name()

         #在所有的尺寸格式中，寻找跟素材一样样式，在创建黑板，并设置位置
        if _constant=="":
            _allFormat=nuke.formats()
            for _eachFormat in _allFormat:
                if _eachFormat.width() == _w and _eachFormat.height() == _h:
                    _constant=nuke.nodes.Constant(format=_eachFormat.name()).name()
                    _constant1=nuke.nodes.Constant(format=_eachFormat.name()).name()
                    _node=nuke.toNode(_constant)
                    _node1=nuke.toNode(_constant1)
                    break

        #在每个素材中记录摄像机，并记录黑板的名字
        for each in _source:
            camStr=self.checkFile(each)
            if camStr:
                _sortedCam[camStr[0]]=each
                if not _backDropStr:
                    _backDropStr = camStr[1]
                else:
                    each.setSelected(False)
        _sheeNode = nuke.toNode(_contactSheet)
        _sheeNode1 = nuke.toNode(_contactSheet1)
        _conNode = nuke.toNode(_constant)
        _conNode1 = nuke.toNode(_constant1)

        for _x in range(18):
            _sheeNode.setInput(_x, _conNode)
            _sheeNode1.setInput(_x, _conNode1)

        #判断素材的格式
        myfileFlagEXR = False
        #查询第一个素材的路径
        myfileName = _source[0]['file'].value()
        #获取素材的格式
        myfileNameType = os.path.splitext(myfileName)[1]
        if myfileNameType:
            if myfileNameType.find('exr')>=0:
                myfileFlagEXR = True

        MergCamL = []
        MergCamR = []

        myii = 0
        myii1 = 0
        for _k, _v in _sortedCam.iteritems():
            #print _k
            #print _v
            _sourceNode = _v
            myKey = _k
            if self.mode == 1:
                if self.num[myKey] < 7:
                    _sheeNode.setInput(self.num[myKey]-1, _sourceNode)
                    _pick = _pattern[self.num[myKey]-1]
                    #设置素材的在nuke中的位置
                    _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(), _bbox[1]*_pick[1]+_dot.ypos())
                    MergCamL.append(_sourceNode)
                else:
                    _sheeNode1.setInput(self.num[myKey]-7, _sourceNode)
                    _pick1 = _pattern[self.num[myKey]-1]
                    #设置素材的在nuke的位置
                    _sourceNode.setXYpos(_bbox[0]*_pick1[0] + _dot.xpos(), _bbox[1]*_pick1[1]+_dot.ypos())
                    MergCamR.append(_sourceNode)
            
            elif self.mode == 2:
                if not myfileFlagEXR:
                    if self.num[myKey] < 7:
                        _sheeNode.setInput(self.num[myKey]-1, _sourceNode)
                        _pick = _pattern[self.num[myKey]-1]
                        #设置素材的在nuke中的位置
                        _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(), _bbox[1]*_pick[1]+_dot.ypos())
                        MergCamL.append(_sourceNode)
                    else:
                        _sheeNode1.setInput(self.num[myKey]-7, _sourceNode)
                        _pick1 = _pattern[self.num[myKey]-1]
                        #设置素材的在nuke的位置
                        _sourceNode.setXYpos(_bbox[0]*_pick1[0]+_dot.xpos(), _bbox[1]*_pick1[1]+_dot.ypos())
                        MergCamR.append(_sourceNode)

                else:
                    if self.num[myKey]<7:
                        if myii == 0:
                            myShuffle = nuke.nodes.Shuffle()
                            myShuffle.setInput(0, _sourceNode)
                            _pick = _pattern[self.num[myKey]-1]
                            _sheeNode.setInput(self.num[myKey]-1,myShuffle)
                            _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(), _bbox[1]*_pick[1]+_dot.ypos())
                            myShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(), _bbox[1]*_pick[1]+_dot.ypos())
                        else:
                            self.setSelecteNone()
                            newMyShuffle = nuke.clone(myShuffle)
                            newMyShuffle.setInput(0, _sourceNode)
                            _pick = _pattern[self.num[myKey]-1]
                            _sheeNode.setInput(self.num[myKey]-1, newMyShuffle)
                            _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(), _bbox[1]*_pick[1]+_dot.ypos())
                            newMyShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(), _bbox[1]*_pick[1]+_dot.ypos())
                        MergCamL.append(_sourceNode)
                        myii = myii + 1

                    else:
                        if myii1 == 0:
                            myShuffle1 = nuke.nodes.Shuffle()
                            myShuffle1.setInput(0, _sourceNode)
                            _pick1 = _pattern[self.num[myKey]-1]
                            _sheeNode1.setInput(self.num[myKey]-7, myShuffle1)

                            _sourceNode.setXYpos(_bbox[0]*_pick1[0]+_dot.xpos(), _bbox[1]*_pick1[1]+_dot.ypos())
                            myShuffle1.setXYpos(_bbox[0]*_pick1[0]+_dot.xpos(), _bbox[1]*_pick1[1]+_dot.ypos())
                        else:
                            self.setSelecteNone()
                            newMyShuffle1 = nuke.clone(myShuffle1)
                            newMyShuffle1.setInput(0, _sourceNode)
                            _pick1 = _pattern[self.num[myKey]-1]
                            _sheeNode1.setInput(self.num[myKey]-7, newMyShuffle1)

                            _sourceNode.setXYpos(_bbox[0]*_pick1[0]+_dot.xpos(), _bbox[1]*_pick1[1]+_dot.ypos())
                            newMyShuffle1.setXYpos(_bbox[0]*_pick1[0]+_dot.xpos(), _bbox[1]*_pick1[1]+_dot.ypos())
                        MergCamR.append(_sourceNode)
                        myii1 = myii1 + 1


        self.setSelecteNone()

        for each in MergCamL:
            each.setSelected(1)

        _sheeNode.setXYpos(_dot.xpos()-_bbox[0]*3-_bbox[0]/2, _dot.ypos()+_bbox[1]*2-30)

        _conNode.setXYpos(_dot.xpos()-_bbox[0]*2,_dot.ypos()+_bbox[1]*1-10)

        #删除黑板
        conUsed = _conNode.dependent()

        if not conUsed:
            nuke.delete(_conNode)
        else:
            _conNode.setSelected(1)
        _sheeNode.setSelected(1)

        bd = nukescripts.autoBackdrop()
        bd.knob('label').setValue(_backDropStr)
        myOldbdHeight = bd.knob('bdheight').value()
        bd.knob('bdheight').setValue(myOldbdHeight+15)

        self.setSelecteNone()
        for each in MergCamR:
            each.setSelected(1)

        _sheeNode1.setXYpos(_dot.xpos()+_bbox[0]*3+_bbox[0]/2, _dot.ypos()+_bbox[1]*2-30)

        _conNode1.setXYpos(_dot.xpos()+_bbox[0]*5,_dot.ypos()+_bbox[1]*1-10)
        _conNode1.setSelected(1)
        _sheeNode1.setSelected(1)
        nuke.delete(_dot)
        bd1 = nukescripts.autoBackdrop()
        bd1.knob('label').setValue(_backDropStr)
        myOldbdHeight = bd1.knob('bdheight').value()
        bd1.knob('bdheight').setValue(myOldbdHeight+15)

#FKBSMergCamLeftRight().FKBSMergCam(1)
