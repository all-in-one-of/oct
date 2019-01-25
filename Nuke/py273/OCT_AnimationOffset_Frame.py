# *-* coding: utf-8 *-*
import nuke
def animationOffset_Frame():
    p = nuke.Panel('AnimationOffset_Frame')
    p.setWidth(200)
    p.addSingleLineInput('Offset frame', '')
    p.addButton('Cancel')
    p.addButton('Apply')
    result = p.show()

    if result:
        Offset_Frame = float(p.value('Offset frame'))

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
                                key.x = currentTime + Offset_Frame
                                key.y = currentValue
                               