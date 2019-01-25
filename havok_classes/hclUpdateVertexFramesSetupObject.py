from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
import struct


class hclUpdateVertexFramesSetupObject(hclOperatorSetupObject):
    name: str
    buffer: hclBufferSetupObject
    vertexSelection: hclVertexSelectionInput
    updateNormals: bool
    updateTangents: bool
    updateBiTangents: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.buffer = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.updateNormals = struct.unpack('>?', infile.read(1))
        self.updateTangents = struct.unpack('>?', infile.read(1))
        self.updateBiTangents = struct.unpack('>?', infile.read(1))
