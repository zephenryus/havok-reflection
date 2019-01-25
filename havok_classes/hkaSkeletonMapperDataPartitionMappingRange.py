import struct


class hkaSkeletonMapperDataPartitionMappingRange(object):
    startMappingIndex: int
    numMappings: int

    def __init__(self, infile):
        self.startMappingIndex = struct.unpack('>i', infile.read(4))
        self.numMappings = struct.unpack('>i', infile.read(4))
