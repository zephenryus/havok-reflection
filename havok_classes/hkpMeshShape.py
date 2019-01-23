from .hkpShapeCollection import hkpShapeCollection
from .hkpMeshShapeSubpart import hkpMeshShapeSubpart


class hkpMeshShape(hkpShapeCollection):
	scaling: any
	numBitsForSubpartIndex: int
	subparts: hkpMeshShapeSubpart
	weldingInfo: any
	weldingType: any
	radius: float
	pad: int
