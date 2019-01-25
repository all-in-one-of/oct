//Maya ASCII 2012 scene
//Name: phx_clouds.ma
//Last modified: Mon, Sep 28, 2015 11:26:25 am
//Codeset: UTF-8
requires maya "2012";
requires "vrayformaya" "3.15.01";
requires "phoenixfd" "2.2.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "201103110020-796618";
fileInfo "osv" "Linux 3.10.0-229.1.2.el7.x86_64 #1 SMP Fri Mar 27 03:04:26 UTC 2015 x86_64";
createNode transform -s -n "persp";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -120.00998047710877 50.144529108069186 99.758292151821834 ;
	setAttr ".r" -type "double3" -13.538352729607709 -49.800000000001234 0 ;
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
		-min 9.9999997473787516e-05 -smx 180 -at "float";
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
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 177.7809344548422;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".vrayCameraPhysicalOn" 1;
	setAttr ".vrayCameraPhysicalFocalLength" 34.324321746826172;
	setAttr ".vrayCameraPhysicalFOV" 54.432220458984375;
	setAttr ".vrayCameraPhysicalLensFile" -type "string" "";
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
	setAttr ".t" -type "double3" 0 0 100.1 ;
createNode camera -s -n "frontShape" -p "front";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 100.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 100.1 0 0 ;
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
	setAttr ".gre" 100;
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
	setAttr ".ver" 21;
	setAttr ".ct" 16;
	setAttr ".ui" 0;
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
	setAttr ".objvs" no;
	setAttr ".fcal" 0;
	setAttr ".fsk" 0;
	setAttr ".fmt" no;
	setAttr ".cm" 0;
	setAttr ".cfl" 0;
	setAttr ".cfi" 0;
	setAttr ".cq" 20;
	setAttr ".cun" yes;
	setAttr ".adm" 0;
	setAttr ".ams" 1000;
	setAttr ".spf1" 2;
	setAttr ".spf2" 2;
	setAttr ".spf3" 2;
	setAttr ".as" no;
	setAttr ".dc" no;
	setAttr ".fs" no;
	setAttr ".rs" no;
	setAttr ".rsf" 0;
	setAttr ".ref" 0;
	setAttr ".rswm" no;
	setAttr ".rsi" -type "string" "$(simoutput)";
	setAttr ".rso" -type "string" "$(implicit)";
	setAttr ".rsor" -type "string" "/home/yordan/PhoenixSamples/data/phx_clouds.ma_Phoenix2_frames/@PhoenixFDSim1@PhoenixFDSimulator1_resim_####.aur";
	setAttr ".rsir" -type "string" "/home/yordan/PhoenixSamples/data/phx_clouds.ma_Phoenix2_frames/@PhoenixFDSim1@PhoenixFDSimulator1_####.aur";
	setAttr ".rsaf" 0;
	setAttr ".rstc" 0;
	setAttr ".rsa" 1;
	setAttr ".rsam" 2;
	setAttr ".wvs" 3;
	setAttr ".wvc" 0.0010000000474974513;
	setAttr ".rsgtb" no;
	setAttr ".rsgtbm" 0;
	setAttr ".lgr" yes;
	setAttr ".mun" 0;
	setAttr ".uns" 2;
	setAttr ".xsz" 203;
	setAttr ".ysz" 168;
	setAttr ".zsz" 60;
	setAttr ".bx" 0;
	setAttr ".by" 0;
	setAttr ".bz" 0;
	setAttr ".gpa" 1;
	setAttr ".lby" 1;
	setAttr ".lto" 90;
	setAttr ".ag" 0;
	setAttr ".gt" 1000;
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
	setAttr ".csz" 0.512;
	setAttr ".wfmv" 1;
	setAttr ".wfm" yes;
	setAttr ".egr" yes;
	setAttr ".gr" 1;
	setAttr ".egrv" no;
	setAttr ".tsc" 1;
	setAttr ".vmv" no;
	setAttr ".vrt" 0.20000000298023224;
	setAttr ".vrtsrfsm" 0.30000001192092896;
	setAttr ".vrtsrft" 0.10000000149011612;
	setAttr ".vrtlow" 0.30000001192092896;
	setAttr ".pd" 0;
	setAttr ".cool" 0;
	setAttr ".smdiss" 0;
	setAttr ".sb" 0;
	setAttr ".fb" 0;
	setAttr ".fmm" -1;
	setAttr ".ra" 1;
	setAttr ".rd" 1;
	setAttr ".rij" yes;
	setAttr ".grv" -type "float3" 0 -9.8000002 0 ;
	setAttr ".brn" no;
	setAttr ".be" 10;
	setAttr ".big" 600;
	setAttr ".bp" 10;
	setAttr ".liq" no;
	setAttr ".lqsteps" 1;
	setAttr ".lqsharpness" 0.5;
	setAttr ".lqad" 0;
	setAttr ".lqsurft" 0;
	setAttr ".lqvisc" 0;
	setAttr ".nonnewt" 0;
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
	setAttr ".hlvary" no;
	setAttr ".foutlife" 0;
	setAttr ".fsize" 0.10000000149011612;
	setAttr ".fsizevar" 3;
	setAttr ".fszdstrb" 200;
	setAttr ".fshrink" 0;
	setAttr ".fcycles" 3000;
	setAttr ".frise" 10;
	setAttr ".ffall" 1000;
	setAttr ".fsticky" 0;
	setAttr ".fptrn" 0;
	setAttr ".fptrnsz" 10;
	setAttr ".fmvel" no;
	setAttr ".fmid" no;
	setAttr ".fmage" no;
	setAttr ".splashes" no;
	setAttr ".spbirth" 5;
	setAttr ".spbthres" 60;
	setAttr ".REYNOLDS" 60;
	setAttr ".spsize" 0.05000000074505806;
	setAttr ".spsizevar" 5;
	setAttr ".spszdstrb" 100;
	setAttr ".spshrink" 0;
	setAttr ".airfr" 1;
	setAttr ".sp2foam" 0;
	setAttr ".spfohminage" 0;
	setAttr ".fohdepth" 1;
	setAttr ".affectlq" 0;
	setAttr ".spto" 0;
	setAttr ".vmult" 1;
	setAttr ".spsplit" 0;
	setAttr ".spstick" 0;
	setAttr ".spvel" no;
	setAttr ".spid" no;
	setAttr ".spage" no;
	setAttr ".sq" 14;
	setAttr ".bi" -1;
	setAttr ".ci" no;
	setAttr ".ot" yes;
	setAttr ".osm" no;
	setAttr ".ou" no;
	setAttr ".ow" no;
	setAttr ".osp" no;
	setAttr ".ov" no;
	setAttr ".of" no;
	setAttr ".opi" no;
	setAttr ".opa" no;
	setAttr ".opth" -type "string" "$(implicit)";
	setAttr ".opthr" -type "string" "/home/yordan/PhoenixSamples/data/phx_clouds.ma_Phoenix2_frames/@PhoenixFDSim1@PhoenixFDSimulator1_####.aur";
	setAttr ".prtcmp" yes;
	setAttr ".ipref" yes;
	setAttr ".ipth" -type "string" "$(simoutput)";
	setAttr ".ipthr" -type "string" "/home/yordan/PhoenixSamples/data/phx_clouds.ma_Phoenix2_frames/@PhoenixFDSim1@PhoenixFDSimulator1_####.aur";
	setAttr ".inm" 0;
	setAttr ".t2f" 1;
	setAttr ".iro" 0;
	setAttr ".iml" 0;
	setAttr ".ipa" 0;
	setAttr ".il" 0;
	setAttr ".play_speed" 1;
	setAttr ".ibm" 0;
	setAttr ".ifyz" no;
	setAttr ".iln" no;
	setAttr ".itse" no;
	setAttr ".isse" no;
	setAttr ".iwse" no;
	setAttr ".ifse" no;
	setAttr ".ivse" no;
	setAttr ".usrchmap" -type "string" "";
	setAttr ".its" -type "float3" 0 0.5 0.1 ;
	setAttr ".isms" -type "float3" 0 0.5 0.1 ;
	setAttr ".iws" -type "float3" 0 0.5 0.1 ;
	setAttr ".ifs" -type "float3" 0 0.5 0.1 ;
	setAttr ".ivs" -type "float3" 0 0.5 0.1 ;
	setAttr ".iel" yes;
	setAttr ".ieh" no;
	setAttr ".irl" yes;
	setAttr ".sg" yes;
	setAttr ".sgs" no;
	setAttr ".ois" no;
	setAttr ".avo" yes;
	setAttr ".cr" 100;
	setAttr ".andr" no;
	setAttr ".vt" yes;
	setAttr ".vtn" no;
	setAttr ".vtc" -type "float3" 0 0 0 ;
	setAttr ".vtc2" -type "float3" 1 0 0 ;
	setAttr ".vtt" 350;
	setAttr ".vtt2" 600;
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
	setAttr ".vspc" -type "float3" 0 0 1 ;
	setAttr ".vspce" yes;
	setAttr ".vprtc" -type "float3" 1 0 0 ;
	setAttr ".vprtce" yes;
	setAttr ".vprts" 1;
	setAttr ".gve" no;
	setAttr ".gvd" 1;
	setAttr ".gvg" 2.2000000476837158;
	setAttr ".gvge" no;
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
	setAttr ".vm" no;
	setAttr ".vmd" no;
	setAttr ".vmc" -type "float3" 0.22 0.22 0.94999999 ;
	setAttr ".vma" 1;
	setAttr ".vmas" no;
	setAttr ".rend" yes;
	setAttr ".jitter" yes;
	setAttr ".rendstep" 70;
	setAttr ".rendshadstep" 200;
	setAttr ".softb" 0;
	setAttr ".rvmult" 1;
	setAttr ".sampler" 2;
	setAttr ".sarg" 1;
	setAttr ".ret" -type "float3" 0 0 0 ;
	setAttr ".wrapx" 2;
	setAttr ".wrapy" 2;
	setAttr ".wrapz" 2;
	setAttr ".meshType" 0;
	setAttr ".oceanlevel" 50;
	setAttr ".ocean" no;
	setAttr ".smoothmesh" 5;
	setAttr ".meshsubdiv" 2;
	setAttr ".rsl_x" 0.5;
	setAttr ".rsl_t" 1000;
	setAttr ".rsl_s" 0.5;
	setAttr ".rsl_v" 20;
	setAttr ".rsl_f" 0.10000000149011612;
	setAttr ".solidbelow" no;
	setAttr ".geommode" no;
	setAttr ".hhfactor" 1;
	setAttr ".heathaze" 1;
	setAttr ".rendsolid" no;
	setAttr ".rendMode" 0;
	setAttr ".probabilistic" 1;
	setAttr ".bias" 1;
	setAttr ".usebias" no;
	setAttr ".uvwmb" no;
	setAttr ".displacement" yes;
	setAttr ".displmul" 2;
	setAttr ".displ2d" 1;
	setAttr ".displ0" -type "float3" 0 0 0 ;
	setAttr ".displ1" -type "float3" 0 0 0 ;
	setAttr ".displ2" -type "float3" 0.31146249 0.31146249 0.31146249 ;
	setAttr ".mid" -type "float3" 0 0 0 ;
	setAttr ".vn" 0;
	setAttr ".vz" 0;
	setAttr ".usegizmo" no;
	setAttr ".invgizmo" no;
	setAttr ".DIMode_gpu" 2;
	setAttr ".GIMode_gpu" 0;
	setAttr ".gpusamplescnt" 1;
	setAttr ".earg" 0;
	setAttr ".et" -type "float3" 0 0 0 ;
	setAttr ".em" no;
	setAttr ".no_alpha_e" 0;
	setAttr ".etmult" 1;
	setAttr ".al_enable" yes;
	setAttr ".elc" 0;
	setAttr ".elpm" 1;
	setAttr ".elrm" 1;
	setAttr ".elp" no;
	setAttr ".selfshadow" 2;
	setAttr ".elpl" 0;
	setAttr ".al_decay" 2;
	setAttr ".els" 0;
	setAttr ".elsd" 8;
	setAttr ".elcsd" 1000;
	setAttr ".elco" 0.0099999997764825821;
	setAttr ".gridreduct" 5;
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
	setAttr ".simple_color" -type "float3" 0.69590294 0.69590294 0.69590294 ;
	setAttr ".pmbounces" yes;
	setAttr ".lightcache" yes;
	setAttr ".lightcachesr" 0;
	setAttr ".noscatter" 3;
	setAttr ".dsd" 10;
	setAttr ".difmul" 1;
	setAttr ".transfown" 1;
	setAttr ".transfext" 1;
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
	setAttr ".tm" yes;
	setAttr ".transpmode" 1;
	setAttr ".stoptransp" 0.99000000953674316;
	setAttr ".skiptransp" 0.0010000000474974513;
	setAttr ".smoketransp" 0.5;
	setAttr ".trl_t" 100;
	setAttr ".tro_t" 300;
	setAttr ".trm_t" 0.15000000596046448;
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
	setAttr ".ecolor_t[0].ecolor_tc" -type "float3" 1 0.19711408 0.0011649216 ;
	setAttr ".ecolor_t[0].ecolor_ti" 3;
	setAttr ".ecolor_t[1].ecolor_tp" 2000.0010986328125;
	setAttr ".ecolor_t[1].ecolor_tc" -type "float3" 1 0.39821142 0.061485976 ;
	setAttr ".ecolor_t[1].ecolor_ti" 3;
	setAttr -s 2 ".ecolor_s";
	setAttr ".ecolor_s[0].ecolor_sp" 0.55000001192092896;
	setAttr ".ecolor_s[0].ecolor_sc" -type "float3" 1 0.19711408 0.0011649216 ;
	setAttr ".ecolor_s[0].ecolor_si" 3;
	setAttr ".ecolor_s[1].ecolor_sp" 1.0000004768371582;
	setAttr ".ecolor_s[1].ecolor_sc" -type "float3" 1 0.39821142 0.061485976 ;
	setAttr ".ecolor_s[1].ecolor_si" 3;
	setAttr -s 2 ".ecolor_v";
	setAttr ".ecolor_v[0].ecolor_vp" 220;
	setAttr ".ecolor_v[0].ecolor_vc" -type "float3" 1 0.19711408 0.0011649216 ;
	setAttr ".ecolor_v[0].ecolor_vi" 3;
	setAttr ".ecolor_v[1].ecolor_vp" 400.00021362304688;
	setAttr ".ecolor_v[1].ecolor_vc" -type "float3" 1 0.39821142 0.061485976 ;
	setAttr ".ecolor_v[1].ecolor_vi" 3;
	setAttr -s 2 ".ecolor_f";
	setAttr ".ecolor_f[0].ecolor_fp" 0.55000001192092896;
	setAttr ".ecolor_f[0].ecolor_fc" -type "float3" 1 0.19711408 0.0011649216 ;
	setAttr ".ecolor_f[0].ecolor_fi" 3;
	setAttr ".ecolor_f[1].ecolor_fp" 1.0000004768371582;
	setAttr ".ecolor_f[1].ecolor_fc" -type "float3" 1 0.39821142 0.061485976 ;
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
	setAttr -s 14 ".epower_t[0:13]"  1100 25.51508141 3 1161.43823242 79.38175964 3 1226.30786133
		 233.79103088 3 1294.80078125 653.46136475 3 1367.11901855 1737.57226563 3 1443.4765625
		 4405.52978516 3 1524.098999023 10674.27734375 3 1609.22424316 24767.05859375 3 1699.10424805
		 55141.30859375 3 1794.00390625 118026.078125 3 1894.2043457 243318.21875 3 2000.0010986328
		 483980.09375 3 1974.28686523 412181.71875 3 1995.5012207 470705.03125 3;
	setAttr -s 14 ".epower_s[0:13]"  0.55000001 25.51508141 3 0.58071911 79.38175964 
		3 0.61315393 233.79103088 3 0.64740038 653.46136475 3 0.68355954 1737.57226563 3 0.72173828
		 4405.52978516 3 0.7620495 10674.27734375 3 0.80461216 24767.05859375 3 0.84955209
		 55141.30859375 3 0.89700198 118026.078125 3 0.94710219 243318.21875 3 1.000000476837
		 483980.09375 3 0.98714346 412181.71875 3 0.99775058 470705.03125 3;
	setAttr -s 14 ".epower_v[0:13]"  220 25.51508141 3 232.28764343 79.38175964 3 245.26156616
		 233.79103088 3 258.96014404 653.46136475 3 273.42379761 1737.57226563 3 288.6953125
		 4405.52978516 3 304.8197937 10674.27734375 3 321.84484863 24767.05859375 3 339.8208313
		 55141.30859375 3 358.80078125 118026.078125 3 378.84088135 243318.21875 3 400.00021362305
		 483980.09375 3 394.85736084 412181.71875 3 399.10021973 470705.03125 3;
	setAttr -s 14 ".epower_f[0:13]"  0.55000001 25.51508141 3 0.58071911 79.38175964 
		3 0.61315393 233.79103088 3 0.64740038 653.46136475 3 0.68355954 1737.57226563 3 0.72173828
		 4405.52978516 3 0.7620495 10674.27734375 3 0.80461216 24767.05859375 3 0.84955209
		 55141.30859375 3 0.89700198 118026.078125 3 0.94710219 243318.21875 3 1.000000476837
		 483980.09375 3 0.98714346 412181.71875 3 0.99775058 470705.03125 3;
	setAttr -s 3 ".tpower_t[0:2]"  300 0 3 367.82839966 0.15000001 3 400 0.15000001 
		3;
	setAttr -s 9 ".tpower_s[0:8]"  0.14 0 3 0.43599999 0.025 3 0.50319999 0.054000001 
		3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 3 0.74000001 0 3 0.81999999 0.050000001 
		3 0.94 0 3;
	setAttr -s 9 ".tpower_v[0:8]"  90 0 3 278.70001221 0.025 3 321.53997803 0.054000001 
		3 331.73999023 0.1 3 332.25 0.1 1 343.7250061 0 3 472.5 0 3 523.5 0.050000001 3 600
		 0 3;
	setAttr -s 9 ".tpower_f[0:8]"  0.14 0 3 0.43599999 0.025 3 0.50319999 0.054000001 
		3 0.51920003 0.1 3 0.51999998 0.1 1 0.53799999 0 3 0.74000001 0 3 0.81999999 0.050000001 
		3 0.94 0 3;
