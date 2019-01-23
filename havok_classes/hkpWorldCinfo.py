from .hkReferencedObject import hkReferencedObject
from .hkAabb import hkAabb
from .hkpCollisionFilter import hkpCollisionFilter
from .hkpConvexListFilter import hkpConvexListFilter
from .hkWorldMemoryAvailableWatchDog import hkWorldMemoryAvailableWatchDog


class hkpWorldCinfo(hkReferencedObject):
	gravity: any
	broadPhaseQuerySize: int
	contactRestingVelocity: float
	broadPhaseType: any
	broadPhaseBorderBehaviour: any
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
	contactPointGeneration: any
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
	simulationType: any
	enableSimulationIslands: bool
	minDesiredIslandSize: int
	processActionsInSingleThread: bool
	allowIntegrationOfIslandsWithoutConstraintsInASeparateJob: bool
	frameMarkerPsiSnap: float
	fireCollisionCallbacks: bool
