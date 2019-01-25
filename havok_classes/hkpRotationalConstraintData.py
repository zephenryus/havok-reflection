from .hkpConstraintData import hkpConstraintData
from .hkpRotationalConstraintDataAtoms import hkpRotationalConstraintDataAtoms


class hkpRotationalConstraintData(hkpConstraintData):
    atoms: hkpRotationalConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpRotationalConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
