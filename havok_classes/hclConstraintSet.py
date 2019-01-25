from .hkReferencedObject import hkReferencedObject
from enum import Enum


class MaxConstraintSetSize(Enum):
    MAX_CONSTRAINT_SET_SIZE = 128


class hclConstraintSet(hkReferencedObject):
    name: str
    type: enumerate

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.type = enumerate(infile)  # TYPE_ENUM
