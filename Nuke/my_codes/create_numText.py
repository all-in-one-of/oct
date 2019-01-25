#=====================create  x direction axis==============
import nuke
sels = nuke.selectedNodes()
stuffH = 8135
stuffW = 6858
ratio = (float(stuffH) / float(stuffW))
horizonta_line_num = 80
vertical_line_num = int(horizonta_line_num / ratio)
# =========locator position=============
loc_pot = nuke.nodes.Dot(name="location")
sel_pos_x = sels[0].xpos()
sel_pos_y = sels[0].ypos()
x_bias = -600
y_bias = 100
loc_pot.setXYpos(sel_pos_x + x_bias, sel_pos_y + y_bias)
#===========calculate =============
loc_x = loc_pot.xpos()
loc_y = loc_pot.ypos()
tx2txDis_y = (float(stuffH) / float(horizonta_line_num))
tx2txDis_x = (float(stuffW) / float(vertical_line_num))
tx2txDis_dic = {'x': tx2txDis_x, 'y': tx2txDis_y}
# print("\n".join(dir(nuke.nodes.Grid())))
x_axis_loc = 0
y_axis_loc = 0
axisLoc = {'x': [0, x_axis_loc], 'y': [y_axis_loc, 0]}
ori = 'x'
create_nds = []
aboveNd = ""
interval_num = 1

# horizonta_line_num
for n in range(horizonta_line_num):
    # n = 0
    if not n % interval_num:
        nm_n = n / interval_num
        tx_nd = nuke.nodes.Text2(name="axis_{}_{:d}".format(ori, nm_n))
        # tx_nd.setSelected(1)
        tx_nd.setXYpos(loc_x + 5, loc_y + 5)
        dis = axisLoc[ori]
        # box_x = axisLoc[ori][0] + 10
        # box_r = box_x + 90 * 3
        # box_y = n * tx2txDis_dic['y'] + 5
        # box_t = box_y + 90

        box_x = n * int(tx2txDis_dic['x'] - 0.5)
        box_r = box_x + 90 * 3
        box_y = axisLoc[ori][1] + 10
        box_t = box_y + 90

        tx_nd['box'].setValue([box_x, box_y, box_r, box_t])
        tx_nd['xjustify'].setValue('left')
        tx_nd['yjustify'].setValue('bottom')
        # tx_nd.knob('font_size').setValue(90)
        # tx_nd.knob('font_width').setValue(90)
        # tx_nd.knob('font_height').setValue(90)
        # tx_nd.knob('message').setValue('{:02d}'.format(n))
        if n != 0:
            tx_nd.setInput(0, aboveNd)
        aboveNd = tx_nd
        create_nds.append(tx_nd)

for n in range(len(create_nds)):
    create_nds[n].knob('font_size').setValue(90)
    create_nds[n].knob('font_width').setValue(90)
    create_nds[n].knob('font_height').setValue(90)

for n in range(len(create_nds)):
    create_nds[n].knob('message').setValue('{:02d}'.format(n))

create_nds = []
aboveNd = ""

move_axis = [0, 0]
tras_axis = nuke.createNode('Transform')
tras_axis['translate'].setValue(move_axis)
tras_axis.setXYpos(create_nds[-1].xpos(), create_nds[-1].ypos() + 30)
tras_axis.setInput(0, create_nds[-1])

# mergnd = nuke.toNode('Merge1')
mergnd.connectInput(0, tras_axis)


#====================create y direction axis =============================


#=====================create  x direction axis==============
import nuke
sels = nuke.selectedNodes()
stuffH = 8135
stuffW = 6858
ratio = (float(stuffH) / float(stuffW))
horizonta_line_num = 80
vertical_line_num = int(horizonta_line_num / ratio)
# =========locator position=============
loc_pot = nuke.nodes.Dot(name="location")
sel_pos_x = sels[0].xpos()
sel_pos_y = sels[0].ypos()
x_bias = -600
y_bias = 100
loc_pot.setXYpos(sel_pos_x + x_bias, sel_pos_y + y_bias)
# ===========calculate =============
#===========calculate =============
loc_x = loc_pot.xpos()
loc_y = loc_pot.ypos()

