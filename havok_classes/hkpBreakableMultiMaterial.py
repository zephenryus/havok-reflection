from .hkpBreakableMaterial import hkpBreakableMaterial
from .hkpBreakableMultiMaterialInverseMapping import hkpBreakableMultiMaterialInverseMapping


class hkpBreakableMultiMaterial(hkpBreakableMaterial):
    subMaterials: hkpBreakableMaterial
    inverseMapping: hkpBreakableMultiMaterialInverseMapping
