//Maya ASCII 2011 scene
//Name: phx_cascade2.ma
//Last modified: Wed, May 15, 2013 06:39:07 PM
//Codeset: 1251
requires maya "2011";
requires "vrayformaya" "3.05.01";
requires "phoenixfd" "2.0.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2011";
fileInfo "version" "2011 x64";
fileInfo "cutIdentifier" "201003190311-771506";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 3.2206576181646391 14.836093027962004 4.2523414357796421 ;
	setAttr ".r" -type "double3" -61.200000000015635 26.000000000000259 0 ;
	setAttr ".rp" -type "double3" -1.1102230246251565e-015 -4.4408920985006262e-016 
		0 ;
	setAttr ".rpt" -type "double3" -5.9374028776423247e-018 1.6686070926123788e-016 
		4.9959049138386399e-016 ;
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
	setAttr ".fl" 34.999999999999979;
	setAttr ".coi" 10.366604208591736;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 4.9466459723715008 4.9999934267497022 0.20327798451317136 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".dfg" yes;
	setAttr ".vrayCameraPhysicalOn" 1;
	setAttr ".vrayCameraPhysicalFocalLength" 26.165645599365234;
	setAttr ".vrayCameraPhysicalFOV" 54.432224273681641;
	setAttr ".vrayCameraPhysicalLensFile" -type "string" "";
	setAttr ".vrayCameraPhysicalShutterSpeed" 50;
	setAttr ".vrayCameraPhysicalISO" 25;
createNode transform -s -n "top";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 100.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -0.6576641968068857 8.1850537593861858 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 11.307747224582055;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 8.8636363636363615 4.2187500000000027 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "PhoenixFDSim1";
	setAttr ".t" -type "double3" -4.35 7.3 0.2 ;
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
	setAttr ".ct" 63;
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
	setAttr ".cm" 0;
	setAttr ".cfl" 0;
	setAttr ".cfi" 0;
	setAttr ".cq" 20;
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
	setAttr ".rsor" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1_resim";
	setAttr ".rsir" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1";
	setAttr ".rso" -type "string" "$(implicit)";
	setAttr ".rsaf" 1;
	setAttr ".rstc" 0;
	setAttr ".rsa" 1;
	setAttr ".rsam" 0;
	setAttr ".wvs" 3;
	setAttr ".wvc" 0.0010000000474974513;
	setAttr ".lgr" yes;
	setAttr ".mun" 3;
	setAttr ".uns" 1;
	setAttr ".csz" 0.10000000149011612;
	setAttr ".xsz" 121;
	setAttr ".ysz" 29;
	setAttr ".zsz" 43;
	setAttr ".bx" 0;
	setAttr ".by" 0;
	setAttr ".bz" 0;
	setAttr ".gpa" 1;
	setAttr ".ag" 0;
	setAttr ".gt" 1000;
	setAttr ".lby" 1;
	setAttr ".lto" 90;
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
	setAttr ".wfm" yes;
	setAttr ".egr" yes;
	setAttr ".gr" 1;
	setAttr ".egrv" no;
	setAttr ".grv" -type "float3" 0 -9.8000002 0 ;
	setAttr ".tsc" 1;
	setAttr ".vrt" 0;
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
	setAttr ".lqsharpness" 1;
	setAttr ".lqad" 0;
	setAttr ".lqsurft" 0;
	setAttr ".lqvisc" 0;
	setAttr ".drying" 0.0099999997764825821;
	setAttr ".flevel" 50;
	setAttr ".initfill" no;
	setAttr ".wetting" yes;
	setAttr ".flatliquids" no;
	setAttr ".strongsurf" yes;
	setAttr ".foam" no;
	setAttr ".fbirth" 100;
	setAttr ".fbthres" 50;
	setAttr ".fhlf" 10;
	setAttr ".foutlife" 0;
	setAttr ".fsize" 0.10000000149011612;
	setAttr ".fsizevar" 3;
	setAttr ".fszdstrb" 200;
	setAttr ".fcycles" 3000;
	setAttr ".frise" 10;
	setAttr ".ffall" 1000;
	setAttr ".fsticky" 0;
	setAttr ".fptrn" 0;
	setAttr ".fptrnsz" 10;
	setAttr ".splashes" no;
	setAttr ".spbirth" 5;
	setAttr ".spbthres" 60;
	setAttr ".spsize" 0.05000000074505806;
	setAttr ".spsizevar" 5;
	setAttr ".spszdstrb" 100;
	setAttr ".airfr" 1;
	setAttr ".sp2foam" 0;
	setAttr ".sp2liquid" no;
	setAttr ".spto" 0;
	setAttr ".vmult" 1;
	setAttr ".spsplit" 0;
	setAttr ".sq" 14;
	setAttr ".bi" -1;
	setAttr ".ci" no;
	setAttr ".ot" yes;
	setAttr ".osm" no;
	setAttr ".ou" no;
	setAttr ".ow" no;
	setAttr ".osp" no;
	setAttr ".ov" yes;
	setAttr ".of" no;
	setAttr ".opi" no;
	setAttr ".opth" -type "string" "$(implicit)";
	setAttr ".opthr" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1";
	setAttr ".uset2f" no;
	setAttr ".t2f" 1;
	setAttr ".iro" 0;
	setAttr ".iml" 0;
	setAttr ".ipa" 0;
	setAttr ".play_speed" 1;
	setAttr ".ibm" 0;
	setAttr ".ipth" -type "string" "$(simoutput)";
	setAttr ".ipthr" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim1@PhoenixFDSimulator1";
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
	setAttr ".ieh" yes;
	setAttr ".sg" yes;
	setAttr ".sgs" no;
	setAttr ".cr" 100;
	setAttr ".ois" no;
	setAttr ".avo" yes;
	setAttr ".andr" no;
	setAttr ".vt" yes;
	setAttr ".vtn" no;
	setAttr ".vtc" -type "float3" 0 0 0.5 ;
	setAttr ".vtc2" -type "float3" 0 0 1.001 ;
	setAttr ".vtt" 0.5;
	setAttr ".vtt2" 1;
	setAttr ".vs" no;
	setAttr ".vsc" -type "float3" 0.5 0.5 0.5 ;
	setAttr ".vsc2" -type "float3" 0 0 0 ;
	setAttr ".vst" 0.0099999997764825821;
	setAttr ".vst2" 1;
	setAttr ".vu" yes;
	setAttr ".vur" yes;
	setAttr ".vuc" -type "float3" 0.44999999 0.55000001 0.44999999 ;
	setAttr ".vuc2" -type "float3" 0 0.5 0 ;
	setAttr ".vut" 1;
	setAttr ".vut2" 1000;
	setAttr ".vw" yes;
	setAttr ".vwc" -type "float3" 0.30000001 0.30000001 0 ;
	setAttr ".vwc2" -type "float3" 0.89999998 0.89999998 0 ;
	setAttr ".vwt" 0.0099999997764825821;
	setAttr ".vwt2" 1000;
	setAttr ".vfu" yes;
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
	setAttr ".vspc" -type "float3" 0 0 1 ;
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
	setAttr ".vmc" -type "float3" 0.22 0.22 0.94999999 ;
	setAttr ".vma" 0.5;
	setAttr ".vmas" no;
	setAttr ".rsl_x" 0.5;
	setAttr ".rsl_t" 0.40000000596046448;
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
	setAttr ".geommode" yes;
	setAttr ".heathaze" 1;
	setAttr ".rendsolid" yes;
	setAttr ".rendMode" 3;
	setAttr ".bias" 1;
	setAttr ".usebias" no;
	setAttr ".wrapx" 2;
	setAttr ".wrapy" 2;
	setAttr ".wrapz" 2;
	setAttr ".oceanlevel" 50;
	setAttr ".ocean" no;
	setAttr ".smoothmesh" 5;
	setAttr ".displacement" no;
	setAttr ".displmul" 1;
	setAttr ".displ2d" 1;
	setAttr ".displ0" -type "float3" 0 0 0 ;
	setAttr ".displ1" -type "float3" 0 0 0 ;
	setAttr ".displ2" -type "float3" 0 0 0 ;
	setAttr ".mid" -type "float3" 0 0 0 ;
	setAttr ".vn" 0;
	setAttr ".vz" 0;
	setAttr ".usegizmo" yes;
	setAttr ".invgizmo" yes;
	setAttr ".earg" 0;
	setAttr ".et" -type "float3" 0 0 0 ;
	setAttr ".em" no;
	setAttr ".no_alpha_e" no;
	setAttr ".elc" 0;
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
	setAttr ".ecolor_t[0].ecolor_tc" -type "float3" 1 0.19712909 0.0011662382 ;
	setAttr ".ecolor_t[0].ecolor_ti" 3;
	setAttr ".ecolor_t[1].ecolor_tp" 2000.0010986328125;
	setAttr ".ecolor_t[1].ecolor_tc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_t[1].ecolor_ti" 3;
	setAttr -s 2 ".ecolor_s";
	setAttr ".ecolor_s[0].ecolor_sp" 0.55000001192092896;
	setAttr ".ecolor_s[0].ecolor_sc" -type "float3" 1 0.19712909 0.0011662382 ;
	setAttr ".ecolor_s[0].ecolor_si" 3;
	setAttr ".ecolor_s[1].ecolor_sp" 1.0000004768371582;
	setAttr ".ecolor_s[1].ecolor_sc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_s[1].ecolor_si" 3;
	setAttr -s 2 ".ecolor_v";
	setAttr ".ecolor_v[0].ecolor_vp" 220;
	setAttr ".ecolor_v[0].ecolor_vc" -type "float3" 1 0.19712909 0.0011662382 ;
	setAttr ".ecolor_v[0].ecolor_vi" 3;
	setAttr ".ecolor_v[1].ecolor_vp" 400.00021362304687;
	setAttr ".ecolor_v[1].ecolor_vc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_v[1].ecolor_vi" 3;
	setAttr -s 2 ".ecolor_f";
	setAttr ".ecolor_f[0].ecolor_fp" 0.55000001192092896;
	setAttr ".ecolor_f[0].ecolor_fc" -type "float3" 1 0.19712909 0.0011662382 ;
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
	setAttr -s 14 ".epower_t[0:13]"  1100 25.554504 3 1161.4382 78.974503 
		3 1226.3079 231.1813 3 1294.8008 655.27289 3 1367.119 1731.8934 3 1443.4766 
		4359.9619 3 1524.099 10680.139 3 1609.2242 24719.855 3 1699.1041 55058.258 
		3 1794.0039 118313.66 3 1894.2043 243318.33 3 2000.0011 483980.19 3 1974.2869 
		412181.72 3 1995.5011 470704.94 3;
	setAttr -s 14 ".epower_s[0:13]"  0.55000001 25.554504 3 0.58071911 
		78.974503 3 0.61315393 231.1813 3 0.64740038 655.27289 3 0.68355954 1731.8934 
		3 0.72173828 4359.9619 3 0.7620495 10680.139 3 0.8046121 24719.855 3 
		0.84955204 55058.258 3 0.89700192 118313.66 3 0.94710219 243318.33 3 1.0000005 
		483980.19 3 0.9871434 412181.72 3 0.99775052 470704.94 3;
	setAttr -s 14 ".epower_v[0:13]"  220 25.554504 3 232.28764 78.974503 
		3 245.26157 231.1813 3 258.96014 655.27289 3 273.4238 1731.8934 3 288.69531 
		4359.9619 3 304.81979 10680.139 3 321.84485 24719.855 3 339.82083 55058.258 
		3 358.80078 118313.66 3 378.84088 243318.33 3 400.00021 483980.19 3 394.85736 
		412181.72 3 399.10022 470704.94 3;
	setAttr -s 14 ".epower_f[0:13]"  0.55000001 25.554504 3 0.58071911 
		78.974503 3 0.61315393 231.1813 3 0.64740038 655.27289 3 0.68355954 1731.8934 
		3 0.72173828 4359.9619 3 0.7620495 10680.139 3 0.8046121 24719.855 3 
		0.84955204 55058.258 3 0.89700192 118313.66 3 0.94710219 243318.33 3 1.0000005 
		483980.19 3 0.9871434 412181.72 3 0.99775052 470704.94 3;
	setAttr -s 3 ".tpower_t[0:2]"  0 0 0 0.30000001 0 1 0.5 0.25 
		0;
	setAttr -s 9 ".tpower_s[0:8]"  0.14 0 3 0.43600002 0.025 3 
		0.50319999 0.054000001 3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 
		3 0.74000001 0 3 0.82000005 0.050000001 3 0.94 0 3;
	setAttr -s 9 ".tpower_v[0:8]"  90 0 3 278.70001 0.025 3 321.54001 
		0.054000001 3 331.73999 0.1 3 332.25 0.1 1 343.72501 0 3 472.5 0 3 
		523.5 0.050000001 3 600 0 3;
	setAttr -s 9 ".tpower_f[0:8]"  0.14 0 3 0.43600002 0.025 3 
		0.50319999 0.054000001 3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 
		3 0.74000001 0 3 0.82000005 0.050000001 3 0.94 0 3;
