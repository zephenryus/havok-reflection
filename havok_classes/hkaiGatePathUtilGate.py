import struct


class hkaiGatePathUtilGate(object):
    origin: vector4
    uLen: float
    vLen: float
    type: enumerate

    def __init__(self, infile):
        self.origin = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.uLen = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.vLen = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.type = enumerate(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} origin={origin}, uLen={uLen}, vLen={vLen}, type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "origin": self.origin,
            "uLen": self.uLen,
            "vLen": self.vLen,
            "type": self.type,
        })
