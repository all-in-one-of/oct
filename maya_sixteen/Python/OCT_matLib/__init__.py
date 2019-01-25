#!/usr/bin/env python
# coding: utf-8

import maya.cmds as mc
import os

def matLib_Tools():
	# allName = ["renhj","yangh"]
	# Name = os.getenv('username')
	# if Name in allName:
	import OCT_TextureLibrary_YH
	i = OCT_TextureLibrary_YH.OCT_TextureLibrary()
	i.show()
	# else:
	# 	mc.confirmDialog(title=u"提示",message=u"你目前还没权限访问质感库！")
	# 	return