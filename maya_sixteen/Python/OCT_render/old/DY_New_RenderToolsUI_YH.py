#!/usr/bin/env python
# coding=utf-8

import maya.cmds as mc
import maya.mel as mm
import os


def DY_New_PreRendersUI_YH():
	if mm.eval('window -exists DY_RenderTools'):
		mm.eval('deleteUI DY_RenderTools')
	getCamWindow=mm.eval('window -wh 240 200 -resizeToFitChildren 1 -sizeable 1 DY_RenderTools')
	mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center') 
	mc.radioButtonGrp('renderLayerOption',columnAlign2=('left','left'),columnWidth2=(100,150),numberOfRadioButtons=2,label='Render Options:',labelArray2=('Current Layer','All Renderable Layers'),sl=1,vertical=True,enable=True)
	mc.setParent('..')
	mc.columnLayout(rowSpacing=2,columnWidth=50,columnAlign='center')
	mc.radioButtonGrp('myPlayblastOptions',columnAlign3=('left','left','left'),columnWidth3=(95,60,40),numberOfRadioButtons=2,label='PlayblastOptions:',labelArray2=('Yes','No'),sl=1,enable=True)
	mc.intSliderGrp('myIntByFrame',label='By frame:',field=True,minValue=1,maxValue=500,value=0,cl3=('left','left','left'),cw3=(60,40,160))     
    	mm.eval('frameLayout -label Cameras -borderStyle etchedIn -w 270 -enable 1 camFrame')
	mc.columnLayout(rowSpacing=5)
	allCam=mc.listCameras(p=True)
	count=len(allCam)
	step=count/3
	mode=count%3
	if step>0:
		for i in range(step):
			mc.rowLayout(numberOfColumns=3,columnWidth3=(90,90,90))
			for j in range(3):
				mc.checkBox(allCam[3*i+j],l=allCam[3*i+j],v=0)
			mc.setParent('..')
	if mode>0:
		if mode==1:
			mc.rowLayout(numberOfColumns=1, columnWidth1=90)
		elif mode==2:
			mc.rowLayout(numberOfColumns=1, columnWidth2=(90, 90))
		for i in range(mode):
			mc.checkBox(allCam[count-mode+i],l=allCam[count-mode+i], v=0)
		mc.setParent('..')
	mc.setParent('..')
	mc.setParent('..')
    	mc.rowLayout(numberOfColumns=4, columnWidth4=(50, 80, 80, 20), columnAlign4=('center','center','center','center'))
    	mc.text(l='', vis=0)
    	mm.eval('button -l OK -width 50 -align center -c myCatchRender_zwz')
    	mc.button(l='Close', width=50, c=('mc.deleteUI(\"'+getCamWindow+'\",window=True)'))
   	mc.text(l='',vis=0)
   	mc.setParent('..')
   	mm.eval(u'frameLayout -label "打开文件夹" -borderStyle etchedIn -w 270 -enable 1 path')
   	mc.button(l=u'工程素材文件夹',w=150,h=30,align='center',command=openfile_zwz)
	mc.showWindow(getCamWindow)
	
def openfile_zwz(*args):
	imgDir=mm.eval('workspace -query -fileRuleEntry "images"')
	fullPath=mc.workspace(expandName=imgDir)
	print fullPath
	os.startfile(fullPath)
	
mm.eval(u'''global proc myCatchRender_zwz()
{
    int $the_start_frame = `getAttr defaultRenderGlobals.startFrame`;
    currentTime $the_start_frame;
    doRender_zwz();
}


//中断功能
global proc myEndProgress(){
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
  
  
  global proc doRender_zwz()
  {
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
    
   global int $render;
   //第一次运行时的当前层
   global string $currentRenderlayer;
   //print $currentRenderlayer; 
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
       	confirmDialog -message "请选择要渲染的摄像机..." -button "重新选择";
    	return;
    }
    
    string $buf[] = `listConnections "renderLayerManager.renderLayerId"`;
    if ($all)
    {
        for ($layer in $buf)
        {
            if (`getAttr ($layer + ".renderable")`)
            {	//所有的Render Layer
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
   		 $amount = 0;
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
    if($cframe<=$the_end_frame && $cframe>=$the_start_frame){ 
    	//逐个摄像机渲染
    	if((size($renderCam)-1)>=$c && $cframe<=$the_end_frame){
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
	if($if_interrupt==0){
			  if(`filetest -f ($path+"."+$the_images)`){
					sysFile -delete ($path+"."+$the_images);
				}
   				 if(`getAttr "defaultRenderGlobals.currentRenderer"`=="mentalRay" || `getAttr "defaultRenderGlobals.currentRenderer"`=="mayaSoftware"){
    				renderWindowSaveImageCallback "renderView" $path "Maya IFF";
    			}else if(`getAttr "defaultRenderGlobals.currentRenderer"`=="vray"){
    				if(!(`filetest -d  $fn2`)){
           				sysFile -makeDir  $fn2;
       	 		 }
    			renderWindowSaveImageCallback "renderView" $path "PNG";
   			 	}
			}
			if(`getAttr "defaultRenderGlobals.currentRenderer"`=="arnold"){	
			if(!(`filetest -d  $fn2`)){
           		sysFile -makeDir  $fn2;         		 		
       	 	 }
       	 	 if((`progressWindow -query -isCancelled`)){
       	 	 	sysFile -delete ($path+"."+$the_images);
       	 	 }
        	 sysFile -cp ($path+"."+$the_images) ($old_path+"."+$the_images);
	}
	if($jframe==1){
		jumpFrame();
	}			
}


//保存之后跳帧
global proc jumpFrame(){
    int $ByFrame;
	string $CRENDERLAYER=`editRenderLayerGlobals -q  -crl`;
	global int $num_layer;
	int $cframe=`currentTime -q`;
	global int $the_s_f;
	global int $the_e_f;
	global int $frames;
	global int $amount;
	global string $show;
	int $the_start_frame = `getAttr defaultRenderGlobals.startFrame`;
    int $the_end_frame = `getAttr defaultRenderGlobals.endFrame`;
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
}

 //判断渲染器
global proc string currentRenderer_zwz(){
	string $the_images;
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
    		setAttr -type "string" "vraySettings.imageFormatStr" "png"; 
    		$the_images="png"; 		
    		setAttr -type "string" "vraySettings.fileNamePrefix" "<Scene>/<Layer>/<Camera>/<Camera>"; 
    	}
    return $the_images;
} ''')
