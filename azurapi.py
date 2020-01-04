import json
import requests

from utils import UnknownShipException, is_str_int


# Constants
MAIN_URL = "https://raw.githubusercontent.com/AzurAPI"
SHIP_LIST = f"{MAIN_URL}/azurapi-js-setup/master/ships.json"
CHAPTER_LIST = f"{MAIN_URL}/azurapi-js-setup/master/chapters.json"
EQUIPMENT_LIST = f"{MAIN_URL}/azurapi-js-setup/master/equipments.json"
VERSION_INFO = f"{MAIN_URL}/azurapi-js-setup/master/version-info.json"


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

    # Not necessary since user can just access the property but just this is just more user friendly
    def get_all_ships(self):
        return self.ship_list

    def get_ship_by_id(self, ship_id):

        # Makes sure it is an integer if a string was used as input and error for floats
        if isinstance(ship_id, str) and not is_str_int(ship_id):
            raise ValueError("a non integer input was given (string)")
        elif isinstance(ship_id, float):
            raise ValueError("a non integer input was given (float)")
        elif isinstance(ship_id, int):
            ship_id = str(ship_id)

        if len(ship_id) != 3:
            raise ValueError("id must be padded to 3 digits long e.g. 077")

        if not ship_id in self.ship_list:
            raise UnknownShipException("the id provided does not match any ships")

        return self.ship_list[ship_id]

    def get_ship_by_name(self, ship_name):
        
        # As of now, I cannot think of a better way to do this than nested loops
        for ship_id in self.ship_list:

            ship_names = self.ship_list[ship_id]["names"]
            for lang in ship_names:

                # I validated None just in case a name is missing somewhere
                if ship_names[lang] is None:
                    continue

                # Case insensitive check for the name of the ship
                if ship_names[lang].lower() == ship_name.lower():
                    return self.ship_list[ship_id]

        raise UnknownShipException("the name provided does not match any ships")

    def get_ship(self, ship):

        # As per recommended by Python's EAFP rule, nested try/except is used
        # Tries to find by id first, then move to find by name if failed
        # If both failed, raise an error message
        try:
            return self.get_ship_by_id(ship)
        except (ValueError, UnknownShipException):
            try:
                return self.get_ship_by_name(ship)
            except UnknownShipException:
                raise UnknownShipException("the input provided does not match any ships")


if __name__ == "__main__":
    azurapi = AzurAPI()
    print(azurapi.get_version())