createNode transform -n "PhoenixFDSim2";
	setAttr ".t" -type "double3" 4.8 0 0.1 ;
createNode PhoenixFDSimulator -n "PhoenixFDSimulator2" -p "PhoenixFDSim2";
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
	setAttr ".ct" 63;
	setAttr ".ui" 0;
	setAttr ".tl" 0;
	setAttr ".nsys0" -1;
	setAttr ".nsys1" -1;
	setAttr ".ssf" yes;
	setAttr ".saf" 20;
	setAttr ".sof" 20;
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
	setAttr ".cq" 20;
	setAttr ".cun" no;
	setAttr ".adm" 0;
	setAttr ".ams" 4;
	setAttr ".spf1" 2;
	setAttr ".spf2" 2;
	setAttr ".as" no;
	setAttr ".dc" no;
	setAttr ".rs" no;
	setAttr ".rswm" no;
	setAttr ".rscq" 2;
	setAttr ".rsi" -type "string" "$(simoutput)";
	setAttr ".rsor" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim2@PhoenixFDSimulator2_resim";
	setAttr ".rsir" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim2@PhoenixFDSimulator2";
	setAttr ".rso" -type "string" "$(implicit)";
	setAttr ".rsaf" 0;
	setAttr ".rstc" 0;
	setAttr ".rsa" 1;
	setAttr ".rsam" 2;
	setAttr ".wvs" 3;
	setAttr ".wvc" 0.0010000000474974513;
	setAttr ".lgr" yes;
	setAttr ".mun" 3;
	setAttr ".uns" 1;
	setAttr ".csz" 0.10000000149011612;
	setAttr ".xsz" 74;
	setAttr ".ysz" 37;
	setAttr ".zsz" 100;
	setAttr ".bx" 0;
	setAttr ".by" 0;
	setAttr ".bz" 1;
	setAttr ".gpa" 1;
	setAttr ".ag" 0;
	setAttr ".gt" 1000;
	setAttr ".lby" 1;
	setAttr ".lto" 90;
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
	setAttr ".wfm" yes;
	setAttr ".egr" yes;
	setAttr ".gr" 1;
	setAttr ".egrv" no;
	setAttr ".grv" -type "float3" 0 -9.8000002 0 ;
	setAttr ".tsc" 1;
	setAttr ".vrt" 0;
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
	setAttr ".flevel" 50;
	setAttr ".initfill" no;
	setAttr ".wetting" yes;
	setAttr ".flatliquids" no;
	setAttr ".strongsurf" yes;
	setAttr ".foam" no;
	setAttr ".fbirth" 10;
	setAttr ".fbthres" 60;
	setAttr ".fhlf" 10;
	setAttr ".foutlife" 0;
	setAttr ".fsize" 0.019999999552965164;
	setAttr ".fsizevar" 0.10000000149011612;
	setAttr ".fszdstrb" 200;
	setAttr ".fcycles" 3000;
	setAttr ".frise" 10;
	setAttr ".ffall" 1000;
	setAttr ".fsticky" 0;
	setAttr ".fptrn" 0;
	setAttr ".fptrnsz" 10;
	setAttr ".splashes" yes;
	setAttr ".spbirth" 100;
	setAttr ".spbthres" 40;
	setAttr ".spsize" 0.029999999329447746;
	setAttr ".spsizevar" 0.10000000149011612;
	setAttr ".spszdstrb" 100;
	setAttr ".airfr" 1;
	setAttr ".sp2foam" 0;
	setAttr ".sp2liquid" no;
	setAttr ".spto" 0;
	setAttr ".vmult" 1;
	setAttr ".spsplit" 0;
	setAttr ".sq" 14;
	setAttr ".bi" -1;
	setAttr ".ci" no;
	setAttr ".ot" yes;
	setAttr ".osm" no;
	setAttr ".ou" no;
	setAttr ".ow" no;
	setAttr ".osp" no;
	setAttr ".ov" yes;
	setAttr ".of" no;
	setAttr ".opi" no;
	setAttr ".opth" -type "string" "$(implicit)";
	setAttr ".opthr" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim2@PhoenixFDSimulator2";
	setAttr ".uset2f" no;
	setAttr ".t2f" 1;
	setAttr ".iro" 0;
	setAttr ".iml" 0;
	setAttr ".ipa" 0;
	setAttr ".play_speed" 1;
	setAttr ".ibm" 0;
	setAttr ".ipth" -type "string" "$(simoutput)";
	setAttr ".ipthr" -type "string" "D:\\PhoenixFD_cache\\phx_cascade2.ma_Phoenix2_frames\\@PhoenixFDSim2@PhoenixFDSimulator2";
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
	setAttr ".ieh" yes;
	setAttr ".sg" yes;
	setAttr ".sgs" no;
	setAttr ".cr" 100;
	setAttr ".ois" no;
	setAttr ".avo" yes;
	setAttr ".andr" no;
	setAttr ".vt" yes;
	setAttr ".vtn" no;
	setAttr ".vtc" -type "float3" 0.40150002 0.428725 0.55000001 ;
	setAttr ".vtc2" -type "float3" 0 0 1 ;
	setAttr ".vtt" 0.20000000298023224;
	setAttr ".vtt2" 1;
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
	setAttr ".vw" yes;
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
	setAttr ".vspc" -type "float3" 0.449 0.449 1 ;
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
	setAttr ".vmc" -type "float3" 0.22 0.22 0.94999999 ;
	setAttr ".vma" 0.5;
	setAttr ".vmas" no;
	setAttr ".rsl_x" 0.5;
	setAttr ".rsl_t" 0.40000000596046448;
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
	setAttr ".geommode" yes;
	setAttr ".heathaze" 1;
	setAttr ".rendsolid" yes;
	setAttr ".rendMode" 3;
	setAttr ".bias" 1;
	setAttr ".usebias" no;
	setAttr ".wrapx" 2;
	setAttr ".wrapy" 2;
	setAttr ".wrapz" 2;
	setAttr ".oceanlevel" 50;
	setAttr ".ocean" no;
	setAttr ".smoothmesh" 5;
	setAttr ".displacement" no;
	setAttr ".displmul" 1;
	setAttr ".displ2d" 1;
	setAttr ".displ0" -type "float3" 0 0 0 ;
	setAttr ".displ1" -type "float3" 0 0 0 ;
	setAttr ".displ2" -type "float3" 0 0 0 ;
	setAttr ".mid" -type "float3" 0 0 0 ;
	setAttr ".vn" 0;
	setAttr ".vz" 0;
	setAttr ".usegizmo" no;
	setAttr ".invgizmo" yes;
	setAttr ".earg" 1;
	setAttr ".et" -type "float3" 0 0 0 ;
	setAttr ".em" no;
	setAttr ".no_alpha_e" no;
	setAttr ".elc" 0;
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
	setAttr ".simple_color" -type "float3" 0.5 0.5 0.5 ;
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
	setAttr ".trl_t" 1700;
	setAttr ".tro_t" 300;
	setAttr ".trm_t" 0.10000000149011612;
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
	setAttr ".ecolor_t[0].ecolor_tc" -type "float3" 1 0.19712909 0.0011662382 ;
	setAttr ".ecolor_t[0].ecolor_ti" 3;
	setAttr ".ecolor_t[1].ecolor_tp" 2000.0010986328125;
	setAttr ".ecolor_t[1].ecolor_tc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_t[1].ecolor_ti" 3;
	setAttr -s 2 ".ecolor_s";
	setAttr ".ecolor_s[0].ecolor_sp" 0.55000001192092896;
	setAttr ".ecolor_s[0].ecolor_sc" -type "float3" 1 0.19712909 0.0011662382 ;
	setAttr ".ecolor_s[0].ecolor_si" 3;
	setAttr ".ecolor_s[1].ecolor_sp" 1.0000004768371582;
	setAttr ".ecolor_s[1].ecolor_sc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_s[1].ecolor_si" 3;
	setAttr -s 2 ".ecolor_v";
	setAttr ".ecolor_v[0].ecolor_vp" 220;
	setAttr ".ecolor_v[0].ecolor_vc" -type "float3" 1 0.19712909 0.0011662382 ;
	setAttr ".ecolor_v[0].ecolor_vi" 3;
	setAttr ".ecolor_v[1].ecolor_vp" 400.00021362304687;
	setAttr ".ecolor_v[1].ecolor_vc" -type "float3" 1 0.39821133 0.061485972 ;
	setAttr ".ecolor_v[1].ecolor_vi" 3;
	setAttr -s 2 ".ecolor_f";
	setAttr ".ecolor_f[0].ecolor_fp" 0.55000001192092896;
	setAttr ".ecolor_f[0].ecolor_fc" -type "float3" 1 0.19712909 0.0011662382 ;
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
	setAttr -s 14 ".epower_t[0:13]"  1100 25.554504 3 1161.4382 78.974503 
		3 1226.3079 231.1813 3 1294.8008 655.27289 3 1367.119 1731.8934 3 1443.4766 
		4359.9619 3 1524.099 10680.139 3 1609.2242 24719.855 3 1699.1041 55058.258 
		3 1794.0039 118313.66 3 1894.2043 243318.33 3 2000.0011 483980.19 3 1974.2869 
		412181.72 3 1995.5011 470704.94 3;
	setAttr -s 14 ".epower_s[0:13]"  0.55000001 25.554504 3 0.58071911 
		78.974503 3 0.61315393 231.1813 3 0.64740038 655.27289 3 0.68355954 1731.8934 
		3 0.72173828 4359.9619 3 0.7620495 10680.139 3 0.8046121 24719.855 3 
		0.84955204 55058.258 3 0.89700192 118313.66 3 0.94710219 243318.33 3 1.0000005 
		483980.19 3 0.9871434 412181.72 3 0.99775052 470704.94 3;
	setAttr -s 14 ".epower_v[0:13]"  220 25.554504 3 232.28764 78.974503 
		3 245.26157 231.1813 3 258.96014 655.27289 3 273.4238 1731.8934 3 288.69531 
		4359.9619 3 304.81979 10680.139 3 321.84485 24719.855 3 339.82083 55058.258 
		3 358.80078 118313.66 3 378.84088 243318.33 3 400.00021 483980.19 3 394.85736 
		412181.72 3 399.10022 470704.94 3;
	setAttr -s 14 ".epower_f[0:13]"  0.55000001 25.554504 3 0.58071911 
		78.974503 3 0.61315393 231.1813 3 0.64740038 655.27289 3 0.68355954 1731.8934 
		3 0.72173828 4359.9619 3 0.7620495 10680.139 3 0.8046121 24719.855 3 
		0.84955204 55058.258 3 0.89700192 118313.66 3 0.94710219 243318.33 3 1.0000005 
		483980.19 3 0.9871434 412181.72 3 0.99775052 470704.94 3;
	setAttr -s 9 ".tpower_t[0:8]"  300 0 3 929 0.025 3 1071.8 0.054000001 
		3 1105.8 0.1 3 1107.5 0.1 1 1145.75 0 3 1575 0 3 1745 0.050000001 
		3 2000 0 3;
	setAttr -s 9 ".tpower_s[0:8]"  0.14 0 3 0.43600002 0.025 3 
		0.50319999 0.054000001 3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 
		3 0.74000001 0 3 0.82000005 0.050000001 3 0.94 0 3;
	setAttr -s 9 ".tpower_v[0:8]"  90 0 3 278.70001 0.025 3 321.54001 
		0.054000001 3 331.73999 0.1 3 332.25 0.1 1 343.72501 0 3 472.5 0 3 
		523.5 0.050000001 3 600 0 3;
	setAttr -s 9 ".tpower_f[0:8]"  0.14 0 3 0.43600002 0.025 3 
		0.50319999 0.054000001 3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 
		3 0.74000001 0 3 0.82000005 0.050000001 3 0.94 0 3;
