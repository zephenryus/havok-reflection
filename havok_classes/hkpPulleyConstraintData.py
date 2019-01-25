from .hkpConstraintData import hkpConstraintData
from .hkpPulleyConstraintDataAtoms import hkpPulleyConstraintDataAtoms


class hkpPulleyConstraintData(hkpConstraintData):
    atoms: hkpPulleyConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpPulleyConstraintDataAtoms(infile)  # TYPE_STRUCT
