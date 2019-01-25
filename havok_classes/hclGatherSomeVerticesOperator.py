from .hclOperator import hclOperator
from typing import List
from .common import get_array
from .hclGatherSomeVerticesOperatorVertexPair import hclGatherSomeVerticesOperatorVertexPair
import struct


class hclGatherSomeVerticesOperator(hclOperator):
    vertexPairs: List[hclGatherSomeVerticesOperatorVertexPair]
    inputBufferIdx: int
    outputBufferIdx: int
    gatherNormals: bool

    def __init__(self, infile):
        self.vertexPairs = get_array(infile, hclGatherSomeVerticesOperatorVertexPair, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.gatherNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexPairs=[{vertexPairs}], inputBufferIdx={inputBufferIdx}, outputBufferIdx={outputBufferIdx}, gatherNormals={gatherNormals}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexPairs": self.vertexPairs,
            "inputBufferIdx": self.inputBufferIdx,
            "outputBufferIdx": self.outputBufferIdx,
            "gatherNormals": self.gatherNormals,
        })
