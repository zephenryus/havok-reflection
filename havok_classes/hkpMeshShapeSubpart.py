from .common import any
import struct
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

    def __init__(self, infile):
        self.vertexBase = any(infile)  # TYPE_POINTER
        self.vertexStriding = struct.unpack('>i', infile.read(4))
        self.numVertices = struct.unpack('>i', infile.read(4))
        self.indexBase = any(infile)  # TYPE_POINTER
        self.stridingType = MeshShapeIndexStridingType(infile)  # TYPE_ENUM
        self.materialIndexStridingType = MeshShapeMaterialIndexStridingType(infile)  # TYPE_ENUM
        self.indexStriding = struct.unpack('>i', infile.read(4))
        self.flipAlternateTriangles = struct.unpack('>i', infile.read(4))
        self.numTriangles = struct.unpack('>i', infile.read(4))
        self.materialIndexBase = any(infile)  # TYPE_POINTER
        self.materialIndexStriding = struct.unpack('>i', infile.read(4))
        self.materialBase = any(infile)  # TYPE_POINTER
        self.materialStriding = struct.unpack('>i', infile.read(4))
        self.numMaterials = struct.unpack('>i', infile.read(4))
        self.triangleOffset = struct.unpack('>i', infile.read(4))
