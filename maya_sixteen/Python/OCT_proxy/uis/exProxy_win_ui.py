# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exProxy_win.ui'
#
# Created: Thu Mar 28 11:11:11 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_exchProxyWin(object):
    def setupUi(self, exchProxyWin):
        exchProxyWin.setObjectName(_fromUtf8("exchProxyWin"))
        exchProxyWin.resize(438, 324)
        exchProxyWin.setMaximumSize(QtCore.QSize(440, 325))
        self.ctWidget = QtGui.QWidget(exchProxyWin)
        self.ctWidget.setObjectName(_fromUtf8("ctWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.ctWidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.mainWidget = QtGui.QWidget(self.ctWidget)
        self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sel_grp_bx = QtGui.QGroupBox(self.mainWidget)
        self.sel_grp_bx.setObjectName(_fromUtf8("sel_grp_bx"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.sel_grp_bx)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sel_rb = QtGui.QRadioButton(self.sel_grp_bx)
        self.sel_rb.setChecked(True)
        self.sel_rb.setObjectName(_fromUtf8("sel_rb"))
        self.sel_all_grp = QtGui.QButtonGroup(exchProxyWin)
        self.sel_all_grp.setObjectName(_fromUtf8("sel_all_grp"))
        self.sel_all_grp.addButton(self.sel_rb)
        self.horizontalLayout_2.addWidget(self.sel_rb)
        self.all_rb = QtGui.QRadioButton(self.sel_grp_bx)
        self.all_rb.setObjectName(_fromUtf8("all_rb"))
        self.sel_all_grp.addButton(self.all_rb)
        self.horizontalLayout_2.addWidget(self.all_rb)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.sel_grp_bx)
        self.src_grp_bx = QtGui.QGroupBox(self.mainWidget)
        self.src_grp_bx.setObjectName(_fromUtf8("src_grp_bx"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.src_grp_bx)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.src_ar_rb = QtGui.QRadioButton(self.src_grp_bx)
        self.src_ar_rb.setChecked(True)
        self.src_ar_rb.setObjectName(_fromUtf8("src_ar_rb"))
        self.srcGrp = QtGui.QButtonGroup(exchProxyWin)
        self.srcGrp.setObjectName(_fromUtf8("srcGrp"))
        self.srcGrp.addButton(self.src_ar_rb)
        self.horizontalLayout_4.addWidget(self.src_ar_rb)
        self.src_vr_rb = QtGui.QRadioButton(self.src_grp_bx)
        self.src_vr_rb.setObjectName(_fromUtf8("src_vr_rb"))
        self.srcGrp.addButton(self.src_vr_rb)
        self.horizontalLayout_4.addWidget(self.src_vr_rb)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.src_grp_bx)
        self.targ_grp_bx = QtGui.QGroupBox(self.mainWidget)
        self.targ_grp_bx.setObjectName(_fromUtf8("targ_grp_bx"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.targ_grp_bx)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.targ_ar_rb = QtGui.QRadioButton(self.targ_grp_bx)
        self.targ_ar_rb.setObjectName(_fromUtf8("targ_ar_rb"))
        self.targGrp = QtGui.QButtonGroup(exchProxyWin)
        self.targGrp.setObjectName(_fromUtf8("targGrp"))
        self.targGrp.addButton(self.targ_ar_rb)
        self.horizontalLayout.addWidget(self.targ_ar_rb)
        self.targ_vr_rb = QtGui.QRadioButton(self.targ_grp_bx)
        self.targ_vr_rb.setChecked(True)
        self.targ_vr_rb.setObjectName(_fromUtf8("targ_vr_rb"))
        self.targGrp.addButton(self.targ_vr_rb)
        self.horizontalLayout.addWidget(self.targ_vr_rb)
        self.targ_mod_rb = QtGui.QRadioButton(self.targ_grp_bx)
        self.targ_mod_rb.setObjectName(_fromUtf8("targ_mod_rb"))
        self.targGrp.addButton(self.targ_mod_rb)
        self.horizontalLayout.addWidget(self.targ_mod_rb)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.targ_grp_bx)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.re_lb = QtGui.QLabel(self.mainWidget)
        self.re_lb.setObjectName(_fromUtf8("re_lb"))
        self.horizontalLayout_3.addWidget(self.re_lb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.ex_bt = QtGui.QToolButton(self.mainWidget)
        self.ex_bt.setObjectName(_fromUtf8("ex_bt"))
        self.horizontalLayout_3.addWidget(self.ex_bt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.mainWidget)
        exchProxyWin.setCentralWidget(self.ctWidget)
        self.menubar = QtGui.QMenuBar(exchProxyWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        exchProxyWin.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(exchProxyWin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        exchProxyWin.setStatusBar(self.statusbar)

        self.retranslateUi(exchProxyWin)
        QtCore.QObject.connect(self.src_ar_rb, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.targ_ar_rb.setDisabled)
        QtCore.QObject.connect(self.src_vr_rb, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.targ_vr_rb.setDisabled)
        QtCore.QObject.connect(self.src_vr_rb, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.targ_ar_rb.setChecked)
        QtCore.QObject.connect(self.src_ar_rb, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.targ_vr_rb.setChecked)
        QtCore.QMetaObject.connectSlotsByName(exchProxyWin)

    def retranslateUi(self, exchProxyWin):
        exchProxyWin.setWindowTitle(_translate("exchProxyWin", "代理替换--v1.01", None))
        self.sel_grp_bx.setTitle(_translate("exchProxyWin", "选择代理/全部代理", None))
        self.sel_rb.setText(_translate("exchProxyWin", "selected objects", None))
        self.all_rb.setText(_translate("exchProxyWin", "All Proxy", None))
        self.src_grp_bx.setTitle(_translate("exchProxyWin", "原代理", None))
        self.src_ar_rb.setText(_translate("exchProxyWin", "Arnold Proxy", None))
        self.src_vr_rb.setText(_translate("exchProxyWin", "VRay Proxy", None))
        self.targ_grp_bx.setTitle(_translate("exchProxyWin", "转换为", None))
        self.targ_ar_rb.setText(_translate("exchProxyWin", "Arnold Proxy", None))
        self.targ_vr_rb.setText(_translate("exchProxyWin", "VRay Proxy", None))
        self.targ_mod_rb.setText(_translate("exchProxyWin", "Model", None))
        self.re_lb.setText(_translate("exchProxyWin", "   共替换了：", None))
        self.ex_bt.setText(_translate("exchProxyWin", "PEPLACE", None))

