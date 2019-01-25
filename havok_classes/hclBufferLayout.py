from enum import Enum
from .hclBufferLayoutBufferElement import hclBufferLayoutBufferElement
from .hclBufferLayoutSlot import hclBufferLayoutSlot
import struct
from .enums import TriangleFormat


class SlotFlags(Enum):
    SF_NO_ALIGNED_START = 0
    SF_16BYTE_ALIGNED_START = 1
    SF_64BYTE_ALIGNED_START = 3


class TriangleFormat(Enum):
    TF_THREE_INT32S = 0
    TF_THREE_INT16S = 1
    TF_OTHER = 2


class hclBufferLayout(object):
    elementsLayout: hclBufferLayoutBufferElement
    slots: hclBufferLayoutSlot
    numSlots: int
    triangleFormat: TriangleFormat

    def __init__(self, infile):
        self.elementsLayout = hclBufferLayoutBufferElement(infile)  # TYPE_STRUCT:TYPE_VOID
        self.slots = hclBufferLayoutSlot(infile)  # TYPE_STRUCT:TYPE_VOID
        self.numSlots = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.triangleFormat = TriangleFormat(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} elementsLayout={elementsLayout}, slots={slots}, numSlots={numSlots}, triangleFormat={triangleFormat}>".format(**{
            "class_name": self.__class__.__name__,
            "elementsLayout": self.elementsLayout,
            "slots": self.slots,
            "numSlots": self.numSlots,
            "triangleFormat": self.triangleFormat,
        })
