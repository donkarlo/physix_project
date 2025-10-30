from mathx.linalg.tensor.tensor_representable import TensorRepresentable
from typing import Protocol, runtime_checkable


@runtime_checkable
class Quantifiable(Protocol):
    pass