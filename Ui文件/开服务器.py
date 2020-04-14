# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '开服务器.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.accstate.setText(_translate("Form", "账户状态"))
        self.power.setText(_translate("Form", "开机"))
        self.pushButton.setText(_translate("Form", "服务器状态"))
        self.save.setText(_translate("Form", "保存上传"))
        self.imf.setText(_translate("Form", "TextLabel"))
