from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclVertexSelectionInput import hclVertexSelectionInput
import struct


class hclSkinSetupObject(hclOperatorSetupObject):
    name: str
    transformSetSetup: any
    referenceBufferSetup: any
    outputBufferSetup: any
    vertexSelection: hclVertexSelectionInput
    skinNormals: bool
    skinTangents: bool
    skinBiTangents: bool
    useDualQuaternionMethod: bool

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.transformSetSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.referenceBufferSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.outputBufferSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vertexSelection = hclVertexSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.skinNormals = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.skinTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.skinBiTangents = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.useDualQuaternionMethod = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", transformSetSetup={transformSetSetup}, referenceBufferSetup={referenceBufferSetup}, outputBufferSetup={outputBufferSetup}, vertexSelection={vertexSelection}, skinNormals={skinNormals}, skinTangents={skinTangents}, skinBiTangents={skinBiTangents}, useDualQuaternionMethod={useDualQuaternionMethod}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "transformSetSetup": self.transformSetSetup,
            "referenceBufferSetup": self.referenceBufferSetup,
            "outputBufferSetup": self.outputBufferSetup,
            "vertexSelection": self.vertexSelection,
            "skinNormals": self.skinNormals,
            "skinTangents": self.skinTangents,
            "skinBiTangents": self.skinBiTangents,
            "useDualQuaternionMethod": self.useDualQuaternionMethod,
        })
