from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclBufferSetupObject import hclBufferSetupObject
from .hclTriangleSelectionInput import hclTriangleSelectionInput
from .hclTransformSetSetupObject import hclTransformSetSetupObject
from .common import any


class hclMeshBoneDeformSetupObject(hclOperatorSetupObject):
    name: str
    inputBufferSetupObject: hclBufferSetupObject
    inputTriangleSelection: hclTriangleSelectionInput
    outputTransformSetSetupObject: hclTransformSetSetupObject
    deformedBones: any
    maxTrianglesPerBone: int
    minimumTriangleWeight: float
