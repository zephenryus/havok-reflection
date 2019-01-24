from .hkReferencedObject import hkReferencedObject
from .hkpShape import hkpShape
from .common import any


class hkpShapeInfo(hkReferencedObject):
    shape: hkpShape
    isHierarchicalCompound: bool
    hkdShapesCollected: bool
    childShapeNames: any
    childTransforms: any
    transform: any
