from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiVolume import hkaiVolume


class FlagBits(Enum):
    CARVER_ERODE_EDGES = 1


class hkaiCarver(hkReferencedObject):
    volume: any
    flags: any

    def __init__(self, infile):
        self.volume = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} volume={volume}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "volume": self.volume,
            "flags": self.flags,
        })
