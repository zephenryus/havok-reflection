from .hkReferencedObject import hkReferencedObject
from .hkaiEdgeFollowingBehavior import hkaiEdgeFollowingBehavior
import struct
from .common import vector4


class hkaiBehaviorBlockedDetector(hkReferencedObject):
    behavior: hkaiEdgeFollowingBehavior
    prevRuntimeID: int
    prevPos: vector4
    avgProgress: float
    smoothingFactor: float
    blockedThreshold: float
    sqrTeleportationThreshold: float
    blocked: bool

    def __init__(self, infile):
        self.behavior = hkaiEdgeFollowingBehavior(infile)  # TYPE_POINTER
        self.prevRuntimeID = struct.unpack('>i', infile.read(4))
        self.prevPos = struct.unpack('>4f', infile.read(16))
        self.avgProgress = struct.unpack('>f', infile.read(4))
        self.smoothingFactor = struct.unpack('>f', infile.read(4))
        self.blockedThreshold = struct.unpack('>f', infile.read(4))
        self.sqrTeleportationThreshold = struct.unpack('>f', infile.read(4))
        self.blocked = struct.unpack('>?', infile.read(1))
