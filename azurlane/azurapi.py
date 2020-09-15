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
        return self.__get_file_data(self.updater.ships_file)

    def getShipById(self, sid):
        
        ship_list = self.__get_file_data(self.updater.ships_file)

        if len(sid) < 3:
            sid = "0" + sid

        ship = next((ship for ship in ship_list if ship['id'] == sid), None)

        if ship is None:
            raise UnknownShipException("the id provided does not match any ships")

        return ship

    def getShipByName(self, ship):
        
        ship_list = self.__get_file_data(self.updater.ships_file)
        ship = next((s for s in ship_list if ship.lower() in [sh.lower() for sh in s['names'].values() if sh is not None]), None)

        if ship is None:
            raise UnknownShipException("the name provided does not match any ships")

        return ship

    def getShip(self, ship):

        # As per recommended by Python's EAFP rule, nested try/except is used
        # Tries to find by name first, then move to find by id if failed
        # If both failed, raise an error message
        try:
            return self.getShipByName(ship)
        except (ValueError, UnknownShipException):
            try:
                return self.getShipById(ship)
            except UnknownShipException:
                raise UnknownShipException("the input provided does not match any ships")
        
    def getAllShipsByLang(self, language):
        
        if language not in AVAILABLE_LANGS:
            raise UnknownLanguageException("the language provided is not supported")
        
        language = "code" if language == "official" else language
        
        ship_list = self.__get_file_data(self.updater.ships_file)
        return [ship for ship in ship_list if ship['names'][language] is not None]
    
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
        ship = next((ship for ship in ships_list if ship.get("names")[language].lower() == name.lower()), None)
        
        if ship is None:
            raise UnknownShipException("the language and name provided does not match any ships")

        return ship
        
    def getShipByEnglishName(self, ship):
        return self.getShipByLang("en", ship)
    
    def getShipByChineseName(self, ship):
        return self.getShipByLang("cn", ship)
    
    def getShipByJapaneseName(self, ship):
        return self.getShipByLang("jp", ship)
    
    def getShipByKoreanName(self, ship):
        return self.getShipByLang("kr", ship)
    
    def getShipByOfficialName(self, ship):
        return self.getShipByLang("code", ship)
    
    # Alternative names for the same method
    getShipByNameEn = getShipByEnglishName
    getShipByNameCn = getShipByChineseName
    getShipByNameJp = getShipByJapaneseName
    getShipByNameKr = getShipByKoreanName
    getShipByNameOfficial = getShipByOfficialName
    
    def getAllShipsFromFaction(self, faction):
                
        try:
            nation = to_lower_trimmed(get_faction_from_input(faction))
        except AttributeError:
            raise UnknownFactionException(f'Unknown faction/nationality: "{faction}"')
            
        return [ship for ship in self.getAllShips() if to_lower_trimmed(ship['nationality']) == nation]

    
    # Alternative names for the same method
    getAllShipsFromNation = getAllShipsFromFaction
    getAllShipsFromNationality = getAllShipsFromFaction

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
        
        try:
            if not self.chapter_list[chap][stage]:
                raise UnknownChapterException(f"Unknown chapter: {chap}-{stage}")
            elif diff is not None:
                if not self.chapter_list[chap][stage][diff]:
                    raise UnknownDifficultyException(f"Unknown difficulty: {chap}-{stage} ({diff})")
                else:
                    return self.chapter_list[chap][stage][diff]
            else:
                return self.chapter_list[chap][stage]
        except KeyError:
            raise UnknownDifficultyException(f"Unknown chapter: {chap}-{stage}")
                
    def getMemory(self, memory):
        
        memories = self.__get_file_data(self.updater.memories_files)
        for mem in memories.keys():
            if memory.lower() == mem.lower():
                return memories[mem]

        raise UnknownMemoryException(f'Unknown memory to view: "{memory}"')

    def getAllEquipments(self):
        return list(self.__get_file_data(self.updater.equipments_file).values())
    
    def getAllEquipmentsByLang(self, language):
        
        if language not in AVAILABLE_LANGS:
            raise UnknownLanguageException("the language provided is not supported")
        
        if language in ["official", "code"]:
            return self.getAllEquipments()
            
        equipment_list = self.__get_file_data(self.updater.equipments_file)

        found_equipments = []
    
        for equipment in equipment_list:
            
            equipment_names = equipment_list[equipment]["names"]
            
            if equipment_names[language] is None:
                continue
                
            found_equipments.append(equipment_list[equipment])
        
        return found_equipments
    
    def getEquipmentByLang(self, language, name):
        
        if language in ["official", "code"]: 
            equipment_list = self.__get_file_data(self.updater.equipments_file)
            
            for equipment in list(equipment_list.keys()):
                if name.lower() == equipment.lower(): return equipment_list[equipment]
            
            raise UnknownEquipmentException("the language and name provided does not match any equipments")
        
        equipment_list = self.getAllEquipmentsByLang(language)
        

        try:
            return [equipment for equipment in equipment_list if equipment.get("names")[language].lower() == name.lower()][0]
        except (StopIteration, TypeError, IndexError):
            raise UnknownEquipmentException("the language and name provided does not match any equipments")
        
    def getEquipmentByEnglishName(self, name):
        return self.getEquipmentByLang("en", name)
    
    def getEquipmentByChineseName(self, name):
        return self.getEquipmentByLang("cn", name)
    
    def getEquipmentByJapaneseName(self, name):
        return self.getEquipmentByLang("jp", name)
    
    def getEquipmentByKoreanName(self, name):
        return self.getEquipmentByLang("kr", name)
    
    def getEquipmentByOfficialName(self, name):
        return self.getEquipmentByLang("code", name)
    
    # Alternative names for the same method
    getEquipmentByNameEn = getEquipmentByEnglishName
    getEquipmentByNameCn = getEquipmentByChineseName
    getEquipmentByNameJp = getEquipmentByJapaneseName
    getEquipmentByNameKr = getEquipmentByKoreanName
    getEquipmentByNameOfficial = getEquipmentByOfficialName