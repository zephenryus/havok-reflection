from .hclOperator import hclOperator
from .common import any
import struct


class hclGatherAllVerticesOperator(hclOperator):
    vertexInputFromVertexOutput: any
    inputBufferIdx: int
    outputBufferIdx: int
    gatherNormals: bool
    partialGather: bool

    def __init__(self, infile):
        self.vertexInputFromVertexOutput = any(infile)  # TYPE_ARRAY
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))
        self.gatherNormals = struct.unpack('>?', infile.read(1))
        self.partialGather = struct.unpack('>?', infile.read(1))
