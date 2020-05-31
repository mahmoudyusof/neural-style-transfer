# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
import sys
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
from PIL.ImageQt import ImageQt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.content = QtWidgets.QLabel(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(10, 20, 361, 221))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.content.setFont(font)
        self.content.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.content.setAutoFillBackground(False)
        self.content.setStyleSheet("background-color: #ddd; color: #888;")
        self.content.setAlignment(QtCore.Qt.AlignCenter)
        self.content.setObjectName("content")
        self.style = QtWidgets.QLabel(self.centralwidget)
        self.style.setGeometry(QtCore.QRect(420, 20, 361, 221))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.style.setFont(font)
        self.style.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.style.setAutoFillBackground(False)
        self.style.setStyleSheet("background-color: #ddd; color: #888;")
        self.style.setAlignment(QtCore.Qt.AlignCenter)
        self.style.setObjectName("style")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(420, 280, 361, 221))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.result.setFont(font)
        self.result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.result.setAutoFillBackground(False)
        self.result.setStyleSheet("background-color: #ddd; color: #888;")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(10, 380, 281, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.run.setFont(font)
        self.run.setObjectName("run")
        self.epoch_input = QtWidgets.QLineEdit(self.centralwidget)
        self.epoch_input.setGeometry(QtCore.QRect(200, 310, 91, 23))
        self.epoch_input.setObjectName("epoch_input")
        self.epoch_label = QtWidgets.QLabel(self.centralwidget)
        self.epoch_label.setGeometry(QtCore.QRect(10, 310, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.epoch_label.setFont(font)
        self.epoch_label.setObjectName("epoch_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionopen_style = QtWidgets.QAction(MainWindow)
        self.actionopen_style.setObjectName("actionopen_style")
        self.menufile.addAction(self.actionopen)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionopen_style)
        self.menubar.addAction(self.menufile.menuAction())

        self.content.mousePressEvent = self.open_content
        self.style.mousePressEvent = self.open_style

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_content(self, evt):
        f = QtWidgets.QFileDialog().getOpenFileName(
            filter="Image files (*.jpg *.png *.jpeg)")[0]

        pix = QtGui.QPixmap(f)
        self.content.setPixmap(pix.scaled(
            self.content.size(), Qt.KeepAspectRatio, Qt.FastTransformation))

        image = pix.toImage().convertToFormat(QtGui.QImage.Format_RGBA8888)

        width = image.width()
        height = image.height()
        n_channels = int(image.depth() / 8)

        ptr = image.bits()
        ptr.setsize(height * width * n_channels)
        arr = np.frombuffer(ptr, np.uint8).reshape((height, width, n_channels))
        print(arr[:, :, :3].shape)

    def open_style(self, evt):
        f = QtWidgets.QFileDialog().getOpenFileName(
            filter="Image files (*.jpg *.png *.jpeg)")[0]

        pix = QtGui.QPixmap(f)
        self.style.setPixmap(pix.scaled(
            self.style.size(), Qt.KeepAspectRatio, Qt.FastTransformation))

        image = pix.toImage().convertToFormat(QtGui.QImage.Format_RGBA8888)

        width = image.width()
        height = image.height()
        n_channels = int(image.depth() / 8)

        ptr = image.bits()
        ptr.setsize(height * width * n_channels)
        arr = np.frombuffer(ptr, np.uint8).reshape((height, width, n_channels))
        print(arr[:, :, :3].shape)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NST"))
        self.content.setText(_translate("MainWindow", "Choose content image"))
        self.style.setText(_translate("MainWindow", "Choose Style image"))
        self.result.setText(_translate("MainWindow", "Result"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.epoch_label.setText(_translate(
            "MainWindow", "number of iterations"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionopen_style.setText(_translate("MainWindow", "open style"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)

    win.show()

    sys.exit(app.exec_())
