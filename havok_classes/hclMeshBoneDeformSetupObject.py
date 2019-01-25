from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTriangleSelectionInput import hclTriangleSelectionInput
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .common import any
import struct


class hclMeshBoneDeformSetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: hclBufferSetupObject
    inputTriangleSelection: hclTriangleSelectionInput
    outputTransformSetSetupObject: hclTransformSetSetupObject
    deformedBones: any
    maxTrianglesPerBone: int
    minimumTriangleWeight: float

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.inputBufferSetupObject = hclBufferSetupObject(infile)  # TYPE_POINTER
        self.inputTriangleSelection = hclTriangleSelectionInput(infile)  # TYPE_STRUCT
        self.outputTransformSetSetupObject = hclTransformSetSetupObject(infile)  # TYPE_POINTER
        self.deformedBones = any(infile)  # TYPE_ARRAY
        self.maxTrianglesPerBone = struct.unpack('>I', infile.read(4))
        self.minimumTriangleWeight = struct.unpack('>f', infile.read(4))
