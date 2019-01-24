from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import vector4, any
from .hkaiAdaptiveRanger import hkaiAdaptiveRanger
from .hkaiAstarCostModifier import hkaiAstarCostModifier
from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter
from .hkaiAvoidanceProperties import hkaiAvoidanceProperties
from .enums import State


class State(Enum):
    STATE_NEEDS_NEW_PATH = 0
    STATE_FOLLOWING_PATH = 1
    STATE_SLOWING_TO_GOAL = 2
    STATE_GOAL_REACHED = 3
    STATE_PATH_FAILED = 4
    STATE_WANDERED_OFF_PATH = 5
    STATE_REPATHING_INCOMPLETE_PATH = 6
    STATE_MANUAL_CONTROL = 7


class AvoidanceEnabledMaskBits(Enum):
    AVOID_BOUNDARIES = 1
    AVOID_CHARACTERS = 2
    AVOID_OBSTACLES = 4
    AVOID_NONE = 0
    AVOID_ALL = 7


class AvoidanceState(Enum):
    AVOIDANCE_SUCCESS = 0
    AVOIDANCE_FAILURE = 1


class hkaiCharacter(hkReferencedObject):
    userData: int
    position: vector4
    forward: vector4
    velocity: vector4
    up: vector4
    currentNavMeshFace: int
    currentNavVolumeCell: int
    radius: float
    desiredSpeed: float
    adaptiveRanger: hkaiAdaptiveRanger
    costModifier: hkaiAstarCostModifier
    edgeFilter: hkaiAstarEdgeFilter
    hitFilter: any
    steeringFilter: any
    agentFilterInfo: int
    avoidanceProperties: hkaiAvoidanceProperties
    avoidanceState: float
    agentPriority: int
    avoidanceType: int
    avoidanceEnabledMask: any
    state: State
    behaviorListeners: any
    layer: int
