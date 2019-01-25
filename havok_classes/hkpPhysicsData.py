from .hkReferencedObject import hkReferencedObject
from .hkpWorldCinfo import hkpWorldCinfo
from .hkpPhysicsSystem import hkpPhysicsSystem


class hkpPhysicsData(hkReferencedObject):
    worldCinfo: hkpWorldCinfo
    systems: hkpPhysicsSystem

    def __init__(self, infile):
        self.worldCinfo = hkpWorldCinfo(infile)  # TYPE_POINTER
        self.systems = hkpPhysicsSystem(infile)  # TYPE_ARRAY
