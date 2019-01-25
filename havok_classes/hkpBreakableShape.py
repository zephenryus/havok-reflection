from .hkReferencedObject import hkReferencedObject
from .hkcdShape import hkcdShape
from .hkpBreakableMaterial import hkpBreakableMaterial


class hkpBreakableShape(hkReferencedObject):
    physicsShape: hkcdShape
    material: hkpBreakableMaterial

    def __init__(self, infile):
        self.physicsShape = hkcdShape(infile)  # TYPE_POINTER
        self.material = hkpBreakableMaterial(infile)  # TYPE_POINTER
