from .hkpConstraintData import hkpConstraintData
from .hkpHingeConstraintDataAtoms import hkpHingeConstraintDataAtoms


class hkpHingeConstraintData(hkpConstraintData):
    atoms: hkpHingeConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpHingeConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
