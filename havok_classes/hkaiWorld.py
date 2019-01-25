from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import vector4, any
import struct
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

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))
        self.streamingCollection = hkaiStreamingCollection(infile)  # TYPE_POINTER
        self.cutter = hkaiNavMeshCutter(infile)  # TYPE_POINTER
        self.clearanceCacheManager = hkaiNavMeshClearanceCacheManager(infile)  # TYPE_POINTER
        self.performValidationChecks = struct.unpack('>?', infile.read(1))
        self.dynamicNavMeshMediator = hkaiDynamicNavMeshQueryMediator(infile)  # TYPE_POINTER
        self.dynamicNavVolumeMediator = hkaiDynamicNavVolumeMediator(infile)  # TYPE_POINTER
        self.overlapManager = hkaiOverlapManager(infile)  # TYPE_POINTER
        self.silhouetteGenerationParameters = hkaiSilhouetteGenerationParameters(infile)  # TYPE_STRUCT
        self.silhouetteExtrusion = struct.unpack('>f', infile.read(4))
        self.forceSilhouetteUpdates = struct.unpack('>?', infile.read(1))
        self.listeners = any(infile)  # TYPE_ARRAY
        self.silhouetteGenerators = hkaiSilhouetteGenerator(infile)  # TYPE_ARRAY
        self.obstacleGenerators = hkaiObstacleGenerator(infile)  # TYPE_ARRAY
        self.avoidancePairProps = hkaiAvoidancePairProperties(infile)  # TYPE_POINTER
        self.navMeshPathRequests = any(infile)  # TYPE_ARRAY
        self.navVolumePathRequests = any(infile)  # TYPE_ARRAY
        self.isPathRequestArrayLocked = struct.unpack('>?', infile.read(1))
        self.maxRequestsPerStep = struct.unpack('>i', infile.read(4))
        self.maxEstimatedIterationsPerStep = struct.unpack('>i', infile.read(4))
        self.priorityThreshold = struct.unpack('>i', infile.read(4))
        self.numPathRequestsPerTask = struct.unpack('>i', infile.read(4))
        self.numBehaviorUpdatesPerTask = struct.unpack('>i', infile.read(4))
        self.numCharactersPerAvoidanceTask = struct.unpack('>i', infile.read(4))
        self.maxPathSearchEdgesOut = struct.unpack('>i', infile.read(4))
        self.maxPathSearchPointsOut = struct.unpack('>i', infile.read(4))
        self.defaultPathfindingInput = hkaiPathfindingUtilFindPathInput(infile)  # TYPE_STRUCT
        self.defaultVolumePathfindingInput = hkaiVolumePathfindingUtilFindPathInput(infile)  # TYPE_STRUCT
