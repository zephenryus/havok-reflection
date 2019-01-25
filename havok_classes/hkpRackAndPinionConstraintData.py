from .hkpConstraintData import hkpConstraintData
from enum import Enum
from .hkpRackAndPinionConstraintDataAtoms import hkpRackAndPinionConstraintDataAtoms


class Type(Enum):
    TYPE_RACK_AND_PINION = 0
    TYPE_SCREW = 1


class hkpRackAndPinionConstraintData(hkpConstraintData):
    atoms: hkpRackAndPinionConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpRackAndPinionConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