createNode transform -n "PhoenixFDSrc1";
	setAttr ".t" -type "double3" 55.654113799763742 0 37.370159337463463 ;
	setAttr ".s" -type "double3" 9.1999998092651367 9.1999998092651367 9.1999998092651367 ;
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
	setAttr ".gre" 100;
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
	setAttr ".dc" 40;
	setAttr ".dcm" 1;
	setAttr ".tp" 600;
	setAttr ".tpm" 0.20059457421302795;
	setAttr ".sm" 0;
	setAttr ".smm" 1;
	setAttr ".uv" -type "float3" 0 0 0 ;
	setAttr ".uvm" -type "float3" 0 0 0 ;
	setAttr ".fl" 1;
	setAttr ".flm" 1;
	setAttr ".vl" 1;
	setAttr ".prt" 100;
	setAttr ".prtm" 1;
	setAttr ".prtl" 0;
	setAttr ".prtlr" 0;
	setAttr ".noise" 0;
	setAttr ".utp" yes;
	setAttr ".usm" no;
	setAttr ".uuv" no;
	setAttr ".ufl" no;
	setAttr ".uvl" no;
	setAttr ".uprt" no;
	setAttr ".ins" 0;
	setAttr ".tb" 1;
	setAttr ".pt" 0;
	setAttr ".ups" no;
	setAttr ".mt" -type "float3" 0 0 0 ;
	setAttr ".ls" 1;
	setAttr ".lc" -type "float3" 1 0 0 ;
	setAttr ".mod[0].ms" 0;
	setAttr ".mod[0].mro" 0;
	setAttr ".mod[0].mrs" 1;
	setAttr ".mod[0].ma" 0;
	setAttr ".mod[0].msp" 1;
	setAttr ".mod[0].mrv" 1;