createNode transform -n "pCylinder1";
	setAttr ".t" -type "double3" -5.8821815274310687 9.7270835427163984 -8.8223746881567564 ;
	setAttr ".r" -type "double3" 0 0 90 ;
createNode transform -n "transform4" -p "pCylinder1";
	setAttr ".v" no;
createNode mesh -n "pCylinderShape1" -p "transform4";
	addAttr -ci true -sn "mso" -ln "miShadingSamplesOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "msh" -ln "miShadingSamples" -min 0 -smx 8 -at "float";
	addAttr -ci true -sn "mdo" -ln "miMaxDisplaceOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "mmd" -ln "miMaxDisplace" -min 0 -smx 1 -at "float";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
createNode transform -n "pCylinder2";
	setAttr ".t" -type "double3" -5.8821815274310687 9.7270835427163984 -8.8223746881567564 ;
	setAttr ".r" -type "double3" 0 0 90 ;
	setAttr ".s" -type "double3" 0.8 1.1 0.8 ;
createNode transform -n "transform3" -p "pCylinder2";
	setAttr ".v" no;
createNode mesh -n "pCylinderShape2" -p "transform3";
	addAttr -ci true -sn "mso" -ln "miShadingSamplesOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "msh" -ln "miShadingSamples" -min 0 -smx 8 -at "float";
	addAttr -ci true -sn "mdo" -ln "miMaxDisplaceOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "mmd" -ln "miMaxDisplace" -min 0 -smx 1 -at "float";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0:59]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 84 ".uvst[0].uvsp[0:83]" -type "float2" 0.64860266 0.10796607 
		0.62640899 0.064408496 0.59184152 0.029841021 0.54828393 0.0076473355 0.5 -7.4505806e-008 
		0.45171607 0.0076473504 0.40815851 0.029841051 0.37359107 0.064408526 0.3513974 0.10796608 
		0.34374997 0.15625 0.3513974 0.20453392 0.37359107 0.24809146 0.40815854 0.28265893 
		0.4517161 0.3048526 0.5 0.3125 0.54828387 0.3048526 0.59184146 0.28265893 0.62640893 
		0.24809146 0.6486026 0.2045339 0.65625 0.15625 0.375 0.3125 0.38749999 0.3125 0.39999998 
		0.3125 0.41249996 0.3125 0.42499995 0.3125 0.43749994 0.3125 0.44999993 0.3125 0.46249992 
		0.3125 0.4749999 0.3125 0.48749989 0.3125 0.49999988 0.3125 0.51249987 0.3125 0.52499986 
		0.3125 0.53749985 0.3125 0.54999983 0.3125 0.56249982 0.3125 0.57499981 0.3125 0.5874998 
		0.3125 0.59999979 0.3125 0.61249977 0.3125 0.62499976 0.3125 0.375 0.68843985 0.38749999 
		0.68843985 0.39999998 0.68843985 0.41249996 0.68843985 0.42499995 0.68843985 0.43749994 
		0.68843985 0.44999993 0.68843985 0.46249992 0.68843985 0.4749999 0.68843985 0.48749989 
		0.68843985 0.49999988 0.68843985 0.51249987 0.68843985 0.52499986 0.68843985 0.53749985 
		0.68843985 0.54999983 0.68843985 0.56249982 0.68843985 0.57499981 0.68843985 0.5874998 
		0.68843985 0.59999979 0.68843985 0.61249977 0.68843985 0.62499976 0.68843985 0.64860266 
		0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5 
		0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974 
		0.79546607 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854 
		0.97015893 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893 
		0.93559146 0.6486026 0.89203393 0.65625 0.84375 0.5 0.15000001 0.5 0.83749998;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
	setAttr -s 42 ".vt[0:41]"  1.0461628 -7 -0.33991891 0.88991934 -7 -0.64656419 
		0.64656419 -7 -0.88991922 0.33991888 -7 -1.0461627 0 -7 -1.1000005 -0.33991888 -7 
		-1.0461627 -0.64656407 -7 -0.88991904 -0.88991898 -7 -0.64656401 -1.0461625 -7 -0.33991876 
		-1.1000003 -7 0 -1.0461625 -7 0.33991876 -0.88991892 -7 0.64656389 -0.64656389 -7 
		0.88991886 -0.33991876 -7 1.0461624 -3.2782555e-008 -7 1.1000001 0.33991867 -7 1.0461622 
		0.64656377 -7 0.8899188 0.88991874 -7 0.64656383 1.0461622 -7 0.3399187 1.1 -7 0 
		1.0461628 7 -0.33991891 0.88991934 7 -0.64656419 0.64656419 7 -0.88991922 0.33991888 
		7 -1.0461627 0 7 -1.1000005 -0.33991888 7 -1.0461627 -0.64656407 7 -0.88991904 -0.88991898 
		7 -0.64656401 -1.0461625 7 -0.33991876 -1.1000003 7 0 -1.0461625 7 0.33991876 -0.88991892 
		7 0.64656389 -0.64656389 7 0.88991886 -0.33991876 7 1.0461624 -3.2782555e-008 7 1.1000001 
		0.33991867 7 1.0461622 0.64656377 7 0.8899188 0.88991874 7 0.64656383 1.0461622 7 
		0.3399187 1.1 7 0 0 -7 0 0 7 0;
	setAttr -s 100 ".ed[0:99]"  0 1 0 1 2 0 
		2 3 0 3 4 0 4 5 0 5 6 0 
		6 7 0 7 8 0 8 9 0 9 10 0 
		10 11 0 11 12 0 12 13 0 13 14 0 
		14 15 0 15 16 0 16 17 0 17 18 0 
		18 19 0 19 0 0 20 21 0 21 22 0 
		22 23 0 23 24 0 24 25 0 25 26 0 
		26 27 0 27 28 0 28 29 0 29 30 0 
		30 31 0 31 32 0 32 33 0 33 34 0 
		34 35 0 35 36 0 36 37 0 37 38 0 
		38 39 0 39 20 0 0 20 1 1 21 1 
		2 22 1 3 23 1 4 24 1 5 25 1 
		6 26 1 7 27 1 8 28 1 9 29 1 
		10 30 1 11 31 1 12 32 1 13 33 1 
		14 34 1 15 35 1 16 36 1 17 37 1 
		18 38 1 19 39 1 40 0 1 40 1 1 
		40 2 1 40 3 1 40 4 1 40 5 1 
		40 6 1 40 7 1 40 8 1 40 9 1 
		40 10 1 40 11 1 40 12 1 40 13 1 
		40 14 1 40 15 1 40 16 1 40 17 1 
		40 18 1 40 19 1 20 41 1 21 41 1 
		22 41 1 23 41 1 24 41 1 25 41 1 
		26 41 1 27 41 1 28 41 1 29 41 1 
		30 41 1 31 41 1 32 41 1 33 41 1 
		34 41 1 35 41 1 36 41 1 37 41 1 
		38 41 1 39 41 1;
	setAttr -s 60 ".fc[0:59]" -type "polyFaces" 
		f 4 0 41 -21 -41 
		mu 0 4 20 21 42 41 
		f 4 1 42 -22 -42 
		mu 0 4 21 22 43 42 
		f 4 2 43 -23 -43 
		mu 0 4 22 23 44 43 
		f 4 3 44 -24 -44 
		mu 0 4 23 24 45 44 
		f 4 4 45 -25 -45 
		mu 0 4 24 25 46 45 
		f 4 5 46 -26 -46 
		mu 0 4 25 26 47 46 
		f 4 6 47 -27 -47 
		mu 0 4 26 27 48 47 
		f 4 7 48 -28 -48 
		mu 0 4 27 28 49 48 
		f 4 8 49 -29 -49 
		mu 0 4 28 29 50 49 
		f 4 9 50 -30 -50 
		mu 0 4 29 30 51 50 
		f 4 10 51 -31 -51 
		mu 0 4 30 31 52 51 
		f 4 11 52 -32 -52 
		mu 0 4 31 32 53 52 
		f 4 12 53 -33 -53 
		mu 0 4 32 33 54 53 
		f 4 13 54 -34 -54 
		mu 0 4 33 34 55 54 
		f 4 14 55 -35 -55 
		mu 0 4 34 35 56 55 
		f 4 15 56 -36 -56 
		mu 0 4 35 36 57 56 
		f 4 16 57 -37 -57 
		mu 0 4 36 37 58 57 
		f 4 17 58 -38 -58 
		mu 0 4 37 38 59 58 
		f 4 18 59 -39 -59 
		mu 0 4 38 39 60 59 
		f 4 19 40 -40 -60 
		mu 0 4 39 40 61 60 
		f 3 -1 -61 61 
		mu 0 3 1 0 82 
		f 3 -2 -62 62 
		mu 0 3 2 1 82 
		f 3 -3 -63 63 
		mu 0 3 3 2 82 
		f 3 -4 -64 64 
		mu 0 3 4 3 82 
		f 3 -5 -65 65 
		mu 0 3 5 4 82 
		f 3 -6 -66 66 
		mu 0 3 6 5 82 
		f 3 -7 -67 67 
		mu 0 3 7 6 82 
		f 3 -8 -68 68 
		mu 0 3 8 7 82 
		f 3 -9 -69 69 
		mu 0 3 9 8 82 
		f 3 -10 -70 70 
		mu 0 3 10 9 82 
		f 3 -11 -71 71 
		mu 0 3 11 10 82 
		f 3 -12 -72 72 
		mu 0 3 12 11 82 
		f 3 -13 -73 73 
		mu 0 3 13 12 82 
		f 3 -14 -74 74 
		mu 0 3 14 13 82 
		f 3 -15 -75 75 
		mu 0 3 15 14 82 
		f 3 -16 -76 76 
		mu 0 3 16 15 82 
		f 3 -17 -77 77 
		mu 0 3 17 16 82 
		f 3 -18 -78 78 
		mu 0 3 18 17 82 
		f 3 -19 -79 79 
		mu 0 3 19 18 82 
		f 3 -20 -80 60 
		mu 0 3 0 19 82 
		f 3 20 81 -81 
		mu 0 3 80 79 83 
		f 3 21 82 -82 
		mu 0 3 79 78 83 
		f 3 22 83 -83 
		mu 0 3 78 77 83 
		f 3 23 84 -84 
		mu 0 3 77 76 83 
		f 3 24 85 -85 
		mu 0 3 76 75 83 
		f 3 25 86 -86 
		mu 0 3 75 74 83 
		f 3 26 87 -87 
		mu 0 3 74 73 83 
		f 3 27 88 -88 
		mu 0 3 73 72 83 
		f 3 28 89 -89 
		mu 0 3 72 71 83 
		f 3 29 90 -90 
		mu 0 3 71 70 83 
		f 3 30 91 -91 
		mu 0 3 70 69 83 
		f 3 31 92 -92 
		mu 0 3 69 68 83 
		f 3 32 93 -93 
		mu 0 3 68 67 83 
		f 3 33 94 -94 
		mu 0 3 67 66 83 
		f 3 34 95 -95 
		mu 0 3 66 65 83 
		f 3 35 96 -96 
		mu 0 3 65 64 83 
		f 3 36 97 -97 
		mu 0 3 64 63 83 
		f 3 37 98 -98 
		mu 0 3 63 62 83 
		f 3 38 99 -99 
		mu 0 3 62 81 83 
		f 3 39 80 -100 
		mu 0 3 81 80 83 ;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "polySurface1";
