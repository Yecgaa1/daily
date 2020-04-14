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
import ctypes, requests

headers = {'API-Key': 'VVFXA4VPMGQCDDDC3WVHNIEELQ3HHYHSIYCA'}
state = 0
id = ""
i = 0

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "user.ini")
conf = configparser.ConfigParser()
conf.read(cfgpath, encoding="utf-8")


class Ui_New(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def wrong(self, code):
        if code == 403:
            self.imf.setText("请检查api")
        elif code == 404:
            self.imf.setText("请检查网络")
        else:
            self.imf.setText("请检查程序")

    def statecheck(self):
        global i
        if i==0:
            i=10
        while i > 0:
            req = requests.get("https://api.vultr.com/v1/server/list", headers=headers, timeout=3)
            if req.status_code != 200:
                self.wrong(req.status_code)
                return
            result = json.loads(req.text)
            try:
                self.imf.setText('电源状态:' + result[id]["power_status"] + '\n系统状态' + result[id]['server_state'])
            except:
                self.imf.setText('开机没成功')
            time.sleep(10)
            i-=1
        return

    def run(self):
        global id, state, i
        if state == 0:
            self.imf.setText("5s后尝试开机，如误触请关闭")
            time.sleep(5)
            # snapshotid=conf.get("Server", 'snapshot')
            # OSID = conf.get("Server", 'OSID')
            # VPSPLANID = conf.get("Server", 'VPSPLANID')
            # DCID = conf.get("Server", 'DCID')
            SNAPSHOTID = "cd75ce7d47b62"
            OSID = "164"
            DCID = "25"
            VPSPLANID = "202"
            data = {'DCID': DCID, 'VPSPLANID': VPSPLANID, 'SNAPSHOTID': SNAPSHOTID, 'OSID': OSID}
            print(data)
            req = requests.post("https://api.vultr.com/v1/server/create", headers=headers, data=data, timeout=3)
            if req.status_code != 200:
                self.wrong(req.status_code)
                return
            result = json.loads(req.text)
            id = result['SUBID']
            self.imf.setText("启动成功，id为" + id + "\n 10s后检查状态")
            state = 1
            i = 150
            time.sleep(10)
            self.statecheck()
            return
        elif state == 1:
            if id == "":
                self.imf.setText("请手动去网站关机")
                return
            self.imf.setText("10s后尝试开机，如误触请关闭")
            time.sleep(10)
            data = {'SUBID': id}
            req = requests.post("https://api.vultr.com/v1/server/destroy", headers=headers, data=data, timeout=3)
            if req.status_code != 200:
                self.wrong(req.status_code)
                return
            else:
                self.imf.setText("成功关机")
                return

    def accstate1(self):
        req = requests.get("https://api.vultr.com/v1/account/info", headers=headers, timeout=3)
        if req.status_code != 200:
            self.wrong(req.status_code)
            return
        result = json.loads(req.text)
        self.imf.setText(str(result))
        return

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(419, 291)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accstate = QtWidgets.QPushButton(Form)
        self.accstate.setObjectName("accstate")
        self.horizontalLayout.addWidget(self.accstate)
        self.power = QtWidgets.QPushButton(Form)
        self.power.setObjectName("power")
        self.horizontalLayout.addWidget(self.power)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.save = QtWidgets.QPushButton(Form)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.imf = QtWidgets.QLabel(Form)
        self.imf.setObjectName("imf")
        self.gridLayout_2.addWidget(self.imf, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.imf.setWordWrap(True)
        self.accstate.clicked.connect(self.accstate1)
        self.pushButton.clicked.connect(self.statecheck)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.accstate.setText(_translate("Form", "账户状态"))
        self.power.setText(_translate("Form", "开机"))
        self.pushButton.setText(_translate("Form", "服务器状态"))
        self.save.setText(_translate("Form", "保存上传"))


if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    Newapp = QApplication(sys.argv)
    ex = Ui_New()
    ex.show()
    sys.exit(Newapp.exec_())
