from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkpLinearClearanceConstraintDataAtoms import hkpLinearClearanceConstraintDataAtoms


class Type(Enum):
    PRISMATIC = 0
    HINGE = 1
    BALL_SOCKET = 2


class hkpLinearClearanceConstraintData(hkpConstraintData):
    atoms: hkpLinearClearanceConstraintDataAtoms
