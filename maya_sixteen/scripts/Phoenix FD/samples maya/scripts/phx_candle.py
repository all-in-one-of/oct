import maya.cmds as cmds
from phxfd import *

def OnSimulationStep(node, t, dt):
	setsystem('core')
	r = 3
	cx = cmds.getAttr(node + '.xSize')/2 + 0.5
	cy = cmds.getAttr(node + '.ySize')/2 + 0.5
	for x in range(-r, r):
		for y in range(-r, r):
			for z in range(7, 15):
				if x*x+y*y < r*r:
					inject((x+cx, y+cy, z), 12, 1800)
