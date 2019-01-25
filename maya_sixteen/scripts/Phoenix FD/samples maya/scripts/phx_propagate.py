import maya.cmds as cmds
from phxfd import *

def OnSimulationBegin(node, t, dt):
	sizex = cmds.getAttr(node + '.xSize')
	sizey = cmds.getAttr(node + '.ySize')
	sizez = cmds.getAttr(node + '.zSize')
	for x in range(sizex):
		for y in range(sizey):
			for z in range(sizez):
				dx = x - sizex/2
				dz = z - sizez/2
				if dx*dx + dz*dz < 10:
					setFl((x, y, z), 0.5)
