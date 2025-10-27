from physix.quantity.scalar_quantifiable import ScalarQuantity
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator
from physix.quantity.scalar_quantifiable import TensorQuantifiable


class Decorator(Decorator, TensorQuantifiable):
    def __init__(self, inner: TensorQuantifiable):
        super(Decorator).__init__(inner)