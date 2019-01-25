from .hkpBreakableMaterial import hkpBreakableMaterial
from typing import List
from .common import get_array
from .hkpBreakableMultiMaterialInverseMapping import hkpBreakableMultiMaterialInverseMapping


class hkpBreakableMultiMaterial(hkpBreakableMaterial):
    subMaterials: List[hkpBreakableMaterial]
    inverseMapping: any

    def __init__(self, infile):
        self.subMaterials = get_array(infile, hkpBreakableMaterial, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.inverseMapping = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} subMaterials=[{subMaterials}], inverseMapping={inverseMapping}>".format(**{
            "class_name": self.__class__.__name__,
            "subMaterials": self.subMaterials,
            "inverseMapping": self.inverseMapping,
        })
