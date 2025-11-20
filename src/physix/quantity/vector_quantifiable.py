from mathx.linalg.tensor.vector.vector_representable import VectorRepresentable
from physix.quantity.quantifiable import Quantifiable
from typing import Protocol, runtime_checkable


@runtime_checkable
class VectorQuantifiable(Quantifiable, VectorRepresentable, Protocol):
    """
    So that you can decorate it with time or unit
    """
    ...
