from .hkpBinaryAction import hkpBinaryAction
from .common import vector4
import struct


class hkpDashpotAction(hkpBinaryAction):
    point: vector4
    strength: float
    damping: float
    impulse: vector4

    def __init__(self, infile):
        self.point = struct.unpack('>4f', infile.read(16))
        self.strength = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
        self.impulse = struct.unpack('>4f', infile.read(16))
