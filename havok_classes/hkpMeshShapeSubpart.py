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
        self.vertexBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.vertexStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numVertices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.indexBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.stridingType = MeshShapeIndexStridingType(infile)  # TYPE_ENUM:TYPE_INT8
        self.materialIndexStridingType = MeshShapeMaterialIndexStridingType(infile)  # TYPE_ENUM:TYPE_INT8
        self.indexStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.flipAlternateTriangles = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numTriangles = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.materialIndexBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.materialIndexStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.materialBase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.materialStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numMaterials = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.triangleOffset = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexBase={vertexBase}, vertexStriding={vertexStriding}, numVertices={numVertices}, indexBase={indexBase}, stridingType={stridingType}, materialIndexStridingType={materialIndexStridingType}, indexStriding={indexStriding}, flipAlternateTriangles={flipAlternateTriangles}, numTriangles={numTriangles}, materialIndexBase={materialIndexBase}, materialIndexStriding={materialIndexStriding}, materialBase={materialBase}, materialStriding={materialStriding}, numMaterials={numMaterials}, triangleOffset={triangleOffset}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexBase": self.vertexBase,
            "vertexStriding": self.vertexStriding,
            "numVertices": self.numVertices,
            "indexBase": self.indexBase,
            "stridingType": self.stridingType,
            "materialIndexStridingType": self.materialIndexStridingType,
            "indexStriding": self.indexStriding,
            "flipAlternateTriangles": self.flipAlternateTriangles,
            "numTriangles": self.numTriangles,
            "materialIndexBase": self.materialIndexBase,
            "materialIndexStriding": self.materialIndexStriding,
            "materialBase": self.materialBase,
            "materialStriding": self.materialStriding,
            "numMaterials": self.numMaterials,
            "triangleOffset": self.triangleOffset,
        })
