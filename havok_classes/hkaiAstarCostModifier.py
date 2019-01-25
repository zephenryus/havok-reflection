from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import CostModifierType


class CostModifierType(Enum):
    COST_MODIFIER_DEFAULT = 0
    COST_MODIFIER_USER = 1


class hkaiAstarCostModifier(hkReferencedObject):
    type: CostModifierType

    def __init__(self, infile):
        self.type = CostModifierType(infile)  # TYPE_ENUM
