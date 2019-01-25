# -*- coding: utf-8 -*-
import maya.cmds as mc

def SetUnlockCameras_zwz(MyCamera,value):
	mc.setAttr('%s.tx'%MyCamera,lock = value)
	mc.setAttr('%s.ty'%MyCamera,lock = value)
	mc.setAttr('%s.tz'%MyCamera,lock = value)
	mc.setAttr('%s.rx'%MyCamera,lock = value)
	mc.setAttr('%s.ry'%MyCamera,lock = value)
	mc.setAttr('%s.rz'%MyCamera,lock = value)

def SetkCamerastoZero_zwz(MyCamera):
	mc.setAttr('%s.tx'%MyCamera,0)
	mc.setAttr('%s.ty'%MyCamera,0)
	mc.setAttr('%s.tz'%MyCamera,0)
	mc.setAttr('%s.rx'%MyCamera,0)
	mc.setAttr('%s.ry'%MyCamera,0)
	mc.setAttr('%s.rz'%MyCamera,0)

def ChangeXxbOldCameras_zwz():
    if mc.confirmDialog( title=u'温馨提示', message=u'是否需要更新摄像机！', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' ):
        FirstP = ''
        SecondP = ''
        MyLL = MyLM = MyLR = MyRL = MyRM = MyRR = ''
        AllFirstP = []
        allMyCameras= mc.listCameras(p= True)
        for MyCamera in allMyCameras:
            if not MyCamera.find('persp')>=0:
                if MyCamera.find('camL_L')>=0:
                    MyLL = MyCamera
                    firstP = mc.listRelatives(MyCamera,p=True)[0]
                    AllFirstP.append(firstP)
                    SecondP = mc.listRelatives(firstP,p=True)[0]
                    SetUnlockCameras_zwz(MyCamera,False)
                    mc.parent(MyCamera,w=True)
                    SetkCamerastoZero_zwz(MyCamera)
                    mc.setAttr('%s.ry'%MyCamera,240)
                if MyCamera.find('camL_M')>=0:
                    MyLM = MyCamera
                    firstP = mc.listRelatives(MyCamera,p=True)[0]
                    AllFirstP.append(firstP)
                    SetUnlockCameras_zwz(MyCamera,False)
                    mc.parent(MyCamera,w=True)
                    SetkCamerastoZero_zwz(MyCamera)
                    mc.setAttr('%s.ry'%MyCamera,180)
                if MyCamera.find('camL_R')>=0:
                    MyLR = MyCamera
                    firstP = mc.listRelatives(MyCamera,p=True)[0]
                    AllFirstP.append(firstP)
                    SetUnlockCameras_zwz(MyCamera,False)
                    mc.parent(MyCamera,w=True)
                    SetkCamerastoZero_zwz(MyCamera)
                    mc.setAttr('%s.ry'%MyCamera,120)
                if MyCamera.find('camR_L')>=0:
                    MyRL = MyCamera
                    firstP = mc.listRelatives(MyCamera,p=True)[0]
                    AllFirstP.append(firstP)
                    SetUnlockCameras_zwz(MyCamera,False)
                    mc.parent(MyCamera,w=True)
                    SetkCamerastoZero_zwz(MyCamera)
                    mc.setAttr('%s.ry'%MyCamera,240)
                if MyCamera.find('camR_M')>=0:
                    MyRM = MyCamera
                    firstP = mc.listRelatives(MyCamera,p=True)[0]
                    AllFirstP.append(firstP)
                    SetUnlockCameras_zwz(MyCamera,False)
                    mc.parent(MyCamera,w=True)
                    SetkCamerastoZero_zwz(MyCamera)
                    mc.setAttr('%s.ry'%MyCamera,180)
                if MyCamera.find('camR_R')>=0:
                    MyRR = MyCamera
                    firstP = mc.listRelatives(MyCamera,p=True)[0]
                    AllFirstP.append(firstP)
                    SetUnlockCameras_zwz(MyCamera,False)
                    mc.parent(MyCamera,w=True)
                    SetkCamerastoZero_zwz(MyCamera)
                    mc.setAttr('%s.ry'%MyCamera,120)
        for each in AllFirstP:
            try:
                mc.delete(each)
            except:
                pass
        if (MyLL and MyLM and MyLR and MyRL and MyRM and MyRR):
            myCamLG = mc.group(MyLL,MyLM,MyLR,name = 'Cam_L')
            mc.setAttr('%s.tx'%myCamLG,0.034)
            myCamRG = mc.group(MyRL,MyRM,MyRR,name = 'Cam_R')
            mc.setAttr('%s.tx'%myCamRG,-0.034)
            mylocator = mc.spaceLocator(p=(0,0,0))[0]
            mc.pointConstraint(SecondP,mylocator,w=1)
            mc.orientConstraint(SecondP,mylocator,w=1)
            tmp = mc.getAttr('%s.tx'%mylocator)
            mc.setAttr('%s.tx'%myCamLG,tmp)
            mc.setAttr('%s.tx'%myCamRG,tmp)
            tmp = mc.getAttr('%s.ty'%mylocator)
            mc.setAttr('%s.ty'%myCamLG,tmp)
            mc.setAttr('%s.ty'%myCamRG,tmp)
            tmp = mc.getAttr('%s.tz'%mylocator)
            mc.setAttr('%s.tz'%myCamLG,tmp)
            mc.setAttr('%s.ty'%myCamRG,tmp)
            tmp = mc.getAttr('%s.rx'%mylocator)
            mc.setAttr('%s.rx'%myCamLG,tmp)
            mc.setAttr('%s.rx'%myCamRG,tmp)
            tmp = mc.getAttr('%s.ry'%mylocator)
            mc.setAttr('%s.ry'%myCamLG,tmp)
            mc.setAttr('%s.ry'%myCamRG,tmp)
            tmp = mc.getAttr('%s.rz'%mylocator)
            mc.setAttr('%s.rz'%myCamLG,tmp)
            mc.setAttr('%s.rz'%myCamRG,tmp)
            mc.parent(myCamLG ,SecondP)
            mc.parent(myCamRG ,SecondP)
            mc.xform(myCamLG ,os=True,t=[0.034,0,0])
            mc.xform(myCamRG ,os=True,t=[-0.034,0,0])
            SetUnlockCameras_zwz(MyLL,True)
            SetUnlockCameras_zwz(MyLM,True)
            SetUnlockCameras_zwz(MyLR,True)
            SetUnlockCameras_zwz(MyRL,True)
            SetUnlockCameras_zwz(MyRM,True)
            SetUnlockCameras_zwz(MyRR,True)
            mc.delete(mylocator)
            mc.confirmDialog( title=u'温馨提示', message=u'摄像机已更新！', button=['ok'], defaultButton='ok', dismissString='No' )
        else:
            mc.confirmDialog( title=u'警告', message=u'没有相应的摄像机或其命名不对', button=['ok'], defaultButton='ok', dismissString='No' )
