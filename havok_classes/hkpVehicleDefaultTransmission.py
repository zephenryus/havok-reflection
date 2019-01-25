from .hkpVehicleTransmission import hkpVehicleTransmission
import struct
from .common import any


class hkpVehicleDefaultTransmission(hkpVehicleTransmission):
    downshiftRPM: float
    upshiftRPM: float
    primaryTransmissionRatio: float
    clutchDelayTime: float
    reverseGearRatio: float
    gearsRatio: any
    wheelsTorqueRatio: any

    def __init__(self, infile):
        self.downshiftRPM = struct.unpack('>f', infile.read(4))
        self.upshiftRPM = struct.unpack('>f', infile.read(4))
        self.primaryTransmissionRatio = struct.unpack('>f', infile.read(4))
        self.clutchDelayTime = struct.unpack('>f', infile.read(4))
        self.reverseGearRatio = struct.unpack('>f', infile.read(4))
        self.gearsRatio = any(infile)  # TYPE_ARRAY
        self.wheelsTorqueRatio = any(infile)  # TYPE_ARRAY
