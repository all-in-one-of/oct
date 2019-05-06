#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = MayaBatchTools.py
__author__ = zhangben 
__mtime__ = 2019/4/13 : 16:10
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""
print("I am MayaBatchTools")
import copy,os,re,sys,subprocess,time,_winreg
from PyQt4 import QtGui,QtCore
import xml.etree.ElementTree as ET
import datetime
import qdarkstyle

# sys.path.append(r"F:\Development\octProj\oct\maya_sixteen\Python")
# reload(sys)
# sys.setdefaultencoding('utf-8')
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# from OCT_Pipeline.scripts.utility.MayaBatchConsole.ui import MayaBatchTools_base_ui
import MayaBatchTools_base_ui

reload(MayaBatchTools_base_ui)

# FILE_LOC = os.path.dirname(os.path.realpath('__file__'))
FILE_LOC = os.path.dirname(os.path.abspath(sys.argv[0]))
print FILE_LOC

print("load all need modules!!!!!!!!!!!!!")

def GetMayaRootPath(mayaVer = 2016):
    # aReg = _winreg.ConnectRegistry(None,_winreg.HKEY_LOCAL_MACHINE)
    aKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Autodesk Maya {}".format(mayaVer))
    value = _winreg.QueryValueEx(aKey,'InstallLocation')
    return value

# FILE_LOC = os.path.dirname(os.path.realpath('__file__'))
# FILE_LOC = os.path.split(__file__)[0]
# FILE_LOC = os.path.dirname(os.path.abspath(sys.argv[0]))
# print FILE_LOC
MAYA_ROOT_DIR = GetMayaRootPath()

