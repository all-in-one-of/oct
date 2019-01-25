# *-* coding: utf-8 *-*
import nuke, re, os, nukescripts.utils

def warnMsg(msg):
    nuke.message(msg)

class MergeCamLeftRightCon():
    def __init__(self):
        self.numSelect = 0
        self.num={"L_L":1, "L_M":2, "L_R":3, "R_L":1, "R_M":2, "R_R":3}

    def checkFile(self, readNode):
        #改变节点的路径符号
        f = readNode.knob('file').value().replace('\\','/')
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
        pattern1 = re.compile('^(\w+)([LR$_DLMRU]{3})$')
        pattern2 = re.compile('^(\w+)([LR$_DLMRU]{4})$')
        pattern3 = re.compile('^(\w+)([BF$_DLMRU]{4})$')
        m = None
        #pp、baseN可能是摄像机名，在这两个中匹配，匹配出一个或者两个的
        nameType = None
        myCameraGroup = [pp, baseN]
        for i in myCameraGroup:
            if self.numSelect <= 9:
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
        allmySelectedNodes = nuke.selectedNodes()
        if allmySelectedNodes:
            for mySelectedNode in allmySelectedNodes:
                mySelectedNode.setSelected(False)

    def oldMergeCamera(self):
        #定义_source为所选的素材、_contactSheet方格 _constant黑板 _backDropStr背板、保存的摄像机字典
        _source = nuke.selectedNodes('Read')
        #self.numSelect = len(_source)
        _contactSheet_L,_contactSheet_R,_constant_L,_constant_R,_backDropStr_L,_backDropStr_R = '', '', '', '', '', ''
        _sortedCamL = {}
        _sortedCamR = {}

        if len(_source) == 0:
            nuke.message("No Read Nodes Selected...")
            return

        for each in _source:
            camStr=self.checkFile(each)
            if camStr:
                if "L_" in camStr[0]:
                    _sortedCamL[camStr[0]]=each
                    if not _backDropStr_L:
                        _backDropStr_L = camStr[1]
                    
                elif "R_" in camStr[0]:
                    _sortedCamR[camStr[0]] = each
                    if not _backDropStr_R:
                        _backDropStr_R = camStr[1]
            else:
                each.setSelected(False)

        #以第一个素材为例，定义素材的格式_w  _h
        #相对于nuke的节点大小_bbox, 节点的位置_pos
        _node = _source[0]
        _w = _node.knob('format').value().width()
        _h = _node.knob('format').value().height()
        _bbox = [_node.screenWidth(), _node.screenHeight()]
        _pos = [_node.xpos(), _node.ypos()]

        #常见点节点，并设置它的坐标为第一个素材的节点位置
        _dot = nuke.nodes.Dot()
        _dot.setXYpos(_pos[0], _pos[1])
        if len(_sortedCamL)<=3:
            _patternL=((-1, 0), (0, 0), (1, 0))

        if len(_sortedCamR)<=3:
            _patternR=((2, 0), (3, 0), (4, 0))

        if _contactSheet_L == "":
            if len(_sortedCamL)<=3:
                _contactSheet_L = nuke.nodes.ContactSheet(width=_w*3,height=_h,rows=1,columns=3,roworder='TopBottom').name()

        if _contactSheet_R == "":
            if len(_sortedCamR)<=3:
                _contactSheet_R = nuke.nodes.ContactSheet(width=_w*3,height=_h,rows=1,columns=3,roworder='TopBottom').name()

        _node_L = nuke.toNode(_contactSheet_L)
        _node_L.setXYpos(_dot.xpos()+_bbox[0]*0,_dot.ypos()+_bbox[1]*2)
        _node_R = nuke.toNode(_contactSheet_R)
        _node_R.setXYpos(_dot.xpos()+_bbox[0]*1,_dot.ypos()+_bbox[1]*2)

        #在所有的尺寸格式中，寻找跟素材一样样式，在创建黑板，并设置位置
        if _constant_L == "" and _constant_R=="":
            _allFormat = nuke.formats()
            for _eachFormat in _allFormat:
                if _eachFormat.width() == _w and _eachFormat.height() == _h:
                    _constant_L = nuke.nodes.Constant(format=_eachFormat.name()).name()
                    _node_L= nuke.toNode(_constant_L)
                    _constant_R = nuke.nodes.Constant(format=_eachFormat.name()).name()
                    _nod_R = nuke.toNode(_constant_R)

        _sheetNode_L = nuke.toNode(_contactSheet_L)
        _sheetNode_R = nuke.toNode(_contactSheet_R)
        _conNode_L = nuke.toNode(_constant_L)
        _conNode_R = nuke.toNode(_constant_R)

        if len(_sortedCamL)<=3:
            for _x in range(3):
                _sheetNode_L.setInput(_x, _conNode_L)

        if len(_sortedCamR)<=3:
            for _x in range(3):
                _sheetNode_R.setInput(_x, _conNode_R)   

        for _k, _v in _sortedCamL.iteritems():
            _sourceNode = _v
            #查找摄像机相对应的方格通道，链接，并调整位置
            if _k[0] == "_":
                myKey = _k[1::]
            else:
                myKey = _k     
            if len(_sortedCamL)<=3:
                _sheetNode_L.setInput(self.num[myKey]-1,_sourceNode)
                _pick = _patternL[self.num[myKey]-1]
                _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())

        #取消所有的选择
        nuke.delete(_conNode_L)
        self.setSelecteNone()
        for _k, _v in _sortedCamL.iteritems():
            _v.setSelected(1)

        _sheetNode_L.setXYpos(_dot.xpos()+_bbox[0]*0,_dot.ypos()+_bbox[1]*1)
        #_conNode.setXYpos(_dot.xpos()+_bbox[0]*1+86,_dot.ypos()+_bbox[1]*1-45)

        bd_L = nukescripts.autoBackdrop()
        bd_L.knob('label').setValue(_backDropStr_L)
        myOldbdHeight = bd_L.knob('bdheight').value()
        bd_L.knob('bdheight').setValue(myOldbdHeight+15)

        for _k, _v in _sortedCamR.iteritems():
            _sourceNode = _v
            #查找摄像机相对应的方格通道，链接，并调整位置
            if _k[0] == "_":
                myKey = _k[1::]
            else:
                myKey = _k     
            if len(_sortedCamR)<=3:
                _sheetNode_R.setInput(self.num[myKey]-1,_sourceNode)
                _pick = _patternR[self.num[myKey]-1]
                _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos()+50,_bbox[1]*_pick[1]+_dot.ypos())
            #取消所有的选择
        nuke.delete(_conNode_R)
        self.setSelecteNone()
        for _k, _v in _sortedCamR.iteritems():
            _v.setSelected(1)

        _sheetNode_R.setXYpos(_dot.xpos()+_bbox[0]*3+50,_dot.ypos()+_bbox[1]*1)
        nuke.delete(_dot)
        bd_R = nukescripts.autoBackdrop()
        bd_R.knob('label').setValue(_backDropStr_L)
        myOldbdHeight = bd_R.knob('bdheight').value()
        bd_R.knob('bdheight').setValue(myOldbdHeight+15)

        self.setSelecteNone()
        nukescripts.stereo.setViewsForStereo()

        joinviewsNode = nuke.createNode('JoinViews', inpanel=False)
        _sheetNode_R.setSelected(1)
        _sheetNode_L.setSelected(1)
        joinviewsNode.setInput(1, _sheetNode_R)
        joinviewsNode.setInput(0, _sheetNode_L)
        joinviewsNode.setXYpos((_sheetNode_L.xpos()+_sheetNode_R.xpos())/2, _sheetNode_R.ypos()+80)

            
