import struct


class hkaiAvoidancePairPropertiesPairData(object):
    key: int
    weight: float
    cosViewAngle: float

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.weight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cosViewAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} key={key}, weight={weight}, cosViewAngle={cosViewAngle}>".format(**{
            "class_name": self.__class__.__name__,
            "key": self.key,
            "weight": self.weight,
            "cosViewAngle": self.cosViewAngle,
        })
