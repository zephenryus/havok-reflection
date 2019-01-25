from .hkpConstraintAtom import hkpConstraintAtom
import struct


class hkpEllipticalLimitConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    elipticalLimitEnabled: bool
    coneLimitEnabled: bool
    angle0: float
    angle1: float
    coneAngle: float
    angleCorrected0: float
    angleCorrected1: float
    coneAngleCorrected: float
    angleCorrected0Inv: float
    angleCorrected1Inv: float
    angularLimitsTauFactor: float
    angularLimitsDampFactor: float

    def __init__(self, infile):
        self.isEnabled = struct.unpack('>B', infile.read(1))
        self.elipticalLimitEnabled = struct.unpack('>?', infile.read(1))
        self.coneLimitEnabled = struct.unpack('>?', infile.read(1))
        self.angle0 = struct.unpack('>f', infile.read(4))
        self.angle1 = struct.unpack('>f', infile.read(4))
        self.coneAngle = struct.unpack('>f', infile.read(4))
        self.angleCorrected0 = struct.unpack('>f', infile.read(4))
        self.angleCorrected1 = struct.unpack('>f', infile.read(4))
        self.coneAngleCorrected = struct.unpack('>f', infile.read(4))
        self.angleCorrected0Inv = struct.unpack('>f', infile.read(4))
        self.angleCorrected1Inv = struct.unpack('>f', infile.read(4))
        self.angularLimitsTauFactor = struct.unpack('>f', infile.read(4))
        self.angularLimitsDampFactor = struct.unpack('>f', infile.read(4))
