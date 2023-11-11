# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 779)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_info = QtWidgets.QFrame(self.centralwidget)
        self.frame_info.setMinimumSize(QtCore.QSize(80, 500))
        self.frame_info.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_info.setStyleSheet("background-color:rgb(240,240,240)")
        self.frame_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_info.setObjectName("frame_info")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_info)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 77, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_chat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_chat.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.btn_chat.setFont(font)
        self.btn_chat.setStyleSheet("QPushButton {background-color: rgb(240,240,240);}\n"
                                    "                                                QPushButton:hover{background-color: rgb(209,209,209);}\n"
                                    "                                            ")
        self.btn_chat.setFlat(True)
        self.btn_chat.setObjectName("btn_chat")
        self.verticalLayout_2.addWidget(self.btn_chat)
        self.btn_contact = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_contact.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.btn_contact.setFont(font)
        self.btn_contact.setStyleSheet("QPushButton {background-color: rgb(240,240,240);}\n"
                                       "                                                QPushButton:hover{background-color: rgb(209,209,209);}\n"
                                       "                                            ")
        self.btn_contact.setFlat(True)
        self.btn_contact.setObjectName("btn_contact")
        self.verticalLayout_2.addWidget(self.btn_contact)
        self.btn_myinfo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_myinfo.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.btn_myinfo.setFont(font)
        self.btn_myinfo.setStyleSheet("QPushButton {background-color: rgb(240,240,240);}\n"
                                      "                                                QPushButton:hover{background-color: rgb(209,209,209);}\n"
                                      "                                            ")
        self.btn_myinfo.setFlat(True)
        self.btn_myinfo.setObjectName("btn_myinfo")
        self.verticalLayout_2.addWidget(self.btn_myinfo)
        self.btn_about = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_about.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.btn_about.setFont(font)
        self.btn_about.setStyleSheet("QPushButton {background-color: rgb(240,240,240);}\n"
                                     "                                                QPushButton:hover{background-color: rgb(209,209,209);}\n"
                                     "                                            ")
        self.btn_about.setFlat(True)
        self.btn_about.setObjectName("btn_about")
        self.verticalLayout_2.addWidget(self.btn_about)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.myavatar = QtWidgets.QLabel(self.frame_info)
        self.myavatar.setGeometry(QtCore.QRect(10, 40, 60, 60))
        self.myavatar.setObjectName("myavatar")
        self.horizontalLayout.addWidget(self.frame_info)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_chat = QtWidgets.QWidget()
        self.page_chat.setObjectName("page_chat")
        self.stackedWidget.addWidget(self.page_chat)
        self.page_contact = QtWidgets.QWidget()
        self.page_contact.setObjectName("page_contact")
        self.stackedWidget.addWidget(self.page_contact)
        self.page_myinfo = QtWidgets.QWidget()
        self.page_myinfo.setObjectName("page_myinfo")
        self.stackedWidget.addWidget(self.page_myinfo)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.menu_F.addSeparator()
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_3)
        self.menu_F.addAction(self.action_4)
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_chat.setText(_translate("MainWindow", "聊天"))
        self.btn_contact.setText(_translate("MainWindow", "好友"))
        self.btn_myinfo.setText(_translate("MainWindow", "我的"))
        self.btn_about.setText(_translate("MainWindow", "关于"))
        self.myavatar.setText(_translate("MainWindow", "avatar"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu.setTitle(_translate("MainWindow", "编辑"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.action_3.setText(_translate("MainWindow", "保存"))
        self.action_4.setText(_translate("MainWindow", "退出"))
        self.action.setText(_translate("MainWindow", "关于"))
