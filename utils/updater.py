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
        self.chapters_file = f"{self.data_folder}\\chapters.json"
        self.equipments_file = f"{self.data_folder}\\equipments.json"
        self.version_file = f"{self.data_folder}\\version-info.json"
        
        self.files = [self.ships_file, self.chapters_file, self.equipments_file, self.version_file]
        
    def update_check(self):
        
        update_check = []
        version_info = requests.get(VERSION_INFO).json()
        
        with open(self.version_file, "r") as file_data:
            file_data = json.load(file_data)
            
            if file_data["ships"]["version-number"] < version_info["ships"]["version-number"]:
                update_check.append(True)
            else:
                update_check.append(False)
                
            if file_data["equipments"]["version-number"] < version_info["equipments"]["version-number"]:
                update_check.append(True)
            else:
                update_check.append(False)
                
            return update_check

    def version_update(self):
                
        ship_list = requests.get(SHIP_LIST).json()
        equipment_list = requests.get(EQUIPMENT_LIST).json()
        version_info = requests.get(VERSION_INFO).json()
        chapter_list = requests.get(CHAPTER_LIST).json()
        _list = [ship_list, chapter_list, equipment_list, version_info]
        
        if not os.listdir(self.data_folder):
            for i in range(len(self.files)):
                with open(self.files[i], "w", encoding="utf-8") as f:
                    json.dump(_list[i], f, ensure_ascii=False, indent=4)
                    
        ship_update, equipment_update = self.update_check()
        
        if ship_update:
            with open(self.ships_file, "w", encoding="utf-8") as f:
                json.dump(ship_list, f, ensure_ascii=False, indent=4)
                
        if equipment_update:
            with open(self.equipments_file, "w", encoding="utf-8") as f:
                json.dump(equipment_list, f, ensure_ascii=False, indent=4)