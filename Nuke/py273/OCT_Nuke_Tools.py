# *-* coding: utf-8 *-*
import nuke, re, os, nukescripts.utils

def warnMsg(msg):
    nuke.message(msg)

class mergeCam():
    def __init__(self):
        #根据部门和特殊需要添加Shuffle，mode=1为不添加，2为添加
        self.mode = 1
        self.numSelect = 0
        self.num3={"LL":1, "LR":1, "L":1, "ML":2, "MR":2, "M":2, "RL":3, "RR":3, "R":3}
        self.num = {"LD":7, "DL":7, "D":8, "RD":9, "DR":9, "L":4, "M":5, "R":6, "LU":1, "UL":1, "U":2, "RU":3, "UR":3,\
            "F_LD":13, "F_DL":13, "F_D":14, "F_RD":15, "F_DR":15, "F_L":7, "F_M":8, "F_R":9, "F_LU":1, "F_UL":1, "F_U":2, "F_RU":3, "F_UR":3,\
            "B_LD":16, "B_DL":16, "B_D":17, "B_RD":18, "B_DR":18, "B_L":10, "B_M":11, "B_R":12, "B_LU":4, "B_UL":4, "B_U":5, "B_RU":6, "B_UR":6}

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
        pattern1 = re.compile('^(\w+)([DLMRU]{1})$')
        pattern2 = re.compile('^(\w+)([DLMRU]{2})$')
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

    def mergeCamera(self,mymodel):
        self.mode = mymodel
        #定义_source为所选的素材、_contactSheet方格 _constant黑板 _backDropStr背板、保存的摄像机字典
        _source = nuke.selectedNodes('Read')
        self.numSelect = len(_source)
        _contactSheet, _constant, _backDropStr = '', '', ''
        _sortedCam = {}

        #搜索所选的内容
        if len(nuke.selectedNodes('ContactSheet')):
            _contactSheet = nuke.selectedNodes('ContactSheet')[0]

        if len(nuke.selectedNodes('Constant')):
            _constant = nuke.selectedNodes('Constant')[0]

        if len(_source) == 0:
            nuke.message("No Read Nodes Selected...")
            return

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
        if self.numSelect<=3:
            _pattern=((-1, 0), (0, 0), (1, 0))
        elif self.numSelect <= 9:
            _pattern = ((-1, -2), (-0, -2), (1, -2), \
                        (-1, -1), (0, -1), (1, -1), \
                        (-1, 0), (0, 0), (1, 0))
        else:
            _pattern = ((-3, -2), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), \
                        (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1), \
                        (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0))

        #查找输出尺寸
        # _format = nuke.knob("format").split()
        #当方格为空时创建方格，并设置它的位置
        if _contactSheet == "":
            if self.numSelect <= 3:
                _contactSheet = nuke.nodes.ContactSheet(width=_w*3,height=_h,rows=1,columns=3,roworder='TopBottom').name()
            elif self.numSelect <= 9:
                _contactSheet = nuke.nodes.ContactSheet(width=_w*3,height=_h*3,rows=3,columns=3,roworder='TopBottom').name()
            else:
                _contactSheet = nuke.nodes.ContactSheet(width=_w*6,height=_h*3,rows=3,columns=6,roworder='TopBottom').name()
            _node = nuke.toNode(_contactSheet)
            _node.setXYpos(_dot.xpos()+_bbox[0]*0,_dot.ypos()+_bbox[1]*2)
        #在所有的尺寸格式中，寻找跟素材一样样式，在创建黑板，并设置位置
        if _constant == "":
            _allFormat = nuke.formats()
            for _eachFormat in _allFormat:
                if _eachFormat.width() == _w and _eachFormat.height() == _h:
                    _constant = nuke.nodes.Constant(format=_eachFormat.name()).name()
                    _node = nuke.toNode(_constant)
                    #_node.setXYpos(_dot.xpos()+_bbox[0]*1,_dot.ypos()+_bbox[1]*-1)

        #在每个素材中记录摄像机，且记录背板的名字
        for each in _source:
            camStr = self.checkFile(each)
            if camStr:
                _sortedCam[camStr[0]] = each
                if not _backDropStr:
                    _backDropStr = camStr[1]
            else:
                each.setSelected(False)

        _sheetNode = nuke.toNode(_contactSheet)

        _conNode = nuke.toNode(_constant)

        if self.numSelect<=3:
            for _x in range(3):
                _sheetNode.setInput(_x, _conNode)
        elif self.numSelect <= 9:
            for _x in range(9):
                _sheetNode.setInput(_x, _conNode)
        else:
            for _x in range(18):
                _sheetNode.setInput(_x, _conNode)
        #判断素材的格式
        myfileFlagEXR =False
        myfileName = _source[0]['file'].value()
        myfileNameType = os.path.splitext(myfileName)[1]
        if myfileNameType:
            if myfileNameType.find('exr')>=0:
                myfileFlagEXR = True
        myii = 0
        for _k, _v in _sortedCam.iteritems():
            _sourceNode = _v
            #查找摄像机相对应的方格通道，链接，并调整位置
            if _k[0] == "_":
                myKey = _k[1::]
            else:
                myKey = _k
   
            #当时exr时，添加shuffle通道节点
            if self.mode == 1:
                if self.numSelect<=3:
                    _sheetNode.setInput(self.num3[myKey]-1,_sourceNode)
                    _pick = _pattern[self.num3[myKey]-1]
                    _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                else:
                    _sheetNode.setInput(self.num[myKey]-1,_sourceNode)
                    _pick = _pattern[self.num[myKey]-1]
                    _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                
            #当时exr时，根据需要添加shuffle通道节点 
            elif self.mode == 2: 
                if not myfileFlagEXR:
                    if self.numSelect<=3:
                        _pick = _pattern[self.num3[myKey]-1]
                        _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                        _sheetNode.setInput(self.num3[myKey]-1,_sourceNode)
                    else:
                        _pick = _pattern[self.num[myKey]-1]
                        _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                        _sheetNode.setInput(self.num[myKey]-1,_sourceNode)
                    _sourceNode.setSelected(1)
                else:
                    if myii == 0:
                        myShuffle =nuke.nodes.Shuffle()
                        myShuffle.setInput(0,_sourceNode)
                        if self.numSelect<=3:
                            _pick = _pattern[self.num3[myKey]-1]
                            _sheetNode.setInput(self.num3[myKey]-1,myShuffle)
                            _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                            myShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                        else:
                            _pick = _pattern[self.num[myKey]-1]
                            _sheetNode.setInput(self.num[myKey]-1,myShuffle)
                            _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                            myShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                    else:
                        self.setSelecteNone()
                        newMyShuffle = nuke.clone(myShuffle)
                        newMyShuffle.setInput(0, _sourceNode)
                        if self.numSelect<=3:
                            _pick = _pattern[self.num3[myKey]-1]
                            _sheetNode.setInput(self.num3[myKey]-1, newMyShuffle)
                            _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                            newMyShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                        else:
                            _pick = _pattern[self.num[myKey]-1]
                            _sheetNode.setInput(self.num[myKey]-1, newMyShuffle)
                            _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                            newMyShuffle.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
                        
            # _pick = _pattern[self.num[myKey]-1]
            # _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos()+20)
            # myShuffle.setSelected(1)
            # _sourceNode.setSelected(1)
            myii = myii + 1
        _sheetNode.setSelected(1)

        for each in _source:
            each.setSelected(1)
        #创建背板，并设置名字，
        #bd = nukescripts.autoBackdrop()
        #bd.knob('label').setValue(_backDropStr)
        _sheetNode.setXYpos(_dot.xpos()+_bbox[0]*0,_dot.ypos()+_bbox[1]*1)
        if self.numSelect ==5:
            _conNode.setXYpos(_dot.xpos()+_bbox[0]*1,_dot.ypos()+_bbox[1]*1-50)
        else:
            _conNode.setXYpos(_dot.xpos()+_bbox[0]*1+86,_dot.ypos()+_bbox[1]*1-45)

        #删除黑板
        conUsed = _conNode.dependent()

        if not conUsed:
            nuke.delete(_conNode)
        else:
            _conNode.setSelected(1)

        nuke.delete(_dot)
        bd = nukescripts.autoBackdrop()
        bd.knob('label').setValue(_backDropStr)
        myOldbdHeight = bd.knob('bdheight').value()
        bd.knob('bdheight').setValue(myOldbdHeight+15)


