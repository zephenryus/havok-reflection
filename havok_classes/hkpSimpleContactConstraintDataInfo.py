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
        self.flags = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.biNormalAxis = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.rollingFrictionMultiplier = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.internalData1 = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.rhsRolling = struct.unpack('>h', infile.read(2))  # TYPE_HALF:TYPE_VOID
        self.contactRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.data = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} flags={flags}, biNormalAxis={biNormalAxis}, rollingFrictionMultiplier={rollingFrictionMultiplier}, internalData1={internalData1}, rhsRolling={rhsRolling}, contactRadius={contactRadius}, data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "flags": self.flags,
            "biNormalAxis": self.biNormalAxis,
            "rollingFrictionMultiplier": self.rollingFrictionMultiplier,
            "internalData1": self.internalData1,
            "rhsRolling": self.rhsRolling,
            "contactRadius": self.contactRadius,
            "data": self.data,
        })
