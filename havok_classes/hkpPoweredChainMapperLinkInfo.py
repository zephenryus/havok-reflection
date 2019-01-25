import struct
from .hkpConstraintInstance import hkpConstraintInstance


class hkpPoweredChainMapperLinkInfo(object):
    firstTargetIdx: int
    numTargets: int
    limitConstraint: hkpConstraintInstance

    def __init__(self, infile):
        self.firstTargetIdx = struct.unpack('>i', infile.read(4))
        self.numTargets = struct.unpack('>i', infile.read(4))
        self.limitConstraint = hkpConstraintInstance(infile)  # TYPE_POINTER
