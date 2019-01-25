allNs = mc.ls(type="nurbsCurve")
for myN in allNs:
    myt = mc.listRelatives(myN,p=True)[0]
    if myt.find('master')>=0:
        myTV = mc.xform(myt,q=True,ws=True,t=True)
        rrL = mc.xform(myt, q=True, ro=True)
        ssL = mc.xform(myt, q=True, r=True, s=True)
        myBall = mc.polySphere()
        mc.xform(myBall,t=myTV)
        mc.xform(myBall, ro=(rrL[0], rrL[1], rrL[2]))
        mc.xform(myBall, s=(ssL[0], ssL[1], ssL[2]))


    PROJECT_PATH = "\\octvision.com\cg"
allTexFiles = mc.ls(type='file')
if allTexFiles:
    for texFile in allTexFiles:
        try:
            texFileName = mc.getAttr('%s.fileTextureName' % texFile)
        except:
            pass
        else:
            if texFileName:
                if texFileName.find('${OCTV_PROJECTS}') >= 0:
                    texFileName = texFileName.replace('${OCTV_PROJECTS}', PROJECT_PATH)
                elif texFileName.find('z:') >= 0:
                    texFileName = texFileName.replace('z:', OCT_DRIVE)
                elif texFileName.find('Z:') >= 0:
                    texFileName = texFileName.replace('Z:', OCT_DRIVE)
                mc.setAttr('%s.fileTextureName' % texFile, texFileName, type="string")


PROJECT_PATH = r"W:/Working_Project/Katu/lib"
allTexFiles = mc.ls(type='file')
if allTexFiles:
    for texFile in allTexFiles:
        try:
            texFileName = mc.getAttr('%s.fileTextureName' % texFile)
        except:
            pass
        else:
            if texFileName:
                if texFileName.find('F:/znX') >= 0:
                    texFileName = texFileName.replace(r'F:/znX', PROJECT_PATH)
                    mc.setAttr('%s.fileTextureName' % texFile, texFileName, type="string")