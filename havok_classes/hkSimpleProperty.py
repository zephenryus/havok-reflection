import struct
from .hkSimplePropertyValue import hkSimplePropertyValue


class hkSimpleProperty(object):
    key: int
    alignmentPadding: int
    value: hkSimplePropertyValue

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.alignmentPadding = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.value = hkSimplePropertyValue(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} key={key}, alignmentPadding={alignmentPadding}, value={value}>".format(**{
            "class_name": self.__class__.__name__,
            "key": self.key,
            "alignmentPadding": self.alignmentPadding,
            "value": self.value,
        })
