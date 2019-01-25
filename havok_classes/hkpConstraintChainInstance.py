from .hkpConstraintInstance import hkpConstraintInstance
from .hkpEntity import hkpEntity
from .hkpConstraintChainInstanceAction import hkpConstraintChainInstanceAction
import struct


class hkpConstraintChainInstance(hkpConstraintInstance):
    chainedEntities: hkpEntity
    action: hkpConstraintChainInstanceAction
    chainConnectedness: int

    def __init__(self, infile):
        self.chainedEntities = hkpEntity(infile)  # TYPE_ARRAY
        self.action = hkpConstraintChainInstanceAction(infile)  # TYPE_POINTER
        self.chainConnectedness = struct.unpack('>L', infile.read(8))
