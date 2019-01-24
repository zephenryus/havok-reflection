from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiGatePathPathGate import hkaiGatePathPathGate
from .common import vector4
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
