//Maya ASCII 2013ff10 scene
//Name: phx_pool.ma
//Last modified: Tue, Jul 02, 2013 01:52:59 PM
//Codeset: 1251
requires maya "2013ff10";
requires "vrayformaya" "3.05.01";
requires "phoenixfd" "2.1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2013";
fileInfo "version" "2013 x64";
fileInfo "cutIdentifier" "201209140124-844721";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -2.7646232208582071 5.1558504845264661 5.9904341559436336 ;
	setAttr ".r" -type "double3" -27.33835273895393 -743.79999999967413 0 ;
	setAttr ".rp" -type "double3" 0 -4.4408920985006262e-016 -1.7763568394002505e-015 ;
	setAttr ".rpt" -type "double3" 1.468804094820204e-015 -1.5618377773402925e-015 -4.7634171006917615e-016 ;
createNode camera -s -n "perspShape" -p "persp";
	addAttr -ci true -sn "vrayCameraPhysicalOn" -ln "vrayCameraPhysicalOn" -at "long";
	addAttr -ci true -sn "vrayCameraPhysicalType" -ln "vrayCameraPhysicalType" -at "long";
	addAttr -ci true -sn "vrayCameraPhysicalFilmWidth" -ln "vrayCameraPhysicalFilmWidth" 
		-dv 36 -min 0 -smx 135 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalFocalLength" -ln "vrayCameraPhysicalFocalLength" 
		-dv 40 -min 0 -smx 100 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalSpecifyFOV" -ln "vrayCameraPhysicalSpecifyFOV" 
		-dv 2 -at "long";
	addAttr -ci true -sn "vrayCameraPhysicalFOV" -ln "vrayCameraPhysicalFOV" -dv 90 
		-min 9.9999997473787516e-005 -smx 180 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalZoomFactor" -ln "vrayCameraPhysicalZoomFactor" 
		-dv 1 -min 0 -smx 10 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalDistortionType" -ln "vrayCameraPhysicalDistortionType" 
		-at "long";
	addAttr -ci true -sn "vrayCameraPhysicalDistortion" -ln "vrayCameraPhysicalDistortion" 
		-min -1 -smx 1 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalLensFile" -ln "vrayCameraPhysicalLensFile" 
		-dt "string";
	addAttr -ci true -uac -sn "vrayCameraPhysicalDistortionMap" -ln "vrayCameraPhysicalDistortionMap" 
		-at "float3" -nc 3;
	addAttr -ci true -sn "vrayCameraPhysicalDistortionMapr" -ln "vrayCameraPhysicalDistortionMapR" 
		-dv 1 -at "float" -p "vrayCameraPhysicalDistortionMap";
	addAttr -ci true -sn "vrayCameraPhysicalDistortionMapg" -ln "vrayCameraPhysicalDistortionMapG" 
		-dv 1 -at "float" -p "vrayCameraPhysicalDistortionMap";
	addAttr -ci true -sn "vrayCameraPhysicalDistortionMapb" -ln "vrayCameraPhysicalDistortionMapB" 
		-dv 1 -at "float" -p "vrayCameraPhysicalDistortionMap";
	addAttr -ci true -sn "vrayCameraPhysicalFNumber" -ln "vrayCameraPhysicalFNumber" 
		-dv 8 -min 0 -smx 32 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalLensShift" -ln "vrayCameraPhysicalLensShift" 
		-min -100 -smx 100 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalShutterSpeed" -ln "vrayCameraPhysicalShutterSpeed" 
		-dv 200 -min 0 -smx 1000 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalShutterAngle" -ln "vrayCameraPhysicalShutterAngle" 
		-dv 180 -min 0 -max 360 -smn 0 -smx 360 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalShutterOffset" -ln "vrayCameraPhysicalShutterOffset" 
		-min -360 -max 360 -smn 0 -smx 360 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalLatency" -ln "vrayCameraPhysicalLatency" 
		-min 0 -smx 10 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalISO" -ln "vrayCameraPhysicalISO" -dv 100 
		-min 0 -smx 400 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalSpecifyFocus" -ln "vrayCameraPhysicalSpecifyFocus" 
		-at "long";
	addAttr -ci true -sn "vrayCameraPhysicalFocusDistance" -ln "vrayCameraPhysicalFocusDistance" 
		-dv 200 -min 0.0099999997764825821 -smx 400 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalExposure" -ln "vrayCameraPhysicalExposure" 
		-dv 1 -at "long";
	addAttr -ci true -uac -sn "vrayCameraPhysicalWhiteBalance" -ln "vrayCameraPhysicalWhiteBalance" 
		-at "float3" -nc 3;
	addAttr -ci true -sn "vrayCameraPhysicalWhiteBalancer" -ln "vrayCameraPhysicalWhiteBalanceR" 
		-dv 1 -at "float" -p "vrayCameraPhysicalWhiteBalance";
	addAttr -ci true -sn "vrayCameraPhysicalWhiteBalanceg" -ln "vrayCameraPhysicalWhiteBalanceG" 
		-dv 1 -at "float" -p "vrayCameraPhysicalWhiteBalance";
	addAttr -ci true -sn "vrayCameraPhysicalWhiteBalanceb" -ln "vrayCameraPhysicalWhiteBalanceB" 
		-dv 1 -at "float" -p "vrayCameraPhysicalWhiteBalance";
	addAttr -ci true -sn "vrayCameraPhysicalVignetting" -ln "vrayCameraPhysicalVignetting" 
		-dv 1 -at "long";
	addAttr -ci true -sn "vrayCameraPhysicalVignettingAmount" -ln "vrayCameraPhysicalVignettingAmount" 
		-dv 1 -min 0 -smx 1 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalBladesEnable" -ln "vrayCameraPhysicalBladesEnable" 
		-at "long";
	addAttr -ci true -sn "vrayCameraPhysicalBladesNum" -ln "vrayCameraPhysicalBladesNum" 
		-dv 5 -min 0 -smx 16 -at "long";
	addAttr -ci true -sn "vrayCameraPhysicalBladesRotation" -ln "vrayCameraPhysicalBladesRotation" 
		-min 0 -smx 6.2800002098083496 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalCenterBias" -ln "vrayCameraPhysicalCenterBias" 
		-min -10 -smx 10 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalAnisotropy" -ln "vrayCameraPhysicalAnisotropy" 
		-min -1 -smx 1 -at "float";
	addAttr -ci true -sn "vrayCameraPhysicalUseDof" -ln "vrayCameraPhysicalUseDof" -at "long";
	addAttr -ci true -sn "vrayCameraPhysicalUseMoBlur" -ln "vrayCameraPhysicalUseMoBlur" 
		-at "long";
	addAttr -ci true -sn "vrayCameraPhysicalSubdivs" -ln "vrayCameraPhysicalSubdivs" 
		-dv 6 -min 1 -smx 32 -at "long";
	setAttr -k off ".v" no;
	setAttr ".fl" 25.70664979741208;
	setAttr ".coi" 7.7737980579598691;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".dr" yes;
	setAttr ".vrayCameraPhysicalOn" 1;
	setAttr ".vrayCameraPhysicalType" 1;
	setAttr ".vrayCameraPhysicalFocalLength" 19.318265914916992;
	setAttr ".vrayCameraPhysicalFOV" 70.000022888183594;
	setAttr ".vrayCameraPhysicalLensFile" -type "string" "";
	setAttr ".vrayCameraPhysicalISO" 30;
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.1719565530906315 100.1 -0.33028597457582398 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 44.171309346904287;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 23.77701989704412;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 2.1541354320262665 -0.064105324749960252 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 55.112060544389315;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "PhoenixFDSim1";
createNode PhoenixFDSimulator -n "PhoenixFDSimulator1" -p "PhoenixFDSim1";
	setAttr ".cch" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".isc" no;
	setAttr ".bbx" no;
	setAttr ".icn" -type "string" "";
	setAttr ".vwm" 2;
	setAttr ".tpv" 0;
	setAttr ".uit" 0;
	setAttr -k off ".v" yes;
	setAttr ".io" no;
	setAttr ".tmp" no;
	setAttr ".gh" no;
	setAttr ".obcc" -type "float3" 0 0 0 ;
	setAttr ".uoc" no;
	setAttr ".oc" 0;
	setAttr ".ovdt" 0;
	setAttr ".ovlod" 0;
	setAttr ".ovs" yes;
	setAttr ".ovt" yes;
	setAttr ".ovp" yes;
	setAttr ".ove" no;
	setAttr ".ovv" yes;
	setAttr ".ovc" 0;
	setAttr ".lodv" yes;
	setAttr ".rlid" 0;
	setAttr ".rndr" yes;
	setAttr ".lovc" 0;
	setAttr ".gc" 0;
	setAttr ".gpr" 3;
	setAttr ".gps" 3;
	setAttr ".gss" 1;
	setAttr ".gap" 1;
	setAttr ".gcp" -type "float3" 0.447 1 1 ;
	setAttr ".gla" 1;
	setAttr ".gac" -type "float3" 0.87800002 0.67799997 0.66299999 ;
	setAttr ".grs" 0;
	setAttr ".gre" 125;
	setAttr ".rt" 0;
	setAttr ".rv" no;
	setAttr ".vf" 1;
	setAttr ".mb" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".csh" yes;
	setAttr ".rcsh" yes;
	setAttr ".vbo" no;
	setAttr ".mvs" 1;
	setAttr ".gao" no;
	setAttr ".gal" 1;
	setAttr ".sso" no;
	setAttr ".ssa" 1;
	setAttr ".msa" 1;
	setAttr ".vso" no;
	setAttr ".vss" 1;
	setAttr ".dej" no;
	setAttr ".iss" no;
	setAttr ".vis" yes;
	setAttr ".tw" no;
	setAttr ".rtw" yes;
	setAttr ".pv" -type "double2" 0 0 ;
	setAttr ".di" no;
	setAttr ".dcol" no;
	setAttr ".dcc" -type "string" "color";
	setAttr ".ih" no;
	setAttr ".ds" yes;
	setAttr ".op" no;
	setAttr ".smo" yes;
	setAttr ".bbs" -type "float3" 1.5 1.5 1.5 ;
	setAttr ".fbda" yes;
	setAttr ".dsr" 6;
	setAttr ".xsr" 5;
	setAttr ".fth" 0;
	setAttr ".nat" 30;
	setAttr ".dhe" no;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ver" 3;
	setAttr ".ct" 83;
	setAttr ".ui" 3;
	setAttr ".tl" 0;
	setAttr ".nsys0" -1;
	setAttr ".nsys1" -1;
	setAttr ".ssf" yes;
	setAttr ".saf" 0;
	setAttr ".sof" 0;
	setAttr ".usc" no;
	setAttr ".scf" -type "string" "";
	setAttr ".objvox" 0;
	setAttr ".objvel" 0;
	setAttr ".fcal" 0;
	setAttr ".fsk" 0;
	setAttr ".fmt" no;
	setAttr ".cm" 1;
	setAttr ".cfl" 0;
	setAttr ".cfi" 0;
	setAttr ".cq" 40;
	setAttr ".cun" no;
	setAttr ".adm" 0;
	setAttr ".ams" 1000;
	setAttr ".spf1" 2;
	setAttr ".spf2" 2;
	setAttr ".as" no;
	setAttr ".dc" no;
	setAttr ".rs" no;
	setAttr ".rswm" no;
	setAttr ".rscq" 2;
	setAttr ".rsi" -type "string" "$(simoutput)";
	setAttr ".rsor" -type "string" "D:\\PhoenixFD_cache\\phx_pool.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1_resim";
	setAttr ".rsir" -type "string" "D:\\PhoenixFD_cache\\phx_pool.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1";
	setAttr ".rso" -type "string" "$(implicit)";
	setAttr ".rsaf" 1;
	setAttr ".rstc" 0;
	setAttr ".rsa" 1;
	setAttr ".rsam" 0;
	setAttr ".wvs" 3;
	setAttr ".wvc" 0.0010000000474974513;
	setAttr ".lgr" yes;
	setAttr ".mun" 4;
	setAttr ".uns" 1;
	setAttr ".csz" 0.03;
	setAttr ".xsz" 230;
	setAttr ".ysz" 230;
	setAttr ".zsz" 100;
	setAttr ".bx" 0;
	setAttr ".by" 0;
	setAttr ".bz" 0;
	setAttr ".gpa" 1;
	setAttr ".ag" 0;
	setAttr ".gt" 0.0099999997764825821;
	setAttr ".lby" 2;
	setAttr ".lto" 5;
	setAttr ".nbig" yes;
	setAttr ".am" 0;
	setAttr ".ale" no;
	setAttr ".alxp" 0;
	setAttr ".alxn" 0;
	setAttr ".alyp" 0;
	setAttr ".alyn" 0;
	setAttr ".alzp" 0;
	setAttr ".alzn" 0;
	setAttr ".acam" -type "string" "";
	setAttr ".wfmv" 1;
	setAttr ".wfm" no;
	setAttr ".egr" yes;
	setAttr ".gr" 1;
	setAttr ".egrv" no;
	setAttr ".grv" -type "float3" 0 -9.8000002 0 ;
	setAttr ".tsc" 1;
	setAttr ".vrt" 0;
	setAttr ".vmv" no;
	setAttr ".pd" 0;
	setAttr ".cool" 0;
	setAttr ".sb" 0;
	setAttr ".fb" 0;
	setAttr ".fmm" 0;
	setAttr ".ra" 0;
	setAttr ".rd" 1;
	setAttr ".rij" no;
	setAttr ".brn" no;
	setAttr ".be" 10;
	setAttr ".big" 600;
	setAttr ".bp" 10;
	setAttr ".liq" yes;
	setAttr ".lqsteps" 1;
	setAttr ".lqsharpness" 0.5;
	setAttr ".lqad" 0;
	setAttr ".lqsurft" 0;
	setAttr ".lqvisc" 0;
	setAttr ".drying" 0.0099999997764825821;
	setAttr ".flevel" 60;
	setAttr ".initfill" yes;
	setAttr ".wetting" no;
	setAttr ".flatliquids" yes;
	setAttr ".strongsurf" no;
	setAttr ".foam" yes;
	setAttr ".fbirth" 20;
	setAttr ".fbthres" 40;
	setAttr ".fhlf" 0.5;
	setAttr ".foutlife" 5;
	setAttr ".fsize" 0.004999999888241291;
	setAttr ".fsizevar" 2;
	setAttr ".fszdstrb" 25;
	setAttr ".fcycles" 0;
	setAttr ".frise" 1;
	setAttr ".ffall" 50;
	setAttr ".fsticky" 0;
	setAttr ".fptrn" 5;
	setAttr ".fptrnsz" 10;
	setAttr ".splashes" yes;
	setAttr ".spbirth" 3000;
	setAttr ".spbthres" 20;
	setAttr ".spsize" 0.004999999888241291;
	setAttr ".spsizevar" 2;
	setAttr ".spszdstrb" 100;
	setAttr ".airfr" 2;
	setAttr ".sp2foam" 0.5;
	setAttr ".sp2liquid" no;
	setAttr ".spto" 3;
	setAttr ".vmult" 1;
	setAttr ".spsplit" 1;
	setAttr ".sq" 14;
	setAttr ".bi" 1;
	setAttr ".ci" no;
	setAttr ".ot" yes;
	setAttr ".osm" yes;
	setAttr ".ou" no;
	setAttr ".ow" no;
	setAttr ".osp" no;
	setAttr ".ov" yes;
	setAttr ".of" no;
	setAttr ".opi" no;
	setAttr ".opth" -type "string" "$(implicit)";
	setAttr ".opthr" -type "string" "D:\\PhoenixFD_cache\\phx_pool.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1";
	setAttr ".uset2f" no;
	setAttr ".t2f" 1;
	setAttr ".iro" 0;
	setAttr ".iml" 0;
	setAttr ".ipa" 0;
	setAttr ".play_speed" 1;
	setAttr ".ibm" 0;
	setAttr ".ipth" -type "string" "$(simoutput)";
	setAttr ".ipthr" -type "string" "D:\\PhoenixFD_cache\\phx_pool.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1";
	setAttr ".ifyz" no;
	setAttr ".its" -type "float3" 0 0.5 0.1 ;
	setAttr ".itse" no;
	setAttr ".isms" -type "float3" 0 0.5 0.1 ;
	setAttr ".isse" no;
	setAttr ".iws" -type "float3" 0 0.5 0.1 ;
	setAttr ".iwse" no;
	setAttr ".ifs" -type "float3" 0 0.5 0.1 ;
	setAttr ".ifse" no;
	setAttr ".iel" yes;
	setAttr ".ieh" no;
	setAttr ".sg" yes;
	setAttr ".sgs" no;
	setAttr ".cr" 15.436241149902344;
	setAttr ".ois" no;
	setAttr ".avo" yes;
	setAttr ".andr" no;
	setAttr ".vt" yes;
	setAttr ".vtn" no;
	setAttr ".vtc" -type "float3" 0 0 0.5 ;
	setAttr ".vtc2" -type "float3" 0 0 1.001 ;
	setAttr ".vtt" 0.5;
	setAttr ".vtt2" 0.99000000953674316;
	setAttr ".vs" no;
	setAttr ".vsc" -type "float3" 0.5 0.5 0.5 ;
	setAttr ".vsc2" -type "float3" 0 0 0 ;
	setAttr ".vst" 0.0099999997764825821;
	setAttr ".vst2" 1;
	setAttr ".vu" no;
	setAttr ".vur" yes;
	setAttr ".vuc" -type "float3" 0.44999999 0.55000001 0.44999999 ;
	setAttr ".vuc2" -type "float3" 0 0.5 0 ;
	setAttr ".vut" 1;
	setAttr ".vut2" 1000;
	setAttr ".vw" no;
	setAttr ".vwc" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".vwc2" -type "float3" 0.89999998 0.89999998 0 ;
	setAttr ".vwt" 0.0099999997764825821;
	setAttr ".vwt2" 1000;
	setAttr ".vfu" no;
	setAttr ".vfc" -type "float3" 0.44999999 0.55000001 0.55000001 ;
	setAttr ".vfc2" -type "float3" 0 0.5 0.5 ;
	setAttr ".vft" 0.0099999997764825821;
	setAttr ".vft2" 1;
	setAttr ".vv" no;
	setAttr ".vvc" -type "float3" 0.44999999 0.44999999 0.44999999 ;
	setAttr ".vvc2" -type "float3" 0 0 0.5 ;
	setAttr ".vvt" 10;
	setAttr ".vvt2" 100;
	setAttr ".vfoc" -type "float3" 1 1 1 ;
	setAttr ".vfoce" yes;
	setAttr ".vspc" -type "float3" 0 0 0.37099999 ;
	setAttr ".vspce" yes;
	setAttr ".vprtc" -type "float3" 1 0 0 ;
	setAttr ".vprtce" yes;
	setAttr ".vprts" 1;
	setAttr ".gve" no;
	setAttr ".gvd" 1;
	setAttr ".gvl" yes;
	setAttr ".gvml" 1;
	setAttr ".gva" -type "float3" 0 0 0 ;
	setAttr ".gvs" 50;
	setAttr ".gvse" no;
	setAttr ".gvb" yes;
	setAttr ".gvbg" -type "float3" 0 0 0 ;
	setAttr ".gvst" no;
	setAttr ".gvp" -type "string" "$(implicit)";
	setAttr ".gvss" no;
	setAttr ".gvm" no;
	setAttr ".gif" 0;
	setAttr ".vm" yes;
	setAttr ".vmd" no;
	setAttr ".vmc" -type "float3" 0.22 0.22 0.94999999 ;
	setAttr ".vma" 0.80000001192092896;
	setAttr ".vmas" no;
	setAttr ".rsl_x" 0.5;
	setAttr ".rsl_t" 0.5;
	setAttr ".rsl_s" 0.5;
	setAttr ".rsl_v" 20;
	setAttr ".rsl_f" 0.10000000149011612;
	setAttr ".rend" yes;
	setAttr ".jitter" yes;
	setAttr ".rendstep" 50;
	setAttr ".softb" 0;
	setAttr ".rvmult" 1;
	setAttr ".sampler" 2;
	setAttr ".sarg" 1;
	setAttr ".ret" -type "float3" 0 0 0 ;
	setAttr ".solidbelow" no;
	setAttr ".geommode" no;
	setAttr ".heathaze" 1;
	setAttr ".rendsolid" no;
	setAttr ".rendMode" 4;
	setAttr ".bias" 1;
	setAttr ".usebias" yes;
	setAttr ".uvwmb" no;
	setAttr ".wrapx" 2;
	setAttr ".wrapy" 2;
	setAttr ".wrapz" 2;
	setAttr ".oceanlevel" 60;
	setAttr ".ocean" yes;
	setAttr ".smoothmesh" 3;
	setAttr ".meshsubdiv" 2;
	setAttr ".displacement" yes;
	setAttr ".displmul" 1;
	setAttr ".displ2d" 2;
	setAttr ".displ0" -type "float3" 0 0 0 ;
	setAttr ".displ1" -type "float3" 0 0 0 ;
	setAttr ".displ2" -type "float3" 0 0 0 ;
	setAttr ".mid" -type "float3" 0 0 0 ;
	setAttr ".vn" 0;
	setAttr ".vz" 0;
	setAttr ".usegizmo" no;
	setAttr ".invgizmo" no;
	setAttr ".earg" 0;
	setAttr ".et" -type "float3" 0 0 0 ;
	setAttr ".em" no;
	setAttr ".no_alpha_e" no;
	setAttr ".elc" 0;
	setAttr ".elce" yes;
	setAttr ".elpm" 1;
	setAttr ".elrm" 1;
	setAttr ".elp" no;
	setAttr ".elss" no;
	setAttr ".elpl" 0;
	setAttr ".els" 0;
	setAttr ".elsd" 8;
	setAttr ".elcsd" 1000;
	setAttr ".elco" 0.0099999997764825821;
	setAttr ".erl_t" 900;
	setAttr ".ero_t" 1100;
	setAttr ".erm_t" 483977;
	setAttr ".erl_s" 0.44999998807907104;
	setAttr ".ero_s" 0.55000001192092896;
	setAttr ".erm_s" 483977;
	setAttr ".erl_v" 180;
	setAttr ".ero_v" 220;
	setAttr ".erm_v" 483977;
	setAttr ".erl_f" 0.44999998807907104;
	setAttr ".ero_f" 0.55000001192092896;
	setAttr ".erm_f" 483977;
	setAttr ".darg" 6;
	setAttr ".dt" -type "float3" 0 0 1 ;
	setAttr ".dm" no;
	setAttr ".simple_color" -type "float3" 0.1 0.40000001 0.69999999 ;
	setAttr ".pmbounces" yes;
	setAttr ".lightcache" yes;
	setAttr ".lightcachesr" 0;
	setAttr ".noscatter" 2;
	setAttr ".dsd" 10;
	setAttr ".difmul" 1;
	setAttr ".drl_t" 4000;
	setAttr ".dro_t" 0;
	setAttr ".drl_s" 1;
	setAttr ".dro_s" 0;
	setAttr ".drl_v" 400;
	setAttr ".dro_v" 0;
	setAttr ".drl_f" 1;
	setAttr ".dro_f" 0;
	setAttr ".targ" 1;
	setAttr ".tt" -type "float3" 0 0 0 ;
	setAttr ".tm" no;
	setAttr ".transpmode" 1;
	setAttr ".stoptransp" 0.99000000953674316;
	setAttr ".skiptransp" 0.0010000000474974513;
	setAttr ".smoketransp" 0.5;
	setAttr ".trl_t" 1;
	setAttr ".tro_t" 0;
	setAttr ".trm_t" 0.25;
	setAttr ".trl_s" 0.80000001192092896;
	setAttr ".tro_s" 0.14000000059604645;
	setAttr ".trm_s" 0.10000000149011612;
	setAttr ".trl_v" 510;
	setAttr ".tro_v" 90;
	setAttr ".trm_v" 0.10000000149011612;
	setAttr ".trl_f" 0.80000001192092896;
	setAttr ".tro_f" 0.14000000059604645;
	setAttr ".trm_f" 0.10000000149011612;
	setAttr -s 2 ".ecolor_t";
	setAttr ".ecolor_t[0].ecolor_tp" 1100;
	setAttr ".ecolor_t[0].ecolor_tc" -type "float3" 1 0.1971141 0.0011649206 ;
	setAttr ".ecolor_t[0].ecolor_ti" 3;
	setAttr ".ecolor_t[1].ecolor_tp" 2000.0010986328125;
	setAttr ".ecolor_t[1].ecolor_tc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_t[1].ecolor_ti" 3;
	setAttr -s 2 ".ecolor_s";
	setAttr ".ecolor_s[0].ecolor_sp" 0.55000001192092896;
	setAttr ".ecolor_s[0].ecolor_sc" -type "float3" 1 0.1971141 0.0011649206 ;
	setAttr ".ecolor_s[0].ecolor_si" 3;
	setAttr ".ecolor_s[1].ecolor_sp" 1.0000004768371582;
	setAttr ".ecolor_s[1].ecolor_sc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_s[1].ecolor_si" 3;
	setAttr -s 2 ".ecolor_v";
	setAttr ".ecolor_v[0].ecolor_vp" 220;
	setAttr ".ecolor_v[0].ecolor_vc" -type "float3" 1 0.1971141 0.0011649206 ;
	setAttr ".ecolor_v[0].ecolor_vi" 3;
	setAttr ".ecolor_v[1].ecolor_vp" 400.00021362304687;
	setAttr ".ecolor_v[1].ecolor_vc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_v[1].ecolor_vi" 3;
	setAttr -s 2 ".ecolor_f";
	setAttr ".ecolor_f[0].ecolor_fp" 0.55000001192092896;
	setAttr ".ecolor_f[0].ecolor_fc" -type "float3" 1 0.1971141 0.0011649206 ;
	setAttr ".ecolor_f[0].ecolor_fi" 3;
	setAttr ".ecolor_f[1].ecolor_fp" 1.0000004768371582;
	setAttr ".ecolor_f[1].ecolor_fc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_f[1].ecolor_fi" 3;
	setAttr ".dcolor_t[0].dcolor_tp" 0;
	setAttr ".dcolor_t[0].dcolor_tc" -type "float3" 1 1 1 ;
	setAttr ".dcolor_t[0].dcolor_ti" 3;
	setAttr ".dcolor_s[0].dcolor_sp" 0;
	setAttr ".dcolor_s[0].dcolor_sc" -type "float3" 1 1 1 ;
	setAttr ".dcolor_s[0].dcolor_si" 3;
	setAttr ".dcolor_v[0].dcolor_vp" 0;
	setAttr ".dcolor_v[0].dcolor_vc" -type "float3" 1 1 1 ;
	setAttr ".dcolor_v[0].dcolor_vi" 3;
	setAttr ".dcolor_f[0].dcolor_fp" 0;
	setAttr ".dcolor_f[0].dcolor_fc" -type "float3" 1 1 1 ;
	setAttr ".dcolor_f[0].dcolor_fi" 3;
	setAttr -s 14 ".epower_t[0:13]"  1100 25.51508522 3 1161.43823242
		 79.3817749 3 1226.30786133 233.79096985 3 1294.80078125 653.46130371 3 1367.11901855
		 1737.57226563 3 1443.4765625 4405.52978516 3 1524.098999023 10674.27929688 
		3 1609.22424316 24767.060546875 3 1699.10412598 55141.3125 3 1794.00390625
		 118026.09375 3 1894.2043457 243318.328125 3 2000.0010986328 483980.15625 3
		 1974.28686523 412181.71875 3 1995.50109863 470704.9375 3;
	setAttr -s 14 ".epower_s[0:13]"  0.55000001 25.51508522 3 0.58071911
		 79.3817749 3 0.61315393 233.79096985 3 0.64740038 653.46130371 3 0.68355954
		 1737.57226563 3 0.72173828 4405.52978516 3 0.7620495 10674.27929688 3 0.80461216
		 24767.060546875 3 0.84955204 55141.3125 3 0.89700198 118026.09375 3 0.94710219
		 243318.328125 3 1.000000476837 483980.15625 3 0.9871434 412181.71875 3 0.99775052
		 470704.9375 3;
	setAttr -s 14 ".epower_v[0:13]"  220 25.51508522 3 232.28764343 79.3817749 
		3 245.26156616 233.79096985 3 258.96014404 653.46130371 3 273.42379761 1737.57226563 
		3 288.6953125 4405.52978516 3 304.8197937 10674.27929688 3 321.84484863 24767.060546875 
		3 339.8208313 55141.3125 3 358.80078125 118026.09375 3 378.84088135 243318.328125 
		3 400.00021362305 483980.15625 3 394.85736084 412181.71875 3 399.10021973
		 470704.9375 3;
	setAttr -s 14 ".epower_f[0:13]"  0.55000001 25.51508522 3 0.58071911
		 79.3817749 3 0.61315393 233.79096985 3 0.64740038 653.46130371 3 0.68355954
		 1737.57226563 3 0.72173828 4405.52978516 3 0.7620495 10674.27929688 3 0.80461216
		 24767.060546875 3 0.84955204 55141.3125 3 0.89700198 118026.09375 3 0.94710219
		 243318.328125 3 1.000000476837 483980.15625 3 0.9871434 412181.71875 3 0.99775052
		 470704.9375 3;
	setAttr -s 3 ".tpower_t[0:2]"  0 0 0 0.20000002 0 1 0.40000001
		 0.25 0;
	setAttr -s 9 ".tpower_s[0:8]"  0.14 0 3 0.43599999 0.025 3 0.50319999
		 0.054000001 3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 3 0.74000001
		 0 3 0.81999999 0.050000001 3 0.94 0 3;
	setAttr -s 9 ".tpower_v[0:8]"  90 0 3 278.70001221 0.025 3 321.53997803
		 0.054000001 3 331.73999023 0.1 3 332.25 0.1 1 343.7250061 0 3 472.5 0 
		3 523.5 0.050000001 3 600 0 3;
	setAttr -s 9 ".tpower_f[0:8]"  0.14 0 3 0.43599999 0.025 3 0.50319999
		 0.054000001 3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 3 0.74000001
		 0 3 0.81999999 0.050000001 3 0.94 0 3;
