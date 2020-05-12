# -*- coding: utf-8 -*-

"""
__author__ = "Rizwan Hasan"
__copyright__ = "Copyright 2020"
__license__ = "MIT"
__version__ = "3.0"
__maintainer__ = "Rizwan Hasan"
__email__ = "rizwan.hasan486@gmail.com"

"""
import os
import sys

from PySide2.QtWidgets import QApplication, QStyleFactory

from hashchecker.app import MainWindow

# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
