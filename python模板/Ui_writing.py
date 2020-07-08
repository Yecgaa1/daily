# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
import sys, os, configparser

# 基本五大包导入


# PyQt5.QtWidgets import*
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# 以下为导入功能包
import socket
import json
import hashlib
import time
import ctypes



class Ui_New(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)





if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    Newapp = QApplication(sys.argv)
    ex = Ui_New()
    ex.show()
    sys.exit(Newapp.exec_())