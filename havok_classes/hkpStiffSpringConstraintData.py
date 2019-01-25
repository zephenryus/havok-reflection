from .hkpConstraintData import hkpConstraintData
from .hkpStiffSpringConstraintDataAtoms import hkpStiffSpringConstraintDataAtoms


class hkpStiffSpringConstraintData(hkpConstraintData):
    atoms: hkpStiffSpringConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpStiffSpringConstraintDataAtoms(infile)  # TYPE_STRUCT
