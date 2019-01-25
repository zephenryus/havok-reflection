from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array


class hclStorageSetupMeshSectionBoneInfluences(hkReferencedObject):
    boneIndices: List[int]
    weights: List[float]

    def __init__(self, infile):
        self.boneIndices = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.weights = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} boneIndices=[{boneIndices}], weights=[{weights}]>".format(**{
            "class_name": self.__class__.__name__,
            "boneIndices": self.boneIndices,
            "weights": self.weights,
        })
