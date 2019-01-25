from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
from .hclVertexFloatInput import hclVertexFloatInput
import struct


class hclBlendSetupObject(hclOperatorSetupObject):
    name: str
    A: hclBufferSetupObject
    B: hclBufferSetupObject
    C: hclBufferSetupObject
    vertexSelection: hclVertexSelectionInput
    blendWeights: hclVertexFloatInput
    mapToScurve: bool
    blendNormals: bool
    blendTangents: bool
    blendBitangents: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.A = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.B = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.C = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.blendWeights = hclVertexFloatInput(infile)  # TYPE_STRUCT
        self.mapToScurve = struct.unpack('>?', infile.read(1))
        self.blendNormals = struct.unpack('>?', infile.read(1))
        self.blendTangents = struct.unpack('>?', infile.read(1))
        self.blendBitangents = struct.unpack('>?', infile.read(1))
