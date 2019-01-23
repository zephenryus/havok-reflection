from .hkReferencedObject import hkReferencedObject
from .hkaiAdaptiveRanger import hkaiAdaptiveRanger
from .hkaiAstarCostModifier import hkaiAstarCostModifier
from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter
from .hkaiAvoidanceProperties import hkaiAvoidanceProperties


class hkaiCharacter(hkReferencedObject):
	userData: int
	position: any
	forward: any
	velocity: any
	up: any
	currentNavMeshFace: int
	currentNavVolumeCell: int
	radius: float
	desiredSpeed: float
	adaptiveRanger: hkaiAdaptiveRanger
	costModifier: hkaiAstarCostModifier
	edgeFilter: hkaiAstarEdgeFilter
	hitFilter: any
	steeringFilter: any
	agentFilterInfo: int
	avoidanceProperties: hkaiAvoidanceProperties
	avoidanceState: float
	agentPriority: int
	avoidanceType: int
	avoidanceEnabledMask: any
	state: any
	behaviorListeners: any
	layer: int
