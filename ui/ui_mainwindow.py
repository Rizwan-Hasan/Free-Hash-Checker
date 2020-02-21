# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 270)
        MainWindow.setMinimumSize(QSize(480, 270))
        MainWindow.setMaximumSize(QSize(480, 270))
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(20, 20))
        self.MainTab = QWidget()
        self.MainTab.setObjectName(u"MainTab")
        self.layoutWidget = QWidget(self.MainTab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 11, 431, 138))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 3)
        self.labelFileExplore = QLabel(self.layoutWidget)
        self.labelFileExplore.setObjectName(u"labelFileExplore")
        self.labelFileExplore.setFrameShape(QFrame.NoFrame)
        self.labelFileExplore.setPixmap(QPixmap(u":/folder/folder.png"))
        self.labelFileExplore.setScaledContents(True)

        self.horizontalLayout.addWidget(self.labelFileExplore)

        self.lineEditFileExplore = QLineEdit(self.layoutWidget)
        self.lineEditFileExplore.setObjectName(u"lineEditFileExplore")
        self.lineEditFileExplore.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditFileExplore)

        self.buttonSelectFile = QPushButton(self.layoutWidget)
        self.buttonSelectFile.setObjectName(u"buttonSelectFile")
        icon1 = QIcon()
        icon1.addFile(u":/select/cursor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSelectFile.setIcon(icon1)

        self.horizontalLayout.addWidget(self.buttonSelectFile)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonClearHashBox = QPushButton(self.layoutWidget)
        self.buttonClearHashBox.setObjectName(u"buttonClearHashBox")
        icon2 = QIcon()
        icon2.addFile(u":/clear/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClearHashBox.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.buttonClearHashBox)

        self.lineEditHashBox = QLineEdit(self.layoutWidget)
        self.lineEditHashBox.setObjectName(u"lineEditHashBox")
        self.lineEditHashBox.setMaxLength(128)
        self.lineEditHashBox.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.lineEditHashBox)

        self.buttonCopyToClipboard = QPushButton(self.layoutWidget)
        self.buttonCopyToClipboard.setObjectName(u"buttonCopyToClipboard")
        icon3 = QIcon()
        icon3.addFile(u":/copy/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCopyToClipboard.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.buttonCopyToClipboard)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttnClearCheckHashBox = QPushButton(self.layoutWidget)
        self.buttnClearCheckHashBox.setObjectName(u"buttnClearCheckHashBox")
        self.buttnClearCheckHashBox.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.buttnClearCheckHashBox)

        self.lineEditCheckHashBox = QLineEdit(self.layoutWidget)
        self.lineEditCheckHashBox.setObjectName(u"lineEditCheckHashBox")
        self.lineEditCheckHashBox.setMaxLength(128)
        self.lineEditCheckHashBox.setReadOnly(False)
        self.lineEditCheckHashBox.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEditCheckHashBox)

        self.buttonCheckHash = QPushButton(self.layoutWidget)
        self.buttonCheckHash.setObjectName(u"buttonCheckHash")
        icon4 = QIcon()
        icon4.addFile(u":/check/magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCheckHash.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.buttonCheckHash)


        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, -1, -1, -1)
        self.comboBoxHashChoices = QComboBox(self.layoutWidget)
        self.comboBoxHashChoices.addItem("")
        self.comboBoxHashChoices.addItem("")
        self.comboBoxHashChoices.addItem("")
        self.comboBoxHashChoices.addItem("")
        self.comboBoxHashChoices.addItem("")
        self.comboBoxHashChoices.addItem("")
        self.comboBoxHashChoices.setObjectName(u"comboBoxHashChoices")
        self.comboBoxHashChoices.setEnabled(True)
        self.comboBoxHashChoices.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxHashChoices.setFrame(True)

        self.horizontalLayout_2.addWidget(self.comboBoxHashChoices)

        self.progressBarHashCaclulation = QProgressBar(self.layoutWidget)
        self.progressBarHashCaclulation.setObjectName(u"progressBarHashCaclulation")
        self.progressBarHashCaclulation.setMaximum(100)
        self.progressBarHashCaclulation.setValue(0)
        self.progressBarHashCaclulation.setTextVisible(True)
        self.progressBarHashCaclulation.setInvertedAppearance(False)
        self.progressBarHashCaclulation.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_2.addWidget(self.progressBarHashCaclulation)

        self.buttonHashCalculate = QPushButton(self.layoutWidget)
        self.buttonHashCalculate.setObjectName(u"buttonHashCalculate")
        icon5 = QIcon()
        icon5.addFile(u":/calculate/calculator.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonHashCalculate.setIcon(icon5)
        self.buttonHashCalculate.setCheckable(False)
        self.buttonHashCalculate.setFlat(False)

        self.horizontalLayout_2.addWidget(self.buttonHashCalculate)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        icon6 = QIcon()
        icon6.addFile(u":/home/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.MainTab, icon6, "")
        self.SettingsTab = QWidget()
        self.SettingsTab.setObjectName(u"SettingsTab")
        icon7 = QIcon()
        icon7.addFile(u":/settings/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.SettingsTab, icon7, "")
        self.AboutTab = QWidget()
        self.AboutTab.setObjectName(u"AboutTab")
        icon8 = QIcon()
        icon8.addFile(u":/about/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.AboutTab, icon8, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonClearHashBox.clicked.connect(self.lineEditHashBox.clear)
        self.buttnClearCheckHashBox.clicked.connect(self.lineEditCheckHashBox.clear)
        self.buttonClearHashBox.clicked.connect(self.lineEditFileExplore.clear)
        self.buttonClearHashBox.clicked.connect(self.progressBarHashCaclulation.reset)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Free Hash Checker", None))
        self.labelFileExplore.setText("")
        self.lineEditFileExplore.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a file for calculating the hash", None))
        self.buttonSelectFile.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.buttonClearHashBox.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lineEditHashBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Calculated hash will be displayed here", None))
        self.buttonCopyToClipboard.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.buttnClearCheckHashBox.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lineEditCheckHashBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste your existing hash here for checking", None))
        self.buttonCheckHash.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.comboBoxHashChoices.setItemText(0, QCoreApplication.translate("MainWindow", u"MD5", None))
        self.comboBoxHashChoices.setItemText(1, QCoreApplication.translate("MainWindow", u"SHA1", None))
        self.comboBoxHashChoices.setItemText(2, QCoreApplication.translate("MainWindow", u"SHA224", None))
        self.comboBoxHashChoices.setItemText(3, QCoreApplication.translate("MainWindow", u"SHA256", None))
        self.comboBoxHashChoices.setItemText(4, QCoreApplication.translate("MainWindow", u"SHA384", None))
        self.comboBoxHashChoices.setItemText(5, QCoreApplication.translate("MainWindow", u"SHA512", None))

        self.comboBoxHashChoices.setCurrentText(QCoreApplication.translate("MainWindow", u"MD5", None))
        self.progressBarHashCaclulation.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.buttonHashCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SettingsTab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutTab), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

