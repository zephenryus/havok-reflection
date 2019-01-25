from .hkReferencedObject import hkReferencedObject
from .hkpBreakableMultiMaterialInverseMappingDescriptor import hkpBreakableMultiMaterialInverseMappingDescriptor
from .common import any


class hkpBreakableMultiMaterialInverseMapping(hkReferencedObject):
    descriptors: hkpBreakableMultiMaterialInverseMappingDescriptor
    subShapeIds: any

    def __init__(self, infile):
        self.descriptors = hkpBreakableMultiMaterialInverseMappingDescriptor(infile)  # TYPE_ARRAY
        self.subShapeIds = any(infile)  # TYPE_ARRAY
