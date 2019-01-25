from .hkpBroadPhaseHandle import hkpBroadPhaseHandle
import struct


class hkpTypedBroadPhaseHandle(hkpBroadPhaseHandle):
    type: int
    ownerOffset: int
    objectQualityType: int
    collisionFilterInfo: int

    def __init__(self, infile):
        self.type = struct.unpack('>b', infile.read(1))
        self.ownerOffset = struct.unpack('>b', infile.read(1))
        self.objectQualityType = struct.unpack('>b', infile.read(1))
        self.collisionFilterInfo = struct.unpack('>I', infile.read(4))
