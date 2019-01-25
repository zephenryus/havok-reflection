from .hkpConstraintData import hkpConstraintData
from .hkpStiffSpringConstraintDataAtoms import hkpStiffSpringConstraintDataAtoms


class hkpStiffSpringConstraintData(hkpConstraintData):
    atoms: hkpStiffSpringConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpStiffSpringConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
