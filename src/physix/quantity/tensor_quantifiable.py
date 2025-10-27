from mathx.linalg.tensor.tensor_representable import TensorRepresentable
from typing import Protocol

class TensorQuantifiable(Protocol, TensorRepresentable):
    """
    So that you can decorate it with time or unit
    """
    ...