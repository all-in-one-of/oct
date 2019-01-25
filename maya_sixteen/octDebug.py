# *-* coding: utf-8 *-*

# -*- coding: utf-8 -*-
import nuke, re, os, nukescripts.utils


def __init__():
    mode = 1


numSelect = 0
num = {'A': 1, '1L': 1, '1R': 1, 'B': 2, '2L': 2, '2R': 2, 'C': 3, '3L': 3, '3R': 3, 'D': 4, 'E': 5,
       'F': 6, 'G': 7, 'H': 8, 'I': 9}

num4 = {'1_A': 1, '1_B': 2, '1_C': 3, '2_A': 4, '2_B': 5, '2_C': 6, }

num6 = {'1_A': 1, '_1_A': 1, '1_B': 2, '_1_B': 2, '1_C': 3, '_1_C': 3, '1_D': 4, '_1_D': 4, '2_A': 5,
        '_2_A': 5, '2_B': 6, '_2_B': 6, '2_C': 7, '_2_C': 7, '2_D': 8, '_2_D': 8, '3_A': 9, '_3_A': 9,
        '3_B': 10, '_3_B': 10, '3_C': 11, '_3_C': 11, '_3_D': 12, '3_D': 12}

FKBSNum6 = {'1_A': 1, '_1_A': 1, '1_B': 2, '_1_B': 2, '1_C': 3, '_1_C': 3, '1_E': 4, '_1_E': 4, '1_F': 5,
            '_1_F': 5, '1_G': 6, '_1_G': 6}

SGFCNum5 = {'1_A': 1, '_1_A': 1, '1_B': 2, '_1_B': 2, '1_C': 3, '_1_C': 3, '2_A': 4, '_2_A': 4, '2_B': 5,
            '_2_B': 5, '2_C': 6, '_2_C': 6, '3_A': 7, '_3_A': 7, '3_B': 8, '_3_B': 8, '3_C': 9, '_3_C': 9}


def checkFile(readNode, FileName):
    f = readNode.knob('file').value().replace('\\', '/')


if not f:
    warnMsg('warning File')
    # basn是摄像机名、pa是路径名、pplist是路径分割后的列表
baseN = os.path.basename(f).split('.')[0]
pa = os.path.dirname(f)
ppList = pa.split('/')
backDropStr = ''

# 如果存在路径，设置backDropStr名为摄像机名，pp为摄像机名
if not pa:
    nuke.message('warning')
    return
else:
    if len(ppList):
        pp = ppList.pop()
# 判断是否有摄像机名
if not baseN:
    warnMsg('warning baseName')
    return

# 正则表达式规则：字幕和数字类型，包含有DLMRU其中2个字幕，并且有后缀名
pattern1 = re.compile('^(\w+)([ABCDEFG]{1})$')
pattern2 = re.compile('^(\w+)([ABCDEFG]{2})$')
pattern3 = re.compile('^(\w+)([1-9$_ABCDEFG]{4})$')
pattern4 = re.compile('^(\w+)([1-9$_LR]{2})$')
m = None
# pp、baseN可能是摄像机名，在这两个中匹配，匹配出一个或者两个的
nameType = None
myCameraGroup = [pp, baseN]

for i in myCameraGroup:
    if numSelect <= 3 and FileName != "CPSH":
        m = pattern2.match(i)
        if m == None:
            m = pattern1.match(i)
        if m == None:
            m = pattern4.match(i)
        if m == None:
            continue

    else:
        m = pattern3.match(i)
        if m == None:
            m = pattern2.match(i)
        if m == None:
            m = pattern1.match(i)
        if m == None:
            m = pattern4.match(i)
        if m == None:
            continue
    if m:
        nameType = myCameraGroup.index(i)
        break

# 如果存在路径，设置backDropStr名为摄像机名，pp为摄像机名
if not nameType is None:
    if nameType == 0:
        if len(ppList) and pp:
            backDropStr = ppList.pop()
    else:
        backDropStr = pp

