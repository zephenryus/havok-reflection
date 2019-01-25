import struct


class hclMeshMeshDeformOperatorTriangleVertexPair(object):
    localPosition: vector4
    localNormal: vector4
    triangleIndex: int
    weight: float

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.localNormal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.triangleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.weight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localPosition={localPosition}, localNormal={localNormal}, triangleIndex={triangleIndex}, weight={weight}>".format(**{
            "class_name": self.__class__.__name__,
            "localPosition": self.localPosition,
            "localNormal": self.localNormal,
            "triangleIndex": self.triangleIndex,
            "weight": self.weight,
        })
