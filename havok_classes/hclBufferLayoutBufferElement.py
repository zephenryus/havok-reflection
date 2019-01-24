from .enums import VectorConversion


class hclBufferLayoutBufferElement(object):
    vectorConversion: VectorConversion
    vectorSize: int
    slotId: int
    slotStart: int
