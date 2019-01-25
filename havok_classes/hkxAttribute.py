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
    value: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.value = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", value={value}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "value": self.value,
        })
