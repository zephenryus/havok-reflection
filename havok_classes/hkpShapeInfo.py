from .hkReferencedObject import hkReferencedObject
from .hkpShape import hkpShape


class hkpShapeInfo(hkReferencedObject):
	shape: hkpShape
	isHierarchicalCompound: bool
	hkdShapesCollected: bool
	childShapeNames: any
	childTransforms: any
	transform: any
