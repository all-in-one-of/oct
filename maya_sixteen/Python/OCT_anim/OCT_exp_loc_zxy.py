# -*- coding: UTF-8 -*-

import maya.cmds as mc
import maya.OpenMaya as om

first_full_name = None
last_full_name = None
final_loc = None


def exp_loc_ui():
    if mc.windowPref('OCT_exp_loc_ui', exists=True):
        mc.windowPref('OCT_exp_loc_ui', remove=True)
    if mc.window('OCT_exp_loc_ui', exists=True):
        mc.deleteUI('OCT_exp_loc_ui', window=True)
    mc.window("OCT_exp_loc_ui", title=u"相对路径动画导出工具", menuBar=True,
              widthHeight=(168, 120), resizeToFitChildren=False, sizeable=True)
    mc.columnLayout('formLyt', adjustableColumn=True)
    mc.button('create_point_btn', label=u'创建新原点Locator', w=200, aop=True,
              c='OCT_anim.OCT_exp_loc_zxy.create_new_zero_point()', backgroundColor=(0.3, 0.7, 0.3))
    mc.button('create_path_btn', label=u'创建相对运动Locator', w=200, aop=True,
              c='OCT_anim.OCT_exp_loc_zxy.make_path()', backgroundColor=(0.3, 0.7, 0.3))
    mc.button('exp_btn', label=u'导出Locator', w=200, h=35, aop=True,
              c='OCT_anim.OCT_exp_loc_zxy.export_loc()', backgroundColor=(0.9, 0.3, 0.3))
    mc.setParent('..')
    mc.showWindow('OCT_exp_loc_ui')


def check_selection_obj():
    global first_full_name
    global last_full_name
    if not len(mc.ls(sl=True)) == 2:
        om.MGlobal.displayError(u'请选择两个DAG物体')
        return

    first = mc.ls(sl=True, head=True)
    last = mc.ls(sl=True, tail=True)
    selectionList = om.MSelectionList()
    selectionList.add(first[0])
    selectionList.add(last[0])
    path = om.MDagPath()
    try:
        selectionList.getDagPath(0, path)
    except:
        om.MGlobal.displayError(u'请选择DAG物体')
        return
    first_full_name = path.fullPathName()

    path = om.MDagPath()
    try:
        selectionList.getDagPath(1, path)
    except:
        om.MGlobal.displayError(u'请选择DAG物体')
        return
    last_full_name = path.fullPathName()


def create_new_zero_point():
    check_selection_obj()
    new_zero_loc = mc.spaceLocator(n='new_zero_locator', p=[0.0, 0.0, 0.0])
    point_constraint = mc.pointConstraint(first_full_name, new_zero_loc[0])
    orient_constraint = mc.orientConstraint(first_full_name, new_zero_loc[0])
    mc.delete(point_constraint, orient_constraint)
    mc.parentConstraint(last_full_name, new_zero_loc[0], mo=True, w=True)
    return new_zero_loc[0]


def make_path():
    global final_loc

    # 首选原点物体, 后选运动物体
    check_selection_obj()
    # 按选择顺序创建LOCATOR, 并且约束到相同的位移
    zero_loc = mc.spaceLocator(n='loc_o', p=[0.0, 0.0, 0.0])
    new_loc = mc.spaceLocator(n='loc_move', p=[0.0, 0.0, 0.0])
    mc.pointConstraint(first_full_name, zero_loc[0])
    mc.orientConstraint(first_full_name, zero_loc[0])
    mc.pointConstraint(last_full_name, new_loc[0])
    mc.orientConstraint(last_full_name, new_loc[0])
    # 将运动物体的LOC父子关系到原点物体的LOC
    mc.parent(new_loc[0], zero_loc[0])
    # 创建一个新的LOC, 作为最终LOC
    loc = mc.spaceLocator(n='final_motion_loc', p=[0.0, 0.0, 0.0])
    # 连接属性
    mc.connectAttr('%s.translate' % new_loc[0], '%s.translate' % loc[0], f=True)
    mc.connectAttr('%s.rotate' % new_loc[0], '%s.rotate' % loc[0], f=True)
    st = mc.playbackOptions(q=True, min=True)
    et = mc.playbackOptions(q=True, max=True)
    # BAKE ATTRIBUTE
    mc.bakeResults(sm=True, sb=True, dic=True, pok=True, sac=False, ral=False,
                   bol=False, cp=False, s=False, t=(st, et))
    mc.disconnectAttr('%s.translate' % new_loc[0], '%s.translate' % loc[0])
    mc.disconnectAttr('%s.rotate' % new_loc[0], '%s.rotate' % loc[0])
    final_loc = loc[0]


def export_loc():
    mc.select(final_loc, r=True)
    mc.ExportSelection()