# 如果有找到匹配的，把那个摄像机保存到result中
result = None
if m is not None:
    try:
        result = m.groups()[1]
    except:
        result = -1
print result
# 返回那个摄像机,
return [result, backDropStr]


# 去掉所有所选择的点
def setSelecteNone():
    allmySelectedNodes = nuke.selectedNodes()


if allmySelectedNodes:
    for mySelectedNode in allmySelectedNodes:
        mySelectedNode.setSelected(False)
flag = 3


def mergeCamera(flag, mymodel, FileName):


if FileName == "DNTG" and flag == 3:
    mode = 1
# 选择所有的节点
_source = nuke.selectedNodes('Read')
numSelect = len(_source)
# 定义_contactSheet方格 _constant黑板 _backDropStr背板、保存的摄像机字典
_contactSheet, _constant, _backDropStr = '', '', ''
_sortedCam = {}
# 搜索所选的内容
if len(nuke.selectedNodes('ContactSheet')):
    _contactSheet = nuke.selectedNodes('ContactSheet')[0]
if len(nuke.selectedNodes('Constant')):
    _constant = nuke.selectedNodes('Constant')[0]

if len(_source) == 0:
    nuke.message('No Read Nodes Selected...')
    return
if len(_source) != flag and (flag == 6 and flag < len(_source) and (
        FileName != "CPSH" or FileName != " FKBS") and FileName != "SGFC"):
    nuke.message(
        '\xe4\xbd\xa0\xe6\x89\x80\xe9\x80\x89\xe6\x8b\xa9\xe7\x9a\x84\xe7\xb4\xa0\xe6\x9d\x90\xe4\xb8\xaa\xe6\x95\xb0\xe4\xb8\x8e\xe4\xbd\xa0\xe9\x80\x89\xe6\x8b\xa9\xe7\x9a\x84\xe5\x90\x88\xe5\xb9\xb6\xe9\x80\x89\xe9\xa1\xb9\xe4\xb8\x8d\xe7\x9b\xb8\xe5\x90\x8c')
    return

# 以所选的第一个素材为例，定义素材的格式_w _h
_node = _source[0]
# 获取第一个素材在nuke中的位置
_w = _node.knob('format').value().width()

_h = _node.knob('format').value().height()

# 获取第一个素材的大小
_bbox = [_node.screenWidth(), _node.screenHeight()]
_pos = [_node.xpos(), _node.ypos()]

# 常见点节点，并设置它的坐标为第一个素材的节点位置
_dot = nuke.nodes.Dot()
_dot.setXYpos(_pos[0], _pos[1])

_pattern = ''
if numSelect <= 3 and FileName == "":
    _pattern = ((-1, 0), (0, 0), (1, 0))


elif numSelect <= 3 and FileName == "DNTG":
    _pattern = ((-1, 0), (0, 0), (1, 0))


elif numSelect <= 3 and FileName == "DNTG":
    _pattern = ((-1, 0), (0, 0), (1, 0))

elif numSelect == 4 and FileName == "":
    _pattern = ((-1, -1), (0, -1), (1, -1), \
                (-1, 0), (0, 0), (1, 0))

elif numSelect <= 6 and FileName == "CPSH":
    _pattern = ((-2, -2), (-1, -2), (0, -2), (1, -2), \
                (-2, -1), (-1, -1), (0, -1), (1, -1), \
                (-2, 0), (-1, 0), (0, 0), (1, 0))
elif numSelect <= 6 and FileName == "FKBS":
    _pattern = ((-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0))

elif FileName == "SGFC" and flag == 5:
    _pattern = ((-1, -2), (0, -2), (1, -2), \
                (-1, -1), (0, -1), (1, -1), \
                (-1, 0), (0, 0), (1, 0))

elif FileName == "DNTG" and flag == 3:
    _pattern = ((-1, 0), (0, 0), (1, 0))

