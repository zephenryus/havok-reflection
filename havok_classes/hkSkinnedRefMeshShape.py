from .hkMeshShape import hkMeshShape
from .hkSkinnedMeshShape import hkSkinnedMeshShape
from .common import any


class hkSkinnedRefMeshShape(hkMeshShape):
    skinnedMeshShape: hkSkinnedMeshShape
    bones: any
    localFromRootTransforms: any
    name: str

    def __init__(self, infile):
        self.skinnedMeshShape = hkSkinnedMeshShape(infile)  # TYPE_POINTER
        self.bones = any(infile)  # TYPE_ARRAY
        self.localFromRootTransforms = any(infile)  # TYPE_ARRAY
        self.name = struct.unpack('>s', infile.read(0))
