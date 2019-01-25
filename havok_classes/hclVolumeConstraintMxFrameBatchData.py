import struct


class hclVolumeConstraintMxFrameBatchData(object):
    frameVector: vector4
    particleIndex: int
    weight: float

    def __init__(self, infile):
        self.frameVector = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.particleIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.weight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} frameVector={frameVector}, particleIndex={particleIndex}, weight={weight}>".format(**{
            "class_name": self.__class__.__name__,
            "frameVector": self.frameVector,
            "particleIndex": self.particleIndex,
            "weight": self.weight,
        })
