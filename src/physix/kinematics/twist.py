from mathx.vec.vec import Vec

class Twist:
    def __init__(self, linear:Vec, angular:Vec):
        self._linear = linear
        self._angular = angular