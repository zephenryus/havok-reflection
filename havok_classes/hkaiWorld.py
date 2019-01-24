from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import vector4, any
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkaiNavMeshCutter import hkaiNavMeshCutter
from .hkaiNavMeshClearanceCacheManager import hkaiNavMeshClearanceCacheManager
from .hkaiDynamicNavMeshQueryMediator import hkaiDynamicNavMeshQueryMediator
from .hkaiDynamicNavVolumeMediator import hkaiDynamicNavVolumeMediator
from .hkaiOverlapManager import hkaiOverlapManager
from .hkaiSilhouetteGenerationParameters import hkaiSilhouetteGenerationParameters
from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator
from .hkaiObstacleGenerator import hkaiObstacleGenerator
from .hkaiAvoidancePairProperties import hkaiAvoidancePairProperties
from .hkaiPathfindingUtilFindPathInput import hkaiPathfindingUtilFindPathInput
from .hkaiVolumePathfindingUtilFindPathInput import hkaiVolumePathfindingUtilFindPathInput


class StepThreading(Enum):
    STEP_SINGLE_THREADED = 0
    STEP_MULTI_THREADED = 1


class CharacterCallbackType(Enum):
    CALLBACK_PRECHARACTER_STEP = 0
    CALLBACK_POSTCHARACTER_STEP = 1


class PathType(Enum):
    PATH_TYPE_NAVMESH = 0
    PATH_TYPE_NAVVOLUME = 1


class hkaiWorld(hkReferencedObject):
    up: vector4
    streamingCollection: hkaiStreamingCollection
    cutter: hkaiNavMeshCutter
    clearanceCacheManager: hkaiNavMeshClearanceCacheManager
    performValidationChecks: bool
    dynamicNavMeshMediator: hkaiDynamicNavMeshQueryMediator
    dynamicNavVolumeMediator: hkaiDynamicNavVolumeMediator
    overlapManager: hkaiOverlapManager
    silhouetteGenerationParameters: hkaiSilhouetteGenerationParameters
    silhouetteExtrusion: float
    forceSilhouetteUpdates: bool
    listeners: any
    silhouetteGenerators: hkaiSilhouetteGenerator
    obstacleGenerators: hkaiObstacleGenerator
    avoidancePairProps: hkaiAvoidancePairProperties
    navMeshPathRequests: any
    navVolumePathRequests: any
    isPathRequestArrayLocked: bool
    maxRequestsPerStep: int
    maxEstimatedIterationsPerStep: int
    priorityThreshold: int
    numPathRequestsPerTask: int
    numBehaviorUpdatesPerTask: int
    numCharactersPerAvoidanceTask: int
    maxPathSearchEdgesOut: int
    maxPathSearchPointsOut: int
    defaultPathfindingInput: hkaiPathfindingUtilFindPathInput
    defaultVolumePathfindingInput: hkaiVolumePathfindingUtilFindPathInput
