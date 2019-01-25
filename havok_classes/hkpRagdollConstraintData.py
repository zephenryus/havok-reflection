from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkpRagdollConstraintDataAtoms import hkpRagdollConstraintDataAtoms


class MotorIndex(Enum):
    MOTOR_TWIST = 0
    MOTOR_PLANE = 1
    MOTOR_CONE = 2
    NUM_MOTOR_INDICES = 3


class hkpRagdollConstraintData(hkpConstraintData):
    atoms: hkpRagdollConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpRagdollConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
