# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mm
import os
import string

def DY_New_PreRendersUI_YH():
    if mc.window('DY_RenderTools',exists=True):
        mc.deleteUI('DY_RenderTools')
    getCamWindow=mc.window('DY_RenderTools',wh=(360,200),resizeToFitChildren=1,sizeable=False)    
    mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center') 
    mc.radioButtonGrp('renderLayerOption',columnAlign3=('left','left','left'),columnWidth3=(110,100,100),numberOfRadioButtons=2,label='Render Options:',labelArray2=('Current Layer','All Renderable Layers'),sl=1,enable=True)
    mc.setParent('..')
    mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center')
    mc.radioButtonGrp('myPlayblastOptions',columnAlign3=('left','left','left'),columnWidth3=(110,100,100),numberOfRadioButtons=2,label='PlayblastOptions:',labelArray2=('Yes','No'),sl=1,enable=True)
    mc.intSliderGrp('myIntByFrame',label='By frame:',field=True,minValue=1,maxValue=500,value=0,cl3=('left','left','left'),cw3=(60,40,260)) 
    mc.textFieldGrp('myMissFrame',label='Miss frame:',text='',editable=True,ct2=('left','left'),cw2=(55,305))
    mc.frameLayout('camFrame', label="Cameras", borderStyle="etchedIn", w=360, enable=True)
    mc.columnLayout(rowSpacing=5)
    allCam=mc.listCameras(p=True)
    count=len(allCam)
    step=count/3
    mode=count%3
    if step>0:
        for i in range(step):
            mc.rowLayout(numberOfColumns=3,columnWidth3=(120,120,120))
            for j in range(3):
                mc.checkBox(allCam[3*i+j],l=allCam[3*i+j],v=0)
            mc.setParent('..')
    if mode>0:
        if mode==1:
            mc.rowLayout(numberOfColumns=1,columnWidth1=90)
        elif mode==2:
            mc.rowLayout(numberOfColumns=1,columnWidth2=(120,90))
        for i in range(mode):
            mc.checkBox(allCam[count-mode+i],l=allCam[count-mode+i],v=0)
            mc.setParent('..')
    mc.setParent('..')
    mc.setParent('..')
    mc.rowLayout(numberOfColumns=4,columnWidth4=(80,120,120,20),columnAlign4=('center','center','center','center'))
    mc.text(l='',vis=0)
    mc.button(l='OK',w=80,h=35,backgroundColor = (0.0,0.7,0),align='center',c=missFrameRender)
    mc.button(l='Close',width=80,h=35,backgroundColor = (0.7,0.0,0),c=('mc.deleteUI(\"'+getCamWindow+'\",window=True)'))
    mc.text(l='',vis=0)
    mc.setParent('..')
    mc.frameLayout('path',l=u'打开文件夹',borderStyle='etchedIn',w=360,enable=1)
    mc.button(l=u'工程素材文件夹',w=150,h=30,backgroundColor = (0.7,0.5,0),align='center', command=openfile_zwz)
    mc.showWindow(getCamWindow)

#打开工程素材文件夹    
def openfile_zwz(*args):
    imgDir=mm.eval('workspace -query -fileRuleEntry "images"')
    fullPath=mc.workspace(expandName=imgDir)
    os.startfile(fullPath)
    
#获取输入的值是否正确
def missFrameRender(*args):
    missList=[]
    start=[]
    missFrame=mc.textFieldGrp('myMissFrame',q=True,text=True)
    if missFrame=="":
        mm.eval('myCatchRender_zwz()')
    else:
        missList=missFrame.split(",")
        for i in range(len(missList)):
            if "-" in missList[0]:
                start=missList[0].split("-")
                for f in start[0]:
                    if f not in string.digits:
                        mc.confirmDialog(message=u"请重新输入Miss Frame!!!",button="OK")
                        return
                mc.currentTime(start[0])
            else:
                for f in missList[0]:
                    if f not in string.digits:
                        mc.confirmDialog(message=u"请重新输入Miss Frame!!!",button="OK")
                        return
                mc.currentTime(missList[0])
                    
            if "-" in missList[i]:
                start=missList[i].split("-")
                for f in start[0]:
                    if f not in string.digits:
                        mc.confirmDialog(message=u"请重新输入Miss Frame!!!",button="OK")
                        return
                for f in start[1]:
                    if f not in string.digits:
                        mc.confirmDialog(message=u"请重新输入Miss Frame!!!",button="OK")
                        return
            else:
                for f in missList[i]:
                    if f not in string.digits:
                        mc.confirmDialog(message=u"请重新输入Miss Frame!!!",button="OK")
                        return
        mm.eval('do_missFrameRender()')            
                
                
