# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication, QStyleFactory

import buildAll
from main import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    buildAll.main()
    main()