createNode transform -n "pPlane1";
	setAttr ".t" -type "double3" 0 0.1 0 ;
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
createNode transform -n "transform3";
createNode VRaySunTarget -n "VRaySunTarget1" -p "transform3";
	setAttr -k off ".v";
createNode VRayGeoSun -n "VRayGeoSun1" -p "transform3";
	setAttr ".t" -type "double3" -49.484860566854543 121.4863482479973 -33.909219372528668 ;
	setAttr ".gyear" 2011;
	setAttr ".gmonth" 11;
	setAttr ".gday" 28;
	setAttr ".gdvalue" 332;
	setAttr ".gtvalue" 12;
createNode VRaySunShape -n "VRaySunShape1" -p "VRayGeoSun1";
	setAttr -k off ".v";
createNode transform -n "pointLight1" -p "VRayGeoSun1";
	setAttr ".t" -type "double3" 1.1734259556812152 0.29142472200547653 -1.6113556571776741 ;
	setAttr ".r" -type "double3" 78.621645088310274 -31.689312496499511 -69.038651103735276 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
createNode pointLight -n "pointLightShape1" -p "pointLight1";
	setAttr -k off ".v";
	setAttr ".us" no;
createNode place3dTexture -n "place3dTexture1";
	setAttr ".t" -type "double3" 0 8.7995859847221727 38.956082358644494 ;
	setAttr ".s" -type "double3" 10 10 10 ;
