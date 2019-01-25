from .hkReferencedObject import hkReferencedObject
from .hkpWorldCinfo import hkpWorldCinfo
from typing import List
from .common import get_array
from .hkpPhysicsSystem import hkpPhysicsSystem


class hkpPhysicsData(hkReferencedObject):
    worldCinfo: any
    systems: List[hkpPhysicsSystem]

    def __init__(self, infile):
        self.worldCinfo = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.systems = get_array(infile, hkpPhysicsSystem, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} worldCinfo={worldCinfo}, systems=[{systems}]>".format(**{
            "class_name": self.__class__.__name__,
            "worldCinfo": self.worldCinfo,
            "systems": self.systems,
        })
