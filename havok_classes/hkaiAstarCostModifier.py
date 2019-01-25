from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .enums import CostModifierType


class CostModifierType(Enum):
    COST_MODIFIER_DEFAULT = 0
    COST_MODIFIER_USER = 1


class hkaiAstarCostModifier(hkReferencedObject):
    type: CostModifierType

    def __init__(self, infile):
        self.type = CostModifierType(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
        })
