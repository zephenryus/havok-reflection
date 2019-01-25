import struct


class hkpTyremarkPoint(object):
    pointLeft: vector4
    pointRight: vector4

    def __init__(self, infile):
        self.pointLeft = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.pointRight = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} pointLeft={pointLeft}, pointRight={pointRight}>".format(**{
            "class_name": self.__class__.__name__,
            "pointLeft": self.pointLeft,
            "pointRight": self.pointRight,
        })
