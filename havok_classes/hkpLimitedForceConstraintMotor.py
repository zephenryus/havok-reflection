from .hkpConstraintMotor import hkpConstraintMotor
import struct


class hkpLimitedForceConstraintMotor(hkpConstraintMotor):
    minForce: float
    maxForce: float

    def __init__(self, infile):
        self.minForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} minForce={minForce}, maxForce={maxForce}>".format(**{
            "class_name": self.__class__.__name__,
            "minForce": self.minForce,
            "maxForce": self.maxForce,
        })