createNode transform -n "pSphere1";
createNode mesh -n "pSphereShape1" -p "pSphere1";
	addAttr -ci true -sn "mso" -ln "miShadingSamplesOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "msh" -ln "miShadingSamples" -min 0 -smx 8 -at "float";
	addAttr -ci true -sn "mdo" -ln "miMaxDisplaceOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "mmd" -ln "miMaxDisplace" -min 0 -smx 1 -at "float";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
	setAttr ".vnm" 0;
createNode transform -s -n "vrayEnvironmentPreviewTm";
createNode VRayEnvironmentPreview -s -n "vrayEnvironmentPreview" -p "vrayEnvironmentPreviewTm";
	setAttr -k off ".v";
createNode transform -n "PhoenixFDFm1";
	setAttr ".t" -type "double3" 3.9724501152519713 0 2.0715579372247377 ;
	setAttr ".s" -type "double3" 1.5 1.5 1.5 ;
createNode PhoenixFDFoam -n "PhoenixFDFoam1" -p "PhoenixFDFm1";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".hlw" 0.10000000149011612;
	setAttr ".hlm" 0;
	setAttr ".sct" 1;
	setAttr ".mod" 0;
	setAttr ".mob" 2;
	setAttr ".eme" yes;
	setAttr ".pmprimary" yes;
	setAttr ".aal" -type "attributeAlias" {"rendGizmo","gizmo"} ;