def doMerge(model):
    doSetup = mergeCam()
    doSetup.mergeCamera(model)

def replaceFilePath_UI():
    p = nuke.Panel('OCT_Nuke_ReplaceFilePath')
    p.setWidth(200)
    p.addSingleLineInput('New Path','')
    p.addBooleanCheckBox('All Read Nodes', False)
    p.addButton('Cancel')
    p.addButton('Apply')
    p.setWidth(350)
    result = p.show()

    if result:
        pathVal = p.value('New Path')
        allVal = p.value('All Read Nodes')
        if pathVal is not None:
            if os.path.isdir(pathVal):
                replaceFilePath(pathVal,allVal)
            else:
                nuke.message('New path not found...')
                replaceFilePath_UI()

def replaceFilePath(path,allNodes):
    if allNodes:
        sel = nuke.allNodes('Read')
    else:
        sel = nuke.selectedNodes()

    if not len(sel):
        nuke.message('Please select least Read Nodes...')
        return

    readNodes = []
    for each in sel:
        if each.Class() == 'Read':
            readNodes.append(each)

    if not len(readNodes):
        nuke.message('Please select least Read Nodes...')
        return

    newPath = path
    for each in readNodes:
        oldPath = each.knob('file').value()
        parentDir = os.path.dirname(oldPath).split('/').pop()
        bName = os.path.basename(oldPath)
        newFullPath = os.path.join(newPath,parentDir).replace('\\', '/')
        newFullPath = os.path.join(newFullPath,bName).replace('\\', '/')
        each.knob('file').setValue(newFullPath)

        oldProxy = each.knob('proxy').value()
        if oldProxy:
            parentProxy = os.path.dirname(oldProxy).split('/').pop()
            bProxy = os.path.basename(oldProxy)
            newProxy = os.path.join(newPath,parentProxy).replace('\\', '/')
            newProxy = os.path.join(newProxy,bProxy).replace('\\', '/')
            each.knob('proxy').setValue(newProxy)

