from .hkcdStaticTreeCodec3Axis import hkcdStaticTreeCodec3Axis
import struct


class hkcdStaticTreeCodec3Axis4(hkcdStaticTreeCodec3Axis):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
        })
