from .common import vector4
import struct


class hkpBallSocketChainDataConstraintInfo(object):
    pivotInA: vector4
    pivotInB: vector4
    flags: int

    def __init__(self, infile):
        self.pivotInA = struct.unpack('>4f', infile.read(16))
        self.pivotInB = struct.unpack('>4f', infile.read(16))
        self.flags = struct.unpack('>I', infile.read(4))