# 当方格为空时，并设置它的坐标为第一个素材的节点位置
if _contactSheet == "":
    if numSelect <= 3 and FileName == "":
        _contactSheet = nuke.nodes.ContactSheet(width=_w * 3, height=_h * 1, rows=1, columns=3,
                                                roworder='TopButtom').name()

    if numSelect <= 3 and FileName == "DNTG":
        _contactSheet = nuke.nodes.ContactSheet(width=_w * 3, height=_h * 1, rows=1, columns=3,
                                                roworder='TopButtom').name()

    elif numSelect == 4 and FileName == "":
        _contactSheet = nuke.nodes.ContactSheet(width=_w * 3, height=_w * 2, rows=2, columns=3,
                                                roworder='TopButtom').name()

    elif numSelect <= 6 and FileName == "CPSH":
        _contactSheet = nuke.nodes.ContactSheet(width=_w * 4, height=_h * 3, rows=3, columns=4,
                                                roworder='TopButtom').name()

    elif numSelect <= 6 and FileName == "FKBS":
        _contactSheet = nuke.nodes.ContactSheet(width=_w * 6, height=_h, rows=1, columns=6,
                                                roworder='TopButtom').name()

    elif FileName == "SGFC":
        _contactSheet = nuke.nodes.ContactSheet(width=_w * 3, height=_h * 3, rows=3, columns=3,
                                                roworder='TopButtom').name()

    elif FileName == "DNTG":
        _contactSheet = nuke.nodes.ContactSheet(width=_w * 3, height=_h * 1, rows=1, columns=3,
                                                roworder='TopButtom').name()

    _node = nuke.toNode(_contactSheet)
    _node = _node.setXYpos(_dot.xpos() + _bbox[0] * 0, _dot.ypos() + _bbox[1] * 3)

# 在所有的尺寸格式中，寻找跟素材一样样式，在创建黑板，并设置位置
if _constant == "":
    _allFormat = nuke.formats()
