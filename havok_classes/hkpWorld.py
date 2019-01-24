from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpSimulation import hkpSimulation
from .common import vector4, any
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
