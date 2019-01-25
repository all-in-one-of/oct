# *-* coding: utf-8 *-*
import nuke,re,os,nukescripts.utils

class MergeMSS_sc14_Cam():
    def __init__(self):
        self.num = {"L":1, "_L":1, "R":2, "_R":2}

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
        pattern1 = re.compile('^(\w+)([LR]{1})$')
        pattern2 = re.compile('^(\w+)([LR]{2})$')
        #pattern3 = re.compile('^(\w+)([$_LR]{4})$')
        m = None
        #pp、baseN可能是摄像机名，在这两个中匹配，匹配出一个或者两个的
        nameType = None
        myCameraGroup = [pp, baseN]
        for i in myCameraGroup:
            # if self.numSelect <= 9:
            m = pattern2.match(i)
            if m == None:
                m = pattern1.match(i)
                if m == None:
                    continue
            # else:
            #     m = pattern3.match(i)
            #     if m == None:
            #         m = pattern2.match(i)
            #         if m == None:
            #             m = pattern1.match(i)
            #             if m == None:
            #                 continue
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


    def mergeMSSCam(self):
        _source = nuke.selectedNodes('Read')
        if len(_source)==0:
            nuke.message('No Read Nodes Selected...')
            return
        #以所选的第一个素材为例，定义素材的格式_w _h
        _node = _source[0]
        #获取第一个素材在nuke中的位置
        _w = _node.knob('format').value().width()
  
        _h = _node.knob('format').value().height()

        _bbox = [_node.screenWidth(),_node.screenHeight()]
        _pos = [_node.xpos(),_node.ypos()]
        #常见点节点，并设置它的坐标为第一个素材的节点位置
        _dot=nuke.nodes.Dot()
        _dot.setXYpos(_pos[0],_pos[1])

        _pattern = ((0,0),(1,0))

        #保存的摄像机字典
        _sortedCam = {}
        _constant = ""
        _backDropStr = ""
        j = 0  

        flag = True


        _contactSheet = nuke.nodes.ContactSheet(width=_w*2,height=_h,rows=1,columns=2,roworder='TopBottom').name()
        _node = nuke.toNode(_contactSheet)
        _node.setXYpos(_dot.xpos()+_bbox[0]*0,_dot.ypos()+_bbox[1]*2)

        for each in _source:
            camStr = self.checkFile(each)
            if camStr:
                _sortedCam[camStr[0]] = each
                if not _backDropStr:
                    _backDropStr = camStr[1]
            else:
                each.setSelected(False)

        _sheetNode = nuke.toNode(_contactSheet)

        for _k, _v in _sortedCam.iteritems():
            _sourceNode = _v
            #查找摄像机相对应的方格通道，链接，并调整位置
            if _k[0] == "_":
                myKey = _k[1::]
            else:
                myKey = _k
   
            _sheetNode.setInput(self.num[myKey]-1,_sourceNode)
            _pick = _pattern[self.num[myKey]-1]
            _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())


        
        #在所有的尺寸格式中，寻找跟素材一样样式，在创建黑板，并设置位置
        # flag = True
        # if _constant == "":
        #     _allFormat = nuke.formats()
        #     _constant = nuke.nodes.Constant()
        #     for _eachFormat in _allFormat:
        #         if _eachFormat.width() == _w*2 and _eachFormat.height() == _h:
        #             myFormat = _eachFormat.name()
        #             if myFormat != None:
        #                 _constant['format'].setValue(myFormat)
        #                 flag = False
        #                 break
        #     if flag:
        #         while True:
        #             mySize = ('my_Size%s' % j)
        #             if mySize not in [eachFormat.name() for eachFormat in _allFormat]:
        #                 break
        #             else:
        #                 j += 1
        #         widthHeight = str(_w*2) + " " + str(_h)
        #         square = widthHeight+" "+mySize
        #         nuke.addFormat(square)
        #         _constant['format'].setValue(mySize)

        #     _node = nuke.toNode(_constant.name())


        # #在每个素材中记录摄像机，并记录黑板的名字
        # for each in _source:
        #     camStr = self.checkFile(each)
        #     #print camStr
        #     if camStr:
        #         _sortedCam[camStr[0]] = each
        #         if not _backDropStr:
        #             _backDropStr = camStr[1]
        #         else:
        #             each.setSelected(False)

        # #判断素材的格式
        # myfileFlagEXR =False
        # myfileName = _source[0]['file'].value()
        # myfileNameType = os.path.splitext(myfileName)[1]
        # if myfileNameType:
        #     if myfileNameType.find('exr')>=0:
        #         myfileFlagEXR = True

       
        # MergeNode=nuke.nodes.Merge2()
        # for _k, _v in _sortedCam.iteritems():
        #     _sourceNode = _v
        #     #查找摄像机相对应的方格通道，链接，并调整位置
        #     if _k[0] == "_":
        #         myKey = _k[1::]
        #     else:
        #         myKey = _k
   
        #     #当时exr时，添加shuffle通道节点
            
        #     _pick=_pattern[self.num[myKey]-1]
        #     _sourceNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos())
        #     TransformNode = nuke.nodes.Transform()
        #     TransformNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos(),_bbox[1]*_pick[1]+_dot.ypos()+_bbox[1]+10)
        #     TransformNode.setInput(0, _sourceNode)
        #     if int(self.num[myKey]) == 1:
        #         MergeNode.setInput(int(self.num[myKey]), TransformNode)
        #     else:
        #         TransformNode['translate'].setValue([_w, 0])
        #         MergeNode.setInput(int(self.num[myKey])+1, TransformNode)

           
        # MergeNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos()+30,_bbox[1]*_pick[1]+_dot.ypos()+_bbox[1]+40)
        # MergeNode.setInput(0, _node)
        
        # _node.setXYpos(_bbox[0]*_pattern[0][0]-_bbox[0]+_dot.xpos(), _bbox[1]*1+_dot.ypos()) 

       
        _sheetNode.setXYpos(_bbox[0]*_pick[0]+_dot.xpos()+30,_bbox[1]*_pick[1]+_dot.ypos()+_bbox[1]+40)

        nuke.delete(_dot)
        self.setSelecteNone()
        for each in _source:
            each.setSelected(1) 
        _node.setSelected(1) 

        bd=nukescripts.autoBackdrop()
        bd.knob('label').setValue(_backDropStr)
        myOldbdHeight = bd.knob('bdheight').value()
        bd.knob('bdheight').setValue(myOldbdHeight+80)

#MergeMSS_sc14_Cam().mergeMSSCam()