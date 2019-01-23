from .hkpConvexShape import hkpConvexShape


class hkpTriangleShape(hkpConvexShape):
	weldingInfo: int
	weldingType: any
	isExtruded: int
	vertexA: any
	vertexB: any
	vertexC: any
	extrusion: any
