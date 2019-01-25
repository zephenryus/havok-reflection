from .hkpShapeCollection import hkpShapeCollection
from .common import any
from .hkpSimpleMeshShapeTriangle import hkpSimpleMeshShapeTriangle
import struct
from .enums import WeldingType


class hkpSimpleMeshShape(hkpShapeCollection):
    vertices: any
    triangles: hkpSimpleMeshShapeTriangle
    materialIndices: any
    radius: float
    weldingType: WeldingType

    def __init__(self, infile):
        self.vertices = any(infile)  # TYPE_ARRAY
        self.triangles = hkpSimpleMeshShapeTriangle(infile)  # TYPE_ARRAY
        self.materialIndices = any(infile)  # TYPE_ARRAY
        self.radius = struct.unpack('>f', infile.read(4))
        self.weldingType = WeldingType(infile)  # TYPE_ENUM