class MayaBatchTools(QtGui.QMainWindow, MayaBatchTools_base_ui.Ui_MayaBatchT_win):
    def __init__(self ):
        super(MayaBatchTools,self).__init__()
        self.setupUi(self)
        self.MainTable.horizontalHeader().resizeSection(0, 50)
        self.MainTable.horizontalHeader().resizeSection(1, 350)
        self.MainTable.horizontalHeader().resizeSection(2, 100)
        self.MainTable.horizontalHeader().resizeSection(3, 150)
        self.MainTable.horizontalHeader().resizeSection(4, 150)
        self.MainTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed) # pyqt4
        # self.MainTable.horizontalHeader().setSectionResizeMode(0,QtGui.QHeaderView.) # pyqt5
        # self.palette = QtGui.QPalette()
        # self.palette.setColor(QtGui.QPalette.background,QtCore.Qt.red)
        # self.setPalette(palette)
        # =======   about system command part=========================
        self.thread = None
        self.menuLoc = {'menu':'MN','menu_tb':'TB','menu_pop':'POP'}
        self.cwd = os.getcwd()
        self.xml_file = os.path.abspath(os.path.join(FILE_LOC, 'MayabatchConsole.xml'))
        self.cmdGather = {}
        self.missions = []
        self.missions_dict = {}
        self.missioned = []
        self.missioned_dict = {}
        self.newAddMissions = []
        # ========= about sub process =====================
        self.allThreads = []
        #======= call sub window output======================
        self.optwin = None
        # ========== config relative fuctions=========================
        self._configMenu(self.menu)
        self._configMenu(self.menu_tb)
        self.menu.triggered[QtGui.QAction].connect(self.parseCmd)
        self.menu_tb.triggered[QtGui.QAction].connect(self.parseCmd)
        self.toolBar.actionTriggered[QtGui.QAction].connect(self.toolbar_run)
        # self.toolBar.actionTriggered[QtGui.QAction].connect(self.debug_cmd)
        # self.toolBar.actionTriggered[QtGui.QAction].connect(self.bar_bt_cmd)
        # self.startMis_mnac.triggered().connect(self.run)
        # self.button_cmd_connect()
        # if os.getenv('username') in ['zhangben']:
        #     mis_minus = QtGui.QAction(self)
        #     icon1 = QtGui.QIcon()
        #     icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/console_res/cnsl_minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #     mis_minus.setIcon(icon1)
        #     mis_minus.setObjectName("mis_minus")
        #     self.toolBar.addAction(mis_minus)
        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
        self.move(1050,540)
        self.show()
        # print self.cmdGather

    def _configMenu(self,pmenu,loc = None,mode=None,root=None):# set menu
        if not loc: loc = self.menuLoc[str(pmenu.objectName())]
        modeList = ['Maya Batch','Checkin']
        if root == None:
            tree = ET.parse(self.xml_file)
            root = tree.getroot()
        if not len(root): return
        # if not root.attrib: pmenu = self.menu
        # pmenu_nm = pmenu.objectName()
        if root.attrib.has_key('label') and root.attrib['label'] in modeList: mode = root.attrib['label']
        for ea in root:
            if ea.tag == 'menuItem':
                if ea.attrib.has_key('label'):
                    addAct = QtGui.QAction(self)
                    addAct.setObjectName(u'{}_{}'.format((loc),self.name_trans(ea.attrib['label'])))
                    addAct.setText(ea.attrib['label'])
                    pmenu.addAction(addAct)
                    self.cmdGather[addAct.objectName()] = ea.attrib
                    self.cmdGather[addAct.objectName()].update({'pMenu':pmenu.objectName(),'mode':mode})
                    if mode == 'Maya Batch': self.cmdGather[addAct.objectName()].update({'filter':"Maya Files (*.ma *.mb)"})
                    # elif mode == 'Checkin' :
                    #     # print ("  checkin menu  items : \n")
                    #     # print ea.attrib
                    #     if ea.attrib.has_key['class']:
                    # print self.cmdGather
                elif ea.attrib.has_key('divider'):
                    pmenu.addSeparator()
            elif ea.tag == 'menu':
                nmstr = ea.attrib['label']
                addMenu = QtGui.QMenu(pmenu)
                addMenu.setObjectName(u'{}_{}'.format(loc,self.name_trans(nmstr)))
                addMenu.setTitle(nmstr)
                pmenu.addAction(addMenu.menuAction())
                self._configMenu(addMenu,loc,mode,ea)


    def parseCmd(self,q):# 选择文件后 整理所有 commands
        actnm = q.objectName()
        commandMode = self.cmdGather[actnm]['mode']
        maya_batch_path = re.sub(r'\\', '/', os.path.abspath(os.path.join(MAYA_ROOT_DIR[0], r'bin\mayabatch.exe')))
        cmdStr = self.cmdGather[actnm]['command'] if self.cmdGather[actnm].has_key('command') else self.cmdGather[actnm]['class']
        _filter = self.cmdGather[actnm]['filter'] if self.cmdGather[actnm].has_key('filter') else 'All Files (*)'
        # exec_cmd = "{} -command \"{}\" -log \"e:/dev_output/wtfwtfwtf.log\"".format(maya_batch_path,cmdStr)
        exec_cmd = "\"{}\" -command \"{}\" ".format(maya_batch_path,cmdStr) if commandMode == 'Maya Batch' else cmdStr
        pfm_cmd = {actnm:[exec_cmd,commandMode]}
        print ("line 132 ",pfm_cmd)
        # self.slot_btn_chooseMutiFile()
        sel_files = QtGui.QFileDialog.getOpenFileNames(self,u"选那些要处理的文件们",r"E:\work\JMWC\scenes",  # 起始路径
                                                  _filter,None,
                                                  QtGui.QFileDialog.DontUseNativeDialog)
        for ea_file in sel_files:
            file_nm = os.path.split(str(ea_file))[-1]
            perform_command = re.sub('%s',"\\\"{}\\\"".format(str(ea_file)),pfm_cmd[actnm][0])
            if pfm_cmd[actnm][1] == 'Checkin': perform_command = '{} {}'.format(pfm_cmd[actnm][0],ea_file)
            missions_count = len(self.missions)
            if perform_command not in self.missions:
                self.missions.append(perform_command)## 因为字典是无需的，所以需要个list 来记录 要执行的任务
                # self.missions_dict[perform_command] = [pfm_cmd[actnm][0],file_nm,pfm_cmd[actnm][1]]
                self.missions_dict[perform_command] = {'fileName':file_nm,'mode':pfm_cmd[actnm][1],'state':'add','id':"{:05d}".format(missions_count)}
                self.newAddMissions.append(perform_command) ## 新添加的任务
                print perform_command

        self.add_rows()

    def toolbar_run(self,q):# tool bar 按钮们运行 命令
        # print(os.linesep.join(sys.path))
        if str(q.objectName()) == "mis_clear":# 清除所有任务列表
            self.MainTable.clearContents()
            self.missions = []
            self.missions_dict.clear()
        elif str(q.objectName()) == "mis_run":# 运行
            self._cmd_mis_run(q)
        elif str(q.objectName()) == "mis_end":#停止
            self.thread.stop()
        elif str(q.objectName()) == "mis_minus":
            self._cmd_mis_minus()
        elif str(q.objectName()) == "mis_td":
            self.tdCk_cmd()
        else:
            self.bar_bt_cmd(q)

    def tdCk_cmd(self):# td test action cmd
        print("{0}>>>check: part 1 ----------------{0}".format(os.linesep))
        screen = QtGui.QDesktopWidget().screenGeometry()
        print screen.width()
        print screen.height()
        # print len(self.missions)
        #
        # for ea in self.missions:
        #     print self.missions_dict[ea]
        print("{0}>>>check: part 2 ----------------{0}".format(os.linesep))
        print self.pos().x()
        print self.pos().y()

        print("{0}>>>check: part 3 ----------------{0}".format(os.linesep))
        desktop = QtGui.QApplication.desktop()
        print(desktop.screenCount())
        screen_rect = desktop.screenGeometry(0)
        available_rect = desktop.availableGeometry(0)
        print("MAJOR MONITOR: ",screen_rect,"   ",available_rect)
        screen_rect_2 = desktop.screenGeometry(1)
        available_rect_2 = desktop.availableGeometry(1)
        print("MINOR MONITOR: ",screen_rect_2,"   ",available_rect_2)

    def set_optWin_position(self):#设置 输出窗口 的出现位置
        desktop = QtGui.QApplication.desktop()
        print(desktop.screenCount())
        screen_rect = desktop.screenGeometry(0)
        available_rect = desktop.availableGeometry(0)
        print("MAJOR MONITOR: ", screen_rect, "   ", available_rect)
        screen_rect_2 = desktop.screenGeometry(1)
        available_rect_2 = desktop.availableGeometry(1)
        print("MINOR MONITOR: ", screen_rect_2, "   ", available_rect_2)
        # sel_id = self.sel_rows_ids()
        # print sel_id
        # for ea in self.sel_rows_ids():
        #     # print ea
        #     mis_cell = self.MainTable.item(ea, 5)
        #     if not mis_cell or str(mis_cell.text()) == "":
        #         print(u"你选择了空行，没有任务")
        #         continue
        #     mis_str = str(mis_cell.text())
        #     print self.missions_dict[mis_str]


    def _cmd_mis_run(self,q): # run action connected function
        # self.optwin = optUI(self)
        # self.optwin.show()
        self.call_opt()
        self.thread = PerformCmdThread(self)
        self.thread.dispSignal.connect(self._prnt)
        self.thread.start()
        self.allThreads.append(self.thread)

    def _prnt(self,val):#run  thread signal connect fuction
        opt = self.optwin.opt_txt
        cursor = opt.textCursor()
        # for ea in self.missions:
        cursor.movePosition(cursor.End)
        val_str = map(str,val)
        if val_str[0].startswith('>>>'):
            cursor.insertText("{}{}".format(unicode(val[0]), os.linesep))
        elif val_str[0].startswith('<<<'):
            mis = re.sub("^<<<","",val_str[0])
            id = self.missions.index(mis)
            prevMis = self.missions[id-1] if id != 0 else None
            self.missions_dict[mis]['state'] = val_str[1]
            self.config_column_0(self.missions_dict[mis]['rowId'], status=val_str[1])  # 配置行首图标#  done  error  running watting
            # if prevMis and self.missions_dict[prevMis]['state'] == 'running': self.missions_dict[prevMis]['state'] = 'done'
            # if prevMis and self.missions_dict[prevMis]['state'] == 'running': self.missions_dict[prevMis]['state'] = 'done'
        else:
            cursor.insertText("{}{}".format(val[1],os.linesep))


    def slotStopAllThread(self):
        for thread in self.allThreads:
            if thread.isRunning():
                thread.stop()
        del self.allThreads[:]

    def _cmd_mis_minus(self):
        sel_id = self.sel_rows_ids()
        print sel_id
        for ea in self.sel_rows_ids():
            # print ea
            mis_cell = self.MainTable.item(ea, 5)
            if not mis_cell or str(mis_cell.text()) == "":
                print(u"你选择了空行，没有任务")
                continue
            mis_str = str(mis_cell.text())
            self.MainTable.removeRow(ea)
            self.refresh_varis(mis_str)
        self.refresh_mis_rowid()

    def sys_cmd(self,id,mis_str):#运行系统命令行命令 配置 table 任务相关行的 内容
        cur_1 = datetime.datetime.now()
        st_time = cur_1.strftime('%y-%m-%d %H:%M:%S')
        self.MainTable.setItem(id,3,QtGui.QTableWidgetItem(QtCore.QString("{}".format(st_time))))
        self.config_column_0(id, status='running')
        import time
        time.sleep(5)
        # subprocess.Popen(mis_str)
        print("some prcedure running")
        time.sleep(5)
        cur_2 = datetime.datetime.now()
        end_time = cur_2.strftime('%y-%m-%d %H:%M:%S')
        self.MainTable.setItem(id, 4, QtGui.QTableWidgetItem(QtCore.QString("{}".format(end_time))))
        self.config_column_0(id, status='done')
    def call_opt(self,close=False):## output window
        if close:
            if self.optwin: self.optwin.close()
            else: self.optwin = opt_dialog()
        else:
            if not self.optwin:  self.optwin = opt_dialog()
        self.optwin.show()
        # return self.optwin
    def sel_rows_ids(self):# 获得选择的 任务行标
        sel_inds = self.MainTable.selectedIndexes()
        rows = len(sel_inds) / 6
        if not len(sel_inds):return None
        elif len(sel_inds) == 6 : return [sel_inds[0].row()]
        if sel_inds[0].row() != sel_inds[1].row():  return [eaInd.row() for eaInd in sel_inds[:rows]]
        else: return [eaInd.row() for eaInd in sel_inds[::6]]


    def bar_bt_cmd(self,q): # 测试
        print self.get_insertIndxs()
    #     # colPos = self.MainTable.columnCount()
    #     # self.MainTable.insertColumn(colPos)
    #     # print self.MainTable.selectedIndexes()
    #     # sel_rangs =  self.MainTable.selectedRanges()
    #     print("--------------------")
    #     for eaInd in self.MainTable.selectedIndexes():
    #         print eaInd.row()
    #         self.add_rows(eaInd.row())
    def refresh_varis(self,mis):
        mis_describe = copy.deepcopy(self.missions_dict[mis])
        self.missions.remove(mis)
        self.missions_dict.pop(mis)
        print("Miss ID : {} removed!===========".format(mis_describe['id']))

    def refresh_mis_rowid(self):# 更新 行索引值
        for n in range(self.MainTable.rowCount()):
            mis_nm = self.MainTable.item(n, 5)
            if not mis_nm or str(mis_nm.text()) == "": continue

            self.missions_dict[str(mis_nm.text())]['rowId'] = n

    def add_rows(self):# 配置所有行的内容
        add_mis_count = len(self.newAddMissions)
        tmp_addmis = copy.deepcopy(self.newAddMissions)
        insert_pos = self.get_insertIndxs()
        # print ("line 185----",insert_pos)
        for n in range(add_mis_count):
            line_1 = insert_pos[0] + n
            print ("+++++++++++++")
            # print self.newAddMissions[n]
            self.config_single_row(line_1,tmp_addmis[n])
            self.newAddMissions.remove(tmp_addmis[n])

        # self.MainTable.setItem(rowId,0,QtGui.QTableWidgetItem(QtCore.QString("{}".format(rowId))))
    def config_single_row(self,rowId,mis): # 配置 一行的内容
        if rowId + 1 >= self.MainTable.rowCount():
            self.MainTable.insertRow(self.MainTable.rowCount())
        #add column 0
        self.config_column_0(rowId)
        # column 1
        # print self.missions_dict[mis[rowId]]
        tx = self.missions_dict[mis]['fileName']
        self.MainTable.setItem(rowId, 1, QtGui.QTableWidgetItem(QtCore.QString("{}".format(tx))))
        #column 2
        misMode = self.missions_dict[mis]['mode']
        self.MainTable.setItem(rowId, 2, QtGui.QTableWidgetItem(QtCore.QString("{}".format(misMode))))
        #column 5
        self.MainTable.setItem(rowId, 5, QtGui.QTableWidgetItem(QtCore.QString("{}".format(mis))))
        self.missions_dict[mis]['state'] = 'added'
        self.missions_dict[mis]['rowId'] = rowId
        print("Mission recored on TABLE: {}".format(self.missions_dict[mis]['id']))

    def get_insertIndxs(self):# 获得增加行的索引
        start_id = 0
        mis_counts = len(self.missions)
        end_id = mis_counts
        rows = self.MainTable.rowCount()
        table_stat = self.get_non_emptyRows(rows)
        emp_rows = len(table_stat['empt'])
        no_emp_rows = len(table_stat['non_em'])
        if no_emp_rows: start_id = no_emp_rows
        if mis_counts > emp_rows:
            add_num = mis_counts - emp_rows
            end_id = start_id + add_num -1
        return [start_id,end_id]

    def iconLabel(self):# 图标+文字 组合一个空间  暂未启用
        print ("------------------")
        iclb_w = QtGui.QWidget()
        layout = QtGui.QHBoxLayout()
        label = QtGui.QLabel()
        title = QtGui.QLabel("wild Lion's Browser")
        pixmap = QtGui.QPixmap(':cell/console_res/cell_ic_waitting.png')
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)
        title.setMinimumHeight(pixmap.height())
        title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(title)
        iclb_w.setLayout(layout)
        return iclb_w

    def config_column_0(self,row,status = 'waitting'):#配置行首图标#  done  error  running watting
        pic_lab = QtGui.QLabel()
        pic_lab_pixmap = QtGui.QPixmap(':cell/console_res/cell_ic_{}.png'.format(status))
        pic_lab.setPixmap(pic_lab_pixmap)
        pic_lab.setAlignment(QtCore.Qt.AlignCenter)
        pic_lab.setScaledContents(True)
        self.MainTable.setCellWidget(row, 0, pic_lab)

    def refresh_table(self):# 刷新 table
        mis_counts = len(self.missions_dict)
        rows = self.MainTable.rowCount()
        table_stat = self.get_non_emptyRows(rows)
        emp_rows = len(table_stat['empt'])
        if mis_counts > emp_rows: self.MainTable.setRowCount(mis_counts)


    def get_non_emptyRows(self,rows):## 当前table 中的信息数据
        # rows = self.MainTable.rowCount()
        cur_items ={'non_em':{},'empt':{}}
        for i in range(rows):
            it = self.MainTable.item(i,1)
            if it and it.text():
                cur_items['non_em'][i] = it.text()
            else:
                cur_items['empt'][i] = i
        return cur_items


    def debug_cmd(self,q):
        # row_count = self.MainTable.rowCount()
        # print row_count
        # column_count =self.MainTable.columnCount()
        # print column_count
        print(self.MainTable.currentIndex().row())




    def name_trans(self,nameStr):# trans label string to a python variable name string
        return re.sub(' ','_',nameStr)

    def __configMenu_abandon_(self,pmenu,menuDic):# set menu  abandon
    # self.menuInfoDic = {'menu': {'Maya Batch': {'menu': {'TD Test': {'menuItem': {'test 01':"what else"}},'TD Test2': {'menuItem': {'test 02':"what else"}}}}},
    #                     'menuItem': {"hahah":"print(\'ok\')"}}
    #
    # self.menuInfoDic = {'menu': {'label':'Maya Batch','menu': {'label':'TD Test','menuItem': {'test 01': "what else"}},
    #                                                         'TD Test2': {'menuItem': {'test 02': "what else"}}},
    #                     'menuItem': {"hahah": "print(\'ok\')"}}

    # self.menuInfoDic = {'menu': {'label': 'Maya Batch', 'menu': {'label': 'TD Test', 'menuItem': {'label':u'测试','command':"what else"}}},
    #                     'menuItem': {"hahah": "print(\'ok\')"}}
    #menuDic = self.menuInfoDic
        if menuDic.has_key('menu'):
            for each_mn in menuDic['menu']:
                addMenu = QtGui.QMenu(pmenu)
                addMenu.setObjectName(self.name_trans(each_mn))
                addMenu.setTitle(each_mn)
                pmenu.addAction(addMenu.menuAction())
                self.__configMenu__(addMenu, menuDic['menu'][each_mn])
        if menuDic.has_key('menuItem'):
            for each_ac in menuDic['menuItem']:
                addAct = QtGui.QAction(self)
                addAct.setObjectName(self.name_trans(each_ac))
                addAct.setText(each_ac)
                pmenu.addAction(each_ac)