createNode transform -n "transform5" -p "polySurface1";
	setAttr ".v" no;
createNode mesh -n "polySurfaceShape1" -p "transform5";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
createNode transform -n "pCube1";
	setAttr ".t" -type "double3" -12.59666909959013 18.225982498472757 -0.76340210840891487 ;
createNode transform -n "transform6" -p "pCube1";
	setAttr ".v" no;
createNode mesh -n "pCubeShape1" -p "transform6";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
createNode transform -n "polySurface2";
	setAttr ".t" -type "double3" -0.03855781625329513 -0.40463185635498533 9.0644251450264761 ;
	setAttr ".r" -type "double3" -180 0 -10 ;
	setAttr ".rp" -type "double3" -5.88218092918396 10.264988422393799 -8.8223743438720703 ;
	setAttr ".sp" -type "double3" -5.88218092918396 10.264988422393799 -8.8223743438720703 ;
createNode mesh -n "polySurfaceShape2" -p "polySurface2";
	addAttr -ci true -sn "mso" -ln "miShadingSamplesOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "msh" -ln "miShadingSamples" -min 0 -smx 8 -at "float";
	addAttr -ci true -sn "mdo" -ln "miMaxDisplaceOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "mmd" -ln "miMaxDisplace" -min 0 -smx 1 -at "float";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
