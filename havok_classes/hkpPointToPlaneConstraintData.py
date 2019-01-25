from .hkpConstraintData import hkpConstraintData
from .hkpPointToPlaneConstraintDataAtoms import hkpPointToPlaneConstraintDataAtoms


class hkpPointToPlaneConstraintData(hkpConstraintData):
    atoms: hkpPointToPlaneConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpPointToPlaneConstraintDataAtoms(infile)  # TYPE_STRUCT
