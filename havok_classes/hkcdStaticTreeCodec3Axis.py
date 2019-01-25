import struct


class hkcdStaticTreeCodec3Axis(object):
    xyz: int

    def __init__(self, infile):
        self.xyz = struct.unpack('>B', infile.read(1))