if FileName == "DNTG":
    for _eachFormat in _allFormat:
        if _eachFormat.width() == 6858:
            _constant = nuke.nodes.Constant(format=_eachFormat.name()).name()
            _node = nuke.toNode(_constant)
            _node = _node.setXYpos(_d
            break
else:
    for _eachFormat in _allFormat:
        if _eachFormat.width() == _w and _eachFormat.height() == _h:
            _constant = nuke.nodes.Constant(format=_eachFormat.name()).name()
            _node = nuke.toNode(_constant)

if numSelect == 4 and FileName == "":
    myCrop = nuke.nodes.Crop()
    myCrop['box'].setValue([0, _w / 2, _w * 3, _w * 2])
    myCrop['reformat'].setValue(True)
    _allFormat = nuke.formats()
    for _eachFormat in _allFormat:
        if _eachFormat.width() == _w and _eachFormat.height() == _h:
            _constant1 = nuke.nodes.Constant(format=_eachFormat.name()).name()
            _node1 = nuke.toNode(_constant1)
            if not _eachFormat.name():
                widthHeight = str(_w) + " " + str(_h)
                square = widthHeight + " " + "myCrops"
                nuke.addFormat(square)
                _node1['format'].setValue("myCrops")
            break

# 在每个素材中记录摄像机，并记录黑板的名字
for each in _source:
    camStr = checkFile(each, FileName)
    if camStr:
        _sortedCam[camStr[0]] = each
        if not _backDropStr:
            _backDropStr = camStr[1]
        else:
            each.setSelected(False)
_sheeNode = nuke.toNode(_contactSheet)
_conNode = nuke.toNode(_constant)

# 根据所选的素材的个数创建ContactSheet和Constant连接的线
if numSelect == 3 and FileName == "":
    for _x in range(9):
        _sheeNode.setInput(_x, _conNode)



else:
    for _x in range(18):
        _sheeNode.setInput(_x, _conNode)
if numSelect == 4 and FileName == "":
    myCrop.setInput(0, _sheeNode)

# 判断素材的格式
myfileFlagEXR = False
# 查询第一个素材的路径
myfileName = _source[0]['file'].value()
# 获取素材的格式
myfileNameType = os.path.splitext(myfileName)[1]
if myfileNameType:
    if myfileNameType.find('exr') >= 0:
        myfileFlagEXR = True

myii = 0
myMer = 0
for _k, _v in _sortedCam.iteritems():
    # print _k,
    print(":"),
    # print _v
    _sourceNode = _v
    # 查找摄像机对应的方格通道，链接，并调整位置
    if _k[0] == "_":
        myKey = _k[1::]
    else:
        myKey = _k
        # print myKey
        # 当时exr时，添加shuffle通道节点
    if mode == 1:
        if numSelect == 3 and FileName == "DNTG":
            _sheeNode.setInput(num[myKey] - 1, _sourceNode)
            TransformNode = nuke.nodes.Transform()
            nuke.delete(_dot)
            bd = nukescripts.autoBackdrop()
            bd.knob('label').setValue(_backDropStr)
            myOldbdHeight = bd.knob('bdheight').value()
            bd.knob('bdheight').setValue(myOldbdHeight + 30)

            _pick = _pattern[num[myKey] - 1]
            # 设置素材的在nuke中的位置
            _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

        myii = myii + 1

        # FKBS特殊的比例相机
        elif numSelect == 4 and FileName == "":
        if _sourceNode.knob('format').value().height() == _sourceNode.knob('format').value().width() / 2:
            _pick = _pattern[num4[myKey] - 1]
            if myMer == 0:
                TransformNode = nuke.nodes.Transform()
                MergeNode = nuke.nodes.Merge2()
                MergeNode.setInput(1, TransformNode)
                TransformNode['translate'].setValue([0, _sourceNode.knob('format').value().height()])
                TransformNode.setInput(0, _sourceNode)

                _sheeNode.setInput(num4[myKey] - 1, MergeNode)
                MergeNode.setInput(0, _node1)
                MergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
                TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
                _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
            else:
                TransformNode = nuke.nodes.Transform()
                setSelecteNone()
                newMergeNode = nuke.clone(MergeNode)
                newMergeNode.setInput(1, TransformNode)
                TransformNode['translate'].setValue([0, _sourceNode.knob('format').value().height()])
                TransformNode.setInput(0, _sourceNode)

                _sheeNode.setInput(num4[myKey] - 1, newMergeNode)
                newMergeNode.setInput(0, _node1)
                newMergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
                TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
                _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
            myMer = myMer + 1
        else:
            _sheeNode.setInput(num4[myKey] - 1, _sourceNode)
            _pick = _pattern[num4[myKey] - 1]
            _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())


    elif numSelect <= 6 and FileName == "CPSH":
        print myKey
        _sheeNode.setInput(num6[myKey] - 1, _sourceNode)
        _pick = _pattern[num6[myKey] - 1]
        _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

    elif numSelect <= 6 and FileName == "FKBS":
        print myKey
        print FKBSNum6[myKey]
        print _pattern
        _pattern[FKBSNum6[myKey] - 1]
        _sheeNode.setInput(FKBSNum6[myKey] - 1, _sourceNode)
        _pick = _pattern[FKBSNum6[myKey] - 1]
        _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

    if FileName == "SGFC":
        _sheeNode.setInput(SGFCNum5[myKey] - 1, _sourceNode)
        _pick = _pattern[SGFCNum5[myKey] - 1]
        # 设置素材的在nuke中的位置
        _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

