import struct


class hclSimClothDataParticleData(object):
    mass: float
    invMass: float
    radius: float
    friction: float

    def __init__(self, infile):
        self.mass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.invMass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.friction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} mass={mass}, invMass={invMass}, radius={radius}, friction={friction}>".format(**{
            "class_name": self.__class__.__name__,
            "mass": self.mass,
            "invMass": self.invMass,
            "radius": self.radius,
            "friction": self.friction,
        })
