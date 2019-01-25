from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkpRigidBody import hkpRigidBody
from .hkpTriggerVolumeEventInfo import hkpTriggerVolumeEventInfo
import struct


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
    overlappingBodies: List[hkpRigidBody]
    eventQueue: List[hkpTriggerVolumeEventInfo]
    triggerBody: any
    sequenceNumber: int
    isProcessingBodyOverlaps: bool
    newOverlappingBodies: List[any]

    def __init__(self, infile):
        self.overlappingBodies = get_array(infile, hkpRigidBody, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.eventQueue = get_array(infile, hkpTriggerVolumeEventInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.triggerBody = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.sequenceNumber = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.isProcessingBodyOverlaps = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.newOverlappingBodies = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} overlappingBodies=[{overlappingBodies}], eventQueue=[{eventQueue}], triggerBody={triggerBody}, sequenceNumber={sequenceNumber}, isProcessingBodyOverlaps={isProcessingBodyOverlaps}, newOverlappingBodies=[{newOverlappingBodies}]>".format(**{
            "class_name": self.__class__.__name__,
            "overlappingBodies": self.overlappingBodies,
            "eventQueue": self.eventQueue,
            "triggerBody": self.triggerBody,
            "sequenceNumber": self.sequenceNumber,
            "isProcessingBodyOverlaps": self.isProcessingBodyOverlaps,
            "newOverlappingBodies": self.newOverlappingBodies,
        })
