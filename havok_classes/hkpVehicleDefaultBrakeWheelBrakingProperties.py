import struct


class hkpVehicleDefaultBrakeWheelBrakingProperties(object):
    maxBreakingTorque: float
    minPedalInputToBlock: float
    isConnectedToHandbrake: bool

    def __init__(self, infile):
        self.maxBreakingTorque = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minPedalInputToBlock = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.isConnectedToHandbrake = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxBreakingTorque={maxBreakingTorque}, minPedalInputToBlock={minPedalInputToBlock}, isConnectedToHandbrake={isConnectedToHandbrake}>".format(**{
            "class_name": self.__class__.__name__,
            "maxBreakingTorque": self.maxBreakingTorque,
            "minPedalInputToBlock": self.minPedalInputToBlock,
            "isConnectedToHandbrake": self.isConnectedToHandbrake,
        })
