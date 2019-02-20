#!/usr/bin/python
# -*- coding: utf-8 -*- 
import re
import maya.cmds as mc
import maya.mel as mm
import maya.utils as mu
import os

class CreateAnimationForUnity_zwz():
    def __init__(self):
        #UI
        self._windowSize = (700, 308)
        self._windowName = 'OCT_CreateAnimationForUnityUI_zwz1'
        self._textFG = 'LongValue'
        self._textDateFBG = 'pathTextFB'
        self._textTranFBG = 'TranTextFB'
        self._TranValue = 0.0
        self._endFrameV = 0 #结束帧
        self._TranDict = {}#位移字典
        self._tranDVBG = []#位移变量数组 非常重要
        self._myCube = ''
        self._dateFileName = '' #数据文件地址
        self._tranFileName = '' #位置融合数据

    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName, window=True)
        if mc.windowPref(self._windowName, q=True, exists=True):
            mc.windowPref(self._windowName, remove=True)
            
    def show(self):
        self.close()
        #make the window
        win = mc.window(self._windowName, title=u"导入数据生成动画_zwz", menuBar=True, widthHeight=self._windowSize, sizeable=False)
        mc.columnLayout()
        mc.text( label=u'''根据采集的数据,生成25帧的路径。   \n操作步骤：\n第一步:输入间距，选择采集数据文件，点击生成路径。
第二步：根据路径，创建一个Txt文件，内容要求如下：
开始帧到段结束帧，倍率，融合帧范围
1-580,0.1,00 (第一段，第一个必须为去，第一段融合帧要为0)
581-1250,1,100（开始帧和上一帧差值为1）
1251-2000,4,50 (融合值不易太大)
2001-3550,1,100
3551-4377,4,50
4378-5286,1,100（结束帧为实际动画的帧数）''', 
            align='left' )
        mc.textFieldGrp(self._textFG, label=u'请输入路径间距(0.01-100):', cw2=[150, 30], cal=[1, 'left'], text='1' )
        mc.textFieldButtonGrp(self._textDateFBG, label=u'采集数据文件路径：',  ed=False, text='',columnWidth3=[109,525,100], buttonLabel=u'选择文件', bc=self.fileDateGet)
        mc.textFieldButtonGrp(self._textTranFBG, label=u'动态位置文件路径：',  ed=False, text='',columnWidth3=[109,525,100], buttonLabel=u'选择文件', bc=self.fileTranGet)
        mc.button('new',label=u'点击生成',w=700,h=35, bgc=[100, 20,0], c=self.Doit)
        mc.showWindow(win)
        
    def fileDateGet(self):
        getFileName = []
        getFileName = mc.fileDialog2(fileMode=1, caption="选择文件")
        self._dateFileName = ''
        if getFileName:
            self._dateFileName = getFileName[0]
            if self.getEndFrameV():
                print getFileName
                mc.textFieldButtonGrp(self._textDateFBG, e=True, text=self._dateFileName)
            else:
                mc.textFieldButtonGrp(self._textDateFBG, e=True, text='')
        else:
            mc.textFieldButtonGrp(self._textDateFBG, e=True, text='')


    def fileTranGet(self):
        if self._dateFileName:
            getFileName = []
            getFileName = mc.fileDialog2(fileMode=1, caption="选择文件")
            self._tranFileName = ''
            if getFileName:
                self._tranFileName = getFileName[0]
                if self.getTranDict():
                    print self._tranFileName
                    mc.textFieldButtonGrp(self._textTranFBG, e=True, text=self._tranFileName)
                else:
                    mc.textFieldButtonGrp(self._textTranFBG, e=True, text='')
            else:
                mc.textFieldButtonGrp(self._textTranFBG, e=True, text='')
        else:
            mc.confirmDialog(title=u"提示", message=u'请先选择采集数据文件！')
    
    #检查数据文件是否是有效的文件
    def getEndFrameV(self, *args):
        FileTex = open(self._dateFileName)
        self._endFrameV = 0
        ErrorFlag = True
        i = 0
        for line in FileTex:
            i+=1
            if line.find("Index")>=0:
                #读取帧数，并设置帧数
                FrameFL = re.findall(r"Index:(.+?),", line)
                if FrameFL:
                    FrameNum =  int(FrameFL[0])
                    if FrameNum%4==0:
                        rotaFV = re.findall(r"\((.+?)\)", line)
                        if rotaFV:
                            self._endFrameV += 1
                            ErrorFlag = False
                        else:
                            ErrorFlag = True
                            print 1
                            break
                else:
                    print 2
                    ErrorFlag = True
                    break
        print ErrorFlag
        if not ErrorFlag:
            if self._endFrameV > 0:
                return True
            else:
                mc.confirmDialog(title=u"提示",message=u'采集的数据文件没有有效数据！\n请检查一下选择的文件是否有错！')
                return False
        else:
            mc.confirmDialog(title=u"提示",message=u'采集的数据 %s 文件在第%s行数据存在异常\n请自行修改采集的数据文件后保存并重新加载！' % (os.path.basename(self._dateFileName),i))
            self._endFrameV = 0
            return False

    #检查位置文件的是否符合规范
    def getTranDict(self, *args):
        tranTexLen = len(open(self._tranFileName).readlines())
        myFile = open(self._tranFileName)
        i=0
        DeafV = 0 #默认数据
        self._TranDict.clear() #位移字典
        qFlag = 0 #数据为0
        OneNumNow = 0
        TwoNumNow = 0
        OneNumBefore = 0
        TwoNumBefore = 0
        moveVList = []
        Trantransit = 0
        #判断偏移值文本数据是否正常,并把数据保存到字典中
        for line in myFile:
            i+=1
            lineTex = line.split(",")
            if len(lineTex)!=3:
                #数据存在非法数据
                self._TranDict.clear()
                mc.confirmDialog(title=u"提示", message=u'第%s行存在非法数据!\n当前行的数字结构不对！' % i)
                break
            if lineTex[0].find("-") < 0:
                #数据存在非法数据
                self._TranDict.clear()
                mc.confirmDialog(title=u"提示", message=u'第%s行存在非法数据!\n帧数字符串结构不对！' % i)
                break
            else:
                #判断数据是否为数字
                NumA = lineTex[0].split("-")
                if i == 1 and NumA[0] != "1" and lineTex[2] != "0":
                    self._TranDict.clear()
                    mc.confirmDialog(title=u"提示", message=u'存在非法数据!\n第一个数字必须为1,且位移过度值为0')
                    break
                try:
                    OneNumNow = int(NumA[0])
                    TwoNumNow = int(NumA[1])
                    float(lineTex[1])
                    Trantransit = int(lineTex[2])
                except:
                    self._TranDict.clear()
                    mc.confirmDialog(title=u"提示", message=u'第%s行存在非法数据!\n存在非数字字符串！\n要求第1、2、4位整数；第2可带小数' % i)
                    break
                #过渡至为非偶数时
                if Trantransit%2 != 0:
                    self._TranDict.clear()
                    mc.confirmDialog(title=u"提示", message=u'存在非法数据！\n第%s行的位移融合值要为偶数' % i)
                    break
                if i == 1:
                    qFlag = TwoNumNow
                    OneNumBefore = OneNumNow
                    TwoNumBefore = TwoNumNow
                else:
                    #位移过度值取值不对
                    print Trantransit,TwoNumNow, TwoNumBefore, OneNumNow,OneNumBefore
                    if (Trantransit/2>(TwoNumNow-TwoNumBefore)/2) or (Trantransit/2>(OneNumNow-OneNumBefore)/2):
                        self._TranDict.clear()
                        mc.confirmDialog(title=u"提示", message=u'存在非法数据！\n第%s行的第四位的位移过渡值过大'%i)
                        break
                    else:
                        OneNumBefore = OneNumNow
                        TwoNumBefore = TwoNumNow
                    #帧数取值不对
                    if i == tranTexLen:
                        if TwoNumNow<=OneNumNow:
                            self._TranDict.clear()
                            mc.confirmDialog(title=u"提示", message=u'存在非法数据！\n最后一行的结束帧不可小于或等于开始帧！')
                            break
                        if TwoNumNow!=self._endFrameV:
                            print TwoNumNow,self._endFrameV
                            self._TranDict.clear()
                            mc.confirmDialog(title=u"提示", message=u'存在非法数据！\n最后一行的结束帧跟动画结束帧不一致！')
                            break
                    else:
                        ##判断数据是否连续
                        # print OneNumNow,qFlag
                        if OneNumNow != (qFlag+1):
                            # print OneNumNow,qFlag
                            self._TranDict.clear()
                            mc.confirmDialog(title=u"提示", message=u'存在非法数据！\n第%s行的开始帧跟上一行的结束帧不连续！' % i)
                            break
                        else:
                            qFlag = TwoNumNow
                self._TranDict[lineTex[0]]=[lineTex[1],lineTex[2].strip()]
        if self._TranDict: 
            return True
        else:
            return False

    def GetMoveList(self, *args):
        myFile = open(self._tranFileName)
        #TranRangeList = self._TranDict.keys()
        #TranRangeList.reverse()
        self._tranDVBG = []  #位移过度值变量数组，最重要的
        tranDVB = 0
        changeFrameTemp = 0 #位移过度量记录 
        groupFame = []
        f = 0
        for line in myFile:
            f+=1
            lineTex = line.split(",")[0]
            groupFame.append(lineTex)
        i = 0
        jj = 0
        changeValueAfter = 0
        Framelen = len(groupFame)
        for TranRangeV in groupFame:
            i+=1
            #分理处开始和结束帧
            numList = TranRangeV.split("-")
            OneNum = int(numList[0])   #开始帧
            TwoNum = int(numList[1])   #结束帧
            changeValueNow = self._TranDict[TranRangeV][1]  #当前的位移融合值变量值
            #生明
            changeValueAfter = 0  #下一帧过度融合帧数值
            changeFrameD = 0    #末端帧数处理范围
            if i==1:
                #获取倍数
                tranDVBNow = float(self._TranDict[TranRangeV][0])
                tranDVBAfter = float(self._TranDict[groupFame[i]][0])
                #多少帧处理完毕
                changeValueAfter = int(self._TranDict[groupFame[i]][1])
                changeFrameD = int(changeValueAfter)/2
                #print changeFrameD,changeValueAfter,changeValueNow
                #分2段处理
                FisrDoNum = OneNum
                SecondDoNum = TwoNum-changeFrameD
                ThirdDoNum = TwoNum
                for j in range(FisrDoNum, SecondDoNum+1):
                    self._tranDVBG.append(tranDVBNow)
                #取过度值
                tranDVB = (tranDVBAfter-tranDVBNow)/changeValueAfter
                b = 1
                for k in range(SecondDoNum+1, ThirdDoNum+1):
                    tranTemp = tranDVB*b
                    self._tranDVBG.append(tranDVBNow+tranTemp)
                    b+=1
                changeFrameTemp = changeFrameD
                # print self._tranDVBG
                #print len(self._tranDVBG)
            elif i==Framelen:
                #获取倍数
                tranDVBNow = float(self._TranDict[TranRangeV][0])
                #分2段处理
                FisrDoNum = OneNum
                SecondDoNum = OneNum+changeFrameTemp
                ThirdDoNum = TwoNum
                #第一段
                bbb=changeFrameTemp
                for jjj in range(FisrDoNum, SecondDoNum):
                    bbb-=1
                    tranTemp = tranDVB*bbb
                    #print tranTemp
                    self._tranDVBG.append(tranDVBNow-tranTemp)
                # print self._tranDVBG
                # print len(self._tranDVBG)
                for kk in range(SecondDoNum, ThirdDoNum+1):
                    self._tranDVBG.append(tranDVBNow)
                # print self._tranDVBG
                # print len(self._tranDVBG)
            else:
                        #获取倍数
                tranDVBNow = float(self._TranDict[TranRangeV][0])
                tranDVBAfter = float(self._TranDict[groupFame[i]][0])
                #多少帧处理完毕、末端
                changeValueAfter = int(self._TranDict[groupFame[i]][1])
                changeFrameD = int(changeValueAfter)/2
                #分三段,前面缓环节,后面环节
                FisrDoNum = OneNum
                SecondDoNum = OneNum+changeFrameTemp
                ThirdDoNum = TwoNum-changeFrameD
                fourDoNum = TwoNum
                #print FisrDoNum,SecondDoNum,ThirdDoNum
                bb=changeFrameTemp
                for jj in range(FisrDoNum, SecondDoNum):
                    bb-=1
                    tranTemp = tranDVB*bb
                    #print tranTemp
                    self._tranDVBG.append(tranDVBNow-tranTemp)
                    
                # print self._tranDVBG
                # print len(self._tranDVBG)
                for kk in range(SecondDoNum, ThirdDoNum+1):
                    self._tranDVBG.append(tranDVBNow)
                # print self._tranDVBG
                # print len(self._tranDVBG)
                tt=1
                #重新去过度值
                tranDVB = (tranDVBAfter-tranDVBNow)/changeValueAfter
                for vv in range(ThirdDoNum, fourDoNum):
                    tranTemp = tranDVB*tt
                    self._tranDVBG.append(tranDVBNow+tranTemp)
                    tt+=1
                # print self._tranDVBG
                # print len(self._tranDVBG)
                changeFrameTemp = changeFrameD

    def CreateAni(self, *args):
        #创建cube
        if mc.objExists("myAniCube"):
            mc.delete("myAniCube")
        self._myCube = mc.polyCube(n="myAniCube")[0]
        f = open(self._dateFileName)             # 返回一个文件对象  
        line = f.readline()             # 调用文件的 readline()方法 
        FrameValue = 0
        SecTime = 0 
        rotaFV = ""
        while line:  
            #print line                 # 后面跟 ',' 将忽略换行符  
            # print(line, end = '')　　　# 在 Python 3中使用
            if line.find("Index")>=0:
                #读取帧数，并设置帧数
                FrameFL = re.findall(r"Index:(.+?),", line)
                if FrameFL:
                    FrameNum =  int(FrameFL[0])
                    if FrameNum%4==0:
                        FrameValue += 1
                        mc.currentTime(FrameValue, u=False)
                        #读取旋转值，并旋转
                        rotaFV = re.findall(r"\((.+?)\)", line)
                        if rotaFV:
                            rotaFL = rotaFV[0].split(",")
                            mc.rotate(rotaFL[0], -float(rotaFL[1]), rotaFL[2], self._myCube, a=True)
                            mc.setKeyframe("%s.rotate" % self._myCube)
                            #设置位置值
                            if self._tranDVBG:
                                mc.move(0, 0, self._TranValue*self._tranDVBG[FrameValue-1], self._myCube, r=True, os=True, wd=True)
                            else:
                                mc.move(0, 0, self._TranValue, self._myCube, r=True, os=True, wd=True)
                            mc.setKeyframe("%s.t" % self._myCube)
            elif line.find("save")>=0:
                SecTime+=1
                # print SecTime
            else:
                pass
            line = f.readline() 
        f.close()
        tmpSnap = []
        tmpSnapShape = ""
        if FrameValue >= 1:
            mc.playbackOptions(min=1, ast=1, max=FrameValue, aet=FrameValue)
            tmpSnap = mc.snapshot(self._myCube, mt=True, startTime=0, endTime=FrameValue, increment=1)
            tmpSnapShape = mc.listRelatives(tmpSnap[0])[0]
            print tmpSnapShape
            mc.setAttr("%s.showFrames" % tmpSnapShape, 1)
            mc.currentTime(1, u=True)

    def Doit(self, *args):
        self._tranDVBG=[]
        mc.currentUnit(t="pal") #设置帧率
        mc.playbackOptions(min=1, ast=1, max=25, aet=25)
        self._TranValue = float(mc.textFieldGrp(self._textFG, tx=True, q=True))
        if (self._TranValue>0.01) & (self._TranValue<=100.0):
            if self._dateFileName and self._dateFileName[-4::]==".txt":
                if self._tranFileName:
                    self.GetMoveList()
                    #print self._tranDVBG
                mu.executeInMainThreadWithResult(self.CreateAni)
            else:
                mc.confirmDialog(title=u"提示",message=u'请选择采集数据的txt文件！')
        else:
            mc.confirmDialog(title=u"提示",message=u'输入的间距值在0到10之前!\n请重新输入')
    


# i= CreateAnimationForUnity_zwz()
# i.show()