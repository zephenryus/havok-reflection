from .hkpConstraintAtom import hkpConstraintAtom
import struct
from .hkpConstraintMotor import hkpConstraintMotor


class hkpRagdollMotorConstraintAtom(hkpConstraintAtom):
    isEnabled: bool
    initializedOffset: int
    previousTargetAnglesOffset: int
    target_bRca: any
    motors: any

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.initializedOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.previousTargetAnglesOffset = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.target_bRca = any(infile)  # TYPE_MATRIX3:TYPE_VOID
        self.motors = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, initializedOffset={initializedOffset}, previousTargetAnglesOffset={previousTargetAnglesOffset}, target_bRca={target_bRca}, motors={motors}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "initializedOffset": self.initializedOffset,
            "previousTargetAnglesOffset": self.previousTargetAnglesOffset,
            "target_bRca": self.target_bRca,
            "motors": self.motors,
        })
