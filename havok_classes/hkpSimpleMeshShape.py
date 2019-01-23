from .hkpShapeCollection import hkpShapeCollection
from .hkpSimpleMeshShapeTriangle import hkpSimpleMeshShapeTriangle


class hkpSimpleMeshShape(hkpShapeCollection):
	vertices: any
	triangles: hkpSimpleMeshShapeTriangle
	materialIndices: any
	radius: float
	weldingType: any
