import struct


class hkMeshTextureRawBufferDescriptor(object):
    offset: int
    stride: int
    numElements: int

    def __init__(self, infile):
        self.offset = struct.unpack('>q', infile.read(8))  # TYPE_INT64:TYPE_VOID
        self.stride = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.numElements = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offset={offset}, stride={stride}, numElements={numElements}>".format(**{
            "class_name": self.__class__.__name__,
            "offset": self.offset,
            "stride": self.stride,
            "numElements": self.numElements,
        })
