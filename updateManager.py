import logging

import requests

import infoManager

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s:%(levelname)s:%(message)s'
)


class updateManager:

    def __init__(self):
        self.__url: str = 'https://rizwan-hasan.github.io/Free-Hash-Checker/updates.json'
        self.__updateData: dict

    def haveUpdate(self):
        if self.__checkUpdate() is True:
            if self.__updateData['version'] != infoManager.informationManger().version:
                return True
            else:
                return False
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
        return self.__updateData


updateManager().haveUpdate()
