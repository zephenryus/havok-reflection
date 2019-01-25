from .hkcdStaticTreeCodec3Axis import hkcdStaticTreeCodec3Axis
import struct


class hkcdStaticTreeCodec3Axis6(hkcdStaticTreeCodec3Axis):
    hiData: int
    loData: int

    def __init__(self, infile):
        self.hiData = struct.unpack('>B', infile.read(1))
        self.loData = struct.unpack('>H', infile.read(2))