# 当时exr时，根据需要添加shuffle通道节点
elif mode == 2:
if numSelect == 3 and FileName == "":
    _pick = _pattern[num[myKey] - 1]
    _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
    if not myfileFlagEXR:
        _sheeNode.setInput(num[myKey] - 1, _sourceNode)
        _sourceNode.setSelected(1)
    else:
        if myii == 0:
            myShuffle = nuke.nodes.Shuffle()
            myShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(num[myKey] - 1, myShuffle)
            myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
        else:
            setSelecteNone()
            newMyShuffle = nuke.clone(myShuffle)
            newMyShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(num[myKey] - 1, newMyShuffle)
            newMyShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

# FKBS特殊的比例相机
elif numSelect == 4 and FileName == "":
    _pick = _pattern[num4[myKey] - 1]
    _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
    if not myfileFlagEXR:
        if _sourceNode.knob('format').value().height() == _sourceNode.knob(
                'format').value().width() / 2:
            if myMer == 0:
                TransformNode = nuke.nodes.Transform()
                MergeNode = nuke.nodes.Merge2()
                MergeNode.setInput(1, TransformNode)
                TransformNode['translate'].setValue([0, _sourceNode.knob('format').value().height()])
                TransformNode.setInput(0, _sourceNode)

                _sheeNode.setInput(num4[myKey] - 1, MergeNode)
                MergeNode.setInput(0, _node1)
                MergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
                TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                       _bbox[1] * _pick[1] + _dot.ypos())
                myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
                _sourceNode.setSelected(1)
            else:
                TransformNode = nuke.nodes.Transform()
                setSelecteNone()
                newMergeNode = nuke.clone(MergeNode)
                newMergeNode.setInput(1, TransformNode)
                TransformNode['translate'].setValue([0, _sourceNode.knob('format').value().height()])
                TransformNode.setInput(0, _sourceNode)

                _sheeNode.setInput(num4[myKey] - 1, newMergeNode)
                newMergeNode.setInput(0, _node1)
                newMergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                      _bbox[1] * _pick[1] + _dot.ypos())
                TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                       _bbox[1] * _pick[1] + _dot.ypos())
                myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
                _sourceNode.setSelected(1)
            myMer = myMer + 1
        else:
            _sheeNode.setInput(num4[myKey] - 1, _sourceNode)
            _pick = _pattern[num4[myKey] - 1]
            _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

    else:
        if myii == 0:
            if _sourceNode.knob('format').value().height() == _sourceNode.knob(
                    'format').value().width() / 2:
                if myMer == 0:
                    TransformNode = nuke.nodes.Transform()
                    MergeNode = nuke.nodes.Merge2()
                    MergeNode.setInput(1, TransformNode)
                    TransformNode['translate'].setValue(
                        [0, _sourceNode.knob('format').value().height()])

                    myShuffle = nuke.nodes.Shuffle()

                    TransformNode.setInput(0, _sourceNode)

                    myShuffle.setInput(0, MergeNode)

                    _sheeNode.setInput(num4[myKey] - 1, myShuffle)

                    MergeNode.setInput(0, _node1)
                    MergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                       _bbox[1] * _pick[1] + _dot.ypos())
                    TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                           _bbox[1] * _pick[1] + _dot.ypos())
                    myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                       _bbox[1] * _pick[1] + _dot.ypos())

                else:
                    TransformNode = nuke.nodes.Transform()
                    setSelecteNone()
                    newMergeNode = nuke.clone(MergeNode)
                    newMergeNode.setInput(1, TransformNode)
                    TransformNode['translate'].setValue(
                        [0, _sourceNode.knob('format').value().height()])
                    TransformNode.setInput(0, _sourceNode)
                    myShuffle = nuke.nodes.Shuffle()

                    myShuffle.setInput(0, newMergeNode)
                    _sheeNode.setInput(num4[myKey] - 1, myShuffle)

                    newMergeNode.setInput(0, _node1)
                    newMergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                          _bbox[1] * _pick[1] + _dot.ypos())
                    TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                           _bbox[1] * _pick[1] + _dot.ypos())
                    myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                       _bbox[1] * _pick[1] + _dot.ypos())
                    _sourceNode.setSelected(1)

            else:
                myShuffle = nuke.nodes.Shuffle()
                myShuffle.setInput(0, _sourceNode)
                _sheeNode.setInput(num4[myKey] - 1, myShuffle)
                myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
        else:
            if _sourceNode.knob('format').value().height() == _sourceNode.knob(
                    'format').value().width() / 2:
                if myMer == 0:
                    TransformNode = nuke.nodes.Transform()
                    MergeNode = nuke.nodes.Merge2()
                    MergeNode.setInput(1, TransformNode)
                    TransformNode['translate'].setValue(
                        [0, _sourceNode.knob('format').value().height()])

                    newMyShuffle = nuke.clone(myShuffle)

                    TransformNode.setInput(0, _sourceNode)

                    newMyShuffle.setInput(0, MergeNode)

                    _sheeNode.setInput(num4[myKey] - 1, newMyShuffle)

                    MergeNode.setInput(0, _node1)
                    MergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                       _bbox[1] * _pick[1] + _dot.ypos())
                    TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                           _bbox[1] * _pick[1] + _dot.ypos())
                    newMyShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                          _bbox[1] * _pick[1] + _dot.ypos())

                else:
                    TransformNode = nuke.nodes.Transform()
                    setSelecteNone()
                    newMergeNode = nuke.clone(MergeNode)
                    newMergeNode.setInput(1, TransformNode)
                    TransformNode['translate'].setValue(
                        [0, _sourceNode.knob('format').value().height()])
                    TransformNode.setInput(0, _sourceNode)
                    newMyShuffle = nuke.clone(myShuffle)

                    myShuffle.setInput(0, newMyShuffle)
                    _sheeNode.setInput(num4[myKey] - 1, newMyShuffle)

                    newMergeNode.setInput(0, _node1)
                    newMergeNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                          _bbox[1] * _pick[1] + _dot.ypos())
                    TransformNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                           _bbox[1] * _pick[1] + _dot.ypos())
                    newMyShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                          _bbox[1] * _pick[1] + _dot.ypos())
                    _sourceNode.setSelected(1)

            else:
                setSelecteNone()
                newMyShuffle = nuke.clone(myShuffle)
                newMyShuffle.setInput(0, _sourceNode)
                _sheeNode.setInput(num4[myKey] - 1, newMyShuffle)
                newMyShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(),
                                      _bbox[1] * _pick[1] + _dot.ypos())

