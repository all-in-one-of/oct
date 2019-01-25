import nuke

def animationCurve_convert():
    p = nuke.Panel('AnimationCurve_FPSConvert')
    p.setWidth(200)
    p.addSingleLineInput('Original FPS', '')
    p.addSingleLineInput('New FPS', '')
    p.addButton('Cancel')
    p.addButton('Apply')
    result = p.show()

    if result:
        ORIG_FPS = float(p.value('Original FPS'))
        NEW_FPS = float(p.value('New FPS'))
        RATIO =  NEW_FPS / ORIG_FPS

        all_selected_nodes = nuke.selectedNodes()
        
        count = len(all_selected_nodes)
        if count ==  0:
            return

        for eachNode in all_selected_nodes:
            allKnobs = eachNode.knobs()

            for eachKnob in allKnobs.values():
                if eachKnob.isAnimated():
                    try:
                        allCurves = eachKnob.animations()
                    except:
                        continue
                    else:
                        for eachCurve in allCurves:
                            allKeys = eachCurve.keys()
                            for key in allKeys:
                                currentTime = key.x
                                currentValue = key.y
                                key.x = currentTime * RATIO
                                key.y = currentValue
                                key.interpolation = nuke.CUBIC
                                key.extrapolation = nuke.LINEAR
