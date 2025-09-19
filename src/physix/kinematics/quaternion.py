from mathx.vec.vec import Vec
import numpy as np

class Quaternion(Vec):
    __slots__ = ("_qw", "_qx", "_qy", "_qz")
    def __init__(self, qw:float, qx:float, qy:float, qz:float):
        self._qw = qw
        self._qx = qx
        self._qy = qy
        self._qz = qz
        super().__init__(Vec((self._qw,self._qx,self._qy,self._qz)))

    def normalize(self):
        pass

    def conjugate(self):
        pass

    def multiply(self, other:"Quaternion"):
        pass

    def from_axis_angle(self, axis:float, theta:float):
        pass