import os
import json
import requests
from typing import Union
from pathlib import Path
from core.exceptions import AzurApiException
from core.types import IVersionTypes, IUpdateTypes


# Constants
MAIN_URL = 'https://raw.githubusercontent.com/AzurAPI/azurapi-js-setup/master'

LIST_NAMES = [
    'ships.json',
    'equipments.json',
    'version-info.json',
    'chapters.json',
    'memories.internal.json'
]
LIST_URLS = [f'{MAIN_URL}/{name}' for name in LIST_NAMES]


class Updater:

    def __init__(self, directory: Union[str, Path]) -> None:
        self.data_folder = f'{directory}{os.sep}azurapi_data'

       # Create data folder if it does not exist
        if not os.path.exists(self.data_folder):
            os.mkdir(self.data_folder)

        self.update()

    def __download_data(self, url, file_name):
        with open(f'{self.data_folder}{os.sep}{file_name}', 'w', encoding='utf-8') as f:
            try:
                data = requests.get(url).json()
            except:
                raise AzurApiException(
                    'Invalid URL provided or data in URL is not JSON.'
                )
            else:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def check_files(self) -> bool:
        for index in range(len(LIST_NAMES)):
            if not os.path.exists(f'{self.data_folder}{os.sep}{LIST_NAMES[index]}'):
                return False
        return True

    def check_updates(self) -> IUpdateTypes:

        has_updates: IUpdateTypes = {
            'ships': False,
            'eqiupments': False,
            'versions': False
        }

        with open(f'{self.data_folder}{os.sep}{LIST_NAMES[2]}') as f:

            response = requests.get(LIST_URLS[2])
            remotev: IVersionTypes = response.json()
            localv: IVersionTypes = json.load(f)

            for index in range(len(remotev)):
                remote: int = remotev[list(remotev)[index]]['version-number']
                local: int = localv[list(localv)[index]]['version-number']

                if remote != local:
                    if not has_updates['versions']:
                        has_updates['versions'] = True
                    has_updates[list(has_updates)[index]] = True

        return has_updates

    def update(self) -> IUpdateTypes:

        updated: IUpdateTypes = {
            'ships': False,
            'eqiupments': False,
            'versions': False
        }

        if not self.check_files():
            for index in range(len(LIST_NAMES)):
                self.__download_data(LIST_URLS[index], LIST_NAMES[index])
            return updated

        has_updates = self.check_updates()

        for index, update in enumerate(has_updates):
            if has_updates[update]:
                updated[list(updated)[index]] = True
                self.__download_data(LIST_URLS[index], LIST_NAMES[index])

        return updated