createNode transform -n "PhoenixFDFm2";
	setAttr ".t" -type "double3" 3.8483118038908506 0 -0.28132781366428761 ;
	setAttr ".s" -type "double3" 1.2999999523162842 1.2999999523162842 1.2999999523162842 ;
createNode PhoenixFDFoam -n "PhoenixFDFoam2" -p "PhoenixFDFm2";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".col" -type "float3" 0.49352255 0.55568779 0.61005569 ;
	setAttr ".sct" 1;
	setAttr ".mod" 2;
	setAttr ".mob" 1;
	setAttr ".eme" yes;
	setAttr ".pmprimary" yes;
	setAttr ".lc" -type "float3" 0 0 1 ;
	setAttr ".aal" -type "attributeAlias" {"rendGizmo","gizmo"} ;
createNode transform -n "transform5";
	setAttr ".t" -type "double3" -0.86945190778455173 0.55286127239561789 1.9404922253898935 ;
createNode VRaySunTarget -n "VRaySunTarget1" -p "transform5";
	setAttr -k off ".v";
createNode VRayGeoSun -n "VRayGeoSun1" -p "transform5";
	setAttr ".t" -type "double3" -9.8452770894262898 8.6088576366209448 7.6259632335648879 ;
	setAttr ".gyear" 2011;
	setAttr ".gmonth" 10;
	setAttr ".gday" 5;
	setAttr ".gdvalue" 278;
	setAttr ".gtvalue" 12;
