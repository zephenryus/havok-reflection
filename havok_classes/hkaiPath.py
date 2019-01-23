from .hkReferencedObject import hkReferencedObject
from .hkaiPathPathPoint import hkaiPathPathPoint


class hkaiPath(hkReferencedObject):
	points: hkaiPathPathPoint
	referenceFrame: any