elif numSelect <= 6 and FileName == "CPSH":
    _pick = _pattern[num6[myKey] - 1]
    _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
    if not myfileFlagEXR:
        _sheeNode.setInput(num6[myKey] - 1, _sourceNode)
        _sourceNode.setSelected(1)
    else:
        if myii == 0:
            myShuffle = nuke.nodes.Shuffle()
            myShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(num6[myKey] - 1, myShuffle)
            myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
        else:
            setSelecteNone()
            newMyShuffle = nuke.clone(myShuffle)
            newMyShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(num6[myKey] - 1, newMyShuffle)
            newMyShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
elif numSelect <= 6 and FileName == 'FKBS':
    _pick = _pattern[FKBSNum6[myKey] - 1]
    _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
    if not myfileFlagEXR:
        _sheeNode.setInput(FKBSNum6[myKey] - 1, _sourceNode)
        _sourceNode.setSelected(1)
    else:
        if myii == 0:
            myShuffle = nuke.nodes.Shuffle()
            myShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(FKBSNum6[myKey] - 1, myShuffle)
            myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
        else:
            setSelecteNone()
            newMyShuffle = nuke.clone(myShuffle)
            newMyShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(FKBSNum6[myKey] - 1, newMyShuffle)
            newMyShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

elif FileName == 'SGFC':
    _pick = _pattern[SGFCNum5[myKey] - 1]
    _sourceNode.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
    if not myfileFlagEXR:
        _sheeNode.setInput(SGFCNum5[myKey] - 1, _sourceNode)
        _sourceNode.setSelected(1)
    else:
        if myii == 0:
            myShuffle = nuke.nodes.Shuffle()
            myShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(SGFCNum5[myKey] - 1, myShuffle)
            myShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())
        else:
            setSelecteNone()
            newMyShuffle = nuke.clone(myShuffle)
            newMyShuffle.setInput(0, _sourceNode)
            _sheeNode.setInput(SGFCNum5[myKey] - 1, newMyShuffle)
            newMyShuffle.setXYpos(_bbox[0] * _pick[0] + _dot.xpos(), _bbox[1] * _pick[1] + _dot.ypos())

