from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
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
