from .hkpConstraintData import hkpConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpGenericConstraintDataScheme import hkpGenericConstraintDataScheme


class hkpGenericConstraintData(hkpConstraintData):
    atoms: hkpBridgeAtoms
    scheme: hkpGenericConstraintDataScheme

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT
        self.scheme = hkpGenericConstraintDataScheme(infile)  # TYPE_STRUCT