createNode transform -n "pCylinder3";
	setAttr ".t" -type "double3" -8.5533431433768161 10.741130220655643 0.2983370494182277 ;
	setAttr ".r" -type "double3" 0 0 -100 ;
createNode mesh -n "pCylinderShape3" -p "pCylinder3";
	addAttr -ci true -sn "mso" -ln "miShadingSamplesOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "msh" -ln "miShadingSamples" -min 0 -smx 8 -at "float";
	addAttr -ci true -sn "mdo" -ln "miMaxDisplaceOverride" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "mmd" -ln "miMaxDisplace" -min 0 -smx 1 -at "float";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
createNode transform -n "PhoenixFDSrc1";
	setAttr ".t" -type "double3" -8.8808658795896953 -1.7763568394002505e-015 -2.4809568839000811 ;
	setAttr ".s" -type "double3" 2.2000000476837158 2.2000000476837158 2.2000000476837158 ;
createNode PhoenixFDSource -n "PhoenixFDSource1" -p "PhoenixFDSrc1";
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
	setAttr ".grs" 0;
	setAttr ".gre" 125;
	setAttr ".rt" 0;
	setAttr ".rv" no;
	setAttr ".vf" 1;
	setAttr ".mb" yes;
	setAttr ".vir" no;
	setAttr ".vif" no;
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
	setAttr ".uwo" no;
	setAttr ".lp" -type "double3" 0 0 0 ;
	setAttr ".los" -type "double3" 1 1 1 ;
	setAttr ".mode" 0;
	setAttr ".dc" 5;
	setAttr ".dcm" 1;
	setAttr ".tp" 1;
	setAttr ".tpm" 1;
	setAttr ".sm" 0;
	setAttr ".smm" 1;
	setAttr ".uvm" 0;
	setAttr ".uv" -type "float3" 0 0 0 ;
	setAttr ".fl" 1;
	setAttr ".flm" 1;
	setAttr ".vl" 2;
	setAttr ".prt" 100;
	setAttr ".prtm" 1;
	setAttr ".noise" 0;
	setAttr ".utp" yes;
	setAttr ".usm" no;
	setAttr ".uuv" no;
	setAttr ".ufl" no;
	setAttr ".uvl" yes;
	setAttr ".uprt" no;
	setAttr ".ins" 0;
	setAttr ".tb" 1;
	setAttr ".pt" 0;
	setAttr ".ups" no;
	setAttr ".ls" 1;
	setAttr ".lc" -type "float3" 1 0 0 ;
	setAttr ".mt" -type "float3" 0 0 0 ;
	setAttr ".mod[0].ms" 0;
	setAttr ".mod[0].mro" 0;
	setAttr ".mod[0].mrs" 1;
	setAttr ".mod[0].ma" 0;
	setAttr ".mod[0].msp" 1;
	setAttr ".mod[0].mrv" 1;
