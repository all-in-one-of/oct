import maya.cmds as cmds

def fix_animation():
	sel_controller = cmds.ls(sl=True)
	
	if len(sel_controller)<1:
		cmds.error(u'请选择一个控制器或物体')
	else:	
		for item_controller in sel_controller:
			list_attrs = cmds.listAttr(item_controller, k=True)
			
			for item_attr in list_attrs:
				attr_node = item_controller + '_' + item_attr
				output_attr = attr_node + '.output'
				input_attr = item_controller + '.' + item_attr
				#print output_attr
				#print input_attr	
				
				if cmds.objExists(attr_node):
					if not cmds.isConnected(output_attr, input_attr):
						cmds.connectAttr(output_attr, input_attr, f=True)
			
fix_animation()
