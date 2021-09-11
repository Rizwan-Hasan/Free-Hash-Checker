# -*- coding: utf-8 -*-

import logging
import os
import time

from PySide2.QtCore import Slot
from PySide2.QtGui import QCloseEvent, QGuiApplication, QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from hashcalc import HashingMethods
from infoManager import informationManger
from ui.ui_mainwindow import Ui_MainWindow
from updateManager import updateManager

logging.basicConfig(level=logging.DEBUG, format="%(name)s:%(levelname)s:%(message)s")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__hashCalculator: HashingMethods

        # Setting fixed window size to disable full screen ↓
        self.setFixedWidth(self.size().width())
        self.setFixedHeight(self.minimumSizeHint().height())

        # ↓
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__makeWindowCenter()

        # Window customizing ↓
        self.setWindowTitle("Free Hash Checker")

        # Clipboard setup ↓
        self.__clipboard = QApplication.clipboard()
        self.__clipboard.clear(mode=self.__clipboard.Clipboard)

        # Resetting progress bar ↓
        self.ui.progressBarHashCaclulation.reset()

        # Updating about information ↓
        self.__aboutInformationSetter()

        # Default Button's Behaviour Set ↓
        self.ui.buttonSelectFile.clicked.connect(self.__buttonSelectFile_Func)
        self.ui.buttonHashCalculate.clicked.connect(self.__buttonHashCalculate__Func)
        self.ui.buttonClearHashBox.clicked.connect(self.__buttonClearHashBox_Func)
        self.ui.buttonCopyToClipboard.clicked.connect(self.__buttonCopyToClipboard_Func)
        self.ui.buttonCheckHash.clicked.connect(self.__buttonCheckHash_Func)

        # Drag and Drop in GroupBoxHashCalculation ↓
        self.ui.groupBoxHashCalculation.setAcceptDrops(True)
        self.ui.groupBoxHashCalculation.dragEnterEvent = lambda event: event.accept()
        self.ui.groupBoxHashCalculation.dragMoveEvent = lambda event: event.accept()
        self.ui.groupBoxHashCalculation.dropEvent = (
            lambda event: self.__buttonSelectFile_Func(
                fileName=[url.toLocalFile() for url in event.mimeData().urls()]
            )
        )

        # Default ToolTip Information Setter ↓
        self.__toolTipInfoSetter()

        # Set License Text ↓
        self.ui.licenseTextBrowser.setText(informationManger().getLicense())

        # Hiding Menu Bar and Status Bar ↓
        self.ui.menubar.hide()
        self.ui.statusbar.hide()

        # Showing application update ↓
        # self.__updateMessageBox()

    def __updateMessageBox(self):
        appUpdates = updateManager()
        if appUpdates.haveUpdate() is True:
            updateData = appUpdates.getUpdateData()
            message: str = """<html><head/><body><p>Version: {0}</p><p>Go to download page, 
            <a style=\"text-decoration: none\" href=\"{1}\">Click Here</a></p></body></html>""".format(
                updateData["version"], updateData["update"]
            )
            QMessageBox.information(
                self, "New update!", message, QMessageBox.Ok, QMessageBox.Ok
            )
        else:
            pass

    # For launching windows in center ↓
    def __makeWindowCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    # Close button behaviour ↓
    @Slot(QCloseEvent)
    def closeEvent(self, event: QCloseEvent):
        buttonReply = QMessageBox.question(
            self,
            "Warning",
            "Sure to exit?",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Cancel,
        )
        if buttonReply == QMessageBox.Ok:
            try:
                self.__hashCalculator.terminateThread()
            except AttributeError:
                pass
            event.accept()
        else:
            event.ignore()

    def __aboutInformationSetter(self):
        info = informationManger()
        self.ui.developerName.setText(info.developerName)
        self.ui.developerEmail.setText(info.developerEmail)
        self.ui.logoCreditName.setText(info.logoCreditName)
        self.ui.logoCreditEmail.setText(info.logoCreditEmail)
        self.ui.icons8Credit.setText(info.icons8Credit)
        self.ui.sourceCodeLink.setText(info.sourceCodeLink)
        self.ui.applicationVersion.setText(info.applicationVersion)

    # Default ToolTip Information Setter↓
    def __toolTipInfoSetter(self):
        self.ui.buttonSelectFile.setToolTip("Click to select file.")
        self.ui.buttonHashCalculate.setToolTip("Start calculation.")
        self.ui.buttonClearHashBox.setToolTip("Clear all.")
        self.ui.buttonClearCheckHashBox.setToolTip("C")
        self.ui.buttonCopyToClipboard.setToolTip("Copy hash to the clipboard.")
        self.ui.buttonCheckHash.setToolTip("Paste & Check hash matching result.")
        self.ui.lineEditFileExplore.setToolTip(
            "Selected file location will be shown here."
        )
        self.ui.lineEditHashBox.setToolTip("Calculated hash will be shown here.")
        self.ui.progressBarHashCaclulation.setToolTip(
            "Calculation's progress will be shown here."
        )
        self.ui.buttonClearCheckHashBox.setToolTip("Clear pasted hash.")
        self.ui.lineEditCheckHashBox.setToolTip(
            "Pasted hash will be shown here for matching."
        )
        self.ui.developerName.setToolTip(informationManger().developerName)
        info = informationManger()
        self.ui.developerName.setToolTip(info.developerNameTooltip)
        self.ui.developerEmail.setToolTip(info.developerEmailTooltip)
        self.ui.logoCreditName.setToolTip(info.logoCreditNameTooltip)
        self.ui.logoCreditEmail.setToolTip(info.logoCreditEmailTooltip)
        self.ui.icons8Credit.setToolTip(info.icons8CreditTooltip)
        self.ui.sourceCodeLink.setToolTip(info.sourceCodeLinkTooltip)
        self.ui.applicationVersion.setToolTip(info.applicationVersionTooltip)
        self.ui.licenseTextBrowser.setToolTip(info.licenseTextBrowserTooltip)

    def __buttonSelectFile_Func(self, fileName: list = []):
        if not fileName:
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.AnyFile)
            fileName = dialog.getOpenFileName(
                self, self.tr(u"Select a File"), str(), self.tr(u"All Files (*)")
            )
        fileName = fileName[0]
        if fileName:
            self.ui.lineEditFileExplore.clear()
            self.ui.lineEditFileExplore.setText(fileName)
            self.ui.labelFileExplore.setPixmap(QPixmap(":ok/ok.png"))
            logging.info('File selected "{0}"'.format(fileName))
            try:
                self.ui.buttonHashCalculate.clicked.disconnect()
            except RuntimeError:
                pass
            self.ui.buttonHashCalculate.clicked.connect(
                self.__buttonHashCalculate__Func
            )

    def __buttonHashCalculate__Func(self):
        if not os.path.isfile(self.ui.lineEditFileExplore.text()):
            QMessageBox().warning(
                None, "Warning", "Please select a file to continue!", QMessageBox.Ok
            )
        else:
            self.__hashCalculator = HashingMethods()
            self.__hashCalculator.setHashName(self.ui.comboBoxHashChoices.currentText())
            self.__hashCalculator.setFileLoc(self.ui.lineEditFileExplore.text())
            self.__hashCalculator.signalEmitter.calculatedHash.connect(
                self.__on_finished_hash_calculation
            )
            self.__hashCalculator.signalEmitter.progressBarValue.connect(
                self.__on_going_progressbar
            )
            self.__hashCalculator.start()
            if self.__hashCalculator.isRunning():
                self.ui.progressBarHashCaclulation.setFormat("%p%")
                self.ui.buttonHashCalculate.setText("Cancel")
                self.ui.buttonHashCalculate.setIcon(QIcon(":/cancel/cancel.png"))
                self.ui.buttonHashCalculate.clicked.disconnect()
                self.ui.buttonHashCalculate.clicked.connect(
                    self.__btnHashCalculatorThreadCanceler_Func
                )

    # noinspection PyCallingNonCallable
    @Slot(str)
    def __on_finished_hash_calculation(self, calculatedHash):
        self.ui.lineEditHashBox.setText(calculatedHash)
        self.ui.buttonHashCalculate.setText("Calculate")
        self.ui.buttonHashCalculate.setIcon(QIcon(":/calculate/drawing-compass.png"))
        self.ui.buttonHashCalculate.clicked.disconnect()
        self.ui.buttonHashCalculate.clicked.connect(self.__buttonHashCalculate__Func)
        logging.info("Response received: " + calculatedHash)
        while self.__hashCalculator.isFinished() is False:
            time.sleep(0.5)
        logging.info("Hash Calculator Thread Finished")

    # noinspection PyTypeChecker,PyCallingNonCallable
    @Slot(int)
    def __on_going_progressbar(self, value):
        self.ui.progressBarHashCaclulation.setValue(value)

    def __btnHashCalculatorThreadCanceler_Func(self):
        buttonReply = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure to cancel?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if buttonReply == QMessageBox.Yes:
            self.__hashCalculator.terminateThread()
            self.ui.buttonHashCalculate.clicked.disconnect()
            self.ui.buttonHashCalculate.setText("Calculate")
            self.ui.buttonHashCalculate.setIcon(
                QIcon(":/calculate/drawing-compass.png")
            )
            self.ui.progressBarHashCaclulation.reset()
            self.ui.buttonHashCalculate.clicked.connect(
                self.__buttonHashCalculate__Func
            )
        else:
            pass

    def __buttonClearHashBox_Func(self):
        self.ui.lineEditFileExplore.clear()
        self.ui.labelFileExplore.setPixmap(QPixmap(u":/folder/opened-folder.png"))
        self.ui.lineEditHashBox.clear()
        self.ui.progressBarHashCaclulation.reset()
        try:
            if self.__hashCalculator.isRunning() is True:
                self.__btnHashCalculatorThreadCanceler_Func()
        except AttributeError:
            pass
        try:
            self.ui.buttonHashCalculate.clicked.disconnect()
        except RuntimeError:
            pass
        self.ui.buttonHashCalculate.clicked.connect(self.__buttonHashCalculate__Func)

    def __buttonCopyToClipboard_Func(self):
        self.__clipboard.setText(self.ui.lineEditHashBox.text())

    def __buttonCheckHash_Func(self):
        if not self.ui.lineEditHashBox.text().strip():
            return
        elif (
            self.ui.lineEditHashBox.text().strip()
            == self.ui.lineEditCheckHashBox.text().strip()
        ):
            QMessageBox.information(
                self,
                "Result",
                "Good news! It's Matched!",
                QMessageBox.Ok,
                QMessageBox.Ok,
            )
        else:
            QMessageBox.information(
                self, "Result", "Bad news! Not Matched!", QMessageBox.Ok, QMessageBox.Ok
            )


if __name__ == "__main__":
    print("Hello World")
