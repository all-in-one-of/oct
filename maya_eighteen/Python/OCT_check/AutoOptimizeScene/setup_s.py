# -*- coding: utf-8 -*-
import sys
import os
 
#pyqtPath = 'D:/Work/maya_Scripts/AutoOptimizeScene'
pyqtPath = 'D:/MayaSixteenScripts/Python/OCT_check/AutoOptimizeScene'
if pyqtPath not in sys.path:
    sys.path.append (pyqtPath)
    
import AutoOptimizeScene_v2 as aos
reload (aos)
aos.AutoOptimizeScene()