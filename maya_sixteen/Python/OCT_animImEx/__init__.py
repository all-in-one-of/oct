#!/usr/bin/env python
# coding: utf-8 


import maya.cmds as mc
import threading

def animImport():
    from OCT_animImport import ReadXmlDataToMaya_YH
    if mc.window("Ui_ReadXmlDataToMaya", exists=True):
        mc.deleteUI("Ui_ReadXmlDataToMaya", window=True)
    dialog = ReadXmlDataToMaya_YH()
    t = threading.Thread(None, dialog.show())
    t.start()

def animExport():
    from OCT_animExport import WriteDataToXml_YH
    if mc.window("Ui_WriteDataToXml", exists=True):
        mc.deleteUI("Ui_WriteDataToXml", window=True)
    dialog = WriteDataToXml_YH()
    t = threading.Thread(None, dialog.show())
    t.start()