from mathx.linalg.tensor.vec.vec_representable import VecRepresentable
from typing import Protocol


class VectorQuantifiable(Protocol, VecRepresentable):
    """
    So that you can decorate it with time or unit
    """
    ...