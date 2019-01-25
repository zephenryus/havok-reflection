import struct


class hkSkinnedMeshShapePart(object):
    startVertex: int
    numVertices: int
    startIndex: int
    numIndices: int
    boneSetId: int
    meshSectionIndex: int
    boundingSphere: vector4

    def __init__(self, infile):
        self.startVertex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numVertices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.startIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numIndices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.boneSetId = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.meshSectionIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.boundingSphere = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startVertex={startVertex}, numVertices={numVertices}, startIndex={startIndex}, numIndices={numIndices}, boneSetId={boneSetId}, meshSectionIndex={meshSectionIndex}, boundingSphere={boundingSphere}>".format(**{
            "class_name": self.__class__.__name__,
            "startVertex": self.startVertex,
            "numVertices": self.numVertices,
            "startIndex": self.startIndex,
            "numIndices": self.numIndices,
            "boneSetId": self.boneSetId,
            "meshSectionIndex": self.meshSectionIndex,
            "boundingSphere": self.boundingSphere,
        })
