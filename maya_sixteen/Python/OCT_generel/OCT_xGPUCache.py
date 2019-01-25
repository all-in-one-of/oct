#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import maya.cmds as mc
import os
import maya.mel as mm


def window_xGPU():
            
    if mc.window("xGPU",ex=True):
        mc.deleteUI("xGPU")
    mc.window("xGPU",title="xGPUcache V1.2",sizeable=True)
    mc.rowColumnLayout(numberOfColumns=1)
    mc.frameLayout(label=u"步骤一：选择要导出的场景模型")
    mc.rowColumnLayout(numberOfColumns=2,cw=[(1,200),(2,185)])
    mc.textScrollList("the_cj_list",w=200,h=110,bgc=(0.3,0.3,0.3))

    mc.rowColumnLayout(numberOfColumns=2,cw=[(1,90),(2,90)])
    mc.text(label=u"           → 代理文件导出")
    mc.text(label=u"设置 ←                  ")
    
    mc.text(label="")     
    mc.text(label="")
    
    mc.text(label="")     
    mc.text(label="") 
         
    mc.text(label=u"输出代理")
    mc.optionMenu("the_dai",label="")
    mc.menuItem(l="Arnold")
    mc.menuItem(l="Vray")        

    mc.text(label="")     
    mc.text(label="") 
                   
    mc.text(label="")     
    mc.text(label="")         
    mc.button(label=u"载入所选",h=30,c="OCT_generel.OCT_xGPUCache.load_cj()")
    mc.button(label=u"清空列表",c="OCT_generel.OCT_xGPUCache.remove_cj()")

    mc.setParent( '..' )  
    mc.setParent( '..' )
                    
    mc.frameLayout(label=u"步骤二 : 选择所有需要转化缓存的组或者模型")
    mc.rowColumnLayout(numberOfColumns=2,cw=[(1,200),(2,185)])
    
    mc.textScrollList("the_mod_list",w=200,h=170,bgc=(0.3,0.3,0.3))
     
    mc.rowColumnLayout(numberOfColumns=1)
    mc.text(label=u"→ 缓存导出设置 ←")
    
    mc.rowColumnLayout(numberOfColumns=3,cw=[(1,80),(2,50),(3,50)])
    mc.text(label="")
    mc.text(label="")
    mc.text(label="")
    
    mc.text(label=u"缓存类型")
    mc.optionMenu("cacheData",label="",cc="OCT_generel.OCT_xGPUCache.getCacheName()")
    mc.menuItem(l="ABC")
    mc.menuItem(l="GPU")        
    mc.menuItem(l="GEO") 
    mc.menuItem(l="blend") 
    mc.text(label="")
    
    mc.text(label="")
    mc.text(label="")
    mc.text(label="")           

    mc.text(label="Start/End")
    get_start_frame = mc.playbackOptions(q=True,min=True)
    get_end_frame = mc.playbackOptions(q=True,max=True)
    mc.intField("the_ST_ABC",v=get_start_frame)
    mc.intField("the_ET_ABC",v=get_end_frame )
    
    mc.text(label="Evaluate every")
    mc.floatField("the_EVA_every",v=1.0000)
    mc.text(label="")
    
    mc.text(label="")
    mc.text(label="")
    mc.text(label="")
    
    mc.text(label=u"是否导出UV")
    mc.checkBox("if_write_UV",label="UV W",v=1)    
    mc.text(label="rite           ")    
   
    mc.text(label=u"是否合并模型")
    mc.checkBox("if_combine",label="Comb",v=0)
    mc.text(label="")
   
    mc.text(label="")   
    mc.text(label="")
    mc.text(label="")
    

        
    mc.setParent( '..' ) 

    
    mc.rowColumnLayout(numberOfColumns=2,cw=[(1,90),(2,90)])
    mc.button(label=u"载入所选",h=30,c="OCT_generel.OCT_xGPUCache.load_mesh()")
    mc.button(label=u"清空列表",c="OCT_generel.OCT_xGPUCache.remove_mesh()")
        
    mc.setParent( '..' ) 
    mc.setParent( '..' )                        
    mc.setParent( '..' )
    mc.setParent( '..' )            
    mc.frameLayout(label=u"步骤三 : 是否有其他物体需要一并导出（如摄像机、灯光等等）")
    mc.rowColumnLayout(numberOfColumns=2,cw=[(1,200),(2,185)])
    mc.textScrollList("the_others_list",w=200,h=80,bgc=(0.3,0.3,0.3))
    mc.rowColumnLayout(numberOfColumns=1)
    mc.text(label="")
    mc.text(label="")    
    mc.text(label=u"→ 如果没有，可清空 ←")
    mc.text(label="")
      
    mc.rowColumnLayout(numberOfColumns=2,cw=[(1,90),(2,90)])
    mc.button(label=u"载入所选",h=30,c="OCT_generel.OCT_xGPUCache.load_others()")
    mc.button(label=u"清空列表",c="OCT_generel.OCT_xGPUCache.remove_others()")
    mc.setParent( '..' ) 
    mc.setParent( '..' ) 
    mc.setParent( '..' ) 
    
    mc.setParent( '..' ) 
    mc.frameLayout(label=u"步骤四 : 最后的输出设置")
    mc.rowColumnLayout(numberOfColumns=3,cw=[(1,90),(2,230),(3,60)])
    get_defaut_path = mc.workspace(en="scenes")
    mc.text(fn="boldLabelFont",label=u"文件输出位置：")
    the_out_abc_path = mc.textField("thePath_to_out",ed=False,tx=get_defaut_path+"/")
    mc.button(label=u"浏览...",c="OCT_generel.OCT_xGPUCache.set_path_output()")
    mc.text(fn="boldLabelFont",label=u"文件名：")
    get_current_filename = mc.file(q=True,sn=True)
    get_basename=os.path.splitext(os.path.basename(get_current_filename))
    mc.textField("the_out_file_name",tx=get_basename[0]+"_for_ABC")
    mc.optionMenu("the_ma_mb",label="")
    mc.menuItem(l=".mb")
    mc.menuItem(l=".ma")
    mc.setParent( '..' ) 
    mc.rowColumnLayout(numberOfColumns=4,cw=[(1,60),(2,100),(3,60),(4,100)])
    mc.text(label="")
    mc.button(label=u"开始转换",c="OCT_generel.OCT_xGPUCache.if_start()")
    mc.text(label="")
    mc.button(label=u"打开目录",c="OCT_generel.OCT_xGPUCache.open_path_output()")
    mc.text(label="")
    
    mc.setParent( '..' ) 
    
                  
    mc.showWindow("xGPU")
    


