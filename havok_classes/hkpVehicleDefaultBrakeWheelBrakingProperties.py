import struct


class hkpVehicleDefaultBrakeWheelBrakingProperties(object):
    maxBreakingTorque: float
    minPedalInputToBlock: float
    isConnectedToHandbrake: bool

    def __init__(self, infile):
        self.maxBreakingTorque = struct.unpack('>f', infile.read(4))
        self.minPedalInputToBlock = struct.unpack('>f', infile.read(4))
        self.isConnectedToHandbrake = struct.unpack('>?', infile.read(1))
