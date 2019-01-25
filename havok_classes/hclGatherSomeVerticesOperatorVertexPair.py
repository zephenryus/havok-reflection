import struct


class hclGatherSomeVerticesOperatorVertexPair(object):
    indexInput: int
    indexOutput: int

    def __init__(self, infile):
        self.indexInput = struct.unpack('>H', infile.read(2))
        self.indexOutput = struct.unpack('>H', infile.read(2))
