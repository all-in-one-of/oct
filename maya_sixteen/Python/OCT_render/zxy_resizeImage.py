# -*- coding: utf-8 -*-

import os
import tempfile
import subprocess
import threading

import maya.cmds as mc
import maya.OpenMaya as om
import maya.OpenMayaUI as ui

from PyQt4 import QtCore
from PyQt4 import QtGui
import sip


CPAU_PATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
FCOPY_PATH = r'\\octvision.com\cg\Tech\bin\FastCopy341\FastCopy.exe'
REMOTE_USER = r'octvision.com\supermaya'
REMOTE_PWD = 'supermaya'


def get_maya_window():
    ptr = ui.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)


class ReSizeDialog(QtGui.QDialog):

    mode = 0
    index = 2
    size_index = float(1.000 / 2.000)
    file_nodes = []
    file_name = None
    file_ext = None
    file_dir = None
    temp_file = None
    is_writable = None
    remote_dir = None

    def __init__(self, parent=get_maya_window()):
        super(ReSizeDialog, self).__init__(parent)
        self.setObjectName('resize_dialog')
        self.setWindowTitle('Resize Texture')
        self.setWindowFlags(
            QtCore.Qt.Dialog | QtCore.Qt.WindowMinimizeButtonHint)
        self.resize(200, 250)
        self.setMinimumSize(QtCore.QSize(200, 250))
        self.setMaximumSize(QtCore.QSize(200, 250))

        self.mode_frame = QtGui.QFrame(self)
        self.mode_frame.setFrameStyle(
            QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.mode_frame.setMaximumHeight(70)
        self.mode_label = QtGui.QLabel(self)
        self.mode_label.setFrameStyle(
            QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        self.mode_label.setMaximumHeight(25)
        self.mode_label.setSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        self.mode_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mode_label.setAutoFillBackground(True)
        self.mode_label.setBackgroundRole(QtGui.QPalette.Dark)
        self.mode_label.setObjectName('mode_label')
        self.mode_label.setText('Mode')
        self.selected_rb = QtGui.QRadioButton(self)
        self.selected_rb.setObjectName('selected_rb')
        self.selected_rb.setText('Selected')
        self.selected_rb.setChecked(True)
        self.all_rb = QtGui.QRadioButton(self)
        self.all_rb.setObjectName('all_rb')
        self.all_rb.setText('All Textures')
        self.all_rb.setChecked(False)
        self.mode_bg = QtGui.QButtonGroup(self)
        self.mode_bg.addButton(self.selected_rb, 0)
        self.mode_bg.addButton(self.all_rb, 1)

        self.mode_layout = QtGui.QHBoxLayout()
        self.mode_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.mode_layout.addWidget(self.selected_rb)
        self.mode_layout.addWidget(self.all_rb)

        self.mode_frame_layout = QtGui.QVBoxLayout()
        self.mode_frame_layout.setMargin(0)
        self.mode_frame_layout.addWidget(self.mode_label, 1)
        self.mode_frame_layout.addLayout(self.mode_layout, 1)
        self.mode_frame.setLayout(self.mode_frame_layout)

        self.size_frame = QtGui.QFrame(self)
        self.size_frame.setFrameStyle(
            QtGui.QFrame.Box | QtGui.QFrame.Plain)
        self.size_frame.setMaximumHeight(90)
        self.size_label = QtGui.QLabel(self)
        self.size_label.setFrameStyle(
            QtGui.QFrame.Sunken | QtGui.QFrame.StyledPanel)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        self.size_label.setMaximumHeight(25)
        self.size_label.setAutoFillBackground(True)
        self.size_label.setBackgroundRole(QtGui.QPalette.Dark)
        self.size_label.setObjectName('size_label')
        self.size_label.setText('Size')
        self.size_2_rb = QtGui.QRadioButton(self)
        self.size_2_rb.setObjectName('size_2_rb')
        self.size_2_rb.setText('1 / 2')
        self.size_2_rb.setChecked(True)
        self.size_4_rb = QtGui.QRadioButton(self)
        self.size_4_rb.setObjectName('size_4_rb')
        self.size_4_rb.setText('1 / 4')
        self.size_4_rb.setChecked(False)
        self.size_8_rb = QtGui.QRadioButton(self)
        self.size_8_rb.setObjectName('size_8_rb')
        self.size_8_rb.setText('1 / 8')
        self.size_8_rb.setChecked(False)
        self.size_16_rb = QtGui.QRadioButton(self)
        self.size_16_rb.setObjectName('size_16_rb')
        self.size_16_rb.setText('1 / 16')
        self.size_16_rb.setChecked(False)
        self.size_bg = QtGui.QButtonGroup(self)
        self.size_bg.addButton(self.size_2_rb, 0)
        self.size_bg.addButton(self.size_4_rb, 1)
        self.size_bg.addButton(self.size_8_rb, 2)
        self.size_bg.addButton(self.size_16_rb, 3)

        self.size_layout = QtGui.QGridLayout()
        self.size_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.size_layout.addWidget(self.size_2_rb, 0, 0)
        self.size_layout.addWidget(self.size_4_rb, 0, 1)
        self.size_layout.addWidget(self.size_8_rb, 1, 0)
        self.size_layout.addWidget(self.size_16_rb, 1, 1)

        self.size_frame_layout = QtGui.QVBoxLayout()
        self.size_frame_layout.setMargin(0)
        self.size_frame_layout.addWidget(self.size_label, 1)
        self.size_frame_layout.addLayout(self.size_layout, 1)
        self.size_frame.setLayout(self.size_frame_layout)

        self.resize_btn = QtGui.QPushButton(self)
        self.resize_btn.setObjectName('resize_btn')
        self.resize_btn.setText('ReSize')

        self.reset_btn = QtGui.QPushButton(self)
        self.reset_btn.setObjectName('reset_btn')
        self.reset_btn.setText('Reset')

        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.setSpacing(5)
        self.main_layout.addWidget(self.mode_frame)
        self.main_layout.addWidget(self.size_frame)
        self.main_layout.addWidget(self.resize_btn)
        self.main_layout.addWidget(self.reset_btn)

        self.setLayout(self.main_layout)

        self.worker = Worker()

        QtCore.QObject.connect(
            self.mode_bg, QtCore.SIGNAL('buttonClicked(int)'), self.set_mode)
        QtCore.QObject.connect(
            self.size_bg, QtCore.SIGNAL('buttonClicked(int)'), self.set_size)
        self.resize_btn.clicked.connect(self.btn_clicked)
        self.reset_btn.clicked.connect(self.reset_clicked)

    def set_mode(self, id):
        self.mode = id

    def set_size(self, id):
        if id == 0:
            self.index = 2
        elif id == 1:
            self.index = 4
        elif id == 2:
            self.index = 8
        elif id == 3:
            self.index = 16

        self.size_index = float(1.000 / self.index)

    def get_file_nodes(self):
        if self.mode:
            self.file_nodes = mc.ls(type='file', long=True)
            if len(self.file_nodes):
                return True
            else:
                self.show_msg_dialog('The scene not have a file node')
                return False

        del self.file_nodes[:]
        # all_shader = self.get_shader()
        # if len(all_shader):
        #     self.iter_shaders(all_shader)
        #     if len(self.file_nodes):
        #         return True
        #     else:
        #         self.show_msg_dialog(
        #             'The material of the selected objects\n not have a file node')
        #         return False
        # else:
        #     self.show_msg_dialog('Nothing Selected')
        #     return False
        self.file_nodes = mc.ls(type='file', long=True, sl = True)
        if len(self.file_nodes):
                return True
        else:
            self.show_msg_dialog('Nothing Selected')
            return False

    # 递归材质球, 获得 File node
    def iter_shaders(self, all_shader):
        all_file = []
        del all_file[:]

        for each in all_shader:
            all_up_node = mc.hyperShade(lun=each)
            if not len(all_up_node):
                continue

            for each_up_node in all_up_node:
                if mc.nodeType(each_up_node) == 'file':
                    self.file_nodes.append(each_up_node)

    # 获得当前选择物体的材质球
    def get_shader(self):
        allMyShapes = []
        allShapes = mc.ls(
            selection=True, dagObjects=True, shapes=True, rq=True)
        for Shape in allShapes:
            ShapeType = mc.nodeType(Shape)
            if ShapeType == 'mesh' or ShapeType == 'nurbsSurface' or ShapeType == 'subdiv':
                if not mc.getAttr("%s.intermediateObject" % Shape):
                    allMyShapes.append(Shape)
        del allShapes
        allSgs = []
        for MyShape in allMyShapes:
            allAssignSG1 = allAssignSG2 = []
            try:
                allAssignSG1 = mc.listConnections(
                    MyShape + '.instObjGroups.objectGroups', d=True, s=False)
            except:
                pass
            try:
                allAssignSG2 = mc.listConnections(
                    MyShape + '.instObjGroups', d=True, s=False)
            except:
                pass
            if allAssignSG1:
                for each in allAssignSG1:
                    if mc.nodeType(each) == 'shadingEngine':
                        allSgs.append(each)
            if allAssignSG2:
                for each in allAssignSG2:
                    if mc.nodeType(each) == 'shadingEngine':
                        allSgs.append(each)
        allMySg = set(allSgs)
        del allSgs

        allSelShader = []

        for MySg in allMySg:
            eachShader = ''
            try:
                eachShader = mc.listConnections(
                    MySg + '.miShadowShader', s=True, d=False)[0]
            except:
                pass
            else:
                allSelShader.append(eachShader)
            if not eachShader:
                try:
                    eachShader = mc.listConnections(
                        MySg + '.surfaceShader', s=True, d=False)[0]
                except:
                    continue
                else:
                    if mc.nodeType(eachShader) == 'VRayMtl':
                        allSelShader.append(eachShader)
                    elif (mc.nodeType(eachShader) == 'lambert' or
                          mc.nodeType(eachShader) == 'blinn' or
                          mc.nodeType(eachShader) == 'phong' or
                          mc.nodeType(eachShader) == 'phongE' or
                          mc.nodeType(eachShader) == 'surfaceShader' or
                          mc.nodeType(eachShader) == 'anisotropic' or
                          mc.nodeType(eachShader) == 'layeredShader' or
                          mc.nodeType(eachShader) == 'oceanShader'):
                        allSelShader.append(eachShader)
                    elif (mc.nodeType(eachShader) == 'aiHair' or
                          mc.nodeType(eachShader) == 'aiAmbientOcclusion' or
                          mc.nodeType(eachShader) == 'aiStandard'):
                        allSelShader.append(eachShader)
                    else:
                        if mc.nodeType(eachShader) != 'displacementShader':
                            allSelShader.append(eachShader)

        return allSelShader

    def set_new_file(self, node, path):
        try:
            mc.setAttr('%s.fileTextureName' % node, path, type='string')
            mc.setAttr('%s.fileTextureName' % node, path, type='string')
            print path
        except:
            return False

        return True

    def resize_texture(self, node):
        selectionList = om.MSelectionList()
        selectionList.add(node)
        file_obj = om.MObject()
        selectionList.getDependNode(0, file_obj)
        im = om.MImage()
        try:
            im.readFromTextureNode(file_obj)
        except:
            del im
            return False

        width_util = om.MScriptUtil()
        width_util.createFromInt(0)
        width_ptr = width_util.asUintPtr()

        height_util = om.MScriptUtil()
        height_util.createFromInt(0)
        height_ptr = height_util.asUintPtr()
        try:
            im.getSize(width_ptr, height_ptr)
        except:
            im.release()
            return False

        if not self.check_folder():
            return False

        if self.is_writable:
            output_file = [os.path.join(
                           self.file_dir.absolutePath().toLocal8Bit().data(),
                           self.file_name).replace('\\', '/'), self.file_ext]
        else:
            if self.temp_file:
                output_file = [self.temp_file, self.file_ext]
            else:
                return False

        util = om.MScriptUtil()
        width = util.getUint(width_ptr)
        height = util.getUint(height_ptr)
        try:
            im.resize(int(width * self.size_index), int(height * self.size_index))
        except:
            im.release()
            return False

        try:
            output_file_format = str(output_file[1]).lower()
            im.writeToFile(output_file[0],output_file_format)
        except:
            im.release()
            self.show_warning('An error occurred when write a texture file')
            return False

        im.release()
        del im
        return output_file[0]

    def check_folder(self):
        sub_dir = '1_%d' % self.index
        if self.file_dir.cd(sub_dir):
            return True
        else:
            return self.create_folder(sub_dir)

    def create_folder(self, sub_dir):
        if self.is_writable:
            if self.file_dir.mkdir(sub_dir):
                if self.file_dir.cd(sub_dir):
                    return True
                else:
                    self.show_warning('An error occurred when entering a sub-folder')
            else:
                self.show_warning('An error occurred when creating a sub-folder')
        else:
            # 调用外部 CPAU 创建目录
            return True

        return False

    def check_file(self, node):
        tex_path = mc.getAttr('%s.fileTextureName' % node)
        file_info = QtCore.QFileInfo(tex_path)
        self.file_name = file_info.fileName().toLocal8Bit().data()
        self.file_ext = file_info.suffix()
        self.file_dir = file_info.dir()
        self.check_writable(file_info)
        if self.is_writable is False:
            self.temp_file = os.path.join(
                tempfile.gettempdir(), file_info.fileName().toLocal8Bit().data()).replace('/', '\\')
        if self.file_dir.dirName() in ['1_2', '1_4', '1_8', '1_16']:
            return False
        else:
            return True

    def check_writable(self, file_info):
        file_path = os.path.join(self.file_dir.absolutePath().toLocal8Bit().data(), 'check_writable.txt').replace('\\', '/')
        try:
            f = file(file_path, 'w')
        except:
            self.remote_dir = os.path.join(
                file_info.absoluteDir().absolutePath().toLocal8Bit().data(), '1_%d' % self.index).replace('/', '\\')
            self.is_writable = False
        else:
            self.remote_dir = None
            self.is_writable = True
            f.close()
            del f
            try:
                os.remove(file_path)
            except:
                pass

    def btn_clicked(self):
        if self.get_file_nodes():
            self.progress_dialog = QtGui.QProgressDialog(
                'Resizing the pictures...Please wait', 'Cancel', 0, 100, self)
            self.progress_dialog.setWindowTitle('Resizing...')
            self.progress_dialog.setModal(True)
            self.progress_dialog.setRange(1, 100)
            self.progress_dialog.show()
            count = len(self.file_nodes)
            percent = float(1.000 / count) * 100
            progress = 0
            for each in self.file_nodes:
                self.temp_file = None
                if self.check_file(each):
                    self.progress_dialog.setLabelText(each)
                    new_file = self.resize_texture(each)
                    if new_file:
                        if self.is_writable is False:
                            self.worker.ready(self.temp_file, self.remote_dir)
                            while True:
                                if self.worker.wait():
                                    break
                                else:
                                    self.worker.msleep(100)
                            new_file = os.path.join(self.remote_dir, self.file_name).replace('\\', '/')
                        if self.set_new_file(each, new_file):
                            # print new_file
                            pass
                        else:
                            self.show_warning(
                                'Set a new path for the %s is abnormal' % each)
                    else:
                        self.show_warning('%s.fileTextureName is invalid.' % each)
                progress += percent
                self.progress_dialog.setValue(progress)
            self.progress_dialog.setValue(100)
        else:
            return False

    def reset_texture(self, node):
        if self.file_dir.cdUp():
            new_path = os.path.join(self.file_dir.absolutePath().toLocal8Bit().data(),
                                    self.file_name).replace('\\', '/')
            mc.setAttr('%s.fileTextureName' % node, new_path, type='string')

    def reset_clicked(self):
        if self.get_file_nodes():
            for each in self.file_nodes:
                if not self.check_file(each):
                    self.reset_texture(each)

    def show_error(self, msg):
        om.MGlobal.displayError(msg)

    def show_warning(self, msg):
        om.MGlobal.displayWarning(msg)

    def show_msg_dialog(self, msg):
        QtGui.QMessageBox.information(self, 'Information', msg)


class Worker(QtCore.QThread):
    temp_file = None
    remote_dir = None

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)

    def __del__(self):
        self.wait()

    def ready(self, temp, remote):
        self.temp_file = temp
        self.remote_dir = remote
        self.start()

    def run(self):
        cmd = r'%s -u %s -p %s -ex "%s /force_close /cmd=sync \"%s\" /to=\"%s\""' % (
            CPAU_PATH, REMOTE_USER, REMOTE_PWD, FCOPY_PATH, self.temp_file, self.remote_dir)
        # print cmd
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=False)
        p.communicate()
        while True:
            if not subprocess.Popen.poll(p) is None:
                del p
                break
            else:
                self.msleep(100)


# if mc.window("resize_dialog", exists=True):
#     mc.deleteUI("resize_dialog", window=True)
# dialog = ReSizeDialog()
# t = threading.Thread(None, dialog.show())
# t.start()