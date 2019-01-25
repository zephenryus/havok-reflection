import struct


class hkaiGatePathSmoothOptions(object):
    minRounds: int
    maxRounds: int
    initialMinRounds: int
    initialMaxRounds: int
    quiescenceDistance: float
    quiescenceSinAngle: float

    def __init__(self, infile):
        self.minRounds = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.maxRounds = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.initialMinRounds = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.initialMaxRounds = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.quiescenceDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.quiescenceSinAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} minRounds={minRounds}, maxRounds={maxRounds}, initialMinRounds={initialMinRounds}, initialMaxRounds={initialMaxRounds}, quiescenceDistance={quiescenceDistance}, quiescenceSinAngle={quiescenceSinAngle}>".format(**{
            "class_name": self.__class__.__name__,
            "minRounds": self.minRounds,
            "maxRounds": self.maxRounds,
            "initialMinRounds": self.initialMinRounds,
            "initialMaxRounds": self.initialMaxRounds,
            "quiescenceDistance": self.quiescenceDistance,
            "quiescenceSinAngle": self.quiescenceSinAngle,
        })
