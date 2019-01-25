from .enums import ComponentType, ComponentUsage
import struct


class hkVertexFormatElement(object):
    dataType: ComponentType
    numValues: int
    usage: ComponentUsage
    subUsage: int
    flags: any
    pad: int

    def __init__(self, infile):
        self.dataType = ComponentType(infile)  # TYPE_ENUM:TYPE_UINT8
        self.numValues = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.usage = ComponentUsage(infile)  # TYPE_ENUM:TYPE_UINT8
        self.subUsage = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.pad = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} dataType={dataType}, numValues={numValues}, usage={usage}, subUsage={subUsage}, flags={flags}, pad={pad}>".format(**{
            "class_name": self.__class__.__name__,
            "dataType": self.dataType,
            "numValues": self.numValues,
            "usage": self.usage,
            "subUsage": self.subUsage,
            "flags": self.flags,
            "pad": self.pad,
        })
