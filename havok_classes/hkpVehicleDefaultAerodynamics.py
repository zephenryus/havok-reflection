from .hkpVehicleAerodynamics import hkpVehicleAerodynamics
import struct
from .common import vector4


class hkpVehicleDefaultAerodynamics(hkpVehicleAerodynamics):
    airDensity: float
    frontalArea: float
    dragCoefficient: float
    liftCoefficient: float
    extraGravityws: vector4

    def __init__(self, infile):
        self.airDensity = struct.unpack('>f', infile.read(4))
        self.frontalArea = struct.unpack('>f', infile.read(4))
        self.dragCoefficient = struct.unpack('>f', infile.read(4))
        self.liftCoefficient = struct.unpack('>f', infile.read(4))
        self.extraGravityws = struct.unpack('>4f', infile.read(16))
