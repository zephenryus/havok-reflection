from .hkLocalFrame import hkLocalFrame
import struct


class hkaSkeletonLocalFrameOnBone(object):
    localFrame: hkLocalFrame
    boneIndex: int

    def __init__(self, infile):
        self.localFrame = hkLocalFrame(infile)  # TYPE_POINTER
        self.boneIndex = struct.unpack('>h', infile.read(2))
