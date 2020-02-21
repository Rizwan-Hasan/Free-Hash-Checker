# -*- coding: utf-8 -*-

import logging
import sys

from PySide2.QtCore import Slot, QThreadPool
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
        self.__hashCalculator = HashingMethods()
        self.pool = QThreadPool()
        #
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__makeWindowCenter()

        # Window customizing ↓
        self.setWindowTitle('Free Hash Checker')

        # Button Setter Functions ↓
        self.__buttonFunctionSetter()

    # For launching windows in center ↓
    def __makeWindowCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def __buttonFunctionSetter(self):
        self.ui.buttonSelectFile.clicked.connect(lambda func: self.__buttonSelectFile_Func())
        self.ui.buttonHashCalculate.clicked.connect(lambda func: self.__buttonHashCalculate__Func())

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
        self.__hashCalculator.emitter.done.connect(self.__on_worker_done)
        self.__hashCalculator.setProgressBar(self.ui.progressBarHashCaclulation)
        self.__hashCalculator.start()

    @Slot(str)
    def __on_worker_done(self, calculatedHash):
        # modify the UI
        self.ui.lineEditHashBox.setText(calculatedHash)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
