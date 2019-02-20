import maya.cmds as cmds
from phxfd import *

def OnSimulationBegin(node, t, dt):
	sizex = cmds.getAttr(node + '.xSize')
	sizey = cmds.getAttr(node + '.ySize')
	sizez = cmds.getAttr(node + '.zSize')
	c = 0.2
	for x in range(sizex):
		for y in range(sizey):
			for z in range(sizez):
				setUVW((x,y,z), (x*c,y*c,z*c))