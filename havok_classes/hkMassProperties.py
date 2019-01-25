import struct


class hkMassProperties(object):
    volume: float
    mass: float
    centerOfMass: vector4
    inertiaTensor: any

    def __init__(self, infile):
        self.volume = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.mass = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.centerOfMass = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.inertiaTensor = any(infile)  # TYPE_MATRIX3:TYPE_VOID

    def __repr__(self):
        return "<{class_name} volume={volume}, mass={mass}, centerOfMass={centerOfMass}, inertiaTensor={inertiaTensor}>".format(**{
            "class_name": self.__class__.__name__,
            "volume": self.volume,
            "mass": self.mass,
            "centerOfMass": self.centerOfMass,
            "inertiaTensor": self.inertiaTensor,
        })