class opt_dialog(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(opt_dialog, self).__init__(parent)
        self.resize(800,400)
        self.myQWidget = QtGui.QWidget()
        self.setCentralWidget(self.myQWidget)
        self.hly = QtGui.QVBoxLayout()
        self.myQWidget.setLayout(self.hly)
        self.opt_txt = QtGui.QTextEdit(self)
        self.opt_txt.setMinimumSize(QtCore.QSize(350, 600))
        self.opt_txt.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.opt_txt.setOverwriteMode(False)
        self.opt_txt.setObjectName("opt_txt")
        self.hly.addWidget(self.opt_txt)

        self.clbtn = QtGui.QPushButton('clear contents',self)
        self.hly.addWidget(self.clbtn)

        self.clbtn.clicked.connect(self.opt_txt.clear)

        self.setWindowTitle('command output')
        self.move(10,10)

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())

class PerformCmdThread(QtCore.QThread):
    dispSignal = QtCore.pyqtSignal(list)
    def __init__(self,parent=None):
        super(PerformCmdThread,self).__init__(parent)
        # self.mis_dict = mis_dict #当前线程序号
        # self.cmdStr = parent.cmd
        self.keepRunning = True #当前线程是否进行
        self.p = parent
        self.proc = QtCore.QProcess()
    def stop(self):
        self.keepRunning = False
    def run(self):
        misLst = self.p.missions
        misDict = copy.deepcopy(self.p.missions_dict)
        phy_id = int(self.currentThreadId())
        i = 1
        mis_count = len(misLst)
        if not mis_count:
            self.dispSignal.emit([">>>WAITING ADD MISSIONS......"])
            return
            # self.p.call_opt()
        optwin = self.p.optwin
        # while self.keepRunning:
            # i = i + 1
            # self.dispSignal.emit("Thread {} --> ( Physical ID = {:>5},val = {}）".format(self.number,phy_id,self.cmdStr ))
        for ea in misLst:
            if not self.keepRunning:
                self.dispSignal.emit([">>>MISSIONS ABORTED......"])
                return
            if not misDict[ea]['state'] == 'added':
                continue
            # while self.keepRunning:
            signalLst = ["<<<{}".format(ea),'running']
            self.dispSignal.emit(signalLst)
            # time.sleep(3)
            # self.dispSignal.emit("Thread {} --> ( Physical ID = {:>5},val = {})".format(misDict[ea]['id'],phy_id,ea))

            # self.runSubProc("print \"hello world\" ")
            ret = self.runSubpr(ea)

            if re.search('error:',ret,re.I):
                self.dispSignal.emit(["<<<{}".format(ea), 'error'])
            else:
                self.dispSignal.emit(["<<<{}".format(ea),'done'])
            i +=1
            # self.msleep(500)
            # self.keepRunning = False
        self.dispSignal.emit([">>>ALL MISISIONS COMPLETE...<<<"]  )
        self.keepRunning = True
    def runSubpr(self,per_cmd):# 运行系统命令，获得返回值
        # print per_cmd
        optTx = self.p.optwin.opt_txt
        cursor = optTx.textCursor()
        grab_return = []
        p = subprocess.Popen(per_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,shell=True)
        LAST_RET = None
        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            opt = line.decode('cp936').encode(encoding='UTF-8')
            if line:
                grab_return.append(opt)
                self.dispSignal.emit([per_cmd,opt])
                # for ea in self.missions:
                # cursor.movePosition(cursor.End)
                # cursor.insertText(line)
                LAST_RET = line
        return LAST_RET
    # def readOpt(self):
    #     self.p.optwin.opt_txt.append(QtCore.QString(self.proc.readyReadStandardOutput()))
    # @pyqtSlot()
    # def readStdOutput(self):
    #     self.p.optwin.opt_txt.append(QtCore.QString(self.proc.readAllStandardOutput()))
    #
    # def runSubProc(self,cmdStr):
    #     # self.proc.readyReadStandardOutput.connect
    #     self.proc.start(cmdStr)
    #     self.proc.setProcessChannelMode(QtCore.QProcess.MergedChannels)
    #     QtCore.QObject.connect(self.proc,QtCore.SIGNAL("readyReadStandardOutPut()"),self.proc,QtCore.SLOT("readStdOutput()"))






class optUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(optUI, self).__init__(parent)
        self.p = parent
        self.initUI()

    def initUI(self):
        self.resize(800,400)
        lyt = QtGui.QVBoxLayout()

        self.opt = QtGui.QTextEdit()
        self.runbt = QtGui.QPushButton('Run')
        self.runbt.clicked.connect(self.callProgram)

        lyt.addWidget(self.opt)
        lyt.addWidget(self.runbt)

        centralWidget = QtGui.QWidget()
        centralWidget.setLayout(lyt)
        self.setCentralWidget(centralWidget)

        self.process = QtCore.QProcess(self)
        self.process.readyRead.connect(self.dataReady)

        # self.process.start.connect()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
        self.move(100,100)


    def callProgram(self,cmdStrLst):
        self.process.start("ping",['127.0.0.1'])

    def runPro(self):
        misLst = self.p.missions
        misDict = copy.deepcopy(self.p.missions_dict)
        phy_id = int(self.currentThreadId())
        i = 1
        mis_count = len(misLst)
        if not mis_count:
            self.dispSignal.emit([">>>WAITING ADD MISSIONS......"])
            return
            # self.p.call_opt()
        optwin = self.p.optwin
        # while self.keepRunning:
            # i = i + 1
            # self.dispSignal.emit("Thread {} --> ( Physical ID = {:>5},val = {}）".format(self.number,phy_id,self.cmdStr ))
        for ea in misLst:
            if not self.keepRunning:
                self.dispSignal.emit([">>>MISSIONS ABORTED......"])
                return
            if not misDict[ea]['state'] == 'added':
                continue
            # while self.keepRunning:
            signalLst = [ea,'running']
            self.dispSignal.emit(signalLst)
            # time.sleep(3)
            # self.dispSignal.emit("Thread {} --> ( Physical ID = {:>5},val = {})".format(misDict[ea]['id'],phy_id,ea))

            self.runSubProc("print \"hello world\" ")

            self.dispSignal.emit([ea,'done'])
            i +=1
            self.msleep(500)
            # self.keepRunning = False
        self.dispSignal.emit([">>>ALL MISISIONS COMPLETE...<<<"]  )
        self.keepRunning = True
    # def runSubpr(self,per_cmd):# 运行系统命令，获得返回值
    #     grab_return = []
    #     p = subprocess.Popen(per_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,shell=True)
    #     while p.poll() is None:
    #         line = p.stdout.readline()
    #         line = line.strip()
    #         opt = line.decode('cp936').encode(encoding='UTF-8')
    #         if line:
    #             grab_return.append(opt)
    #     return grab_return


    def dataReady(self):
        cursor = self.opt.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(self.process.readAll().data().decode('gb18030'))
        self.opt.ensureCursorVisible()












if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    widget = MayaBatchTools()
    # widget.resize(400, 300)
    widget.show()
    widget.raise_()

    sys.exit(app.exec_())
