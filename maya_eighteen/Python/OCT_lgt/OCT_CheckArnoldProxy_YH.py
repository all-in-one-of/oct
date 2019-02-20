#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mm
import os 
import shutil
import time
import subprocess

class checkArnoldProxy_YH():
    def __init__(self):
        self.myDictARs = {}
        self.myDictTex = {}

    def arnoldProxy(self):
        if mc.getAttr("defaultRenderGlobals.currentRenderer")=="arnold":
            aiNodes=mc.ls(type="aiStandIn")
            OCT_ArnoldPath="//octvision.com/CG/Resource/Material_Library/Proxy/Arnold/sourceimages"
            Path=mc.workspace(expandName="sourceimages")
            fileDso=[]
            flag=False
            aiNodesSet=[]
            allSets=list(set(mc.ls(sets=True))-set(['defaultLightSet', 'defaultObjectSet', 'initialParticleSE', 'initialShadingGroup']))
            if "OCT_AiNodesSet" in allSets:
                mc.delete("OCT_AiNodesSet")
            for aiNode in aiNodes:
                arnoldDso=mc.getAttr(aiNode+".dso")
                if arnoldDso=="":
                    mc.confirmDialog(message=(aiNode+"代理文件路径为空！"))
                    return
                allPath=""
                if arnoldDso in fileDso:
                    continue
                if "/" in arnoldDso:
                    allPath=arnoldDso.split("/")
                elif "\\" in arnoldDso:
                    allPath=arnoldDso.split("\\")
                    
                buf=""
                if allPath:
                    buf=os.path.splitext(allPath[-1])[0]
                else:
                    buf=os.path.splitext(arnoldDso)[0]
                    
                if not os.path.isfile(OCT_ArnoldPath+"/"+buf+".ass"):
                    flag=False
                    aiNodesSet.append(aiNode)
                    print (OCT_ArnoldPath+u'路径下没有:'+buf+".ass")
                    
                else:
                    try:
                        shutil.copy2((OCT_ArnoldPath+"/"+buf+".ass"),Path)
                        print(OCT_ArnoldPath+"/"+buf+".ass")
                        flag=True

                    except:
                        print(u'拷贝代理文件出错！\n')
                buf=""
                if allPath:
                    buf=os.path.splitext(allPath[-1])[0]
                else:
                    buf=os.path.splitext(arnoldDso)[0]
               
                #网路路径
                ArnoldPath=(OCT_ArnoldPath+"/arnoldTex/"+buf)
                #本机路径
                
                myPath=Path+"/arnoldTex/"+buf
                if os.path.isdir(ArnoldPath):
                    if not os.path.isdir(myPath):
                        os.makedirs(myPath)

                    myAllMaps=mc.getFileList(filespec=(ArnoldPath+"/*"))
                    for maps in myAllMaps:
                        sourcePath=ArnoldPath+"/"+maps
                        destPath=myPath
                        if os.path.isfile(sourcePath):
                            try:
                                shutil.copy2(sourcePath,myPath)
                            except:
                                print(u'拷贝代理文件出错！\n')
                    
                elif(os.path.isdir(ArnoldPath)) and (not os.path.isdir(myPath)):
                    mc.confirmDialog(message=(ArnoldPath+u'目录存在'+myPath+u'目录不存在'))
                    return
                if flag:    
                    fileDso.append(arnoldDso)
            mc.select(d=True)
            if aiNodesSet:
                for aiSet in aiNodesSet:
                    mc.select(aiSet,add=True)
                mc.sets(n='OCT_AiNodesSet')

    def arnoldProxyNew(self):
        if mc.getAttr("defaultRenderGlobals.currentRenderer")=="arnold":
            aiNodes=mc.ls(type="aiStandIn")
            OCT_ArnoldPaths= r"//octvision.com/CG/Resource/Material_Library/Proxy/ProxySeed"
            OCT_ArnoldList = os.listdir(OCT_ArnoldPaths)
            Path= mc.workspace(expandName="sourceimages")+"/arnoldtex"
            fileDso=[]
            flag=False
            aiNodesSet=[]
            allSets=list(set(mc.ls(sets=True))-set(['defaultLightSet', 'defaultObjectSet', 'initialParticleSE', 'initialShadingGroup']))
            if "OCT_AiNodesSet" in allSets:
                mc.delete("OCT_AiNodesSet")

            if not os.path.isdir(Path):
                os.makedirs(Path)
                time.sleep(0.1)

            for aiNode in aiNodes:
                arnoldDso = mc.getAttr("%s.dso"%aiNode)
                if arnoldDso == "":
                    mc.confirmDialog(message="%s代理文件路径为空！"%aiNode)
                    return

                arnoldPath = arnoldDso.replace("\\","/")
                
                allPath = arnoldPath.split("/")     
                
                buf = allPath[-1].split("_AR")[0]
               
                OCT_ArnoldPath = ""
                for p in OCT_ArnoldList:
                    pathFile = r"%s/%s/%s/sourceimages/arnoldtex/%s_AR.ass"%(OCT_ArnoldPaths,p,buf,buf)
                    if os.path.isfile(pathFile):
                        OCT_ArnoldPath = "%s/%s"%(OCT_ArnoldPaths,p)
                
                if OCT_ArnoldPath == "":
                    print(u'%s节点%s路径下没有对应的%s代理文件\n'%(aiNode,OCT_ArnoldPaths,allPath[-1]))

                if not os.path.isfile(OCT_ArnoldPath+"/"+buf+"/sourceimages/arnoldtex/"+buf+"_AR.ass"):
                    flag=False
                    aiNodesSet.append(aiNode)
                    print u"%s/%s/sourceimages/arnoldtex/路径下没有:%s.ass"%(OCT_ArnoldPath,buf,buf)
                    #print (OCT_ArnoldPath+"/"+buf+"/sourceimages/arnoldtex/"+u'路径下没有:'+buf+".ass")
                    
                else:
                    oldPath_AR = "%s/%s/sourceimages/arnoldtex/%s_AR.ass"%(OCT_ArnoldPath,buf,buf)
                    oldPath_tex = "%s/%s/sourceimages/arnoldtex/%s"%(OCT_ArnoldPath,buf,buf)

                    myPath = "%s/%s"%(Path, buf)
                    if not oldPath_AR in self.myDictARs.keys():
                        self.myDictARs.update({oldPath_AR:[aiNode]})
                        self.myDictTex.update({oldPath_tex:myPath})
                    else:
                        self.myDictARs[oldPath_AR].append(aiNode)


            for key in self.myDictARs.keys():
                temp = os.path.basename(key)
                arnoldAttr = '%s/%s'%(Path,temp)
                if os.path.isfile(arnoldAttr):
                    os.remove(arnoldAttr)
                    time.sleep(0.2)
                try:
                    sourcepath =  key.replace("/","\\")   
                    destPath = Path.replace("/","\\")  
                    cmd = 'COPY /Y "%s" "%s"' % (sourcepath, destPath)

                    cmd = str(cmd).encode("gb2312")
                    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                    while True:
                        if not p.poll() is None:
                            del p
                            break  

                    for i in self.myDictARs[key]:
                        mc.setAttr("%s.dso"%i, arnoldAttr, type='string')
                except:
                    print(u'拷贝代理文件出错！\n')
 
            for key in self.myDictTex.keys():
                if os.path.isdir(key):
                    if not os.path.isdir(self.myDictTex[key]):
                        os.makedirs(self.myDictTex[key])
                        time.sleep(0.01)

                    myAllMaps = os.listdir(key)
                    for maps in myAllMaps:
                        sourcePath = key+"/"+maps
                        destPath = self.myDictTex[key]
                        name = r"%s/%s"%(destPath,maps)
                        
                        if os.path.isfile(name):
                            os.remove(name)
                            time.sleep(0.1)
                        try:
                            sourcepaths =  sourcePath.replace("/","\\")   
                            destPaths = destPath.replace("/","\\")  
                            cmd = 'COPY /Y "%s" "%s"' % (sourcepaths, destPaths)

                            
                            cmd = str(cmd).encode("gb2312")
                            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                            while True:
                                if not p.poll() is None:
                                    del p
                                    break  
                            # shutil.copy2(sourcePath,destPath)
                            # time.sleep(0.2)
                        except:
                            print(u'拷贝贴图出错aaaaaa！%s\n'%sourcePath)
                
                
            if aiNodesSet:
                for aiSet in aiNodesSet:
                    mc.select(aiSet,add=True)
                mc.sets(n='OCT_AiNodesSet')
            mc.confirmDialog(message = u"拷贝完成!")
            return

#checkArnoldProxy_YH().arnoldProxyNew()