createNode VRaySunShape -n "VRaySunShape1" -p "VRayGeoSun1";
	setAttr -k off ".v";
	setAttr ".on" no;
	setAttr ".inv" yes;
	setAttr ".hillum" 50000;
	setAttr ".skymod" 1;
	setAttr ".subdivs" 3;
	setAttr ".shb" 0.0099999997764825821;
	setAttr ".photonRadius" 5.0561800003051758;
createNode place3dTexture -n "place3dTexture1";
createNode transform -n "pPlane1";
	setAttr ".t" -type "double3" 24.264637211101665 -10 -58.610833754702966 ;
createNode mesh -n "pPlaneShape1" -p "pPlane1";
	addAttr -ci true -sn "mso" -ln "miShadingSamplesOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "msh" -ln "miShadingSamples" -min 0 -smx 8 -at "float";
	addAttr -ci true -sn "mdo" -ln "miMaxDisplaceOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "mmd" -ln "miMaxDisplace" -min 0 -smx 1 -at "float";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vnm" 0;
createNode PhoenixFDPGroup -n "PG_PhoenixFDSimulator1_Foam_0";
	setAttr ".gn" -type "string" "Foam";
createNode PhoenixFDPGroup -n "PG_PhoenixFDSimulator1_Splashes_0";
	setAttr ".gn" -type "string" "Splashes";
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 4 ".lnk";
	setAttr -s 4 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode objectSet -n "phxsim_set1";
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n"
		+ "                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n"
		+ "            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n"
		+ "            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n"
		+ "                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n"
		+ "                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n"
		+ "                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n"
		+ "            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n"
		+ "            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n"
		+ "                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n"
		+ "                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n"
		+ "                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n"
		+ "            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n"
		+ "            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n"
		+ "                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n"
		+ "                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n"
		+ "                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -shadows 0\n                $editorName;\n            modelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n"
		+ "            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n"
		+ "            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n"
		+ "            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -shadows 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n                -showReferenceNodes 1\n                -showReferenceMembers 1\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n"
		+ "                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n"
		+ "                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n"
		+ "            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n"
		+ "            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n"
		+ "                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n"
		+ "                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n"
		+ "                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n"
		+ "                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n"
		+ "                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n"
		+ "                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n"
		+ "                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n"
		+ "                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n"
		+ "            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n"
		+ "                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n"
		+ "                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range -1 -1 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n"
		+ "                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range -1 -1 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n"
		+ "            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n"
		+ "                -ignoreAssets 1\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -island 0\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -syncedSelection 1\n                -extendToShapes 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"VFBPanelType\" (localizedPanelLabel(\"V-Ray Frame Buffer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"VFBPanelType\" -l (localizedPanelLabel(\"V-Ray Frame Buffer\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"V-Ray Frame Buffer\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n"
		+ "                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n"
		+ "                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n"
		+ "                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -shadows 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n"
		+ "                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n"
		+ "                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -shadows 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 250 -ast 1 -aet 250 ";
	setAttr ".st" 6;
