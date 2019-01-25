from .hkpConvexShape import hkpConvexShape
import struct
from .enums import WeldingType


class hkpTriangleShape(hkpConvexShape):
    weldingInfo: int
    weldingType: WeldingType
    isExtruded: int
    vertexA: vector4
    vertexB: vector4
    vertexC: vector4
    extrusion: vector4

    def __init__(self, infile):
        self.weldingInfo = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.weldingType = WeldingType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.isExtruded = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.vertexA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.vertexB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.vertexC = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.extrusion = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} weldingInfo={weldingInfo}, weldingType={weldingType}, isExtruded={isExtruded}, vertexA={vertexA}, vertexB={vertexB}, vertexC={vertexC}, extrusion={extrusion}>".format(**{
            "class_name": self.__class__.__name__,
            "weldingInfo": self.weldingInfo,
            "weldingType": self.weldingType,
            "isExtruded": self.isExtruded,
            "vertexA": self.vertexA,
            "vertexB": self.vertexB,
            "vertexC": self.vertexC,
            "extrusion": self.extrusion,
        })
