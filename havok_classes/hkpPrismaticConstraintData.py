from .hkpConstraintData import hkpConstraintData
from .hkpPrismaticConstraintDataAtoms import hkpPrismaticConstraintDataAtoms


class hkpPrismaticConstraintData(hkpConstraintData):
    atoms: hkpPrismaticConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpPrismaticConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
