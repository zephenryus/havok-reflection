import struct


class hkcdStaticTreeCodec3Axis(object):
    xyz: int

    def __init__(self, infile):
        self.xyz = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} xyz={xyz}>".format(**{
            "class_name": self.__class__.__name__,
            "xyz": self.xyz,
        })
