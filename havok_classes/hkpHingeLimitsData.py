from .hkpConstraintData import hkpConstraintData
from .hkpHingeLimitsDataAtoms import hkpHingeLimitsDataAtoms


class hkpHingeLimitsData(hkpConstraintData):
    atoms: hkpHingeLimitsDataAtoms

    def __init__(self, infile):
        self.atoms = hkpHingeLimitsDataAtoms(infile)  # TYPE_STRUCT
