from core.types.helpers.stats import StatLevels
from typing import Union, Tuple
from ..types.helpers import StatsType


class LevelStats:

    def __init__(self, type: StatsType) -> None:
        self.__type: StatsType = type

    def all_info(self) -> StatsType:
        return self.__type

    def armor(self) -> str:
        return self.all_info().get('armor')

    def reload(self) -> str:
        return self.all_info().get('reload')

    def luck(self) -> str:
        return self.all_info().get('luck')

    def firepower(self) -> str:
        return self.all_info().get('firepower')

    def torpedo(self) -> str:
        return self.all_info().get('torpedo')

    def evasion(self) -> str:
        return self.all_info().get('evasion')

    def speed(self) -> str:
        return self.all_info().get('speed')

    def antiair(self) -> str:
        return self.all_info().get('antiair')

    def aviation(self) -> str:
        return self.all_info().get('aviation')

    def oil_consumption(self) -> str:
        return self.all_info().get('oilConsumption')

    def accuracy(self) -> str:
        return self.all_info().get('accuracy')

    def anti_submarine_warfare(self) -> str:
        return self.all_info().get('anti_submarine_warfare')

    def oxygen(self) -> Union[str, None]:
        '''
        Only returns a value if the ship hull type is submarine
        '''
        return self.all_info().get('oxygen')

    def ammunition(self) -> Union[str, None]:
        '''
        Only returns a value if the ship hull type is submarine
        '''
        return self.all_info().get('ammunition')

    def hunting_range(self) -> Union[Tuple[Tuple[str]], None]:
        '''
        Only returns a value if the ship hull type is submarine
        '''
        return self.all_info().get('huntingRange')


class Stats:

    def __init__(self, stats: StatLevels) -> None:
        self.__stats: StatLevels = stats

    def all_info(self) -> StatLevels:
        return self.__stats

    def base_stats(self) -> LevelStats:
        return LevelStats(self.all_info().get('baseStats'))

    def level_100(self) -> LevelStats:
        return LevelStats(self.all_info().get('level100'))

    def level_120(self) -> LevelStats:
        return LevelStats(self.all_info().get('level120'))

    def level_100_retrofit(self) -> LevelStats:
        '''
        Only returns a value if the ship can be retrofit
        '''
        return LevelStats(self.all_info().get('level100Retrofit'))

    def level_120_retrofit(self) -> LevelStats:
        '''
        Only returns a value if the ship can be retrofit
        '''
        return LevelStats(self.all_info().get('level120Retrofit'))
