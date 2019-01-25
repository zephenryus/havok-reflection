from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import vector4
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
    collisionFilter: hkpCollisionFilter
    convexListFilter: hkpConvexListFilter
    expectedMaxLinearVelocity: float
    sizeOfToiEventQueue: int
    expectedMinPsiDeltaTime: float
    memoryWatchDog: hkWorldMemoryAvailableWatchDog
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
        self.gravity = struct.unpack('>4f', infile.read(16))
        self.broadPhaseQuerySize = struct.unpack('>i', infile.read(4))
        self.contactRestingVelocity = struct.unpack('>f', infile.read(4))
        self.broadPhaseType = BroadPhaseType(infile)  # TYPE_ENUM
        self.broadPhaseBorderBehaviour = BroadPhaseBorderBehaviour(infile)  # TYPE_ENUM
        self.mtPostponeAndSortBroadPhaseBorderCallbacks = struct.unpack('>?', infile.read(1))
        self.broadPhaseWorldAabb = hkAabb(infile)  # TYPE_STRUCT
        self.collisionTolerance = struct.unpack('>f', infile.read(4))
        self.collisionFilter = hkpCollisionFilter(infile)  # TYPE_POINTER
        self.convexListFilter = hkpConvexListFilter(infile)  # TYPE_POINTER
        self.expectedMaxLinearVelocity = struct.unpack('>f', infile.read(4))
        self.sizeOfToiEventQueue = struct.unpack('>i', infile.read(4))
        self.expectedMinPsiDeltaTime = struct.unpack('>f', infile.read(4))
        self.memoryWatchDog = hkWorldMemoryAvailableWatchDog(infile)  # TYPE_POINTER
        self.broadPhaseNumMarkers = struct.unpack('>i', infile.read(4))
        self.contactPointGeneration = ContactPointGeneration(infile)  # TYPE_ENUM
        self.allowToSkipConfirmedCallbacks = struct.unpack('>?', infile.read(1))
        self.solverTau = struct.unpack('>f', infile.read(4))
        self.solverDamp = struct.unpack('>f', infile.read(4))
        self.solverIterations = struct.unpack('>i', infile.read(4))
        self.solverMicrosteps = struct.unpack('>i', infile.read(4))
        self.maxConstraintViolation = struct.unpack('>f', infile.read(4))
        self.forceCoherentConstraintOrderingInSolver = struct.unpack('>?', infile.read(1))
        self.snapCollisionToConvexEdgeThreshold = struct.unpack('>f', infile.read(4))
        self.snapCollisionToConcaveEdgeThreshold = struct.unpack('>f', infile.read(4))
        self.enableToiWeldRejection = struct.unpack('>?', infile.read(1))
        self.enableDeprecatedWelding = struct.unpack('>?', infile.read(1))
        self.iterativeLinearCastEarlyOutDistance = struct.unpack('>f', infile.read(4))
        self.iterativeLinearCastMaxIterations = struct.unpack('>i', infile.read(4))
        self.deactivationNumInactiveFramesSelectFlag0 = struct.unpack('>B', infile.read(1))
        self.deactivationNumInactiveFramesSelectFlag1 = struct.unpack('>B', infile.read(1))
        self.deactivationIntegrateCounter = struct.unpack('>B', infile.read(1))
        self.shouldActivateOnRigidBodyTransformChange = struct.unpack('>?', infile.read(1))
        self.deactivationReferenceDistance = struct.unpack('>f', infile.read(4))
        self.toiCollisionResponseRotateNormal = struct.unpack('>f', infile.read(4))
        self.useCompoundSpuElf = struct.unpack('>?', infile.read(1))
        self.maxSectorsPerMidphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.maxSectorsPerNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.processToisMultithreaded = struct.unpack('>?', infile.read(1))
        self.maxEntriesPerToiMidphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.maxEntriesPerToiNarrowphaseCollideTask = struct.unpack('>i', infile.read(4))
        self.maxNumToiCollisionPairsSinglethreaded = struct.unpack('>i', infile.read(4))
        self.numToisTillAllowedPenetrationSimplifiedToi = struct.unpack('>f', infile.read(4))
        self.numToisTillAllowedPenetrationToi = struct.unpack('>f', infile.read(4))
        self.numToisTillAllowedPenetrationToiHigher = struct.unpack('>f', infile.read(4))
        self.numToisTillAllowedPenetrationToiForced = struct.unpack('>f', infile.read(4))
        self.enableDeactivation = struct.unpack('>?', infile.read(1))
        self.simulationType = SimulationType(infile)  # TYPE_ENUM
        self.enableSimulationIslands = struct.unpack('>?', infile.read(1))
        self.minDesiredIslandSize = struct.unpack('>I', infile.read(4))
        self.processActionsInSingleThread = struct.unpack('>?', infile.read(1))
        self.allowIntegrationOfIslandsWithoutConstraintsInASeparateJob = struct.unpack('>?', infile.read(1))
        self.frameMarkerPsiSnap = struct.unpack('>f', infile.read(4))
        self.fireCollisionCallbacks = struct.unpack('>?', infile.read(1))
