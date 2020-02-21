import logging
import os
from hashlib import md5, sha1, sha224, sha384, sha256, sha512

from PySide2.QtCore import QThread, Signal, QObject
from PySide2.QtWidgets import QLineEdit
from tqdm import tqdm

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s - %(levelname)s : %(message)s'
)


class HashingMethods(QThread):
    __BLOCKSIZE: int = 4096
    __fileLoc: str
    __lineEditHashBox: QLineEdit
    __hashName: str

    class __SignalEmitter(QObject):
        calculatedHash = Signal(str)
        progressBarValue = Signal(int)

    signalEmitter = __SignalEmitter()

    def run(self):
        self.__hashCalculate()
        self.quit()

    def setBLOCKSIZE(self, blocksize: int):
        self.__BLOCKSIZE = blocksize

    def setFileLoc(self, fileLoc: str):
        self.__fileLoc = fileLoc

    def setHashName(self, hashName: str):
        self.__hashName = hashName

    def getHash(self):
        return self.__calculatedHash

    # noinspection PyMethodMayBeStatic
    def __hashDecider(self):
        if self.__hashName == 'md5':
            return md5()
        elif self.__hashName == 'sha1':
            return sha1()
        elif self.__hashName == 'sha224':
            return sha224()
        elif self.__hashName == 'sha256':
            return sha256()
        elif self.__hashName == 'sha384':
            return sha384()
        elif self.__hashName == 'sha512':
            return sha512()

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
                    # noinspection PyUnresolvedReferences
                    self.signalEmitter.progressBarValue.emit(count)
                hasher.update(fileData)
                fileData = file.read(self.__BLOCKSIZE)
            else:
                count = 100
                consoleProgressBar.update(count)
                consoleProgressBar.close()
                # noinspection PyUnresolvedReferences
                self.signalEmitter.progressBarValue.emit(count)

            calculatedHash: str = hasher.hexdigest()
            logging.info(calculatedHash)
            # noinspection PyUnresolvedReferences
            self.signalEmitter.calculatedHash.emit(calculatedHash)


if __name__ == '__main__':
    print('Hello World')