def start_trans():

    get_frame_start = mc.intField("the_ST_ABC",q=True,v=True)
    get_frame_end = mc.intField("the_ET_ABC",q=True,v=True)
    write_UV = ["","-uvWrite"]
    # world_Space = ["","-worldSpace"]
    ifUV = int(mc.checkBox("if_write_UV",q=True,v=True))
    # ifWP = 1
    daili = mc.optionMenu("the_dai",q=True,sl=True)
    get_cj_list = mc.textScrollList("the_cj_list",q=True,ai=True)
    if_comb = int(mc.checkBox("if_combine",q=True,v=True))    
    get_final_out_path = mc.textField("thePath_to_out",q=True,tx=True)
    get_final_out_filename = mc.textField("the_out_file_name",q=True,tx=True)
    get_the_step = mc.floatField("the_EVA_every",q=True,v=True)
    dataType = int(mc.optionMenu("cacheData",q=True,sl=True))
    all_need_to_cache = mc.textScrollList("the_mod_list",q=True,ai=True)
    all_need_to_string = ""
    all_need_to_cache_string = ""
    all_need_to_cache_string_2 = ""
    #导出代理
  

    #输出缓存 
    if if_comb == 1 and str(all_need_to_cache)!="None":
        for oneGroup in all_need_to_cache:
            Groups = mc.listRelatives(oneGroup, allParents=True)
            group_M = mc.ls(oneGroup, dag = True, ni = True, shapes = True)
            if len(group_M) > 1:
                objComb = mc.polyUnite(oneGroup, ch=True, mergeUVSets=True, name = oneGroup +"_comb")
                if Groups:
                    mc.parent(objComb[0], Groups[0])

            if len(group_M) == 1: 
                oneObj = mc.listRelatives(group_M[0], allParents=True)
                mc.rename(oneObj,oneGroup + "_comb")    
            all_need_to_string += "\""+ oneGroup + "_comb" + "\","

        if str(all_need_to_string) != 0:
            mc.textScrollList("the_mod_list",e=True,ra=True)
            exec("mc.textScrollList(\"the_mod_list\",e=True,append=("+all_need_to_string[0:-1]+"))")
    all_need_to_cache = mc.textScrollList("the_mod_list",q=True,ai=True)        
    for one_cache in all_need_to_cache :
        all_need_to_cache_string += " -root "+one_cache
        all_need_to_cache_string_2 += one_cache+" "    
    #导出ABC缓存
    if dataType==1:       
        get_cache_path = mc.workspace(en="cache")  
        get_cache_paths = r'%s/alembic/' % get_cache_path
        if not os.path.isdir(get_cache_paths):
            os.makedirs(get_cache_paths)
        # mc.AbcExport(j="-frameRange "+str(get_frame_start)+" "+str(get_frame_end)+" "+"-step "+str(get_the_step)+" "+write_UV[ifUV]+" -worldSpace"+all_need_to_cache_string+" -file "+get_final_out_path+get_final_out_filename+".abc");
        mc.AbcExport(j="-frameRange "+str(get_frame_start)+" "+str(get_frame_end)+" "+"-step "+str(get_the_step)+" "+write_UV[ifUV]+" -worldSpace"+all_need_to_cache_string+" -file "+get_cache_paths+get_final_out_filename+".abc");
        mc.delete(all_need_to_cache,ch=True)
        #mm.eval("AbcImport -mode import -connect \""+all_need_to_cache_string_2[0:-1]+"\" \""+get_final_out_path+get_final_out_filename+".abc"+"\"")
        mm.eval("AbcImport -mode import -connect \""+all_need_to_cache_string_2[0:-1]+"\" \""+get_cache_paths+get_final_out_filename+".abc"+"\"")
    

    #导出GPU缓存
    if dataType==2:  
        get_cache_path = mc.workspace(en="cache")  
        get_cache_paths = r'%s/alembic/' % get_cache_path
        if not os.path.isdir(get_cache_paths):
            os.makedirs(get_cache_paths)
        mc.select(all_need_to_cache,r=True)
        # mc.gpuCache(all_need_to_cache, startTime  = get_frame_start, endTime  = get_frame_end, saveMultipleFiles = False, optimize = False, writeMaterials = False, dataFormat = "ogawa", wuv = ifUV, directory= get_final_out_path, fileName  = get_final_out_filename)
        mc.gpuCache(all_need_to_cache, startTime  = get_frame_start, endTime  = get_frame_end, saveMultipleFiles = False, optimize = False, writeMaterials = False, dataFormat = "ogawa", wuv = ifUV, directory= get_cache_paths, fileName  = get_final_out_filename)
        for one_gpu in all_need_to_cache :
            mc.polyTriangulate(one_gpu) 
        mc.delete(all_need_to_cache,ch=True) 
        # mm.eval("AbcImport -mode import -connect \"" +all_need_to_cache_string_2[0:-1] + "\" -createIfNotFound " + " \"" +get_final_out_path+get_final_out_filename+".abc"+"\"")
        mm.eval("AbcImport -mode import -connect \"" +all_need_to_cache_string_2[0:-1] + "\" -createIfNotFound " + " \"" +get_cache_paths+get_final_out_filename+".abc"+"\"")
    

    #导出几何体缓存
    if dataType==3:  
       all_need_to_cache_shape = mc.ls(all_need_to_cache, dagObjects=True, ni=True, shapes=True)
       cacheFiles = mc.cacheFile(r = True, sch = True, dtf = True, fm = 'OneFile', spm = 1, smr = 1, directory = get_final_out_path, fileName = get_final_out_filename, st = get_frame_start, et = get_frame_end, points = all_need_to_cache_shape)
       mc.delete(all_need_to_cache,ch=True)
       myswichList = []
       myswichNode = []
       myNewcacheObjects = []
       switchText = ''
       for each in all_need_to_cache_shape:
           switch = mm.eval('createHistorySwitch("%s",false)'% each)
           myNewcacheObjects.append(each)
           myswichNode.append(switch)
           switchText = '%s.inp[0]' % switch
           myswichList.append(switchText)
           mc.setAttr( '%s.playFromCache' % switch, 1 )
       mc.cacheFile(f=get_final_out_filename ,directory=get_final_out_path, cnm= myNewcacheObjects, ia=myswichList ,attachFile=True)
       
    #输出blend缓存
    if dataType==4: 
       mc.select(all_need_to_cache,r=True)             
       mm.eval('x_bakeShape(%s,%s,%s, "%s", 0, 0)' %(get_frame_start, get_frame_end, get_the_step, get_final_out_filename))
       mc.textScrollList("the_mod_list",e=True,ra=True)
       exec("mc.textScrollList(\"the_mod_list\",e=True,append=(get_final_out_filename+'_bakeshape_gp'))")
       mc.delete(all_need_to_cache,ch=True)
       mc.select(hi = True)
    #导出另存文件
    all_need_to_cache = mc.textScrollList("the_mod_list",q=True,ai=True)        
    all_need_others = mc.textScrollList("the_others_list",q=True,ai=True)
    if str(all_need_others)!="None":
        mc.select(all_need_others+all_need_to_cache,r=True)
    else:
        mc.select(all_need_to_cache,r=True)    
    maormb = mc.optionMenu("the_ma_mb",q=True,sl=True)
    MA_MB  = ["mayaBinary","mayaAscii"]
    ma_mb  = [".mb",".ma"] 
    mm.eval("file -force -options \"v=0;\" -typ \""+MA_MB[maormb-1]+"\" -pr -es \""+get_final_out_path+get_final_out_filename+ma_mb[maormb-1]+"\"")
  
       
