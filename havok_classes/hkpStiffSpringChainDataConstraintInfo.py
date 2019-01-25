from .common import vector4
import struct


class hkpStiffSpringChainDataConstraintInfo(object):
    pivotInA: vector4
    pivotInB: vector4
    springLength: float

    def __init__(self, infile):
        self.pivotInA = struct.unpack('>4f', infile.read(16))
        self.pivotInB = struct.unpack('>4f', infile.read(16))
        self.springLength = struct.unpack('>f', infile.read(4))
