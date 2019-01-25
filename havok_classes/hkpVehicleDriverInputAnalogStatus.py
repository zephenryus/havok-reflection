from .hkpVehicleDriverInputStatus import hkpVehicleDriverInputStatus
import struct


class hkpVehicleDriverInputAnalogStatus(hkpVehicleDriverInputStatus):
    positionX: float
    positionY: float
    handbrakeButtonPressed: bool
    reverseButtonPressed: bool

    def __init__(self, infile):
        self.positionX = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.positionY = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.handbrakeButtonPressed = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.reverseButtonPressed = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} positionX={positionX}, positionY={positionY}, handbrakeButtonPressed={handbrakeButtonPressed}, reverseButtonPressed={reverseButtonPressed}>".format(**{
            "class_name": self.__class__.__name__,
            "positionX": self.positionX,
            "positionY": self.positionY,
            "handbrakeButtonPressed": self.handbrakeButtonPressed,
            "reverseButtonPressed": self.reverseButtonPressed,
        })
