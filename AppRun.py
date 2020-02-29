# -*- coding: utf-8 -*-

import sys

#
import requests
from PySide2.QtGui import qApp
from PySide2.QtWidgets import QApplication, QStyleFactory

from app import MainWindow


def main():
    app = QApplication(sys.argv)
    qApp.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
