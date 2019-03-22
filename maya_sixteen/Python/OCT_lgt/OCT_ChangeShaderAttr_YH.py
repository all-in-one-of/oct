# -*- coding: utf-8 -*-

import maya.mel as mm


def ChangeMayaShderAttr_YH():
	mm.eval(u'''//Update
	global proc updateShaderAttr (int $isColor, string $updateAttr,string $updateColor)
	{	
	int $selectedOrAll = `radioButtonGrp -q -sl selectedOrAll`;
	
	string $targetShader[] = {};
	//$isColor为0,1,2是lambert，blinn，phongE，phong，anisotropic材质，为3,4,5是VRayMtl材质
	if ($selectedOrAll == 1) {
		if ($isColor==3 || $isColor==4 || $isColor==5){
			$targetShader=`ls -typ VRayMtl -typ file -sl`;
		}else if($isColor==6 || $isColor==7 || $isColor==8){
			$targetShader = `ls -typ aiStandard -typ file -sl`;
		}else{
			$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file -sl`;
		}	
	}
	else {
		if($isColor==3 || $isColor==4 || $isColor==5){
			$targetShader=`ls -typ VRayMtl -typ file`;
		}else if($isColor==6 || $isColor==7 || $isColor==8){
			$targetShader=`ls -typ aiStandard -typ file`;
		}else{
			$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file`;
		}	
	}

	if ( size($targetShader) == 0 ) {
		print ("No shader selected.\\n");
		return;
	}
	
	float $updateAttrValue = 0;
	float $updateAttrColor[3] = {};
	
	if ($isColor == 1) {
		$updateAttrColor = `colorSliderButtonGrp -q -rgb $updateColor`;
	}
	else if ($isColor == 0 || $isColor==4 || $isColor==7) {
		$updateAttrValue = `floatSliderButtonGrp -pre 3 -q -v $updateColor`;
	}
	else if ($isColor == 2 || $isColor==5 || $isColor==8) {
		$updateAttrValue = `checkBox -q -v $updateColor`;
	}else if($isColor==3 || $isColor==6){
		$updateAttrColor = `colorSliderButtonGrp -q -rgb $updateColor`;
	}
	float $value = 0;
	int $i = 0;
	string $connected[];
		
	for ($i=0; $i<size($targetShader); $i++) {
		if (`attributeExists $updateAttr $targetShader[$i]`) {
			
			$connected = `listConnections -p 1 -c 1 ($targetShader[$i] + "." + $updateAttr)`;
			print ($targetShader[$i] + "." + $updateAttr);
			if (size($connected)) {
				if (catch(`disconnectAttr $connected[1] $connected[0]`))
				{
					print ("Cannot disconnect " + $connected[1] + " and " + $connected[0] + "\\n");
				}
			}
			
			if ( $isColor == 1 || $isColor==3 || $isColor==6) {			
				setAttr ($targetShader[$i] + "." + $updateAttr) $updateAttrColor[0] $updateAttrColor[1] $updateAttrColor[2];
				print ($targetShader[$i] + "." + $updateAttr + " => " + $updateAttrColor[0] + " " + $updateAttrColor[1] + " " + $updateAttrColor[2]);
			}
			else {

				if($updateColor=="hilightGlossiness" && $updateAttrValue==false){
					floatSliderButtonGrp -e -en 1 -pre 3 -label "HightGlossiness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"hilightGlossiness\\",\\"hilightGlossiness\\")" -sbc "CreateRenderNode(3, \\"hilightGlossiness\\")" hilightGlossiness;	
				}else{
					floatSliderButtonGrp -e -en 0 -pre 3 -label "HightGlossiness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"hilightGlossiness\\",\\"hilightGlossiness\\")" -sbc "CreateRenderNode(3, \\"hilightGlossiness\\")" hilightGlossiness;	
				}
				if($updateColor=="fresnelIOR" && $updateAttrValue==false){
					floatSliderButtonGrp -e -en 1 -pre 3 -label "Fresnel IOR " -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"fresnelIOR\\",\\"fresnelIOR\\")" -sbc "CreateRenderNode(3, \\"fresnelIOR\\")" fresnelIOR;	
				}else{
					floatSliderButtonGrp -e -en 0 -pre 3 -label "Fresnel IOR " -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"fresnelIOR\\",\\"fresnelIOR\\")" -sbc "CreateRenderNode(3, \\"fresnelIOR\\")" fresnelIOR;	
				}
				if($updateColor=="reflectionDimDistance" && $updateAttrValue==true){
					floatSliderButtonGrp -e -en 1 -pre 3 -label "Dim distance" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1000000000 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimDistance\\",\\"reflectionDimDistance\\")"  reflectionDimDistance;	
					floatSliderButtonGrp -e -en 1 -pre 3 -label "Dim distance On" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimFallOff\\",\\"reflectionDimFallOff\\")" reflectionDimFallOff;	
				}else{
					floatSliderButtonGrp -e -en 0 -pre 3 -label "Dim distance" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1000000000 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimDistance\\",\\"reflectionDimDistance\\")"  reflectionDimDistance;	
					floatSliderButtonGrp -e -en 0 -pre 3 -label "Dim distance On" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimFallOff\\",\\"reflectionDimFallOff\\")" reflectionDimFallOff;	
				}
				if($updateColor=="refractionExitColor" && $updateAttrValue==true){
					colorSliderButtonGrp -e -en 1 -label "refractionExitColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"refractionExitColor\\",\\"refractionExitColor\\")" -sbc "CreateRenderNode(3, \\"refractionExitColor\\")"  refractionExitColor;
				}else{
					colorSliderButtonGrp -e -en 0 -label "refractionExitColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"refractionExitColor\\",\\"refractionExitColor\\")" -sbc "CreateRenderNode(3, \\"refractionExitColor\\")"  refractionExitColor;
				}
				setAttr ($targetShader[$i] + "." + $updateAttr) $updateAttrValue;
				print ($targetShader[$i] + "." + $updateAttr + " => " + $updateAttrValue);
			}
		}
		else {
			print("----------------------------------- Ignored : \\"" + $targetShader[$i] + "." + $updateAttr + "\\n");
		}
	}
	if (`checkBox -q -v hilightGlossiness`==false){
		floatSliderButtonGrp -e -en 1 -pre 3 -label "HightGlossiness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"hilightGlossiness\\",\\"hilightGlossiness\\")" -sbc "CreateRenderNode(3, \\"hilightGlossiness\\")" hilightGlossiness;		
	}
	 if(`checkBox -q -v fresnelIOR`==false){
		floatSliderButtonGrp -e -en 1 -pre 3 -label "Fresnel IOR " -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"fresnelIOR\\",\\"fresnelIOR\\")" -sbc "CreateRenderNode(3, \\"fresnelIOR\\")" fresnelIOR;			
	} 
	if(`checkBox -q -v reflectionDimDistance`==true){
		floatSliderButtonGrp -e -en 1 -pre 3 -label "Dim distance" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1000000000 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimDistance\\",\\"reflectionDimDistance\\")"  reflectionDimDistance;	
		floatSliderButtonGrp -e -en 1 -pre 3 -label "Dim distance On" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimFallOff\\",\\"reflectionDimFallOff\\")" reflectionDimFallOff;			
	}
	if(`checkBox -q -v refractionExitColor`==true){
		colorSliderButtonGrp -e -en 1 -label "refractionExitColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"refractionExitColor\\",\\"refractionExitColor\\")" -sbc "CreateRenderNode(3, \\"refractionExitColor\\")"  refractionExitColor;
	}		
}

//CreateRenderNode
global proc CreateRenderNode(int $isColor, string $updateAttr){
	
	int $selectedOrAll = `radioButtonGrp -q -sl selectedOrAll`;
	string $targetShader[]={};
	global string $targetShaders[]={};
	if ($selectedOrAll == 1) {
		if ($isColor==3){
			$targetShader=`ls -typ VRayMtl -typ file -sl`;
		}else if($isColor==6){
			$targetShader=`ls -typ aiStandard -typ file -sl`;
		}else{
			$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file -sl`;
		}
	}
	else {
		if($isColor==3){
			$targetShader=`ls -typ VRayMtl -typ file`;
		}else if($isColor==6){
			$targetShader=`ls -typ aiStandard -typ file`;
		}else{
			$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file`;
		}	
	}
	if ( size($targetShader) == 0 ) {
		print ("No shader selected.\\n");
		return;
	}
	
	string $connected[];
	int $j=0;
	for ($i=0; $i<size($targetShader); $i++) {
		if (`attributeExists $updateAttr $targetShader[$i]`) {
			$targetShaders[$j]=$targetShader[$i];
			$j++;
		}else{
			print("----------------------------------- Ignored : \\"" + $targetShader[$i] + "." + $updateAttr + "\\n");
		} 
	}
	//print (size($targetShaders));
	if(size($targetShaders)==0){
		print "NO match shader Attribute";
		return;
	}
	if(`window -exists TransferShader`)
	{
     deleteUI -window TransferShader;   
    }
	window -t "create Render Node" -w 300 -h 100 TransferShader;
	columnLayout  -adjustableColumn 01 -rowSpacing 10 -columnWidth 250 TransferShader;
	text -l "先创建createRenderNodeWindows" -h 35;
  	button -label "createRenderNodeWindows "  -h 25 -c ("shader "+$targetShaders[0]+" "+$updateAttr);
  	button -label "TransferShaderAttr "  -h 25 -c ("TransferShaderTransferUVMatApply "+$updateAttr+" "+$isColor);
	showWindow TransferShader;
	
	
}

//赋材质属性
global proc TransferShaderTransferUVMatApply(string $updateAttr,int $isColor){
	int $selectedOrAll = `radioButtonGrp -q -sl selectedOrAll`;
	global string $targetShaders[];
	string $targetShader[];
	if ($isColor==3){
			$targetShader=`ls -typ VRayMtl -typ file -sl`;
	}else if($isColor==6){
		$targetShader=`ls -typ aiStandard -typ file -sl`;
	}else{
		$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file -sl`;
	}
	if (($selectedOrAll == 2)&&(size($targetShader)==1)) {
		string $target[];
		if($isColor==3){
			$target=`ls -typ VRayMtl -typ file`;
		}else if($isColor==6){
			$targetShader=`ls -typ aiStandard -typ file`;
		}else{
			$target = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file`;
		}
		string $shading=`connectionInfo -sourceFromDestination  ($targetShader[0]+"."+$updateAttr)`;
		if(size($shading)==0){
			print "你所选择的材质球没有链接";
			return;
		}
		int $i=0;
		for ($i=0; $i<size($target);$i++) {
			if($target[$i]==$targetShader[0]){
				continue;
			}
			if (`attributeExists $updateAttr $target[$i]`) {
				$connected = `listConnections -p 1 -c 1 ($target[$i] + "." + $updateAttr)`;
				//print ($targetShader[$i] + "." + $updateAttr);
				if (size($connected)) {
					if (catch(`disconnectAttr $connected[1] $connected[0]`))
					{
						print ("Cannot disconnect " + $connected[1] + " and " + $connected[0] + "\\n");
					}
				}
				connectAttr -force $shading ($target[$i]+"."+$updateAttr);
			}else{
				print("----------------------------------- Ignored : \\"" + $targetShader[$i] + "." + $updateAttr + "\\n");
			} 
		}
	}else {
		int $i=1;
		if(size($targetShaders)==1){
			print "没有要赋属性的材质";
			return;
		}
		string $shading=`connectionInfo -sourceFromDestination  ($targetShaders[0]+"."+$updateAttr)`;
		//string $shading[]=`listConnections -source 1 -destination 0 ($targetShaders[0]+"."+$updateAttr)`;
		if(size($shading)==0){
			print "请先创建CreateRenderNode";
			return;
		}
		for($i=1;$i<size($targetShaders);$i++){
			if (`attributeExists $updateAttr $targetShaders[$i]`) {
				$connected = `listConnections -p 1 -c 1 ($targetShaders[$i] + "." + $updateAttr)`;
				if (size($connected)) {
					if (catch(`disconnectAttr $connected[1] $connected[0]`))
					{
						print ("Cannot disconnect " + $connected[1] + " and " + $connected[0] + "\\n");
					}
				}	
				//defaultNavigation -force true -connectToExisting -source $shading -destination  ($targetShaders[$i]+"."+$updateAttr);
				connectAttr -force $shading ($targetShaders[$i]+"."+$updateAttr);
			}
		}
	}
}

//visor
//Create Render Node window 
global proc shader(string $targ,string $attr){
	defaultNavigation -createNew -destination  ($targ+"."+$attr);	
	if (`attributeExists $attr $targ`) {
		$connected = `listConnections -p 1 -c 1 ($targ + "." + $attr)`;
		if (size($connected)) {
			if (catch(`disconnectAttr $connected[1] $connected[0]`))
			{
				print ("Cannot disconnect " + $connected[1] + " and " + $connected[0] + "\\n");
			}
		}
	}
}

global proc breakBumpConn () {
	
	int $selectedOrAll = `radioButtonGrp -q -sl selectedOrAll`;
	
	string $targetShader[] = {};
	
	if ($selectedOrAll == 1) {
		$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file -sl`;
	}
	else {
		$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file`;
	}
	
	if ( size($targetShader) == 0 ) {
		print ("No shader selected.\\n");
		return;
	}
	
	string $connected[];
	
	for ($i=0; $i<size($targetShader); $i++) {
		
		if (`attributeExists "normalCamera" $targetShader[$i]`) {
			$connected = `listConnections -p 1 -c 1 ($targetShader[$i] + ".color")`;
			
			if (size($connected)) {
				disconnectAttr $connected[1] $connected[0];
			}
		}
	}
}

global proc optionMenuGrpType(int $isColor,string $updateAttr){
	int $selectedOrAll = `radioButtonGrp -q -sl selectedOrAll`;
	string $targetShader[] = {};
	
	if ($selectedOrAll == 1) {
		if ($isColor==3 ){
			$targetShader=`ls -typ VRayMtl -typ file -sl`;
		}else{
			$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file -sl`;
		}	
	}
	else {
		if($isColor==3){
			$targetShader=`ls -typ VRayMtl -typ file`;
		}else{
			$targetShader = `ls -typ lambert -typ blinn -typ phongE -typ phong -typ anisotropic -typ file`;
		}	
	}
	string $getoptionMenuGrpValue=`optionMenuGrp -q -v $updateAttr`;
	int  $updateAttrValue;
	if($updateAttr=="brdfType"){
		if($getoptionMenuGrpValue=="Phong"){
			$updateAttrValue=0;
		}else if($getoptionMenuGrpValue=="Blinn"){
			$updateAttrValue=1;
		}else if($getoptionMenuGrpValue=="Ward"){
			$updateAttrValue=2;
		}
	}else if($updateAttr=="affectAlpha"){
		if($getoptionMenuGrpValue=="Color only"){
			$updateAttrValue=0;
		}else if($getoptionMenuGrpValue=="Color+alpha"){
			$updateAttrValue=1;
		}else if($getoptionMenuGrpValue=="All channels"){
			$updateAttrValue=2;
		}
	}
	int $i;
	for ($i=0; $i<size($targetShader);$i++) {
		if (`attributeExists $updateAttr $targetShader[$i]`) {
			setAttr ($targetShader[$i] + "." + $updateAttr) $updateAttrValue;
		}else{
			print("----------------------------------- Ignored : \\"" + $targetShader[$i] + "." + $updateAttr + "\\n");
		} 
	}
}

global proc shaderMultiEditOverrideUI() {
	
	if (`window -ex shaderMultiEditOverrideWin`) {
		deleteUI shaderMultiEditOverrideWin;
		windowPref -remove shaderMultiEditOverrideWin;
	}
	
	int $colorButtonHeight = 23;
	int $floatButtonHeight = 22;
	
	window
		-tlc 180 200 -wh 460 655
		-menuBar true 
		-title "Shader Mutli Editor Override"
		shaderMultiEditOverrideWin;
	string $form=`formLayout`;
	tabLayout "tabs";
	formLayout -edit 
				-attachForm "tabs" "top" 0 
				-attachForm "tabs" "left" 0
				-attachForm "tabs" "bottom" 0 
				-attachForm "tabs" "right" 0 $form;
	scrollLayout -hst 0 -vst 8 -p "tabs" "普通材质";
	rowLayout -numberOfColumns 1 -adjustableColumn 1
    	-columnAttach 1 "both"  0
	    -columnAttach 2 "both"  0
		-columnWidth2 400 300
		defaultRowLayout;
	frameLayout -borderStyle "etchedIn" -label "Shader Multi Editor";
	text -l "Support mostly used attr of Lambert, Phong, PhongE, Blinn, Anisotropic, File node";
			text -l "[ Note: Original connections will be broken ]";
			separator;
				
			radioButtonGrp -nrb 2 -l "Target" -labelArray2 "Selected" "All in Scene" -select 1 -cw 1 60 -cw 2 70 selectedOrAll;
			separator;
			
			colorSliderButtonGrp -label "color" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"color\\",\\"color\\")" -sbc "CreateRenderNode(1,\\"color\\")" color;
			colorSliderButtonGrp -label "transparency" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"transparency\\",\\"transparency\\")" -sbc "CreateRenderNode(1,\\"transparency\\")" transparency;
			colorSliderButtonGrp -label "ambientColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"ambientColor\\",\\"ambientColor\\")" -sbc "CreateRenderNode(1,\\"ambientColor\\")" ambientColor;
			colorSliderButtonGrp -label "incandescence" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"incandescence\\",\\"incandescence\\")" -sbc "CreateRenderNode(1,\\"incandescence\\")" incandescence;
			colorSliderButtonGrp -label "specularColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"specularColor\\",\\"specularColor\\")" -sbc "CreateRenderNode(1,\\"specularColor\\")" specularColor;
			colorSliderButtonGrp -label "reflectedColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"reflectedColor\\",\\"reflectedColor\\")" -sbc "CreateRenderNode(1,\\"reflectedColor\\")" reflectedColor;
			colorSliderButtonGrp -label "whiteness" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"whiteness\\",\\"whiteness\\")" -sbc "CreateRenderNode(1,\\"whiteness\\")" whiteness;
				
			separator;
				
			colorSliderButtonGrp -label "colorGain" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay false -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"colorGain\\",\\"colorGain\\")" colorGain;
			colorSliderButtonGrp -label "colorOffset" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay false -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(1, \\"colorOffset\\", \\"colorOffset\\")" colorOffset;
				
			separator;
			button -l "Break Bump Mapping Connections" -c "breakBumpConn()";
				
			floatSliderButtonGrp -pre 3 -label "diffuse" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"diffuse\\",\\"diffuse\\")" -sbc "CreateRenderNode(1,\\"diffuse\\")"diffuse;
			floatSliderButtonGrp -pre 3 -label "translucence" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"translucence\\",\\"translucence\\")" -sbc "CreateRenderNode(1,\\"translucence\\")" translucence;
			floatSliderButtonGrp -pre 3 -label "translucenceDepth" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"translucenceDepth\\",\\"translucenceDepth\\")"  -sbc "CreateRenderNode(1,\\"translucenceDepth\\")"  translucenceDepth;
			floatSliderButtonGrp -pre 3 -label "translucenceFocus" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"translucenceFocus\\",\\"translucenceFocus\\")" -sbc "CreateRenderNode(1,\\"translucenceFocus\\")" translucenceFocus;
			floatSliderButtonGrp -pre 3 -label "eccentricity" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"eccentricity\\",\\"eccentricity\\")"  -sbc "CreateRenderNode(1,\\"eccentricity\\")" eccentricity;
				
			separator;
				
			floatSliderButtonGrp -pre 3 -label "specularRollOff" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"specularRollOff\\",\\"specularRollOff\\")"  -sbc "CreateRenderNode(1,\\"specularRollOff\\")" specularRollOff;
			floatSliderButtonGrp -pre 3 -label "reflectivity" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"reflectivity\\",\\"reflectivity\\")" -sbc "CreateRenderNode(1,\\"reflectivity\\")"  reflectivity;
			floatSliderButtonGrp -pre 0 -label "reflectionLimit" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"reflectionLimit\\",\\"reflectionLimit\\")" -sbc "CreateRenderNode(1,\\"reflectionLimit\\")"  reflectionLimit;
			floatSliderButtonGrp -pre 3 -label "reflectionSpecularity" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"reflectionSpecularity\\",\\"reflectionSpecularity\\")" -sbc "CreateRenderNode(1,\\"reflectionSpecularity\\")" reflectionSpecularity;
				
			separator;
				
			floatSliderButtonGrp -pre 3 -label "angle" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 360 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"angle\\",\\"angle\\")" -sbc  "CreateRenderNode(1,\\"angle\\")" angle;
			floatSliderButtonGrp -pre 3 -label "spreadX" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0.1 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"spreadX\\",\\"spreadX\\")" -sbc "CreateRenderNode(1,\\"spreadX\\")" spreadX;
			floatSliderButtonGrp -pre 3 -label "spreadY" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0.1 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"spreadY\\",\\"spreadY\\")"  -sbc "CreateRenderNode(1,\\"spreadY\\")" spreadY;
			floatSliderButtonGrp -pre 3 -label "roughness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"roughness\\",\\"roughness\\")" -sbc "CreateRenderNode(1,\\"roughness\\")" roughness;
			floatSliderButtonGrp -pre 3 -label "fresnelRefractiveIndex" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 1 -max 3 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"fresnelRefractiveIndex\\",\\"fresnelRefractiveIndex\\")" -sbc "CreateRenderNode(1,\\"fresnelRefractiveIndex\\")" fresnelRefractiveIndex;
			floatSliderButtonGrp -pre 3 -label "highlightSize" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"highlightSize\\",\\"highlightSize\\")"  -sbc "CreateRenderNode(1,\\"highlightSize\\")" highlightSize;
			floatSliderButtonGrp -pre 3 -label "cosinePower" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 2 -max 100 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"cosinePower\\",\\"cosinePower\\")" -sbc "CreateRenderNode(1,\\"cosinePower\\")" cosinePower;
			floatSliderButtonGrp -pre 3 -label "glowIntensity" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"glowIntensity\\",\\"glowIntensity\\")" -sbc "CreateRenderNode(1,\\"glowIntensity\\")" glowIntensity;
			floatSliderButtonGrp -pre 3 -label "matteOpacity" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"matteOpacity\\",\\"matteOpacity\\")" -sbc "CreateRenderNode(1,\\"matteOpacity\\")"  matteOpacity;
				
			separator;
								
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "refractions" -align "right" refractions;
				button -l "UPDATE" -c "updateShaderAttr(2, \\"refractions\\",\\"refractions\\")";
			setParent..;
				
			separator;
				
			floatSliderButtonGrp -pre 3 -label "refractiveIndex" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0.01 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"refractiveIndex\\",\\"refractiveIndex\\")" -sbc "CreateRenderNode(1,\\"refractiveIndex\\")" refractiveIndex;
			floatSliderButtonGrp -pre 3 -label "refractionLimit" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"refractionLimit\\",\\"refractionLimit\\")" -sbc "CreateRenderNode(1,\\"refractionLimit\\")" refractionLimit;
			floatSliderButtonGrp -pre 3 -label "lightAbsorbance" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"lightAbsorbance\\",\\"lightAbsorbance\\")" -sbc "CreateRenderNode(1,\\"lightAbsorbance\\")" lightAbsorbance;
			floatSliderButtonGrp -pre 3 -label "surfaceThickness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"surfaceThickness\\",\\"surfaceThickness\\")" -sbc "CreateRenderNode(1,\\"surfaceThickness\\")"  surfaceThickness;
			floatSliderButtonGrp -pre 3 -label "shadowAttenuation" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"shadowAttenuation\\",\\"shadowAttenuation\\")" -sbc "CreateRenderNode(1,\\"shadowAttenuation\\")"  shadowAttenuation;
				
			separator;
				
			floatSliderButtonGrp -pre 0 -s 1 -label "filterType" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 5 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"filterType\\",\\"filterType\\")" filterType;
			floatSliderButtonGrp -pre 3 -label "filter" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"filter\\",\\"filter\\")" filter;
			floatSliderButtonGrp -pre 3 -label "filterOffset" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(0, \\"filterOffset\\",\\"filterOffset\\")" filterOffset;
		
		setParent..;
		setParent..;
		setParent..;
		setParent..;
		
		scrollLayout -hst 0 -vst 8 -p "tabs" "VRayMtl";
		rowLayout -numberOfColumns 1 -adjustableColumn 1
    	-columnAttach 1 "both"  0
	    -columnAttach 2 "both"  0
		-columnWidth2 400 300
		defaultRowLayout;
	frameLayout -borderStyle "etchedIn" -label "Shader Multi Editor";
	text -l "Support mostly used attr of VrayMtl";
			text -l "[ Note: Original connections will be broken ]";
			separator;
			colorSliderButtonGrp -label "diffuseColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"color\\",\\"diffuseColor\\")" -sbc "CreateRenderNode(3, \\"color\\")" diffuseColor;
			colorSliderButtonGrp -label "opacityMap" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"transparency\\",\\"opacityMap\\")" -sbc "CreateRenderNode(3, \\"transparency\\")"  opacityMap;
			colorSliderButtonGrp -label "self_Illumination" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"illumColor\\",\\"self_Illumination\\")" -sbc "CreateRenderNode(3, \\"illumColor\\")"  self_Illumination;
			separator;
			colorSliderButtonGrp -label "reflectionColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"reflectionColor\\",\\"reflectionColor\\")" -sbc "CreateRenderNode(3, \\"diffuseColor\\")"  reflectionColor;
			colorSliderButtonGrp -label "reflectionExitColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"reflectionExitColor\\",\\"reflectionExitColor\\")" -sbc "CreateRenderNode(3, \\"reflectionExitColor\\")"  reflectionExitColor;
			separator;
			
			colorSliderButtonGrp -label "refractionColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"refractionColor\\",\\"refractionColor\\")" -sbc "CreateRenderNode(3, \\"refractionColor\\")"  refractionColor;
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "refractionExitColorOn" -align "right"  refractionExitColor;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"refractionExitColorOn\\",\\"refractionExitColor\\")";
			setParent..;
			colorSliderButtonGrp -en 0 -label "refractionExitColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"refractionExitColor\\",\\"refractionExitColor\\")" -sbc "CreateRenderNode(3, \\"refractionExitColor\\")"  refractionExitColor;
			colorSliderButtonGrp -label "fogColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay false -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(3, \\"fogColor\\",\\"fogColor\\")"  fogColor;
		
			separator;
			
			floatSliderButtonGrp -pre 3 -label "diffuseColorAmount" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"diffuseColorAmount\\",\\"diffuseColorAmount\\")" -sbc "CreateRenderNode(3, \\"diffuseColorAmount\\")" diffuseColorAmount;		
			floatSliderButtonGrp -pre 3 -label "RoughnessAmount" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"roughnessAmount\\",\\"roughnessAmount\\")" -sbc "CreateRenderNode(3, \\"roughnessAmount\\")" roughnessAmount;	
			
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
			//columnLayout;
			optionMenuGrp  -l "Brdf Type" -h 20 brdfType;
			menuItem -label "Phong";
			menuItem -label "Blinn";
			menuItem -label "Ward";
			button -l "UPDATE" -c "optionMenuGrpType(3,\\"brdfType\\")";
			optionMenuGrp -e -v "Blinn" -l "Brdf Type" -h 20 brdfType;
			setParent..;
			floatSliderButtonGrp -pre 3 -label "reflectionColorAmount" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionColorAmount\\",\\"reflectionColorAmount\\")" -sbc "CreateRenderNode(3, \\"reflectionColorAmount\\")" reflectionColorAmount;	
			separator;
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Lock highlight and reflection glossiness" -align "right" -v 1 hilightGlossiness;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"hilightGlossinessLock\\",\\"hilightGlossiness\\")";
			setParent..;
			
			floatSliderButtonGrp -en 0 -pre 3 -label "HightGlossiness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"hilightGlossiness\\",\\"hilightGlossiness\\")" -sbc "CreateRenderNode(3, \\"hilightGlossiness\\")" hilightGlossiness;	
			separator;
			floatSliderButtonGrp -pre 3 -label "reflectionGlossiness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionGlossiness\\",\\"reflectionGlossiness\\")" -sbc "CreateRenderNode(3, \\"reflectionGlossiness\\")" reflectionGlossiness;	
			floatSliderButtonGrp -pre 0 -v 1 -label "reflectionsubdivs" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 1 -max 20 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionSubdivs\\",\\"reflectionSubdivs\\")" reflectionSubdivs;	
			separator;
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Use interpolation" -align "right" reflInterpolation;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"reflInterpolation\\",\\"reflInterpolation\\")";
			setParent..;
			
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Use Frasnel" -align "right" useFresnel;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"useFresnel\\",\\"useFresnel\\")";
			setParent..;
			
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Lock Fresnel IOR To Refraction IOR" -align "right" -v 1 fresnelIOR;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"lockFresnelIORToRefractionIOR\\",\\"fresnelIOR\\")";
			setParent..;
			floatSliderButtonGrp -en 0 -pre 3 -label "Fresnel IOR " -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"fresnelIOR\\",\\"fresnelIOR\\")" -sbc "CreateRenderNode(3, \\"fresnelIOR\\")" fresnelIOR;	
		
			separator;
			floatSliderButtonGrp -pre 0 -v 1 -label "Maxdepth" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 1 -max 10 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionsMaxDepth\\",\\"reflectionsMaxDepth\\")"  reflectionsMaxDepth;
			floatSliderButtonGrp -pre 3 -label "softenEdge" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"softenEdge\\",\\"softenEdge\\")" softenEdge;		
			separator;
			
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Trace Reflections" -align "right" -v 1 traceReflections;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"traceReflections\\",\\"traceReflections\\")";
			setParent..;
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Reflect on Back Side" -align "right" reflectOnBackSide;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"reflectOnBackSide\\",\\"reflectOnBackSide\\")";
			setParent..;
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Fix Dark Edges" -align "right" fixDarkEdges;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"fixDarkEdges\\",\\"fixDarkEdges\\")";
			setParent..;
			separator;
			
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Dim distance on" -align "right"  reflectionDimDistance;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"reflectionDimDistanceOn\\",\\"reflectionDimDistance\\")";
			setParent..;
			floatSliderButtonGrp -en 0 -pre 3 -label "Dim distance" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1000000000 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimDistance\\",\\"reflectionDimDistance\\")"  reflectionDimDistance;	
			floatSliderButtonGrp -en 0 -pre 3 -label "Dim distance On" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"reflectionDimFallOff\\",\\"reflectionDimFallOff\\")" reflectionDimFallOff;	
			separator;
			
			floatSliderButtonGrp -pre 3 -v 1 -label "refractionColorAmount" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"refractionColorAmount\\",\\"refractionColorAmount\\")" -sbc "CreateRenderNode(3, \\"refractionColorAmount\\")"  refractionColorAmount;	
			
			floatSliderButtonGrp -pre 3 -v 1 -label "refractionGlossiness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"refractionGlossiness\\",\\"refractionGlossiness\\")" -sbc "CreateRenderNode(3, \\"refractionGlossiness\\")"  refractionGlossiness;	
			floatSliderButtonGrp -pre 3 -v 8 -label "refractionSubdivs" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 1 -max 64 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"refractionSubdivs\\",\\"refractionSubdivs\\")"  refractionSubdivs;	
			
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Use interpolation" -align "right" refrInterpolation;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"refrInterpolation\\",\\"refrInterpolation\\")";
			setParent..;
			
			floatSliderButtonGrp -pre 3 -v 1.6 -label "refractionIOR" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"refractionIOR\\",\\"refractionIOR\\")" -sbc "CreateRenderNode(3, \\"refractionIOR\\")"  refractionIOR;	
			
			floatSliderButtonGrp -pre 3 -v 1 -label "fogMultiplier" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 1 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"fogMult\\",\\"fogMult\\")"  fogMult;	
			floatSliderButtonGrp -pre 3 -label "fogBias" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min -3 -max 3 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"fogBias\\",\\"fogBias\\")"  fogBias;	
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "Trace Refractions" -align "right" traceRefractions;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"traceRefractions\\",\\"traceRefractions\\")";
			setParent..;
			floatSliderButtonGrp -pre 3 -v 1 -label "refractionsMaxDepth" -field true -buttonLabel "UPDATE" -symbolButtonDisplay false -cw 1 130 -cw 2 50 -min 1 -max 10 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(4, \\"refractionsMaxDepth\\",\\"refractionsMaxDepth\\")"  refractionsMaxDepth;	
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -v 1 -label "Affect Shadows" -align "right" affectShadows;
				button -l "UPDATE" -c "updateShaderAttr(5, \\"affectShadows\\",\\"affectShadows\\")";
			setParent..;
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
			optionMenuGrp -l "Affect Channels" -h 20  affectAlpha;
			menuItem -label "Color only";
			menuItem -label "Color+alpha";
			menuItem -label "All channels";
			button -l "UPDATE" -c "optionMenuGrpType(3,\\"affectAlpha\\")";
			setParent..;
			
		setParent..;
		setParent..;
		setParent..;
		setParent..;
		
		scrollLayout -hst 0 -vst 8 -p "tabs" "Arnold";
		rowLayout -numberOfColumns 1 -adjustableColumn 1
    	-columnAttach 1 "both"  0
	    -columnAttach 2 "both"  0
		-columnWidth2 400 300
		defaultRowLayout;
		frameLayout -borderStyle "etchedIn" -label "Shader Multi Editor";
		//AiStandard
			separator;
			text -l "Support mostly used attr of AiStandard";
			text -l "[ Note: Original connections will be broken ]";

			text -l "";
			text -l "Matte";
			rowLayout -nc 2 -cw 1 344 -cw 2 200;
				checkBox -label "EnableMatte" -align "right" aiEnableMatte;
				button -l "UPDATE" -c "updateShaderAttr(8, \\"aiEnableMatte\\",\\"aiEnableMatte\\")";
				
			setParent..;
				colorSliderButtonGrp -label "Matte color" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(6, \\"aiMatteColor\\",\\"aiMatteColor\\")" -sbc "CreateRenderNode(6,\\"aiMatteColor\\")" aiMatteColor;
				floatSliderButtonGrp -pre 3 -v 1 -label "Matte Opacity" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(7, \\"aiMatteColorA\\",\\"aiMatteColorA\\")"  -sbc "CreateRenderNode(6,\\"aiMatteColorA\\")"  aiMatteColorA;	

			text -l "";
			text -l "Diffuse";
		    colorSliderButtonGrp -label "color" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(6, \\"color\\",\\"difcolor\\")" -sbc "CreateRenderNode(6,\\"color\\")" difcolor;

		    floatSliderButtonGrp -pre 3 -v 1 -label "Weight" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(7, \\"Kd\\",\\"Kd\\")"  -sbc "CreateRenderNode(6,\\"Kd\\")"  Kd;	
		    floatSliderButtonGrp -pre 3 -v 0 -label "Roughness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(7, \\"diffuseRoughness\\",\\"diffuseRoughness\\")"  -sbc "CreateRenderNode(6,\\"diffuseRoughness\\")"  diffuseRoughness;	


		    separator;
		    text -l "";
			text -l "Specluar";
			colorSliderButtonGrp -label "Color" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(6, \\"KsColor\\",\\"KsColor\\")" -sbc "CreateRenderNode(6,\\"KsColor\\")" KsColor;

			floatSliderButtonGrp -pre 3 -v 0 -label "Weight" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(7, \\"Ks\\",\\"Ks\\")"  -sbc "CreateRenderNode(6,\\"Ks\\")"  Ks;
			floatSliderButtonGrp -pre 3 -v 1 -label "Roughness" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(7, \\"specularRoughness\\",\\"specularRoughness\\")"  -sbc "CreateRenderNode(6,\\"specularRoughness\\")"  specularRoughness;

			separator;
			text -l "";
			text -l "Reflection";
			colorSliderButtonGrp -label "Color" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(6, \\"KrColor\\",\\"KrColor\\")" -sbc "CreateRenderNode(6,\\"KrColor\\")" KrColor;
			floatSliderButtonGrp -pre 3 -v 1 -label "Weight" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(7, \\"Kr\\",\\"Kr\\")"  -sbc "CreateRenderNode(6,\\"Kr\\")"  Kr;	

			separator;
			text -l "";
			text -l "Refraction";
			colorSliderButtonGrp -label "KtColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(6, \\"KtColor\\",\\"KtColor\\")" -sbc "CreateRenderNode(6,\\"KtColor\\")" KtColor;
			colorSliderButtonGrp -label "opacity" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(6, \\"opacity\\",\\"opacity\\")" -sbc "CreateRenderNode(6,\\"opacity\\")" opacity;

			text -l "";
			text -l "Emission";
			colorSliderButtonGrp -label "emissionColor" -buttonLabel "UPDATE" -rgb 0 0 0 -symbolButtonDisplay true -cw 1 130 -cw 2 60 -cw 3 145 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(6, \\"emissionColor\\",\\"emissionColor\\")" -sbc "CreateRenderNode(6,\\"emissionColor\\")" emissionColor;
			floatSliderButtonGrp -pre 3 -v 1 -label "emissionScale" -field true -buttonLabel "UPDATE" -symbolButtonDisplay true -cw 1 130 -cw 2 50 -min 0 -max 1 -fieldMaxValue 99999 -image "navButtonUnconnected.xpm" -bc "updateShaderAttr(7, \\"emission\\",\\"emission\\")"  -sbc "CreateRenderNode(6,\\"emission\\")"  emission;	

		setParent defaultRowLayout;
				
	showWindow shaderMultiEditOverrideWin;

}
	
	''')