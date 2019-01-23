from .hkpShapeCollection import hkpShapeCollection
from .hkpListShapeChildInfo import hkpListShapeChildInfo


class hkpListShape(hkpShapeCollection):
	childInfo: hkpListShapeChildInfo
	flags: int
	numDisabledChildren: int
	aabbHalfExtents: any
	aabbCenter: any
	enabledChildren: int
