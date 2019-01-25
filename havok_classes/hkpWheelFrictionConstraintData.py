from .hkpConstraintData import hkpConstraintData
from .hkpWheelFrictionConstraintDataAtoms import hkpWheelFrictionConstraintDataAtoms


class hkpWheelFrictionConstraintData(hkpConstraintData):
    atoms: hkpWheelFrictionConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpWheelFrictionConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
