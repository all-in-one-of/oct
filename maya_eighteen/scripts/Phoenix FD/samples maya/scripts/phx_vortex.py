import maya.cmds as cmds
from phxfd import *

def OnSimulationBegin(node, t, dt):
	sx = cmds.getAttr(node + '.xSize')
	sy = cmds.getAttr(node + '.ySize')
	sz = cmds.getAttr(node + '.zSize')
	for x in range(0, sx):
		for y in range(0, sy):
			for z in range(sz/2):
				setT((x, y, z), 1.0)
