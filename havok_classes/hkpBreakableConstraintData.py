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
        self.atoms = hkpBridgeAtoms(infile)  # TYPE_STRUCT:TYPE_VOID
        self.childRuntimeSize = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.childNumSolverResults = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.solverResultLimit = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.removeWhenBroken = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.revertBackVelocityOnBreak = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} atoms={atoms}, childRuntimeSize={childRuntimeSize}, childNumSolverResults={childNumSolverResults}, solverResultLimit={solverResultLimit}, removeWhenBroken={removeWhenBroken}, revertBackVelocityOnBreak={revertBackVelocityOnBreak}>".format(**{
            "class_name": self.__class__.__name__,
            "atoms": self.atoms,
            "childRuntimeSize": self.childRuntimeSize,
            "childNumSolverResults": self.childNumSolverResults,
            "solverResultLimit": self.solverResultLimit,
            "removeWhenBroken": self.removeWhenBroken,
            "revertBackVelocityOnBreak": self.revertBackVelocityOnBreak,
        })
