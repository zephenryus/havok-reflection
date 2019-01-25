from .hkpConstraintData import hkpConstraintData
from .hkpFixedConstraintDataAtoms import hkpFixedConstraintDataAtoms


class hkpFixedConstraintData(hkpConstraintData):
    atoms: hkpFixedConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpFixedConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
