# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_diag.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 279)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(310, 5, 81, 51))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 5, 301, 271))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.deviceLabel = QtWidgets.QLabel(self.frame)
        self.deviceLabel.setGeometry(QtCore.QRect(0, 0, 91, 25))
        self.deviceLabel.setObjectName("deviceLabel")
        self.deviceEdit = QtWidgets.QLineEdit(self.frame)
        self.deviceEdit.setGeometry(QtCore.QRect(110, 0, 181, 25))
        self.deviceEdit.setObjectName("deviceEdit")
        self.ipLabel = QtWidgets.QLabel(self.frame)
        self.ipLabel.setGeometry(QtCore.QRect(0, 70, 91, 25))
        self.ipLabel.setObjectName("ipLabel")
        self.userEdit = QtWidgets.QLineEdit(self.frame)
        self.userEdit.setGeometry(QtCore.QRect(110, 105, 181, 25))
        self.userEdit.setObjectName("userEdit")
        self.userLabel = QtWidgets.QLabel(self.frame)
        self.userLabel.setGeometry(QtCore.QRect(0, 105, 91, 25))
        self.userLabel.setObjectName("userLabel")
        self.psdEdit = QtWidgets.QLineEdit(self.frame)
        self.psdEdit.setGeometry(QtCore.QRect(110, 140, 181, 25))
        self.psdEdit.setObjectName("psdEdit")
        self.pwdLabel = QtWidgets.QLabel(self.frame)
        self.pwdLabel.setGeometry(QtCore.QRect(0, 140, 91, 25))
        self.pwdLabel.setObjectName("pwdLabel")
        self.startTimeLabel = QtWidgets.QLabel(self.frame)
        self.startTimeLabel.setGeometry(QtCore.QRect(0, 175, 91, 25))
        self.startTimeLabel.setObjectName("startTimeLabel")
        self.startTimeEdit = QtWidgets.QTimeEdit(self.frame)
        self.startTimeEdit.setGeometry(QtCore.QRect(110, 175, 181, 25))
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.enddTimeLabel = QtWidgets.QLabel(self.frame)
        self.enddTimeLabel.setGeometry(QtCore.QRect(0, 210, 91, 25))
        self.enddTimeLabel.setObjectName("enddTimeLabel")
        self.endTimeEdit_2 = QtWidgets.QTimeEdit(self.frame)
        self.endTimeEdit_2.setGeometry(QtCore.QRect(110, 210, 181, 25))
        self.endTimeEdit_2.setObjectName("endTimeEdit_2")
        self.connectLabel = QtWidgets.QLabel(self.frame)
        self.connectLabel.setGeometry(QtCore.QRect(0, 35, 91, 25))
        self.connectLabel.setObjectName("connectLabel")
        self.commandLabel = QtWidgets.QLabel(self.frame)
        self.commandLabel.setGeometry(QtCore.QRect(0, 240, 91, 25))
        self.commandLabel.setObjectName("commandLabel")
        self.ipEdit = QtWidgets.QLineEdit(self.frame)
        self.ipEdit.setGeometry(QtCore.QRect(110, 70, 181, 25))
        self.ipEdit.setObjectName("ipEdit")
        self.connectcomboBox = QtWidgets.QComboBox(self.frame)
        self.connectcomboBox.setGeometry(QtCore.QRect(110, 35, 181, 25))
        self.connectcomboBox.setObjectName("connectcomboBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.deviceLabel.setText(_translate("Dialog", "     设备"))
        self.ipLabel.setText(_translate("Dialog", "    IP地址"))
        self.userLabel.setText(_translate("Dialog", "    用户名"))
        self.pwdLabel.setText(_translate("Dialog", "    密码"))
        self.startTimeLabel.setText(_translate("Dialog", "  开始时间"))
        self.enddTimeLabel.setText(_translate("Dialog", "  结束时间"))
        self.connectLabel.setText(_translate("Dialog", "   连接方式"))
        self.commandLabel.setText(_translate("Dialog", "  输入命令"))
