from .hkReferencedObject import hkReferencedObject
from .hclClothStateBufferAccess import hclClothStateBufferAccess
from .hclClothStateTransformSetAccess import hclClothStateTransformSetAccess


class hclClothState(hkReferencedObject):
	name: any
	operators: any
	usedBuffers: hclClothStateBufferAccess
	usedTransformSets: hclClothStateTransformSetAccess
	usedSimCloths: any
