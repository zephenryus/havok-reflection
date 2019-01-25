from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hclClothSetupObject import hclClothSetupObject
from .hclNamedSetupMesh import hclNamedSetupMesh
from .hclNamedTransformSetSetupObject import hclNamedTransformSetSetupObject


class hclClothSetupContainer(hkReferencedObject):
    clothSetupDatas: List[hclClothSetupObject]
    namedSetupMeshWrappers: List[hclNamedSetupMesh]
    namedTransformSetWrappers: List[hclNamedTransformSetSetupObject]

    def __init__(self, infile):
        self.clothSetupDatas = get_array(infile, hclClothSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.namedSetupMeshWrappers = get_array(infile, hclNamedSetupMesh, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.namedTransformSetWrappers = get_array(infile, hclNamedTransformSetSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} clothSetupDatas=[{clothSetupDatas}], namedSetupMeshWrappers=[{namedSetupMeshWrappers}], namedTransformSetWrappers=[{namedTransformSetWrappers}]>".format(**{
            "class_name": self.__class__.__name__,
            "clothSetupDatas": self.clothSetupDatas,
            "namedSetupMeshWrappers": self.namedSetupMeshWrappers,
            "namedTransformSetWrappers": self.namedTransformSetWrappers,
        })
