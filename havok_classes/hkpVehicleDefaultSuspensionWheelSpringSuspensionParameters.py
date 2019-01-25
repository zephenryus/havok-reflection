import struct


class hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters(object):
    strength: float
    dampingCompression: float
    dampingRelaxation: float

    def __init__(self, infile):
        self.strength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dampingCompression = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dampingRelaxation = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} strength={strength}, dampingCompression={dampingCompression}, dampingRelaxation={dampingRelaxation}>".format(**{
            "class_name": self.__class__.__name__,
            "strength": self.strength,
            "dampingCompression": self.dampingCompression,
            "dampingRelaxation": self.dampingRelaxation,
        })
