from typing import Union, Optional

from physix.dimension.dimension import Dimension


class Unit:
    def __init__(self, name:str, dimension:Dimension):
        self.__name = name
        self._dimension = dimension

    def get_name(self) -> str:
        return self.__name

    def get_dimension(self) -> Dimension:
        return self._dimension
