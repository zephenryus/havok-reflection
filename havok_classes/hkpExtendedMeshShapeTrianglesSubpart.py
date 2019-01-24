from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart
from .common import any, vector4
from .enums import IndexStridingType


class hkpExtendedMeshShapeTrianglesSubpart(hkpExtendedMeshShapeSubpart):
    numTriangleShapes: int
    vertexBase: any
    numVertices: int
    indexBase: any
    vertexStriding: int
    triangleOffset: int
    indexStriding: int
    stridingType: IndexStridingType
    flipAlternateTriangles: int
    extrusion: vector4
    transform: any
