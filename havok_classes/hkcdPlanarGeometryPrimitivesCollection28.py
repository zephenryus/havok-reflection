from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
import struct


class hkcdPlanarGeometryPrimitivesCollection28(hkReferencedObject):
    storage: List[int]
    primaryBitmap: int
    secondaryBitmaps: int
    freeBlocks: int

    def __init__(self, infile):
        self.storage = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.primaryBitmap = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.secondaryBitmaps = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.freeBlocks = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} storage=[{storage}], primaryBitmap={primaryBitmap}, secondaryBitmaps={secondaryBitmaps}, freeBlocks={freeBlocks}>".format(**{
            "class_name": self.__class__.__name__,
            "storage": self.storage,
            "primaryBitmap": self.primaryBitmap,
            "secondaryBitmaps": self.secondaryBitmaps,
            "freeBlocks": self.freeBlocks,
        })
