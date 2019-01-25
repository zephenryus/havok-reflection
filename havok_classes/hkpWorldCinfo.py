from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .enums import BroadPhaseType, BroadPhaseBorderBehaviour, ContactPointGeneration, SimulationType
from .hkAabb import hkAabb
from .hkpCollisionFilter import hkpCollisionFilter
from .hkpConvexListFilter import hkpConvexListFilter
from .hkWorldMemoryAvailableWatchDog import hkWorldMemoryAvailableWatchDog


class SolverType(Enum):
    SOLVER_TYPE_INVALID = 0
    SOLVER_TYPE_2ITERS_SOFT = 1
    SOLVER_TYPE_2ITERS_MEDIUM = 2
    SOLVER_TYPE_2ITERS_HARD = 3
    SOLVER_TYPE_4ITERS_SOFT = 4
    SOLVER_TYPE_4ITERS_MEDIUM = 5
    SOLVER_TYPE_4ITERS_HARD = 6
    SOLVER_TYPE_8ITERS_SOFT = 7
    SOLVER_TYPE_8ITERS_MEDIUM = 8
    SOLVER_TYPE_8ITERS_HARD = 9
    SOLVER_TYPE_MAX_ID = 10


class SimulationType(Enum):
    SIMULATION_TYPE_INVALID = 0
    SIMULATION_TYPE_DISCRETE = 1
    SIMULATION_TYPE_CONTINUOUS = 2
    SIMULATION_TYPE_MULTITHREADED = 3


class ContactPointGeneration(Enum):
    CONTACT_POINT_ACCEPT_ALWAYS = 0
    CONTACT_POINT_REJECT_DUBIOUS = 1
    CONTACT_POINT_REJECT_MANY = 2


class BroadPhaseType(Enum):
    BROADPHASE_TYPE_SAP = 0
    BROADPHASE_TYPE_TREE = 1
    BROADPHASE_TYPE_HYBRID = 2


class BroadPhaseBorderBehaviour(Enum):
    BROADPHASE_BORDER_ASSERT = 0
    BROADPHASE_BORDER_FIX_ENTITY = 1
    BROADPHASE_BORDER_REMOVE_ENTITY = 2
    BROADPHASE_BORDER_DO_NOTHING = 3


