from .common import vector4
import struct


class hclVolumeConstraintMxApplyBatchData(object):
    frameVector: vector4
    particleIndex: int
    stiffness: float

    def __init__(self, infile):
        self.frameVector = struct.unpack('>4f', infile.read(16))
        self.particleIndex = struct.unpack('>H', infile.read(2))
        self.stiffness = struct.unpack('>f', infile.read(4))
