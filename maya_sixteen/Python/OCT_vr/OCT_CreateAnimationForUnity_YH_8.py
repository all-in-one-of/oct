#!/usr/bin/python
# -*- coding: utf-8 -*- 
import maya.cmds as mc
import maya.mel as mm
import re
import maya.utils as mu
import os

class CreateAnimationForUnity():
    def __init__(self):
        self._windowSize = [400, 550]
        self._windowName  = 'OCT_CreateAnimationForUnityUI'
        self._textDateFBG = 'pathTextFB'
        self._textTranFBG = 'TranTextFB'
        self._textSub = 'Subsection'
        self._textFG = 'LongValue' 
        self._textDateFBG = 'pathTextFB'
        self._textTranFBG = 'TranTextFB'
        self._textSaveFBG = 'SaveTextFB'        
        self._TranValue = 0.0
        self._endFrameV = 0 #����֡
        self._TranDict = {}#λ���ֵ�
        self._tranDVBG = []#λ�Ʊ������� �ǳ���Ҫ
        self._myCube = ''
        self._dateFileName = '' #�����ļ���ַ
        self._tranFileName = '' #λ���ں�����  

        self._textSubT = ''     
    
    def close(self):
        if mc.window(self._windowName, q=True, exists=True):
            mc.deleteUI(self._windowName, window=True)
        if mc.windowPref(self._windowName, q=True, exists=True):
            mc.windowPref(self._windowName, remove=True)
                       

    def show(self):
        self.close()
        win = mc.window(self._windowName, t = u'�����������ɶ���', widthHeight = self._windowSize)
        mc.formLayout('formLyt', numberOfDivisions=100)
        one = mc.columnLayout('First_Set', parent = 'formLyt')
        
        mc.rowLayout('PathRow', numberOfColumns = 3, columnAttach3 = ['left','left','left'], columnWidth3 = [5, 260, 35], columnOffset3 =[2, 2, 2], adjustableColumn3 = True, parent = 'First_Set')
        mc.textFieldButtonGrp(self._textDateFBG, label=u'�ɼ������ļ�·����',  ed=False, text='',columnWidth3=[109,230,100], buttonLabel=u'ѡ���ļ�', bc=self.fileDateGet)

        mc.rowLayout('oneRow', numberOfColumns = 3, columnAttach3 = ['left','left','left'], columnWidth3 = [5,260,35], columnOffset3 =[2,2,2], adjustableColumn3 = True, parent = 'First_Set')
        mc.textFieldButtonGrp(self._textTranFBG, label=u'��̬�ļ���ȡ·����',  ed=False, text='',columnWidth3=[109,230,100], buttonLabel=u'ѡ���ļ�', bc=self.fileTranGet)

        mc.rowLayout('addRow', numberOfColumns = 3, columnAttach3 = ['left','left','left'], columnWidth3 = [5,260,35], columnOffset3 =[2,2,2], adjustableColumn3 = True, parent = 'First_Set')
        mc.textFieldButtonGrp(self._textSaveFBG, label=u'��̬�ļ�����·����',  ed=False, text='',columnWidth3=[109,230,100], buttonLabel=u'�����ļ�', bc= self.fileSaveGet)

        mc.rowLayout('twoRow',numberOfColumns = 4, columnAttach4 = ['left','left','left','left'], columnWidth4 = [5,68,70,88], columnOffset4 =[2,2,10,15], adjustableColumn4 = True, parent = 'First_Set')
        mc.text(label=u'��ʼ֡��', w = 68, parent = 'twoRow')
        mc.textField('startFrame', text = '1', width = 80, alwaysInvokeEnterCommandOnReturn= True, parent = 'twoRow')
        mc.text(label=u'����֡��', w = 68,parent = 'twoRow')
        mc.textField('endFrame', text = '25', width = 80, alwaysInvokeEnterCommandOnReturn= True, parent = 'twoRow')
        
        mc.rowLayout('threeRow', numberOfColumns = 5, columnAttach5 = ['left', 'left', 'left', 'left', 'left'], columnWidth5 = [50, 50, 50, 35, 35], columnOffset5 =[10, 10, 10,10,20], adjustableColumn5 = True, parent = 'First_Set')
        mc.textField(self._textSub, text = '1', width = 40, alwaysInvokeEnterCommandOnReturn= True, parent = 'threeRow')      
        mc.button(l = u'�����ֶε�', width = 60, command = lambda *arg:self.Subsection() , parent = 'threeRow')        
        mc.text(label=u'��������', w = 60, parent = 'threeRow')
        mc.textFieldGrp(self._textFG, cw2=[150, 50], cal=[1, 'left'], text='1' , parent = 'threeRow')              
        mc.button(l = u'����', width = 150, parent = 'threeRow',c= self.Doit)
        
        mc.setParent('First_Set')
        two =mc.scrollLayout('Subsection_set',horizontalScrollBarThickness=16,verticalScrollBarThickness=16, w = 400,h = 400)
        mc.rowLayout('fourRow', adjustableColumn1 = True, backgroundColor = [0.1 , 0.1 , 0.1], w = 400, parent = 'Subsection_set')
        mc.text(l = u'-------------------------------------------�ֶ�����-------------------------------------------', parent = 'fourRow')        
        mc.rowColumnLayout('fiveRow', numberOfColumns=3, columnWidth=[(1, 60), (2, 80), (3, 90)], parent = 'Subsection_set')
        mc.text(l = u'ÿ����ʼ֡', parent = 'fiveRow')
        mc.text(l = u'ͷβ�ں�֡', parent = 'fiveRow')
        mc.text(l = u'��������', parent = 'fiveRow')
    
        self.Subsection()

        mc.showWindow(win)