myii = myii + 1
_sheeNode.setSelected(1)

for each in _source:
    each.setSelected(1)
if numSelect == 3 and FileName == "":
    _sheeNode.setXYpos(_dot.xpos() + _bbox[0] * 0, _dot.ypos() + _bbox[1] * 2 - 30)
    _conNode.setXYpos(_dot.xpos() + _bbox[0] * 1, _dot.ypos() + _bbox[1] * 1 - 10)

elif numSelect == 4 and FileName == "":
    _sheeNode.setXYpos(_dot.xpos() + _bbox[0] * 0, _dot.ypos() + _bbox[1] * 1)
    _conNode.setXYpos(_dot.xpos() + _bbox[0] * 1, _dot.ypos() + _bbox[1] * 1 - 10)
    _node1.setXYpos(_dot.xpos() - _bbox[0] * 1, _dot.ypos() + _bbox[1] * 1 - 10)
    myCrop.setXYpos(_dot.xpos() + _bbox[0] * 0, _dot.ypos() + _bbox[1] * 1 + 30)

elif numSelect <= 6 and FileName == "CPSH":
    _sheeNode.setXYpos(_dot.xpos() + _bbox[0] * 0 - 45, _dot.ypos() + _bbox[1] * 1)
    _conNode.setXYpos(_dot.xpos() + 10, _dot.ypos() + 10)

elif numSelect <= 6 and FileName == 'FKBS':
    _sheeNode.setXYpos(_dot.xpos() + _bbox[0] * 0 - 45, _dot.ypos() + _bbox[1] * 2 - 30)
    _conNode.setXYpos(_dot.xpos() + _bbox[0] * 1, _dot.ypos() + _bbox[1] * 1 - 10)

elif FileName == 'SGFC':
    _sheeNode.setXYpos(_dot.xpos() + _bbox[0] * 0, _dot.ypos() + _bbox[1] * 2 - 30)
    _conNode.setXYpos(_dot.xpos() + _bbox[0] * 1, _dot.ypos() + _bbox[1] * 1 - 10)

    # if numSelect==3:
    # _conNode.setXYpos(_dot.xpos()+_bbox[0]*1,_dot.ypos()+_bbox[1]*1-10)

# 删除黑板
conUsed = _conNode.dependent()

if not conUsed:
    nuke.delete(_conNode)
else:
    _conNode.setSelected(1)

if numSelect == 4 and FileName == "":
    _node1.setSelected(1)
    myCrop.setSelected(1)

nuke.delete(_dot)
bd = nukescripts.autoBackdrop()
bd.knob('label').setValue(_backDropStr)
myOldbdHeight = bd.knob('bdheight').value()
bd.knob('bdheight').setValue(myOldbdHeight + 30)

# 合并选择相机的界面
mergeSelectCamUI(1)


def mergeSelectCamUI(model):
    p = nuke.Panel('Merg Select Cam Tools')


