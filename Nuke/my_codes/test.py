# if sourceSels == None:
#     sourceSels = nuke.selectedNodes('Read')
#     numSelect = len(sourceSels)
# _dot = nuke.nodes.Dot()
# sourceSels = sorted(sourceSels, key=lambda eaNd: checkFile(eaNd, FileName)[0])
# if not checkFile(sourceSels[0], FileName)[0]:
#     sourceSels = sorted(sourceSels, key=lambda eaNd: checkFile4ef(eaNd)[0])
# _dot.setXYpos(sourceSels[0].xpos(), sourceSels[0].ypos())
# left_edge = _dot.xpos() # min(eand.xpos() for eand in sourceSels)
# top_edge = _dot.ypos()#min(eand.ypos() for eand in sourceSels)
# _sortedCam = {}
# # cleare select
# for i in sourceSels:
#     i['selected'].setValue(False)
# transData = calculate_data(sourceSels)
# centerData = [1143, 4343.5]
# merge_inputPlugs = {0: 1, 1: 3, 2: 4}
# x_pos_v = left_edge
# transLst = []
# rndlyer = []
# rndCam = []
# totalwidth = 0
# for each in sourceSels:
#     # each['selected'].setValue(True)
#     camStr = checkFile(each, FileName)
#     if camStr[0] == None:
#         camStr = checkFile4ef(each)
#         rndlyer.append(stuff_info(each,True)["rndLayer"])
#         rndCam.append(stuff_info(each,True)["rndCam"])
#     else:
#         rndlyer.append(stuff_info(each)["rndLayer"])
#         rndCam.append(stuff_info(each)["rndCam"])
#     if not camStr: nuke.error("sutff name promeblem")
#     each.setXYpos(x_pos_v, top_edge)
#     ea_w = each.screenWidth()
#     ea_h = each.screenHeight()
#     ea_left = each.xpos()
#     ea_top = each.ypos()
#     ea_bottom = ea_top - ea_h
#     totalwidth += ea_w
#     trnsnd = nuke.nodes.Transform()
#     trnsnd['translate'].setValue([transData[camStr[0]][0], transData[camStr[0]][1]])
#     trnsnd['center'].setValue([centerData[0], centerData[1]])
#     trnsnd.setXYpos(ea_left, ea_bottom + 180)
#     trnsnd.setInput(0, each)
#     transLst.append(trnsnd)
#     x_pos_v += (ea_w + 33)
# MergeNode = nuke.nodes.Merge2()
# MergeNode.setXYpos(transLst[1].xpos(), transLst[1].ypos() + 80)
# for n in range(len(transLst)):
#     MergeNode.setInput(merge_inputPlugs[n], transLst[n])
# 
# _setFormat = [eafmt for eafmt in nuke.formats() if eafmt.width() == 6858]
# 
# if not len(_setFormat):
#     dntgfmt = "6858 8687 DNTG MergCams"
#     addfmg = nuke.addFormat(dntgfmt)
#     _constant = nuke.nodes.Constant(format=addfmg.name())
# else:
#     _constant = nuke.nodes.Constant(format=_setFormat[0].name())
# 
# _constant.setXYpos((MergeNode.xpos() + 160), MergeNode.ypos() - 50)
# _constant.knob("channels").setValue("rgb")
# MergeNode.setInput(0, _constant)
# rndlyer = [rndlyer[n] for n in range(len(rndlyer)) if rndlyer[n] not in rndlyer[:n]]
# if len(rndlyer) != 1:
#     from PySide import QtGui
#     msgBox = QtGui.QMessageBox()
#     msgBox.setText("Please selecte the stuffs those in the same render layer")
#     msgBox.exec_()
# rndCam = [rndCam[n] for n in range(len(rndCam)) if rndCam[n] not in rndCam[:n]]
# if len(rndlyer) != 1:
#     from PySide import QtGui
#     msgBox = QtGui.QMessageBox()
#     msgBox.setText("Please selecte the stuffs those in the same side camera")
#     msgBox.exec_()
# bdrp = nuke.nodes.BackdropNode(xpos=(_dot.xpos() - 15), bdwidth=totalwidth + 160, ypos=(_dot.ypos() - 75),
#                                bdheight=(MergeNode.ypos() - top_edge) + 130,
#                                tile_color=int((random.random() * (16 - 10))) + 10, note_font_size=45)
# 
# camsDict = {'l':'left','r':'right','L':'Left','R':'Right'}
# cam_nm = re.search('[lr]',rndCam[0],re.I).group()
# drpName = "camera  {} {}".format(camsDict[cam_nm],rndlyer[0])
# bdrp.setName(drpName)
# drp_lab = "{} : {}".format(camsDict[cam_nm],rndlyer[0])
# bdrp.knob("label").setValue(drp_lab)
# nuke.delete(_dot)
# 
# 
# 
# sel_tx = nuke.selectedNodes('Transform')
# for each in sel_tx:
#     ea_tx = each.knob('translate').getValue()
#     each.knob('translate').setValue([1571,ea_tx[1]])
#
#
# sel = nuke.selectedNodes()
#
# sel[0].knob('translate').getValue()
# sel[0].knob('translate').setValue([10,10])
#
# sel_tx = nuke.selectedNodes('Text2')
# for each in sel_tx:
#     ea_tx = each.knob('translate').getValue()
#     each.knob('translate').setValue([ea_tx[0],4685])
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# # add  grid
# 
# 
# sels = nuke.selectedNodes()
# 
# stuffH = 8135
# stuffW = 6858
# lineNum = 10
# eachHigh = stuffH / lineNum
# 
# pos_x = sels[0].xpos()
# pos_y = sels[0].ypos()
# 
# # print("\n".join(dir(nuke.nodes.Grid())))
# gridNode = ""
# aboveNd = sels[0]
# 
# transLate_dist = stuffH / lineNum
# current_ty = stuffH - transLate_dist
# 
# for i in range(lineNum):
#     new_yp = pos_y + 35
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=(pos_x + 300), ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
# 
#     grdNode.knob("translate").setValue([0, current_ty])
#     grdNode.knob("color").setValue([1, 0, 0, 1])
#     grdNode.knob("size").setValue(25)
# 
#     grdNode.knob("translate")
# 
# sels = nuke.selectedNodes()
# for eachSel in sels:
#     eachSel.knob("size").setValue(25)
# 
# sels = nuke.selectedNodes()
# 
# stuffH = 8135
# stuffW = 6858
# lineNum = 100
# eachHigh = stuffH / lineNum
# 
# horizonta_num = 100
# vertically_num = 84
# 
# pos_x = sels[0].xpos()
# pos_y = sels[0].ypos()
# 
# # print("\n".join(dir(nuke.nodes.Grid())))
# gridNode = ""
# aboveNd = sels[0]
# 
# transLate_dist = stuffH / lineNum
# current_ty = stuffH - transLate_dist
# 
# i = 3
# for i in range(lineNum):
#     new_yp = pos_y + 35
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=(pos_x + 300), ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
#     grdNode.knob("translate").setValue([0, current_ty])
#     grdNode.knob("color").setValue([1, 0, 0, 1])
#     grdNode.knob("size").setValue(25)
# 
#     grdNode.knob("translate")
# 
# sels = nuke.selectedNodes()
# for eachSel in sels:
#     eachSel.knob("size").setValue(25)
# 
# sels = nuke.selectedNodes()
# 
# stuffH = 8135
# stuffW = 6858
# lineNum = 100
# eachHigh = stuffH / lineNum
# 
# horizonta_num = 100
# vertically_num = 84
# 
# pos_x = sels[0].xpos()
# pos_y = sels[0].ypos()
# 
# # print("\n".join(dir(nuke.nodes.Grid())))
# gridNode = ""
# aboveNd = sels[0]
# 
# transLate_dist_h = stuffH / horizonta_num
# transLate_dist_w = stuffW / vertically_num
# 
# current_ty = stuffH - transLate_dist_h
# current_tx = 0
# 
# for i in range(transLate_dist_h):
#     new_yp = pos_y + 35
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=(pos_x + 300), ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
#     grdNode.knob("translate").setValue([0, current_ty])
#     grdNode.knob("color").setValue([1, 0, 0, 1])
#     grdNode.knob("size").setValue(25)
#     cr_xy = grdNode.knob(transLate
#     ").getValue()
# 
#     current_ty = cr_xy[1]
#     current_tx = cr_xy[0]
# 
#     for i in range(transLate_dist_h):
#         new_yp = pos_y + 35
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=(pos_x + 300), ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
#     grdNode.knob("translate").setValue([current_tx, 0])
#     grdNode.knob("color").setValue([1, 0, 0, 1])
#     grdNode.knob("size").setValue(25)
#     cr_xy = grdNode.knob(transLate
#     ").getValue()
#     current_ty = cr_xy[1]
#     current_tx = cr_xy[0]
# 
#     sels = nuke.selectedNodes()
#     for eachSel in sels:
#         eachSel.knob("size").setValue(25)sels = nuke.selectedNodes()
# 
#     sels = nuke.selectedNodes()
# 
#     stuffH = 8135
#     stuffW = 6858
#     lineNum = 100
#     eachHigh = stuffH / lineNum
# 
#     horizonta_num = 100
#     vertically_num = 84
#     pos_x = sels[0].xpos()
#     pos_y = sels[0].ypos()
#     # print("\n".join(dir(nuke.nodes.Grid())))
#     gridNode = ""
#     aboveNd = sels[0]
# 
#     transLate_dist_h = stuffH / horizonta_num
#     transLate_dist_w = stuffW / vertically_num
#     current_ty = stuffH - transLate_dist_h
#     current_tx = 0
#     clor = [1, 1, 1, 1]
# 
#     h_v_dict = {"horizontal": [0, current_ty], "vertically": [current_tx, 0]}
# 
#     dir_nams = h_v_dict.keys()[0]
# 
#     for i in range(transLate_dist_h):
#         new_yp = pos_y + 35
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=(pos_x + 300), ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
#     grdNode.knob("translate").setValue(h_v_dict[dir_nams])
#     grdNode.knob("color").setValue(clor)
#     grdNode.knob("size").setValue(25)
#     grdNode.knob("number").setValue(.05)
#     cr_xy = grdNode.knob("translate").getValue()
#     current_ty = cr_xy[1] - transLate_dist_h
#     current_tx = cr_xy[0]
# 
#     for i in range(transLate_dist_h):
#         new_yp = pos_y + 35
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=(pos_x + 300), ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
#     grdNode.knob("translate").setValue([current_tx, 0])
#     grdNode.knob("color").setValue([1, 0, 0, 1])
#     grdNode.knob("size").setValue(25)
#     cr_xy = grdNode.knob("translate").getValue()
#     current_ty = cr_xy[1] - transLate_dist_h
#     current_tx = cr_xy[0] + transLate_dist_w
# 
#     sels = nuke.selectedNodes()
#     for eachSel in sels:
#         eachSel.knob("size").setValue(0.25)
# 
#     sels = nuke.selectedNodes()
# 
#     stuffH = 8135
#     stuffW = 6858
# 
#     ratio = (float(stuffH) / float(stuffW))
#     horizonta_line_num = 80
#     vertical_line_num = int(horizonta_num / ratio)
# 
#     # =========locator position=============
# 
#     loc_pot = nuke.nodes.Dot(name="location")
#     sel_pos_x = sels[0].xpos()
#     sel_pos_y = sels[0].ypos()
# 
#     x_bias = -600
#     y_bias = 100
# 
#     loc_pot.setXYpos(sel_pos_x + x_bias, sel_pos_y + y_bias)
# 
#     # ===========calculate =============
# 
#     loc_x = loc_pot.xpos()
#     loc_y = loc_pot.ypos()
# 
#     tx_pos = stuffH
# 
#     tx2txDis_y = (float(stuffH) / float(horizonta_num))
#     tx2txDis_x = (float(stuffW) / float(vertically_num))
# 
#     tx2txDis_dic = {'x': tx2txDis_x, 'y': tx2txDis_y}
#     # print("\n".join(dir(nuke.nodes.Grid())))
# 
#     create_nds = []
#     aboveNd = ""
# 
#     x_axis_loc = 100
#     y_axis_loc = 200
# 
#     axisLoc = {'x': [0, x_axis_loc], 'y': [y_axis_loc, 0]}
# 
#     ori = 'y'
# 
#     tx_st_x = 0
#     tx_st_y = 0
# 
#     ft_sz = 80
#     for n in range(horizonta_line_num):
#     # n = 0
#         tx_nd = nuke.nodes.Text2(name="idTx_{}".format(n))
#     tx_nd.setXYpos(loc_x + 5, loc_y + n)
#     tx_nd.knob("message").setValue("{:d}".format(n))
#     dis = axisLoc[ori]
#     box_x = axisLoc[ori][0] + 10
#     box_r = box_x + ft_sz
#     box_y = n * tx2txDis_dic['y']
#     box_t = box_y + ft_sz
#     tx_nd['box'].setValue([box_x, box_r, box_y, box_t])
# 
#     tx_nd['xjustify'].setValue('left')
#     tx_nd['yjustify'].setValue('bottom')
#     tx_nd['font_size'].setValue(ft_sz)
#     tx_nd['global_font_scale'].setValue(5)
#     if not n:
#         tx_nd.setInput(0, aboveNd)
#     aboveNd = tx_nd
# 
#     p = nuke.selectedNodes()[0]
# 
#     p['font_size'].setValue(100)
# 
#     current_ty = stuffH - transLate_dist_h
#     current_tx = 0
#     clor = [1, 1, 1, 1]
#     h_v_dict = {"horizontal": [0, current_ty], "vertically": [current_tx, 0]}
#     pos_bias = 0
#     pos_x_bias = pos_x + 350
# 
#     dir_nams = h_v_dict.keys()[0]
#     maxNum = vertically_num
# 
#     for i in range(maxNum):
#         new_yp = pos_y + pos_bias
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=pos_x_bias, ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
#     grdNode.knob("translate").setValue(h_v_dict[dir_nams])
#     grdNode.knob("color").setValue(clor)
#     grdNode.knob("size").setValue(.2)
#     grdNode.knob("number").setValue(1)
#     cr_xy = grdNode.knob("translate").getValue()
#     if dir_nams == "horizontal":
#         current_ty = cr_xy[1] - transLate_dist_h
#     else:
#         current_tx = cr_xy[0] + transLate_dist_w
#     h_v_dict[dir_nams] = [current_tx, current_ty]
# 
#     sels = nuke.selectedNodes()
# 
#     stuffH = 8135
#     stuffW = 6858
# 
#     ratio = (float(stuffH) / float(stuffW))
#     horizonta_line_num = 80
#     vertical_line_num = int(horizonta_num / ratio)
# 
#     # =========locator position=============
# 
#     loc_pot = nuke.nodes.Dot(name="location")
#     sel_pos_x = sels[0].xpos()
#     sel_pos_y = sels[0].ypos()
# 
#     x_bias = -600
#     y_bias = 100
# 
#     loc_pot.setXYpos(sel_pos_x + x_bias, sel_pos_y + y_bias)
# 
#     # ===========calculate =============
# 
#     loc_x = loc_pot.xpos()
#     loc_y = loc_pot.ypos()
# 
#     tx_pos = stuffH
# 
#     tx2txDis_y = (float(stuffH) / float(horizonta_num))
#     tx2txDis_x = (float(stuffW) / float(vertically_num))
# 
#     tx2txDis_dic = {'x': tx2txDis_x, 'y': tx2txDis_y}
#     # print("\n".join(dir(nuke.nodes.Grid())))
# 
#     create_nds = []
#     aboveNd = ""
# 
#     x_axis_loc = 100
#     y_axis_loc = 200
# 
#     axisLoc = {'x': [0, x_axis_loc], 'y': [y_axis_loc, 0]}
# 
#     ori = 'y'
# 
#     tx_st_x = 0
#     tx_st_y = 0
# 
#     ft_sz = 80
#     for n in range(horizonta_line_num):
#     # n = 0
#         tx_nd = nuke.nodes.Text2(name="idTx_{}".format(n))
#     tx_nd.setXYpos(loc_x + 5, loc_y + n)
#     tx_nd.knob("message").setValue("{:d}".format(n))
#     dis = axisLoc[ori]
#     box_x = axisLoc[ori][0] + 10
#     box_r = box_x + ft_sz
#     box_y = n * tx2txDis_dic['y']
#     box_t = box_y + ft_sz
#     tx_nd['box'].setValue([box_x, box_r, box_y, box_t])
# 
#     tx_nd['xjustify'].setValue('left')
#     tx_nd['yjustify'].setValue('bottom')
#     tx_nd['font_size'].setValue(ft_sz)
#     tx_nd['global_font_scale'].setValue(5)
#     if not n:
#         tx_nd.setInput(0, aboveNd)
#     aboveNd = tx_nd
# 
#     p = nuke.selectedNodes()[0]
# 
#     p['font_size'].setValue(100)
# 
#     current_ty = stuffH - transLate_dist_h
#     current_tx = 0
#     clor = [1, 1, 1, 1]
#     h_v_dict = {"horizontal": [0, current_ty], "vertically": [current_tx, 0]}
#     pos_bias = 0
#     pos_x_bias = pos_x + 350
# 
#     dir_nams = h_v_dict.keys()[0]
#     maxNum = vertically_num
# 
#     for i in range(maxNum):
#         new_yp = pos_y + pos_bias
#     grdNode = nuke.nodes.Grid(name="CropGrid_{:02d}".format(i + 1), xpos=pos_x_bias, ypos=pos_y)
#     grdNode.setInput(0, aboveNd)
#     pos_y = new_yp
#     aboveNd = grdNode
#     grdNode.knob("translate").setValue(h_v_dict[dir_nams])
#     grdNode.knob("color").setValue(clor)
#     grdNode.knob("size").setValue(.2)
#     grdNode.knob("number").setValue(1)
#     cr_xy = grdNode.knob("translate").getValue()
#     if dir_nams == "horizontal":
#         current_ty = cr_xy[1] - transLate_dist_h
#     else:
#         current_tx = cr_xy[0] + transLate_dist_w
#     h_v_dict[dir_nams] = [current_tx, current_ty]
# 
#     bdrp = nuke.nodes.BackdropNode(xpos=pos_x_bias - 20, bdwidth=130, ypos=(sels[0].ypos() - 35), bdheight=(80),
#                                    tile_color=int((random.random() * (16 - 10))) + 10, note_font_size=45)
#     bdrp.setName(dir_nams)
#     drp_lab = "direction: {}".format(dir_nams)
# 
#     bdrp = nuke.nodes.BackdropNode(xpos=pos_x_bias - 20, bdwidth=130, ypos=(sels[0].ypos() - 35), bdheight=(80),
#                                    tile_color=int((random.random() * (16 - 10))) + 10, note_font_size=45)
#     bdrp.setName(dir_nams)
#     drp_lab = "direction: {}".format(dir_nams)
# 
# 
# 
# 
# 
# 
# 
# 
