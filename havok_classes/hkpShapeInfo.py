from .hkReferencedObject import hkReferencedObject
from .hkpShape import hkpShape
import struct
from .common import any


class hkpShapeInfo(hkReferencedObject):
    shape: hkpShape
    isHierarchicalCompound: bool
    hkdShapesCollected: bool
    childShapeNames: any
    childTransforms: any
    transform: any

    def __init__(self, infile):
        self.shape = hkpShape(infile)  # TYPE_POINTER
        self.isHierarchicalCompound = struct.unpack('>?', infile.read(1))
        self.hkdShapesCollected = struct.unpack('>?', infile.read(1))
        self.childShapeNames = any(infile)  # TYPE_ARRAY
        self.childTransforms = any(infile)  # TYPE_ARRAY
        self.transform = any(infile)  # TYPE_TRANSFORM
