import os
import json
import requests

from .utils import *
from .updater import AzurApiUpdater

# Constants
MAIN_URL = "https://raw.githubusercontent.com/AzurAPI"
SHIP_LIST = f"{MAIN_URL}/azurapi-js-setup/master/ships.json"
CHAPTER_LIST = f"{MAIN_URL}/azurapi-js-setup/master/chapters.json"
EQUIPMENT_LIST = f"{MAIN_URL}/azurapi-js-setup/master/equipments.json"
VERSION_INFO = f"{MAIN_URL}/azurapi-js-setup/master/version-info.json"
MEMORIES_INFO = f"{MAIN_URL}/azurapi-js-setup/master/memories.json"
AVAILABLE_LANGS = ["en", "cn", "jp", "kr", "code", "official"]

class AzurAPI:

    def __init__(self, folder = os.getcwd()):
        self.ship_list = requests.get(SHIP_LIST).json()
        self.chapter_list = requests.get(CHAPTER_LIST).json()
        self.equipment_list = requests.get(EQUIPMENT_LIST).json()
        self.version_info = requests.get(VERSION_INFO).json()
        self.memories_info = requests.get(MEMORIES_INFO).json()
        
        self.updater = AzurApiUpdater(folder)
        self.updater.update()

    def __get_file_data(self, file):
        with open(file, "r", encoding="utf8") as data:
            return json.load(data)
        
    def getVersion(self):
        version_data = self.__get_file_data(self.updater.version_file)
        ships_version = version_data["ships"]["version-number"]
        equipments_version = version_data["equipments"]["version-number"]
        return f"Ships Version: {ships_version} | Equipments Version: {equipments_version}"

    # Not necessary since user can just access the property but this is just more user friendly
    def getAllShips(self):
        return list(self.__get_file_data(self.updater.ships_file).values())

    def getShipById(self, sid):
        
        ship_list = self.__get_file_data(self.updater.ships_file)

        # Makes sure it is an integer if a string was used as input and error for floats
        if isinstance(sid, str) and not is_str_int(sid):
            raise ValueError("a non integer input was given (string)")
        elif isinstance(sid, float):
            raise ValueError("a non integer input was given (float)")
        elif isinstance(sid, int):
            sid = str(sid)

        if len(sid) != 3:
            raise ValueError("id must be padded to 3 digits long e.g. 077")

        if sid not in ship_list:
            raise UnknownShipException("the id provided does not match any ships")

        return ship_list[sid]

    def getShipByName(self, name):
        
        ship_list = self.__get_file_data(self.updater.ships_file)

        # As of now, I cannot think of a better way to do this than nested loops
        for ship_id in ship_list:

            ship_names = ship_list[ship_id]["names"]
            for lang in ship_names:

                # I validated None just in case a name is missing somewhere
                if ship_names[lang] is None:
                    continue

                # Case insensitive check for the name of the ship
                if ship_names[lang].lower() == name.lower():
                    return ship_list[ship_id]

        raise UnknownShipException("the name provided does not match any ships")

    def getShip(self, ship):

        # As per recommended by Python's EAFP rule, nested try/except is used
        # Tries to find by id first, then move to find by name if failed
        # If both failed, raise an error message
        try:
            return self.getShipById(ship)
        except (ValueError, UnknownShipException):
            try:
                return self.getShipByName(ship)
            except UnknownShipException:
                raise UnknownShipException("the input provided does not match any ships")
        
    def getAllShipsByLang(self, language):
        
        if language not in AVAILABLE_LANGS:
            raise UnknownLanguageException("the language provided is not supported")
        
        language = "code" if language == "official" else language
        
        ship_list = self.__get_file_data(self.updater.ships_file)
        
        found_ships = []
    
        for ship_id in ship_list:
            
            ship_names = ship_list[ship_id]["names"]
            
            if ship_names[language] is None:
                continue
                
            found_ships.append(ship_list[ship_id])
        
        return found_ships
    
    def getAllShipsByEnglishName(self):
        return self.getAllShipsByLang("en")
    
    def getAllShipsByChineseName(self):
        return self.getAllShipsByLang("cn")
    
    def getAllShipsByJapaneseName(self):
        return self.getAllShipsByLang("jp")
    
    def getAllShipsByKoreanNames(self):
        return self.getAllShipsByLang("kr")
    
    def getAllShipsByOfficialName(self):
        return self.getAllShipsByLang("code")
    
    def getShipByLang(self, language, name):
        
        ships_list = self.getAllShipsByLang(language)

        try:
            return [ship for ship in ships_list if ship.get("names")[language].lower() == name.lower()][0]
        except (StopIteration, TypeError, IndexError):
            raise UnknownShipException("the language and name provided does not match any ships")
        
    def getShipByEnglishName(self, name):
        return self.getShipByLang("en", name)
    
    def getShipByChinesehName(self, name):
        return self.getShipByLang("cn", name)
    
    def getShipByJapaneseName(self, name):
        return self.getShipByLang("jp", name)
    
    def getShipByKoreanName(self, name):
        return self.getShipByLang("kr", name)
    
    def getShipByOfficialName(self, name):
        return self.getShipByLang("code", name)
    
    # Alternative names for the same method
    getShipByNameEn = getShipByEnglishName
    getShipByNameCn = getShipByChinesehName
    getShipByNameJp = getShipByJapaneseName
    getShipByNameKr = getShipByKoreanName
    getShipByNameOfficial = getShipByOfficialName

    def getChapter(self, chapter, **kwargs):

        # Check if "-" is in the chapter argument
        if "-" not in chapter:
            raise ValueError("The chapter code must be padded as '1-1'")

        # Split the chapter
        [c, s] = chapter.split("-")

        # Python makes these an integer for some reason
        chap = str(c)
        stage = str(s)
        diff = kwargs.get("diff", None)

        if not self.chapter_list[chap][stage]:
            raise UnknownChapterException(f"Unknown chapter: {chap}-{stage}")
        elif diff is not None:
            if not self.chapter_list[chap][stage][diff]:
                raise UnknownDifficultyException(f"Unknown difficulty: {chap}-{stage} ({diff})")
            else:
                return self.chapter_list[chap][stage][diff]
        else:
            return self.chapter_list[chap][stage]
                
    def getMemory(self, memory):
        
        memories = self.__get_file_data(self.updater.memories_files)
        for mem in memories.keys():
            if memory.lower() == mem.lower():
                return memories[mem]

        raise UnknownMemoryException(f'Unknown memory to view: "{memory}"')

    def getAllShipsFromFaction(self, faction):
                
        try:
            nation = to_lower_trimmed(get_faction_from_input(faction))
        except AttributeError:
            raise UnknownFactionException(f'Unknown faction/nationality: "{faction}"')
            
        found_ships = []
        
        for ship in self.getAllShips():
            if to_lower_trimmed(ship["nationality"]) == nation:
                found_ships.append(ship)
        
        return found_ships
    
    # Alternative names for the same method
    getAllShipsFromNation = getAllShipsFromFaction
    getAllShipsFromNationality = getAllShipsFromFaction