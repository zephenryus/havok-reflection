import struct


class hclBoneSpaceDeformerLocalBlockUnpackedPN(object):
    localPosition: vector4
    localNormal: vector4

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.localNormal = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localPosition={localPosition}, localNormal={localNormal}>".format(**{
            "class_name": self.__class__.__name__,
            "localPosition": self.localPosition,
            "localNormal": self.localNormal,
        })
