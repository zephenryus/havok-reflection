from .hkpConstraintData import hkpConstraintData
from .hkpPointToPlaneConstraintDataAtoms import hkpPointToPlaneConstraintDataAtoms


class hkpPointToPlaneConstraintData(hkpConstraintData):
    atoms: hkpPointToPlaneConstraintDataAtoms

    def __init__(self, infile):
        self.atoms = hkpPointToPlaneConstraintDataAtoms(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
        })
