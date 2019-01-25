from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
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

    def __init__(self, infile):
        self.userData = struct.unpack('>L', infile.read(8))
        self.position = struct.unpack('>4f', infile.read(16))
        self.forward = struct.unpack('>4f', infile.read(16))
        self.velocity = struct.unpack('>4f', infile.read(16))
        self.up = struct.unpack('>4f', infile.read(16))
        self.currentNavMeshFace = struct.unpack('>I', infile.read(4))
        self.currentNavVolumeCell = struct.unpack('>I', infile.read(4))
        self.radius = struct.unpack('>f', infile.read(4))
        self.desiredSpeed = struct.unpack('>f', infile.read(4))
        self.adaptiveRanger = hkaiAdaptiveRanger(infile)  # TYPE_STRUCT
        self.costModifier = hkaiAstarCostModifier(infile)  # TYPE_POINTER
        self.edgeFilter = hkaiAstarEdgeFilter(infile)  # TYPE_POINTER
        self.hitFilter = any(infile)  # TYPE_POINTER
        self.steeringFilter = any(infile)  # TYPE_POINTER
        self.agentFilterInfo = struct.unpack('>I', infile.read(4))
        self.avoidanceProperties = hkaiAvoidanceProperties(infile)  # TYPE_POINTER
        self.avoidanceState = struct.unpack('>f', infile.read(4))
        self.agentPriority = struct.unpack('>I', infile.read(4))
        self.avoidanceType = struct.unpack('>H', infile.read(2))
        self.avoidanceEnabledMask = any(infile)  # TYPE_FLAGS
        self.state = State(infile)  # TYPE_ENUM
        self.behaviorListeners = any(infile)  # TYPE_ARRAY
        self.layer = struct.unpack('>I', infile.read(4))
