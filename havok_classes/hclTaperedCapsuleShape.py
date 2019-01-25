from .hclShape import hclShape
from .common import vector4
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
        self.small = struct.unpack('>4f', infile.read(16))
        self.big = struct.unpack('>4f', infile.read(16))
        self.coneApex = struct.unpack('>4f', infile.read(16))
        self.coneAxis = struct.unpack('>4f', infile.read(16))
        self.lVec = struct.unpack('>4f', infile.read(16))
        self.dVec = struct.unpack('>4f', infile.read(16))
        self.tanThetaVecNeg = struct.unpack('>4f', infile.read(16))
        self.smallRadius = struct.unpack('>f', infile.read(4))
        self.bigRadius = struct.unpack('>f', infile.read(4))
        self.l = struct.unpack('>f', infile.read(4))
        self.d = struct.unpack('>f', infile.read(4))
        self.cosTheta = struct.unpack('>f', infile.read(4))
        self.sinTheta = struct.unpack('>f', infile.read(4))
        self.tanTheta = struct.unpack('>f', infile.read(4))
        self.tanThetaSqr = struct.unpack('>f', infile.read(4))
