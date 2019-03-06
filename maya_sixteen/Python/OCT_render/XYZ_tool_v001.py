##################################################################################
# Hi,This is a script to Create XYZ Depth Aov in Arnold                          #
# Instructions,																	 #				
#     1.Load ARNOLD in render settings tab before Run the script                 #
#     2.Click on create Button(It will create XYZ Depth shader as well as AOV)   #                                      
#     3.Adjust Min and Max values According to your Scene                        # 
# NOTE:- Do not click multiple times on Create button                            #
# please report bug and comments to me via mail:- anshad.k2005@gmail.com         #
# Special Thanks to Aritra Sarkar                                                #
#                                                           Script by Anshad.K.A #                                                     
#                                                                                #
##################################################################################

import maya.cmds as pymel
import mtoa.aovs as aovs


class xyzDepthTool():
    def __init__(self):
        pass

    @staticmethod
    def createall():
        Mysshdr = pymel.shadingNode("surfaceShader", asShader=True)
        pymel.rename(Mysshdr, "An_XYZ")

        Mysampler = pymel.shadingNode("samplerInfo", asUtility=True)
        pymel.rename(Mysampler, "An_sampler")

        Myrange = pymel.shadingNode("setRange", asUtility=True)
        pymel.rename(Myrange, "An_range")

        Mymltipl = pymel.shadingNode("multiplyDivide", asUtility=True)
        pymel.rename(Mymltipl, "An_multy")

        pymel.connectAttr("An_sampler.pointCameraX", "An_multy.input1X", force=True)
        pymel.connectAttr("An_sampler.pointCameraY", "An_multy.input1Y", force=True)
        pymel.connectAttr("An_sampler.pointCameraZ", "An_multy.input1Z", force=True)
        pymel.setAttr("An_multy.input2X", 1)
        pymel.setAttr("An_multy.input2Y", 1)
        pymel.setAttr("An_multy.input2Z", 1)

        pymel.connectAttr(" An_multy.outputX", "An_range.valueX", force=True)
        pymel.connectAttr(" An_multy.outputY", "An_range.valueY", force=True)
        pymel.connectAttr(" An_multy.outputZ", "An_range.valueZ", force=True)
        pymel.setAttr("An_range.minX", 1)
        pymel.setAttr("An_range.minY", 1)
        pymel.setAttr("An_range.minZ", 1)

        pymel.connectAttr(" An_range.outValue.outValueX", "An_XYZ.outColorR", force=True)
        pymel.connectAttr(" An_range.outValue.outValueY", "An_XYZ.outColorG", force=True)
        pymel.connectAttr(" An_range.outValue.outValueZ", "An_XYZ.outColorB", force=True)

        aovs.AOVInterface().addAOV('XYZ')
        pymel.connectAttr("An_XYZ.outColor", "aiAOV_XYZ.defaultValue", force=True)

    @staticmethod
    def adjustall():
        Xyz = pymel.window(title="XYZ Adjust", s=True, wh=(100, 50))
        pymel.columnLayout(adj=True)
        pymel.text(l="Adjust the Min & Max values")
        pymel.attrControlGrp(l="X Min", attribute='An_range.oldMinX')
        pymel.attrControlGrp(l="X Max", attribute='An_range.oldMaxX')
        pymel.attrControlGrp(l="Y Min", attribute='An_range.oldMinY')
        pymel.attrControlGrp(l="Y Max", attribute='An_range.oldMaxY')
        pymel.attrControlGrp(l="Z Min", attribute='An_range.oldMinZ')
        pymel.attrControlGrp(l="Z Max", attribute='An_range.oldMaxZ')

        pymel.showWindow(Xyz)

    @staticmethod
    # inverts multiply value
    def InvertM():
        pymel.setAttr("An_multy.input2X", -1)
        pymel.setAttr("An_multy.input2Y", -1)
        pymel.setAttr("An_multy.input2Z", -1)
        print "Multiply Inverted"

    @staticmethod
    # delete shader and xyz custom aov
    def Removeit():
        pymel.delete("An_XYZ*", "An_range*", "An_multy*", "An_sampler*")
        # import mtoa.aovs as aovs
        aovs.AOVInterface().removeAOV('XYZ')

    #########################################################################################
    def main(self):
        print self.__class__.__name__
        if pymel.window('xyzToolWin', ex=True):
            pymel.deleteUI('xyzToolWin')
        XyzTool = pymel.window('xyzToolWin', title="XYZ Depth", s=True, wh=(100, 50))

        pymel.columnLayout(columnAttach=('both', 20), rowSpacing=10, adj=True)
        pymel.text(l="Click on Create then adjust the Min & Max values")
        # ins_xdpt = xyzDepthTool()
        # crtallCmd = 'ins_xdpt = xyzDepthTool()\nins_xdpt.createall()'

        # b1 = pymel.button(l="Create", w=10, h=40, c='{}.createall()'.format(self.__class__.__name__))
        b1 = pymel.button(l="Create", w=10, h=40, c='import OCT_render.XYZ_tool_v001 as xyzt\nins_xyzt=xyzt.xyzDepthTool()\nins_xyzt.createall()')
        # creates an Aov and a custom depth shader which calculates x,y and z
        pymel.text(l="Click to adjust the Min & Max values")
        pymel.button(l="Adjust", w=10, h=40, c="ins_xyzt.adjustall()")
        # to adjust the xyz depth values
        pymel.text(l="Click to Invert Multiply Value")
        pymel.button(l="Invert", w=10, h=40, c="ins_xyzt.InvertM()")
        pymel.text(l="To delete Aov and Shader")
        pymel.button(l="Delete", w=10, h=40, c="ins_xyzt.Removeit()")
        pymel.text(l="By Anshad")
        pymel.showWindow(XyzTool)


if __name__ == "__main__":
    ins_t = xyzDepthTool()
    ins_t.main()