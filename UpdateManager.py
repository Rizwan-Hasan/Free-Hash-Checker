import logging
import platform

import requests

import infoManager

logging.basicConfig(level=logging.DEBUG, format="%(name)s:%(levelname)s:%(message)s")


class UpdateManager:
    def __init__(self):
        self.__url = "https://rizwan-hasan.github.io/Free-Hash-Checker/updates.json"
        self.__updateData = {"version": infoManager.InformationManger().version}
        try:
            self.__updateData = requests.get(self.__url).json()
        except requests.exceptions.ConnectionError:
            logging.warning("No Internet! Can't check updates")

    def have_update(self):
        if self.__updateData["version"] != infoManager.InformationManger().version:
            return True
        return False

    def __check_update(self):
        try:
            self.__updateData = requests.get(self.__url).json()
            return True
        except requests.exceptions.ConnectionError:
            logging.warning("No Internet! Can't check updates")
        return False

    def get_update_data(self):
        if platform.system().lower() == "windows":
            del self.__updateData["linux"]
            self.__updateData["update"] = self.__updateData["windows"]
            del self.__updateData["windows"]

        del self.__updateData["windows"]
        self.__updateData["update"] = self.__updateData["linux"]
        del self.__updateData["linux"]

        return self.__updateData


if __name__ == "__main__":
    print("Hello World")
