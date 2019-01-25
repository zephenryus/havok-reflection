from .enums import SlotFlags
import struct


class hclBufferLayoutSlot(object):
    flags: SlotFlags
    stride: int

    def __init__(self, infile):
        self.flags = SlotFlags(infile)  # TYPE_ENUM
        self.stride = struct.unpack('>B', infile.read(1))
