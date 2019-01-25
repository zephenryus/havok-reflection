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
        self.inputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.outputBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.numberOfVertices = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.startVertexIn = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.startVertexOut = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.copyNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} inputBufferIdx={inputBufferIdx}, outputBufferIdx={outputBufferIdx}, numberOfVertices={numberOfVertices}, startVertexIn={startVertexIn}, startVertexOut={startVertexOut}, copyNormals={copyNormals}>".format(**{
            "class_name": self.__class__.__name__,
            "inputBufferIdx": self.inputBufferIdx,
            "outputBufferIdx": self.outputBufferIdx,
            "numberOfVertices": self.numberOfVertices,
            "startVertexIn": self.startVertexIn,
            "startVertexOut": self.startVertexOut,
            "copyNormals": self.copyNormals,
        })
