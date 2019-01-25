from .hkReferencedObject import hkReferencedObject
from .common import any
import struct


class hkcdPlanarGeometryPrimitivesCollection28(hkReferencedObject):
    storage: any
    primaryBitmap: int
    secondaryBitmaps: int
    freeBlocks: int

    def __init__(self, infile):
        self.storage = any(infile)  # TYPE_ARRAY
        self.primaryBitmap = struct.unpack('>I', infile.read(4))
        self.secondaryBitmaps = struct.unpack('>I', infile.read(4))
        self.freeBlocks = struct.unpack('>I', infile.read(4))
