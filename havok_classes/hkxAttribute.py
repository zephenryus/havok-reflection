from enum import Enum
from .hkReferencedObject import hkReferencedObject


class Hint(Enum):
    HINT_NONE = 0
    HINT_IGNORE = 1
    HINT_TRANSFORM = 2
    HINT_SCALE = 4
    HINT_TRANSFORM_AND_SCALE = 6
    HINT_FLIP = 8


class hkxAttribute(object):
    name: str
    value: hkReferencedObject

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.value = hkReferencedObject(infile)  # TYPE_POINTER
