from .hkReferencedObject import hkReferencedObject
from .hkcdPlanarSolidNode import hkcdPlanarSolidNode
from .hkAabb import hkAabb


class hkcdPlanarSolidNodeStorage(hkReferencedObject):
	storage: hkcdPlanarSolidNode
	aabbs: hkAabb
	firstFreeNodeId: int
