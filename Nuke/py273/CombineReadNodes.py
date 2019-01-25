# *-* coding: utf-8 *-*

import nuke

# 按路径归类Read节点
# 遍历视图中所有节点
# 遍历Input 节点中是否有Read节点
# 检测节点是否有多个，如有多个统一连到第一个
# 删除重复的Read节点

class Combine_Read_Nodes(object):
    def run(self):
        readNodeFilePathList = {}
        ReadNodes = nuke.allNodes('Read')
        for ReadNode in ReadNodes:
            filePath = ReadNode['file'].value()
            if filePath in readNodeFilePathList:
                readNodeFilePathList[filePath].append(ReadNode)
            else:
                readNodeFilePathList[filePath] = [ReadNode]

        for nodeName in nuke.allNodes():
            inputsNum = nodeName.inputs()
            if not inputsNum:
                continue
            for id in xrange(inputsNum):
                inputNodeName = nodeName.input(id)
                if inputNodeName in ReadNodes:
                    filePath = inputNodeName['file'].value()
                    if len(readNodeFilePathList[filePath]) > 1:
                        nodeName.setInput(id, readNodeFilePathList[filePath][0])

        for filePath in readNodeFilePathList:
            num = len(readNodeFilePathList[filePath])
            if num > 1:
                for id in xrange(1, num):
                    nuke.delete(readNodeFilePathList[filePath][id])
            


