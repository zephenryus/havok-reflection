from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
from .hkaiPathFollowingProperties import hkaiPathFollowingProperties
from .hkaiPath import hkaiPath
from .hkaiPath import hkaiPath


class hkaiPathFollowingBehavior(hkaiSingleCharacterBehavior):
	pathFollowingProperties: hkaiPathFollowingProperties
	currentPath: hkaiPath
	currentPathFixed: hkaiPath
	currentPathSegment: int
	previousPathSegment: int
	newCharacterState: int
	changeSegmentDistance: float
	tempChangeSegmentDistance: float
	updateQuerySize: float
	characterRadiusMultiplier: float
	characterToPathStartThreshold: float
	useSectionLocalPaths: bool
	pathType: any
	lastPointIsGoal: bool
	needsRepath: bool
	passiveAvoidance: bool
	savedCharacterState: any
