from .hkReferencedObject import hkReferencedObject
from .hkaiWorld import hkaiWorld


class hkaiBehavior(hkReferencedObject):
    world: any

    def __init__(self, infile):
        self.world = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} world={world}>".format(**{
            "class_name": self.__class__.__name__,
            "world": self.world,
        })
