from .hkpVehicleDriverInput import hkpVehicleDriverInput
import struct


class hkpVehicleDefaultAnalogDriverInput(hkpVehicleDriverInput):
    slopeChangePointX: float
    initialSlope: float
    deadZone: float
    autoReverse: bool

    def __init__(self, infile):
        self.slopeChangePointX = struct.unpack('>f', infile.read(4))
        self.initialSlope = struct.unpack('>f', infile.read(4))
        self.deadZone = struct.unpack('>f', infile.read(4))
        self.autoReverse = struct.unpack('>?', infile.read(1))
