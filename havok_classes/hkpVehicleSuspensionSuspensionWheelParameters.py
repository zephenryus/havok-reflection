import struct


class hkpVehicleSuspensionSuspensionWheelParameters(object):
    hardpointChassisSpace: vector4
    directionChassisSpace: vector4
    length: float

    def __init__(self, infile):
        self.hardpointChassisSpace = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.directionChassisSpace = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.length = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} hardpointChassisSpace={hardpointChassisSpace}, directionChassisSpace={directionChassisSpace}, length={length}>".format(**{
            "class_name": self.__class__.__name__,
            "hardpointChassisSpace": self.hardpointChassisSpace,
            "directionChassisSpace": self.directionChassisSpace,
            "length": self.length,
        })
