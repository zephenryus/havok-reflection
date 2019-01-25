import struct
from .hkpConstraintMotor import hkpConstraintMotor


class hkpPoweredChainDataConstraintInfo(object):
    pivotInA: vector4
    pivotInB: vector4
    aTc: any
    bTc: any
    motors: any
    switchBodies: bool

    def __init__(self, infile):
        self.pivotInA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.pivotInB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.aTc = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.bTc = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.motors = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.switchBodies = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pivotInA={pivotInA}, pivotInB={pivotInB}, aTc={aTc}, bTc={bTc}, motors={motors}, switchBodies={switchBodies}>".format(**{
            "class_name": self.__class__.__name__,
            "pivotInA": self.pivotInA,
            "pivotInB": self.pivotInB,
            "aTc": self.aTc,
            "bTc": self.bTc,
            "motors": self.motors,
            "switchBodies": self.switchBodies,
        })
