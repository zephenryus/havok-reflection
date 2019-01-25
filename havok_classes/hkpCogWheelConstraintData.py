from .hkpConstraintData import hkpConstraintData
from .hkpCogWheelConstraintDataAtoms import hkpCogWheelConstraintDataAtoms


class hkpCogWheelConstraintData(hkpConstraintData):
    atoms: hkpCogWheelConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpCogWheelConstraintDataAtoms(infile)  # TYPE_STRUCT
