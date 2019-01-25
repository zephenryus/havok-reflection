import struct


class hkMultipleVertexBufferElementInfo(object):
    vertexBufferIndex: int
    elementIndex: int

    def __init__(self, infile):
        self.vertexBufferIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.elementIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexBufferIndex={vertexBufferIndex}, elementIndex={elementIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexBufferIndex": self.vertexBufferIndex,
            "elementIndex": self.elementIndex,
        })
