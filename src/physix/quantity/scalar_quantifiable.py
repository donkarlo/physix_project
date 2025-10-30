from mathx.linalg.tensor.tensor_representable import TensorRepresentable
from mathx.linalg.tensor.vector.vector import Vector
from physix.quantity.quantifiable import Quantifiable
from typing import runtime_checkable, Protocol


@runtime_checkable
class ScalarQuantifiable(Quantifiable, Protocol):
    pass