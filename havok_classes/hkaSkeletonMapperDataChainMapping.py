import struct
from .common import any


class hkaSkeletonMapperDataChainMapping(object):
    startBoneA: int
    endBoneA: int
    startBoneB: int
    endBoneB: int
    startAFromBTransform: any
    endAFromBTransform: any

    def __init__(self, infile):
        self.startBoneA = struct.unpack('>h', infile.read(2))
        self.endBoneA = struct.unpack('>h', infile.read(2))
        self.startBoneB = struct.unpack('>h', infile.read(2))
        self.endBoneB = struct.unpack('>h', infile.read(2))
        self.startAFromBTransform = any(infile)  # TYPE_QSTRANSFORM
        self.endAFromBTransform = any(infile)  # TYPE_QSTRANSFORM
