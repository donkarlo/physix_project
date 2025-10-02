from typing import List, Optional

from physix.dimension.unit.unit import Unit
from mathx.linalg.vec.vec import Vec

class Vecs:
    def __init__(self, unit:Unit, vecs:Optional[List[Vec]]=None):
        self._unit = unit
        if vecs is None:
            vecs = []
        self._vecs = vecs

    def add_vec(self, val:Vec)->None:
        self._vecs.append(val)