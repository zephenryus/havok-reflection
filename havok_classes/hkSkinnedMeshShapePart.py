import struct
from .common import vector4


class hkSkinnedMeshShapePart(object):
    startVertex: int
    numVertices: int
    startIndex: int
    numIndices: int
    boneSetId: int
    meshSectionIndex: int
    boundingSphere: vector4

    def __init__(self, infile):
        self.startVertex = struct.unpack('>i', infile.read(4))
        self.numVertices = struct.unpack('>i', infile.read(4))
        self.startIndex = struct.unpack('>i', infile.read(4))
        self.numIndices = struct.unpack('>i', infile.read(4))
        self.boneSetId = struct.unpack('>H', infile.read(2))
        self.meshSectionIndex = struct.unpack('>H', infile.read(2))
        self.boundingSphere = struct.unpack('>4f', infile.read(16))
