# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MayaBatchTools_base.ui'
#
# Created: Thu Apr 18 19:17:26 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import console_all_res_rc
from PyQt4 import QtCore, QtGui

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

class Ui_MayaBatchT_win(object):
    def setupUi(self, MayaBatchT_win):
        MayaBatchT_win.setObjectName(_fromUtf8("MayaBatchT_win"))
        MayaBatchT_win.resize(825, 410)
        MayaBatchT_win.setMinimumSize(QtCore.QSize(845, 295))
        MayaBatchT_win.setMaximumSize(QtCore.QSize(850, 500))
        self.centralwidget = QtGui.QWidget(MayaBatchT_win)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.MainTable = QtGui.QTableWidget(self.centralwidget)
        self.MainTable.setMinimumSize(QtCore.QSize(0, 0))
        self.MainTable.setMaximumSize(QtCore.QSize(827, 1116666))
        self.MainTable.setLineWidth(1)
        self.MainTable.setRowCount(15)
        self.MainTable.setObjectName(_fromUtf8("MainTable"))
        self.MainTable.setColumnCount(6)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setItem(0, 0, item)
        # 设置 不能修改 和 整行选择
        self.MainTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.MainTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        # self.MainTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.MainTable.horizontalHeader().setCascadingSectionResizes(False)
        self.MainTable.horizontalHeader().setDefaultSectionSize(100)
        self.MainTable.horizontalHeader().setHighlightSections(True)
        self.MainTable.horizontalHeader().setSortIndicatorShown(False)
        self.MainTable.horizontalHeader().setStretchLastSection(False)
        self.MainTable.verticalHeader().setVisible(False)
        self.MainTable.verticalHeader().setDefaultSectionSize(19)
        self.gridLayout.addWidget(self.MainTable, 0, 0, 1, 1)
        MayaBatchT_win.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MayaBatchT_win)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MayaBatchT_win.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MayaBatchT_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MayaBatchT_win.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MayaBatchT_win)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MayaBatchT_win.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.mis_run = QtGui.QAction(MayaBatchT_win)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/console_res/cnsl_go.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mis_run.setIcon(icon)
        self.mis_run.setObjectName(_fromUtf8("mis_run"))
        self.mis_end = QtGui.QAction(MayaBatchT_win)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/console_res/cnsl_stp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mis_end.setIcon(icon1)
        self.mis_end.setObjectName(_fromUtf8("mis_end"))
        self.mis_ref = QtGui.QAction(MayaBatchT_win)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/console_res/console_icon_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mis_ref.setIcon(icon2)
        self.mis_ref.setObjectName(_fromUtf8("mis_ref"))
        self.mis_clear = QtGui.QAction(MayaBatchT_win)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/console_res/console_icon_clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mis_clear.setIcon(icon3)
        self.mis_clear.setObjectName(_fromUtf8("mis_clear"))
        #add  minus action ==========================
        self.mis_minus = QtGui.QAction(self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/console_res/cnsl_minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mis_minus.setIcon(icon4)
        self.mis_minus.setObjectName("mis_minus")
        #add a toolbutton -------------------
        self.mis_add_bt = QtGui.QToolButton(self)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbar/console_res/cnsl_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mis_add_bt.setIcon(icon5)
        self.mis_add_bt.setIconSize(QtCore.QSize(24, 24))
        self.mis_add_bt.setObjectName("mis_add_bt")
        self.mis_add_bt.setBaseSize(QtCore.QSize(24, 24))
        self.mis_add_bt.setAutoRaise(True)
        # add a select mode toggle button
        self.emptyWidget = QtGui.QWidget(MayaBatchT_win)
        self.emptyWidget.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        self.emptyWidget.setBaseSize(100,5)

        self.mis_selCk = QtGui.QCheckBox(MayaBatchT_win)
        self.mis_selCk.setCheckable(True)
        self.mis_selCk.setObjectName(_fromUtf8("mis_selCk"))

        #check mission button for CHECK not show to user
        self.mis_td = QtGui.QAction(self)
        self.mis_td.setObjectName("mis_td")
        self.mis_td.setText("TD CHEK")

        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.mis_add_bt)#--add toolbutton
        self.toolBar.addAction(self.mis_run)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.mis_end)
        self.toolBar.addAction(self.mis_ref)
        self.toolBar.addAction(self.mis_clear)
        self.toolBar.addAction(self.mis_minus)
        self.toolBar.addSeparator()
        if os.getenv("username") in ['zhangben']:
            self.toolBar.addAction(self.mis_td)
        self.toolBar.addWidget(self.emptyWidget)
        self.toolBar.addWidget(self.mis_selCk)



        self.menu_tb = QtGui.QMenu()
        self.menu_tb.setObjectName('menu_tb')
        self.mis_add_bt.setMenu(self.menu_tb)

        self.retranslateUi(MayaBatchT_win)
        QtCore.QMetaObject.connectSlotsByName(MayaBatchT_win)

    def retranslateUi(self, MayaBatchT_win):
        MayaBatchT_win.setWindowTitle(_translate("MayaBatchT_win", "OCT Console", None))
        item = self.MainTable.horizontalHeaderItem(0)
        item.setText(_translate("MayaBatchT_win", "状态", None))
        item = self.MainTable.horizontalHeaderItem(1)
        item.setText(_translate("MayaBatchT_win", "任务", None))
        item = self.MainTable.horizontalHeaderItem(2)
        item.setText(_translate("MayaBatchT_win", "操作", None))
        item = self.MainTable.horizontalHeaderItem(3)
        item.setText(_translate("MayaBatchT_win", "开始时间", None))
        item = self.MainTable.horizontalHeaderItem(4)
        item.setText(_translate("MayaBatchT_win", "结束时间", None))
        __sortingEnabled = self.MainTable.isSortingEnabled()
        self.MainTable.setSortingEnabled(False)
        self.MainTable.setSortingEnabled(__sortingEnabled)
        self.menu.setTitle(_translate("MayaBatchT_win", "添加任务", None))
        self.menu_2.setTitle(_translate("MayaBatchT_win", "启动", None))
        self.menu_3.setTitle(_translate("MayaBatchT_win", "结束", None))
        self.toolBar.setWindowTitle(_translate("MayaBatchT_win", "toolBar", None))
        self.mis_run.setText(_translate("MayaBatchT_win", "全部", None))
        self.mis_end.setText(_translate("MayaBatchT_win", "停止", None))
        self.mis_ref.setText(_translate("MayaBatchT_win", "referesh", None))
        self.mis_ref.setToolTip(_translate("MayaBatchT_win", "refresh", None))
        self.mis_clear.setText(_translate("MayaBatchT_win", "Clear", None))
        self.mis_clear.setToolTip(_translate("MayaBatchT_win", "cleare missions", None))
        self.mis_selCk.setText(_translate("MayaBatchT_win", "只运行选择的任务 勾我", None))
        self.mis_selCk.setToolTip(_translate("MayaBatchT_win", "Select Mode", None))
        self.mis_minus.setText(_translate("MayaBatchT_win", "minus mission", None))

