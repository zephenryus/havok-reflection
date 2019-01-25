import struct


class hkAabb16(object):
    min: int
    key: int
    max: int
    key1: int

    def __init__(self, infile):
        self.min = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.key = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.max = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.key1 = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} min={min}, key={key}, max={max}, key1={key1}>".format(**{
            "class_name": self.__class__.__name__,
            "min": self.min,
            "key": self.key,
            "max": self.max,
            "key1": self.key1,
        })