createNode polySphere -n "polySphere1";
	setAttr ".r" 0.24;
createNode animCurveTL -n "pSphere1_translateX";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1.25 2.96 20 -1.13;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
createNode animCurveTL -n "pSphere1_translateY";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1.25 3.29 20 0.32;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
createNode animCurveTL -n "pSphere1_translateZ";
	setAttr ".tan" 10;
	setAttr ".wgt" no;
	setAttr -s 2 ".ktv[0:1]"  1.25 -3.55 20 0.64;
	setAttr -s 2 ".kit[1]"  18;
	setAttr -s 2 ".kot[1]"  18;
createNode VRaySettingsNode -s -n "vraySettings";
	setAttr ".cmph" 60;
	setAttr ".csd" 0.5;
	setAttr ".cmd" 0.0099999997764825821;
	setAttr ".aafon" no;
	setAttr ".dma" 5;
	setAttr ".imcp" 1;
	setAttr ".iminr" -4;
	setAttr ".imaxr" -3;
	setAttr ".icts" 0.4;
	setAttr ".ints" 0.3;
	setAttr ".impass" no;
	setAttr ".cmco" yes;
	setAttr ".cmsm" yes;
	setAttr ".catype" 8;
	setAttr ".cafov" 50;
	setAttr ".caoet" yes;
	setAttr ".cavte" yes;
	setAttr ".cammb" no;
	setAttr ".vrscfile" -type "string" "C:/pgroup.vrscene";
	setAttr ".micv" no;
	setAttr ".srgx" 32;
	setAttr ".srgy" 32;
	setAttr ".sltp" yes;
	setAttr ".wi" 1280;
	setAttr ".he" 720;
	setAttr ".aspr" 1.7777777910232544;
	setAttr ".aspl" no;
	setAttr ".fnprx" -type "string" "D:\\pool\\pool";
	setAttr ".animbo" yes;
	setAttr ".noa" yes;
	setAttr ".pxa" 0.99956250190734863;
	setAttr ".bkc" -type "string" "map1";
	setAttr ".vfbOn" yes;
	setAttr ".vfbSA" -type "Int32Array" 198 786 10 -2 -2 1337 793
		 1584 145 10 145 50497 1 60 145 0 162 113 449
		 290 63 706 1 1 1 0 0 0 0 1 0
		 5 0 1065353216 1 1 2 1065353216 1065353216 1065353216 1065353216 1 0
		 5 0 0 0 0 1 0 5 0 1065353216 1 137531
		 65536 1 1313131313 65536 944879383 0 -525502228 1065353216 1621981420 1034147594 1053609164 1065353216
		 2 0 0 -1097805629 -1097805629 1049678019 1049678019 0 2 1065353216 1065353216 -1097805629
		 -1097805629 1049678019 1049678019 0 2 1 2 8 4 0 0 1394627405
		 1819043176 1735148576 12832 840436920 0 840422664 0 840408408 0 840403744 0 840403832
		 0 840403568 0 840403392 0 840403216 0 840403040 0 840402776 0 840402512
		 16777215 0 70 1 32 53 1632775510 1868963961 1632444530 622879097 2036429430 1936876918
		 544108393 1701978236 1919247470 1835627552 1915035749 1701080677 1835627634 12901 1378702848 1713404257 1293972079 543258977
		 892350003 540094510 1701978236 1919247470 1835627552 807411813 807411816 942940269 7550254 16777216 16777216 0
		 0 0 0 1 1 0 0 0 0 11 1936614732 1701209669
		 7566435 1 0 1 0 1101004800 1101004800 1082130432 0 0 0 1077936128
		 0 0 0 1 0 0 1112014848 1101004800 1 0 0 0
		 0 82176 0 16576 0 0 0 0 16448 0 65536 65536 ;
	setAttr ".stampOn" yes;
	setAttr ".mSceneName" -type "string" "C:/source/svn/Aura2/Maya/samples/phx_pool.ma";
