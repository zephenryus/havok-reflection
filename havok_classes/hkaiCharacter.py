from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .hkaiAdaptiveRanger import hkaiAdaptiveRanger
from .hkaiAstarCostModifier import hkaiAstarCostModifier
from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter
from .hkaiAvoidanceProperties import hkaiAvoidanceProperties
from .enums import State
from typing import List
from .common import get_array


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
    costModifier: any
    edgeFilter: any
    hitFilter: any
    steeringFilter: any
    agentFilterInfo: int
    avoidanceProperties: any
    avoidanceState: float
    agentPriority: int
    avoidanceType: int
    avoidanceEnabledMask: any
    state: State
    behaviorListeners: List[any]
    layer: int

    def __init__(self, infile):
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.position = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.forward = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.velocity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.currentNavMeshFace = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.currentNavVolumeCell = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.desiredSpeed = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.adaptiveRanger = hkaiAdaptiveRanger(infile)  # TYPE_STRUCT:TYPE_VOID
        self.costModifier = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.edgeFilter = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.hitFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.steeringFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.agentFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.avoidanceProperties = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.avoidanceState = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.agentPriority = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.avoidanceType = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.avoidanceEnabledMask = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.state = State(infile)  # TYPE_ENUM:TYPE_INT32
        self.behaviorListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.layer = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} userData={userData}, position={position}, forward={forward}, velocity={velocity}, up={up}, currentNavMeshFace={currentNavMeshFace}, currentNavVolumeCell={currentNavVolumeCell}, radius={radius}, desiredSpeed={desiredSpeed}, adaptiveRanger={adaptiveRanger}, costModifier={costModifier}, edgeFilter={edgeFilter}, hitFilter={hitFilter}, steeringFilter={steeringFilter}, agentFilterInfo={agentFilterInfo}, avoidanceProperties={avoidanceProperties}, avoidanceState={avoidanceState}, agentPriority={agentPriority}, avoidanceType={avoidanceType}, avoidanceEnabledMask={avoidanceEnabledMask}, state={state}, behaviorListeners=[{behaviorListeners}], layer={layer}>".format(**{
            "class_name": self.__class__.__name__,
            "userData": self.userData,
            "position": self.position,
            "forward": self.forward,
            "velocity": self.velocity,
            "up": self.up,
            "currentNavMeshFace": self.currentNavMeshFace,
            "currentNavVolumeCell": self.currentNavVolumeCell,
            "radius": self.radius,
            "desiredSpeed": self.desiredSpeed,
            "adaptiveRanger": self.adaptiveRanger,
            "costModifier": self.costModifier,
            "edgeFilter": self.edgeFilter,
            "hitFilter": self.hitFilter,
            "steeringFilter": self.steeringFilter,
            "agentFilterInfo": self.agentFilterInfo,
            "avoidanceProperties": self.avoidanceProperties,
            "avoidanceState": self.avoidanceState,
            "agentPriority": self.agentPriority,
            "avoidanceType": self.avoidanceType,
            "avoidanceEnabledMask": self.avoidanceEnabledMask,
            "state": self.state,
            "behaviorListeners": self.behaviorListeners,
            "layer": self.layer,
        })
