import struct
from .hkpConstraintInstance import hkpConstraintInstance


class hkpPoweredChainMapperLinkInfo(object):
    firstTargetIdx: int
    numTargets: int
    limitConstraint: any

    def __init__(self, infile):
        self.firstTargetIdx = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numTargets = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.limitConstraint = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} firstTargetIdx={firstTargetIdx}, numTargets={numTargets}, limitConstraint={limitConstraint}>".format(**{
            "class_name": self.__class__.__name__,
            "firstTargetIdx": self.firstTargetIdx,
            "numTargets": self.numTargets,
            "limitConstraint": self.limitConstraint,
        })
