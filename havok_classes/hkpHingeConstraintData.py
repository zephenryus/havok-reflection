from .hkpConstraintData import hkpConstraintData
from .hkpHingeConstraintDataAtoms import hkpHingeConstraintDataAtoms


class hkpHingeConstraintData(hkpConstraintData):
    atoms: hkpHingeConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpHingeConstraintDataAtoms(infile)  # TYPE_STRUCT
