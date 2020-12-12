import logging
import platform

import requests

import infoManager

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s:%(levelname)s:%(message)s')


class updateManager:
    def __init__(self):
        self.__url: str = 'https://rizwan-hasan.github.io/Free-Hash-Checker/updates.json'
        self.__updateData: dict = {
            'version': infoManager.informationManger().version
        }
        try:
            self.__updateData = requests.get(self.__url).json()
        except requests.exceptions.ConnectionError:
            logging.warning('No Internet! Can\'t check updates')

    def haveUpdate(self):
        if self.__updateData['version'] != infoManager.informationManger(
        ).version:
            return True
        else:
            return False

    def __checkUpdate(self):
        try:
            self.__updateData = requests.get(self.__url).json()
            return True
        except requests.exceptions.ConnectionError:
            logging.warning('No Internet! Can\'t check updates')
            return False

    def getUpdateData(self):
        if platform.system().lower() == 'windows':
            del self.__updateData['linux']
            self.__updateData['update'] = self.__updateData['windows']
            del self.__updateData['windows']
        else:
            del self.__updateData['windows']
            self.__updateData['update'] = self.__updateData['linux']
            del self.__updateData['linux']

        return self.__updateData


if __name__ == "__main__":
    print('Hello World')
