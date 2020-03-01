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
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(511, 321)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(20, 21))
        self.MainTab = QWidget()
        self.MainTab.setObjectName(u"MainTab")
        self.verticalLayout_MainTab = QVBoxLayout(self.MainTab)
        self.verticalLayout_MainTab.setObjectName(u"verticalLayout_MainTab")
        self.groupBoxHashCalculation = QGroupBox(self.MainTab)
        self.groupBoxHashCalculation.setObjectName(u"groupBoxHashCalculation")
        self.groupBoxHashCalculation.setFlat(False)
        self.groupBoxHashCalculation.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBoxHashCalculation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.labelFileExplore = QLabel(self.groupBoxHashCalculation)
        self.labelFileExplore.setObjectName(u"labelFileExplore")
        self.labelFileExplore.setFrameShape(QFrame.NoFrame)
        self.labelFileExplore.setPixmap(QPixmap(u":/folder/opened-folder.png"))
        self.labelFileExplore.setScaledContents(True)

        self.horizontalLayout.addWidget(self.labelFileExplore)

        self.lineEditFileExplore = QLineEdit(self.groupBoxHashCalculation)
        self.lineEditFileExplore.setObjectName(u"lineEditFileExplore")
        self.lineEditFileExplore.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditFileExplore)

        self.buttonSelectFile = QPushButton(self.groupBoxHashCalculation)
        self.buttonSelectFile.setObjectName(u"buttonSelectFile")
        icon1 = QIcon()
        icon1.addFile(u":/select/import-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSelectFile.setIcon(icon1)
        self.buttonSelectFile.setIconSize(QSize(20, 21))

        self.horizontalLayout.addWidget(self.buttonSelectFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonClearHashBox = QPushButton(self.groupBoxHashCalculation)
        self.buttonClearHashBox.setObjectName(u"buttonClearHashBox")
        icon2 = QIcon()
        icon2.addFile(u":/clear/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClearHashBox.setIcon(icon2)
        self.buttonClearHashBox.setIconSize(QSize(20, 21))

        self.horizontalLayout_3.addWidget(self.buttonClearHashBox)

        self.lineEditHashBox = QLineEdit(self.groupBoxHashCalculation)
        self.lineEditHashBox.setObjectName(u"lineEditHashBox")
        self.lineEditHashBox.setMaxLength(128)
        self.lineEditHashBox.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.lineEditHashBox)

        self.buttonCopyToClipboard = QPushButton(self.groupBoxHashCalculation)
        self.buttonCopyToClipboard.setObjectName(u"buttonCopyToClipboard")
        icon3 = QIcon()
        icon3.addFile(u":/copy/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCopyToClipboard.setIcon(icon3)
        self.buttonCopyToClipboard.setIconSize(QSize(20, 21))

        self.horizontalLayout_3.addWidget(self.buttonCopyToClipboard)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.comboBoxHashChoices = QComboBox(self.groupBoxHashCalculation)
        icon4 = QIcon()
        icon4.addFile(u":/rhombus/rhombus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBoxHashChoices.addItem(icon4, "")
        self.comboBoxHashChoices.addItem(icon4, "")
        self.comboBoxHashChoices.addItem(icon4, "")
        self.comboBoxHashChoices.addItem(icon4, "")
        self.comboBoxHashChoices.addItem(icon4, "")
        self.comboBoxHashChoices.addItem(icon4, "")
        self.comboBoxHashChoices.setObjectName(u"comboBoxHashChoices")
        self.comboBoxHashChoices.setEnabled(True)
        self.comboBoxHashChoices.setEditable(False)
        self.comboBoxHashChoices.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBoxHashChoices.setIconSize(QSize(16, 16))
        self.comboBoxHashChoices.setFrame(True)

        self.horizontalLayout_2.addWidget(self.comboBoxHashChoices)

        self.progressBarHashCaclulation = QProgressBar(self.groupBoxHashCalculation)
        self.progressBarHashCaclulation.setObjectName(u"progressBarHashCaclulation")
        self.progressBarHashCaclulation.setMaximum(100)
        self.progressBarHashCaclulation.setValue(0)
        self.progressBarHashCaclulation.setTextVisible(True)
        self.progressBarHashCaclulation.setInvertedAppearance(False)
        self.progressBarHashCaclulation.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_2.addWidget(self.progressBarHashCaclulation)

        self.buttonHashCalculate = QPushButton(self.groupBoxHashCalculation)
        self.buttonHashCalculate.setObjectName(u"buttonHashCalculate")
        icon5 = QIcon()
        icon5.addFile(u":/calculate/drawing-compass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonHashCalculate.setIcon(icon5)
        self.buttonHashCalculate.setIconSize(QSize(20, 21))
        self.buttonHashCalculate.setCheckable(False)
        self.buttonHashCalculate.setAutoDefault(False)
        self.buttonHashCalculate.setFlat(False)

        self.horizontalLayout_2.addWidget(self.buttonHashCalculate)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_MainTab.addWidget(self.groupBoxHashCalculation)

        self.groupBoxHashMatcher = QGroupBox(self.MainTab)
        self.groupBoxHashMatcher.setObjectName(u"groupBoxHashMatcher")
        self.groupBoxHashMatcher.setCheckable(True)
        self.groupBoxHashMatcher.setChecked(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxHashMatcher)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonClearCheckHashBox = QPushButton(self.groupBoxHashMatcher)
        self.buttonClearCheckHashBox.setObjectName(u"buttonClearCheckHashBox")
        self.buttonClearCheckHashBox.setIcon(icon2)
        self.buttonClearCheckHashBox.setIconSize(QSize(20, 21))

        self.horizontalLayout_4.addWidget(self.buttonClearCheckHashBox)

        self.lineEditCheckHashBox = QLineEdit(self.groupBoxHashMatcher)
        self.lineEditCheckHashBox.setObjectName(u"lineEditCheckHashBox")
        self.lineEditCheckHashBox.setMaxLength(128)
        self.lineEditCheckHashBox.setReadOnly(False)
        self.lineEditCheckHashBox.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEditCheckHashBox)

        self.buttonCheckHash = QPushButton(self.groupBoxHashMatcher)
        self.buttonCheckHash.setObjectName(u"buttonCheckHash")
        icon6 = QIcon()
        icon6.addFile(u":/check/magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonCheckHash.setIcon(icon6)
        self.buttonCheckHash.setIconSize(QSize(20, 21))

        self.horizontalLayout_4.addWidget(self.buttonCheckHash)


        self.verticalLayout_MainTab.addWidget(self.groupBoxHashMatcher)

        icon7 = QIcon()
        icon7.addFile(u":/home/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.MainTab, icon7, "")
        self.AboutTab = QWidget()
        self.AboutTab.setObjectName(u"AboutTab")
        self.verticalLayout_7 = QVBoxLayout(self.AboutTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(self.AboutTab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(True)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.developerName = QLabel(self.layoutWidget)
        self.developerName.setObjectName(u"developerName")
        self.developerName.setScaledContents(False)
        self.developerName.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.developerName)

        self.developerEmail = QLabel(self.layoutWidget)
        self.developerEmail.setObjectName(u"developerEmail")
        self.developerEmail.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.developerEmail)

        self.logoCreditName = QLabel(self.layoutWidget)
        self.logoCreditName.setObjectName(u"logoCreditName")
        self.logoCreditName.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.logoCreditName)

        self.logoCreditEmail = QLabel(self.layoutWidget)
        self.logoCreditEmail.setObjectName(u"logoCreditEmail")

        self.verticalLayout_2.addWidget(self.logoCreditEmail)

        self.icons8Credit = QLabel(self.layoutWidget)
        self.icons8Credit.setObjectName(u"icons8Credit")
        self.icons8Credit.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.icons8Credit)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.hashCheckerHeader = QLabel(self.layoutWidget1)
        self.hashCheckerHeader.setObjectName(u"hashCheckerHeader")
        self.hashCheckerHeader.setPixmap(QPixmap(u":/header/header.png"))

        self.verticalLayout_4.addWidget(self.hashCheckerHeader)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_2 = QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sourceCodeLink = QLabel(self.groupBox_2)
        self.sourceCodeLink.setObjectName(u"sourceCodeLink")
        self.sourceCodeLink.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.sourceCodeLink)


        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.layoutWidget1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.applicationVersion = QLabel(self.groupBox_4)
        self.applicationVersion.setObjectName(u"applicationVersion")

        self.verticalLayout_6.addWidget(self.applicationVersion)


        self.horizontalLayout_5.addWidget(self.groupBox_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_7.addWidget(self.splitter)

        self.licenseTextBrowser = QTextBrowser(self.AboutTab)
        self.licenseTextBrowser.setObjectName(u"licenseTextBrowser")
        self.licenseTextBrowser.setOpenExternalLinks(True)

        self.verticalLayout_7.addWidget(self.licenseTextBrowser)

        icon8 = QIcon()
        icon8.addFile(u":/about/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.AboutTab, icon8, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(450, 0))
        self.statusbar.setMaximumSize(QSize(600, 326))
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 511, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.buttonClearCheckHashBox.clicked.connect(self.lineEditCheckHashBox.clear)

        self.tabWidget.setCurrentIndex(0)
        self.buttonHashCalculate.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Free Hash Checker", None))
        self.groupBoxHashCalculation.setTitle(QCoreApplication.translate("MainWindow", u"Hash Calculation", None))
        self.labelFileExplore.setText("")
        self.lineEditFileExplore.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select a file to begin", None))
        self.buttonSelectFile.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.buttonClearHashBox.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lineEditHashBox.setText("")
        self.lineEditHashBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hash will be displayed here", None))
        self.buttonCopyToClipboard.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.comboBoxHashChoices.setItemText(0, QCoreApplication.translate("MainWindow", u"MD5", None))
        self.comboBoxHashChoices.setItemText(1, QCoreApplication.translate("MainWindow", u"SHA1", None))
        self.comboBoxHashChoices.setItemText(2, QCoreApplication.translate("MainWindow", u"SHA224", None))
        self.comboBoxHashChoices.setItemText(3, QCoreApplication.translate("MainWindow", u"SHA256", None))
        self.comboBoxHashChoices.setItemText(4, QCoreApplication.translate("MainWindow", u"SHA384", None))
        self.comboBoxHashChoices.setItemText(5, QCoreApplication.translate("MainWindow", u"SHA512", None))

        self.comboBoxHashChoices.setCurrentText(QCoreApplication.translate("MainWindow", u"MD5", None))
        self.progressBarHashCaclulation.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.buttonHashCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBoxHashMatcher.setTitle(QCoreApplication.translate("MainWindow", u"Hash Matcher", None))
        self.buttonClearCheckHashBox.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lineEditCheckHashBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste hash here", None))
        self.buttonCheckHash.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.developerName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                                style=\" font-size:10pt; font-weight:600;\">Developer:</span>\n"
"                                                                Rizwan Hasan</span></p></body></html>\n"
"                                                            ", None))
        self.developerEmail.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                                style=\" font-size:10pt; font-weight:600;\">Email:\n"
"                                                                </span>rizwan.hasan486@gmail.com </p></body></html>\n"
"                                                            ", None))
        self.logoCreditName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                                style=\" font-size:10pt; font-weight:600;\">Logo\n"
"                                                                credit: </span>Sakib Khan Inan </p></body></html>\n"
"                                                            ", None))
        self.logoCreditEmail.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                                style=\" font-size:10pt; font-weight:600;\">Email:\n"
"                                                                </span>sakib.khaninan@hotmail.com </p></body></html>\n"
"                                                            ", None))
        self.icons8Credit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                                style=\" font-size:10pt; font-weight:600;\">Icons\n"
"                                                                credit: </span>Icons8</p></body></html>\n"
"                                                            ", None))
        self.hashCheckerHeader.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.sourceCodeLink.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p\n"
"                                                                                    align=\"center\"><a\n"
"                                                                                    href=\"https://github.com/Rizwan-Hasan/Free-Hash-Checker\"><img\n"
"                                                                                    src=\":/github/github.png\"/></a></p></body></html>\n"
"                                                                                ", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Version", None))
        self.applicationVersion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p\n"
"                                                                                    align=\"center\"><span\n"
"                                                                                    style=\" font-size:22pt;\n"
"                                                                                    font-weight:600;\">0.0</span></p></body></html>\n"
"                                                                                ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AboutTab), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

