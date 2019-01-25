from .common import vector4, any
import struct
from .hkaiGatePathUtilGate import hkaiGatePathUtilGate


class hkaiGatePathPathGate(object):
    crossingPoint: vector4
    gate: hkaiGatePathUtilGate
    boundarySegments: any
    cellKey: int

    def __init__(self, infile):
        self.crossingPoint = struct.unpack('>4f', infile.read(16))
        self.gate = hkaiGatePathUtilGate(infile)  # TYPE_STRUCT
        self.boundarySegments = any(infile)  # TYPE_FLAGS
        self.cellKey = struct.unpack('>I', infile.read(4))
