import struct


class hkaSkeletonPartition(object):
    name: str
    startBoneIndex: int
    numBones: int

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.startBoneIndex = struct.unpack('>h', infile.read(2))
        self.numBones = struct.unpack('>h', infile.read(2))
