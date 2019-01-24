from .hclShape import hclShape
from .common import any, vector4
from .hkAabb import hkAabb


class hclConvexPlanesShape(hclShape):
    planeEquations: any
    localFromWorld: any
    worldFromLocal: any
    objAabb: hkAabb
    geomCentroid: vector4
