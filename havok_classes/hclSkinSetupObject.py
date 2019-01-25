from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
import struct


class hclSkinSetupObject(hclOperatorSetupObject):
    name: str
    transformSetSetup: hclTransformSetSetupObject
    referenceBufferSetup: hclBufferSetupObject
    outputBufferSetup: hclBufferSetupObject
    vertexSelection: hclVertexSelectionInput
    skinNormals: bool
    skinTangents: bool
    skinBiTangents: bool
    useDualQuaternionMethod: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.transformSetSetup = hclTransformSetSetupObject(infile)  # TYPE_POINTER
        self.referenceBufferSetup = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.outputBufferSetup = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT
        self.skinNormals = struct.unpack('>?', infile.read(1))
        self.skinTangents = struct.unpack('>?', infile.read(1))
        self.skinBiTangents = struct.unpack('>?', infile.read(1))
        self.useDualQuaternionMethod = struct.unpack('>?', infile.read(1))
