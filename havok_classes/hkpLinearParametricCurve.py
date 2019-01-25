from .hkpParametricCurve import hkpParametricCurve
import struct
from .common import vector4, any


class hkpLinearParametricCurve(hkpParametricCurve):
    smoothingFactor: float
    closedLoop: bool
    dirNotParallelToTangentAlongWholePath: vector4
    points: any
    distance: any

    def __init__(self, infile):
        self.smoothingFactor = struct.unpack('>f', infile.read(4))
        self.closedLoop = struct.unpack('>?', infile.read(1))
        self.dirNotParallelToTangentAlongWholePath = struct.unpack('>4f', infile.read(16))
        self.points = any(infile)  # TYPE_ARRAY
        self.distance = any(infile)  # TYPE_ARRAY
