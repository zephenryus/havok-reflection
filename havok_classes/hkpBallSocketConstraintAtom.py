from .hkpConstraintAtom import hkpConstraintAtom
from .enums import SolvingMethod
import struct
from .hkUFloat8 import hkUFloat8


class hkpBallSocketConstraintAtom(hkpConstraintAtom):
    solvingMethod: SolvingMethod
    bodiesToNotify: int
    velocityStabilizationFactor: hkUFloat8
    enableLinearImpulseLimit: bool
    breachImpulse: float
    inertiaStabilizationFactor: float

    def __init__(self, infile):
        self.solvingMethod = SolvingMethod(infile)  # TYPE_ENUM
        self.bodiesToNotify = struct.unpack('>B', infile.read(1))
        self.velocityStabilizationFactor = hkUFloat8(infile)  # TYPE_STRUCT
        self.enableLinearImpulseLimit = struct.unpack('>?', infile.read(1))
        self.breachImpulse = struct.unpack('>f', infile.read(4))
        self.inertiaStabilizationFactor = struct.unpack('>f', infile.read(4))
