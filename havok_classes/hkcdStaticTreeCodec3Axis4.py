from .hkcdStaticTreeCodec3Axis import hkcdStaticTreeCodec3Axis
import struct


class hkcdStaticTreeCodec3Axis4(hkcdStaticTreeCodec3Axis):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>B', infile.read(1))
