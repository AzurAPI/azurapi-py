import os
import json
from pathlib import Path
from typing import Union, Optional
from core.updater import Updater
from core.entities.ship import AzurShip
from core.exceptions import UnknownShipException
from core.store import LIST_NAMES


class AzurApi:

    def __init__(self, directory: Optional[Union[str, Path]] = os.getcwd(), auto_update: Optional[bool] = True) -> None:

        self.data_folder = f'{directory}{os.sep}azurapi_data'
        self.updater = Updater(self.data_folder)

        if auto_update:
            self.updater.update()

        self.data_files = [
            f'{self.data_folder}{os.sep}{name}' for name in LIST_NAMES
        ]

    def __get_file_data(self, file: Union[str, Path]) -> dict:
        with open(file, 'r', encoding='utf-8') as data:
            return json.load(data)

    def get_ship_by_name(self, name: str) -> AzurShip:
        ships = self.__get_file_data(self.data_files[0])

        found_ship = None
        for ship in ships:
            if name.lower() in [name.lower() for name in ship['names'].values() if name is not None]:
                found_ship = ship
                break
        else:
            raise UnknownShipException(
                'the name provided does not match any ships'
            )

        return AzurShip(found_ship)

    def get_ship_by_id(self, id):

        ships = self.__get_file_data(self.data_files[0])
        ship = next((ship for ship in ships if ship['id'] == id), None)

        if ship is None:
            raise UnknownShipException(
                'the id provided does not match any ships'
            )

        return AzurShip(ship)


if __name__ == "__main__":
    AzurApi()
