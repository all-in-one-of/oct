#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = Copy2
__author__ = zhangben 
__mtime__ = 2019/4/2 : 20:40
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
import sys,os
import shutil
def Copy2(source,target):
    shutil.copy(source,target)

if __name__ == "__main__":
    src_file = sys.argv[1]
    targ_path = sys.argv[2]
    print("{0}{3}{1}{3}{2}".format(sys.argv[0],src_file,targ_path,os.linesep))
    Copy2(src_file,targ_path)

"""


string $OCTV_TECH = `getenv "OCTV_TECH"`;	//OCTV Tech folder
string $invokepath = $OCTV_TECH + "/bin/CPAU.exe -u octvision\\supermaya -p supermaya -ex ";

string	$cmdvar = substituteAllString($OCTV_TECH, "\/", "\\");
$cmd = $invokepath + "\"" + $cmdvar + "\\bin\\FastCopy341\\FastCopy.exe" + " /force_close /cmd=sync \\\"" + $source + "\\\" /to=\\\"" + $dest + "\\\"\" -nowarn -wait";

$source = "E:\\BenDocument\\temp\\4Meiling.bmp";
$dest = "E:\\dev_temp";

$cmd = $invokepath + "\" python.exe F:\\Development\\octProj\\oct\\maya_sixteen\\Python\\OCT_Pipeline\\scripts\\utility\\Copy2.py " + $source + " " + $dest+"\"";

rint ("\n---------------" + $cmd + "\n");
"""