createNode transform -n "PhoenixFDSrc2";
	setAttr ".t" -type "double3" -3.4668266954823483 0 -2.4374135792272629 ;
	setAttr ".s" -type "double3" 2.2999999523162842 2.2999999523162842 2.2999999523162842 ;
createNode PhoenixFDSource -n "PhoenixFDSource2" -p "PhoenixFDSrc2";
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
	setAttr ".grs" 0;
	setAttr ".gre" 125;
	setAttr ".rt" 0;
	setAttr ".rv" no;
	setAttr ".vf" 1;
	setAttr ".mb" yes;
	setAttr ".vir" no;
	setAttr ".vif" no;
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
	setAttr ".uwo" no;
	setAttr ".lp" -type "double3" 0 0 0 ;
	setAttr ".los" -type "double3" 1 1 1 ;
	setAttr ".mode" 0;
	setAttr ".dc" 0.0010000000474974513;
	setAttr ".dcm" 1;
	setAttr ".tp" 1;
	setAttr ".tpm" 1;
	setAttr ".sm" 0;
	setAttr ".smm" 1;
	setAttr ".uvm" 0;
	setAttr ".uv" -type "float3" 0 0 0 ;
	setAttr ".fl" 1;
	setAttr ".flm" 1;
	setAttr ".vl" 1;
	setAttr ".prt" 100;
	setAttr ".prtm" 1;
	setAttr ".noise" 0;
	setAttr ".utp" yes;
	setAttr ".usm" no;
	setAttr ".uuv" no;
	setAttr ".ufl" no;
	setAttr ".uvl" yes;
	setAttr ".uprt" no;
	setAttr ".ins" 2;
	setAttr ".tb" 1;
	setAttr ".pt" 0;
	setAttr ".ups" no;
	setAttr ".ls" 1;
	setAttr ".lc" -type "float3" 0 0 1 ;
	setAttr ".mt" -type "float3" 0 0 0 ;
	setAttr ".mod[0].ms" 0;
	setAttr ".mod[0].mro" 0;
	setAttr ".mod[0].mrs" 1;
	setAttr ".mod[0].ma" 0;
	setAttr ".mod[0].msp" 1;
	setAttr ".mod[0].mrv" 1;
createNode transform -s -n "vrayEnvironmentPreviewTm";
createNode VRayEnvironmentPreview -s -n "vrayEnvironmentPreview" -p "vrayEnvironmentPreviewTm";
	setAttr -k off ".v";
createNode transform -n "transform9";
createNode VRaySunTarget -n "VRaySunTarget1" -p "transform9";
	setAttr -k off ".v";
createNode VRayGeoSun -n "VRayGeoSun1" -p "transform9";
	setAttr ".t" -type "double3" -3.6335276896157467 17.200969975611393 -9.0609372233342533 ;
	setAttr ".gyear" 2011;
	setAttr ".gmonth" 7;
	setAttr ".gday" 11;
	setAttr ".gdvalue" 192;
	setAttr ".gtvalue" 12;
createNode VRaySunShape -n "VRaySunShape1" -p "VRayGeoSun1";
	setAttr -k off ".v";
createNode transform -n "pPlane1";
	setAttr ".t" -type "double3" 4.8152441218414301 0 0.96508711511647605 ;
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
	setAttr ".bnr" 0;
createNode transform -n "directionalLight1";
	setAttr ".r" -type "double3" 47.572263595190769 0 0 ;
createNode directionalLight -n "directionalLightShape1" -p "directionalLight1";
	setAttr -k off ".v";
	setAttr ".in" 70;
createNode transform -n "PhoenixFDFm1";
	setAttr ".t" -type "double3" -3.8736958819147462 1.7763568394002505e-015 0.74392915596298614 ;
	setAttr ".s" -type "double3" 2.5 2.5 2.5 ;
createNode PhoenixFDFoam -n "PhoenixFDFoam1" -p "PhoenixFDFm1";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".mod" 2;
	setAttr ".mob" 1;
	setAttr ".eme" yes;
	setAttr ".lc" -type "float3" 0 0 1 ;
	setAttr ".aal" -type "attributeAlias" {"rendGizmo","gizmo"} ;
createNode transform -n "pCube2";
	setAttr ".tmp" yes;
	setAttr ".t" -type "double3" 4.8 5 0.1 ;
createNode mesh -n "pCubeShape2" -p "pCube2";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".bnr" 0;
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 5 ".lnk";
	setAttr -s 5 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode objectSet -n "set1";
createNode objectSet -n "set2";
	setAttr -s 2 ".dsm";
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n"
		+ "                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n"
		+ "            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n"
		+ "            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n"
		+ "            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n"
		+ "                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n"
		+ "                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n"
		+ "                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n"
		+ "            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n"
		+ "            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n"
		+ "                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n"
		+ "                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n"
		+ "            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n"
		+ "            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n"
		+ "                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n"
		+ "                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n"
		+ "                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n"
		+ "            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -showShapes 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n"
		+ "                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n"
		+ "            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n"
		+ "                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n"
		+ "                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n"
		+ "                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n"
		+ "                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n"
		+ "                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n"
		+ "                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n"
		+ "                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n"
		+ "                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n"
		+ "                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n"
		+ "                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n"
		+ "                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n"
		+ "                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\tif ($useSceneConfig) {\n\t\tscriptedPanel -e -to $panelName;\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n"
		+ "                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n"
		+ "                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                $editorName;\nstereoCameraView -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n"
		+ "                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n"
		+ "                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -shadows 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                $editorName;\nstereoCameraView -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"multiListerPanel\" (localizedPanelLabel(\"Multilister\")) `;\n"
		+ "\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"multiListerPanel\" -l (localizedPanelLabel(\"Multilister\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Multilister\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"devicePanel\" (localizedPanelLabel(\"Devices\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tdevicePanel -unParent -l (localizedPanelLabel(\"Devices\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tdevicePanel -edit -l (localizedPanelLabel(\"Devices\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n"
		+ "\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 150 -ast 1 -aet 150 ";
	setAttr ".st" 6;
createNode polyCylinder -n "polyCylinder1";
	setAttr ".r" 1.1;
	setAttr ".h" 14;
	setAttr ".sc" 1;
	setAttr ".cuv" 3;
createNode polyBoolOp -n "polyBoolOp1";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".im";
	setAttr ".op" 2;
	setAttr ".uth" yes;
createNode groupId -n "groupId1";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts1";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0:59]";
createNode groupId -n "groupId2";
	setAttr ".ihi" 0;
createNode groupId -n "groupId3";
	setAttr ".ihi" 0;
createNode groupId -n "groupId4";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0:79]";
createNode polyCube -n "polyCube1";
	setAttr ".w" 89.379167169221049;
	setAttr ".h" 17.046178156786631;
	setAttr ".d" 25.605765047592143;
	setAttr ".cuv" 4;
createNode polyBoolOp -n "polyBoolOp2";
	setAttr -s 2 ".ip";
	setAttr -s 2 ".im";
	setAttr ".op" 3;
	setAttr ".uth" yes;
createNode groupId -n "groupId6";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0:5]";
createNode groupId -n "groupId7";
	setAttr ".ihi" 0;
createNode groupId -n "groupId8";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0:49]";
createNode polyCylinder -n "polyCylinder2";
	setAttr ".r" 0.6;
	setAttr ".sc" 1;
	setAttr ".cuv" 3;
createNode blinn -n "blinn1";
	setAttr ".it" -type "float3" 1 1 1 ;
createNode shadingEngine -n "blinn1SG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
createNode groupId -n "groupId9";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts5";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[0:39]";
	setAttr ".irc" -type "componentList" 1 "f[40:59]";
createNode groupId -n "groupId10";
	setAttr ".ihi" 0;
