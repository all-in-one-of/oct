# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'abcSingleWin.ui'
#
# Created: Wed Mar 27 22:03:26 2019
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

class Ui_abcS_win(object):
    def setupUi(self, abcS_win):
        abcS_win.setObjectName(_fromUtf8("abcS_win"))
        abcS_win.resize(418, 305)
        abcS_win.setMinimumSize(QtCore.QSize(415, 300))
        abcS_win.setMaximumSize(QtCore.QSize(418, 350))
        self.centralwidget = QtGui.QWidget(abcS_win)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        abcS_win.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(abcS_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        abcS_win.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(abcS_win)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        abcS_win.setStatusBar(self.statusbar)

        self.retranslateUi(abcS_win)
        QtCore.QMetaObject.connectSlotsByName(abcS_win)

    def retranslateUi(self, abcS_win):
        abcS_win.setWindowTitle(_translate("abcS_win", "ABC Single Character", None))

