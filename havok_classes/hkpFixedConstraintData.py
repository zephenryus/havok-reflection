from .hkpConstraintData import hkpConstraintData
from .hkpFixedConstraintDataAtoms import hkpFixedConstraintDataAtoms


class hkpFixedConstraintData(hkpConstraintData):
    atoms: hkpFixedConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpFixedConstraintDataAtoms(infile)  # TYPE_STRUCT
