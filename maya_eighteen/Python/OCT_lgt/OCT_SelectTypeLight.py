# coding=utf-8
import maya.cmds as mc


class SelectTypeLight(object):
    def __init__(self):
        self.lightTypeDict = {
            'Maya Ambient Light':'ambientLight',
            'Maya Directional Light':'directionalLight',
            'Maya Point Light':'pointLight',
            'Maya Spot Light':'spotLight',
            'Maya Area Light':'areaLight',
            'Maya Volume Ligth':'volumeLight',
            'V-Ray Sphere Light':'VRayLightSphereShape',
            'V-Ray Dome Light':'VRayLightDomeShape',
            'V-Ray Rect Light':'VRayLightRectShape',
            'V-Ray IES Light':'VRayLightIESShape',
            'Arnold Area Light':'aiAreaLight',
            'Arnold Skydome Light':'aiSkyDomeLight',
            'Arnold Photometric Light':'aiPhotometricLight'
            }

    def showWindow(self):
        if mc.window('lightTypeWindow', q=True, ex=True):
            mc.deleteUI('lightTypeWindow')
        lightTypeWindow = mc.window('lightTypeWindow', t=u'选择同类型灯光', sizeable=False, w=140, h=70)
        form = mc.formLayout(numberOfDivisions=100)

        self.optionMenu = mc.optionMenu(label=u'灯光类型', w=100, h=20)
        for lightName in self.lightTypeDict:
            mc.menuItem(label=lightName)
        
        rowL = mc.rowLayout(numberOfColumns=2, h=40)
        button_1 = mc.button(l=u'选择', w=80, c=self.selectLight)
        button_2 = mc.button(l=u'取消', w=80, c=self.closeWindow)

        mc.formLayout(form, e=True, 
                      attachForm=[(self.optionMenu, 'top', 5), (self.optionMenu, 'left', 5), (self.optionMenu, 'right', 5), (rowL, 'left', 5), (rowL, 'right', 5), (rowL, 'bottom', 5)], 
                      attachControl=(self.optionMenu, 'bottom', 5, rowL))

        mc.showWindow(lightTypeWindow)

    def closeWindow(self, *args):
        if mc.window('lightTypeWindow', q=True, ex=True):
            mc.deleteUI('lightTypeWindow')

    def selectLight(self, *args):
        lightName = mc.optionMenu(self.optionMenu, q=True, v=True)
        lightType = self.lightTypeDict[lightName]
        lightList = mc.ls(et=lightType)
        if lightList:
            mc.select(lightList)

def main():
    diglog = SelectTypeLight()
    diglog.showWindow()
