from .hkReferencedObject import hkReferencedObject
from .hkaiWorld import hkaiWorld


class hkaiBehavior(hkReferencedObject):
    world: hkaiWorld

    def __init__(self, infile):
        self.world = hkaiWorld(infile)  # TYPE_POINTER
