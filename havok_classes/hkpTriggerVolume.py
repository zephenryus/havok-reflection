from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpRigidBody import hkpRigidBody
from .hkpTriggerVolumeEventInfo import hkpTriggerVolumeEventInfo
from .common import any


class EventType(Enum):
    ENTERED_EVENT = 1
    LEFT_EVENT = 2
    ENTERED_AND_LEFT_EVENT = 3
    TRIGGER_BODY_LEFT_EVENT = 6


class Operation(Enum):
    ADDED_OP = 0
    REMOVED_OP = 1
    CONTACT_OP = 2
    TOI_OP = 3


class hkpTriggerVolume(hkReferencedObject):
    overlappingBodies: hkpRigidBody
    eventQueue: hkpTriggerVolumeEventInfo
    triggerBody: hkpRigidBody
    sequenceNumber: int
    isProcessingBodyOverlaps: bool
    newOverlappingBodies: any
