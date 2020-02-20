# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication, QMainWindow

import buildAll
from ui.ui_mainwindow import Ui_MainWindow

buildAll.main(verbose=False)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
