from .hkpConstraintData import hkpConstraintData
from .hkpHingeLimitsDataAtoms import hkpHingeLimitsDataAtoms


class hkpHingeLimitsData(hkpConstraintData):
    atoms: hkpHingeLimitsDataAtoms

    def __init__(self, infile):
        self.atoms = hkpHingeLimitsDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
