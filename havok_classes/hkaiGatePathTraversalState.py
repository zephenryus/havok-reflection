from .common import vector4
import struct


class hkaiGatePathTraversalState(object):
    curPos: vector4
    curCellIdx: int

    def __init__(self, infile):
        self.curPos = struct.unpack('>4f', infile.read(16))
        self.curCellIdx = struct.unpack('>i', infile.read(4))
