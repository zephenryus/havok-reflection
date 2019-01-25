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
    pathFollowingProperties: any
    currentPath: any
    currentPathFixed: any
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
        self.pathFollowingProperties = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.currentPath = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.currentPathFixed = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.currentPathSegment = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.previousPathSegment = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.newCharacterState = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.changeSegmentDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.tempChangeSegmentDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.updateQuerySize = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterRadiusMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterToPathStartThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useSectionLocalPaths = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pathType = PathType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.lastPointIsGoal = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.needsRepath = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.passiveAvoidance = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.savedCharacterState = State(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} pathFollowingProperties={pathFollowingProperties}, currentPath={currentPath}, currentPathFixed={currentPathFixed}, currentPathSegment={currentPathSegment}, previousPathSegment={previousPathSegment}, newCharacterState={newCharacterState}, changeSegmentDistance={changeSegmentDistance}, tempChangeSegmentDistance={tempChangeSegmentDistance}, updateQuerySize={updateQuerySize}, characterRadiusMultiplier={characterRadiusMultiplier}, characterToPathStartThreshold={characterToPathStartThreshold}, useSectionLocalPaths={useSectionLocalPaths}, pathType={pathType}, lastPointIsGoal={lastPointIsGoal}, needsRepath={needsRepath}, passiveAvoidance={passiveAvoidance}, savedCharacterState={savedCharacterState}>".format(**{
            "class_name": self.__class__.__name__,
            "pathFollowingProperties": self.pathFollowingProperties,
            "currentPath": self.currentPath,
            "currentPathFixed": self.currentPathFixed,
            "currentPathSegment": self.currentPathSegment,
            "previousPathSegment": self.previousPathSegment,
            "newCharacterState": self.newCharacterState,
            "changeSegmentDistance": self.changeSegmentDistance,
            "tempChangeSegmentDistance": self.tempChangeSegmentDistance,
            "updateQuerySize": self.updateQuerySize,
            "characterRadiusMultiplier": self.characterRadiusMultiplier,
            "characterToPathStartThreshold": self.characterToPathStartThreshold,
            "useSectionLocalPaths": self.useSectionLocalPaths,
            "pathType": self.pathType,
            "lastPointIsGoal": self.lastPointIsGoal,
            "needsRepath": self.needsRepath,
            "passiveAvoidance": self.passiveAvoidance,
            "savedCharacterState": self.savedCharacterState,
        })
