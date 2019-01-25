from .hkpConstraintData import hkpConstraintData
from .hkpBallAndSocketConstraintDataAtoms import hkpBallAndSocketConstraintDataAtoms


class hkpBallAndSocketConstraintData(hkpConstraintData):
    atoms: hkpBallAndSocketConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpBallAndSocketConstraintDataAtoms(infile)  # TYPE_STRUCT
