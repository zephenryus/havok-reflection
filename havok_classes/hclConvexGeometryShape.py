from .hclShape import hclShape
from .hkAabb import hkAabb


class hclConvexGeometryShape(hclShape):
	tetrahedraGrid: any
	gridCells: any
	tetrahedraEquations: any
	localFromWorld: any
	worldFromLocal: any
	objAabb: hkAabb
	geomCentroid: any
	invCellSize: any
	gridRes: int
