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
    edgePath: any
    traversalState: hkaiEdgePathTraversalState
    newCharacterState: State
    pathFollowingProperties: any
    highestUserEdgeNotified: int
    userEdgeFakePathPoint: hkaiPathPathPoint
    savedCharacterState: State
    cornerPredictorInitInfo: hkaiEdgeFollowingBehaviorCornerPredictorInitInfo
    passiveAvoidance: bool

    def __init__(self, infile):
        self.updateQuerySize = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.characterRadiusMultiplier = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxIgnoredHeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.edgePath = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.traversalState = hkaiEdgePathTraversalState(infile)  # TYPE_STRUCT:TYPE_VOID
        self.newCharacterState = State(infile)  # TYPE_ENUM:TYPE_INT32
        self.pathFollowingProperties = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.highestUserEdgeNotified = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.userEdgeFakePathPoint = hkaiPathPathPoint(infile)  # TYPE_STRUCT:TYPE_VOID
        self.savedCharacterState = State(infile)  # TYPE_ENUM:TYPE_INT32
        self.cornerPredictorInitInfo = hkaiEdgeFollowingBehaviorCornerPredictorInitInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.passiveAvoidance = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} updateQuerySize={updateQuerySize}, characterRadiusMultiplier={characterRadiusMultiplier}, maxIgnoredHeight={maxIgnoredHeight}, edgePath={edgePath}, traversalState={traversalState}, newCharacterState={newCharacterState}, pathFollowingProperties={pathFollowingProperties}, highestUserEdgeNotified={highestUserEdgeNotified}, userEdgeFakePathPoint={userEdgeFakePathPoint}, savedCharacterState={savedCharacterState}, cornerPredictorInitInfo={cornerPredictorInitInfo}, passiveAvoidance={passiveAvoidance}>".format(**{
            "class_name": self.__class__.__name__,
            "updateQuerySize": self.updateQuerySize,
            "characterRadiusMultiplier": self.characterRadiusMultiplier,
            "maxIgnoredHeight": self.maxIgnoredHeight,
            "edgePath": self.edgePath,
            "traversalState": self.traversalState,
            "newCharacterState": self.newCharacterState,
            "pathFollowingProperties": self.pathFollowingProperties,
            "highestUserEdgeNotified": self.highestUserEdgeNotified,
            "userEdgeFakePathPoint": self.userEdgeFakePathPoint,
            "savedCharacterState": self.savedCharacterState,
            "cornerPredictorInitInfo": self.cornerPredictorInitInfo,
            "passiveAvoidance": self.passiveAvoidance,
        })
