from .hkReferencedObject import hkReferencedObject
from .common import any


class hclStorageSetupMeshSectionBoneInfluences(hkReferencedObject):
    boneIndices: any
    weights: any

    def __init__(self, infile):
        self.boneIndices = any(infile)  # TYPE_ARRAY
        self.weights = any(infile)  # TYPE_ARRAY
