import struct


class hkMonitorStreamColorTableColorPair(object):
    colorName: str
    color: int

    def __init__(self, infile):
        self.colorName = struct.unpack('>s', infile.read(0))
        self.color = struct.unpack('>I', infile.read(4))
