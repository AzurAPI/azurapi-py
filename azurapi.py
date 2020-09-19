import os
import json
from pathlib import Path
from typing import Dict, Union, Optional
from core.types import IVersionTypes
from core.updater import Updater
from core.entities.ship import AzurShip
from core.exceptions import UnknownShipException
from core.store import LIST_NAMES


class AzurApi:

    def __init__(self, directory: Optional[Union[str, Path]] = os.getcwd(), update_on_init: Optional[bool] = True) -> None:

        self.data_folder = f'{directory}{os.sep}azurapi_data'
        self.updater = Updater(self.data_folder)

        if update_on_init:
            self.updater.update()

        self.data_files = [
            f'{self.data_folder}{os.sep}{name}' for name in LIST_NAMES
        ]

    def __get_file_data(self, file: Union[str, Path]) -> dict:
        if not self.updater.check_files():
            self.updater.update()

        with open(file, 'r', encoding='utf-8') as data:
            return json.load(data)

    def get_version(self) -> Dict[str, int]:
        version_file = IVersionTypes(self.__get_file_data(self.data_files[2]))
        versions = {
            'ships': version_file['ships']['version-number'],
            'equipments': version_file['equipments']['version-number']
        }
        return versions

    def get_ship_by_name(self, name: str) -> AzurShip:
        ships = self.__get_file_data(self.data_files[0])

        for ship in ships:
            if name.lower() in [_name.lower() for _name in ship['names'].values() if _name is not None]:
                return AzurShip(ship)
        else:
            raise UnknownShipException(
                'the name provided does not match any ships'
            )

    def get_ship_by_id(self, id: str) -> AzurShip:
        ships = self.__get_file_data(self.data_files[0])
        ship = next((ship for ship in ships if ship['id'] == id), None)

        if ship is None:
            raise UnknownShipException(
                'the id provided does not match any ships'
            )

        return AzurShip(ship)

    def get_ship(self, ship: str) -> AzurShip:
        try:
            return self.get_ship_by_name(ship)
        except UnknownShipException:
            try:
                return self.get_ship_by_id(ship)
            except UnknownShipException:
                raise UnknownShipException(
                    'the argument provided does not match any ships'
                )


if __name__ == "__main__":
    api = AzurApi()
    print(api.get_version())
