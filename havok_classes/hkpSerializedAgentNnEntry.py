from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpEntity import hkpEntity
from .enums import SerializedAgentType
from .hkpSimpleContactConstraintAtom import hkpSimpleContactConstraintAtom
from .common import any
from .hkContactPoint import hkContactPoint
from .hkpSerializedTrack1nInfo import hkpSerializedTrack1nInfo


class SerializedAgentType(Enum):
    INVALID_AGENT_TYPE = 0
    BOX_BOX_AGENT3 = 1
    CAPSULE_TRIANGLE_AGENT3 = 2
    PRED_GSK_AGENT3 = 3
    PRED_GSK_CYLINDER_AGENT3 = 4
    CONVEX_LIST_AGENT3 = 5
    LIST_AGENT3 = 6
    BV_TREE_AGENT3 = 7
    COLLECTION_COLLECTION_AGENT3 = 8
    COLLECTION_AGENT3 = 9


class hkpSerializedAgentNnEntry(hkReferencedObject):
    bodyA: hkpEntity
    bodyB: hkpEntity
    bodyAId: int
    bodyBId: int
    useEntityIds: bool
    agentType: SerializedAgentType
    atom: hkpSimpleContactConstraintAtom
    propertiesStream: any
    contactPoints: hkContactPoint
    cpIdMgr: any
    nnEntryData: int
    trackInfo: hkpSerializedTrack1nInfo
    endianCheckBuffer: int
    version: int
