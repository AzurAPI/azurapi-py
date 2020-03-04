from ..azurapi import AzurAPI
azur = AzurAPI()

try:
    # print(azur.get_chapter(chapter='1-1'))
    print(azur.get_chapter(chapter='1-1', diff='hard'))
except ValueError as e:
    print(f"{type(e).__name__}: {e}")