from .hkMeshShape import hkMeshShape
from .common import any


class hkSkinBinding(hkMeshShape):
    skin: hkMeshShape
    worldFromBoneTransforms: any
    boneNames: any
