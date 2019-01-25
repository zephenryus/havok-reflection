from .hkReferencedObject import hkReferencedObject
from .hkcdShape import hkcdShape
from .hkpBreakableMaterial import hkpBreakableMaterial


class hkpBreakableShape(hkReferencedObject):
    physicsShape: any
    material: any

    def __init__(self, infile):
        self.physicsShape = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.material = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} physicsShape={physicsShape}, material={material}>".format(**{
            "class_name": self.__class__.__name__,
            "physicsShape": self.physicsShape,
            "material": self.material,
        })
