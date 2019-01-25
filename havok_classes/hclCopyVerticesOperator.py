from .hclOperator import hclOperator
import struct


class hclCopyVerticesOperator(hclOperator):
    inputBufferIdx: int
    outputBufferIdx: int
    numberOfVertices: int
    startVertexIn: int
    startVertexOut: int
    copyNormals: bool

    def __init__(self, infile):
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))
        self.numberOfVertices = struct.unpack('>I', infile.read(4))
        self.startVertexIn = struct.unpack('>I', infile.read(4))
        self.startVertexOut = struct.unpack('>I', infile.read(4))
        self.copyNormals = struct.unpack('>?', infile.read(1))
