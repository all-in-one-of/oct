# coding=utf-8

#---------------------------------------------
# 针对KLJZ项目制作的插件
# 随着离相机越近，物体越小
#---------------------------------------------

import maya.OpenMaya as om
import maya.OpenMayaMPx as mpx
import sys, math


kPluginNodeTypeName = 'KLJZ_dts'

dstNodeId = om.MTypeId(0x9233)

# node definition
class DisplacementToScale(mpx.MPxNode):
    obj1_input = om.MObject()
    obj2_input = om.MObject()
    coefficient_input = om.MObject()
    scaleRatio_input = om.MObject()
    scaleAdd_input = om.MObject()
    output = om.MObject()

    def __init__(self):
        mpx.MPxNode.__init__(self)
    
    def compute(slef, plug, dataBlock):
        if(plug == DisplacementToScale.output):
            try:
                obj1DataHandle = dataBlock.inputValue(DisplacementToScale.obj1_input)
                obj1_point = obj1DataHandle.asFloat3()

                obj2DataHandle = dataBlock.inputValue(DisplacementToScale.obj2_input)
                obj2_point = obj2DataHandle.asFloat3()

                coeDataHandle = dataBlock.inputValue(DisplacementToScale.coefficient_input)
                coefficient_point = coeDataHandle.asFloat3()

                scaleDataHandle = dataBlock.inputValue(DisplacementToScale.scaleRatio_input)
                scaleRatio_value = scaleDataHandle.asFloat()

                scaleAddDataHandle = dataBlock.inputValue(DisplacementToScale.scaleAdd_input)
                scaleAdd_value = scaleAddDataHandle.asFloat()

                distance_pow = math.pow((obj1_point[0] - obj2_point[0]),2) + math.pow((obj1_point[1] - obj2_point[1]),2) + math.pow((obj1_point[2] - obj2_point[2]),2)
                distance = math.sqrt(distance_pow)

                value = coefficient_point[0] * distance_pow + coefficient_point[1] * distance + coefficient_point[2] + scaleAdd_value
                if value>scaleAdd_value + 1:
                    value = scaleAdd_value + 1
                elif value < scaleAdd_value +0.25:
                    value = scaleAdd_value +0.25
                value = value * scaleRatio_value

                outputHandle = dataBlock.outputValue(DisplacementToScale.output)
                outputHandle.setFloat(value)
                dataBlock.setClean(plug)
            except:
                om.MGlobal.displayWarning('plugin error~!')
        else:
            om.MGlobal.displayWarning('plugin not run~!')


# node initialize
def nodeInitialize():
    # input
    nAttr_obj1_input = om.MFnNumericAttribute()
    DisplacementToScale.obj1_input = nAttr_obj1_input.create('obj1', 'o1', om.MFnNumericData.k3Float, 0.0)
    nAttr_obj1_input.setStorable(1)

    nAttr_obj2_input = om.MFnNumericAttribute()
    DisplacementToScale.obj2_input = nAttr_obj2_input.create('obj2', 'o2', om.MFnNumericData.k3Float, 0.0)
    nAttr_obj2_input.setStorable(1)

    nAttr_coefficient_input = om.MFnNumericAttribute()
    DisplacementToScale.coefficient_input = nAttr_coefficient_input.create('coefficient', 'c', om.MFnNumericData.k3Float, 0.0)
    nAttr_coefficient_input.setStorable(1)

    nAttr_scaleRatio_input = om.MFnNumericAttribute()
    DisplacementToScale.scaleRatio_input = nAttr_scaleRatio_input.create('scaleRatio', 'sr', om.MFnNumericData.kFloat, 1.0)
    nAttr_scaleRatio_input.setStorable(1)

    nAttr_scaleAdd_input = om.MFnNumericAttribute()
    DisplacementToScale.scaleAdd_input = nAttr_scaleAdd_input.create('scaleAdd', 'sa', om.MFnNumericData.kFloat, 0.0)
    nAttr_scaleAdd_input.setStorable(1)

    # output
    nAttr_output = om.MFnNumericAttribute()
    DisplacementToScale.output = nAttr_output.create('value', 'v', om.MFnNumericData.kFloat, 0.0)
    nAttr_output.setStorable(1)
    nAttr_output.setWritable(0)
    
    
    # add attributes
    DisplacementToScale.addAttribute(DisplacementToScale.obj1_input)
    DisplacementToScale.addAttribute(DisplacementToScale.obj2_input)
    DisplacementToScale.addAttribute(DisplacementToScale.coefficient_input)
    DisplacementToScale.addAttribute(DisplacementToScale.scaleRatio_input)
    DisplacementToScale.addAttribute(DisplacementToScale.scaleAdd_input)
    DisplacementToScale.addAttribute(DisplacementToScale.output)

    DisplacementToScale.attributeAffects(DisplacementToScale.obj1_input, DisplacementToScale.output)
    DisplacementToScale.attributeAffects(DisplacementToScale.obj2_input, DisplacementToScale.output)
    DisplacementToScale.attributeAffects(DisplacementToScale.coefficient_input, DisplacementToScale.output)
    DisplacementToScale.attributeAffects(DisplacementToScale.scaleRatio_input, DisplacementToScale.output)
    DisplacementToScale.attributeAffects(DisplacementToScale.scaleAdd_input, DisplacementToScale.output)

# creator
def nodeCreator():
    return mpx.asMPxPtr(DisplacementToScale())
