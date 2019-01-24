from .enums import ComponentType, ComponentUsage
from .common import any


class hkVertexFormatElement(object):
    dataType: ComponentType
    numValues: int
    usage: ComponentUsage
    subUsage: int
    flags: any
    pad: int
