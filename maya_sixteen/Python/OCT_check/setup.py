# -*- coding: utf-8 -*-
import sys
import os
 
#pyqtPath = 'D:/Work/maya_Scripts/AutoOptimizeScene'
def AutoOptimizeScene():
    # pyqtPath = r'D:\MayaSixteenScripts\Python\OCT_check\AutoOptimizeScene'
    pyqtPath = r'//octvision.com/CG/Tech/maya_sixteen/Python/OCT_check/AutoOptimizeScene'
    if pyqtPath not in sys.path:
        sys.path.append (pyqtPath)
        
    import AutoOptimizeScene_v2 as aos
    #reload (aos)
    aos.AutoOptimizeScene()