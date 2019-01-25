from .hkMeshShape import hkMeshShape
from typing import List
from .common import get_array


class hkSkinBinding(hkMeshShape):
    skin: any
    worldFromBoneTransforms: List[any]
    boneNames: List[str]

    def __init__(self, infile):
        self.skin = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.worldFromBoneTransforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX4
        self.boneNames = get_array(infile, str, 0)  # TYPE_ARRAY:TYPE_STRINGPTR

    def __repr__(self):
        return "<{class_name} skin={skin}, worldFromBoneTransforms=[{worldFromBoneTransforms}], boneNames=[{boneNames}]>".format(**{
            "class_name": self.__class__.__name__,
            "skin": self.skin,
            "worldFromBoneTransforms": self.worldFromBoneTransforms,
            "boneNames": self.boneNames,
        })
