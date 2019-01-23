from .hkReferencedObject import hkReferencedObject
from .hkaAnimatedReferenceFrame import hkaAnimatedReferenceFrame
from .hkaAnnotationTrack import hkaAnnotationTrack


class hkaAnimation(hkReferencedObject):
	type: any
	duration: float
	numberOfTransformTracks: int
	numberOfFloatTracks: int
	extractedMotion: hkaAnimatedReferenceFrame
	annotationTracks: hkaAnnotationTrack
