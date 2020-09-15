import os
from pathlib import Path
from typing import Union, Optional
from core.updater import Updater


class AzurApi:

    def __init__(self, directory: Optional[Union[str, Path]] = os.getcwd(), auto_update: Optional[bool] = True) -> None:
        updater = Updater(directory)
        pass


if __name__ == "__main__":
    AzurApi()
