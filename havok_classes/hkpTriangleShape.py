from .hkpConvexShape import hkpConvexShape
import struct
from .enums import WeldingType
from .common import vector4


class hkpTriangleShape(hkpConvexShape):
    weldingInfo: int
    weldingType: WeldingType
    isExtruded: int
    vertexA: vector4
    vertexB: vector4
    vertexC: vector4
    extrusion: vector4

    def __init__(self, infile):
        self.weldingInfo = struct.unpack('>H', infile.read(2))
        self.weldingType = WeldingType(infile)  # TYPE_ENUM
        self.isExtruded = struct.unpack('>B', infile.read(1))
        self.vertexA = struct.unpack('>4f', infile.read(16))
        self.vertexB = struct.unpack('>4f', infile.read(16))
        self.vertexC = struct.unpack('>4f', infile.read(16))
        self.extrusion = struct.unpack('>4f', infile.read(16))
