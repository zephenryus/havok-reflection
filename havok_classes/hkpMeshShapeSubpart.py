from .common import any
from .enums import MeshShapeIndexStridingType, MeshShapeMaterialIndexStridingType


class hkpMeshShapeSubpart(object):
    vertexBase: any
    vertexStriding: int
    numVertices: int
    indexBase: any
    stridingType: MeshShapeIndexStridingType
    materialIndexStridingType: MeshShapeMaterialIndexStridingType
    indexStriding: int
    flipAlternateTriangles: int
    numTriangles: int
    materialIndexBase: any
    materialIndexStriding: int
    materialBase: any
    materialStriding: int
    numMaterials: int
    triangleOffset: int