#加载物体
def load_mesh():
    get_all_mesh = mc.ls(sl=True,dagObjects=False)
    if not get_all_mesh:
        mc.confirmDialog(title = u'提醒', message = u'请先选择要转换的物体或者组', button='Yes')
        return

    get_all_mesh_string = ""
    get_all_nurbs_string = ""  
    get_all_string = ""
          
    if int(mc.checkBox("if_combine",q=True,v=True)) == 1:
        for one_check in get_all_mesh:
            get_all_mesh_string +=  "\""+ one_check + "\","
        if len(get_all_mesh_string) != 0:
            mc.textScrollList("the_mod_list",e=True,ra=True)
            exec("mc.textScrollList(\"the_mod_list\",e=True,append=("+get_all_mesh_string[0:-1]+"))") 
           
    if int(mc.checkBox("if_combine",q=True,v=True)) == 0: 
       mc.select(hi = True)
       get_all_mesh = mc.ls(selection=True, dagObjects=True, ni=True, shapes=True)
       for one_check_mesh in get_all_mesh:
           if mc.nodeType(one_check_mesh) == "nurbsSurface":
               temp_name = mc.listRelatives(one_check_mesh,p=True)
               group_name = mc.listRelatives(temp_name,f=True,p=True)
               for one_name in temp_name:
                   get_all_nurbs_string +=  "\""+ one_name +"_nurbs"  + "\","
                   mc.nurbsToPoly(one_name, polygonType=1, ch=True, name = one_name+"_nurbs")
                   mc.parent(one_name+"_nurbs", group_name)
            
           if mc.nodeType(one_check_mesh) == "mesh":
               temp_trans = mc.listRelatives(one_check_mesh,f=True,p=True)
               get_all_mesh_string +=  "\""+ temp_trans[0]  + "\","
           get_all_string = get_all_nurbs_string + get_all_mesh_string
       if len(get_all_mesh_string) != 0:
           mc.textScrollList("the_mod_list",e=True,ra=True)
           exec("mc.textScrollList(\"the_mod_list\",e=True,append=("+get_all_string[0:-1]+"))")
       mc.select(cl=True,r=True)    
