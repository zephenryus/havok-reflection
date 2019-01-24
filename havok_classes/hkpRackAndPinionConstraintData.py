from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkpRackAndPinionConstraintDataAtoms import hkpRackAndPinionConstraintDataAtoms


class Type(Enum):
    TYPE_RACK_AND_PINION = 0
    TYPE_SCREW = 1


class hkpRackAndPinionConstraintData(hkpConstraintData):
    atoms: hkpRackAndPinionConstraintDataAtoms
