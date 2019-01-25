from .hkLocalFrame import hkLocalFrame
import struct


class hkaSkeletonLocalFrameOnBone(object):
    localFrame: any
    boneIndex: int

    def __init__(self, infile):
        self.localFrame = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.boneIndex = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localFrame={localFrame}, boneIndex={boneIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "localFrame": self.localFrame,
            "boneIndex": self.boneIndex,
        })