#�ֶδ���

    def Subsection(self):
        _sd = mc.textField('startFrame', query=True, text = True, alwaysInvokeEnterCommandOnReturn= True)         
        _ed = mc.textField( 'endFrame' , query=True, text = True, alwaysInvokeEnterCommandOnReturn= True)         
        self._textSubT = mc.textField(self._textSub, query=True, text=True)
        if self._textSubT!="":
            num = ""
            j = 0
            while True:
                if mc.rowLayout('fiveRow%s'%j, q = True, ex = True):
                    mc.deleteUI('fiveRow%s'%j)
                    j = j + 1
                else:
                    break
              
            num = int (self._textSubT)
            fsd = int (_sd)
            fed = int (_ed)
            	            
            for i in range(num):  
                mc.rowLayout('fiveRow%s'%i, numberOfColumns = 3,columnAttach3 = ['left', 'left', 'left'],columnWidth3 = [60, 70, 180], columnOffset3 =[15, 15, 2], adjustableColumn3 = True, parent = 'Subsection_set')
                mc.textField('frame%s'%i, tx = (fed-fsd)*i/num+fsd, h = 20, parent = 'fiveRow%s'%i) #����ÿ�εĿ�ʼ֡
                if i < 1 :
                   mc.textField('fuse%s'%i, tx = 0, w = 50, h = 20,parent = 'fiveRow%s'%i)
                else :
                   mc.textField('fuse%s'%i, tx = i/i*4, w = 50, h = 20,parent = 'fiveRow%s'%i) #�����ں�ֵ���ʣ�Ϊż��
                mc.floatSliderGrp('scale%s'%i, v = 1, w = 250, h = 20, field = True, min = 0.1, max = 2, parent = 'fiveRow%s'%i)


#ѡ�������ļ�·��
       
    def fileDateGet(self):
        getFileName = []
        getFileName = mc.fileDialog2(fileMode=1, caption="ѡ���ļ�")
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
            
