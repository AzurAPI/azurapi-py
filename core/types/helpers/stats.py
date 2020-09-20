from typing import TypedDict, Union, Tuple


class StatsType(TypedDict):
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
    oilConsumption: str
    accuracy: str
    anti_submarine_warfare: str

    # These will only return values for submarines
    oxygen: Union[str, None]
    ammunition: Union[str, None]
    huntingRange: Union[Tuple[Tuple[str]], None]


class StatLevels(TypedDict):
    baseStats: StatsType
    level100: StatsType
    level120: StatsType
    level100Retrofit: Union[StatsType, None]
    level120Retrofit: Union[StatsType, None]
