from .hkReferencedObject import hkReferencedObject
from .hkpEntity import hkpEntity
from .hkpEntity import hkpEntity
from .hkpSimpleContactConstraintAtom import hkpSimpleContactConstraintAtom
from .hkContactPoint import hkContactPoint
from .hkpSerializedTrack1nInfo import hkpSerializedTrack1nInfo


class hkpSerializedAgentNnEntry(hkReferencedObject):
	bodyA: hkpEntity
	bodyB: hkpEntity
	bodyAId: int
	bodyBId: int
	useEntityIds: bool
	agentType: any
	atom: hkpSimpleContactConstraintAtom
	propertiesStream: any
	contactPoints: hkContactPoint
	cpIdMgr: any
	nnEntryData: int
	trackInfo: hkpSerializedTrack1nInfo
	endianCheckBuffer: int
	version: int
