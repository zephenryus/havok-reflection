from .hkpAction import hkpAction
from .hkpEntity import hkpEntity


class hkpBinaryAction(hkpAction):
    entityA: hkpEntity
    entityB: hkpEntity
