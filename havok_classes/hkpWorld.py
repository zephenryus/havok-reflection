from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpSimulation import hkpSimulation
import struct
from .hkpRigidBody import hkpRigidBody
from typing import List
from .common import get_array
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
    simulation: any
    gravity: vector4
    fixedIsland: any
    fixedRigidBody: any
    activeSimulationIslands: List[any]
    inactiveSimulationIslands: List[any]
    dirtySimulationIslands: List[any]
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
    phantoms: List[hkpPhantom]
    actionListeners: List[any]
    entityListeners: List[any]
    phantomListeners: List[any]
    constraintListeners: List[any]
    worldDeletionListeners: List[any]
    islandActivationListeners: List[any]
    worldPostSimulationListeners: List[any]
    worldPostIntegrateListeners: List[any]
    worldPostCollideListeners: List[any]
    islandPostIntegrateListeners: List[any]
    islandPostCollideListeners: List[any]
    contactListeners: List[any]
    contactImpulseLimitBreachedListeners: List[any]
    worldExtensions: List[any]
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
        self.simulation = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.gravity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.fixedIsland = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.fixedRigidBody = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.activeSimulationIslands = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.inactiveSimulationIslands = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.dirtySimulationIslands = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.maintenanceMgr = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.memoryWatchDog = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.assertOnRunningOutOfSolverMemory = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.broadPhaseType = enumerate(infile)  # TYPE_ENUM:TYPE_INT8
        self.broadPhase = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.broadPhaseDispatcher = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.phantomBroadPhaseListener = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.entityEntityBroadPhaseListener = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.broadPhaseBorderListener = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.multithreadedSimulationJobData = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.collisionInput = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.collisionFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.collisionDispatcher = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.convexListFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.pendingOperations = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.pendingOperationsCount = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.pendingBodyOperationsCount = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.criticalOperationsLockCount = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.criticalOperationsLockCountForPhantoms = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.blockExecutingPendingOperations = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.criticalOperationsAllowed = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.pendingOperationQueues = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.pendingOperationQueueCount = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.multiThreadCheck = hkMultiThreadCheck(infile)  # TYPE_STRUCT:TYPE_VOID
        self.processActionsInSingleThread = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.allowIntegrationOfIslandsWithoutConstraintsInASeparateJob = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.minDesiredIslandSize = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.modifyConstraintCriticalSection = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.isLocked = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.islandDirtyListCriticalSection = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.propertyMasterLock = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.wantSimulationIslands = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.snapCollisionToConvexEdgeThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.snapCollisionToConcaveEdgeThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.enableToiWeldRejection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.wantDeactivation = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.shouldActivateOnRigidBodyTransformChange = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.deactivationReferenceDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toiCollisionResponseRotateNormal = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSectorsPerMidphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxSectorsPerNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.processToisMultithreaded = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.maxEntriesPerToiMidphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxEntriesPerToiNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxNumToiCollisionPairsSinglethreaded = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.simulationType = enumerate(infile)  # TYPE_ENUM:TYPE_INT32
        self.numToisTillAllowedPenetrationSimplifiedToi = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numToisTillAllowedPenetrationToi = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numToisTillAllowedPenetrationToiHigher = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numToisTillAllowedPenetrationToiForced = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.lastEntityUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.lastIslandUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.lastConstraintUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.phantoms = get_array(infile, hkpPhantom, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.actionListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.entityListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.phantomListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.constraintListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.worldDeletionListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.islandActivationListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.worldPostSimulationListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.worldPostIntegrateListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.worldPostCollideListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.islandPostIntegrateListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.islandPostCollideListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.contactListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.contactImpulseLimitBreachedListeners = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.worldExtensions = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.violatedConstraintArray = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.broadPhaseBorder = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.destructionWorld = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.npWorld = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.broadPhaseExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.broadPhaseNumMarkers = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.sizeOfToiEventQueue = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.broadPhaseQuerySize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.broadPhaseUpdateSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contactPointGeneration = enumerate(infile)  # TYPE_ENUM:TYPE_INT8
        self.useCompoundSpuElf = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} simulation={simulation}, gravity={gravity}, fixedIsland={fixedIsland}, fixedRigidBody={fixedRigidBody}, activeSimulationIslands=[{activeSimulationIslands}], inactiveSimulationIslands=[{inactiveSimulationIslands}], dirtySimulationIslands=[{dirtySimulationIslands}], maintenanceMgr={maintenanceMgr}, memoryWatchDog={memoryWatchDog}, assertOnRunningOutOfSolverMemory={assertOnRunningOutOfSolverMemory}, broadPhaseType={broadPhaseType}, broadPhase={broadPhase}, broadPhaseDispatcher={broadPhaseDispatcher}, phantomBroadPhaseListener={phantomBroadPhaseListener}, entityEntityBroadPhaseListener={entityEntityBroadPhaseListener}, broadPhaseBorderListener={broadPhaseBorderListener}, multithreadedSimulationJobData={multithreadedSimulationJobData}, collisionInput={collisionInput}, collisionFilter={collisionFilter}, collisionDispatcher={collisionDispatcher}, convexListFilter={convexListFilter}, pendingOperations={pendingOperations}, pendingOperationsCount={pendingOperationsCount}, pendingBodyOperationsCount={pendingBodyOperationsCount}, criticalOperationsLockCount={criticalOperationsLockCount}, criticalOperationsLockCountForPhantoms={criticalOperationsLockCountForPhantoms}, blockExecutingPendingOperations={blockExecutingPendingOperations}, criticalOperationsAllowed={criticalOperationsAllowed}, pendingOperationQueues={pendingOperationQueues}, pendingOperationQueueCount={pendingOperationQueueCount}, multiThreadCheck={multiThreadCheck}, processActionsInSingleThread={processActionsInSingleThread}, allowIntegrationOfIslandsWithoutConstraintsInASeparateJob={allowIntegrationOfIslandsWithoutConstraintsInASeparateJob}, minDesiredIslandSize={minDesiredIslandSize}, modifyConstraintCriticalSection={modifyConstraintCriticalSection}, isLocked={isLocked}, islandDirtyListCriticalSection={islandDirtyListCriticalSection}, propertyMasterLock={propertyMasterLock}, wantSimulationIslands={wantSimulationIslands}, snapCollisionToConvexEdgeThreshold={snapCollisionToConvexEdgeThreshold}, snapCollisionToConcaveEdgeThreshold={snapCollisionToConcaveEdgeThreshold}, enableToiWeldRejection={enableToiWeldRejection}, wantDeactivation={wantDeactivation}, shouldActivateOnRigidBodyTransformChange={shouldActivateOnRigidBodyTransformChange}, deactivationReferenceDistance={deactivationReferenceDistance}, toiCollisionResponseRotateNormal={toiCollisionResponseRotateNormal}, maxSectorsPerMidphaseCollideTask={maxSectorsPerMidphaseCollideTask}, maxSectorsPerNarrowphaseCollideTask={maxSectorsPerNarrowphaseCollideTask}, processToisMultithreaded={processToisMultithreaded}, maxEntriesPerToiMidphaseCollideTask={maxEntriesPerToiMidphaseCollideTask}, maxEntriesPerToiNarrowphaseCollideTask={maxEntriesPerToiNarrowphaseCollideTask}, maxNumToiCollisionPairsSinglethreaded={maxNumToiCollisionPairsSinglethreaded}, simulationType={simulationType}, numToisTillAllowedPenetrationSimplifiedToi={numToisTillAllowedPenetrationSimplifiedToi}, numToisTillAllowedPenetrationToi={numToisTillAllowedPenetrationToi}, numToisTillAllowedPenetrationToiHigher={numToisTillAllowedPenetrationToiHigher}, numToisTillAllowedPenetrationToiForced={numToisTillAllowedPenetrationToiForced}, lastEntityUid={lastEntityUid}, lastIslandUid={lastIslandUid}, lastConstraintUid={lastConstraintUid}, phantoms=[{phantoms}], actionListeners=[{actionListeners}], entityListeners=[{entityListeners}], phantomListeners=[{phantomListeners}], constraintListeners=[{constraintListeners}], worldDeletionListeners=[{worldDeletionListeners}], islandActivationListeners=[{islandActivationListeners}], worldPostSimulationListeners=[{worldPostSimulationListeners}], worldPostIntegrateListeners=[{worldPostIntegrateListeners}], worldPostCollideListeners=[{worldPostCollideListeners}], islandPostIntegrateListeners=[{islandPostIntegrateListeners}], islandPostCollideListeners=[{islandPostCollideListeners}], contactListeners=[{contactListeners}], contactImpulseLimitBreachedListeners=[{contactImpulseLimitBreachedListeners}], worldExtensions=[{worldExtensions}], violatedConstraintArray={violatedConstraintArray}, broadPhaseBorder={broadPhaseBorder}, destructionWorld={destructionWorld}, npWorld={npWorld}, broadPhaseExtents={broadPhaseExtents}, broadPhaseNumMarkers={broadPhaseNumMarkers}, sizeOfToiEventQueue={sizeOfToiEventQueue}, broadPhaseQuerySize={broadPhaseQuerySize}, broadPhaseUpdateSize={broadPhaseUpdateSize}, contactPointGeneration={contactPointGeneration}, useCompoundSpuElf={useCompoundSpuElf}>".format(**{
            "class_name": self.__class__.__name__,
            "simulation": self.simulation,
            "gravity": self.gravity,
            "fixedIsland": self.fixedIsland,
            "fixedRigidBody": self.fixedRigidBody,
            "activeSimulationIslands": self.activeSimulationIslands,
            "inactiveSimulationIslands": self.inactiveSimulationIslands,
            "dirtySimulationIslands": self.dirtySimulationIslands,
            "maintenanceMgr": self.maintenanceMgr,
            "memoryWatchDog": self.memoryWatchDog,
            "assertOnRunningOutOfSolverMemory": self.assertOnRunningOutOfSolverMemory,
            "broadPhaseType": self.broadPhaseType,
            "broadPhase": self.broadPhase,
            "broadPhaseDispatcher": self.broadPhaseDispatcher,
            "phantomBroadPhaseListener": self.phantomBroadPhaseListener,
            "entityEntityBroadPhaseListener": self.entityEntityBroadPhaseListener,
            "broadPhaseBorderListener": self.broadPhaseBorderListener,
            "multithreadedSimulationJobData": self.multithreadedSimulationJobData,
            "collisionInput": self.collisionInput,
            "collisionFilter": self.collisionFilter,
            "collisionDispatcher": self.collisionDispatcher,
            "convexListFilter": self.convexListFilter,
            "pendingOperations": self.pendingOperations,
            "pendingOperationsCount": self.pendingOperationsCount,
            "pendingBodyOperationsCount": self.pendingBodyOperationsCount,
            "criticalOperationsLockCount": self.criticalOperationsLockCount,
            "criticalOperationsLockCountForPhantoms": self.criticalOperationsLockCountForPhantoms,
            "blockExecutingPendingOperations": self.blockExecutingPendingOperations,
            "criticalOperationsAllowed": self.criticalOperationsAllowed,
            "pendingOperationQueues": self.pendingOperationQueues,
            "pendingOperationQueueCount": self.pendingOperationQueueCount,
            "multiThreadCheck": self.multiThreadCheck,
            "processActionsInSingleThread": self.processActionsInSingleThread,
            "allowIntegrationOfIslandsWithoutConstraintsInASeparateJob": self.allowIntegrationOfIslandsWithoutConstraintsInASeparateJob,
            "minDesiredIslandSize": self.minDesiredIslandSize,
            "modifyConstraintCriticalSection": self.modifyConstraintCriticalSection,
            "isLocked": self.isLocked,
            "islandDirtyListCriticalSection": self.islandDirtyListCriticalSection,
            "propertyMasterLock": self.propertyMasterLock,
            "wantSimulationIslands": self.wantSimulationIslands,
            "snapCollisionToConvexEdgeThreshold": self.snapCollisionToConvexEdgeThreshold,
            "snapCollisionToConcaveEdgeThreshold": self.snapCollisionToConcaveEdgeThreshold,
            "enableToiWeldRejection": self.enableToiWeldRejection,
            "wantDeactivation": self.wantDeactivation,
            "shouldActivateOnRigidBodyTransformChange": self.shouldActivateOnRigidBodyTransformChange,
            "deactivationReferenceDistance": self.deactivationReferenceDistance,
            "toiCollisionResponseRotateNormal": self.toiCollisionResponseRotateNormal,
            "maxSectorsPerMidphaseCollideTask": self.maxSectorsPerMidphaseCollideTask,
            "maxSectorsPerNarrowphaseCollideTask": self.maxSectorsPerNarrowphaseCollideTask,
            "processToisMultithreaded": self.processToisMultithreaded,
            "maxEntriesPerToiMidphaseCollideTask": self.maxEntriesPerToiMidphaseCollideTask,
            "maxEntriesPerToiNarrowphaseCollideTask": self.maxEntriesPerToiNarrowphaseCollideTask,
            "maxNumToiCollisionPairsSinglethreaded": self.maxNumToiCollisionPairsSinglethreaded,
            "simulationType": self.simulationType,
            "numToisTillAllowedPenetrationSimplifiedToi": self.numToisTillAllowedPenetrationSimplifiedToi,
            "numToisTillAllowedPenetrationToi": self.numToisTillAllowedPenetrationToi,
            "numToisTillAllowedPenetrationToiHigher": self.numToisTillAllowedPenetrationToiHigher,
            "numToisTillAllowedPenetrationToiForced": self.numToisTillAllowedPenetrationToiForced,
            "lastEntityUid": self.lastEntityUid,
            "lastIslandUid": self.lastIslandUid,
            "lastConstraintUid": self.lastConstraintUid,
            "phantoms": self.phantoms,
            "actionListeners": self.actionListeners,
            "entityListeners": self.entityListeners,
            "phantomListeners": self.phantomListeners,
            "constraintListeners": self.constraintListeners,
            "worldDeletionListeners": self.worldDeletionListeners,
            "islandActivationListeners": self.islandActivationListeners,
            "worldPostSimulationListeners": self.worldPostSimulationListeners,
            "worldPostIntegrateListeners": self.worldPostIntegrateListeners,
            "worldPostCollideListeners": self.worldPostCollideListeners,
            "islandPostIntegrateListeners": self.islandPostIntegrateListeners,
            "islandPostCollideListeners": self.islandPostCollideListeners,
            "contactListeners": self.contactListeners,
            "contactImpulseLimitBreachedListeners": self.contactImpulseLimitBreachedListeners,
            "worldExtensions": self.worldExtensions,
            "violatedConstraintArray": self.violatedConstraintArray,
            "broadPhaseBorder": self.broadPhaseBorder,
            "destructionWorld": self.destructionWorld,
            "npWorld": self.npWorld,
            "broadPhaseExtents": self.broadPhaseExtents,
            "broadPhaseNumMarkers": self.broadPhaseNumMarkers,
            "sizeOfToiEventQueue": self.sizeOfToiEventQueue,
            "broadPhaseQuerySize": self.broadPhaseQuerySize,
            "broadPhaseUpdateSize": self.broadPhaseUpdateSize,
            "contactPointGeneration": self.contactPointGeneration,
            "useCompoundSpuElf": self.useCompoundSpuElf,
        })
