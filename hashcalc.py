import time

from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QProgressBar


class Hashing(QThread):
    mytest = Signal(str)
    test: QProgressBar

    def run(self):
        print('task started')
        k = 0
        for i in range(1, 100+1):
            time.sleep(.1)
            self.test.setValue(i)
            print(self.test.value())
        print('task finished')

        print(self.exit())
