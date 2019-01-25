from enum import Enum
import struct


class BoundIndex(Enum):
    X_MIN = 0
    X_MAX = 1
    Y_MIN = 2
    Y_MAX = 3
    Z_MIN = 4
    Z_MAX = 5


class hkcdFourAabb(object):
    lx: vector4
    hx: vector4
    ly: vector4
    hy: vector4
    lz: vector4
    hz: vector4

    def __init__(self, infile):
        self.lx = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.hx = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.ly = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.hy = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.lz = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.hz = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} lx={lx}, hx={hx}, ly={ly}, hy={hy}, lz={lz}, hz={hz}>".format(**{
            "class_name": self.__class__.__name__,
            "lx": self.lx,
            "hx": self.hx,
            "ly": self.ly,
            "hy": self.hy,
            "lz": self.lz,
            "hz": self.hz,
        })
