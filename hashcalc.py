import logging
import os
from hashlib import md5, sha1, sha224, sha384, sha256, sha512

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QLineEdit

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s - %(levelname)s : %(message)s"
)


class HashingMethods(QThread):
    __BLOCKSIZE: int = 32768
    __fileLoc: str
    __lineEditHashBox: QLineEdit
    __hashName: str
    __termination: bool

    calculatedHash = Signal(str)
    progressBarValue = Signal(int)

    def run(self):
        self.__hashCalculate()

    def setBLOCKSIZE(self, blocksize: int):
        self.__BLOCKSIZE = blocksize

    def setFileLoc(self, fileLoc: str):
        self.__fileLoc = fileLoc

    def setHashName(self, hashName: str):
        self.__hashName = hashName.lower()

    def getHash(self):
        return self.__calculatedHash

    def __hashDecider(self):
        if self.__hashName == "md5":
            return md5()
        elif self.__hashName == "sha1":
            return sha1()
        elif self.__hashName == "sha224":
            return sha224()
        elif self.__hashName == "sha256":
            return sha256()
        elif self.__hashName == "sha384":
            return sha384()
        elif self.__hashName == "sha512":
            return sha512()

    def terminateThread(self):
        if self.isRunning():
            self.__termination = True

    def __hashCalculate(self):
        count: int = 0
        sizeCount: int = 0
        fileSize = os.stat(self.__fileLoc).st_size
        perUnit = fileSize / 100
        hasher = self.__hashDecider()
        self.__termination = False
        with open(self.__fileLoc, "rb") as file:
            fileData = file.read(self.__BLOCKSIZE)
            while fileData:
                sizeCount += self.__BLOCKSIZE
                if sizeCount >= perUnit:
                    sizeCount -= perUnit
                    count += 1
                    self.progressBarValue.emit(count)
                hasher.update(fileData)
                fileData = file.read(self.__BLOCKSIZE)
                if self.__termination:
                    file.close()
                    return
            else:
                count = 100
                self.progressBarValue.emit(count)

            calculatedHash: str = hasher.hexdigest()
            logging.info("Response from the thread: " + calculatedHash)
            self.calculatedHash.emit(calculatedHash)
            return


if __name__ == "__main__":
    print("Hello World")