def invertpath(pathname=''):
    pathname=pathname.replace('\\','/')
    if pathname[-1]!='/':
        pathname+='/'

    return pathname


def ReplaceFileRootPathUI():
    allreadfiles = nuke.selectedNodes('Read')
    if len(allreadfiles) == 0:
        allreadfiles = nuke.allNodes('Read')
    if not len(allreadfiles):
        nuke.message('no Read file ')
        return
    else:
        a = nukescripts.PythonPanel('ReplaceFileRootPath')
        a.addKnob(nuke.File_Knob('OldRootPath:'))
        #a.knobs()['OldRootPath:'].setValue('aa')
        a.addKnob(nuke.File_Knob('NewRootPath:'))
        reslut = a.showModalDialog()
        if reslut:
            oldfilepath = a.knobs()['OldRootPath:'].getValue()
            newfilepath = a.knobs()['NewRootPath:'].getValue()
            if len(oldfilepath) and len(newfilepath):
                oldfilepath = invertpath(oldfilepath)
                newfilepath = invertpath(newfilepath)
                for singleread in allreadfiles:
                    oldfile = singleread['file'].value()
                    if oldfilepath in oldfile:
                        file = oldfile.replace(oldfilepath, newfilepath)
                        singleread['file'].setValue(file)
            else:
                nuke.message('!!!no something path in OldRootPath:and NewRootPath:!!!')
    return


def Interval_frame_read_zwz():
    a = nukescripts.PythonPanel('Interval_frame_Read')
    a.addKnob(nuke.Text_Knob('Expression: (frame-X)*Y+X\nIf x and y values for empty return null!'))
    a.addKnob(nuke.Int_Knob('X:'))
    a.addKnob(nuke.Int_Knob('Y:'))
    finishedDialog = a.showModalDialog()
    oldfilepath = int(a.knobs()['X:'].getValue())
    newfilepath = int(a.knobs()['Y:'].getValue())
    nuke.selectAll()
    AllNode = nuke.selectedNodes()
    for donode in AllNode:
        donode.setSelected(0)
    if oldfilepath and newfilepath:
        for donode in AllNode:
            if donode.Class() == 'Read':
                donode.knob('frame').setValue('(frame-%s)*%s+%s' % (oldfilepath, newfilepath, oldfilepath))
    else:
        for donode in AllNode:
            if donode.Class() == 'Read':
                donode.knob('frame').setValue('')

