from .hkReferencedObject import hkReferencedObject
from .hkRefCountedProperties import hkRefCountedProperties


class hkpBreakableMaterial(hkReferencedObject):
    strength: float
    typeAndFlags: int
    properties: hkRefCountedProperties
