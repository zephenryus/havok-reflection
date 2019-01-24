from .hkReferencedObject import hkReferencedObject
from .hkcdShape import hkcdShape
from .hkpBreakableMaterial import hkpBreakableMaterial


class hkpBreakableShape(hkReferencedObject):
    physicsShape: hkcdShape
    material: hkpBreakableMaterial
