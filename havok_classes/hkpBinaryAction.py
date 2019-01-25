from .hkpAction import hkpAction
from .hkpEntity import hkpEntity


class hkpBinaryAction(hkpAction):
    entityA: hkpEntity
    entityB: hkpEntity

    def __init__(self, infile):
        self.entityA = hkpEntity(infile)  # TYPE_POINTER
        self.entityB = hkpEntity(infile)  # TYPE_POINTER
