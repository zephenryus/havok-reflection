import struct


class hclSimClothDataParticleData(object):
    mass: float
    invMass: float
    radius: float
    friction: float

    def __init__(self, infile):
        self.mass = struct.unpack('>f', infile.read(4))
        self.invMass = struct.unpack('>f', infile.read(4))
        self.radius = struct.unpack('>f', infile.read(4))
        self.friction = struct.unpack('>f', infile.read(4))
