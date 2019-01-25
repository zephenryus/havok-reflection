from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiGatePathPathGate import hkaiGatePathPathGate
from .common import vector4
import struct
from .hkaiGatePathUtilExponentialSchedule import hkaiGatePathUtilExponentialSchedule


class UpdateTraversalStateResult(Enum):
    UTSR_NORMAL = 0
    UTSR_LOST = 1


class BoundarySegmentBits(Enum):
    BOUNDARYSEGMENT_MINV = 1
    BOUNDARYSEGMENT_MAXU = 2
    BOUNDARYSEGMENT_MAXV = 4
    BOUNDARYSEGMENT_MINU = 8
    BOUNDARYSEGMENT_ALL = 15


class hkaiGatePath(hkReferencedObject):
    gates: hkaiGatePathPathGate
    startPoint: vector4
    schedule: hkaiGatePathUtilExponentialSchedule
    needsInitialSmooth: bool

    def __init__(self, infile):
        self.gates = hkaiGatePathPathGate(infile)  # TYPE_ARRAY
        self.startPoint = struct.unpack('>4f', infile.read(16))
        self.schedule = hkaiGatePathUtilExponentialSchedule(infile)  # TYPE_STRUCT
        self.needsInitialSmooth = struct.unpack('>?', infile.read(1))
