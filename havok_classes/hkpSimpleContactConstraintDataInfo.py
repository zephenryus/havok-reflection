import struct


class hkpSimpleContactConstraintDataInfo(object):
    flags: int
    biNormalAxis: int
    rollingFrictionMultiplier: int
    internalData1: int
    rhsRolling: int
    contactRadius: float
    data: float

    def __init__(self, infile):
        self.flags = struct.unpack('>H', infile.read(2))
        self.biNormalAxis = struct.unpack('>H', infile.read(2))
        self.rollingFrictionMultiplier = struct.unpack('>h', infile.read(2))
        self.internalData1 = struct.unpack('>h', infile.read(2))
        self.rhsRolling = struct.unpack('>h', infile.read(2))
        self.contactRadius = struct.unpack('>f', infile.read(4))
        self.data = struct.unpack('>f', infile.read(4))
