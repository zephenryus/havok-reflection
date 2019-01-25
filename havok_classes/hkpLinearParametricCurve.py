from .hkpParametricCurve import hkpParametricCurve
import struct
from typing import List
from .common import get_array


class hkpLinearParametricCurve(hkpParametricCurve):
    smoothingFactor: float
    closedLoop: bool
    dirNotParallelToTangentAlongWholePath: vector4
    points: List[vector4]
    distance: List[float]

    def __init__(self, infile):
        self.smoothingFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.closedLoop = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.dirNotParallelToTangentAlongWholePath = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.points = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.distance = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} smoothingFactor={smoothingFactor}, closedLoop={closedLoop}, dirNotParallelToTangentAlongWholePath={dirNotParallelToTangentAlongWholePath}, points=[{points}], distance=[{distance}]>".format(**{
            "class_name": self.__class__.__name__,
            "smoothingFactor": self.smoothingFactor,
            "closedLoop": self.closedLoop,
            "dirNotParallelToTangentAlongWholePath": self.dirNotParallelToTangentAlongWholePath,
            "points": self.points,
            "distance": self.distance,
        })
