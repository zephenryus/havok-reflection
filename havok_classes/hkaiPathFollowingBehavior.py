from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
from enum import Enum
from .hkaiPathFollowingProperties import hkaiPathFollowingProperties
from .hkaiPath import hkaiPath
from .enums import PathType, State


class PathType(Enum):
    PATH_TYPE_NAVMESH = 0
    PATH_TYPE_NAVMESH_CLIMBING = 1
    PATH_TYPE_NAVVOLUME = 2


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
    pathType: PathType
    lastPointIsGoal: bool
    needsRepath: bool
    passiveAvoidance: bool
    savedCharacterState: State
