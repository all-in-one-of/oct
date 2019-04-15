import sys
import os
import nuke

version = sys.version.split()
NUKE_ENVIRON_PATH = os.environ['NUKE_PATH']

if version[0] == '2.7.3':
    py_273_path = os.path.join(NUKE_ENVIRON_PATH, r'py273')
    py_273_lib_path = os.path.join(NUKE_ENVIRON_PATH, r'py273\lib')
    sys.path.append(py_273_path)
    sys.path.append(py_273_lib_path)
else:
    py_265_path = os.path.join(NUKE_ENVIRON_PATH, r'py265')
    py_265_lib_path = os.path.join(NUKE_ENVIRON_PATH, r'py265\lib')
    sys.path.append(py_265_path)
    sys.path.append(py_265_lib_path)


#------------------------------
# add plugin
#------------------------------

localpath = r'C:\Program Files\Common Files\OFX\Plugins\NukeToolSet_master'

if not os.path.exists(localpath):
    bat_path = r'NukeToolSet_master\install\copy.bat'
    full_path = os.path.join(NUKE_ENVIRON_PATH, bat_path)
    os.system(full_path)

nuke.pluginAddPath(localpath)

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte()


sys.path.append(r"C:\Python27\Lib\site-packages")

gizmo_localpath = os.path.join(localpath,'gizmos')
for root,dir,file in os.walk(gizmo_localpath):
    nuke.pluginAddPath(root)