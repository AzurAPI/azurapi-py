from ..types.helpers import StarsType


class Stars:

    def __init__(self, stars: StarsType) -> None:
        self.__stars: StarsType = stars

    def all_info(self) -> StarsType:
        return self.__stars

    def graphical(self) -> str:
        return self.all_info().get('stars')

    def count(self) -> int:
        return self.all_info().get('value')
