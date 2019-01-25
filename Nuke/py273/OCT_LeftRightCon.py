# *-* coding: utf-8 *-*

import nuke
import os
import nukescripts

def do_LeftRightConnection():
	allNode = nuke.selectedNodes('ContactSheet')
	AllNode = nuke.selectedNodes()
	if len(allNode)!=2:
		nuke.message('\xe8\xaf\xb7\xe9\x80\x89\xe6\x8b\xa9\xe4\xb8\xa4\xe4\xb8\xaa\xe5\xb7\xa6\xe5\x8f\xb3\xe7\x9c\xbc\xe8\xbf\x9e\xe6\x8e\xa5\xe7\x9a\x84ContactSheet\xe8\x8a\x82\xe7\x82\xb9\xef\xbc\x81')
		return
	else:
		for node in AllNode:
			node.setSelected(0)
		nukescripts.stereo.setViewsForStereo()
		joinviewsNode = nuke.createNode('JoinViews', inpanel=False)
		for node in AllNode:
			if node.Class() == 'ContactSheet':
				seqNum=node.inputs()
				if seqNum<1:
					nuke.message('ContactSheet\xe8\xa6\x81\xe8\xbf\x9e\xe6\x8e\xa5\xe5\xb7\xa6\xe5\x8f\xb3\xe7\x9c\xbc\xe7\x9a\x84read\xe8\x8a\x82\xe7\x82\xb9')
					return
				else:
					ReadNode=node.input(seqNum-1)
					filePath=ReadNode['file'].value()
					baseN=os.path.basename(filePath).split('.')[0]
					if baseN.find('CamL') >= 0 or baseN.find('camL')>0:
						joinviewsNode.setInput(0, node)
						lefts = [node.xpos(), node.ypos()]
					else:
						joinviewsNode.setInput(1, node)
						rights = [node.xpos(), node.ypos()]

		joinviewsNode.setXYpos((lefts[0]+rights[0])/2, lefts[1]+80)