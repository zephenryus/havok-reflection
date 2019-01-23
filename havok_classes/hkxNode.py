from .hkxAttributeHolder import hkxAttributeHolder
from .hkUuid import hkUuid
from .hkReferencedObject import hkReferencedObject
from .hkxNode import hkxNode
from .hkxNodeAnnotationData import hkxNodeAnnotationData


class hkxNode(hkxAttributeHolder):
	name: any
	uuid: hkUuid
	object: hkReferencedObject
	keyFrames: any
	children: hkxNode
	annotations: hkxNodeAnnotationData
	linearKeyFrameHints: any
	userProperties: any
	selected: bool
	bone: bool
