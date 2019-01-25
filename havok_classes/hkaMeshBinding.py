from .hkReferencedObject import hkReferencedObject
from .hkxMesh import hkxMesh
from .hkaSkeleton import hkaSkeleton
from typing import List
from .common import get_array
from .hkaMeshBindingMapping import hkaMeshBindingMapping


class hkaMeshBinding(hkReferencedObject):
    mesh: any
    originalSkeletonName: str
    name: str
    skeleton: any
    mappings: List[hkaMeshBindingMapping]
    boneFromSkinMeshTransforms: List[any]

    def __init__(self, infile):
        self.mesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.originalSkeletonName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.skeleton = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.mappings = get_array(infile, hkaMeshBindingMapping, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.boneFromSkinMeshTransforms = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_TRANSFORM

    def __repr__(self):
        return "<{class_name} mesh={mesh}, originalSkeletonName=\"{originalSkeletonName}\", name=\"{name}\", skeleton={skeleton}, mappings=[{mappings}], boneFromSkinMeshTransforms=[{boneFromSkinMeshTransforms}]>".format(**{
            "class_name": self.__class__.__name__,
            "mesh": self.mesh,
            "originalSkeletonName": self.originalSkeletonName,
            "name": self.name,
            "skeleton": self.skeleton,
            "mappings": self.mappings,
            "boneFromSkinMeshTransforms": self.boneFromSkinMeshTransforms,
        })
