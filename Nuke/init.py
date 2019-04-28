# -*- coding: utf-8 -*-
import sys
import os
import nuke
import shutil

#需要与NukePluginsVersion.txt内容一致
NukePluginsVersion = '1.0'

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


NukePluginsVersion_path = os.path.join(localpath, r'NukePluginsVersion.txt')

if os.path.exists(NukePluginsVersion_path):
    verfile = open(NukePluginsVersion_path,'r')
    try:
        PluginsVersion = verfile.read()
        print (PluginsVersion)
    finally: verfile.close()
    if not PluginsVersion == NukePluginsVersion:
        shutil.rmtree(localpath)
elif not os.path.exists(NukePluginsVersion_path) and os.path.exists(localpath):
    shutil.rmtree(localpath)


if not os.path.exists(localpath):
    bat_path = r'NukeToolSet_master\install\copy.bat'
    full_path = os.path.join(NUKE_ENVIRON_PATH, bat_path)
    os.system(full_path)

nuke.pluginAddPath(localpath)

sys.path.append(r"C:\Python27\Lib\site-packages")

gizmo_localpath = os.path.join(localpath,'gizmos')
for root,dir,file in os.walk(gizmo_localpath):
    nuke.pluginAddPath(root)

