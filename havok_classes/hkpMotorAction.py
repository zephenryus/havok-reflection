from .hkpUnaryAction import hkpUnaryAction
from .common import vector4
import struct


class hkpMotorAction(hkpUnaryAction):
    axis: vector4
    spinRate: float
    gain: float
    active: bool

    def __init__(self, infile):
        self.axis = struct.unpack('>4f', infile.read(16))
        self.spinRate = struct.unpack('>f', infile.read(4))
        self.gain = struct.unpack('>f', infile.read(4))
        self.active = struct.unpack('>?', infile.read(1))
