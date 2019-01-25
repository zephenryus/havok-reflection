from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpStiffSpringConstraintAtom(hkpConstraintAtom):
    length: float
    maxLength: float
    springConstant: float
    springDamping: float

    def __init__(self, infile):
        self.length = struct.unpack('>f', infile.read(4))
        self.maxLength = struct.unpack('>f', infile.read(4))
        self.springConstant = struct.unpack('>f', infile.read(4))
        self.springDamping = struct.unpack('>f', infile.read(4))
