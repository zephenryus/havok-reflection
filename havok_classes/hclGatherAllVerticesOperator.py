from .hclOperator import hclOperator
from typing import List
from .common import get_array
import struct


class hclGatherAllVerticesOperator(hclOperator):
    vertexInputFromVertexOutput: List[int]
    inputBufferIdx: int
    outputBufferIdx: int
    gatherNormals: bool
    partialGather: bool

    def __init__(self, infile):
        self.vertexInputFromVertexOutput = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.gatherNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.partialGather = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexInputFromVertexOutput=[{vertexInputFromVertexOutput}], inputBufferIdx={inputBufferIdx}, outputBufferIdx={outputBufferIdx}, gatherNormals={gatherNormals}, partialGather={partialGather}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexInputFromVertexOutput": self.vertexInputFromVertexOutput,
            "inputBufferIdx": self.inputBufferIdx,
            "outputBufferIdx": self.outputBufferIdx,
            "gatherNormals": self.gatherNormals,
            "partialGather": self.partialGather,
        })
