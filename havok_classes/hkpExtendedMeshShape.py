from .hkpShapeCollection import hkpShapeCollection
from .hkpExtendedMeshShapeTrianglesSubpart import hkpExtendedMeshShapeTrianglesSubpart
from .hkpExtendedMeshShapeTrianglesSubpart import hkpExtendedMeshShapeTrianglesSubpart
from .hkpExtendedMeshShapeShapesSubpart import hkpExtendedMeshShapeShapesSubpart


class hkpExtendedMeshShape(hkpShapeCollection):
	embeddedTrianglesSubpart: hkpExtendedMeshShapeTrianglesSubpart
	aabbHalfExtents: any
	aabbCenter: any
	materialClass: any
	numBitsForSubpartIndex: int
	trianglesSubparts: hkpExtendedMeshShapeTrianglesSubpart
	shapesSubparts: hkpExtendedMeshShapeShapesSubpart
	weldingInfo: any
	weldingType: any
	defaultCollisionFilterInfo: int
	cachedNumChildShapes: int
	triangleRadius: float
	padding: int
