from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
import struct
from .hkaiEdgePath import hkaiEdgePath
from .hkaiEdgePathTraversalState import hkaiEdgePathTraversalState
from .enums import State
from .hkaiPathFollowingProperties import hkaiPathFollowingProperties
from .hkaiPathPathPoint import hkaiPathPathPoint
from .hkaiEdgeFollowingBehaviorCornerPredictorInitInfo import hkaiEdgeFollowingBehaviorCornerPredictorInitInfo


class hkaiEdgeFollowingBehavior(hkaiSingleCharacterBehavior):
    updateQuerySize: float
    characterRadiusMultiplier: float
    maxIgnoredHeight: float
    edgePath: hkaiEdgePath
    traversalState: hkaiEdgePathTraversalState
    newCharacterState: State
    pathFollowingProperties: hkaiPathFollowingProperties
    highestUserEdgeNotified: int
    userEdgeFakePathPoint: hkaiPathPathPoint
    savedCharacterState: State
    cornerPredictorInitInfo: hkaiEdgeFollowingBehaviorCornerPredictorInitInfo
    passiveAvoidance: bool

    def __init__(self, infile):
        self.updateQuerySize = struct.unpack('>f', infile.read(4))
        self.characterRadiusMultiplier = struct.unpack('>f', infile.read(4))
        self.maxIgnoredHeight = struct.unpack('>f', infile.read(4))
        self.edgePath = hkaiEdgePath(infile)  # TYPE_POINTER
        self.traversalState = hkaiEdgePathTraversalState(infile)  # TYPE_STRUCT
        self.newCharacterState = State(infile)  # TYPE_ENUM
        self.pathFollowingProperties = hkaiPathFollowingProperties(infile)  # TYPE_POINTER
        self.highestUserEdgeNotified = struct.unpack('>i', infile.read(4))
        self.userEdgeFakePathPoint = hkaiPathPathPoint(infile)  # TYPE_STRUCT
        self.savedCharacterState = State(infile)  # TYPE_ENUM
        self.cornerPredictorInitInfo = hkaiEdgeFollowingBehaviorCornerPredictorInitInfo(infile)  # TYPE_STRUCT
        self.passiveAvoidance = struct.unpack('>?', infile.read(1))
