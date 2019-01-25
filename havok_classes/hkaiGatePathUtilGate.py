from .common import vector4
import struct


class hkaiGatePathUtilGate(object):
    origin: vector4
    uLen: float
    vLen: float
    type: enumerate

    def __init__(self, infile):
        self.origin = struct.unpack('>4f', infile.read(16))
        self.uLen = struct.unpack('>f', infile.read(4))
        self.vLen = struct.unpack('>f', infile.read(4))
        self.type = enumerate(infile)  # TYPE_ENUM
