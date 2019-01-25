import struct


class hkaSkeletonMapperDataPartitionMappingRange(object):
    startMappingIndex: int
    numMappings: int

    def __init__(self, infile):
        self.startMappingIndex = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numMappings = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startMappingIndex={startMappingIndex}, numMappings={numMappings}>".format(**{
            "class_name": self.__class__.__name__,
            "startMappingIndex": self.startMappingIndex,
            "numMappings": self.numMappings,
        })
