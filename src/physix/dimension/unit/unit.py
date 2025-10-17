from typing import Union, Optional

from physix.dimension.dimension import Dimension


class Unit:
    def __init__(self, name:str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name