#���������ļ�·��
       
    def fileSaveGet(self):
    	num = int(self._textSubT)
    	getTxtFileName = []
    	
        multipleFilters = "txt Files (*.txt);;All Files (*.*)"
        getTxtFileName = mc.fileDialog2(fileMode=0, fileFilter = multipleFilters , caption="�����ļ�")

        self._saveFileName = ''
        if getTxtFileName:
            self._saveFileName = getTxtFileName[0]
            mc.textFieldButtonGrp(self._textSaveFBG, e = True, text = getTxtFileName[0])
      
            path = getTxtFileName[0]
            f = open(path,'wt')
        
            frameDir = []
            fuseDir = []
            scaleDir = []

            for i in range(num):
                frame = mc.textField('frame%s'%i, q = True, tx = True)
                fuse = mc.textField('fuse%s'%i, q = True, tx = True)
                scale = mc.floatSliderGrp('scale%s'%i, q = True, v = True)

                frameDir.append(frame)
                fuseDir.append(fuse)
                scaleDir.append(scale)

            number = len(frameDir)
            _ed = mc.textField( 'endFrame' , query=True, text = True) 

            for i in range(number):
                subEndFrame = '' #ÿһ�ν���֡
                if i == number - 1:
                    subEndFrame = _ed
                else:
                    subEndFrame = int(frameDir[i+1]) - 1

                strs = '%s-%s,%s,%s'%(frameDir[i],subEndFrame,scaleDir[i],fuseDir[i])
                f.write(strs)
                f.write("\n")
            f.close()
        else:
            mc.textFieldButtonGrp(self._textSaveFBG, e=True, text='')
            
