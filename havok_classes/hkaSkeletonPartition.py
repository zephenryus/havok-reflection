import struct


class hkaSkeletonPartition(object):
    name: str
    startBoneIndex: int
    numBones: int

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.startBoneIndex = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.numBones = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", startBoneIndex={startBoneIndex}, numBones={numBones}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "startBoneIndex": self.startBoneIndex,
            "numBones": self.numBones,
        })
