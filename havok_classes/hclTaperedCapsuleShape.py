from .hclShape import hclShape
import struct


class hclTaperedCapsuleShape(hclShape):
    small: vector4
    big: vector4
    coneApex: vector4
    coneAxis: vector4
    lVec: vector4
    dVec: vector4
    tanThetaVecNeg: vector4
    smallRadius: float
    bigRadius: float
    l: float
    d: float
    cosTheta: float
    sinTheta: float
    tanTheta: float
    tanThetaSqr: float

    def __init__(self, infile):
        self.small = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.big = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.coneApex = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.coneAxis = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.lVec = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.dVec = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.tanThetaVecNeg = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.smallRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bigRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.l = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.d = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cosTheta = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sinTheta = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.tanTheta = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.tanThetaSqr = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} small={small}, big={big}, coneApex={coneApex}, coneAxis={coneAxis}, lVec={lVec}, dVec={dVec}, tanThetaVecNeg={tanThetaVecNeg}, smallRadius={smallRadius}, bigRadius={bigRadius}, l={l}, d={d}, cosTheta={cosTheta}, sinTheta={sinTheta}, tanTheta={tanTheta}, tanThetaSqr={tanThetaSqr}>".format(**{
            "class_name": self.__class__.__name__,
            "small": self.small,
            "big": self.big,
            "coneApex": self.coneApex,
            "coneAxis": self.coneAxis,
            "lVec": self.lVec,
            "dVec": self.dVec,
            "tanThetaVecNeg": self.tanThetaVecNeg,
            "smallRadius": self.smallRadius,
            "bigRadius": self.bigRadius,
            "l": self.l,
            "d": self.d,
            "cosTheta": self.cosTheta,
            "sinTheta": self.sinTheta,
            "tanTheta": self.tanTheta,
            "tanThetaSqr": self.tanThetaSqr,
        })
