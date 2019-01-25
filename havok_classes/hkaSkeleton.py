from .hkReferencedObject import hkReferencedObject
from .common import any
from .hkaBone import hkaBone
from .hkaSkeletonLocalFrameOnBone import hkaSkeletonLocalFrameOnBone
from .hkaSkeletonPartition import hkaSkeletonPartition


class hkaSkeleton(hkReferencedObject):
    name: str
    parentIndices: any
    bones: hkaBone
    referencePose: any
    referenceFloats: any
    floatSlots: any
    localFrames: hkaSkeletonLocalFrameOnBone
    partitions: hkaSkeletonPartition

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.parentIndices = any(infile)  # TYPE_ARRAY
        self.bones = hkaBone(infile)  # TYPE_ARRAY
        self.referencePose = any(infile)  # TYPE_ARRAY
        self.referenceFloats = any(infile)  # TYPE_ARRAY
        self.floatSlots = any(infile)  # TYPE_ARRAY
        self.localFrames = hkaSkeletonLocalFrameOnBone(infile)  # TYPE_ARRAY
        self.partitions = hkaSkeletonPartition(infile)  # TYPE_ARRAY
