from .hkpConstraintData import hkpConstraintData
from .hkpDeformableFixedConstraintDataAtoms import hkpDeformableFixedConstraintDataAtoms


class hkpDeformableFixedConstraintData(hkpConstraintData):
    atoms: hkpDeformableFixedConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpDeformableFixedConstraintDataAtoms(infile)  # TYPE_STRUCT
