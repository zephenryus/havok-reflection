from .hkReferencedObject import hkReferencedObject
from .hkaiEdgeFollowingBehavior import hkaiEdgeFollowingBehavior
import struct


class hkaiBehaviorBlockedDetector(hkReferencedObject):
    behavior: any
    prevRuntimeID: int
    prevPos: vector4
    avgProgress: float
    smoothingFactor: float
    blockedThreshold: float
    sqrTeleportationThreshold: float
    blocked: bool

    def __init__(self, infile):
        self.behavior = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.prevRuntimeID = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.prevPos = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.avgProgress = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.smoothingFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.blockedThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sqrTeleportationThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.blocked = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} behavior={behavior}, prevRuntimeID={prevRuntimeID}, prevPos={prevPos}, avgProgress={avgProgress}, smoothingFactor={smoothingFactor}, blockedThreshold={blockedThreshold}, sqrTeleportationThreshold={sqrTeleportationThreshold}, blocked={blocked}>".format(**{
            "class_name": self.__class__.__name__,
            "behavior": self.behavior,
            "prevRuntimeID": self.prevRuntimeID,
            "prevPos": self.prevPos,
            "avgProgress": self.avgProgress,
            "smoothingFactor": self.smoothingFactor,
            "blockedThreshold": self.blockedThreshold,
            "sqrTeleportationThreshold": self.sqrTeleportationThreshold,
            "blocked": self.blocked,
        })
