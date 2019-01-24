from .hkReferencedObject import hkReferencedObject
from .hkpBreakableMultiMaterialInverseMappingDescriptor import hkpBreakableMultiMaterialInverseMappingDescriptor
from .common import any


class hkpBreakableMultiMaterialInverseMapping(hkReferencedObject):
    descriptors: hkpBreakableMultiMaterialInverseMappingDescriptor
    subShapeIds: any
