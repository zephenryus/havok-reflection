import struct


class hkMonitorStreamColorTableColorPair(object):
    colorName: str
    color: int

    def __init__(self, infile):
        self.colorName = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.color = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} colorName=\"{colorName}\", color={color}>".format(**{
            "class_name": self.__class__.__name__,
            "colorName": self.colorName,
            "color": self.color,
        })
