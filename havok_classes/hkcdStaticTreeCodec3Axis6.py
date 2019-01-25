from .hkcdStaticTreeCodec3Axis import hkcdStaticTreeCodec3Axis
import struct


class hkcdStaticTreeCodec3Axis6(hkcdStaticTreeCodec3Axis):
    hiData: int
    loData: int

    def __init__(self, infile):
        self.hiData = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.loData = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} hiData={hiData}, loData={loData}>".format(**{
            "class_name": self.__class__.__name__,
            "hiData": self.hiData,
            "loData": self.loData,
        })
