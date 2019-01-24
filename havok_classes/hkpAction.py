from .hkReferencedObject import hkReferencedObject
from .common import any


class hkpAction(hkReferencedObject):
    world: any
    island: any
    userData: int
    name: str
