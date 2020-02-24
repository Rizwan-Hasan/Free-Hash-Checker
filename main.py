# -*- coding: utf-8 -*-

import logging
import os
import sys
import time

from PySide2.QtCore import Slot
from PySide2.QtGui import QPixmap, QGuiApplication
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QStyleFactory, QMessageBox

from hashcalc import HashingMethods
from ui.ui_mainwindow import Ui_MainWindow

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s:%(levelname)s:%(message)s'
)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__hashCalculator: HashingMethods
        #
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__makeWindowCenter()

        # Window customizing ↓
        self.setWindowTitle('Free Hash Checker')

        # Clipboard setup ↓
        self.__clipboard = QApplication.clipboard()
        self.__clipboard.clear(mode=self.__clipboard.Clipboard)

        # Resetting progress bar ↓
        self.ui.progressBarHashCaclulation.reset()

        # Default Button's Behaviour Set ↓
        self.ui.buttonSelectFile.clicked.connect(lambda func: self.__buttonSelectFile_Func())
        self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())
        self.ui.buttonClearHashBox.clicked.connect(lambda func: self.__buttonClearHashBox_Func())
        self.ui.buttonCopyToClipboard.clicked.connect(lambda func: self.__buttonCopyToClipboard_Func())
        self.ui.buttonCheckHash.clicked.connect(lambda func: self.__buttonCheckHash_Func())

    # For launching windows in center ↓
    def __makeWindowCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def __buttonSelectFile_Func(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        # noinspection PyTypeChecker
        fileName = dialog.getOpenFileName(
            self,
            self.tr(u"Select a File"), str(),
            self.tr(u"All Files (*)")
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
            self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())

    def __buttonHashCalculate__Func(self):
        if not os.path.isfile(self.ui.lineEditFileExplore.text()):
            # noinspection PyTypeChecker
            QMessageBox().warning(None, 'Warning', 'Please select a file to continue!', QMessageBox.Abort)
        else:
            self.__hashCalculator = HashingMethods()
            self.__hashCalculator.setHashName(self.ui.comboBoxHashChoices.currentText())
            self.__hashCalculator.setFileLoc(self.ui.lineEditFileExplore.text())
            self.__hashCalculator.signalEmitter.calculatedHash.connect(self.__on_finished_hash_calculation)
            self.__hashCalculator.signalEmitter.progressBarValue.connect(self.__on_going_progressbar)
            self.__hashCalculator.start()
            if self.__hashCalculator.isRunning():
                self.ui.progressBarHashCaclulation.setFormat('%p%')
                self.ui.buttonHashCalculate.setText('Cancel')
                self.ui.buttonHashCalculate.clicked.disconnect()
                self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__btnHashCalculatorThreadCanceler_Func())

    @Slot(str)
    def __on_finished_hash_calculation(self, calculatedHash):
        self.ui.lineEditHashBox.setText(calculatedHash)
        self.ui.buttonHashCalculate.setText('Calculate')
        self.ui.buttonHashCalculate.clicked.disconnect()
        self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())
        logging.info('Response received: ' + calculatedHash)
        while self.__hashCalculator.isFinished() is False:
            time.sleep(0.5)
        logging.info('Hash Calculator Thread Finished')

    # noinspection PyTypeChecker
    @Slot(int)
    def __on_going_progressbar(self, value):
        self.ui.progressBarHashCaclulation.setValue(value)

    def __btnHashCalculatorThreadCanceler_Func(self):
        self.__hashCalculator.terminateThread()
        self.ui.buttonHashCalculate.clicked.disconnect()
        self.ui.buttonHashCalculate.setText('Calculate')
        self.ui.progressBarHashCaclulation.reset()
        self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())

    def __buttonClearHashBox_Func(self):
        self.ui.lineEditFileExplore.clear()
        self.ui.lineEditHashBox.clear()
        self.ui.progressBarHashCaclulation.reset()
        try:
            self.ui.buttonHashCalculate.clicked.disconnect()
        except RuntimeError:
            pass
        self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())

    def __buttonCopyToClipboard_Func(self):
        self.__clipboard.setText(self.ui.lineEditHashBox.text())

    def __buttonCheckHash_Func(self):
        self.ui.lineEditCheckHashBox.setText(self.__clipboard.text())


def main():
	app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
