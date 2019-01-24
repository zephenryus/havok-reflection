from .hkpConstraintData import hkpConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms
from .hkpGenericConstraintDataScheme import hkpGenericConstraintDataScheme


class hkpGenericConstraintData(hkpConstraintData):
    atoms: hkpBridgeAtoms
    scheme: hkpGenericConstraintDataScheme
