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

    def __init__(self, infile):
        self.mesh = hkxMesh(infile)  # TYPE_POINTER
        self.originalSkeletonName = struct.unpack('>s', infile.read(0))
        self.name = struct.unpack('>s', infile.read(0))
        self.skeleton = hkaSkeleton(infile)  # TYPE_POINTER
        self.mappings = hkaMeshBindingMapping(infile)  # TYPE_ARRAY
        self.boneFromSkinMeshTransforms = any(infile)  # TYPE_ARRAY
