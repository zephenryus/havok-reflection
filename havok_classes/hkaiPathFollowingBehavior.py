from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
from enum import Enum
from .hkaiPathFollowingProperties import hkaiPathFollowingProperties
from .hkaiPath import hkaiPath
import struct
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

    def __init__(self, infile):
        self.pathFollowingProperties = hkaiPathFollowingProperties(infile)  # TYPE_POINTER
        self.currentPath = hkaiPath(infile)  # TYPE_POINTER
        self.currentPathFixed = hkaiPath(infile)  # TYPE_POINTER
        self.currentPathSegment = struct.unpack('>i', infile.read(4))
        self.previousPathSegment = struct.unpack('>i', infile.read(4))
        self.newCharacterState = struct.unpack('>i', infile.read(4))
        self.changeSegmentDistance = struct.unpack('>f', infile.read(4))
        self.tempChangeSegmentDistance = struct.unpack('>f', infile.read(4))
        self.updateQuerySize = struct.unpack('>f', infile.read(4))
        self.characterRadiusMultiplier = struct.unpack('>f', infile.read(4))
        self.characterToPathStartThreshold = struct.unpack('>f', infile.read(4))
        self.useSectionLocalPaths = struct.unpack('>?', infile.read(1))
        self.pathType = PathType(infile)  # TYPE_ENUM
        self.lastPointIsGoal = struct.unpack('>?', infile.read(1))
        self.needsRepath = struct.unpack('>?', infile.read(1))
        self.passiveAvoidance = struct.unpack('>?', infile.read(1))
        self.savedCharacterState = State(infile)  # TYPE_ENUM
