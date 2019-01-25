import struct


class hclMeshBoneDeformOperatorTriangleBonePair(object):
    localBoneTransform: any
    weight: float
    triangleIndex: int

    def __init__(self, infile):
        self.localBoneTransform = any(infile)  # TYPE_MATRIX4:TYPE_VOID
        self.weight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.triangleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localBoneTransform={localBoneTransform}, weight={weight}, triangleIndex={triangleIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "localBoneTransform": self.localBoneTransform,
            "weight": self.weight,
            "triangleIndex": self.triangleIndex,
        })
