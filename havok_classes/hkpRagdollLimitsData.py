from .hkpConstraintData import hkpConstraintData
from .hkpRagdollLimitsDataAtoms import hkpRagdollLimitsDataAtoms


class hkpRagdollLimitsData(hkpConstraintData):
    atoms: hkpRagdollLimitsDataAtoms

    def __init__(self, infile):
        self.atoms = hkpRagdollLimitsDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
