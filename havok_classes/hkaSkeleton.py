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
