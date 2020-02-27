import sys

from PySide2.QtWidgets import QApplication, QStyleFactory

import buildAll
from main import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    # qApp.setStyle(QStyleFactory.create("Fusion"))
    # darkPalette = QPalette()
    # darkColor = QColor(45, 45, 45)
    # disabledColor = QColor(127, 127, 127)
    # darkPalette.setColor(QPalette.Window, darkColor)
    # darkPalette.setColor(QPalette.WindowText, Qt.white)
    # darkPalette.setColor(QPalette.Base, QColor(40, 40, 40))
    # darkPalette.setColor(QPalette.AlternateBase, darkColor)
    # darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
    # darkPalette.setColor(QPalette.ToolTipText, Qt.white)
    # darkPalette.setColor(QPalette.Text, Qt.white)
    # darkPalette.setColor(QPalette.Disabled, QPalette.Text, disabledColor)
    # darkPalette.setColor(QPalette.Button, darkColor)
    # darkPalette.setColor(QPalette.ButtonText, Qt.white)
    # darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, disabledColor)
    # darkPalette.setColor(QPalette.BrightText, Qt.red)
    # darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
    # darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    # darkPalette.setColor(QPalette.HighlightedText, Qt.black)
    # darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, disabledColor)
    # qApp.setPalette(darkPalette)
    # qApp.setStyleSheet("""
    #     QToolTip {
    #         color: #ffffff;
    #         background-color: #2A82DA;
    #         border: 1px solid white;
    #     }""")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    buildAll.main()
    main()
