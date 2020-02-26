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
        MainWindow.resize(450, 233)
        MainWindow.setMinimumSize(QSize(450, 233))
        MainWindow.setMaximumSize(QSize(450, 233))
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
        self.tabWidget.setIconSize(QSize(16, 16))
        self.MainTab = QWidget()
        self.MainTab.setObjectName(u"MainTab")
        self.verticalLayout = QVBoxLayout(self.MainTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.labelFileExplore = QLabel(self.MainTab)
        self.labelFileExplore.setObjectName(u"labelFileExplore")
        self.labelFileExplore.setFrameShape(QFrame.NoFrame)
        self.labelFileExplore.setPixmap(QPixmap(u":/folder/opened-folder.png"))
        self.labelFileExplore.setScaledContents(True)

        self.horizontalLayout.addWidget(self.labelFileExplore)

        self.lineEditFileExplore = QLineEdit(self.MainTab)
        self.lineEditFileExplore.setObjectName(u"lineEditFileExplore")
        self.lineEditFileExplore.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditFileExplore)

        self.buttonSelectFile = QPushButton(self.MainTab)
        self.buttonSelectFile.setObjectName(u"buttonSelectFile")
        icon1 = QIcon()
        icon1.addFile(u":/select/import-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSelectFile.setIcon(icon1)
        self.buttonSelectFile.setIconSize(QSize(20, 21))

        self.horizontalLayout.addWidget(self.buttonSelectFile)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonClearHashBox = QPushButton(self.MainTab)
        self.buttonClearHashBox.setObjectName(u"buttonClearHashBox")
        icon2 = QIcon()
        icon2.addFile(u":/clear/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClearHashBox.setIcon(icon2)
        self.buttonClearHashBox.setIconSize(QSize(20, 21))

        self.horizontalLayout_3.addWidget(self.buttonClearHashBox)

        self.lineEditHashBox = QLineEdit(self.MainTab)
        self.lineEditHashBox.setObjectName(u"lineEditHashBox")
        self.lineEditHashBox.setMaxLength(128)
        self.lineEditHashBox.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.lineEditHashBox)

        self.buttonCopyToClipboard = QPushButton(self.MainTab)
        self.buttonCopyToClipboard.setObjectName(u"buttonCopyToClipboard")
        icon3 = QIcon()
        icon3.addFile(u":/copy/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCopyToClipboard.setIcon(icon3)
        self.buttonCopyToClipboard.setIconSize(QSize(20, 21))

        self.horizontalLayout_3.addWidget(self.buttonCopyToClipboard)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttnClearCheckHashBox = QPushButton(self.MainTab)
        self.buttnClearCheckHashBox.setObjectName(u"buttnClearCheckHashBox")
        self.buttnClearCheckHashBox.setIcon(icon2)
        self.buttnClearCheckHashBox.setIconSize(QSize(20, 21))

        self.horizontalLayout_4.addWidget(self.buttnClearCheckHashBox)

        self.lineEditCheckHashBox = QLineEdit(self.MainTab)
        self.lineEditCheckHashBox.setObjectName(u"lineEditCheckHashBox")
        self.lineEditCheckHashBox.setMaxLength(128)
        self.lineEditCheckHashBox.setReadOnly(False)
        self.lineEditCheckHashBox.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEditCheckHashBox)

        self.buttonCheckHash = QPushButton(self.MainTab)
        self.buttonCheckHash.setObjectName(u"buttonCheckHash")
        icon4 = QIcon()
        icon4.addFile(u":/check/magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCheckHash.setIcon(icon4)
        self.buttonCheckHash.setIconSize(QSize(20, 21))

        self.horizontalLayout_4.addWidget(self.buttonCheckHash)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.comboBoxHashChoices = QComboBox(self.MainTab)
        icon5 = QIcon()
        icon5.addFile(u":/rhombus/rhombus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBoxHashChoices.addItem(icon5, "")
        self.comboBoxHashChoices.addItem(icon5, "")
        self.comboBoxHashChoices.addItem(icon5, "")
        self.comboBoxHashChoices.addItem(icon5, "")
        self.comboBoxHashChoices.addItem(icon5, "")
        self.comboBoxHashChoices.addItem(icon5, "")
        self.comboBoxHashChoices.setObjectName(u"comboBoxHashChoices")
        self.comboBoxHashChoices.setEnabled(True)
        self.comboBoxHashChoices.setEditable(False)
        self.comboBoxHashChoices.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxHashChoices.setIconSize(QSize(16, 16))
        self.comboBoxHashChoices.setFrame(True)

        self.horizontalLayout_2.addWidget(self.comboBoxHashChoices)

        self.progressBarHashCaclulation = QProgressBar(self.MainTab)
        self.progressBarHashCaclulation.setObjectName(u"progressBarHashCaclulation")
        self.progressBarHashCaclulation.setMaximum(100)
        self.progressBarHashCaclulation.setValue(0)
        self.progressBarHashCaclulation.setTextVisible(True)
        self.progressBarHashCaclulation.setInvertedAppearance(False)
        self.progressBarHashCaclulation.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_2.addWidget(self.progressBarHashCaclulation)

        self.buttonHashCalculate = QPushButton(self.MainTab)
        self.buttonHashCalculate.setObjectName(u"buttonHashCalculate")
        icon6 = QIcon()
        icon6.addFile(u":/calculate/drawing-compass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonHashCalculate.setIcon(icon6)
        self.buttonHashCalculate.setIconSize(QSize(20, 21))
        self.buttonHashCalculate.setCheckable(False)
        self.buttonHashCalculate.setAutoDefault(False)
        self.buttonHashCalculate.setFlat(False)

        self.horizontalLayout_2.addWidget(self.buttonHashCalculate)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        icon7 = QIcon()
        icon7.addFile(u":/home/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.MainTab, icon7, "")
        self.SettingsTab = QWidget()
        self.SettingsTab.setObjectName(u"SettingsTab")
        icon8 = QIcon()
        icon8.addFile(u":/settings/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.SettingsTab, icon8, "")
        self.AboutTab = QWidget()
        self.AboutTab.setObjectName(u"AboutTab")
        icon9 = QIcon()
        icon9.addFile(u":/about/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.AboutTab, icon9, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.buttonHashCalculate.setDefault(False)


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

