from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
from .hkaiGateFollowingBehaviorRequestedGoalPoint import hkaiGateFollowingBehaviorRequestedGoalPoint
from .hkaiGatePath import hkaiGatePath
from .hkaiGatePathTraversalState import hkaiGatePathTraversalState
from .hkaiPathFollowingProperties import hkaiPathFollowingProperties
from .enums import State


class hkaiGateFollowingBehavior(hkaiSingleCharacterBehavior):
    updateQuerySize: float
    requestedGoalPoints: hkaiGateFollowingBehaviorRequestedGoalPoint
    gatePath: hkaiGatePath
    traversalState: hkaiGatePathTraversalState
    pathFollowingProperties: hkaiPathFollowingProperties
    newCharacterState: State
    savedCharacterState: State
