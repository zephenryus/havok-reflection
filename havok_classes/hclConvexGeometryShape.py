from .hclShape import hclShape
from .common import any, vector4
from .hkAabb import hkAabb


class hclConvexGeometryShape(hclShape):
    tetrahedraGrid: any
    gridCells: any
    tetrahedraEquations: any
    localFromWorld: any
    worldFromLocal: any
    objAabb: hkAabb
    geomCentroid: vector4
    invCellSize: vector4
    gridRes: int