createNode groupId -n "groupId11";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts6";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "f[40:59]";
createNode objectSet -n "set3";
createNode objectSet -n "set4";
createNode VRaySettingsNode -s -n "vraySettings";
	setAttr ".aafon" no;
	setAttr ".fsd" 4;
	setAttr ".dma" 6;
	setAttr ".smi" 0;
	setAttr ".tre" 0.40000000596046448;
	setAttr ".snot" 0.4;
	setAttr ".icits" 10;
	setAttr ".caoet" yes;
	setAttr ".vrscfile" -type "string" "c:/phx_cascade.vrscene";
	setAttr ".srgx" 32;
	setAttr ".srgy" 32;
	setAttr ".sltp" yes;
	setAttr ".wi" 1280;
	setAttr ".he" 720;
	setAttr ".aspr" 1.7769999504089355;
	setAttr ".aspl" no;
	setAttr ".bkc" -type "string" "map1";
	setAttr ".vfbOn" yes;
	setAttr ".vfbSA" -type "Int32Array" 198 786 10 297 49 1455 1092
		 1600 145 10 145 8406785 1 0 0 0 593 282 158
		 197 63 706 1 1 1 0 0 0 0 1 0
		 5 0 1065353216 1 1 2 1065353216 1065353216 1065353216 1065353216 1 0
		 5 0 0 0 0 1 0 5 0 1065353216 1 137531
		 65536 1 1313131313 65536 944879383 0 -525502228 1065353216 1621981420 1034147594 1053609164 1065353216
		 2 0 0 -1097805629 -1097805629 1049678019 1049678019 0 2 1065353216 1065353216 -1097805629
		 -1097805629 1049678019 1049678019 0 2 1 2 -1 0 0 0 1869111636
		 822108525 538996316 1630347296 1164932213 1851879544 1546657892 538976366 1752378656 1631876975 1819168615 1546723449 538976366
		 1752378656 1933670255 1937007987 1851535648 538976288 1869116205 1852785527 1852399988 1850696805 824211820 538996316 1932337184
		 16777215 0 70 1 32 53 1632775510 1868963961 1632444530 622879097 2036429430 1936876918
		 544108393 1701978236 1919247470 1835627552 1915035749 1701080677 1835627634 12901 1378702848 1713404257 1293972079 543258977
		 892350003 540094510 1701978236 1919247470 1835627552 807411813 807411816 959520877 7551278 16777216 16777216 0
		 0 0 0 1 1 0 0 0 0 11 1936614732 1701209669
		 7566435 1 0 1 0 1101004800 1101004800 1082130432 0 0 0 1077936128
		 0 0 0 1 0 0 1112014848 1101004800 1 0 0 0
		 0 82176 0 16576 0 0 0 0 16448 0 65536 65536 ;
	setAttr ".stampOn" yes;
	setAttr ".mSceneName" -type "string" "C:/source/svn/Aura2/Maya/samples/phx_cascade2.ma";
createNode VRayMtl -n "VRayMtl1";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".dc" -type "float3" 0.5 0.36860001 0.1715 ;
	setAttr ".aal" -type "attributeAlias" {"color","diffuseColor","transparency","opacityMap"
		} ;
createNode shadingEngine -n "VRayMtl1SG";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
createNode VRayMtl -n "vraymtl_water_VRayMtl1";
	addAttr -ci true -h true -sn "aal" -ln "attributeAliasList" -dt "attributeAlias";
	setAttr ".dc" -type "float3" 0 0 0 ;
	setAttr ".rlc" -type "float3" 1 1 1 ;
	setAttr ".rlec" -type "float3" 1 1 1 ;
	setAttr ".hlgl" no;
	setAttr ".hlg" 0.8399999737739563;
	setAttr ".uf" yes;
	setAttr ".rrc" -type "float3" 1 1 1 ;
	setAttr ".rior" 1.3300000429153442;
	setAttr ".fc" -type "float3" 0.75686276 0.85490197 0.85490197 ;
	setAttr ".fmu" 0.05000000074505806;
	setAttr ".afs" yes;
	setAttr ".aal" -type "attributeAlias" {"color","diffuseColor","transparency","opacityMap"
		} ;
createNode shadingEngine -n "vraymtl_water_VRayMtl1SG";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
createNode VRaySky -n "VRaySky1";
createNode VRayRenderElement -n "vrayRE_Caustics";
	addAttr -ci true -sn "vrayClassType" -ln "vrayClassType" -dt "string";
	addAttr -ci true -k true -sn "enabled" -ln "enabled" -dv 1 -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "vray_alias_caustics" -ln "vray_alias_caustics" -dv 109 -at "long";
	addAttr -ci true -sn "vray_name_caustics" -ln "vray_name_caustics" -dt "string";
	addAttr -ci true -sn "vray_colorMapping_caustics" -ln "vray_colorMapping_caustics" 
		-dv 1 -at "long";
	setAttr ".vrayClassType" -type "string" "causticsChannel";
	setAttr ".vray_name_caustics" -type "string" "caustics";
createNode polyPlane -n "polyPlane1";
	setAttr ".w" 8;
	setAttr ".h" 6;
	setAttr ".sw" 1;
	setAttr ".sh" 1;
	setAttr ".cuv" 2;
createNode objectSet -n "phxfoam_set1";
createNode polyCube -n "polyCube2";
	setAttr ".w" 7.4;
	setAttr ".h" 10;
	setAttr ".d" 3.7;
	setAttr ".cuv" 4;
createNode PhoenixFDPGroup -n "PG_PhoenixFDSimulator2_Splashes_0";
	setAttr ".gn" -type "string" "Splashes";
createNode PhoenixFDPGroup -n "PG_PhoenixFDSimulator2_Foam_0";
	setAttr ".gn" -type "string" "Foam";
createNode objectSet -n "phxfoam_set2";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 63;
	setAttr ".unw" 63;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 12 ".dsm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
	setAttr -s 10 ".gn";
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -av ".micc";
	setAttr -cb on ".mica";
	setAttr -cb on ".micw";
	setAttr -cb on ".mirw";
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
	setAttr -cb on ".mimt";
	setAttr -cb on ".miop";
	setAttr -cb on ".mise";
	setAttr -cb on ".mism";
	setAttr -cb on ".mice";
	setAttr -cb on ".micc";
	setAttr -cb on ".mica";
	setAttr -cb on ".micw";
	setAttr -cb on ".mirw";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".s";
select -ne :defaultTextureList1;
select -ne :lightList1;
	setAttr -s 3 ".l";
select -ne :lambert1;
	setAttr ".c" -type "float3" 0.26100001 0.52200001 0.26100001 ;
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
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
	setAttr -k on ".be";
	setAttr -k on ".fec";
	setAttr -k on ".ofc";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av ".sp";
	setAttr -k on ".shs";
	setAttr -k on ".lpr";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".shp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -av ".bll";
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
select -ne :defaultResolution;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr -av ".w" 1280;
	setAttr -av ".h" 720;
	setAttr -av ".pa" 0.99956250190734863;
	setAttr -k on ".al";
	setAttr -av ".dar" 1.7769999504089355;
	setAttr -k on ".off";
	setAttr -k on ".fld";
	setAttr -k on ".zsl";
