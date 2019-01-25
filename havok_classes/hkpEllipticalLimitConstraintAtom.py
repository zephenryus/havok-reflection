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
        self.isEnabled = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.elipticalLimitEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.coneLimitEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.angle0 = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angle1 = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.coneAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angleCorrected0 = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angleCorrected1 = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.coneAngleCorrected = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angleCorrected0Inv = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angleCorrected1Inv = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsTauFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.angularLimitsDampFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} isEnabled={isEnabled}, elipticalLimitEnabled={elipticalLimitEnabled}, coneLimitEnabled={coneLimitEnabled}, angle0={angle0}, angle1={angle1}, coneAngle={coneAngle}, angleCorrected0={angleCorrected0}, angleCorrected1={angleCorrected1}, coneAngleCorrected={coneAngleCorrected}, angleCorrected0Inv={angleCorrected0Inv}, angleCorrected1Inv={angleCorrected1Inv}, angularLimitsTauFactor={angularLimitsTauFactor}, angularLimitsDampFactor={angularLimitsDampFactor}>".format(**{
            "class_name": self.__class__.__name__,
            "isEnabled": self.isEnabled,
            "elipticalLimitEnabled": self.elipticalLimitEnabled,
            "coneLimitEnabled": self.coneLimitEnabled,
            "angle0": self.angle0,
            "angle1": self.angle1,
            "coneAngle": self.coneAngle,
            "angleCorrected0": self.angleCorrected0,
            "angleCorrected1": self.angleCorrected1,
            "coneAngleCorrected": self.coneAngleCorrected,
            "angleCorrected0Inv": self.angleCorrected0Inv,
            "angleCorrected1Inv": self.angleCorrected1Inv,
            "angularLimitsTauFactor": self.angularLimitsTauFactor,
            "angularLimitsDampFactor": self.angularLimitsDampFactor,
        })
