from .hkReferencedObject import hkReferencedObject
from .hkaiPathfindingUtilFindPathInput import hkaiPathfindingUtilFindPathInput
from .hkaiPathfindingUtilFindPathOutput import hkaiPathfindingUtilFindPathOutput


class hkaiNavMeshPathRequestInfo(hkReferencedObject):
	input: hkaiPathfindingUtilFindPathInput
	output: hkaiPathfindingUtilFindPathOutput
	priority: int
	owner: any
	markedForDeletion: bool
