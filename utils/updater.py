import os
import json
import requests


# Constants
MAIN_URL = "https://raw.githubusercontent.com/AzurAPI"
SHIP_LIST = f"{MAIN_URL}/azurapi-js-setup/master/ships.json"
CHAPTER_LIST = f"{MAIN_URL}/azurapi-js-setup/master/chapters.json"
EQUIPMENT_LIST = f"{MAIN_URL}/azurapi-js-setup/master/equipments.json"
VERSION_INFO = f"{MAIN_URL}/azurapi-js-setup/master/version-info.json"


class AzurApiUpdater:

    def __init__(self):
        self.current_dir = os.getcwd()
        self.data_folder = f"{self.current_dir}\data"

        if not os.path.exists(self.data_folder):
            os.mkdir(self.data_folder)

        self.ships_file = f"{self.data_folder}\\ships.json"
        self.equipments_file = f"{self.data_folder}\\equipments.json"
        self.chapters_file = f"{self.data_folder}\\chapters.json"
        self.version_file = f"{self.data_folder}\\version-info.json"

        self.files = [self.ships_file, self.equipments_file,
                      self.chapters_file, self.version_file]

    def update_check(self):

        update_check = []
        version_info = requests.get(VERSION_INFO).json()

        with open(self.version_file, "r") as file_data:
            file_data = json.load(file_data)

            local_version = [file_data["ships"]["version-number"],
                             file_data["equipments"]["version-number"]]

            repo_version = [version_info["ships"]["version-number"],
                            version_info["equipments"]["version-number"]]

            for i in range(len(local_version)):
                if local_version[i] < repo_version[i]:
                    update_check.append(True)
                else:
                    update_check.append(False)

            return update_check

    @staticmethod
    def download_data(file, data):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def version_update(self):

        ship_list = requests.get(SHIP_LIST).json()
        equipment_list = requests.get(EQUIPMENT_LIST).json()
        version_info = requests.get(VERSION_INFO).json()
        chapter_list = requests.get(CHAPTER_LIST).json()

        lists = [ship_list, equipment_list,
                 chapter_list, version_info]

        for i in range(len(self.files)):
            if os.path.isfile(self.files[i]):
                if os.stat(self.files[i]).st_size == 0:
                    self.download_data(self.files[i], lists[i])
                else:
                    continue
            else:
                self.download_data(self.files[i], lists[i])

        updates = self.update_check()

        for i in range(len(updates)):
            if updates[i]:
                self.download_data(self.files[i], lists[i])
