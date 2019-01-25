from .hkpConstraintData import hkpConstraintData
from .hkpRagdollLimitsDataAtoms import hkpRagdollLimitsDataAtoms


class hkpRagdollLimitsData(hkpConstraintData):
    atoms: hkpRagdollLimitsDataAtoms

    def __init__(self, infile):
        self.atoms = hkpRagdollLimitsDataAtoms(infile)  # TYPE_STRUCT
