from .hkpBreakableMaterial import hkpBreakableMaterial
from .hkpBreakableMultiMaterialInverseMapping import hkpBreakableMultiMaterialInverseMapping


class hkpBreakableMultiMaterial(hkpBreakableMaterial):
    subMaterials: hkpBreakableMaterial
    inverseMapping: hkpBreakableMultiMaterialInverseMapping

    def __init__(self, infile):
        self.subMaterials = hkpBreakableMaterial(infile)  # TYPE_ARRAY
        self.inverseMapping = hkpBreakableMultiMaterialInverseMapping(infile)  # TYPE_POINTER
