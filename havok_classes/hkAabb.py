import struct


class hkAabb(object):
    min: vector4
    max: vector4

    def __init__(self, infile):
        self.min = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.max = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} min={min}, max={max}>".format(**{
            "class_name": self.__class__.__name__,
            "min": self.min,
            "max": self.max,
        })
