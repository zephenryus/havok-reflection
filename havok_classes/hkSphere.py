import struct


class hkSphere(object):
    pos: vector4

    def __init__(self, infile):
        self.pos = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pos={pos}>".format(**{
            "class_name": self.__class__.__name__,
            "pos": self.pos,
        })