class hkpWorldCinfo(hkReferencedObject):
    gravity: vector4
    broadPhaseQuerySize: int
    contactRestingVelocity: float
    broadPhaseType: BroadPhaseType
    broadPhaseBorderBehaviour: BroadPhaseBorderBehaviour
    mtPostponeAndSortBroadPhaseBorderCallbacks: bool
    broadPhaseWorldAabb: hkAabb
    collisionTolerance: float
    collisionFilter: any
    convexListFilter: any
    expectedMaxLinearVelocity: float
    sizeOfToiEventQueue: int
    expectedMinPsiDeltaTime: float
    memoryWatchDog: any
    broadPhaseNumMarkers: int
    contactPointGeneration: ContactPointGeneration
    allowToSkipConfirmedCallbacks: bool
    solverTau: float
    solverDamp: float
    solverIterations: int
    solverMicrosteps: int
    maxConstraintViolation: float
    forceCoherentConstraintOrderingInSolver: bool
    snapCollisionToConvexEdgeThreshold: float
    snapCollisionToConcaveEdgeThreshold: float
    enableToiWeldRejection: bool
    enableDeprecatedWelding: bool
    iterativeLinearCastEarlyOutDistance: float
    iterativeLinearCastMaxIterations: int
    deactivationNumInactiveFramesSelectFlag0: int
    deactivationNumInactiveFramesSelectFlag1: int
    deactivationIntegrateCounter: int
    shouldActivateOnRigidBodyTransformChange: bool
    deactivationReferenceDistance: float
    toiCollisionResponseRotateNormal: float
    useCompoundSpuElf: bool
    maxSectorsPerMidphaseCollideTask: int
    maxSectorsPerNarrowphaseCollideTask: int
    processToisMultithreaded: bool
    maxEntriesPerToiMidphaseCollideTask: int
    maxEntriesPerToiNarrowphaseCollideTask: int
    maxNumToiCollisionPairsSinglethreaded: int
    numToisTillAllowedPenetrationSimplifiedToi: float
    numToisTillAllowedPenetrationToi: float
    numToisTillAllowedPenetrationToiHigher: float
    numToisTillAllowedPenetrationToiForced: float
    enableDeactivation: bool
    simulationType: SimulationType
    enableSimulationIslands: bool
    minDesiredIslandSize: int
    processActionsInSingleThread: bool
    allowIntegrationOfIslandsWithoutConstraintsInASeparateJob: bool
    frameMarkerPsiSnap: float
    fireCollisionCallbacks: bool

    def __init__(self, infile):
        self.gravity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.broadPhaseQuerySize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contactRestingVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.broadPhaseType = BroadPhaseType(infile)  # TYPE_ENUM:TYPE_INT8
        self.broadPhaseBorderBehaviour = BroadPhaseBorderBehaviour(infile)  # TYPE_ENUM:TYPE_INT8
        self.mtPostponeAndSortBroadPhaseBorderCallbacks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.broadPhaseWorldAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.collisionTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.collisionFilter = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.convexListFilter = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.expectedMaxLinearVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sizeOfToiEventQueue = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.expectedMinPsiDeltaTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.memoryWatchDog = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.broadPhaseNumMarkers = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.contactPointGeneration = ContactPointGeneration(infile)  # TYPE_ENUM:TYPE_INT8
        self.allowToSkipConfirmedCallbacks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.solverTau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.solverDamp = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.solverIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.solverMicrosteps = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxConstraintViolation = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.forceCoherentConstraintOrderingInSolver = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.snapCollisionToConvexEdgeThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.snapCollisionToConcaveEdgeThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.enableToiWeldRejection = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.enableDeprecatedWelding = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.iterativeLinearCastEarlyOutDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.iterativeLinearCastMaxIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.deactivationNumInactiveFramesSelectFlag0 = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.deactivationNumInactiveFramesSelectFlag1 = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.deactivationIntegrateCounter = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.shouldActivateOnRigidBodyTransformChange = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.deactivationReferenceDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.toiCollisionResponseRotateNormal = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useCompoundSpuElf = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.maxSectorsPerMidphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxSectorsPerNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.processToisMultithreaded = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.maxEntriesPerToiMidphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxEntriesPerToiNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxNumToiCollisionPairsSinglethreaded = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numToisTillAllowedPenetrationSimplifiedToi = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numToisTillAllowedPenetrationToi = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numToisTillAllowedPenetrationToiHigher = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.numToisTillAllowedPenetrationToiForced = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.enableDeactivation = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.simulationType = SimulationType(infile)  # TYPE_ENUM:TYPE_INT8
        self.enableSimulationIslands = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.minDesiredIslandSize = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.processActionsInSingleThread = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.allowIntegrationOfIslandsWithoutConstraintsInASeparateJob = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.frameMarkerPsiSnap = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.fireCollisionCallbacks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} gravity={gravity}, broadPhaseQuerySize={broadPhaseQuerySize}, contactRestingVelocity={contactRestingVelocity}, broadPhaseType={broadPhaseType}, broadPhaseBorderBehaviour={broadPhaseBorderBehaviour}, mtPostponeAndSortBroadPhaseBorderCallbacks={mtPostponeAndSortBroadPhaseBorderCallbacks}, broadPhaseWorldAabb={broadPhaseWorldAabb}, collisionTolerance={collisionTolerance}, collisionFilter={collisionFilter}, convexListFilter={convexListFilter}, expectedMaxLinearVelocity={expectedMaxLinearVelocity}, sizeOfToiEventQueue={sizeOfToiEventQueue}, expectedMinPsiDeltaTime={expectedMinPsiDeltaTime}, memoryWatchDog={memoryWatchDog}, broadPhaseNumMarkers={broadPhaseNumMarkers}, contactPointGeneration={contactPointGeneration}, allowToSkipConfirmedCallbacks={allowToSkipConfirmedCallbacks}, solverTau={solverTau}, solverDamp={solverDamp}, solverIterations={solverIterations}, solverMicrosteps={solverMicrosteps}, maxConstraintViolation={maxConstraintViolation}, forceCoherentConstraintOrderingInSolver={forceCoherentConstraintOrderingInSolver}, snapCollisionToConvexEdgeThreshold={snapCollisionToConvexEdgeThreshold}, snapCollisionToConcaveEdgeThreshold={snapCollisionToConcaveEdgeThreshold}, enableToiWeldRejection={enableToiWeldRejection}, enableDeprecatedWelding={enableDeprecatedWelding}, iterativeLinearCastEarlyOutDistance={iterativeLinearCastEarlyOutDistance}, iterativeLinearCastMaxIterations={iterativeLinearCastMaxIterations}, deactivationNumInactiveFramesSelectFlag0={deactivationNumInactiveFramesSelectFlag0}, deactivationNumInactiveFramesSelectFlag1={deactivationNumInactiveFramesSelectFlag1}, deactivationIntegrateCounter={deactivationIntegrateCounter}, shouldActivateOnRigidBodyTransformChange={shouldActivateOnRigidBodyTransformChange}, deactivationReferenceDistance={deactivationReferenceDistance}, toiCollisionResponseRotateNormal={toiCollisionResponseRotateNormal}, useCompoundSpuElf={useCompoundSpuElf}, maxSectorsPerMidphaseCollideTask={maxSectorsPerMidphaseCollideTask}, maxSectorsPerNarrowphaseCollideTask={maxSectorsPerNarrowphaseCollideTask}, processToisMultithreaded={processToisMultithreaded}, maxEntriesPerToiMidphaseCollideTask={maxEntriesPerToiMidphaseCollideTask}, maxEntriesPerToiNarrowphaseCollideTask={maxEntriesPerToiNarrowphaseCollideTask}, maxNumToiCollisionPairsSinglethreaded={maxNumToiCollisionPairsSinglethreaded}, numToisTillAllowedPenetrationSimplifiedToi={numToisTillAllowedPenetrationSimplifiedToi}, numToisTillAllowedPenetrationToi={numToisTillAllowedPenetrationToi}, numToisTillAllowedPenetrationToiHigher={numToisTillAllowedPenetrationToiHigher}, numToisTillAllowedPenetrationToiForced={numToisTillAllowedPenetrationToiForced}, enableDeactivation={enableDeactivation}, simulationType={simulationType}, enableSimulationIslands={enableSimulationIslands}, minDesiredIslandSize={minDesiredIslandSize}, processActionsInSingleThread={processActionsInSingleThread}, allowIntegrationOfIslandsWithoutConstraintsInASeparateJob={allowIntegrationOfIslandsWithoutConstraintsInASeparateJob}, frameMarkerPsiSnap={frameMarkerPsiSnap}, fireCollisionCallbacks={fireCollisionCallbacks}>".format(**{
            "class_name": self.__class__.__name__,
            "gravity": self.gravity,
            "broadPhaseQuerySize": self.broadPhaseQuerySize,
            "contactRestingVelocity": self.contactRestingVelocity,
            "broadPhaseType": self.broadPhaseType,
            "broadPhaseBorderBehaviour": self.broadPhaseBorderBehaviour,
            "mtPostponeAndSortBroadPhaseBorderCallbacks": self.mtPostponeAndSortBroadPhaseBorderCallbacks,
            "broadPhaseWorldAabb": self.broadPhaseWorldAabb,
            "collisionTolerance": self.collisionTolerance,
            "collisionFilter": self.collisionFilter,
            "convexListFilter": self.convexListFilter,
            "expectedMaxLinearVelocity": self.expectedMaxLinearVelocity,
            "sizeOfToiEventQueue": self.sizeOfToiEventQueue,
            "expectedMinPsiDeltaTime": self.expectedMinPsiDeltaTime,
            "memoryWatchDog": self.memoryWatchDog,
            "broadPhaseNumMarkers": self.broadPhaseNumMarkers,
            "contactPointGeneration": self.contactPointGeneration,
            "allowToSkipConfirmedCallbacks": self.allowToSkipConfirmedCallbacks,
            "solverTau": self.solverTau,
            "solverDamp": self.solverDamp,
            "solverIterations": self.solverIterations,
            "solverMicrosteps": self.solverMicrosteps,
            "maxConstraintViolation": self.maxConstraintViolation,
            "forceCoherentConstraintOrderingInSolver": self.forceCoherentConstraintOrderingInSolver,
            "snapCollisionToConvexEdgeThreshold": self.snapCollisionToConvexEdgeThreshold,
            "snapCollisionToConcaveEdgeThreshold": self.snapCollisionToConcaveEdgeThreshold,
            "enableToiWeldRejection": self.enableToiWeldRejection,
            "enableDeprecatedWelding": self.enableDeprecatedWelding,
            "iterativeLinearCastEarlyOutDistance": self.iterativeLinearCastEarlyOutDistance,
            "iterativeLinearCastMaxIterations": self.iterativeLinearCastMaxIterations,
            "deactivationNumInactiveFramesSelectFlag0": self.deactivationNumInactiveFramesSelectFlag0,
            "deactivationNumInactiveFramesSelectFlag1": self.deactivationNumInactiveFramesSelectFlag1,
            "deactivationIntegrateCounter": self.deactivationIntegrateCounter,
            "shouldActivateOnRigidBodyTransformChange": self.shouldActivateOnRigidBodyTransformChange,
            "deactivationReferenceDistance": self.deactivationReferenceDistance,
            "toiCollisionResponseRotateNormal": self.toiCollisionResponseRotateNormal,
            "useCompoundSpuElf": self.useCompoundSpuElf,
            "maxSectorsPerMidphaseCollideTask": self.maxSectorsPerMidphaseCollideTask,
            "maxSectorsPerNarrowphaseCollideTask": self.maxSectorsPerNarrowphaseCollideTask,
            "processToisMultithreaded": self.processToisMultithreaded,
            "maxEntriesPerToiMidphaseCollideTask": self.maxEntriesPerToiMidphaseCollideTask,
            "maxEntriesPerToiNarrowphaseCollideTask": self.maxEntriesPerToiNarrowphaseCollideTask,
            "maxNumToiCollisionPairsSinglethreaded": self.maxNumToiCollisionPairsSinglethreaded,
            "numToisTillAllowedPenetrationSimplifiedToi": self.numToisTillAllowedPenetrationSimplifiedToi,
            "numToisTillAllowedPenetrationToi": self.numToisTillAllowedPenetrationToi,
            "numToisTillAllowedPenetrationToiHigher": self.numToisTillAllowedPenetrationToiHigher,
            "numToisTillAllowedPenetrationToiForced": self.numToisTillAllowedPenetrationToiForced,
            "enableDeactivation": self.enableDeactivation,
            "simulationType": self.simulationType,
            "enableSimulationIslands": self.enableSimulationIslands,
            "minDesiredIslandSize": self.minDesiredIslandSize,
            "processActionsInSingleThread": self.processActionsInSingleThread,
            "allowIntegrationOfIslandsWithoutConstraintsInASeparateJob": self.allowIntegrationOfIslandsWithoutConstraintsInASeparateJob,
            "frameMarkerPsiSnap": self.frameMarkerPsiSnap,
            "fireCollisionCallbacks": self.fireCollisionCallbacks,
        })
