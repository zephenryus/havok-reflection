from .hkpUnaryAction import hkpUnaryAction
from .common import vector4
import struct


class hkpReorientAction(hkpUnaryAction):
    rotationAxis: vector4
    upAxis: vector4
    strength: float
    damping: float

    def __init__(self, infile):
        self.rotationAxis = struct.unpack('>4f', infile.read(16))
        self.upAxis = struct.unpack('>4f', infile.read(16))
        self.strength = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
