from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart
import struct
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

    def __init__(self, infile):
        self.numTriangleShapes = struct.unpack('>i', infile.read(4))
        self.vertexBase = any(infile)  # TYPE_POINTER
        self.numVertices = struct.unpack('>i', infile.read(4))
        self.indexBase = any(infile)  # TYPE_POINTER
        self.vertexStriding = struct.unpack('>H', infile.read(2))
        self.triangleOffset = struct.unpack('>i', infile.read(4))
        self.indexStriding = struct.unpack('>H', infile.read(2))
        self.stridingType = IndexStridingType(infile)  # TYPE_ENUM
        self.flipAlternateTriangles = struct.unpack('>b', infile.read(1))
        self.extrusion = struct.unpack('>4f', infile.read(16))
        self.transform = any(infile)  # TYPE_QSTRANSFORM
