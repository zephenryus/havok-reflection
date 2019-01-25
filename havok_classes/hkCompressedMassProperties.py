import struct


class hkCompressedMassProperties(object):
    centerOfMass: int
    inertia: int
    majorAxisSpace: int
    mass: float
    volume: float

    def __init__(self, infile):
        self.centerOfMass = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.inertia = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.majorAxisSpace = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.mass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.volume = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} centerOfMass={centerOfMass}, inertia={inertia}, majorAxisSpace={majorAxisSpace}, mass={mass}, volume={volume}>".format(**{
            "class_name": self.__class__.__name__,
            "centerOfMass": self.centerOfMass,
            "inertia": self.inertia,
            "majorAxisSpace": self.majorAxisSpace,
            "mass": self.mass,
            "volume": self.volume,
        })
