import struct
from .hclTransformSetUsage import hclTransformSetUsage


class hclClothStateTransformSetAccess(object):
    transformSetIndex: int
    transformSetUsage: hclTransformSetUsage

    def __init__(self, infile):
        self.transformSetIndex = struct.unpack('>I', infile.read(4))
        self.transformSetUsage = hclTransformSetUsage(infile)  # TYPE_STRUCT