def setAllReadsOnError():
    allmyReads = nuke.selectedNodes('Read')
    if not allmyReads:
        allmyReads = nuke.allNodes('Read')
    for myRead in allmyReads:
        myRead['on_error'].setValue('checkerboard')
        myRead['before'].setValue('black')
        myRead['after'].setValue('black')

def helpDoc():
    os.startfile(r'\\OCTVISION.com\cg\Tech\Nuke\Docs\OCT_Nuke_Tools_help.htm')

def stuffShuffleSimple():
    read_node = nuke.selectedNodes('Read')
    sel0 = read_node[0]
    chnls = sel0.channels()
    lys = list(set([ech.split('.')[0] for ech in chnls]))
    lys.sort()
    p=nuke.Panel('Merge Selected Cameras and Create Channels')
    for layer in lys:
        p.addBooleanCheckBox(layer, False)
    if not p.show():
        print("Nothing selected")
        return None
    foundLy = [ea for ea in lys if p.value(ea) ]
    foundLy.sort()
    for ea_rd in read_node:
        px,py = ea_rd.xpos() -130,ea_rd.ypos() + 135
        ea_rd.setSelected(False)
        h_bias = 140
        v_bias = 40
        pos_index = len(foundLy)
        bd_nm_str = "{}_channles".format(ea_rd.name())
        bd = None
        if nuke.exists(bd_nm_str):
            bd = nuke.toNode(bd_nm_str)
        else:
            bd = nukescripts.autoBackdrop()
            bd.knob('name').setValue("{}_channles".format(ea_rd.name()))
            bd.setXpos(px-25)
            bd.setYpos(py - 25)
            bd.knob('bdwidth').setValue(420)
        bd.selectNodes()
        exist_shfs = len(nuke.selectedNodes("Shuffle"))
        for i in range(pos_index):
            shuf_1=nuke.nodes.Shuffle()
            shuf_1['in'].setValue(foundLy[i])
            shuf_1.setInput(0,ea_rd)
            shuf_1['hide_input'].setValue(True)
            shuf_1.setName("{}_".format(foundLy[i]))
            #shuf_1.knob('label').setValue("ExShf_{}_{}".format(ea_rd.name().upper(),foundLy[i]))
            shuf_1.setXYpos(px + h_bias*((i+exist_shfs)%3),py + v_bias*((i+exist_shfs)/3))
            shuf_1.setSelected(True)
    sel_shf_nm = len(nuke.selectedNodes("Shuffle"))
    newH =  38 + ((sel_shf_nm-1)/3 + 1)*40
    bd.knob('bdheight').setValue(newH)
    for ea in nuke.selectedNodes(): ea.setSelected(False)
def stuffSuffer_auto():
    """
    auto create suffer .....
    :return:
    ben
    """
    read_node = nuke.selectedNodes('Read')
    for ea_rd in read_node:
        #ea_rd = read_node[0]
        nuke.autoplace(ea_rd)
        chnls = ea_rd.channels()
        lys = list(set([ech.split('.')[0] for ech in chnls]))
        px,py = ea_rd.xpos(),ea_rd.ypos() + 105
        ea_rd.setSelected(False)
        h_bias = 140
        v_bias = 40
        shuf_1=nuke.nodes.Shuffle()
        shuf_1['in'].setValue(lys[0])
        shuf_1.setInput(0,ea_rd)
        #shuf_1['hide_input'].setValue(True)
        shuf_1.setName("{}_".format(lys[0]))
        #shuf_1.knob('label').setValue("ExShf_{}_{}".format(ea_rd.name().upper(),foundLy[i]))
        shuf_1.setXYpos(px,py)
        shuf_1.setSelected(True)
        sel_shf_nm = len(nuke.selectedNodes("Shuffle"))
    for ea in nuke.selectedNodes(): ea.setSelected(False)