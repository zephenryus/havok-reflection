from .hkReferencedObject import hkReferencedObject


class hkAlignSceneToNodeOptions(hkReferencedObject):
	invert: bool
	transformPositionX: bool
	transformPositionY: bool
	transformPositionZ: bool
	transformRotation: bool
	transformScale: bool
	transformSkew: bool
	keyframe: int
	nodeName: any
