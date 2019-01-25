from .hkpBinaryAction import hkpBinaryAction
from .common import vector4
import struct


class hkpSpringAction(hkpBinaryAction):
    lastForce: vector4
    positionAinA: vector4
    positionBinB: vector4
    restLength: float
    strength: float
    damping: float
    onCompression: bool
    onExtension: bool

    def __init__(self, infile):
        self.lastForce = struct.unpack('>4f', infile.read(16))
        self.positionAinA = struct.unpack('>4f', infile.read(16))
        self.positionBinB = struct.unpack('>4f', infile.read(16))
        self.restLength = struct.unpack('>f', infile.read(4))
        self.strength = struct.unpack('>f', infile.read(4))
        self.damping = struct.unpack('>f', infile.read(4))
        self.onCompression = struct.unpack('>?', infile.read(1))
        self.onExtension = struct.unpack('>?', infile.read(1))
