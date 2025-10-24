from physix.quantity.quantity import Quantity
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator
from physix.quantity.quantity import Quantifiable


class Decorator(Decorator, Quantifiable):
    def __init__(self, inner: Quantifiable):
        self._inner = inner