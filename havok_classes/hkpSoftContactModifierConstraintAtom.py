from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
import struct


class hkpSoftContactModifierConstraintAtom(hkpModifierConstraintAtom):
    tau: float
    maxAcceleration: float

    def __init__(self, infile):
        self.tau = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxAcceleration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} tau={tau}, maxAcceleration={maxAcceleration}>".format(**{
            "class_name": self.__class__.__name__,
            "tau": self.tau,
            "maxAcceleration": self.maxAcceleration,
        })