mm.eval(u'''global proc myCatchRender_zwz()
{
    int $the_start_frame = `getAttr defaultRenderGlobals.startFrame`;
    currentTime $the_start_frame;
    doRender_zwz();
}

//错帧渲染函数
global proc do_missFrameRender(){
    global string $myDir[];
    //控制摄像机的个数
   global int $c;
      //控制渲染层的个数
   global int $j;
   //控制跳帧
   global int $f;
   global int $miss;
   
   int $all = (`radioButtonGrp -q -sl "renderLayerOption"`)-1;
   int $myPlayblastOptions = (`radioButtonGrp -q -sl "myPlayblastOptions"`)-1;
   string $allCam[] = `listCameras -p`;
   //存放所有摄像机
   string $renderCam[];
   //存放所有层
   string $layers[];
   int $renderStatic =0;
   
   //获取images路径
   string $imgDir = `workspace -query -fileRuleEntry "images"`;
   string $fullPath = `workspace -expandName $imgDir`;
    
   global int $render;
   //第一次运行时的当前层
   global string $currentRenderlayer;
   int $the_start_frame = `getAttr defaultRenderGlobals.startFrame`;
   int $the_end_frame = `getAttr defaultRenderGlobals.endFrame`;
   //摄像机变量
    global string $cam;
    //获取当前层
    string $CRENDERLAYER=`editRenderLayerGlobals -q  -crl`;
    //获取当前帧
    int $cframe=`currentTime -q`;
       
       //保存素材的格式
       global string $the_images;
       //渲染的进度
       global int $amount;
       //当前层渲染了多少帧数
       global int $number;
       
       int $the_end;
    global string $show;
    //还有多少未渲染        
    global int $num_layer;
       global int $frames;
        
       //控制中断
    global int $if_interrupt;
    $if_interrupt=0;
    
       //获取素材路劲 
       string $buffer[];
    string $buffer1[];
    string $fn="";
    global string $path="";
    global string $old_path="";
    global string $fn2="";
    string $fn1="";
    
    //控制跳帧
    global int $jframe;
    
   
    //有多少个用，分割的数字
    int $m;
    int $b;
    //存放提取的帧数
    string $buffer2[];
    string $buffer3[];
    //开始帧
    global int $miss_s_f;
            
       //中断
        progressWindow
       -title "渲染中..."
        -isInterruptable true;
    
    if (`progressWindow -query -isCancelled`) {
       $myDir = {};
       $if_interrupt=1;
       myEndProgress();
       $render=0;
       $j=0;
       $c=0;
       $cam="";
       $jframe=0;
       return;
     }
    string $cmdString = ("activePlane = ''\\n"+
    "i = 1\\n"+
    "while(i):\\n"+
    "    try:\\n"+
    "        tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)\\n"+
    "    except:\\n"+
    "        pass\\n"+
    "    else:\\n"+
    "        if tmp:\\n"+
    "            activePlane = 'modelPanel%d' % i\\n"+
    "            break\\n"+
    "    i += 1\\n");
    python($cmdString);
    string $activePlane = python ("activePlane");

    if ($activePlane=="")
    {
           confirmDialog -message "请在点击主显示窗口" -button "重新选择";
        return;
    }

    //获取选择地摄像机
      for ($eachCam in $allCam) {
          $renderStatic = `checkBox -q -v $eachCam`;
          if ($renderStatic)
              $renderCam[size($renderCam)] = $eachCam;
          }
          
          
     //第一次运行时获取相机
       if($cam==""){
           //$cam=$renderCam[0];
           $number=0;
           $f=1;
           $miss=0;
           string $missFrame=`textFieldGrp -q -text "myMissFrame"`;
        $m=`tokenize $missFrame "," $buffer2`;
        for($i=0;$i<$m;$i++){
            if(`match "-" $buffer2[$i]`==""){
                if($m==1){
                    $miss=1;
                }
                if($i==0){
                    $miss_s_f=$buffer2[0];
                }else if($i==(size($buffer2)-1)){
                    $miss_e_f=$buffer2[$i];        
                }    
            }else{
                $b=`tokenize $buffer2[$i] "-" $buffer3`;
                if($i==0){
                    $miss_s_f=$buffer3[0];
                }else if($i==(size($buffer2)-1)){
                    $miss_e_f=$buffer3[1];        
                }
                $miss=int($buffer3[1])-int($buffer3[0])+$miss;    
            }
        }            
        $miss=$miss+$m-1;
       }

    if(size($renderCam)==0)
    {    
        progressWindow -endProgress;
           confirmDialog -message "请选择要渲染的摄像机..." -button "重新选择";
        return;
    }
    
    string $buf[] = `listConnections "renderLayerManager.renderLayerId"`;
    if ($all)
    {
        for ($layer in $buf)
        {
            if (`getAttr ($layer + ".renderable")`)
            {    //所有的Render Layer
                $layers[size($layers)] = $layer;
            }
        }
    }
    else
    {
        //获取当前的Render Layer（渲染层）
        $layers[size($layers)] = `editRenderLayerGlobals -query -currentRenderLayer`;
    }
    //第一次调用本函数获取的的当前渲染层
    if($render==0){
        $currentRenderlayer=`editRenderLayerGlobals -query -currentRenderLayer`;
        $render=1;   
    }
    
    //把第一次调用本函数的当前渲染层作为所有渲染层的一个
    for($i=0;$i<size($layers);$i++){
        if($currentRenderlayer==$layers[$i]){
            string $temp_render;
            $temp_render=$layers[$i];
            $layers[$i]=$layers[0];
            $layers[0]=$temp_render;
        }          
    }  


    //显示IPR渲染器
    RenderViewWindow;
    setTestResolutionVar(1);        
    $the_end=$miss*size($layers);
       $show="当前渲染层为"+$CRENDERLAYER;
             
        //判断第一层渲染器
       if($cframe==$miss_s_f && $c==0&& $layers[0]==$CRENDERLAYER && $number==0){
           $amount=0;
        progressWindow
         -title "特效渲染"
         -progress $amount
         -status "Frame: 0%"
           -min 0
         -max $the_end
         -isInterruptable true;
         
           $num_layer=size($layers)-1;

           $frames=floor($number*100/$miss);    
        print ("渲染进度："+$CRENDERLAYER+"层，第"+$cframe+"帧， 当前层的进度为："+$frames+"%, 还有："+$num_layer+"层未渲染\\n");
        
        //判断第一层渲染器
        $the_images=currentRenderer_zwz();
            progressWindow -edit
               -progress $amount
                 -status $show; 
                 
    }
    
    setAttr "defaultRenderGlobals.startFrame" $cframe;
    string $images[] = `renderSettings -firstImageName`;
    setAttr "defaultRenderGlobals.startFrame" $the_start_frame;
       
    int $n=`tokenize $images[0] "/" $buffer`;
    $n = `tokenize $images[0] "." $buffer1`; 
    $fn = $buffer[0]+"/"+$buffer[1]+"/";
    
    //渲染中断
    if (`progressWindow -query -isCancelled`) {
        $if_interrupt=1;
         myEndProgress();
         $render=0;
         $cam="";
        $j=0;
        $c=0;
        $jframe=0;
        return;
       
    }
    
    if($number<=$miss){ 
        //逐个摄像机渲染
        if((size($renderCam)-1)>=$c){
             $cam=$renderCam[$c];
            $fn1 =$fn + $cam +"/" +$cam+"."+$buffer1[1];
                 $path = $fullPath  +"/"+$fn1;
                 $old_path= $fullPath+"/tmp/"+$fn1;
                 $fn2=$fullPath+"/"+$fn + $cam;
               $fn3=$fullPath+"/"+$fn + $cam+"/"+$cam;   
            if ($myPlayblastOptions==0)
            {
                lookThru $cam $activePlane;
                currentTime $cframe;
                   updateModelPanelBar $activePlane;
             }       
            if(`getAttr "defaultRenderGlobals.currentRenderer"`=="arnold"){
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "renderSaveImage();do_missFrameRender()";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";              
            }else{
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "renderSaveImage();do_missFrameRender();";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";     
            }
            if((size($renderCam)-1)==$c){
                $jframe=1; 
                $c=0;        
            }else{
                $jframe=0;
                $c++;                 
            }        
      }
    }
    
    //跳层渲染
    if($number>$miss && $j<(size($layers)-1)){
            if(`getAttr "defaultRenderGlobals.currentRenderer"`=="arnold"){
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "do_missFrameRender()";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";              
            }else{
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "do_missFrameRender()";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";     
            }       
            ++$j;
            editRenderLayerGlobals -crl $layers[$j];
            $c=0;
            currentTime $miss_s_f;      
            $jframe=0;    
            $f=1;
            //从第二层开始判断渲染器
            $the_images=currentRenderer_zwz();
            
             setAttr "defaultRenderGlobals.startFrame" $the_start_frame;
             $cframe=`currentTime -q`;
             $num_layer=size($layers)-1-$j;
             $number=0;
             $frames=floor($number*100/$miss);    
             print ("渲染进度："+$layers[$j]+"层，第"+$cframe+"帧，当前层的进度为："+$frames+"%,还有："+$num_layer+"层未渲染\\n");
        
            
    }else if($number>$miss && $j>=(size($layers)-1)){
        $j=0;
        $c=0;
        $cam="";
        $render=0;
        $jframe=0;
        if(`getAttr "defaultRenderGlobals.currentRenderer"`=="vray"){
            setAttr -type "string" "vraySettings.fileNamePrefix" "<Scene>/<Layer>/<Camera>/<Camera>"; 
        }    
        setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "";
        //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
        setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
        setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
        setAttr  "defaultRenderGlobals.postMel" -type "string" "";
        setAttr  "defaultRenderGlobals.preMel" -type "string" "";     
              
        print ("渲染结束！\\n");
        setAttr "defaultRenderGlobals.startFrame" $the_start_frame;
        progressWindow -endProgress;
    }
    
    if (`progressWindow -query -isCancelled`) {
        $if_interrupt=1;
         myEndProgress();
         $render=0;
         $cam="";
        $j=0;
        $c=0; 
        $jframe=0;   
           return;
     }    
     renderWindowRenderCamera render renderView $cam;
}


//中断功能
global proc myEndProgress(){
    if(`getAttr "defaultRenderGlobals.currentRenderer"`=="vray"){
        setAttr -type "string" "vraySettings.fileNamePrefix" "<Scene>/<Layer>/<Camera>/<Camera>"; 
    }
      int $the_start_frame = `getAttr defaultRenderGlobals.startFrame`;
       setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "";
    //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
    setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
    setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
    setAttr  "defaultRenderGlobals.postMel" -type "string" "";
    setAttr  "defaultRenderGlobals.preMel" -type "string" "";
    setAttr "defaultRenderGlobals.startFrame" $the_start_frame;
    progressWindow -endProgress;
    print "渲染中断！\\n";
}

  
  //跳帧渲染函数
  global proc doRender_zwz()
  {
    global string $myDir[];
      //控制摄像机的个数
      global int $c;
      //控制渲染层的个数
   global int $j;
   int $all = (`radioButtonGrp -q -sl "renderLayerOption"`)-1;
   int $myPlayblastOptions = (`radioButtonGrp -q -sl "myPlayblastOptions"`)-1;
   string $allCam[] = `listCameras -p`;
   //存放所有摄像机
   string $renderCam[];
   //存放所有层
   string $layers[];
   int $renderStatic =0;
   
   //获取images路径
   string $imgDir = `workspace -query -fileRuleEntry "images"`;
   string $fullPath = `workspace -expandName $imgDir`;
    //获取文件名
    string $fileName = `file -q -shn -sn`;

   global int $render;
   //第一次运行时的当前层
   global string $currentRenderlayer;
   int $the_start_frame = `getAttr defaultRenderGlobals.startFrame`;
   int $the_end_frame = `getAttr defaultRenderGlobals.endFrame`;
   //摄像机变量
    global string $cam;
    //获取当前层
    string $CRENDERLAYER=`editRenderLayerGlobals -q  -crl`;
    //获取当前帧
    int $cframe=`currentTime -q`;
       
       //保存素材的格式
       global string $the_images;
       //渲染的进度
       global int $amount;
       
       int $the_end;
    global string $show;
    //还有多少未渲染        
    global int $num_layer;
        //当前层渲染的进度
       global int $the_s_f;
    global int $the_e_f;
       global int $frames;
        
       string $buffer[];
    string $buffer1[];
    string $fn="";
    //控制中断
    global int $if_interrupt;
    $if_interrupt=0;
    
    global string $path="";
    global string $old_path="";
    global string $SoftPath = "";
    global string $fn2="";
    string $fn1="";
    //控制跳帧
    global int $jframe;
       //中断
        progressWindow
       -title "渲染中..."
        -isInterruptable true;
    
    if (`progressWindow -query -isCancelled`) {
       $if_interrupt=1;
       myEndProgress();
       $render=0;
       $j=0;
       $c=0;
       $cam="";
       $jframe=0;
       return;
     }
    string $cmdString = ("activePlane = ''\\n"+
    "i = 1\\n"+
    "while(i):\\n"+
    "    try:\\n"+
    "        tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)\\n"+
    "    except:\\n"+
    "        pass\\n"+
    "    else:\\n"+
    "        if tmp:\\n"+
    "            activePlane = 'modelPanel%d' % i\\n"+
    "            break\\n"+
    "    i += 1\\n");
    python($cmdString);
    string $activePlane = python ("activePlane");


    if ($activePlane=="")
    {
           confirmDialog -message "请在点击主显示窗口" -button "重新选择";
        return;
    }


    //获取选择地摄像机
      for ($eachCam in $allCam) {
          $renderStatic = `checkBox -q -v $eachCam`;
          if ($renderStatic)
              $renderCam[size($renderCam)] = $eachCam;
          }
          
          
     //第一次运行时获取相机
       if($cam==""){
           $cam=$renderCam[0];
       }

    if(size($renderCam)==0)
    {
        progressWindow -endProgress;
           confirmDialog -message "请选择要渲染的摄像机..." -button "重新选择";
        return;
    }
    
    string $buf[] = `listConnections "renderLayerManager.renderLayerId"`;
    if ($all)
    {
        for ($layer in $buf)
        {
            if (`getAttr ($layer + ".renderable")`)
            {    //所有的Render Layer
                $layers[size($layers)] = $layer;
            }
        }
    }
    else
    {
        //获取当前的Render Layer（渲染层）
        $layers[size($layers)] = `editRenderLayerGlobals -query -currentRenderLayer`;
    }
    //第一次调用本函数获取的的当前渲染层
    if($render==0){
        $currentRenderlayer=`editRenderLayerGlobals -query -currentRenderLayer`;
        $render=1;   
    }
    
    //把第一次调用本函数的当前渲染层作为所有渲染层的一个
    for($i=0;$i<size($layers);$i++){
        if($currentRenderlayer==$layers[$i]){
            string $temp_render;
            $temp_render=$layers[$i];
            $layers[$i]=$layers[0];
            $layers[0]=$temp_render;
        }          
    }
    
   

    //显示IPR渲染器
    RenderViewWindow;
    setTestResolutionVar(1);
    
       
    $the_end=$the_end_frame*size($layers);
       $show="当前渲染层为"+$CRENDERLAYER;
       
       
        //判断第一层渲染器
       if($cframe==$the_start_frame && $c==0&& $layers[0]==$CRENDERLAYER){
            $amount=0;
        progressWindow
         -title "特效渲染"
         -progress $amount
         -status "Frame: 0%"
           -min $the_start_frame
         -max $the_end
         -isInterruptable true;
         
         //每一层渲染的进度
           $the_s_f=$cframe-$the_start_frame;
           $the_e_f=$the_end_frame-$the_start_frame;
           $frames=floor($the_s_f*100/$the_e_f);
           $num_layer=size($layers)-1;
           
        print ("渲染进度："+$CRENDERLAYER+"层，第"+$cframe+"帧， 当前层的进度为："+$frames+"%, 还有："+$num_layer+"层未渲染\\n");
        
        //判断第一层渲染器
        $the_images=currentRenderer_zwz();
     
            progressWindow -edit
               -progress $amount
                 -status $show; 
                 
    }
    
    setAttr "defaultRenderGlobals.startFrame" $cframe;
    string $images[] = `renderSettings -firstImageName`;
    setAttr "defaultRenderGlobals.startFrame" $the_start_frame;
 
    //int $n=`tokenize $images[0] "/" $buffer`;
    //$n = `tokenize $images[0] "." $buffer1`; 
    //$fn = $buffer[0]+"/"+$buffer[1]+"/";

    int $n=`tokenize $fileName "." $buffer`;

    //没一层名字的文件夹
    string $layersName = "";
    if($CRENDERLAYER == "defaultRenderLayer"){
        $layersName = "masterLayer";
    }else{
        $layersName = $CRENDERLAYER;
    }

    $fn = $buffer[0]+"/"+$layersName +"/";

    
    //渲染中断
    if (`progressWindow -query -isCancelled`) {
        $if_interrupt=1;
         myEndProgress();
         $render=0;
         $cam="";
        $j=0;
        $c=0;
        $jframe=0;
       return;
       
     }
     
    if($cframe<=$the_end_frame && $cframe>=$the_start_frame){ 
        //逐个摄像机渲染
        if((size($renderCam)-1)>=$c && $cframe<=$the_end_frame){
             $cam=$renderCam[$c];
            //$fn1 =$fn + $cam +"/" +$cam+"."+$buffer1[1];
                
                $fn1 =$fn + $cam;
                $SoftPath = $fullPath + "/" +$fn1+"/" +$cam+"."+$cframe;
                 $path = $fullPath  +"/"+$fn1;

                 $old_path= $fullPath+"/tmp/"+$fn1;
                 $fn2=$fullPath+"/"+$fn + $cam;
               $fn3=$fullPath+"/"+$fn + $cam+"/"+$cam;   

            if ($myPlayblastOptions==0)
            {
                lookThru $cam $activePlane;
                currentTime $cframe;
                   updateModelPanelBar $activePlane;
             }       
  
            if(`getAttr "defaultRenderGlobals.currentRenderer"`=="arnold"){
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "renderSaveImage();doRender_zwz()";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";              
            }else{
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "renderSaveImage();doRender_zwz();";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";     
            }
            if((size($renderCam)-1)==$c){
                $jframe=1; 
                $c=0;               
            }else{
                $jframe=0;
                $c++;                 
            }    
      }
    }
    
    //跳层渲染
    if( $cframe>$the_end_frame && $j<(size($layers)-1)){
            //$cam=$renderCam[$c];
            if(`getAttr "defaultRenderGlobals.currentRenderer"`=="arnold"){
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "doRender_zwz()";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";              
            }else{
                setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "";
                //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
                setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
                setAttr  "defaultRenderGlobals.postMel" -type "string" "doRender_zwz()";
                setAttr  "defaultRenderGlobals.preMel" -type "string" "";     
            }       
            ++$j;
            editRenderLayerGlobals -crl $layers[$j];
            $c=0;
            currentTime $the_start_frame;      
            $jframe=0;    
            //从第二层开始判断渲染器
            $the_images=currentRenderer_zwz();
            
             setAttr "defaultRenderGlobals.startFrame" $the_start_frame;
             $cframe=`currentTime -q`;
             $num_layer=size($layers)-1-$j;
             $the_s_f=$cframe-$the_start_frame;
                $the_e_f=$the_end_frame-$the_start_frame;
                $frames=floor($the_s_f*100/$the_e_f);    
             print ("渲染进度："+$layers[$j]+"层，第"+$cframe+"帧，当前层的进度为："+$frames+"%,还有："+$num_layer+"层未渲染\\n");
            
    }else if($cframe>$the_end_frame && $j>=(size($layers)-1)){
        $j=0;
        $c=0;
        $cam="";
        $render=0;
        $jframe=0;    
        if(`getAttr "defaultRenderGlobals.currentRenderer"`=="vray"){
            setAttr -type "string" "vraySettings.fileNamePrefix" "<Scene>/<Layer>/<Camera>/<Camera>"; 
        }
        setAttr  "defaultRenderGlobals.postRenderMel" -type "string" "";
        //setAttr  "defaultRenderGlobals.preRenderMel" -type "string" "";
        setAttr  "defaultRenderGlobals.preRenderLayerMel" -type "string" "";
        setAttr  "defaultRenderGlobals.postRenderLayerMel" -type "string" "";
        setAttr  "defaultRenderGlobals.postMel" -type "string" "";
        setAttr  "defaultRenderGlobals.preMel" -type "string" "";
        $myDir = {};
        print ("渲染结束！\\n");
        setAttr "defaultRenderGlobals.startFrame" $the_start_frame;
        progressWindow -endProgress;
    }
    
    if (`progressWindow -query -isCancelled`) {
        $if_interrupt=1;
         myEndProgress();
         $render=0;
         $cam="";
        $j=0;
        $c=0; 
        $jframe=0;   
           return;
       
     }
    renderWindowRenderCamera ("render","renderView",$cam);
     
 } 
 
 
 //保存函数
global proc renderSaveImage(){
    global string $path;
    global int  $if_interrupt;
    global string $the_images;
    global string $fn2;
    global string $old_path;
    global int $jframe;

    global string $SoftPath;
    global string $cam;

    //获取当前帧
    int $cframe=`currentTime -q`;
    global string $myDir[];
   
    if($if_interrupt==0 &&(!`progressWindow -query -isCancelled`)){
        if(`filetest -f ($SoftPath+"."+$the_images)`){
            sysFile -delete ($SoftPath+"."+$the_images);
        }
        if(`getAttr "defaultRenderGlobals.currentRenderer"`=="mentalRay" || `getAttr "defaultRenderGlobals.currentRenderer"`=="mayaSoftware"){
            renderWindowSaveImageCallback "renderView" $SoftPath "Maya IFF";
        }else if(`getAttr "defaultRenderGlobals.currentRenderer"`=="vray"){
            int $flag = 1;
            for($i = 0; $i<size($myDir); $i++){
                if(dirname($myDir[$i]) == $old_path){
                    $flag = 0;
                }
            }
            if(size($myDir) == 0 || $flag == 1){
                if(!(`filetest -d  $fn2`)){
                   sysFile -makeDir  $fn2;
                 }
                string $listDir[] = `getFileList -fld $old_path`;
                string $new_dir = "";
                int $k = 0;
                int $dir = 0;
                for($dir = 0; $dir<`size($listDir)`;$dir++){
                    $new_dir = $old_path+"/"+$listDir[$dir];
                    if(`filetest -d $new_dir`)
                    {   
                       $myDir[$k] = $new_dir;
                       $k = $k + 1;
                    }
                }
            }
            for($dir = 0;$dir<`size($myDir)`;$dir++){
                string $List[] = `getFileList -fld $myDir[$dir] -fs ($cam+".*"+$cframe+".*")`;
                int $f = 0;
                string $buf[];
                string $newName;
                for($f = 0;$f<size($List);$f++){
                    int $n=`tokenize $List[$f] "." $buf`;
                    if($n == 4 && `gmatch  $buf[1] ("*"+$cframe)`){
                        $newName = $myDir[$dir]+"/"+ $buf[0]+"."+$buf[2]+"."+$buf[1]+"."+$buf[3];
                        sysFile -rename $newName ($myDir[$dir]+"/"+$List[$f]);
                    } 
                }
                
            }
            
            /*if($the_images=="exr"){
               sysFile -cp ($path+"."+$the_images) ($old_path+"."+$the_images);
            }else{
                renderWindowSaveImageCallback "renderView" $path "PNG";
            }*/
        }
        if(`getAttr "defaultRenderGlobals.currentRenderer"`=="arnold"){    
            if(!(`filetest -d  $fn2`)){
                   sysFile -makeDir  $fn2;                          
                 }
                
            sysFile -cp ($path+"."+$the_images) ($old_path+"."+$the_images);
        }
            
     }
     if($jframe==1&&(!`progressWindow -query -isCancelled`)){
            jumpFrame();
    }    
            
}



//保存之后跳帧
global proc jumpFrame(){
    int $ByFrame;
    string $CRENDERLAYER=`editRenderLayerGlobals -q  -crl`;
    global int $num_layer;
    string $buffer2[];
    string $buffer3[];
    global int $miss;
    int $cframe=`currentTime -q`;
    global int $the_s_f;
    global int $the_e_f;
    global int $frames;
    global int $amount;
    global int $number;
    global string $show;
    global int $f;
    global string $the_images;
    string $missFrame=`textFieldGrp -q -text "myMissFrame"`;    
    int $the_start_frame = `getAttr defaultRenderGlobals.startFrame`;
    int $the_end_frame = `getAttr defaultRenderGlobals.endFrame`;
    //是否选择错帧渲染
    if($missFrame==""){
        if($cframe<=$the_end_frame && $cframe>=$the_start_frame){ 
             $ByFrame = `intSliderGrp -q -v "myIntByFrame"`;
                $amount+=$ByFrame;    
             progressWindow -edit
                  -progress $amount
                 -status $show;  
                 $cframe=`currentTime -q`;        
                 $cframe=$cframe+$ByFrame;    
                 currentTime $cframe;
                    if($cframe<=$the_end_frame){
                    $the_s_f=$cframe-$the_start_frame;
                          $the_e_f=$the_end_frame-$the_start_frame;
                          $frames=floor($the_s_f*100/$the_e_f);
                     print ("渲染进度："+$CRENDERLAYER+"层，第"+$cframe+"帧， 当前层的进度为："+$frames+"%, 还有："+$num_layer+"层未渲染\\n");
                }
            }            
    }else{
         $amount+=1;
          progressWindow -edit
              -progress $amount
             -status $show; 
          int $m=`tokenize $missFrame "," $buffer2`; 
          if($number<$miss){     
              if($m==1){
                  if(`match "-" $buffer2[0]`==""){
                      $number=1;
                  }else{
                      int $b=`tokenize $buffer2[0] "-" $buffer3`;
                      if($cframe>=int($buffer3[0])&& $cframe<int($buffer3[1])){
                          currentTime ($cframe+1);
                      }    
                  }
              }else{
                  if(`match "-" $buffer2[$f]`==""){ 
                    currentTime (int($buffer2[$f]));
                    $f++;
                }else{
                    int $b=`tokenize $buffer2[$f] "-" $buffer3`;
                    if($cframe>=int($buffer3[0]) && $cframe<(int($buffer3[1])-1)){
                        currentTime ($cframe+1);
                    }else if($cframe==(int($buffer3[1])-1)){
                        currentTime (int($buffer3[1]));
                        $f++;    
                    }else{
                        currentTime (int($buffer3[0]));
                    }
                }
                } 
          }
          if($number==$miss){
              currentTime ($cframe+1);
          }
          $number+=1;
          $cframe=`currentTime -q`;
          if($number<=$miss){
              $frames=floor($number*100/$miss);
              print ("渲染进度："+$CRENDERLAYER+"层，第"+$cframe+"帧， 当前层的进度为："+$frames+"%, 还有："+$num_layer+"层未渲染\\n");
          } 
      }
      if(`getAttr "defaultRenderGlobals.currentRenderer"`=="vray"&& ($number<=$miss ||$cframe<=$the_end_frame)){
          $the_images=currentRenderer_zwz();
      }            
}


 //判断渲染器
global proc string currentRenderer_zwz(){
    string $the_images;
    int $cframe=`currentTime -q`;
    //global int $traPadding;
    global string $num_2;
     if(`getAttr "defaultRenderGlobals.currentRenderer"`=="arnold"){
            setAttr -type "string" defaultArnoldDriver.aiTranslator "exr";
                setAttr "defaultArnoldDriver.exrCompression" 3; 
                setAttr "defaultArnoldDriver.autocrop" 1;
                $the_images="exr";
                setAttr "defaultRenderGlobals.imageFilePrefix" -type "string" "<Scene>/<RenderLayer>/<Camera>/<Camera>";            
        }else if(`getAttr "defaultRenderGlobals.currentRenderer"`=="mentalRay" || `getAttr "defaultRenderGlobals.currentRenderer"`=="mayaSoftware"){
            setAttr  defaultRenderGlobals.imageFormat 7;   
            $the_images="iff";     
            setAttr "defaultRenderGlobals.imageFilePrefix" -type "string" "<Scene>/<RenderLayer>/<Camera>/<Camera>";    
        }else if(`getAttr "defaultRenderGlobals.currentRenderer"`=="vray"){
            unifiedRenderGlobalsWindow;
            vrayChangeImageFormat;
            setAttr "defaultRenderGlobals.animation" 1;
            setAttr "vraySettings.animBatchOnly" 1;
            if(`getAttr "vraySettings.imageFormatStr"` =="exr (multichannel)"||`getAttr "vraySettings.imageFormatStr"` =="exr"){
                setAttr "vraySettings.imgOpt_exr_compression" 3;
                $the_images="exr";     
            }else{
                setAttr -type "string" "vraySettings.imageFormatStr" "png"; 
                $the_images="PNG";         
            }
            $num_2=$cframe;
            python ("import maya.cmds as cmds");
            python ("import maya.mel as mel");
               python ("Padding = mm.eval('$null_FY=4')");
                python ("num_1 = mm.eval('$null_FY2=$num_2')");
            python ("subNum = Padding - len(num_1)");
            string $fileNum = "";
            int $subNum = python ("Padding - len(num_1)");
            $fileNum = python ("'0'*subNum+num_1");    
            setAttr -type "string" "vraySettings.fileNamePrefix" ("<Scene>/<Layer>/<Camera>/<Camera>."+$fileNum); 
        }
    return $the_images;
} ''')


#DY_New_PreRendersUI_YH()