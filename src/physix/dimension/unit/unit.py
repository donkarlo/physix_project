from mathx.physics.dimension.type.type import Type as DimensionType
from mathx.physics.dimension.unit import Type as UnitType

class Unit:
    def __init__(self, unit_type:UnitType):
        self._unit_type = unit_type

    def __eq__(self, other):
        if self._type_id == other._type_id:
            return True
        return False