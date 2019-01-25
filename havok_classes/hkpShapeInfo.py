from .hkReferencedObject import hkReferencedObject
from .hkpShape import hkpShape
import struct
from typing import List
from .common import get_array


class hkpShapeInfo(hkReferencedObject):
    shape: any
    isHierarchicalCompound: bool
    hkdShapesCollected: bool
    childShapeNames: List[str]
    childTransforms: List[any]
    transform: any

    def __init__(self, infile):
        self.shape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.isHierarchicalCompound = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.hkdShapesCollected = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.childShapeNames = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR
        self.childTransforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_TRANSFORM
        self.transform = any(infile)  # TYPE_TRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} shape={shape}, isHierarchicalCompound={isHierarchicalCompound}, hkdShapesCollected={hkdShapesCollected}, childShapeNames=[{childShapeNames}], childTransforms=[{childTransforms}], transform={transform}>".format(**{
            "class_name": self.__class__.__name__,
            "shape": self.shape,
            "isHierarchicalCompound": self.isHierarchicalCompound,
            "hkdShapesCollected": self.hkdShapesCollected,
            "childShapeNames": self.childShapeNames,
            "childTransforms": self.childTransforms,
            "transform": self.transform,
        })
