from .hclOperator import hclOperator
from .hclGatherSomeVerticesOperatorVertexPair import hclGatherSomeVerticesOperatorVertexPair
import struct


class hclGatherSomeVerticesOperator(hclOperator):
    vertexPairs: hclGatherSomeVerticesOperatorVertexPair
    inputBufferIdx: int
    outputBufferIdx: int
    gatherNormals: bool

    def __init__(self, infile):
        self.vertexPairs = hclGatherSomeVerticesOperatorVertexPair(infile)  # TYPE_ARRAY
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))
        self.gatherNormals = struct.unpack('>?', infile.read(1))
