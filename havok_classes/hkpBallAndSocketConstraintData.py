from .hkpConstraintData import hkpConstraintData
from .hkpBallAndSocketConstraintDataAtoms import hkpBallAndSocketConstraintDataAtoms


class hkpBallAndSocketConstraintData(hkpConstraintData):
    atoms: hkpBallAndSocketConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpBallAndSocketConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