select -ne :defaultLightSet;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -s 3 ".dsm";
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
	setAttr -k off ".mbbf";
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
connectAttr "set1.ub[0]" "PhoenixFDSimulator1.us";
connectAttr ":time1.o" "PhoenixFDSimulator1.ct";
connectAttr "pCubeShape2.msg" "PhoenixFDSimulator1.gizmo";
connectAttr "set2.ub[0]" "PhoenixFDSimulator2.us";
connectAttr ":time1.o" "PhoenixFDSimulator2.ct";
connectAttr "pCubeShape2.msg" "PhoenixFDSimulator2.gizmo";
connectAttr "groupId1.id" "pCylinderShape1.iog.og[1].gid";
connectAttr ":initialShadingGroup.mwc" "pCylinderShape1.iog.og[1].gco";
connectAttr "groupParts1.og" "pCylinderShape1.i";
connectAttr "groupId2.id" "pCylinderShape1.ciog.cog[1].cgid";
connectAttr "groupId3.id" "pCylinderShape2.iog.og[1].gid";
connectAttr ":initialShadingGroup.mwc" "pCylinderShape2.iog.og[1].gco";
connectAttr "groupId4.id" "pCylinderShape2.ciog.cog[1].cgid";
connectAttr "groupParts2.og" "polySurfaceShape1.i";
connectAttr "groupId5.id" "polySurfaceShape1.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "polySurfaceShape1.iog.og[0].gco";
connectAttr "groupId6.id" "pCubeShape1.iog.og[1].gid";
connectAttr ":initialShadingGroup.mwc" "pCubeShape1.iog.og[1].gco";
connectAttr "groupParts3.og" "pCubeShape1.i";
connectAttr "groupId7.id" "pCubeShape1.ciog.cog[1].cgid";
connectAttr "groupParts4.og" "polySurfaceShape2.i";
connectAttr "groupId8.id" "polySurfaceShape2.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "polySurfaceShape2.iog.og[0].gco";
connectAttr "groupId9.id" "pCylinderShape3.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "pCylinderShape3.iog.og[0].gco";
connectAttr "groupId11.id" "pCylinderShape3.iog.og[1].gid";
connectAttr "blinn1SG.mwc" "pCylinderShape3.iog.og[1].gco";
connectAttr "groupParts6.og" "pCylinderShape3.i";
connectAttr "groupId10.id" "pCylinderShape3.ciog.cog[0].cgid";
connectAttr "set3.ub[0]" "PhoenixFDSource1.ns";
connectAttr "blinn1.oc" "PhoenixFDSource1.mt";
connectAttr "set4.ub[0]" "PhoenixFDSource2.ns";
connectAttr ":vraySettings.caet1" ":vrayEnvironmentPreview.bgt";
connectAttr ":vraySettings.caet2" ":vrayEnvironmentPreview.git";
connectAttr ":vraySettings.caet3" ":vrayEnvironmentPreview.rflt";
connectAttr ":vraySettings.caet4" ":vrayEnvironmentPreview.rfrt";
connectAttr "VRaySunTarget1.src" "VRaySunShape1.trg";
connectAttr "polyPlane1.out" "pPlaneShape1.i";
connectAttr "phxfoam_set1.ub[0]" "PhoenixFDFoam1.pss";
connectAttr "VRaySky1.oc" "PhoenixFDFoam1.em";
connectAttr "PhoenixFDSimulator2.avo" "PhoenixFDFoam1.lg";
connectAttr "polyCube2.out" "pCubeShape2.i";
relationship "link" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "VRayMtl1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "vraymtl_water_VRayMtl1SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "VRayMtl1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "vraymtl_water_VRayMtl1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "PhoenixFDSim2.iog" "set1.dsm" -na;
connectAttr "PhoenixFDSrc1.iog" "set2.dsm" -na;
connectAttr "PhoenixFDSim1.iog" "set2.dsm" -na;
connectAttr "pCylinderShape1.o" "polyBoolOp1.ip[0]";
connectAttr "pCylinderShape2.o" "polyBoolOp1.ip[1]";
connectAttr "pCylinderShape1.wm" "polyBoolOp1.im[0]";
connectAttr "pCylinderShape2.wm" "polyBoolOp1.im[1]";
connectAttr "polyCylinder1.out" "groupParts1.ig";
connectAttr "groupId1.id" "groupParts1.gi";
connectAttr "polyBoolOp1.out" "groupParts2.ig";
connectAttr "groupId5.id" "groupParts2.gi";
connectAttr "pCubeShape1.o" "polyBoolOp2.ip[0]";
connectAttr "polySurfaceShape1.o" "polyBoolOp2.ip[1]";
connectAttr "pCubeShape1.wm" "polyBoolOp2.im[0]";
connectAttr "polySurfaceShape1.wm" "polyBoolOp2.im[1]";
connectAttr "polyCube1.out" "groupParts3.ig";
connectAttr "groupId6.id" "groupParts3.gi";
connectAttr "polyBoolOp2.out" "groupParts4.ig";
connectAttr "groupId8.id" "groupParts4.gi";
connectAttr "blinn1.oc" "blinn1SG.ss";
connectAttr "groupId11.msg" "blinn1SG.gn" -na;
connectAttr "pCylinderShape3.iog.og[1]" "blinn1SG.dsm" -na;
connectAttr "blinn1SG.msg" "materialInfo1.sg";
connectAttr "blinn1.msg" "materialInfo1.m";
connectAttr "polyCylinder2.out" "groupParts5.ig";
connectAttr "groupId9.id" "groupParts5.gi";
connectAttr "groupParts5.og" "groupParts6.ig";
connectAttr "groupId11.id" "groupParts6.gi";
connectAttr "pCylinder3.iog" "set3.dsm" -na;
connectAttr "PhoenixFDSim1.iog" "set4.dsm" -na;
connectAttr "VRaySky1.oc" ":vraySettings.caet1";
connectAttr "VRaySky1.oc" ":vraySettings.caet2";
connectAttr "VRaySky1.oc" ":vraySettings.caet3";
connectAttr "VRaySky1.oc" ":vraySettings.caet4";
connectAttr "VRayMtl1.oc" "VRayMtl1SG.ss";
connectAttr "VRayMtl1SG.msg" "materialInfo2.sg";
connectAttr "VRayMtl1.msg" "materialInfo2.m";
connectAttr "vraymtl_water_VRayMtl1.oc" "vraymtl_water_VRayMtl1SG.ss";
connectAttr "PhoenixFDSimulator2.iog" "vraymtl_water_VRayMtl1SG.dsm" -na;
connectAttr "PhoenixFDSimulator1.iog" "vraymtl_water_VRayMtl1SG.dsm" -na;
connectAttr "vraymtl_water_VRayMtl1SG.msg" "materialInfo3.sg";
connectAttr "vraymtl_water_VRayMtl1.msg" "materialInfo3.m";
connectAttr "VRaySunShape1.msg" "VRaySky1.s";
connectAttr "PG_PhoenixFDSimulator2_Splashes_0.msg" "phxfoam_set1.dnsm" -na;
connectAttr "PhoenixFDSimulator2.idc" "PG_PhoenixFDSimulator2_Splashes_0.sdc";
connectAttr "PhoenixFDSimulator2.idc" "PG_PhoenixFDSimulator2_Foam_0.sdc";
connectAttr "PG_PhoenixFDSimulator2_Foam_0.msg" "phxfoam_set2.dnsm" -na;
connectAttr "blinn1SG.pa" ":renderPartition.st" -na;
connectAttr "VRayMtl1SG.pa" ":renderPartition.st" -na;
connectAttr "vraymtl_water_VRayMtl1SG.pa" ":renderPartition.st" -na;
connectAttr "pCylinderShape1.iog.og[1]" ":initialShadingGroup.dsm" -na;
connectAttr "pCylinderShape1.ciog.cog[1]" ":initialShadingGroup.dsm" -na;
connectAttr "pCylinderShape2.iog.og[1]" ":initialShadingGroup.dsm" -na;
connectAttr "pCylinderShape2.ciog.cog[1]" ":initialShadingGroup.dsm" -na;
connectAttr "polySurfaceShape1.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "pCubeShape1.iog.og[1]" ":initialShadingGroup.dsm" -na;
connectAttr "pCubeShape1.ciog.cog[1]" ":initialShadingGroup.dsm" -na;
connectAttr "polySurfaceShape2.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "pCylinderShape3.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "pCylinderShape3.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "pPlaneShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "pCubeShape2.iog" ":initialShadingGroup.dsm" -na;
connectAttr "groupId1.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId2.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId4.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId5.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId6.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId7.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId8.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId9.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId10.msg" ":initialShadingGroup.gn" -na;
connectAttr "blinn1.msg" ":defaultShaderList1.s" -na;
connectAttr "VRayMtl1.msg" ":defaultShaderList1.s" -na;
connectAttr "vraymtl_water_VRayMtl1.msg" ":defaultShaderList1.s" -na;
connectAttr "VRaySky1.msg" ":defaultTextureList1.tx" -na;
connectAttr "VRaySunShape1.ltd" ":lightList1.l" -na;
connectAttr "VRaySunTarget1.msg" ":lightList1.l" -na;
connectAttr "directionalLightShape1.ltd" ":lightList1.l" -na;
connectAttr "VRayGeoSun1.iog" ":defaultLightSet.dsm" -na;
connectAttr "transform9.iog" ":defaultLightSet.dsm" -na;
connectAttr "directionalLight1.iog" ":defaultLightSet.dsm" -na;
// End of phx_cascade2.ma
