from .hclShape import hclShape
from .hkAabb import hkAabb


class hclConvexPlanesShape(hclShape):
	planeEquations: any
	localFromWorld: any
	worldFromLocal: any
	objAabb: hkAabb
	geomCentroid: any
