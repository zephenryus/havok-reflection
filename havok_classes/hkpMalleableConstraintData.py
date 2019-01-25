from .hkpWrappedConstraintData import hkpWrappedConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms
import struct


class hkpMalleableConstraintData(hkpWrappedConstraintData):
    atoms: hkpBridgeAtoms
    strength: float

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.strength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, strength={strength}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "strength": self.strength,
        })
