from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkpLinearClearanceConstraintDataAtoms import hkpLinearClearanceConstraintDataAtoms


class Type(Enum):
    PRISMATIC = 0
    HINGE = 1
    BALL_SOCKET = 2


class hkpLinearClearanceConstraintData(hkpConstraintData):
    atoms: hkpLinearClearanceConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpLinearClearanceConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
