# Form implementation generated from reading ui file 'characterStyle.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 150)
        Dialog.setMinimumSize(QtCore.QSize(250, 150))
        Dialog.setMaximumSize(QtCore.QSize(250, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("img.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        Dialog.setWindowIcon(icon)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(40, 60, 71, 26))
        self.label_16.setMinimumSize(QtCore.QSize(70, 26))
        self.label_16.setMaximumSize(QtCore.QSize(666666, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_16.setFont(font)
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 60, 91, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(40, 25, 70, 26))
        self.label_13.setMinimumSize(QtCore.QSize(70, 26))
        self.label_13.setMaximumSize(QtCore.QSize(666666, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet("")
        self.label_13.setObjectName("label_13")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 25, 91, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 100, 60, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 100, 60, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "字距设置"))
        self.label_16.setText(_translate("Dialog", "行距:"))
        self.lineEdit_2.setText(_translate("Dialog", "1.3"))
        self.label_13.setText(_translate("Dialog", "字距:"))
        self.lineEdit.setText(_translate("Dialog", "1.3"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
