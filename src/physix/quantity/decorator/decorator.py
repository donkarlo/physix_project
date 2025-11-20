from physix.quantity.quantifiable import Quantifiable
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator

class Decorator(BaseDecorator, Quantifiable):
    def __init__(self, inner: Quantifiable):
        BaseDecorator.__init__(self, inner)