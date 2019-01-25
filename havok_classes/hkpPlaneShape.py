from .hkpHeightFieldShape import hkpHeightFieldShape
import struct


class hkpPlaneShape(hkpHeightFieldShape):
    plane: vector4
    aabbCenter: vector4
    aabbHalfExtents: vector4

    def __init__(self, infile):
        self.plane = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.aabbCenter = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} plane={plane}, aabbCenter={aabbCenter}, aabbHalfExtents={aabbHalfExtents}>".format(**{
            "class_name": self.__class__.__name__,
            "plane": self.plane,
            "aabbCenter": self.aabbCenter,
            "aabbHalfExtents": self.aabbHalfExtents,
        })
