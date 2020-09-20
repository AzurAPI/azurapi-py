from typing import TypedDict, Union, List


class _Stats(TypedDict):
    '''
    Interface for ship stats
    '''
    armor: str
    reload: str
    luck: str
    firepower: str
    torpedo: str
    evasion: str
    speed: str
    antiair: str
    aviation: str
    oil_consumption: str
    accuracy: str
    anti_submarine_warfare: str

    # These will only return values for submarines
    oxygen: Union[str, None]
    ammunition: Union[str, None]
    hunting_range: Union[List[List[str]], None]


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

        self.__stars: TypedDict('Stars', {
            'stars': str,  # e.g. ★★☆☆☆
            'value': int   # e.g. 2
        }) = ship_data.get('stars')

        self.__stats: _Stats = ship_data.get('stats')

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

        self.__skills: List[_Skill] = ship_data.get('skills')
        self.__limit_breaks: List[List[str]] = ship_data.get('limitBreaks')

        self.__fleet_tech: TypedDict('FleetTech', {
            'stats_bonus': TypedDict('StatsBonus', {
                'collection': TypedDict('Collection', {
                    'applicable': List[str],
                    'stat': str,
                    'bonus': str
                }),
                'max_level': TypedDict('MaxLevel', {
                    'applicable': List[str],
                    'stat': str,
                    'bonus': str
                })
            }),
            'tech_points': TypedDict('TechPoints', {
                'collection': int,
                'maxLimitBreak': int,
                'maxLevel': int,
                'total': int
            })
        }) = ship_data.get('fleetTech')

        self.__construction: TypedDict('Construction', {
            'construction_time': str,
            'available_in': TypedDict('AvailableIn', {
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

    def id(self) -> str:
        return self.__id

    def all_name_langs(self) -> List[str]:
        '''
        Returns a list of all languages that is available for the ship.
        If the name of that language is None, the language will not be in the list.
        '''
        return [name for name in self.__names if name is not None]

    def all_names(self) -> List[str]:
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
