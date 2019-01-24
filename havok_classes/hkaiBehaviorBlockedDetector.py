from .hkReferencedObject import hkReferencedObject
from .hkaiEdgeFollowingBehavior import hkaiEdgeFollowingBehavior
from .common import vector4


class hkaiBehaviorBlockedDetector(hkReferencedObject):
    behavior: hkaiEdgeFollowingBehavior
    prevRuntimeID: int
    prevPos: vector4
    avgProgress: float
    smoothingFactor: float
    blockedThreshold: float
    sqrTeleportationThreshold: float
    blocked: bool
