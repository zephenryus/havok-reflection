from .hkReferencedObject import hkReferencedObject
from .hclClothSetupObject import hclClothSetupObject
from .hclNamedSetupMesh import hclNamedSetupMesh
from .hclNamedTransformSetSetupObject import hclNamedTransformSetSetupObject


class hclClothSetupContainer(hkReferencedObject):
    clothSetupDatas: hclClothSetupObject
    namedSetupMeshWrappers: hclNamedSetupMesh
    namedTransformSetWrappers: hclNamedTransformSetSetupObject
