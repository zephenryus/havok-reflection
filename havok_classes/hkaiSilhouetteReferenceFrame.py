import struct


class hkaiSilhouetteReferenceFrame(object):
    up: vector4
    referenceAxis: vector4
    orthogonalAxis: vector4

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.referenceAxis = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.orthogonalAxis = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} up={up}, referenceAxis={referenceAxis}, orthogonalAxis={orthogonalAxis}>".format(**{
            "class_name": self.__class__.__name__,
            "up": self.up,
            "referenceAxis": self.referenceAxis,
            "orthogonalAxis": self.orthogonalAxis,
        })
