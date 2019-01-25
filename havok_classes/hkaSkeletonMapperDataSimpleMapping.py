import struct


class hkaSkeletonMapperDataSimpleMapping(object):
    boneA: int
    boneB: int
    aFromBTransform: any

    def __init__(self, infile):
        self.boneA = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.boneB = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.aFromBTransform = any(infile)  # TYPE_QSTRANSFORM:TYPE_VOID

    def __repr__(self):
        return "<{class_name} boneA={boneA}, boneB={boneB}, aFromBTransform={aFromBTransform}>".format(**{
            "class_name": self.__class__.__name__,
            "boneA": self.boneA,
            "boneB": self.boneB,
            "aFromBTransform": self.aFromBTransform,
        })