tx2txDis_y = (float(stuffH) / float(horizonta_line_num))
tx2txDis_x = (float(stuffW) / float(vertical_line_num))
tx2txDis_dic = {'x': tx2txDis_x, 'y': tx2txDis_y}
# print("\n".join(dir(nuke.nodes.Grid())))
x_axis_loc = 0
y_axis_loc = 0
axisLoc = {'x': [0, x_axis_loc], 'y': [y_axis_loc, 0]}
ori = 'y'
create_nds = []
aboveNd = ""
interval_num = 1
# horizonta_line_num
for n in range(horizonta_line_num):
    # n = 0
    if not n % interval_num:
        nm_n = n / interval_num
        tx_nd = nuke.nodes.Text2(name="axis_{}_{:d}".format(ori, nm_n))
        # tx_nd.setSelected(1)
        tx_nd.setXYpos(loc_x + 5, loc_y + 5)
        dis = axisLoc[ori]
        box_x = axisLoc[ori][0] + 10
        box_r = box_x + 90 * 3
        box_y = n * tx2txDis_dic['y'] + 5
        box_t = box_y + 90
        # box_x = n * int(tx2txDis_dic['x'] - 0.5)
        # box_r = box_x + 90 * 3
        # box_y = axisLoc[ori][1] + 10
        # box_t = box_y + 90
        tx_nd['box'].setValue([box_x, box_y, box_r, box_t])
        tx_nd['xjustify'].setValue('left')
        tx_nd['yjustify'].setValue('bottom')
        # tx_nd.knob('font_size').setValue(90)
        # tx_nd.knob('font_width').setValue(90)
        # tx_nd.knob('font_height').setValue(90)
        # tx_nd.knob('message').setValue('{:02d}'.format(n))
        if n != 0:
            tx_nd.setInput(0, aboveNd)
        aboveNd = tx_nd
        create_nds.append(tx_nd)
for n in range(len(create_nds)):
    create_nds[n].knob('font_size').setValue(90)
    create_nds[n].knob('font_width').setValue(90)
    create_nds[n].knob('font_height').setValue(90)

for n in range(len(create_nds)):
    create_nds[n].knob('message').setValue('{:02d}'.format(n))

create_nds = []
aboveNd = ""

move_axis = [0, 0]
tras_axis = nuke.createNode('Transform')
tras_axis['translate'].setValue(move_axis)
tras_axis.setXYpos(create_nds[-1].xpos(), create_nds[-1].ypos() + 30)
tras_axis.setInput(0, create_nds[-1])

# mergnd = nuke.toNode('Merge1')
mergnd.connectInput(0, tras_axis)

































































sels = nuke.selectedNodes()
mergnd = nuke.toNode('Merge2')
stuffH = 8135
stuffW = 6858
ratio = (float(stuffH)/float(stuffW))
horizonta_line_num= 80
vertical_line_num = int(horizonta_line_num/ratio)
#=========locator position=============
loc_pot = nuke.nodes.Dot(name="location")
sel_pos_x = sels[0].xpos()
sel_pos_y = sels[0].ypos()
x_bias = -600
y_bias = 100
loc_pot.setXYpos(sel_pos_x+x_bias,sel_pos_y+y_bias)

tx2txDis_y = (float(stuffH)/float(horizonta_line_num))
tx2txDis_x = (float(stuffW)/float(vertical_line_num))
tx2txDis_dic = {'x':tx2txDis_x,'y':tx2txDis_y}
#print("\n".join(dir(nuke.nodes.Grid())))
x_axis_loc = 0
y_axis_loc = 0
axisLoc = {'x':[0,x_axis_loc],'y':[y_axis_loc,0]}
ori='y'
tx_st_x = 0
tx_st_y = 0
create_nds = []
aboveNd = ""
move_axis = [3228,0]
text_per_num = 1
for n in range(horizonta_line_num):
    # n = 0
    tx_nd = nuke.nodes.Text2(name = "idTx_{}".format(n))
    # tx_nd.setSelected(1)
    tx_nd.setXYpos(loc_x +5 ,loc_y +5)
    dis =axisLoc[ori]
    box_x = axisLoc[ori][0] + 10
    box_r = box_x + ft_sz * 3
    box_y = n * tx2txDis_dic['y'] + 5
    box_t = box_y + ft_sz
    tx_nd['box'].setValue([box_x, box_y, box_r, box_t])
    tx_nd['xjustify'].setValue('left')
    tx_nd['yjustify'].setValue('bottom')
    # tx_nd.knob('font_size').setValue(90)
    # tx_nd.knob('font_width').setValue(90)
    # tx_nd.knob('font_height').setValue(90)
    # tx_nd.knob('message').setValue('{:02d}'.format(n))
    if n != 0:
        tx_nd.setInput(0, aboveNd)
    aboveNd = tx_nd
    create_nds.append(tx_nd)
    # tx_nd.setSelected(0)

# print("\n".join(dir(tx_nd)))

for n in range(len(create_nds)):
    create_nds[n].knob('font_size').setValue(90)
    create_nds[n].knob('font_width').setValue(90)
    create_nds[n].knob('font_height').setValue(90)

for n in range(len(create_nds)):
    create_nds[n].knob('message').setValue('{:02d}'.format(n))


tras_axis = nuke.createNode('Transform')
tras_axis['translate'].setValue(move_axis)
tras_axis.setXYpos(create_nds[-1].xpos(),create_nds[-1].ypos() + 30)
tras_axis.setInput(0,create_nds[-1])


import re
def dis_spec_tex(disVis_num):
    #disVis_num = [16,17,18]
    selTxs = nuke.selectedNodes("Text2")
    for eatx in selTxs:
        nmstr = eatx['name'].getValue()
        num_str = re.search('_\d+',nmstr).group()
        disVis_numStr = [str(m) for m in disVis_num]
        if re.sub('_','',num_str) in disVis_numStr:
            eatx['disable'].setValue(1)
        else:
            eatx['disable'].setValue(0)