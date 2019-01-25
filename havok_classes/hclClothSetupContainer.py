from .hkReferencedObject import hkReferencedObject
from .hclClothSetupObject import hclClothSetupObject
from .hclNamedSetupMesh import hclNamedSetupMesh
from .hclNamedTransformSetSetupObject import hclNamedTransformSetSetupObject


class hclClothSetupContainer(hkReferencedObject):
    clothSetupDatas: hclClothSetupObject
    namedSetupMeshWrappers: hclNamedSetupMesh
    namedTransformSetWrappers: hclNamedTransformSetSetupObject

    def __init__(self, infile):
        self.clothSetupDatas = hclClothSetupObject(infile)  # TYPE_ARRAY
        self.namedSetupMeshWrappers = hclNamedSetupMesh(infile)  # TYPE_ARRAY
        self.namedTransformSetWrappers = hclNamedTransformSetSetupObject(infile)  # TYPE_ARRAY
