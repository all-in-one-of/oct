# -*- coding: utf-8 -*-
import maya.cmds as mc


def OCT_XXBDeleteUnUseCameras_zwz():
    AllCameras = mc.listCameras(p=True)
    mydeCameras = []
    if AllCameras:
        for Camera in AllCameras:
            try:
                unusecamera = mc.listRelatives(Camera, p=True, f=True)[0].split('|')[1].find('CAM')
            except:
                if not (Camera.find('Test_') >= 0 or Camera.find('camL') >= 0 or Camera.find('camR') >= 0 or Camera.find('camL') >= 0 or Camera.find('persp') >= 0 or Camera.find('MasterCam') >= 0 or Camera.find('dl') >= 0 or Camera.find('ml') >= 0 or Camera.find('ul') >= 0):
                    mydeCameras.append(Camera)
            else:
                if unusecamera < 0:
                    if not (Camera.find('Test_') >= 0 or Camera.find('camL') >= 0 or Camera.find('camR') >= 0 or Camera.find('camL') >= 0 or Camera.find('persp') >= 0 or Camera.find('MasterCam') >= 0 or Camera.find('dl') >= 0 or Camera.find('ml') >= 0 or Camera.find('ul') >= 0):
                        mydeCameras.append(Camera)
    if mydeCameras:
        mc.delete(mydeCameras)
