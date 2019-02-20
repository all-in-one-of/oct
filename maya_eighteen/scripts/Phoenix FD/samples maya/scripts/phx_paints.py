import maya.cmds as cmds
from phxfd import *

def OnSimulationBegin(node, t, dt):
	sx = cmds.getAttr(node + '.xSize')
	sy = cmds.getAttr(node + '.ySize')
	sz = cmds.getAttr(node + '.zSize')
	sc = sx/2
	for x in range(sx):
		for y in range(sy):
			for z in range(sz):
				setUVW((x,y,z), (1,0,0) if (x < sc) else (0,0,1))