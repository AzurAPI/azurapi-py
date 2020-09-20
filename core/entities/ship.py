from typing import TypedDict, Union, Tuple
from ..helpers import Stars, Stats
from ..types.helpers import StarsType, StatLevels


class _Slot(TypedDict):
    '''
    Interface for ship slots
    '''
    type: str
    minEfficiency: int  # in percentage
    maxEfficiency: int  # in percentage


class _Skill(TypedDict):
    '''
    Interface for ship skills
    '''
    icon: str  # url
    names: TypedDict('Names', {
        'en': Union[str, None],
        'cn': Union[str, None],
        'jp': Union[str, None],
        'kr': Union[str, None]
    })
    description: str
    color: str  # descriptive color name (not hex code)


class _Artist(TypedDict):
    name: str
    url: str


class AzurShip:
    '''
    Object that returns information about a ship fetched in the azurlane
    ships database with helper methods to help getting data easier.
    '''

    def __init__(self, ship_data: dict) -> None:
        self.__wiki_url: str = ship_data.get('wikiUrl')
        self.__id: str = ship_data.get('id')

        self.__names: TypedDict('ShipNames', {
            'code': str,
            'en': str,
            'cn': Union[str, None],
            'jp': Union[str, None],
            'kr': Union[str, None]
        }) = ship_data.get('names')

        self.__ship_class: str = ship_data.get('class')
        self.__nationality: str = ship_data.get('nationality')
        self.__hull_type: str = ship_data.get('hullType')
        self.__thumbnail: str = ship_data.get('thumbnail')
        self.__rarity: str = ship_data.get('rarity')
        self.__stars: StarsType = ship_data.get('stars')
        self.__stats: StatLevels = ship_data.get('stats')

        self.__slots: TypedDict('Slots', {
            '1': _Slot,
            '2': _Slot,
            '3': _Slot
        }) = ship_data.get('slots')

        # mapped by [key = 'stat type', value = 'enhance value']
        self.__enhance_value: object = ship_data.get('enhanceValue')

        self.__scrap_value: TypedDict('ScrapValue', {
            'coin': int,
            'oil': int,
            'medal': int
        }) = ship_data.get('scrapValue')

        self.__skills: Tuple[_Skill] = ship_data.get('skills')
        self.__limit_breaks: Tuple[Tuple[str]] = ship_data.get('limitBreaks')

        self.__fleet_tech: TypedDict('FleetTech', {
            'statsBonus': TypedDict('StatsTypeBonus', {
                'collection': TypedDict('Collection', {
                    'applicable': Tuple[str],
                    'stat': str,
                    'bonus': str
                }),
                'maxLevel': TypedDict('MaxLevel', {
                    'applicable': Tuple[str],
                    'stat': str,
                    'bonus': str
                })
            }),
            'techPoints': TypedDict('TechPoints', {
                'collection': int,
                'maxLimitBreak': int,
                'maxLevel': int,
                'total': int
            })
        }) = ship_data.get('fleetTech')

        self.__construction: TypedDict('Construction', {
            'constructionTime': str,
            'availableIn': TypedDict('AvailableIn', {
                'light': bool,
                'heavy': bool,
                'aviation': bool,
                'limited': bool,
                'exchange': bool
            })
        }) = ship_data.get('construction')

        self.__misc: TypedDict('Miscellaneous', {
            'artist': str,
            'web': Union[_Artist, None],
            'pixiv': Union[_Artist, None],
            'twitter': Union[_Artist, None],
            'voice': Union[_Artist, None]
        }) = ship_data.get('misc')

    def wiki_url(self) -> str:
        return self.__wiki_url

    def id(self) -> str:
        return self.__id

    def all_name_langs(self) -> Tuple[str]:
        '''
        Returns a list of all languages that is available for the ship.
        If the name of that language is None, the language will not be in the list.
        '''
        return [name for name in self.__names if name is not None]

    def all_names(self) -> Tuple[str]:
        '''
        Returns a list of all names available for the ship.
        If the name in a specific language is None, it will not be in the list.
        '''
        return [self.__names[name] for name in self.__names if name is not None]

    def code_name(self) -> str:
        return self.__names.get('code')

    def english_name(self) -> str:
        return self.__names.get('en')

    def chinese_name(self) -> Union[str, None]:
        return self.__names.get('ch')

    def japanese_name(self) -> Union[str, None]:
        return self.__names.get('jp')

    def korean_name(self) -> Union[str, None]:
        return self.__names.get('kr')

    def ship_class(self) -> str:
        return self.__ship_class

    def nationality(self) -> str:
        return self.__nationality

    def hull_type(self) -> str:
        return self.__hull_type

    def thumbnail(self) -> str:
        return self.__thumbnail

    def rarity(self) -> str:
        return self.__rarity

    def stars(self) -> Stars:
        return Stars(self.__stars)

    def stats(self) -> Stats:
        return Stats(self.__stats)
