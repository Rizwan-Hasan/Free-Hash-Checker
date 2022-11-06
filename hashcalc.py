import logging
import os
from hashlib import md5, sha1, sha224, sha384, sha256, sha512

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QLineEdit

logging.basicConfig(level=logging.DEBUG, format="%(name)s - %(levelname)s : %(message)s")


class HashingMethods(QThread):
    __BLOCKSIZE: int = 32768
    __fileLoc: str
    __lineEditHashBox: QLineEdit
    __hashName: str
    __termination: bool

    calculatedHash = Signal(str)
    progressBarValue = Signal(int)

    def run(self):
        self.__hash_calculate()

    def set_blocksize(self, blocksize: int):
        self.__BLOCKSIZE = blocksize

    def set_file_loc(self, fileloc: str):
        self.__fileLoc = fileloc

    def set_hash_name(self, hash_name: str):
        self.__hashName = hash_name.lower()

    def get_hash(self):
        return self.__calculatedHash  # noqa

    def __hash_decider(self):
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

    def terminate_thread(self):
        if self.isRunning():
            self.__termination = True

    def __hash_calculate(self):
        count: int = 0
        size_count: int = 0
        file_size = os.stat(self.__fileLoc).st_size
        per_unit = file_size / 100
        hasher = self.__hash_decider()
        self.__termination = False
        with open(self.__fileLoc, "rb") as file:
            file_data = file.read(self.__BLOCKSIZE)
            while file_data:
                size_count += self.__BLOCKSIZE
                if size_count >= per_unit:
                    size_count -= per_unit
                    count += 1
                    self.progressBarValue.emit(count)  # noqa
                hasher.update(file_data)
                file_data = file.read(self.__BLOCKSIZE)
                if self.__termination:
                    file.close()
                    return
            else:
                count = 100
                self.progressBarValue.emit(count)  # noqa

            calculated_hash: str = hasher.hexdigest()
            logging.info("Response from the thread: " + calculated_hash)
            self.calculatedHash.emit(calculated_hash)  # noqa
            return


if __name__ == "__main__":
    print("Hello World")
