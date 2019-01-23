from .hkReferencedObject import hkReferencedObject
from .hkpTyremarkPoint import hkpTyremarkPoint


class hkpTyremarksWheel(hkReferencedObject):
	currentPosition: int
	numPoints: int
	tyremarkPoints: hkpTyremarkPoint