def remove_mesh():
    mc.textScrollList("the_mod_list",e=True,ra=True)    
                  
def getCacheName():
    cacheName = mc.optionMenu("cacheData",q=True,sl=True)
    current_filename = mc.file(q=True,sn=True)
    basename = os.path.splitext(os.path.basename(current_filename)) 
    if cacheName ==1:
       mc.textField("the_out_file_name",e=True,tx=basename[0]+"_for_ABC")   
    if cacheName ==2:
       mc.textField("the_out_file_name",e=True,tx=basename[0]+"_for_GPU")
    if cacheName ==3:
       mc.textField("the_out_file_name",e=True,tx=basename[0]+"_for_GEO")
    if cacheName ==4:
       mc.textField("the_out_file_name",e=True,tx=basename[0]+"_for_Blend")          
#加载其他的物体  
def load_others():
    get_all_others = mc.ls(sl=True)
    get_all_others_string = ""
    for one_check in get_all_others:
        get_all_others_string +=  "\""+one_check  + "\","
    if len(get_all_others_string) != 0:
        mc.textScrollList("the_others_list",e=True,ra=True)
        exec("mc.textScrollList(\"the_others_list\",e=True,append=("+get_all_others_string[0:-1]+"))")    
        
def remove_others():
    mc.textScrollList("the_others_list",e=True,ra=True)

