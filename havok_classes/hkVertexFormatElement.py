from .enums import ComponentType, ComponentUsage
import struct
from .common import any


class hkVertexFormatElement(object):
    dataType: ComponentType
    numValues: int
    usage: ComponentUsage
    subUsage: int
    flags: any
    pad: int

    def __init__(self, infile):
        self.dataType = ComponentType(infile)  # TYPE_ENUM
        self.numValues = struct.unpack('>B', infile.read(1))
        self.usage = ComponentUsage(infile)  # TYPE_ENUM
        self.subUsage = struct.unpack('>B', infile.read(1))
        self.flags = any(infile)  # TYPE_FLAGS
        self.pad = struct.unpack('>B', infile.read(1))