#ѡ��ʰȡ��̬���ļ�

    def fileTranGet(self):
        if self._dateFileName:
            getFileName = []
            getFileName = mc.fileDialog2(fileMode=1, caption="ѡ���ļ�")
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
            mc.confirmDialog(title=u"��ʾ", message=u'����ѡ��ɼ������ļ���')
    
    #��������ļ��Ƿ�����Ч���ļ�
    def getEndFrameV(self, *args):
        FileTex = open(self._dateFileName)
        self._endFrameV = 0
        ErrorFlag = True
        i = 0
        for line in FileTex:
            i+=1
            if line.find("Index")>=0:
                #��ȡ֡����������֡��
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
                mc.confirmDialog(title=u"��ʾ",message=u'�ɼ��������ļ�û����Ч���ݣ�\n����һ��ѡ����ļ��Ƿ��д�')
                return False
        else:
            mc.confirmDialog(title=u"��ʾ",message=u'�ɼ������� %s �ļ��ڵ�%s�����ݴ����쳣\n�������޸Ĳɼ��������ļ��󱣴沢���¼��أ�' % (os.path.basename(self._dateFileName),i))
            self._endFrameV = 0
            return False

    #���λ���ļ����Ƿ���Ϲ淶
    def getTranDict(self, *args):
        tranTexLen = len(open(self._tranFileName).readlines())
        myFile = open(self._tranFileName)
        i=0
        DeafV = 0 #Ĭ������
        self._TranDict.clear() #λ���ֵ�
        qFlag = 0 #����Ϊ0
        OneNumNow = 0
        TwoNumNow = 0
        OneNumBefore = 0
        TwoNumBefore = 0
        moveVList = []
        Trantransit = 0
        #�ж�ƫ��ֵ�ı������Ƿ�����,�������ݱ��浽�ֵ���
        for line in myFile:
            i+=1
            lineTex = line.split(",")
            if len(lineTex)!=3:
                #���ݴ��ڷǷ�����
                self._TranDict.clear()
                mc.confirmDialog(title=u"��ʾ", message=u'��%s�д��ڷǷ�����!\n��ǰ�е����ֽṹ���ԣ�' % i)
                break
            if lineTex[0].find("-") < 0:
                #���ݴ��ڷǷ�����
                self._TranDict.clear()
                mc.confirmDialog(title=u"��ʾ", message=u'��%s�д��ڷǷ�����!\n֡���ַ����ṹ���ԣ�' % i)
                break
            else:
                #�ж������Ƿ�Ϊ����
                NumA = lineTex[0].split("-")
                if i == 1 and NumA[0] != "1" and lineTex[2] != "0":
                    self._TranDict.clear()
                    mc.confirmDialog(title=u"��ʾ", message=u'���ڷǷ�����!\n��һ�����ֱ���Ϊ1,��λ�ƹ���ֵΪ0')
                    break
                try:
                    OneNumNow = int(NumA[0])
                    TwoNumNow = int(NumA[1])
                    float(lineTex[1])
                    Trantransit = int(lineTex[2])
                except:
                    self._TranDict.clear()
                    mc.confirmDialog(title=u"��ʾ", message=u'��%s�д��ڷǷ�����!\n���ڷ������ַ�����\nҪ���1��2��4λ��������2�ɴ�С��' % i)
                    break
                #������Ϊ��ż��ʱ
                if Trantransit%2 != 0:
                    self._TranDict.clear()
                    mc.confirmDialog(title=u"��ʾ", message=u'���ڷǷ����ݣ�\n��%s�е�λ���ں�ֵҪΪż��' % i)
                    break
                if i == 1:
                    qFlag = TwoNumNow
                    OneNumBefore = OneNumNow
                    TwoNumBefore = TwoNumNow
                else:
                    #λ�ƹ���ֵȡֵ����
                    print Trantransit,TwoNumNow, TwoNumBefore, OneNumNow,OneNumBefore
                    if (Trantransit/2>(TwoNumNow-TwoNumBefore)/2) or (Trantransit/2>(OneNumNow-OneNumBefore)/2):
                        self._TranDict.clear()
                        mc.confirmDialog(title=u"��ʾ", message=u'���ڷǷ����ݣ�\n��%s�еĵ���λ��λ�ƹ���ֵ����'%i)
                        break
                    else:
                        OneNumBefore = OneNumNow
                        TwoNumBefore = TwoNumNow
                    #֡��ȡֵ����
                    if i == tranTexLen:
                        if TwoNumNow<=OneNumNow:
                            self._TranDict.clear()
                            mc.confirmDialog(title=u"��ʾ", message=u'���ڷǷ����ݣ�\n���һ�еĽ���֡����С�ڻ���ڿ�ʼ֡��')
                            break
                        if TwoNumNow!=self._endFrameV:
                            print TwoNumNow,self._endFrameV
                            self._TranDict.clear()
                            mc.confirmDialog(title=u"��ʾ", message=u'���ڷǷ����ݣ�\n���һ�еĽ���֡����������֡��һ�£�')
                            break
                    else:
                        ##�ж������Ƿ�����
                        # print OneNumNow,qFlag
                        if OneNumNow != (qFlag+1):
                            # print OneNumNow,qFlag
                            self._TranDict.clear()
                            mc.confirmDialog(title=u"��ʾ", message=u'���ڷǷ����ݣ�\n��%s�еĿ�ʼ֡����һ�еĽ���֡��������' % i)
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
        self._tranDVBG = []  #λ�ƹ���ֵ�������飬����Ҫ��
        tranDVB = 0
        changeFrameTemp = 0 #λ�ƹ�������¼ 
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
            #������ʼ�ͽ���֡
            numList = TranRangeV.split("-")
            OneNum = int(numList[0])   #��ʼ֡
            TwoNum = int(numList[1])   #����֡
            changeValueNow = self._TranDict[TranRangeV][1]  #��ǰ��λ���ں�ֵ����ֵ
            #����
            changeValueAfter = 0  #��һ֡�����ں�֡��ֵ
            changeFrameD = 0    #ĩ��֡������Χ
            if i==1:
                #��ȡ����
                tranDVBNow = float(self._TranDict[TranRangeV][0])
                tranDVBAfter = float(self._TranDict[groupFame[i]][0])
                #����֡�������
                changeValueAfter = int(self._TranDict[groupFame[i]][1])
                changeFrameD = int(changeValueAfter)/2
                #print changeFrameD,changeValueAfter,changeValueNow
                #��2�δ���
                FisrDoNum = OneNum
                SecondDoNum = TwoNum-changeFrameD
                ThirdDoNum = TwoNum
                for j in range(FisrDoNum, SecondDoNum+1):
                    self._tranDVBG.append(tranDVBNow)
                #ȡ����ֵ
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
                #��ȡ����
                tranDVBNow = float(self._TranDict[TranRangeV][0])
                #��2�δ���
                FisrDoNum = OneNum
                SecondDoNum = OneNum+changeFrameTemp
                ThirdDoNum = TwoNum
                #��һ��
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
                        #��ȡ����
                tranDVBNow = float(self._TranDict[TranRangeV][0])
                tranDVBAfter = float(self._TranDict[groupFame[i]][0])
                #����֡������ϡ�ĩ��
                changeValueAfter = int(self._TranDict[groupFame[i]][1])
                changeFrameD = int(changeValueAfter)/2
                #������,ǰ�滺����,���滷��
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
                #����ȥ����ֵ
                tranDVB = (tranDVBAfter-tranDVBNow)/changeValueAfter
                for vv in range(ThirdDoNum, fourDoNum):
                    tranTemp = tranDVB*tt
                    self._tranDVBG.append(tranDVBNow+tranTemp)
                    tt+=1
                # print self._tranDVBG
                # print len(self._tranDVBG)
                changeFrameTemp = changeFrameD
             
    def CreateAni(self, *args):
        #����cube
        if mc.objExists("myAniCube"):
            mc.delete("myAniCube")
        self._myCube = mc.polyCube(n="myAniCube")[0]
        f = open(self._dateFileName)             # ����һ���ļ�����  
        line = f.readline()             # �����ļ��� readline()���� 
        FrameValue = 0
        SecTime = 0 
        rotaFV = ""
        while line:  
            #print line                 # ����� ',' �����Ի��з�  
            # print(line, end = '')������# �� Python 3��ʹ��
            if line.find("Index")>=0:
                #��ȡ֡����������֡��
                FrameFL = re.findall(r"Index:(.+?),", line)
                if FrameFL:
                    FrameNum =  int(FrameFL[0])
                    if FrameNum%4==0:
                        FrameValue += 1
                        mc.currentTime(FrameValue, u=False)
                        #��ȡ��תֵ������ת
                        rotaFV = re.findall(r"\((.+?)\)", line)
                        if rotaFV:
                            rotaFL = rotaFV[0].split(",")
                            mc.rotate(rotaFL[0], -float(rotaFL[1]), rotaFL[2], self._myCube, a=True)
                            mc.setKeyframe("%s.rotate" % self._myCube)
                            #����λ��ֵ
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
            mc.textField('startFrame', edit=True, text = "1", alwaysInvokeEnterCommandOnReturn= True) #���ý�����ʼ֡        
            mc.textField('endFrame', edit=True, text = FrameValue, alwaysInvokeEnterCommandOnReturn= True) #���ý������֡  

    def Doit(self, *args):
        self._tranDVBG=[]
        mc.currentUnit(t="pal") #����֡��
        mc.playbackOptions(min=1, ast=1, max=25, aet=25)
        self._TranValue = float(mc.textFieldGrp(self._textFG, tx=True, q=True))
        if (self._TranValue>0.01) & (self._TranValue<=100.0):
            if self._dateFileName and self._dateFileName[-4::]==".txt":
                if self._tranFileName:
                    self.GetMoveList()
                    #print self._tranDVBG
                mu.executeInMainThreadWithResult(self.CreateAni)
            else:
                mc.confirmDialog(title=u"��ʾ",message=u'��ѡ��ɼ����ݵ�txt�ļ���')
        else:
            mc.confirmDialog(title=u"��ʾ",message=u'����ļ��ֵ��0��10֮ǰ!\n����������')
    
            

CreateAnimationForUnity().show()