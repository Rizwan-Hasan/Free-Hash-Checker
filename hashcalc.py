import os
from hashlib import md5, sha1, sha224, sha384, sha256, sha512

from PySide2.QtCore import QThread
from PySide2.QtWidgets import QProgressBar, QLineEdit
from tqdm import tqdm


class HashingMethods(QThread):
    # Specifying how many bytes of the file to open at a time ↓
    __BLOCKSIZE = 4096  # 4096 Byte = 4 KiloByte
    __fileLoc: str = str()
    __progressBar: QProgressBar
    __hashName: str = str()
    __lineEditHashBox: QLineEdit

    def run(self):
        self.__lineEditHashBox.clear()
        self.__lineEditHashBox.setText(self.__hashCalculate())
        self.quit()

    def setBLOCKSIZE(self, blocksize: int):
        self.__BLOCKSIZE = blocksize

    def setFile(self, fileLoc: str):
        self.__fileLoc = fileLoc

    def setHashName(self, hashName: str):
        self.__hashName = hashName

    def setLineEditHashBox(self, lineEditHashBox: QLineEdit):
        self.__lineEditHashBox = lineEditHashBox

    def setProgressBar(self, progressBar: QProgressBar):
        self.__progressBar = progressBar

    # noinspection PyMethodMayBeStatic
    def __hashDecider(self):
        if self.__hashName == 'md5':
            return md5()
        elif self.__hashName == 'sha1':
            return sha1
        elif self.__hashName == 'sha224':
            return sha224
        elif self.__hashName == 'sha256':
            return sha256
        elif self.__hashName == 'sha384':
            return sha384
        elif self.__hashName == 'sha512':
            return sha512

    def __hashCalculate(self):
        count: int = 0
        sizeCount: int = 0
        fileSize = os.stat(self.__fileLoc).st_size
        perUnit = fileSize / 100
        hasher = self.__hashDecider()
        with open(self.__fileLoc, 'rb') as file:
            fileData = file.read(self.__BLOCKSIZE)
            consoleProgressBar: tqdm = tqdm(total=100)
            while fileData:
                sizeCount += self.__BLOCKSIZE
                if sizeCount >= perUnit:
                    sizeCount -= perUnit
                    count += 1
                    consoleProgressBar.update(1)
                    self.__progressBar.setValue(self.__progressBar.value() + 1)
                hasher.update(fileData)
                fileData = file.read(self.__BLOCKSIZE)
            else:
                count = 100
                consoleProgressBar.update(count)
                consoleProgressBar.close()
                self.__progressBar.setValue(count)
            return hasher.hexdigest()


if __name__ == '__main__':
    print('Hello World')
