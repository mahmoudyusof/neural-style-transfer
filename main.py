# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.content = QtWidgets.QLabel(self.centralwidget)
        self.content.setGeometry(QtCore.QRect(10, 20, 59, 15))
        self.content.setObjectName("content")
        self.style = QtWidgets.QLabel(self.centralwidget)
        self.style.setGeometry(QtCore.QRect(
            MainWindow.width()*0.3, 20, 59, 15))
        self.style.setObjectName("style")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(
            MainWindow.width()*0.6, 20, 59, 15))
        self.output.setObjectName("output")
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.content.setText(_translate("MainWindow", "TextLabel"))
        self.style.setText(_translate("MainWindow", "TextLabel"))
        self.style.move(MainWindow.width()*0.3, 20)
        self.output.setText(_translate("MainWindow", "TextLabel"))
        self.output.move(MainWindow.width()*0.6, 20)
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionopen_style.setText(_translate("MainWindow", "open style"))

        self.actionopen.triggered.connect(self.openDialog)

    def openDialog(self):
        filename, types = QtWidgets.QFileDialog.getOpenFileName()
        pmap = QtGui.QPixmap(filename)
        pmap = pmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        self.content.setPixmap(pmap)
        self.content.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)

    win.show()
    sys.exit(app.exec_())
