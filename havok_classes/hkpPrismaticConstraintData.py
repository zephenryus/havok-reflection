from .hkpConstraintData import hkpConstraintData
from .hkpPrismaticConstraintDataAtoms import hkpPrismaticConstraintDataAtoms


class hkpPrismaticConstraintData(hkpConstraintData):
    atoms: hkpPrismaticConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpPrismaticConstraintDataAtoms(infile)  # TYPE_STRUCT
