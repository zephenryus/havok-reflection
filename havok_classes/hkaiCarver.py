from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiVolume import hkaiVolume
from .common import any


class FlagBits(Enum):
    CARVER_ERODE_EDGES = 1


class hkaiCarver(hkReferencedObject):
    volume: hkaiVolume
    flags: any
