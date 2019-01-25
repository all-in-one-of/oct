import maya.cmds as cmds
from phxfd import *

def OnSimulationBegin(node, t, dt):
	sx = cmds.getAttr(node + '.xSize')
	sy = cmds.getAttr(node + '.ySize')
	sz = cmds.getAttr(node + '.zSize')
	for x in range(1, sx/2):
		for y in range(1, sy-1):
			for z in range(sz/3+1):
				setT((x, y, z), 1.0)
