from .common import any
import struct


class hclMeshBoneDeformOperatorTriangleBonePair(object):
    localBoneTransform: any
    weight: float
    triangleIndex: int

    def __init__(self, infile):
        self.localBoneTransform = any(infile)  # TYPE_MATRIX4
        self.weight = struct.unpack('>f', infile.read(4))
        self.triangleIndex = struct.unpack('>H', infile.read(2))
