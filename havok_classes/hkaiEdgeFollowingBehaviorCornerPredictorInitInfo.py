from .common import vector4
import struct


class hkaiEdgeFollowingBehaviorCornerPredictorInitInfo(object):
    positionLocal: vector4
    forwardVectorLocal: vector4
    upLocal: vector4
    positionSectionIndex: int
    nextEdgeIndex: int
    nextIsLeft: bool
    hasInfo: bool

    def __init__(self, infile):
        self.positionLocal = struct.unpack('>4f', infile.read(16))
        self.forwardVectorLocal = struct.unpack('>4f', infile.read(16))
        self.upLocal = struct.unpack('>4f', infile.read(16))
        self.positionSectionIndex = struct.unpack('>i', infile.read(4))
        self.nextEdgeIndex = struct.unpack('>i', infile.read(4))
        self.nextIsLeft = struct.unpack('>?', infile.read(1))
        self.hasInfo = struct.unpack('>?', infile.read(1))
