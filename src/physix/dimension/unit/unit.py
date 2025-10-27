from typing import Union, Optional

from physix.dimension.dimension import Dimension


class Unit:
    def __init__(self, id:str):
        self.__id = id

    def get_id(self) -> str:
        return self.__id
