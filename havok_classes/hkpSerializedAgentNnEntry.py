from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpEntity import hkpEntity
import struct
from .enums import SerializedAgentType
from .hkpSimpleContactConstraintAtom import hkpSimpleContactConstraintAtom
from typing import List
from .common import get_array
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
    bodyA: any
    bodyB: any
    bodyAId: int
    bodyBId: int
    useEntityIds: bool
    agentType: SerializedAgentType
    atom: hkpSimpleContactConstraintAtom
    propertiesStream: List[int]
    contactPoints: List[hkContactPoint]
    cpIdMgr: List[int]
    nnEntryData: int
    trackInfo: hkpSerializedTrack1nInfo
    endianCheckBuffer: int
    version: int

    def __init__(self, infile):
        self.bodyA = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.bodyB = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.bodyAId = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.bodyBId = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.useEntityIds = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.agentType = SerializedAgentType(infile)  # TYPE_ENUM:TYPE_INT8
        self.atom = hkpSimpleContactConstraintAtom(infile)  # TYPE_STRUCT:TYPE_VOID
        self.propertiesStream = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.contactPoints = get_array(infile, hkContactPoint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.cpIdMgr = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.nnEntryData = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.trackInfo = hkpSerializedTrack1nInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.endianCheckBuffer = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.version = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bodyA={bodyA}, bodyB={bodyB}, bodyAId={bodyAId}, bodyBId={bodyBId}, useEntityIds={useEntityIds}, agentType={agentType}, atom={atom}, propertiesStream=[{propertiesStream}], contactPoints=[{contactPoints}], cpIdMgr=[{cpIdMgr}], nnEntryData={nnEntryData}, trackInfo={trackInfo}, endianCheckBuffer={endianCheckBuffer}, version={version}>".format(**{
            "class_name": self.__class__.__name__,
            "bodyA": self.bodyA,
            "bodyB": self.bodyB,
            "bodyAId": self.bodyAId,
            "bodyBId": self.bodyBId,
            "useEntityIds": self.useEntityIds,
            "agentType": self.agentType,
            "atom": self.atom,
            "propertiesStream": self.propertiesStream,
            "contactPoints": self.contactPoints,
            "cpIdMgr": self.cpIdMgr,
            "nnEntryData": self.nnEntryData,
            "trackInfo": self.trackInfo,
            "endianCheckBuffer": self.endianCheckBuffer,
            "version": self.version,
        })
