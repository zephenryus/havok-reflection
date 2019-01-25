import struct
from .hclTransformSetUsage import hclTransformSetUsage


class hclClothStateTransformSetAccess(object):
    transformSetIndex: int
    transformSetUsage: hclTransformSetUsage

    def __init__(self, infile):
        self.transformSetIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.transformSetUsage = hclTransformSetUsage(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} transformSetIndex={transformSetIndex}, transformSetUsage={transformSetUsage}>".format(**{
            "class_name": self.__class__.__name__,
            "transformSetIndex": self.transformSetIndex,
            "transformSetUsage": self.transformSetUsage,
        })
