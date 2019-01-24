from .hkReferencedObject import hkReferencedObject
from .common import any
from .hclClothStateBufferAccess import hclClothStateBufferAccess
from .hclClothStateTransformSetAccess import hclClothStateTransformSetAccess


class hclClothState(hkReferencedObject):
    name: str
    operators: any
    usedBuffers: hclClothStateBufferAccess
    usedTransformSets: hclClothStateTransformSetAccess
    usedSimCloths: any
