from .common import vector4
import struct


class hkpVehicleSuspensionSuspensionWheelParameters(object):
    hardpointChassisSpace: vector4
    directionChassisSpace: vector4
    length: float

    def __init__(self, infile):
        self.hardpointChassisSpace = struct.unpack('>4f', infile.read(16))
        self.directionChassisSpace = struct.unpack('>4f', infile.read(16))
        self.length = struct.unpack('>f', infile.read(4))
