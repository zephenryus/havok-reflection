from .hkaiSingleCharacterBehavior import hkaiSingleCharacterBehavior
import struct
from typing import List
from .common import get_array
from .hkaiGateFollowingBehaviorRequestedGoalPoint import hkaiGateFollowingBehaviorRequestedGoalPoint
from .hkaiGatePath import hkaiGatePath
from .hkaiGatePathTraversalState import hkaiGatePathTraversalState
from .hkaiPathFollowingProperties import hkaiPathFollowingProperties
from .enums import State


class hkaiGateFollowingBehavior(hkaiSingleCharacterBehavior):
    updateQuerySize: float
    requestedGoalPoints: List[hkaiGateFollowingBehaviorRequestedGoalPoint]
    gatePath: any
    traversalState: hkaiGatePathTraversalState
    pathFollowingProperties: any
    newCharacterState: State
    savedCharacterState: State

    def __init__(self, infile):
        self.updateQuerySize = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.requestedGoalPoints = get_array(infile, hkaiGateFollowingBehaviorRequestedGoalPoint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.gatePath = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.traversalState = hkaiGatePathTraversalState(infile)  # TYPE_STRUCT:TYPE_VOID
        self.pathFollowingProperties = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.newCharacterState = State(infile)  # TYPE_ENUM:TYPE_UINT8
        self.savedCharacterState = State(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} updateQuerySize={updateQuerySize}, requestedGoalPoints=[{requestedGoalPoints}], gatePath={gatePath}, traversalState={traversalState}, pathFollowingProperties={pathFollowingProperties}, newCharacterState={newCharacterState}, savedCharacterState={savedCharacterState}>".format(**{
            "class_name": self.__class__.__name__,
            "updateQuerySize": self.updateQuerySize,
            "requestedGoalPoints": self.requestedGoalPoints,
            "gatePath": self.gatePath,
            "traversalState": self.traversalState,
            "pathFollowingProperties": self.pathFollowingProperties,
            "newCharacterState": self.newCharacterState,
            "savedCharacterState": self.savedCharacterState,
        })
