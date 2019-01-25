from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkaiGatePathPathGate import hkaiGatePathPathGate
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
    gates: List[hkaiGatePathPathGate]
    startPoint: vector4
    schedule: hkaiGatePathUtilExponentialSchedule
    needsInitialSmooth: bool

    def __init__(self, infile):
        self.gates = get_array(infile, hkaiGatePathPathGate, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.startPoint = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.schedule = hkaiGatePathUtilExponentialSchedule(infile)  # TYPE_STRUCT:TYPE_VOID
        self.needsInitialSmooth = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} gates=[{gates}], startPoint={startPoint}, schedule={schedule}, needsInitialSmooth={needsInitialSmooth}>".format(**{
            "class_name": self.__class__.__name__,
            "gates": self.gates,
            "startPoint": self.startPoint,
            "schedule": self.schedule,
            "needsInitialSmooth": self.needsInitialSmooth,
        })
