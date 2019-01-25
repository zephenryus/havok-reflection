import struct


class hkaSkeletonMapperDataChainMapping(object):
    startBoneA: int
    endBoneA: int
    startBoneB: int
    endBoneB: int
    startAFromBTransform: any
    endAFromBTransform: any

    def __init__(self, infile):
        self.startBoneA = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.endBoneA = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.startBoneB = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.endBoneB = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.startAFromBTransform = any(infile)  # TYPE_QSTRANSFORM:TYPE_VOID
        self.endAFromBTransform = any(infile)  # TYPE_QSTRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startBoneA={startBoneA}, endBoneA={endBoneA}, startBoneB={startBoneB}, endBoneB={endBoneB}, startAFromBTransform={startAFromBTransform}, endAFromBTransform={endAFromBTransform}>".format(**{
            "class_name": self.__class__.__name__,
            "startBoneA": self.startBoneA,
            "endBoneA": self.endBoneA,
            "startBoneB": self.startBoneB,
            "endBoneB": self.endBoneB,
            "startAFromBTransform": self.startAFromBTransform,
            "endAFromBTransform": self.endAFromBTransform,
        })
