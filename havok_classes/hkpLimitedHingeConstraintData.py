from .hkpConstraintData import hkpConstraintData
from .hkpLimitedHingeConstraintDataAtoms import hkpLimitedHingeConstraintDataAtoms


class hkpLimitedHingeConstraintData(hkpConstraintData):
    atoms: hkpLimitedHingeConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpLimitedHingeConstraintDataAtoms(infile)  # TYPE_STRUCT
