from .hkpVehicleDriverInput import hkpVehicleDriverInput
import struct


class hkpVehicleDefaultAnalogDriverInput(hkpVehicleDriverInput):
    slopeChangePointX: float
    initialSlope: float
    deadZone: float
    autoReverse: bool

    def __init__(self, infile):
        self.slopeChangePointX = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.initialSlope = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.deadZone = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.autoReverse = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} slopeChangePointX={slopeChangePointX}, initialSlope={initialSlope}, deadZone={deadZone}, autoReverse={autoReverse}>".format(**{
            "class_name": self.__class__.__name__,
            "slopeChangePointX": self.slopeChangePointX,
            "initialSlope": self.initialSlope,
            "deadZone": self.deadZone,
            "autoReverse": self.autoReverse,
        })
