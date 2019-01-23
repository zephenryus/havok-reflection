from .hkReferencedObject import hkReferencedObject
from .hkaAnimation import hkaAnimation


class hkaAnimationBinding(hkReferencedObject):
	originalSkeletonName: any
	animation: hkaAnimation
	transformTrackToBoneIndices: any
	floatTrackToFloatSlotIndices: any
	partitionIndices: any
	blendHint: any
