from .enums import SlotFlags
import struct


class hclBufferLayoutSlot(object):
    flags: SlotFlags
    stride: int

    def __init__(self, infile):
        self.flags = SlotFlags(infile)  # TYPE_ENUM:TYPE_UINT8
        self.stride = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} flags={flags}, stride={stride}>".format(**{
            "class_name": self.__class__.__name__,
            "flags": self.flags,
            "stride": self.stride,
        })
