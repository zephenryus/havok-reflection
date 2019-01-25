from .hkpVehicleDriverInputStatus import hkpVehicleDriverInputStatus
import struct


class hkpVehicleDriverInputAnalogStatus(hkpVehicleDriverInputStatus):
    positionX: float
    positionY: float
    handbrakeButtonPressed: bool
    reverseButtonPressed: bool

    def __init__(self, infile):
        self.positionX = struct.unpack('>f', infile.read(4))
        self.positionY = struct.unpack('>f', infile.read(4))
        self.handbrakeButtonPressed = struct.unpack('>?', infile.read(1))
        self.reverseButtonPressed = struct.unpack('>?', infile.read(1))
