from .hkReferencedObject import hkReferencedObject
from .hkaBone import hkaBone
from .hkaSkeletonLocalFrameOnBone import hkaSkeletonLocalFrameOnBone
from .hkaSkeletonPartition import hkaSkeletonPartition


class hkaSkeleton(hkReferencedObject):
	name: any
	parentIndices: any
	bones: hkaBone
	referencePose: any
	referenceFloats: any
	floatSlots: any
	localFrames: hkaSkeletonLocalFrameOnBone
	partitions: hkaSkeletonPartition
