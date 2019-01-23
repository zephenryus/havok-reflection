from .hkReferencedObject import hkReferencedObject
from .hkxSplineControlPoint import hkxSplineControlPoint


class hkxSpline(hkReferencedObject):
	controlPoints: hkxSplineControlPoint
	isClosed: bool
