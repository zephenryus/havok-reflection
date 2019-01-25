import struct
from .common import any


class hkaSkeletonMapperDataSimpleMapping(object):
    boneA: int
    boneB: int
    aFromBTransform: any

    def __init__(self, infile):
        self.boneA = struct.unpack('>h', infile.read(2))
        self.boneB = struct.unpack('>h', infile.read(2))
        self.aFromBTransform = any(infile)  # TYPE_QSTRANSFORM
