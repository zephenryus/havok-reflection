import struct
from .common import any


class hkpCollidableBoundingVolumeData(object):
    min: int
    expansionMin: int
    expansionShift: int
    max: int
    expansionMax: int
    padding: int
    numChildShapeAabbs: int
    capacityChildShapeAabbs: int
    childShapeAabbs: any
    childShapeKeys: any

    def __init__(self, infile):
        self.min = struct.unpack('>I', infile.read(4))
        self.expansionMin = struct.unpack('>B', infile.read(1))
        self.expansionShift = struct.unpack('>B', infile.read(1))
        self.max = struct.unpack('>I', infile.read(4))
        self.expansionMax = struct.unpack('>B', infile.read(1))
        self.padding = struct.unpack('>B', infile.read(1))
        self.numChildShapeAabbs = struct.unpack('>H', infile.read(2))
        self.capacityChildShapeAabbs = struct.unpack('>H', infile.read(2))
        self.childShapeAabbs = any(infile)  # TYPE_POINTER
        self.childShapeKeys = any(infile)  # TYPE_POINTER
