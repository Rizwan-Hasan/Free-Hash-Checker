# -*- coding: utf-8 -*-

import logging
import sys
import time

from PySide2.QtCore import Slot
from PySide2.QtGui import QPixmap, QGuiApplication
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog

from hashcalc import HashingMethods
from ui.ui_mainwindow import Ui_MainWindow

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s - %(levelname)s : %(message)s'
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

        # Default Button Setter Functions ↓
        self.ui.buttonSelectFile.clicked.connect(lambda func: self.__buttonSelectFile_Func())
        self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())

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

    def __buttonHashCalculate__Func(self):
        self.__hashCalculator = HashingMethods()
        self.__hashCalculator.setHashName('sha256')
        self.__hashCalculator.setFileLoc(self.ui.lineEditFileExplore.text())
        self.__hashCalculator.signalEmitter.calculatedHash.connect(self.__on_finished_hash_calculation)
        self.__hashCalculator.signalEmitter.progressBarValue.connect(self.__on_going_progressbar)
        self.__hashCalculator.start()

    @Slot(str)
    def __on_finished_hash_calculation(self, calculatedHash):
        self.ui.lineEditHashBox.setText(calculatedHash)
        logging.info('Response received: ' + calculatedHash)
        while self.__hashCalculator.isFinished() is False:
            time.sleep(0.5)
        logging.info('Hash Calculator Thread Finished')

    # noinspection PyTypeChecker
    @Slot(int)
    def __on_going_progressbar(self, value):
        if self.__hashCalculator.isRunning():
            self.ui.progressBarHashCaclulation.setFormat('%p%')
            self.ui.buttonHashCalculate.setText('Cancel')
            self.ui.buttonHashCalculate.clicked.disconnect()
            self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__btnHashCalculatorThreadCanceler_Func())
        if value == 100:
            self.ui.progressBarHashCaclulation.setFormat('Finished')
            self.ui.buttonHashCalculate.clicked.disconnect()
            self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())
        self.ui.progressBarHashCaclulation.setValue(value)

    def __btnHashCalculatorThreadCanceler_Func(self):
        self.__hashCalculator.terminateThread()
        print('Request QUIT')
        while self.__hashCalculator.isRunning():
            print('Running: {0}'.format(self.__hashCalculator.isRunning()))
        else:
            print('Running: {0}'.format(self.__hashCalculator.isRunning()))
        self.ui.buttonHashCalculate.clicked.disconnect()
        self.ui.buttonHashCalculate.setText('Calculate')
        self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
