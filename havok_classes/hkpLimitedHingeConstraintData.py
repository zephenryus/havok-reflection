from .hkpConstraintData import hkpConstraintData
from .hkpLimitedHingeConstraintDataAtoms import hkpLimitedHingeConstraintDataAtoms


class hkpLimitedHingeConstraintData(hkpConstraintData):
    atoms: hkpLimitedHingeConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpLimitedHingeConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