def load_cj():
    get_all_cj = mc.ls(sl=True)
    get_all_cj_string = ""
    for one_check in get_all_cj:
        get_all_cj_string +=  "\""+one_check  + "\","
    if len(get_all_cj_string) != 0:
        mc.textScrollList("the_cj_list",e=True,ra=True)
        exec("mc.textScrollList(\"the_cj_list\",e=True,append=("+get_all_cj_string[0:-1]+"))")    
        
def remove_cj():
    mc.textScrollList("the_cj_list",e=True,ra=True)    
    
def set_path_output():
    get_path=mc.fileDialog2(fileMode=3,caption="设置输出位置")
    if(str(get_path)!="None"):
        get_path_arr=str(get_path).split("'")
        mc.textField("thePath_to_out",e=True,tx=get_path_arr[1]+"/")       
        
def open_path_output(): 
    get_tx_path=mc.textField("thePath_to_out",q=True,tx=True)
    get_tx_path.replace("\\","/")
    if get_tx_path[-1]!="/":
        get_tx_path=get_tx_path+"/"
    os.startfile(get_tx_path)        


def if_start():
    if not mc.pluginInfo('gpuCache.mll', query=True, loaded=True):
        mc.loadPlugin('gpuCache.mll')
    if_action = mc.confirmDialog( title=u'确认信息', message=u'检查是否有重复名字', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    if if_action == "Yes":
        exec("start_trans()")
    
    # if mc.pluginInfo( 'gpuCache.mll', query=True, loaded=True):
    #    if_action = mc.confirmDialog( title='确认信息', message='检查是否有重复名字', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    #    if if_action == "Yes":
    #       exec("start_trans()")
    # else:
    #     mc.confirmDialog( title='错误', message='请在插件栏里把\n gpucache打开' , dismissString='No' )
    #     return
# window_xGPU()