from .enums import DataUsage
import struct


class hkxVertexAnimationUsageMap(object):
    use: DataUsage
    useIndexOrig: int
    useIndexLocal: int

    def __init__(self, infile):
        self.use = DataUsage(infile)  # TYPE_ENUM:TYPE_UINT16
        self.useIndexOrig = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.useIndexLocal = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} use={use}, useIndexOrig={useIndexOrig}, useIndexLocal={useIndexLocal}>".format(**{
            "class_name": self.__class__.__name__,
            "use": self.use,
            "useIndexOrig": self.useIndexOrig,
            "useIndexLocal": self.useIndexLocal,
        })
