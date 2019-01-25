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
        self.solvingMethod = SolvingMethod(infile)  # TYPE_ENUM:TYPE_UINT8
        self.bodiesToNotify = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.velocityStabilizationFactor = hkUFloat8(infile)  # TYPE_STRUCT:TYPE_VOID
        self.enableLinearImpulseLimit = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.breachImpulse = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.inertiaStabilizationFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} solvingMethod={solvingMethod}, bodiesToNotify={bodiesToNotify}, velocityStabilizationFactor={velocityStabilizationFactor}, enableLinearImpulseLimit={enableLinearImpulseLimit}, breachImpulse={breachImpulse}, inertiaStabilizationFactor={inertiaStabilizationFactor}>".format(**{
            "class_name": self.__class__.__name__,
            "solvingMethod": self.solvingMethod,
            "bodiesToNotify": self.bodiesToNotify,
            "velocityStabilizationFactor": self.velocityStabilizationFactor,
            "enableLinearImpulseLimit": self.enableLinearImpulseLimit,
            "breachImpulse": self.breachImpulse,
            "inertiaStabilizationFactor": self.inertiaStabilizationFactor,
        })
