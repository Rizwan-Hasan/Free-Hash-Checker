# -*- coding: utf-8 -*-

import sys

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__main()

    def __main(self):
        self.ui.buttonSelectFile.clicked.connect(lambda func: self.__buttonSelectFile_Func())

    def __buttonSelectFile_Func(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        # noinspection PyTypeChecker
        fileName = dialog.getOpenFileName(
            self,
            self.tr(u"Select a File"), str(),
            self.tr(u"All Files (*)")
        )
        if fileName[0]:
            self.ui.lineEditFileExplore.clear()
            self.ui.lineEditFileExplore.setText(fileName[0])
            self.ui.labelFileExplore.setPixmap(QPixmap(":ok/ok.png"))
        print(fileName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
