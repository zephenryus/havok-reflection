from .hkReferencedObject import hkReferencedObject
from .hkpRigidBody import hkpRigidBody
from .hkpTriggerVolumeEventInfo import hkpTriggerVolumeEventInfo
from .hkpRigidBody import hkpRigidBody


class hkpTriggerVolume(hkReferencedObject):
	overlappingBodies: hkpRigidBody
	eventQueue: hkpTriggerVolumeEventInfo
	triggerBody: hkpRigidBody
	sequenceNumber: int
	isProcessingBodyOverlaps: bool
	newOverlappingBodies: any
