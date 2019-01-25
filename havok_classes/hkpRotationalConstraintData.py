from .hkpConstraintData import hkpConstraintData
from .hkpRotationalConstraintDataAtoms import hkpRotationalConstraintDataAtoms


class hkpRotationalConstraintData(hkpConstraintData):
    atoms: hkpRotationalConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpRotationalConstraintDataAtoms(infile)  # TYPE_STRUCT
