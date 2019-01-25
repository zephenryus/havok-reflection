import struct
from .hkSimplePropertyValue import hkSimplePropertyValue


class hkSimpleProperty(object):
    key: int
    alignmentPadding: int
    value: hkSimplePropertyValue

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))
        self.alignmentPadding = struct.unpack('>I', infile.read(4))
        self.value = hkSimplePropertyValue(infile)  # TYPE_STRUCT
