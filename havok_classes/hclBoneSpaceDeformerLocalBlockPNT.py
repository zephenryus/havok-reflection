import struct


class hclBoneSpaceDeformerLocalBlockPNT(object):
    localPosition: vector4
    localNormal: int
    localTangent: int

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.localNormal = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID
        self.localTangent = struct.unpack('>h', infile.read(2))  # TYPE_INT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localPosition={localPosition}, localNormal={localNormal}, localTangent={localTangent}>".format(**{
            "class_name": self.__class__.__name__,
            "localPosition": self.localPosition,
            "localNormal": self.localNormal,
            "localTangent": self.localTangent,
        })
