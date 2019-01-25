from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpBreakableMultiMaterialInverseMappingDescriptor import hkpBreakableMultiMaterialInverseMappingDescriptor


class hkpBreakableMultiMaterialInverseMapping(hkReferencedObject):
    descriptors: List[hkpBreakableMultiMaterialInverseMappingDescriptor]
    subShapeIds: List[int]

    def __init__(self, infile):
        self.descriptors = get_array(infile, hkpBreakableMultiMaterialInverseMappingDescriptor, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.subShapeIds = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} descriptors=[{descriptors}], subShapeIds=[{subShapeIds}]>".format(**{
            "class_name": self.__class__.__name__,
            "descriptors": self.descriptors,
            "subShapeIds": self.subShapeIds,
        })
