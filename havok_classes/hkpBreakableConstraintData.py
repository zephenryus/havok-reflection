from .hkpWrappedConstraintData import hkpWrappedConstraintData
from .hkpBridgeAtoms import hkpBridgeAtoms
import struct


class hkpBreakableConstraintData(hkpWrappedConstraintData):
    atoms: hkpBridgeAtoms
    childRuntimeSize: int
    childNumSolverResults: int
    solverResultLimit: float
    removeWhenBroken: bool
    revertBackVelocityOnBreak: bool

    def __init__(self, infile):
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT
        self.childRuntimeSize = struct.unpack('>H', infile.read(2))
        self.childNumSolverResults = struct.unpack('>H', infile.read(2))
        self.solverResultLimit = struct.unpack('>f', infile.read(4))
        self.removeWhenBroken = struct.unpack('>?', infile.read(1))
        self.revertBackVelocityOnBreak = struct.unpack('>?', infile.read(1))
