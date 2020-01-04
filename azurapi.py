import json
import requests

from utils import exceptions, is_str_int


# Constants
MAIN_URL = "https://raw.githubusercontent.com/AzurAPI"
SHIP_LIST = f"{MAIN_URL}/azurapi-js-setup/master/ships.json"
CHAPTER_LIST = f"{MAIN_URL}/azurapi-js-setup/master/chapters.json"
EQUIPMENT_LIST = f"{MAIN_URL}/azurapi-js-setup/master/equipments.json"
VERSION_INFO = f"{MAIN_URL}/azurapi-js-setup/master/version-info.json"
AVAILABLE_LANGS = ["en", "cn", "jp", "kr", "code"]


class AzurAPI:

    def __init__(self):
        self.ship_list = requests.get(SHIP_LIST).json()
        self.chapter_list = requests.get(CHAPTER_LIST).json()
        self.equipment_list = requests.get(EQUIPMENT_LIST).json()
        self.version_info = requests.get(VERSION_INFO).json()

    def get_version(self):
        ships_version = self.version_info["ships"]["version-number"]
        equipments_version = self.version_info["equipments"]["version-number"]
        return f"Ships Version: {ships_version} | Equipments Version: {equipments_version}"

    # Not necessary since user can just access the property but this is just more user friendly
    def get_all_ships(self):
        return self.ship_list

    def get_ship_by_id(self, sid):

        # Makes sure it is an integer if a string was used as input and error for floats
        if isinstance(sid, str) and not is_str_int(sid):
            raise ValueError("a non integer input was given (string)")
        elif isinstance(sid, float):
            raise ValueError("a non integer input was given (float)")
        elif isinstance(sid, int):
            sid = str(sid)

        if len(sid) != 3:
            raise ValueError("id must be padded to 3 digits long e.g. 077")

        if sid not in self.ship_list:
            raise exceptions.UnknownShipException("the id provided does not match any ships")

        return self.ship_list[sid]

    def get_ship_by_name(self, name):

        # As of now, I cannot think of a better way to do this than nested loops
        for ship_id in self.ship_list:

            ship_names = self.ship_list[ship_id]["names"]
            for lang in ship_names:

                # I validated None just in case a name is missing somewhere
                if ship_names[lang] is None:
                    continue

                # Case insensitive check for the name of the ship
                if ship_names[lang].lower() == name.lower():
                    return self.ship_list[ship_id]

        raise exceptions.UnknownShipException("the name provided does not match any ships")

    def get_ship(self, ship):

        # As per recommended by Python's EAFP rule, nested try/except is used
        # Tries to find by id first, then move to find by name if failed
        # If both failed, raise an error message
        try:
            return self.get_ship_by_id(ship)
        except (ValueError, exceptions.UnknownShipException):
            try:
                return self.get_ship_by_name(ship)
            except exceptions.UnknownShipException:
                raise exceptions.UnknownShipException("the input provided does not match any ships")
        
    def get_all_ships_by_lang(self, language):
        
        if language not in AVAILABLE_LANGS:
            raise exceptions.UnknownLanguageException("the language provided is not supported")
        
        found_ships = []
    
        for ship_id in self.ship_list:
            
            ship_names = self.ship_list[ship_id]["names"]
            if ship_names[language] is None:
                continue
                
            found_ships.append(self.ship_list[ship_id])
        
        return found_ships
    
    def get_all_ships_by_en_names(self):
        return self.get_all_ships_by_lang("en")
    
    def get_all_ships_by_cn_names(self):
        return self.get_all_ships_by_cn_names("cn")
    
    def get_all_ships_by_jp_names(self):
        return self.get_all_ships_by_cn_names("jp")
    
    def get_all_ships_by_kr_names(self):
        return self.get_all_ships_by_cn_names("kr")
    
    def get_all_ships_by_code_names(self):
        return self.get_all_ships_by_cn_names("code")
    
    def get_ship_by_lang(self, language, name):
        
        ships_list = self.get_all_ships_by_lang(language)
        ship = [ship for ship in azurapi.get_all_ships_by_en_names() if ship.get("names")[language] == name]
        
        if not ship:
            raise exceptions.UnknownShipException("the language and name provided does not match any ships")
        
        return ship[0]


if __name__ == "__main__":
    azurapi = AzurAPI()
    print(azurapi.get_version())
