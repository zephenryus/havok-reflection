from .common import vector4
import struct


class hclMeshMeshDeformOperatorTriangleVertexPair(object):
    localPosition: vector4
    localNormal: vector4
    triangleIndex: int
    weight: float

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))
        self.localNormal = struct.unpack('>4f', infile.read(16))
        self.triangleIndex = struct.unpack('>H', infile.read(2))
        self.weight = struct.unpack('>f', infile.read(4))
