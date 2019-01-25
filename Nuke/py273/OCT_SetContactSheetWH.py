# -*- coding: utf-8 -*-
import nuke

class changeContactSheetWH():
    def __init__(self):
        pass
    
    def SetWidthHeightUI(self):
        p = nuke.Panel('OCT_SetContactSheetResolution')
        p.setWidth(50)
        p.addSingleLineInput('width:','')
        p.addSingleLineInput('height:','')
        p.addButton('Cancel')
        p.addButton('OK')
        p.setWidth(50)
        p.show() 
        
        widths=p.value('width:')
        heights=p.value('height:')
        
        if widths and heights:
            self.SetContactSheetWH(widths,heights)

    def SetContactSheetWH(self,widths,heights):
        allContactSheet=nuke.selectedNodes('ContactSheet')
        if len(allContactSheet)==0:
            allContactSheet=nuke.allNodes('ContactSheet')
        for each in allContactSheet:
            each['width'].setValue(int(widths))
            each['height'].setValue(int(heights))