createNode VRayMtl -n "vraymtl_water:VRayMtl1";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".dc" -type "float3" 0 0 0 ;
	setAttr ".rlc" -type "float3" 1 1 1 ;
	setAttr ".rlec" -type "float3" 1 1 1 ;
	setAttr ".hlgl" no;
	setAttr ".uf" yes;
	setAttr ".rbs" yes;
	setAttr ".rrc" -type "float3" 1 1 1 ;
	setAttr ".rior" 1.3300000429153442;
	setAttr ".fc" -type "float3" 0.81960785 0.96862745 0.94509804 ;
	setAttr ".fmu" 10;
	setAttr ".afs" yes;
	setAttr ".aal" -type "attributeAlias" {"color","diffuseColor","transparency","opacityMap"
		} ;
createNode shadingEngine -n "vraymtl_water:VRayMtl1SG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
createNode objectSet -n "phxfoam_set1";
createNode objectSet -n "phxfoam_set2";
createNode VRaySky -n "VRaySky1";
createNode remapHsv -n "remapHsv1";
	setAttr -s 2 ".h[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".s[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".v[0:1]"  0 0 1 1 1 1;
createNode PhoenixFDOceanTexture -n "PhoenixFDOceanTexture1";
	addAttr -ci true -h true -sn "vpi" -ln "vrayPluginInfo" -dv 3.545946135838187e-315 
		-at "addr";
	setAttr ".lod" 15;
	setAttr ".vel" 0.20000000298023224;
	setAttr ".seed" 1073741824;
createNode polyPlane -n "polyPlane1";
	setAttr ".w" 100000;
	setAttr ".h" 100000;
	setAttr ".sw" 1;
	setAttr ".sh" 1;
	setAttr ".cuv" 2;
createNode lambert -n "lambert2";
	setAttr ".c" -type "float3" 0 0 0 ;
createNode shadingEngine -n "lambert2SG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 83;
	setAttr ".unw" 83;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 3 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :defaultTextureList1;
	setAttr -s 2 ".tx";
select -ne :lightList1;
	setAttr -s 2 ".l";
select -ne :lambert1;
	setAttr ".c" -type "float3" 0.7233997 0.7233997 0.7233997 ;
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 2 ".u";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr ".ren" -type "string" "vray";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -k on ".gama";
	setAttr ".an" yes;
	setAttr ".fs" 1;
	setAttr ".ef" 250;
	setAttr -k on ".be";
	setAttr -k on ".fec";
	setAttr -k on ".ofc";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -k on ".lpr";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -av -k on ".bll";
	setAttr -k on ".bls";
	setAttr -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
select -ne :defaultResolution;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -av ".w" 1280;
	setAttr -av ".h" 720;
	setAttr -av ".pa" 1;
	setAttr -k on ".al";
	setAttr -av ".dar" 1.7777777910232544;
	setAttr -k on ".off";
	setAttr -k on ".fld";
	setAttr -k on ".zsl";
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -s 2 ".dsm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :defaultObjectSet;
	setAttr ".ro" yes;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off ".eeaa";
	setAttr -k off ".engm";
	setAttr -k off ".mes";
	setAttr -k off ".emb";
	setAttr -av -k off ".mbbf";
	setAttr -k off ".mbs";
	setAttr -k off ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off ".twa";
	setAttr -k off ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
select -ne :hardwareRenderingGlobals;
	setAttr ".vac" 2;
select -ne :defaultHardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".rp";
	setAttr -k on ".cai";
	setAttr -k on ".coi";
	setAttr -cb on ".bc";
	setAttr -av -k on ".bcb";
	setAttr -av -k on ".bcg";
	setAttr -av -k on ".bcr";
	setAttr -k on ".ei";
	setAttr -k on ".ex";
	setAttr -av -k on ".es";
	setAttr -av -k on ".ef";
	setAttr -k on ".bf";
	setAttr -k on ".fii";
	setAttr -av -k on ".sf";
	setAttr -k on ".gr";
	setAttr -k on ".li";
	setAttr -k on ".ls";
	setAttr -k on ".mb";
	setAttr -k on ".ti";
	setAttr -k on ".txt";
	setAttr -k on ".mpr";
	setAttr -k on ".wzd";
	setAttr ".fn" -type "string" "im";
	setAttr -k on ".if";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
	setAttr -k on ".as";
	setAttr -k on ".ds";
	setAttr -k on ".lm";
	setAttr -k on ".fir";
	setAttr -k on ".aap";
	setAttr -k on ".gh";
	setAttr -cb on ".sd";
connectAttr "phxsim_set1.ub[0]" "PhoenixFDSimulator1.us";
connectAttr ":time1.o" "PhoenixFDSimulator1.ct";
connectAttr "PhoenixFDOceanTexture1.oc" "PhoenixFDSimulator1.displ2";
connectAttr "pSphere1_translateX.o" "pSphere1.tx";
connectAttr "pSphere1_translateY.o" "pSphere1.ty";
connectAttr "pSphere1_translateZ.o" "pSphere1.tz";
connectAttr "polySphere1.out" "pSphereShape1.i";
connectAttr ":vraySettings.caet1" ":vrayEnvironmentPreview.bgt";
connectAttr ":vraySettings.caet2" ":vrayEnvironmentPreview.git";
connectAttr ":vraySettings.caet3" ":vrayEnvironmentPreview.rflt";
connectAttr ":vraySettings.caet4" ":vrayEnvironmentPreview.rfrt";
connectAttr "phxfoam_set1.ub[0]" "PhoenixFDFoam1.pss";
connectAttr "PhoenixFDSimulator1.avo" "PhoenixFDFoam1.lg";
connectAttr "VRaySky1.oc" "PhoenixFDFoam1.em";
connectAttr "phxfoam_set2.ub[0]" "PhoenixFDFoam2.pss";
connectAttr "PhoenixFDSimulator1.us" "PhoenixFDFoam2.lg";
connectAttr "VRaySky1.oc" "PhoenixFDFoam2.em";
connectAttr "VRaySunTarget1.src" "VRaySunShape1.trg";
connectAttr "polyPlane1.out" "pPlaneShape1.i";
connectAttr "PhoenixFDSimulator1.idc" "PG_PhoenixFDSimulator1_Foam_0.sdc";
connectAttr "PhoenixFDSimulator1.idc" "PG_PhoenixFDSimulator1_Splashes_0.sdc";
relationship "link" ":lightLinker1" "vraymtl_water:VRayMtl1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "vraymtl_water:VRayMtl1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "VRaySky1.oc" ":vraySettings.caet1";
connectAttr "VRaySky1.oc" ":vraySettings.caet2";
connectAttr "VRaySky1.oc" ":vraySettings.caet3";
connectAttr "VRaySky1.oc" ":vraySettings.caet4";
connectAttr "vraymtl_water:VRayMtl1.oc" "vraymtl_water:VRayMtl1SG.ss";
connectAttr "PhoenixFDSimulator1.iog" "vraymtl_water:VRayMtl1SG.dsm" -na;
connectAttr "vraymtl_water:VRayMtl1SG.msg" "materialInfo1.sg";
connectAttr "vraymtl_water:VRayMtl1.msg" "materialInfo1.m";
connectAttr "PG_PhoenixFDSimulator1_Foam_0.msg" "phxfoam_set1.dnsm" -na;
connectAttr "PG_PhoenixFDSimulator1_Splashes_0.msg" "phxfoam_set2.dnsm" -na;
connectAttr "VRaySunShape1.msg" "VRaySky1.s";
connectAttr "VRaySky1.oc" "remapHsv1.cl";
connectAttr ":time1.o" "PhoenixFDOceanTexture1.ct";
connectAttr "place3dTexture1.wim" "PhoenixFDOceanTexture1.pm";
connectAttr "lambert2.oc" "lambert2SG.ss";
connectAttr "pPlaneShape1.iog" "lambert2SG.dsm" -na;
connectAttr "lambert2SG.msg" "materialInfo2.sg";
connectAttr "lambert2.msg" "materialInfo2.m";
connectAttr "vraymtl_water:VRayMtl1SG.pa" ":renderPartition.st" -na;
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "pSphereShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "PhoenixFDFoam2.iog" ":initialShadingGroup.dsm" -na;
connectAttr "PhoenixFDFoam1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "vraymtl_water:VRayMtl1.msg" ":defaultShaderList1.s" -na;
connectAttr "lambert2.msg" ":defaultShaderList1.s" -na;
connectAttr "VRaySky1.msg" ":defaultTextureList1.tx" -na;
connectAttr "PhoenixFDOceanTexture1.msg" ":defaultTextureList1.tx" -na;
connectAttr "VRaySunShape1.ltd" ":lightList1.l" -na;
connectAttr "VRaySunTarget1.msg" ":lightList1.l" -na;
connectAttr "remapHsv1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place3dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "VRayGeoSun1.iog" ":defaultLightSet.dsm" -na;
connectAttr "transform5.iog" ":defaultLightSet.dsm" -na;
// End of phx_pool.ma
