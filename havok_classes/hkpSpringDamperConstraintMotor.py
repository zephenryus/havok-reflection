from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
import struct


class hkpSpringDamperConstraintMotor(hkpLimitedForceConstraintMotor):
    springConstant: float
    springDamping: float

    def __init__(self, infile):
        self.springConstant = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.springDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} springConstant={springConstant}, springDamping={springDamping}>".format(**{
            "class_name": self.__class__.__name__,
            "springConstant": self.springConstant,
            "springDamping": self.springDamping,
        })
