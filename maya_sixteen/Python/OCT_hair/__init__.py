#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm

import re
import pymel.core as pm

def YetiToCurves():
    sacv=mc.ls(sl=1)
    shape=mc.listRelatives(sacv, shapes=True,f=1)
    new_curs=[]
    for i in shape:
        s=i.split('|')
        new_cur=s[-1].replace('Shape','')+'_f'
        mc.group(em=1,n=new_cur)
        mc.parent(i,new_cur,add=1,s=1)
        new_curs.append(new_cur)
    mc.delete(sacv)
    for i in new_curs:
        mc.rename(i,i.replace('_f',''))

def cut_curve():
    """
    先选所有曲线，最后选mesh
    :return:
    """
    sels = mc.ls(sl=True)
    mesh = sels[-1]
    for sel in sels[:-1]:
        try:
            cur = mc.polyProjectCurve(sel,mesh, ch=0,pointsOnEdges=1,curveSamples=50,automatic=1)[0]
            cur_chr = mc.listRelatives(cur,c=True)[0]
            mc.arclen(cur_chr,ch=True)
            mc.select([sel,cur])
            mm.eval('cutCurvePreset(1,1,0.01,6,0,1,0,2,2)')
            mc.delete(cur)
        except:
            pass



import re
import pymel.core as pm
def centerPivotPosition(poly_mes) :
    bbx = pm.xform(poly_mes, q=True, bb=True, ws=True)
    centerX = (bbx[0] + bbx[3]) / 2.0
    centerY = (bbx[1] + bbx[4]) / 2.0
    centerZ = (bbx[2] + bbx[5]) / 2.0
    return centerX, centerY, centerZ
def boundaryVertexs(all_vertexs) :
    return [each for each in all_vertexs if len(each) == 37]
def bNumNumInc(poly_mesh) :
    all_vertexs = pm.polyInfo(poly_mesh, ve=1)
    num = len(all_vertexs)
    b_num = len(boundaryVertexs(all_vertexs))/2
    inc = int(num)/int(b_num)
    return inc
def cj_cur(select_cur):
    objs = pm.ls(select_cur)
    dags = [k.split(".e")[0] for k in objs]
    duanshu=bNumNumInc(dags)
    cur_p=[]
    a = pm.ls(pm.polyListComponentConversion(objs, fe=True, fv=True, tv=True), fl=True)
    b_all=[]
    for i in range(duanshu):
        print i
        p=centerPivotPosition(a)
        if p not in cur_p:
            cur_p.append(p)
        for i2 in a:
            if i2 not in b_all:
                b_all.append(i2)
        a = pm.ls(pm.polyListComponentConversion(pm.polyListComponentConversion(b_all, fv=True, te=True), fe=True, tv=True), fl=True)
        cc = pm.ls(b_all, fl=True)
        for i3 in cc:
            if i3 in a:
                a.remove(i3)
    cur=pm.curve(p=cur_p)
    return cur
def nb_cur():
    sel = pm.ls(sl=1)
    cur_all=[]
    for i in sel:
        cur=cj_cur(i)
        cur_all.append(cur)
    pm.select(cur_all)
#nb_cur()#选择所以管子的根部的一圈曲线执行，在uv编辑器里面选择，方便选，前提uv一样，uv不一样的话，分批提取吧

def hairTool():
    import hairTools.hairTools as hairTools
    hairTools.hairballUI()
