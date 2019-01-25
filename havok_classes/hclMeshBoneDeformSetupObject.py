from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTriangleSelectionInput import hclTriangleSelectionInput
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from typing import List
from .common import get_array
import struct


class hclMeshBoneDeformSetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: any
    inputTriangleSelection: hclTriangleSelectionInput
    outputTransformSetSetupObject: any
    deformedBones: List[str]
    maxTrianglesPerBone: int
    minimumTriangleWeight: float

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.inputBufferSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.inputTriangleSelection = hclTriangleSelectionInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.outputTransformSetSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.deformedBones = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR
        self.maxTrianglesPerBone = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.minimumTriangleWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", inputBufferSetupObject={inputBufferSetupObject}, inputTriangleSelection={inputTriangleSelection}, outputTransformSetSetupObject={outputTransformSetSetupObject}, deformedBones=[{deformedBones}], maxTrianglesPerBone={maxTrianglesPerBone}, minimumTriangleWeight={minimumTriangleWeight}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "inputBufferSetupObject": self.inputBufferSetupObject,
            "inputTriangleSelection": self.inputTriangleSelection,
            "outputTransformSetSetupObject": self.outputTransformSetSetupObject,
            "deformedBones": self.deformedBones,
            "maxTrianglesPerBone": self.maxTrianglesPerBone,
            "minimumTriangleWeight": self.minimumTriangleWeight,
        })