p.setWidth(100)
p.addBooleanCheckBox('TDHJ Merg 3 Cam', False)
p.addBooleanCheckBox('FKBS Merg 4 Cam', False)
p.addBooleanCheckBox('FKBS Merg 6 Cam', False)
p.addBooleanCheckBox('CPSH Merg 6 Cam', False)
p.addBooleanCheckBox('SGFC Merg 5 or 9 Cam', False)
p.addBooleanCheckBox('Merg 5 Cam', False)
p.addBooleanCheckBox('Merg 9 Cam', False)
p.addBooleanCheckBox('Merg 10 Cam', False)
p.addBooleanCheckBox('Merg 18 Cam', False)
p.addBooleanCheckBox('Merg 1 Cam', False)

p.addButton('Cancel')
p.addButton('OK')
result = p.show()
flag = ''
FileName = ""
if p.value('TDHJ Merg 3 Cam'):
    if flag == '':
        flag = 3
        FileName = ""
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('Merg 5 Cam'):
    if flag == '':
        flag = 5
        FileName = ""
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('Merg 9 Cam'):
    if flag == '':
        flag = 9
        FileName = ""
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('Merg 10 Cam'):
    if flag == '':
        flag = 10
        FileName = ""
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('Merg 18 Cam'):
    if flag == '':
        flag = 18
        FileName = ""
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('CPSH Merg 6 Cam'):
    if flag == '':
        flag = 6
        FileName = "CPSH"
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return
if p.value('FKBS Merg 4 Cam'):
    if flag == '':
        flag = 4
        FileName = ""
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('FKBS Merg 6 Cam'):
    if flag == '':
        flag = 6
        FileName = "FKBS"
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('SGFC Merg 5 or 9 Cam'):
    if flag == '':
        flag = 5
        FileName = "SGFC"
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if p.value('Merg 1 Cam'):
    if flag == '':
        flag = 1
        FileName = ""
    else:
        nuke.message('\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\x80\xe4\xb8\xaa\xef\xbc\x81')
        return

if flag and flag != 1:
    mergeCamera(flag, model, FileName)
    return
elif flag == 1:
    Merg1Cam(flag)
    return


def Merg1Cam(flag):


# 选择所有的节点
_source = nuke.selectedNodes('Read')
numSelect = len(_source)
# 定义_contactSheet方格
_contactSheet = ''

# 搜索所选的内容
if len(nuke.selectedNodes('ContactSheet')):
    _contactSheet = nuke.selectedNodes('ContactSheet')[0]

if len(_source) == 0:
    nuke.message('No Read Nodes Selected...')
    return

if len(_source) != flag:
    nuke.message(
        '\xe4\xbd\xa0\xe6\x89\x80\xe9\x80\x89\xe6\x8b\xa9\xe7\x9a\x84\xe7\xb4\xa0\xe6\x9d\x90\xe4\xb8\xaa\xe6\x95\xb0\xe4\xb8\x8e\xe4\xbd\xa0\xe9\x80\x89\xe6\x8b\xa9\xe7\x9a\x84\xe5\x90\x88\xe5\xb9\xb6\xe9\x80\x89\xe9\xa1\xb9\xe4\xb8\x8d\xe7\x9b\xb8\xe5\x90\x8c')
    return

# 以所选的第一个素材为例，定义素材的格式_w _h
_node = _source[0]
# 获取第一个素材在nuke中的位置
_w = _node.knob('format').value().width()

_h = _node.knob('format').value().height()

# 获取第一个素材的大小
_bbox = [_node.screenWidth(), _node.screenHeight()]
_pos = [_node.xpos(), _node.ypos()]

_contactSheet = nuke.nodes.ContactSheet(width=_w, height=_h, rows=1, columns=1, roworder='TopButtom').name()
_sheeNode = nuke.toNode(_contactSheet)
_sheeNodess = _sheeNode.setXYpos(_node.xpos() + _bbox[0] * 0, _node.ypos() + _bbox[1])

_sheeNode.setInput(0, _node)
_sheeNode.setSelected(1)

# newMergeCam().mergeSelectCamUI(1)