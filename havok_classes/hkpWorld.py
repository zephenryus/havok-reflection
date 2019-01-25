from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpSimulation import hkpSimulation
from .common import vector4, any
import struct
from .hkpRigidBody import hkpRigidBody
from .hkMultiThreadCheck import hkMultiThreadCheck
from .hkpPhantom import hkpPhantom


class ReintegrationRecollideMode(Enum):
    RR_MODE_REINTEGRATE = 1
    RR_MODE_RECOLLIDE_BROADPHASE = 2
    RR_MODE_RECOLLIDE_NARROWPHASE = 4
    RR_MODE_ALL = 7


class MtAccessChecking(Enum):
    MT_ACCESS_CHECKING_ENABLED = 0
    MT_ACCESS_CHECKING_DISABLED = 1


class CachedAabbUpdate(Enum):
    SHIFT_BROADPHASE_UPDATE_ENTITY_AABBS = 0
    SHIFT_BROADPHASE_IGNORE_ENTITY_AABBS = 1


class hkpWorld(hkReferencedObject):
    simulation: hkpSimulation
    gravity: vector4
    fixedIsland: any
    fixedRigidBody: hkpRigidBody
    activeSimulationIslands: any
    inactiveSimulationIslands: any
    dirtySimulationIslands: any
    maintenanceMgr: any
    memoryWatchDog: any
    assertOnRunningOutOfSolverMemory: bool
    broadPhaseType: enumerate
    broadPhase: any
    broadPhaseDispatcher: any
    phantomBroadPhaseListener: any
    entityEntityBroadPhaseListener: any
    broadPhaseBorderListener: any
    multithreadedSimulationJobData: any
    collisionInput: any
    collisionFilter: any
    collisionDispatcher: any
    convexListFilter: any
    pendingOperations: any
    pendingOperationsCount: int
    pendingBodyOperationsCount: int
    criticalOperationsLockCount: int
    criticalOperationsLockCountForPhantoms: int
    blockExecutingPendingOperations: bool
    criticalOperationsAllowed: bool
    pendingOperationQueues: any
    pendingOperationQueueCount: int
    multiThreadCheck: hkMultiThreadCheck
    processActionsInSingleThread: bool
    allowIntegrationOfIslandsWithoutConstraintsInASeparateJob: bool
    minDesiredIslandSize: int
    modifyConstraintCriticalSection: any
    isLocked: int
    islandDirtyListCriticalSection: any
    propertyMasterLock: any
    wantSimulationIslands: bool
    snapCollisionToConvexEdgeThreshold: float
    snapCollisionToConcaveEdgeThreshold: float
    enableToiWeldRejection: bool
    wantDeactivation: bool
    shouldActivateOnRigidBodyTransformChange: bool
    deactivationReferenceDistance: float
    toiCollisionResponseRotateNormal: float
    maxSectorsPerMidphaseCollideTask: int
    maxSectorsPerNarrowphaseCollideTask: int
    processToisMultithreaded: bool
    maxEntriesPerToiMidphaseCollideTask: int
    maxEntriesPerToiNarrowphaseCollideTask: int
    maxNumToiCollisionPairsSinglethreaded: int
    simulationType: enumerate
    numToisTillAllowedPenetrationSimplifiedToi: float
    numToisTillAllowedPenetrationToi: float
    numToisTillAllowedPenetrationToiHigher: float
    numToisTillAllowedPenetrationToiForced: float
    lastEntityUid: int
    lastIslandUid: int
    lastConstraintUid: int
    phantoms: hkpPhantom
    actionListeners: any
    entityListeners: any
    phantomListeners: any
    constraintListeners: any
    worldDeletionListeners: any
    islandActivationListeners: any
    worldPostSimulationListeners: any
    worldPostIntegrateListeners: any
    worldPostCollideListeners: any
    islandPostIntegrateListeners: any
    islandPostCollideListeners: any
    contactListeners: any
    contactImpulseLimitBreachedListeners: any
    worldExtensions: any
    violatedConstraintArray: any
    broadPhaseBorder: any
    destructionWorld: any
    npWorld: any
    broadPhaseExtents: vector4
    broadPhaseNumMarkers: int
    sizeOfToiEventQueue: int
    broadPhaseQuerySize: int
    broadPhaseUpdateSize: int
    contactPointGeneration: enumerate
    useCompoundSpuElf: bool

    def __init__(self, infile):
        self.simulation = hkpSimulation(infile)  # TYPE_POINTER
        self.gravity = struct.unpack('>4f', infile.read(16))
        self.fixedIsland = any(infile)  # TYPE_POINTER
        self.fixedRigidBody = hkpRigidBody(infile)  # TYPE_POINTER
        self.activeSimulationIslands = any(infile)  # TYPE_ARRAY
        self.inactiveSimulationIslands = any(infile)  # TYPE_ARRAY
        self.dirtySimulationIslands = any(infile)  # TYPE_ARRAY
        self.maintenanceMgr = any(infile)  # TYPE_POINTER
        self.memoryWatchDog = any(infile)  # TYPE_POINTER
        self.assertOnRunningOutOfSolverMemory = struct.unpack('>?', infile.read(1))
        self.broadPhaseType = enumerate(infile)  # TYPE_ENUM
        self.broadPhase = any(infile)  # TYPE_POINTER
        self.broadPhaseDispatcher = any(infile)  # TYPE_POINTER
        self.phantomBroadPhaseListener = any(infile)  # TYPE_POINTER
        self.entityEntityBroadPhaseListener = any(infile)  # TYPE_POINTER
        self.broadPhaseBorderListener = any(infile)  # TYPE_POINTER
        self.multithreadedSimulationJobData = any(infile)  # TYPE_POINTER
        self.collisionInput = any(infile)  # TYPE_POINTER
        self.collisionFilter = any(infile)  # TYPE_POINTER
        self.collisionDispatcher = any(infile)  # TYPE_POINTER
        self.convexListFilter = any(infile)  # TYPE_POINTER
        self.pendingOperations = any(infile)  # TYPE_POINTER
        self.pendingOperationsCount = struct.unpack('>i', infile.read(4))
        self.pendingBodyOperationsCount = struct.unpack('>i', infile.read(4))
        self.criticalOperationsLockCount = struct.unpack('>i', infile.read(4))
        self.criticalOperationsLockCountForPhantoms = struct.unpack('>i', infile.read(4))
        self.blockExecutingPendingOperations = struct.unpack('>?', infile.read(1))
        self.criticalOperationsAllowed = struct.unpack('>?', infile.read(1))
        self.pendingOperationQueues = any(infile)  # TYPE_POINTER
        self.pendingOperationQueueCount = struct.unpack('>i', infile.read(4))
        self.multiThreadCheck = hkMultiThreadCheck(infile)  # TYPE_STRUCT
        self.processActionsInSingleThread = struct.unpack('>?', infile.read(1))
        self.allowIntegrationOfIslandsWithoutConstraintsInASeparateJob = struct.unpack('>?', infile.read(1))
        self.minDesiredIslandSize = struct.unpack('>I', infile.read(4))
        self.modifyConstraintCriticalSection = any(infile)  # TYPE_POINTER
        self.isLocked = struct.unpack('>i', infile.read(4))
        self.islandDirtyListCriticalSection = any(infile)  # TYPE_POINTER
        self.propertyMasterLock = any(infile)  # TYPE_POINTER
        self.wantSimulationIslands = struct.unpack('>?', infile.read(1))
        self.snapCollisionToConvexEdgeThreshold = struct.unpack('>f', infile.read(4))
        self.snapCollisionToConcaveEdgeThreshold = struct.unpack('>f', infile.read(4))
        self.enableToiWeldRejection = struct.unpack('>?', infile.read(1))
        self.wantDeactivation = struct.unpack('>?', infile.read(1))
        self.shouldActivateOnRigidBodyTransformChange = struct.unpack('>?', infile.read(1))
        self.deactivationReferenceDistance = struct.unpack('>f', infile.read(4))
        self.toiCollisionResponseRotateNormal = struct.unpack('>f', infile.read(4))
        self.maxSectorsPerMidphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.maxSectorsPerNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.processToisMultithreaded = struct.unpack('>?', infile.read(1))
        self.maxEntriesPerToiMidphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.maxEntriesPerToiNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.maxNumToiCollisionPairsSinglethreaded = struct.unpack('>i', infile.read(4))
        self.simulationType = enumerate(infile)  # TYPE_ENUM
        self.numToisTillAllowedPenetrationSimplifiedToi = struct.unpack('>f', infile.read(4))
        self.numToisTillAllowedPenetrationToi = struct.unpack('>f', infile.read(4))
        self.numToisTillAllowedPenetrationToiHigher = struct.unpack('>f', infile.read(4))
        self.numToisTillAllowedPenetrationToiForced = struct.unpack('>f', infile.read(4))
        self.lastEntityUid = struct.unpack('>I', infile.read(4))
        self.lastIslandUid = struct.unpack('>I', infile.read(4))
        self.lastConstraintUid = struct.unpack('>I', infile.read(4))
        self.phantoms = hkpPhantom(infile)  # TYPE_ARRAY
        self.actionListeners = any(infile)  # TYPE_ARRAY
        self.entityListeners = any(infile)  # TYPE_ARRAY
        self.phantomListeners = any(infile)  # TYPE_ARRAY
        self.constraintListeners = any(infile)  # TYPE_ARRAY
        self.worldDeletionListeners = any(infile)  # TYPE_ARRAY
        self.islandActivationListeners = any(infile)  # TYPE_ARRAY
        self.worldPostSimulationListeners = any(infile)  # TYPE_ARRAY
        self.worldPostIntegrateListeners = any(infile)  # TYPE_ARRAY
        self.worldPostCollideListeners = any(infile)  # TYPE_ARRAY
        self.islandPostIntegrateListeners = any(infile)  # TYPE_ARRAY
        self.islandPostCollideListeners = any(infile)  # TYPE_ARRAY
        self.contactListeners = any(infile)  # TYPE_ARRAY
        self.contactImpulseLimitBreachedListeners = any(infile)  # TYPE_ARRAY
        self.worldExtensions = any(infile)  # TYPE_ARRAY
        self.violatedConstraintArray = any(infile)  # TYPE_POINTER
        self.broadPhaseBorder = any(infile)  # TYPE_POINTER
        self.destructionWorld = any(infile)  # TYPE_POINTER
        self.npWorld = any(infile)  # TYPE_POINTER
        self.broadPhaseExtents = struct.unpack('>4f', infile.read(16))
        self.broadPhaseNumMarkers = struct.unpack('>i', infile.read(4))
        self.sizeOfToiEventQueue = struct.unpack('>i', infile.read(4))
        self.broadPhaseQuerySize = struct.unpack('>i', infile.read(4))
        self.broadPhaseUpdateSize = struct.unpack('>i', infile.read(4))
        self.contactPointGeneration = enumerate(infile)  # TYPE_ENUM
        self.useCompoundSpuElf = struct.unpack('>?', infile.read(1))
