import os
import json
import requests


# Constants
MAIN_URL = "https://raw.githubusercontent.com/AzurAPI"
SHIP_LIST = f"{MAIN_URL}/azurapi-js-setup/master/ships.json"
CHAPTER_LIST = f"{MAIN_URL}/azurapi-js-setup/master/chapters.json"
EQUIPMENT_LIST = f"{MAIN_URL}/azurapi-js-setup/master/equipments.json"
VERSION_INFO = f"{MAIN_URL}/azurapi-js-setup/master/version-info.json"
MEMORIES_INFO = f"{MAIN_URL}/azurapi-js-setup/master/memories.json"

class AzurApiUpdater:

    def __init__(self, folder):
        self.current_dir = folder
        self.data_folder = f"{self.current_dir}{os.sep}data"

        # Create data folder if it does not exist
        if not os.path.exists(self.data_folder):
            os.mkdir(self.data_folder)

        self.ships_file = f"{self.data_folder}{os.sep}ships.json"
        self.equipments_file = f"{self.data_folder}{os.sep}equipments.json"
        self.chapters_file = f"{self.data_folder}{os.sep}chapters.json"
        self.version_file = f"{self.data_folder}{os.sep}version-info.json"
        self.memories_files = f"{self.data_folder}{os.sep}memories.json"

        self.files = [self.ships_file, self.equipments_file,
                      self.chapters_file, self.version_file,
                      self.memories_files]

    def update_check(self):

        update_check = []
        version_info = requests.get(VERSION_INFO).json()

        with open(self.version_file, "r") as file_data:
            file_data = json.load(file_data)

            local_version = [file_data["ships"]["version-number"],
                             file_data["equipments"]["version-number"]]

            repo_version = [version_info["ships"]["version-number"],
                            version_info["equipments"]["version-number"]]

            # If local version is less than repo version, an update is needed
            # Therefore, True is appended to the list
            for i in range(len(local_version)):
                if local_version[i] < repo_version[i]:
                    update_check.append(True)
                else:
                    update_check.append(False)

            return update_check

    @staticmethod
    def __download_data(file, data):
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def version_update(self):

        ship_list = requests.get(SHIP_LIST).json()
        equipment_list = requests.get(EQUIPMENT_LIST).json()
        chapter_list = requests.get(CHAPTER_LIST).json()
        version_info = requests.get(VERSION_INFO).json()
        memories_info = requests.get(MEMORIES_INFO).json()

        lists = [ship_list, equipment_list,
                 chapter_list, version_info,
                 memories_info]

        for i in range(len(self.files)):

            # If file does not exist, download new data
            if os.path.isfile(self.files[i]):

                # If file exists but is empty, download new data
                if os.stat(self.files[i]).st_size == 0:
                    self.__download_data(self.files[i], lists[i])
                else:
                    continue
            else:
                self.__download_data(self.files[i], lists[i])

        # Returns a list e.g. [True, True]
        # element[0] for ships, element[1] for equipments
        updates = self.update_check()

        for i in range(len(updates)):
            if updates[i]:
                self.__download_data(self.files[i], lists[i])
