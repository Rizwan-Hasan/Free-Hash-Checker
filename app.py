import logging
import os
import time

from PySide6.QtCore import Slot, QPropertyAnimation
from PySide6.QtGui import QCloseEvent, QGuiApplication, QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from hashcalc import HashingMethods
from infoManager import InformationManger
from ui.MainWindow import Ui_MainWindow
from UpdateManager import UpdateManager

logging.basicConfig(level=logging.DEBUG, format="%(name)s:%(levelname)s:%(message)s")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__hashCalculator: HashingMethods

        # Setting fixed window size to disable full screen ↓
        self.setMinimumWidth(self.minimumSizeHint().width())
        self.setMaximumHeight(self.minimumSizeHint().height())

        # ↓
        self.__main()

    def __main(self):
        # Making window centered ↓
        self.__make_window_center()

        # Window customizing ↓
        self.setWindowTitle("Free Hash Checker")

        # Clipboard setup ↓
        self.__clipboard = QApplication.clipboard()
        self.__clipboard.clear(mode=self.__clipboard.Mode.Clipboard)

        # Resetting progress bar ↓
        self.ui.progressBarHashCaclulation.reset()

        # Monkey-Patching The QProgressBar ↓
        self.ui.progressBarHashCaclulation.setValueWithAnimation = (
            lambda args: qprogressbar_set_value_with_animation(
                self.ui.progressBarHashCaclulation, args
            )
        )

        # Updating about information ↓
        self.__about_information_setter()

        # Default Button's Behaviour Set ↓
        self.ui.buttonSelectFile.clicked.connect(self.__button_select_file_func)
        self.ui.buttonHashCalculate.clicked.connect(self.__button_hash_calculate__func)
        self.ui.buttonClearHashBox.clicked.connect(self.__button_clear_hashbox__func)
        self.ui.buttonCopyToClipboard.clicked.connect(self.__button_copy_to_clipboard__func)
        self.ui.buttonCheckHash.clicked.connect(self.__button_check_hash__func)

        # Drag and Drop in groupBoxHashCalculation ↓
        self.ui.groupBoxHashCalculation.dragEnterEvent = lambda event: event.accept()
        self.ui.groupBoxHashCalculation.dragMoveEvent = lambda event: event.accept()
        self.ui.groupBoxHashCalculation.dropEvent = (
            lambda event: self.__button_select_file_func(
                file_name=[url.toLocalFile() for url in event.mimeData().urls()]
            )
        )

        # File Insertion Enabler/Disabler ↓
        self.__disable_or_enable_input(disable=False)

        # Default ToolTip Information Setter ↓
        self.__tooltip_info_setter()

        # Set License Text ↓
        self.ui.licenseTextBrowser.setText(InformationManger().get_license())

        # Hiding Menu Bar and Status Bar ↓
        self.ui.menubar.hide()
        self.ui.statusbar.hide()

        # Showing application update ↓
        # self.__update_message_box()

    def __update_message_box(self):
        app_updates = UpdateManager()
        if app_updates.have_update() is True:
            update_data = app_updates.get_update_data()
            message: str = """<html><head/><body><p>Version: {0}</p><p>Go to download page,
            <a style=\"text-decoration: none\" href=\"{1}\">Click Here</a></p></body></html>""".format(
                update_data["version"], update_data["update"]
            )
            QMessageBox.information(
                self, "New update!", message,
                QMessageBox.Ok, QMessageBox.Ok  # noqa
            )
        else:
            pass

    # For launching windows in center ↓
    def __make_window_center(self):
        qt_rectangle = self.frameGeometry()
        center_point = QGuiApplication.primaryScreen().geometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    # Close button behaviour ↓
    @Slot(QCloseEvent)
    def closeEvent(self, event: QCloseEvent):
        button_reply = QMessageBox.question(
            self,
            "Warning",
            "Sure to exit?",
            QMessageBox.Ok | QMessageBox.Cancel,  # noqa
            QMessageBox.Cancel,  # noqa
        )
        if button_reply == QMessageBox.Ok:  # noqa
            try:
                self.__hashCalculator.terminate_thread()
            except AttributeError:
                pass
            event.accept()
        else:
            event.ignore()

    # About Information Setter ↓
    def __about_information_setter(self):
        info = InformationManger()
        self.ui.developerName.setText(info.developerName)
        self.ui.developerEmail.setText(info.developerEmail)
        self.ui.logoCreditName.setText(info.logoCreditName)
        self.ui.logoCreditEmail.setText(info.logoCreditEmail)
        self.ui.icons8Credit.setText(info.icons8Credit)
        self.ui.sourceCodeLink.setText(info.sourceCodeLink)
        self.ui.applicationVersion.setText(info.applicationVersion)

    # Default ToolTip Information Setter ↓
    def __tooltip_info_setter(self):
        self.ui.buttonSelectFile.setToolTip("Click to select file.")
        self.ui.buttonHashCalculate.setToolTip("Start calculation.")
        self.ui.buttonClearHashBox.setToolTip("Clear all.")
        self.ui.buttonClearCheckHashBox.setToolTip("C")
        self.ui.buttonCopyToClipboard.setToolTip("Copy hash to the clipboard.")
        self.ui.buttonCheckHash.setToolTip("Paste & Check hash matching result.")
        self.ui.lineEditFileExplore.setToolTip(
            "Selected file location will be shown here."
        )
        self.ui.lineEditHashBox.setToolTip("Calculated hash will be shown here.")
        self.ui.progressBarHashCaclulation.setToolTip(
            "Calculation's progress will be shown here."
        )
        self.ui.buttonClearCheckHashBox.setToolTip("Clear pasted hash.")
        self.ui.lineEditCheckHashBox.setToolTip(
            "Pasted hash will be shown here for matching."
        )
        self.ui.developerName.setToolTip(InformationManger().developerName)
        info = InformationManger()
        self.ui.developerName.setToolTip(info.developerNameTooltip)
        self.ui.developerEmail.setToolTip(info.developerEmailTooltip)
        self.ui.logoCreditName.setToolTip(info.logoCreditNameTooltip)
        self.ui.logoCreditEmail.setToolTip(info.logoCreditEmailTooltip)
        self.ui.icons8Credit.setToolTip(info.icons8CreditTooltip)
        self.ui.sourceCodeLink.setToolTip(info.sourceCodeLinkTooltip)
        self.ui.applicationVersion.setToolTip(info.applicationVersionTooltip)
        self.ui.licenseTextBrowser.setToolTip(info.licenseTextBrowserTooltip)

    # Disabling Input's ↓
    def __disable_or_enable_input(self, disable: bool):
        self.ui.groupBoxHashCalculation.setAcceptDrops(False if disable else True)
        self.ui.buttonSelectFile.setDisabled(disable)
        self.ui.lineEditFileExplore.setDisabled(disable)

    def __button_select_file_func(self, file_name=None):
        if file_name is None:
            file_name = []
        if not file_name:
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.AnyFile)  # noqa
            file_name = dialog.getOpenFileName(
                self, self.tr("Select a File"), str(), self.tr("All Files (*)")  # noqa
            )
        file_name = file_name[0]
        if file_name:
            self.ui.lineEditFileExplore.clear()
            self.ui.lineEditFileExplore.setText(file_name)
            self.ui.labelFileExplore.setPixmap(QPixmap(":ok/ok.png"))
            logging.info('File selected "{0}"'.format(file_name))
            try:
                self.ui.buttonHashCalculate.clicked.disconnect()
            except RuntimeError:
                pass
            self.ui.buttonHashCalculate.clicked.connect(
                self.__button_hash_calculate__func
            )

    def __button_hash_calculate__func(self):
        if not os.path.isfile(self.ui.lineEditFileExplore.text()):
            QMessageBox().warning(
                None, "Warning", "Please select a file to continue!", QMessageBox.Ok  # noqa
            )
        else:
            self.__disable_or_enable_input(disable=True)
            self.__hashCalculator = HashingMethods()
            self.__hashCalculator.set_hash_name(self.ui.comboBoxHashChoices.currentText())
            self.__hashCalculator.set_file_loc(self.ui.lineEditFileExplore.text())
            self.__hashCalculator.calculatedHash.connect(
                self.__on_finished_hash_calculation
            )
            self.__hashCalculator.progressBarValue.connect(self.__on_going_progressbar)
            self.__hashCalculator.start()
            if self.__hashCalculator.isRunning():
                self.ui.progressBarHashCaclulation.setFormat("%p%")
                self.ui.buttonHashCalculate.setText("Cancel")
                self.ui.buttonHashCalculate.setIcon(QIcon(":/cancel/cancel.png"))
                self.ui.buttonHashCalculate.clicked.disconnect()
                self.ui.buttonHashCalculate.clicked.connect(
                    self.__btn_hash_calculator_thread_canceler__func
                )

    @Slot(str)
    def __on_finished_hash_calculation(self, calculated_hash: str):
        QMessageBox.information(
            self,
            "Result", "Calculation Finished",
            QMessageBox.Ok, QMessageBox.Ok,  # noqa
        )
        self.ui.lineEditHashBox.setText(calculated_hash)
        self.ui.buttonHashCalculate.setText("Calculate")
        self.ui.buttonHashCalculate.setIcon(QIcon(":/calculate/drawing-compass.png"))
        self.ui.buttonHashCalculate.clicked.disconnect()
        self.ui.buttonHashCalculate.clicked.connect(self.__button_hash_calculate__func)
        logging.info("Response received: " + calculated_hash)
        while self.__hashCalculator.isFinished() is False:
            time.sleep(0.5)
        logging.info("Hash Calculator Thread Finished")
        self.__disable_or_enable_input(disable=False)

    @Slot(int)
    def __on_going_progressbar(self, value: int):
        self.ui.progressBarHashCaclulation.setValueWithAnimation(value)

    def __btn_hash_calculator_thread_canceler__func(self):
        button_reply = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure to cancel?",
            QMessageBox.Yes | QMessageBox.No,  # noqa
            QMessageBox.No,  # noqa
        )
        if button_reply == QMessageBox.Yes:  # noqa
            self.__hashCalculator.terminate_thread()
            self.ui.buttonHashCalculate.clicked.disconnect()
            self.ui.buttonHashCalculate.setText("Calculate")
            self.ui.buttonHashCalculate.setIcon(
                QIcon(":/calculate/drawing-compass.png")
            )
            self.ui.progressBarHashCaclulation.reset()
            self.ui.buttonHashCalculate.clicked.connect(
                self.__button_hash_calculate__func
            )
            self.__disable_or_enable_input(disable=False)
        else:
            pass

    def __button_clear_hashbox__func(self):
        self.ui.lineEditFileExplore.clear()
        self.ui.labelFileExplore.setPixmap(QPixmap(":/folder/opened-folder.png"))
        self.ui.lineEditHashBox.clear()
        self.ui.progressBarHashCaclulation.reset()
        try:
            if self.__hashCalculator.isRunning() is True:
                self.__btn_hash_calculator_thread_canceler__func()
        except AttributeError:
            pass
        try:
            self.ui.buttonHashCalculate.clicked.disconnect()
            QMessageBox.information(
                self,
                "Cleared",
                "Successfull",
                QMessageBox.Ok,  # noqa
                QMessageBox.Ok,  # noqa
            )
        except RuntimeError:
            pass
        self.ui.buttonHashCalculate.clicked.connect(self.__button_hash_calculate__func)

    def __button_copy_to_clipboard__func(self):
        self.__clipboard.setText(self.ui.lineEditHashBox.text())
        QMessageBox.information(
            self,
            "Copied", "Copied to your clipboard",
            QMessageBox.Ok, QMessageBox.Ok,  # noqa
        )

    def __button_check_hash__func(self):
        if not self.ui.lineEditHashBox.text().strip():
            return
        elif self.ui.lineEditHashBox.text().strip() == self.ui.lineEditCheckHashBox.text().strip():
            QMessageBox.information(
                self,
                "Result", "Good news! It's Matched!",
                QMessageBox.Ok, QMessageBox.Ok,  # noqa
            )
        else:
            QMessageBox.information(
                self, "Result", "Bad news! Not Matched!",
                QMessageBox.Ok, QMessageBox.Ok  # noqa
            )


# Monkey-Patching Function the QProgressBar inorder to get Animation
def qprogressbar_set_value_with_animation(self, value: int):
    if hasattr(self, "animation"):
        self.animation.stop()
    else:
        self.animation = QPropertyAnimation(targetObject=self, propertyName=b"value")
        self.animation.setDuration(100)
    self.animation.setStartValue(self.value())
    self.animation.setEndValue(value)
    self.animation.start()


if __name__ == "__main__":
    print("Hello World")
