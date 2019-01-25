from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkaiNavMeshCutter import hkaiNavMeshCutter
from .hkaiNavMeshClearanceCacheManager import hkaiNavMeshClearanceCacheManager
from .hkaiDynamicNavMeshQueryMediator import hkaiDynamicNavMeshQueryMediator
from .hkaiDynamicNavVolumeMediator import hkaiDynamicNavVolumeMediator
from .hkaiOverlapManager import hkaiOverlapManager
from .hkaiSilhouetteGenerationParameters import hkaiSilhouetteGenerationParameters
from typing import List
from .common import get_array
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
    streamingCollection: any
    cutter: any
    clearanceCacheManager: any
    performValidationChecks: bool
    dynamicNavMeshMediator: any
    dynamicNavVolumeMediator: any
    overlapManager: any
    silhouetteGenerationParameters: hkaiSilhouetteGenerationParameters
    silhouetteExtrusion: float
    forceSilhouetteUpdates: bool
    listeners: List[any]
    silhouetteGenerators: List[hkaiSilhouetteGenerator]
    obstacleGenerators: List[hkaiObstacleGenerator]
    avoidancePairProps: any
    navMeshPathRequests: List[any]
    navVolumePathRequests: List[any]
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
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.streamingCollection = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.cutter = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.clearanceCacheManager = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.performValidationChecks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.dynamicNavMeshMediator = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.dynamicNavVolumeMediator = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.overlapManager = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.silhouetteGenerationParameters = hkaiSilhouetteGenerationParameters(infile)  # TYPE_STRUCT:TYPE_VOID
        self.silhouetteExtrusion = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.forceSilhouetteUpdates = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.listeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.silhouetteGenerators = get_array(infile, hkaiSilhouetteGenerator, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.obstacleGenerators = get_array(infile, hkaiObstacleGenerator, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.avoidancePairProps = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.navMeshPathRequests = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_VOID
        self.navVolumePathRequests = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_VOID
        self.isPathRequestArrayLocked = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.maxRequestsPerStep = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxEstimatedIterationsPerStep = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.priorityThreshold = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numPathRequestsPerTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numBehaviorUpdatesPerTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numCharactersPerAvoidanceTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxPathSearchEdgesOut = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxPathSearchPointsOut = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.defaultPathfindingInput = hkaiPathfindingUtilFindPathInput(infile)  # TYPE_STRUCT:TYPE_VOID
        self.defaultVolumePathfindingInput = hkaiVolumePathfindingUtilFindPathInput(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} up={up}, streamingCollection={streamingCollection}, cutter={cutter}, clearanceCacheManager={clearanceCacheManager}, performValidationChecks={performValidationChecks}, dynamicNavMeshMediator={dynamicNavMeshMediator}, dynamicNavVolumeMediator={dynamicNavVolumeMediator}, overlapManager={overlapManager}, silhouetteGenerationParameters={silhouetteGenerationParameters}, silhouetteExtrusion={silhouetteExtrusion}, forceSilhouetteUpdates={forceSilhouetteUpdates}, listeners=[{listeners}], silhouetteGenerators=[{silhouetteGenerators}], obstacleGenerators=[{obstacleGenerators}], avoidancePairProps={avoidancePairProps}, navMeshPathRequests=[{navMeshPathRequests}], navVolumePathRequests=[{navVolumePathRequests}], isPathRequestArrayLocked={isPathRequestArrayLocked}, maxRequestsPerStep={maxRequestsPerStep}, maxEstimatedIterationsPerStep={maxEstimatedIterationsPerStep}, priorityThreshold={priorityThreshold}, numPathRequestsPerTask={numPathRequestsPerTask}, numBehaviorUpdatesPerTask={numBehaviorUpdatesPerTask}, numCharactersPerAvoidanceTask={numCharactersPerAvoidanceTask}, maxPathSearchEdgesOut={maxPathSearchEdgesOut}, maxPathSearchPointsOut={maxPathSearchPointsOut}, defaultPathfindingInput={defaultPathfindingInput}, defaultVolumePathfindingInput={defaultVolumePathfindingInput}>".format(**{
            "class_name": self.__class__.__name__,
            "up": self.up,
            "streamingCollection": self.streamingCollection,
            "cutter": self.cutter,
            "clearanceCacheManager": self.clearanceCacheManager,
            "performValidationChecks": self.performValidationChecks,
            "dynamicNavMeshMediator": self.dynamicNavMeshMediator,
            "dynamicNavVolumeMediator": self.dynamicNavVolumeMediator,
            "overlapManager": self.overlapManager,
            "silhouetteGenerationParameters": self.silhouetteGenerationParameters,
            "silhouetteExtrusion": self.silhouetteExtrusion,
            "forceSilhouetteUpdates": self.forceSilhouetteUpdates,
            "listeners": self.listeners,
            "silhouetteGenerators": self.silhouetteGenerators,
            "obstacleGenerators": self.obstacleGenerators,
            "avoidancePairProps": self.avoidancePairProps,
            "navMeshPathRequests": self.navMeshPathRequests,
            "navVolumePathRequests": self.navVolumePathRequests,
            "isPathRequestArrayLocked": self.isPathRequestArrayLocked,
            "maxRequestsPerStep": self.maxRequestsPerStep,
            "maxEstimatedIterationsPerStep": self.maxEstimatedIterationsPerStep,
            "priorityThreshold": self.priorityThreshold,
            "numPathRequestsPerTask": self.numPathRequestsPerTask,
            "numBehaviorUpdatesPerTask": self.numBehaviorUpdatesPerTask,
            "numCharactersPerAvoidanceTask": self.numCharactersPerAvoidanceTask,
            "maxPathSearchEdgesOut": self.maxPathSearchEdgesOut,
            "maxPathSearchPointsOut": self.maxPathSearchPointsOut,
            "defaultPathfindingInput": self.defaultPathfindingInput,
            "defaultVolumePathfindingInput": self.defaultVolumePathfindingInput,
        })
