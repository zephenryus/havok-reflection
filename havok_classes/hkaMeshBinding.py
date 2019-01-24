from .hkReferencedObject import hkReferencedObject
from .hkxMesh import hkxMesh
from .hkaSkeleton import hkaSkeleton
from .hkaMeshBindingMapping import hkaMeshBindingMapping
from .common import any


class hkaMeshBinding(hkReferencedObject):
    mesh: hkxMesh
    originalSkeletonName: str
    name: str
    skeleton: hkaSkeleton
    mappings: hkaMeshBindingMapping
    boneFromSkinMeshTransforms: any
