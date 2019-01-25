from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpStiffSpringConstraintAtom(hkpConstraintAtom):
    length: float
    maxLength: float
    springConstant: float
    springDamping: float

    def __init__(self, infile):
        self.length = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.springConstant = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.springDamping = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} length={length}, maxLength={maxLength}, springConstant={springConstant}, springDamping={springDamping}>".format(**{
            "class_name": self.__class__.__name__,
            "length": self.length,
            "maxLength": self.maxLength,
            "springConstant": self.springConstant,
            "springDamping": self.springDamping,
        })
