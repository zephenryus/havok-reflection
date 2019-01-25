from .hkMeshShape import hkMeshShape
from .hkSkinnedMeshShape import hkSkinnedMeshShape
from typing import List
from .common import get_array


class hkSkinnedRefMeshShape(hkMeshShape):
    skinnedMeshShape: any
    bones: List[int]
    localFromRootTransforms: List[vector4]
    name: str

    def __init__(self, infile):
        self.skinnedMeshShape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.bones = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.localFromRootTransforms = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} skinnedMeshShape={skinnedMeshShape}, bones=[{bones}], localFromRootTransforms=[{localFromRootTransforms}], name=\"{name}\">".format(**{
            "class_name": self.__class__.__name__,
            "skinnedMeshShape": self.skinnedMeshShape,
            "bones": self.bones,
            "localFromRootTransforms": self.localFromRootTransforms,
            "name": self.name,
        })
