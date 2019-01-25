from .hkpBreakableMultiMaterial import hkpBreakableMultiMaterial


class hkpExtendedMeshShapeBreakableMaterial(hkpBreakableMultiMaterial):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
