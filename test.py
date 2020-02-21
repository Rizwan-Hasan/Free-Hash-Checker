import random
import time

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import Slot, Signal, QObject, QRunnable


class MyEmitter(QObject):
    # setting up custom signal
    done = Signal(str)


class MyWorker(QRunnable):

    def __init__(self, name):
        super(MyWorker, self).__init__()
        self.name = name
        self.emitter = MyEmitter()

    def run(self):
        nap = random.choice(range(1, 10))
        print(f"{self.name} worker starting to run for {nap} seconds.")
        time.sleep(nap)
        print(f"{self.name} worker finishing up -> emit signal")
        self.emitter.done.emit(str(self.name))


class MyMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setFixedSize(150, 100)
        self.btn = QtWidgets.QPushButton("launch thread pool")
        self.btn.clicked.connect(self.launch_threadpool)
        self.lbl = QtWidgets.QLabel()
        self.lbl.setText("output label")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.lbl)
        self.setLayout(self.layout)
        self.pool = QtCore.QThreadPool()

    def launch_threadpool(self):
        print("launch_threadpool")
        for name in ("first", "second", "third"):
            worker = MyWorker(name)
            worker.emitter.done.connect(self.on_worker_done)
            self.pool.start(worker)
            time.sleep(0.1)  # to let print() complete lines

    @Slot(str)
    def on_worker_done(self, worker):
        # modify the UI
        print("updating UI")
        self.lbl.setText(f"{worker} worker finished")


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    MainWindow = MyMainWindow()
    MainWindow.show()
    app.exec_()
