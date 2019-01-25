from .hkpExtendedMeshShapeSubpart import hkpExtendedMeshShapeSubpart
import struct
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
        self.numTriangleShapes = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.vertexBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.numVertices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.vertexStriding = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.triangleOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexStriding = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.stridingType = IndexStridingType(infile)  # TYPE_ENUM:TYPE_INT8
        self.flipAlternateTriangles = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.extrusion = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.transform = any(infile)  # TYPE_QSTRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} numTriangleShapes={numTriangleShapes}, vertexBase={vertexBase}, numVertices={numVertices}, indexBase={indexBase}, vertexStriding={vertexStriding}, triangleOffset={triangleOffset}, indexStriding={indexStriding}, stridingType={stridingType}, flipAlternateTriangles={flipAlternateTriangles}, extrusion={extrusion}, transform={transform}>".format(**{
            "class_name": self.__class__.__name__,
            "numTriangleShapes": self.numTriangleShapes,
            "vertexBase": self.vertexBase,
            "numVertices": self.numVertices,
            "indexBase": self.indexBase,
            "vertexStriding": self.vertexStriding,
            "triangleOffset": self.triangleOffset,
            "indexStriding": self.indexStriding,
            "stridingType": self.stridingType,
            "flipAlternateTriangles": self.flipAlternateTriangles,
            "extrusion": self.extrusion,
            "transform": self.transform,
        })
