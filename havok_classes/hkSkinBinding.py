from .hkMeshShape import hkMeshShape
from .common import any


class hkSkinBinding(hkMeshShape):
    skin: hkMeshShape
    worldFromBoneTransforms: any
    boneNames: any

    def __init__(self, infile):
        self.skin = hkMeshShape(infile)  # TYPE_POINTER
        self.worldFromBoneTransforms = any(infile)  # TYPE_ARRAY
        self.boneNames = any(infile)  # TYPE_ARRAY
