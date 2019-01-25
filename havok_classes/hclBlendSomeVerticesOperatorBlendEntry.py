import struct


class hclBlendSomeVerticesOperatorBlendEntry(object):
    vertexIndex: int
    blendWeight: float

    def __init__(self, infile):
        self.vertexIndex = struct.unpack('>H', infile.read(2))
        self.blendWeight = struct.unpack('>f', infile.read(4))
