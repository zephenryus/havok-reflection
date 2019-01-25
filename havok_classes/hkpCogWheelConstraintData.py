from .hkpConstraintData import hkpConstraintData
from .hkpCogWheelConstraintDataAtoms import hkpCogWheelConstraintDataAtoms


class hkpCogWheelConstraintData(hkpConstraintData):
    atoms: hkpCogWheelConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpCogWheelConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