createNode place3dTexture -n "place3dTexture2";
	setAttr ".s" -type "double3" 20 20 20 ;
createNode lightLinker -s -n "lightLinker1";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
createNode displayLayer -n "defaultLayer";
createNode renderLayerManager -n "renderLayerManager";
createNode renderLayer -n "defaultRenderLayer";
	setAttr ".g" yes;
createNode objectSet -n "phxsim_set1";
createNode objectSet -n "phxsource_set1";
createNode noise -n "noise1";
	setAttr ".ail" yes;
createNode place2dTexture -n "place2dTexture1";
createNode polyPlane -n "polyPlane1";
	setAttr ".w" 200;
	setAttr ".h" 200;
	setAttr ".sw" 1;
	setAttr ".sh" 1;
	setAttr ".cuv" 2;
createNode script -n "uiConfigurationScriptNode";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"top\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n"
		+ "                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n"
		+ "                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n"
		+ "                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n"
		+ "            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n"
		+ "            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"side\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n"
		+ "                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n"
		+ "                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n"
		+ "                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n"
		+ "            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"front\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n"
		+ "                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n"
		+ "                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n"
		+ "            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `modelPanel -unParent -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            modelEditor -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n"
		+ "                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -rendererName \"base_OpenGL_Renderer\" \n                -colorResolution 256 256 \n                -bumpResolution 512 512 \n"
		+ "                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 1\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n"
		+ "                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n"
		+ "            -bufferMode \"double\" \n            -twoSidedLighting 1\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -maxConstantTransparency 1\n            -rendererName \"base_OpenGL_Renderer\" \n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n"
		+ "            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n"
		+ "            -shadows 0\n            $editorName;\nmodelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `outlinerPanel -unParent -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels `;\n\t\t\t$editorName = $panelName;\n            outlinerEditor -e \n                -docTag \"isolOutln_fromSeln\" \n                -showShapes 0\n                -showAttributes 0\n                -showConnected 0\n                -showAnimCurvesOnly 0\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 1\n                -showAssets 1\n                -showContainedOnly 1\n                -showPublishedAsConnected 0\n                -showContainerContents 1\n                -ignoreDagHierarchy 0\n"
		+ "                -expandConnections 0\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 0\n                -highlightActive 1\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"defaultSetFilter\" \n                -showSetMembers 1\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n"
		+ "                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n"
		+ "            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"graphEditor\" -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n"
		+ "                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n"
		+ "                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n"
		+ "                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dopeSheetPanel\" -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels `;\n"
		+ "\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n"
		+ "                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n"
		+ "                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showContainerContents 0\n"
		+ "                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n"
		+ "                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" == $panelName) {\n"
		+ "\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"clipEditorPanel\" -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n"
		+ "                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"sequenceEditorPanel\" -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperGraphPanel\" -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n"
		+ "                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n"
		+ "            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"hyperShadePanel\" -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"visorPanel\" -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Texture Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"polyTexturePlacementPanel\" -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Texture Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"renderWindowPanel\" -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"blendShapePanel\" (localizedPanelLabel(\"Blend Shape\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tblendShapePanel -unParent -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tblendShapePanel -edit -l (localizedPanelLabel(\"Blend Shape\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynRelEdPanel\" -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"relationshipPanel\" -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"referenceEditorPanel\" -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"componentEditorPanel\" -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"dynPaintScriptedPanelType\" -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"scriptEditorPanel\" -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"VFBPanelType\" (localizedPanelLabel(\"V-Ray Frame Buffer\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"VFBPanelType\" -l (localizedPanelLabel(\"V-Ray Frame Buffer\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"V-Ray Frame Buffer\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"Stereo\" -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels `;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n"
		+ "                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n"
		+ "                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n"
		+ "                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                $editorName;\nstereoCameraView -e -viewSelected 0 $editorName;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n"
		+ "                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -maxConstantTransparency 1\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n"
		+ "                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -shadows 0\n                -displayMode \"centerEye\" \n"
		+ "                -viewColor 0 0 0 1 \n                $editorName;\nstereoCameraView -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"multiListerPanel\" (localizedPanelLabel(\"Multilister\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"multiListerPanel\" -l (localizedPanelLabel(\"Multilister\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Multilister\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"devicePanel\" (localizedPanelLabel(\"Devices\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\tdevicePanel -unParent -l (localizedPanelLabel(\"Devices\")) -mbv $menusOkayInPanels ;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tdevicePanel -edit -l (localizedPanelLabel(\"Devices\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" == $panelName) {\n\t\tif ($useSceneConfig) {\n\t\t\t$panelName = `scriptedPanel -unParent  -type \"createNodePanel\" -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels `;\n\t\t}\n\t} else {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n"
		+ "\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 1\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -maxConstantTransparency 1\\n    -rendererName \\\"base_OpenGL_Renderer\\\" \\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -shadows 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        setFocus `paneLayout -q -p1 $gMainPane`;\n        sceneUIReplacement -deleteRemaining;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 100 -ast 1 -aet 100 ";
	setAttr ".st" 6;
createNode VRaySettingsNode -s -n "vraySettings";
	setAttr ".cfile" -type "string" "";
	setAttr ".cfile2" -type "string" "";
	setAttr ".casf" -type "string" "";
	setAttr ".casf2" -type "string" "";
	setAttr ".st" 2;
	setAttr ".aafon" no;
	setAttr ".dma" 2;
	setAttr ".sji" no;
	setAttr ".fnm" -type "string" "";
	setAttr ".lcfnm" -type "string" "";
	setAttr ".asf" -type "string" "";
	setAttr ".lcasf" -type "string" "";
	setAttr ".icits" 10;
	setAttr ".ifile" -type "string" "";
	setAttr ".ifile2" -type "string" "";
	setAttr ".iasf" -type "string" "";
	setAttr ".iasf2" -type "string" "";
	setAttr ".pmfile" -type "string" "";
	setAttr ".pmfile2" -type "string" "";
	setAttr ".pmasf" -type "string" "";
	setAttr ".pmasf2" -type "string" "";
	setAttr ".cmtp" 1;
	setAttr ".cmao" 1;
	setAttr ".caoet" yes;
	setAttr ".srgx" 32;
	setAttr ".srgy" 32;
	setAttr ".sltp" yes;
	setAttr ".wi" 1280;
	setAttr ".he" 720;
	setAttr ".aspr" 1.7769999504089355;
	setAttr ".animtp" 1;
	setAttr ".animbo" yes;
	setAttr ".bkc" -type "string" "map1";
	setAttr ".vfbOn" yes;
	setAttr ".vfbSA" -type "Int32Array" 198 786 10 180 62 1328 859 1594 124 0 124 8406273
		 1 44 124 0 323 1 314 464 63 706 1 1 1 0 0 0 0 1 0 5 0 1065353216 1 1 2 1065353216
		 1065353216 1065353216 1065353216 1 0 5 0 0 0 0 1 0 5 0 1065353216 1 137531 65536
		 1 1313131313 65536 944879383 0 -525502228 1065353216 1621981420 1034147594 1053609164
		 1065353216 2 0 0 -1097805629 -1097805629 1049678019 1049678019 0 2 1065353216 1065353216
		 -1097805629 -1097805629 1049678019 1049678019 0 2 1 2 8 4 0 0 1394627405 1819043176
		 1735148576 12832 1109536256 0 16 1 1 8 1419870336 0 1 0 1107636736 0 1469456880 0
		 512875776 0 36954717 0 36954709 0 21825896 16777215 0 70 1 32 53 1632775510 1868963961
		 1632444530 622879097 2036429430 1936876918 544108393 1701978236 1919247470 1835627552
		 1915035749 1701080677 1835627634 12901 1378702848 1713404257 1293972079 543258977
		 892350003 540094510 1701978236 1919247470 1835627552 807411813 857743464 808722541
		 7550766 16777216 16777216 0 0 0 0 1 1 0 0 0 0 11 1936614732 1701209669 7566435 1
		 0 1 0 1101004800 1101004800 1082130432 0 0 0 1077936128 0 0 0 1 0 0 1112014848 1101004800
		 1 0 0 0 0 82176 0 16576 0 0 0 0 16448 0 65536 65536 ;
	setAttr ".stampOn" yes;
	setAttr ".mSceneName" -type "string" "/run/media/yordan/6f186643-a9f0-46e8-a587-ef72bdb9ad57/phoenix4maya_tests/phxfd_maya_test/scenes/phx_clouds.ma";
createNode VRaySky -n "VRaySky1";
createNode projection -n "projection1";
	setAttr ".vt1" -type "float2" 0.5 0.5 ;
	setAttr ".vt2" -type "float2" 0.5 0.5 ;
	setAttr ".vt3" -type "float2" 0.5 0.5 ;
createNode ramp -n "ramp1";
	setAttr -s 2 ".cel";
	setAttr ".cel[2].ep" 0.28499999642372131;
	setAttr ".cel[2].ec" -type "float3" 0 0 0 ;
	setAttr ".cel[3].ep" 0.37000000476837158;
	setAttr ".cel[3].ec" -type "float3" 1 1 1 ;
createNode place2dTexture -n "place2dTexture2";
	setAttr ".c" -type "float2" 1 2 ;
	setAttr ".wv" no;
createNode volumeNoise -n "volumeNoise1";
	setAttr ".ra" 1;
	setAttr ".dm" 4;
	setAttr ".fq" 14;
	setAttr ".fr" 1;
	setAttr ".nty" 3;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 16;
	setAttr ".unw" 16;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".dsm";
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
	setAttr -s 2 ".s";
select -ne :defaultTextureList1;
	setAttr -s 5 ".tx";
select -ne :lightList1;
	setAttr -s 3 ".l";
select -ne :lambert1;
	setAttr ".c" -type "float3" 0.30793333 0.59600002 0 ;
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 4 ".u";
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
	setAttr ".ef" 100;
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
	setAttr -av ".pa" 1;
	setAttr -k on ".al" yes;
	setAttr -av ".dar" 1.7769999504089355;
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
connectAttr "phxsim_set1.ub[0]" "PhoenixFDSimulator1.us";
connectAttr "projection1.oc" "PhoenixFDSimulator1.tt";
connectAttr "volumeNoise1.oc" "PhoenixFDSimulator1.displ2";
connectAttr ":time1.o" "PhoenixFDSimulator1.ct";
connectAttr "phxsource_set1.ub[0]" "PhoenixFDSource1.ns";
connectAttr "noise1.oa" "PhoenixFDSource1.tpm";
connectAttr "polyPlane1.out" "pPlaneShape1.i";
connectAttr "VRaySunTarget1.src" "VRaySunShape1.trg";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "pPlane1.iog" "phxsource_set1.dsm" -na;
connectAttr "place2dTexture1.o" "noise1.uv";
connectAttr "place2dTexture1.ofs" "noise1.fs";
connectAttr "VRaySky1.oc" ":vraySettings.caet1";
connectAttr "VRaySky1.oc" ":vraySettings.caet2";
connectAttr "VRaySky1.oc" ":vraySettings.caet3";
connectAttr "VRaySky1.oc" ":vraySettings.caet4";
connectAttr "VRaySunShape1.msg" "VRaySky1.s";
connectAttr "place3dTexture1.wim" "projection1.pm";
connectAttr "ramp1.oc" "projection1.im";
connectAttr "place2dTexture2.o" "ramp1.uv";
connectAttr "place2dTexture2.ofs" "ramp1.fs";
connectAttr "place3dTexture2.wim" "volumeNoise1.pm";
connectAttr "PhoenixFDSimulator1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "pPlaneShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "noise1.msg" ":defaultTextureList1.tx" -na;
connectAttr "VRaySky1.msg" ":defaultTextureList1.tx" -na;
connectAttr "projection1.msg" ":defaultTextureList1.tx" -na;
connectAttr "ramp1.msg" ":defaultTextureList1.tx" -na;
connectAttr "volumeNoise1.msg" ":defaultTextureList1.tx" -na;
connectAttr "VRaySunShape1.ltd" ":lightList1.l" -na;
connectAttr "VRaySunTarget1.msg" ":lightList1.l" -na;
connectAttr "pointLightShape1.ltd" ":lightList1.l" -na;
connectAttr "place2dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place3dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place3dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "VRayGeoSun1.iog" ":defaultLightSet.dsm" -na;
connectAttr "transform3.iog" ":defaultLightSet.dsm" -na;
// End of phx_clouds.ma
