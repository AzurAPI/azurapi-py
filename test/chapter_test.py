import azurapi as api
azur = api.AzurAPI()

try:
    # print(azur.get_chapter(code='1-1'))
    print(azur.get_chapter_diff(code='1-1', diff='normal'))
except ValueError as e:
    print(f"{type(e).__name__}: {e}")