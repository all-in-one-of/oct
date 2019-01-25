# -*- coding: utf-8 -*-
import maya.mel as mm

def ChangeMayaLightAttr_YH():
	mm.eval(u'''
		global proc changeAttrWithIncrement()
{
	if (`window -ex changeLightAttribute`) {
		deleteUI changeLightAttribute;
		windowPref -remove changeLightAttribute;
	}
string $window = `window -title "change Attribute" -menuBar true  -widthHeight 420 820 changeLightAttribute`;
scrollLayout -hst 0 -vst 8 A;
columnLayout -adjustableColumn true;

			
//textFieldGrp -label "Attribute name" -text dmapResolution Attr_name;
	
	optionMenu -label "Attribute name"  Attr_name;
	    			menuItem -label "dmapResolution";
	    			menuItem -label "dmapFilterSize";
	    			menuItem -label "dmapBias";
	    			menuItem -label "intensity";
	    			menuItem -label "useDepthMapShadows";
	    			menuItem -label "emitSpecular";
	    			menuItem -label "emitDiffuse";
	    			menuItem -label "bumpValue";
	    			menuItem -label "bumpDepth";
    				menuItem -label "Visibility";
    				menuItem -label "aiSamples";
    				menuItem -label "aiNormalize";
    				menuItem -label "aiCastShadows";
			 		menuItem -label "aiShadowDensity";
			 		menuItem -label "aiAffectVolumetrics";
			 		menuItem -label "aiCastVolumetricShadows";
			 		menuItem -label "aiVolumeSamples";
			 		menuItem -label "aiDiffuse";
			 		menuItem -label "aiSpecular";
			 		menuItem -label "aiSss";
			 		menuItem -label "aiVolume";
			 		menuItem -label "aiIndirect";
			 		menuItem -label "aiMaxBounces";
			 		menuItem -label "useRayTraceShadows";
			 		menuItem -label "lightRadius";
			 		menuItem -label "shadowRays";
			 		menuItem -label "rayDepthLimit";

	floatFieldGrp -numberOfFields 1 -label "value"  -value1 128 num;
	
separator;



//*************************************
// action button
//*************************************

button -label "change Value"  -c ("changeAttr");		
		
		
separator;

	floatFieldGrp -numberOfFields 1 -label "increment" -value1 0.5 incre;
	
		button -label "Upadte new Value"   -c ("updateAttr");	
separator;

	floatFieldGrp -numberOfFields 1 -label "multiplier"  -value1 0.5 multi;
	
		button -label "Upadte multiplied Value"  -c ("updateMultiAttr");
separator;
	colorSliderGrp -label "light colour" -rgb 0.2 0.5 0.85 lightColour;
		button -label "Update new Colour" -c ("updateColour");

separator;
	colorSliderGrp -label "shadow colour" -rgb 0.2 0.5 0.85 shadowColour;
		button -label "Update shadow Colour" -c ("updateShadowColour");
separator;
	checkBox -label "Use Ray Trace Shadows" -value true UseRayTraceShadows;
		button -l "Update RayTraceShadows"  -c ("updateRayTraceShadows");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Light Radius" -value1 1 LightRadius;	
		button -label "Upadte Light Radius" -c ("updateLightRadius");

separator;	
	floatFieldGrp -numberOfFields 1 -label " aiRadius" -value1 1 LightAiRadius;	
		button -label "Upadte aiRadius" -c ("updateLightAiRadius");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Shadow Rays" -value1 1 ShadowRays;	
		button -label "Upadte Shadow Rays" -c ("updateShadowRays");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Ray Depth Limit" -value1 1 RayDepthLimit;	
		button -label "Upadte Ray Depth Limit" -c ("updateRayDepthLimit");
//aaaa		
separator;	
	floatFieldGrp -numberOfFields 1 -label "Cone Angle" -value1 1 ConeAngle;	
		button -label "Upadte Cone Angle" -c ("UpadteConeAngle");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Penumbra Angle" -value1 1 PenumbraAngle;	
		button -label "Upadte Penumbra Angle" -c ("UpadtePenumbraAngle");
		
separator;	
	floatFieldGrp -numberOfFields 1 -label "Dropoff" -value1 1 Dropoff;	
		button -label "Upadte Dropoff" -c ("UpadteDropoff");
		
separator;
        text -label "";	
		button -label "Create LightFog" -c ("UpadteLightFog");

separator;
        text -label "";	
		button -label "Select LightFog" -c ("SelectLightFog");

separator;
		colorSliderGrp -label "lightFog Color" -rgb 0.2 0.5 0.85 lightFogColor;	
		button -label "Upadte lightFog Color" -c ("UpadtelightFogColor");

separator;
        floatFieldGrp -numberOfFields 1 -label "lightFog Density" -value1 1 lightFogDensity;	
		button -label "Upadte lightFog Density" -c ("UpadtelightFogDensity");
		

separator;	
	floatFieldGrp -numberOfFields 1 -label "Samples" -bgc 0.3 0.2 0.4 -value1 1 samples;	
		button -label "Upadte new samples" -bgc 0.3 0.2 0.4 -c ("updateSamples");

separator;
	checkBox -label "Normalize" -value true  -bgc 0.3 0.2 0.4 Normalize;
	button -l "Update Normalize" -bgc 0.3 0.2 0.4  -c ("updateAiNormalize");

separator;
	checkBox -label "Cast Shadows" -value true -bgc 0.3 0.2 0.4 CastShadows;
	button -l "Update CastShadows"  -bgc 0.3 0.2 0.4 -c ("updateAiCastShadows");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Shadow Density" -bgc 0.3 0.2 0.4 -value1 1 ShadowDensity;	
		button -label "Upadte new ShadowDensity" -bgc 0.3 0.2 0.4 -c ("updateShadowDensity");

separator;
	checkBox -label "Affect Volumetrics" -value true -bgc 0.3 0.2 0.4  AffectVolumetrics;
	button -l "Update AffectVolumetrics" -bgc 0.3 0.2 0.4  -c ("updateAffectVolumetrics");

separator;
	checkBox -label "Cast Volumetric Shadows" -value true -bgc 0.3 0.2 0.4 CastVolumetricShadows;
	button -l "Update CastVolumetricShadows" -bgc 0.3 0.2 0.4  -c ("updateCastVolumetricShadows");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Volume Samples" -bgc 0.3 0.2 0.4 -value1 1 VolumeSamples;	
		button -label "Upadte new VolumeSamples" -bgc 0.3 0.2 0.4  -c ("updateVolumeSamples");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Diffuse" -bgc 0.3 0.2 0.4  -value1 1 Diffuse;	
		button -label "Upadte new Diffuse" -bgc 0.3 0.2 0.4 -c ("updateaiDiffuse");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Specular" -bgc 0.3 0.2 0.4 -value1 1 Specular;	
		button -label "Upadte new Specular" -bgc 0.3 0.2 0.4 -c ("updateSpecular");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Sss" -bgc 0.3 0.2 0.4 -value1 1 Sss;	
		button -label "Upadte new Sss" -bgc 0.3 0.2 0.4 -c ("updateSss");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Indirect" -bgc 0.3 0.2 0.4  -value1 1 Indirect;	
		button -label "Upadte new Indirect" -bgc 0.3 0.2 0.4 -c ("updateIndirect");
separator;	
	floatFieldGrp -numberOfFields 1 -label "Volume" -bgc 0.3 0.2 0.4  -value1 1 Volume;	
		button -label "Upadte new Volume" -bgc 0.3 0.2 0.4 -c ("updateVolume");

separator;	
	floatFieldGrp -numberOfFields 1 -label "Max Bounces" -bgc 0.3 0.2 0.4 -value1 999 MaxBounces;	
		button -label "Upadte Max Bounces" -bgc 0.3 0.2 0.4 -c ("updateMaxBounces");

//vray灯光
separator;
		colorSliderGrp -label "Light Color" -rgb 0 0 0 LightColor;	
		button -label "Upadte Light Color" -c ("updateLightColor");
		
separator;	
	floatFieldGrp -numberOfFields 1 -label "intensity multiplier"  -value1 30 IntensityMult;	
		button -label "Upadte intensity multiplier"  -c ("upadteIntensitymultiplier");
		
separator;	
	floatFieldGrp -numberOfFields 1 -label "Subdivs"  -value1 30 subdivs;	
		button -label "Upadte Subdivs"  -c ("upadteSubdivs");
		
separator;
	checkBox -label "Shadows" -value true shadows;
	button -l "Update Shadows"  -c ("updateShadows");
	
separator;
	checkBox -label "noDecay" -value true noDecay;
	button -l "Update noDecay"  -c ("updatenoDecay");

separator;
	checkBox -label "invisible" -value true invisible;
	button -l "Update invisible"  -c ("updateInvisible");

//arnold灯光
separator;	
	floatFieldGrp -numberOfFields 1 -label "Exposure"  -value1 0.0 aiExposure;	
		button -label "Upadte Exposure"  -c ("upadteExposure");

separator;
		button -label "Close" -bgc 0.4 0.2 0.3  -c ("deleteUI -window " + $window);
		
showWindow $window;

}


global proc changeAttr()
{
	//***************main***********************

	int $count;
	
//string $attr_name = `optionMenu -q Attr_name`;
	string $attr_name = eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $value = `floatFieldGrp -q -v1 num`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	
	
	
	for($count = 0; $count < $selnum; $count++ )
	{    
		string $text_obj = $sel[$count];
		doing $text_obj $value $attr_name;
	}
}
	

global proc doing(string $text_obj, float $value, string $attr_name)

{
	eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$value+"`)");	
}






global proc updateAttr()
{
	//***************main***********************

	int $count;
	
	string $attr_name = eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $addValue = `floatFieldGrp -q -v1 incre`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	
	
	
	for( $count = 0; $count < $selnum; $count++ )
	{    
		string $text_obj = $sel[$count];
		addUpdate $text_obj $addValue $attr_name;
	}
}


global proc addUpdate(string $text_obj, float $addValue, string $attr_name)

{
//$name = `getAttr ($item + ".fileTextureName")`;
	string $originalValue = `getAttr ($text_obj+"."+$attr_name)`;
	string $updatedValue = $originalValue + $addValue;
	 
	eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$updatedValue+"`)");

}




global proc updateMultiAttr()
{
	//***************main***********************

	int $count;
	
	string $attr_name = eval("optionMenu -q  -v \\"Attr_name\\" ");
	$multiValue = `floatFieldGrp -q -v1 multi`;
	$sel = `ls -sl`;
	int $selnum = size( $sel );
	
	
	
	for( $count = 0; $count < $selnum; $count++ )
	{    
		string $text_obj = $sel[$count];
		multiUpdate $text_obj $multiValue $attr_name;
	}
}


global proc multiUpdate(string $text_obj, float $multiValue, string $attr_name)

{

	float $originalValue = `getAttr ($text_obj+"."+$attr_name)`;
	float $multipledValue = $originalValue * $multiValue;
	 
	eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$multipledValue+"`)");

}





global proc updateColour()
{
	//***************main***********************

	int $count;
	
//string $attr_name = `optionMenu -q Attr_name`;
//string $attr_name = eval("optionMenu -q  -v \\"Attr_name\\" ");
//$value = `floatFieldGrp -q -v1 num`;

	float $lightRGB[] = `colorSliderGrp -q -rgb lightColour`;
	float $lightR = $lightRGB[0];
	float $lightG = $lightRGB[1];
	float $lightB = $lightRGB[2];


	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	
	
	
	for( $count = 0; $count < $selnum; $count++ )
	{    
		string $text_obj = $sel[$count];
		doing $text_obj $lightR colorR;
		doing $text_obj $lightG colorG;
		doing $text_obj $lightB colorB;
	}
}


global proc updateShadowColour()
{
	//***************main***********************

	int $count;
	


	float $shadowRGB[] = `colorSliderGrp -q -rgb shadowColour`;
	float $shadowR = $shadowRGB[0];
	float $shadowG = $shadowRGB[1];
	float $shadowB = $shadowRGB[2];


	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	
	
	
	for( $count = 0; $count < $selnum; $count++ )
	{    
		string $text_obj = $sel[$count];
		doing $text_obj $shadowR shadColorR;
		doing $text_obj $shadowG shadColorG;
		doing $text_obj $shadowB shadColorB;
	}
}

global proc updateSamples(){
	int $count;
	string $attr_name = eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $samples = `floatFieldGrp -q -v1 samples`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$samples+"`)");
	}

}
global proc updateAiNormalize(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	int $Normalize = `checkBox -q -v Normalize`;
	string $sel[]= `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$Normalize+"`)");
	}
}

global proc updateAiCastShadows(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	int $CastShadows = `checkBox -q -v CastShadows`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$CastShadows+"`)");
	}
}

global proc updateRayTraceShadows(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	int $UseRayTraceShadows = `checkBox -q -v UseRayTraceShadows`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$UseRayTraceShadows+"`)");
	}
}

global proc updateLightRadius(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $LightRadius = `floatFieldGrp -q -v1 LightRadius`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$LightRadius+"`)");
	}
}

global proc updateLightAiRadius(){
	int $count;
	string $attr_name="aiRadius";
	float $LightAiRadius = `floatFieldGrp -q -v1 LightAiRadius`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$LightAiRadius+"`)");
	}
}

global proc updateShadowRays(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $ShadowRays = `floatFieldGrp -q -v1 ShadowRays`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$ShadowRays+"`)");
	}
}

global proc updateRayDepthLimit(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $RayDepthLimit = `floatFieldGrp -q -v1 RayDepthLimit`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$RayDepthLimit+"`)");
	}
}

global proc UpadteConeAngle(){
	int $count;
	string $attr_name="coneAngle";
	float $ConeAngle = `floatFieldGrp -q -v1 ConeAngle`;
	string $sel[] = `ls -sl`;
	print $sel;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj[] =`listRelatives -s $sel[$count]`;
		eval ("catch (`setAttr "+$text_obj[0]+"."+$attr_name+" "+$ConeAngle+"`)");
	}
}

global proc UpadtePenumbraAngle(){
	int $count;
	string $attr_name="penumbraAngle";
	float $PenumbraAngle = `floatFieldGrp -q -v1 PenumbraAngle`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$PenumbraAngle+"`)");
	}
}

global proc UpadteDropoff(){
	int $count;
	string $attr_name="dropoff";
	float $Dropoff = `floatFieldGrp -q -v1 Dropoff`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$Dropoff+"`)");
	}
}

global proc UpadteLightFog(){
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		defaultNavigation -createNew -destination ($text_obj+".fogGeometry");
	}
}
global proc SelectLightFog(){
	string $allLights[]=`ls -type "lightFog"`;
	select $allLights;
}

global proc UpadtelightFogColor(){
	int $count;

	float $shadowRGB[] = `colorSliderGrp -q -rgb lightFogColor`;
	float $shadowR = $shadowRGB[0];
	float $shadowG = $shadowRGB[1];
	float $shadowB = $shadowRGB[2];


	string $allLights[]=`ls -type "lightFog"`;
	int $selnum = size($allLights);
	
	
	
	for( $count = 0; $count < $selnum; $count++ )
	{    
		string $text_obj = $allLights[$count];
		doing $text_obj $shadowR colorR;
		doing $text_obj $shadowG colorG;
		doing $text_obj $shadowB colorB;
	}
	
}

global proc UpadtelightFogDensity(){
	string $attr_name="density";
	float $lightFogDensity = `floatFieldGrp -q -v1 lightFogDensity`;
	string $allLights[]=`ls -type "lightFog"`;
	int $selnum = size($allLights);
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $allLights[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$lightFogDensity+"`)");
	} 
}

global proc updateShadowDensity(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $ShadowDensity = `floatFieldGrp -q -v1 ShadowDensity`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$ShadowDensity+"`)");
	}
}

global proc updateAffectVolumetrics(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	int $AffectVolumetrics = `checkBox -q -v AffectVolumetrics`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$AffectVolumetrics+"`)");
	}
}

global proc updateCastVolumetricShadows(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	int $CastVolumetricShadows = `checkBox -q -v CastVolumetricShadows`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$CastVolumetricShadows+"`)");
	}
}

global proc updateVolumeSamples(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	$VolumeSamples = `floatFieldGrp -q -v1 VolumeSamples`;
	$sel = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$VolumeSamples+"`)");
	}
}
global proc updateaiDiffuse(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $Diffuse = `floatFieldGrp -q -v1 Diffuse`;
	$sel = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$Diffuse+"`)");
	}
}

global proc updateSpecular(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $Specular = `floatFieldGrp -q -v1 Specular`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$Specular+"`)");
	}
}

global proc updateSss(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $Sss = `floatFieldGrp -q -v1 Sss`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$Sss+"`)");
	}
}
global proc updateIndirect(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $Indirect = `floatFieldGrp -q -v1 Indirect`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$Indirect+"`)");
	}
}

global proc updateVolume(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $Volume = `floatFieldGrp -q -v1 Volume`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$Volume+"`)");
	}
}

global proc updateMaxBounces(){
	int $count;
	string $attr_name=eval("optionMenu -q  -v \\"Attr_name\\" ");
	float $MaxBounces = `floatFieldGrp -q -v1 MaxBounces`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$MaxBounces+"`)");
	}
}

global proc updateLightColor(){
	int $count;

	float $shadowRGB[] = `colorSliderGrp -q -rgb LightColor`;

	string $allLights[]=`ls -sl`;
	int $selnum = size($allLights);
	
	
	
	for( $count = 0; $count < $selnum; $count++ )
	{    
		string $text_obj = $allLights[$count];
		eval ("catch (`setAttr "+$text_obj+".lightColor"+" "+$shadowRGB[0]+" "+$shadowRGB[1]+" "+$shadowRGB[2]+"`)");
	}
	
}
global proc upadteIntensitymultiplier(){
	int $count;
	string $attr_name="intensityMult";
	float $intensityMult = `floatFieldGrp -q -v1 IntensityMult`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$intensityMult+"`)");
	}
}

global proc upadteSubdivs(){
	int $count;
	string $attr_name="subdivs";
	float $subdivs = `floatFieldGrp -q -v1 subdivs`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$subdivs+"`)");
	}
}

global proc updateShadows(){
	int $count;
	string $attr_name="shadows";
	int $shadows = `checkBox -q -v shadows`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$shadows+"`)");
	}
}

global proc updatenoDecay(){
	int $count;
	string $attr_name="noDecay";
	int $noDecay = `checkBox -q -v noDecay`;
	string $sel[]= `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$noDecay+"`)");
	}
}

global proc updateInvisible(){
	int $count;
	string $attr_name="invisible";
	int $invisible = `checkBox -q -v invisible`;
	string $sel[]= `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$invisible+"`)");
	}
}

global proc upadteExposure(){
	int $count;
	string $attr_name="aiExposure";
	float $subdivs = `floatFieldGrp -q -v1 aiExposure`;
	string $sel[] = `ls -sl`;
	int $selnum = size( $sel );
	for($count=0;$count<$selnum;$count++){
		string $text_obj = $sel[$count];
		eval ("catch (`setAttr "+$text_obj+"."+$attr_name+" "+$subdivs+"`)");
	}
}

''')