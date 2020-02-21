import os
from hashlib import md5, sha1, sha224, sha384, sha256, sha512

from PySide2.QtCore import QThread
from PySide2.QtWidgets import QProgressBar
from tqdm import tqdm


class HashingMethods(QThread):
    # Specifying how many bytes of the file to open at a time ↓
    __BLOCKSIZE = 4096  # 4096 Byte = 4 KiloByte
    __fileLoc: str = str()
    __progressBar: QProgressBar

    def run(self):
        print()

    def setBLOCKSIZE(self, blocksize: int):
        self.__BLOCKSIZE = blocksize

    def setFile(self, fileLoc: str):
        self.__fileLoc = fileLoc

    def setProgressBar(self, progressBar: QProgressBar):
        self.__progressBar = progressBar

    # noinspection PyMethodMayBeStatic
    def __hashDecider(self, hashName: str):
        if hashName == 'md5':
            return md5()
        elif hashName == 'sha1':
            return sha1
        elif hashName == 'sha224':
            return sha224
        elif hashName == 'sha256':
            return sha256
        elif hashName == 'sha384':
            return sha384
        elif hashName == 'sha512':
            return sha512

    def __hashCalculate(self, hashName: str):
        count: int = 0
        sizeCount: int = 0
        fileSize = os.stat(self.__fileLoc).st_size
        perUnit = fileSize / 100
        hasher = self.__hashDecider(hashName)
        with open(self.__fileLoc, 'rb') as file:
            fileData = file.read(self.__BLOCKSIZE)
            consoleProgressBar: tqdm = tqdm(total=100)
            while fileData:
                sizeCount += self.__BLOCKSIZE
                if sizeCount >= perUnit:
                    sizeCount -= perUnit
                    count += 1
                    consoleProgressBar.update(1)
                hasher.update(fileData)
                fileData = file.read(self.__BLOCKSIZE)
            else:
                count = 100
                consoleProgressBar.update(count)
                consoleProgressBar.close()
            return hasher.hexdigest()
