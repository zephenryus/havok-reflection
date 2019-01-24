from .hkReferencedObject import hkReferencedObject
from .hkpWorldCinfo import hkpWorldCinfo
from .hkpPhysicsSystem import hkpPhysicsSystem


class hkpPhysicsData(hkReferencedObject):
    worldCinfo: hkpWorldCinfo
    systems: hkpPhysicsSystem
