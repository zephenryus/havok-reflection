from .hkpConstraintData import hkpConstraintData
from .hkpWheelFrictionConstraintDataAtoms import hkpWheelFrictionConstraintDataAtoms


class hkpWheelFrictionConstraintData(hkpConstraintData):
    atoms: hkpWheelFrictionConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpWheelFrictionConstraintDataAtoms(infile)  # TYPE_STRUCT
