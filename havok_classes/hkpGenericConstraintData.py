from .hkpConstraintData import hkpConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpGenericConstraintDataScheme import hkpGenericConstraintDataScheme


class hkpGenericConstraintData(hkpConstraintData):
    atoms: hkpBridgeAtoms
    scheme: hkpGenericConstraintDataScheme

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.scheme = hkpGenericConstraintDataScheme(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, scheme={scheme}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "scheme": self.scheme,
        })
