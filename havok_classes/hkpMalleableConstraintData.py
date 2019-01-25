from .hkpWrappedConstraintData import hkpWrappedConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms
import struct


class hkpMalleableConstraintData(hkpWrappedConstraintData):
    atoms: hkpBridgeAtoms
    strength: float

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT
        self.strength = struct.unpack('>f', infile.read(4))
