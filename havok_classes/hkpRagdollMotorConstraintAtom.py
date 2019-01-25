from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .common import any
from .hkpConstraintMotor import hkpConstraintMotor


class hkpRagdollMotorConstraintAtom(hkpConstraintAtom):
    isEnabled: bool
    initializedOffset: int
    previousTargetAnglesOffset: int
    target_bRca: any
    motors: hkpConstraintMotor

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>?', infile.read(1))
        self.initializedOffset = struct.unpack('>h', infile.read(2))
        self.previousTargetAnglesOffset = struct.unpack('>h', infile.read(2))
        self.target_bRca = any(infile)  # TYPE_MATRIX3
        self.motors = hkpConstraintMotor(infile)  # TYPE_POINTER
