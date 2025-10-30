from physix.quantity.quantifiable import Quantifiable
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator


class Decorator(Decorator, Quantifiable):
    def __init__(self, inner: Quantifiable):
        super(Decorator, self).__init__(inner)