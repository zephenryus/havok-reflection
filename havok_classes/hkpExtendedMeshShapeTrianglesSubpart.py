from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart


class hkpExtendedMeshShapeTrianglesSubpart(hkpExtendedMeshShapeSubpart):
	numTriangleShapes: int
	vertexBase: any
	numVertices: int
	indexBase: any
	vertexStriding: int
	triangleOffset: int
	indexStriding: int
	stridingType: any
	flipAlternateTriangles: int
	extrusion: any
	transform: any
