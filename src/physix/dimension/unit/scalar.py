from physix.dimension.unit.unit import Unit

class Scalar:
    def __init__(self, val: float, unit:Unit):
        self._unit = unit
        self._val = val

    def get_val(self)->float:
        return self._val

    def get_unit(self)->Unit:
        return self._unit



