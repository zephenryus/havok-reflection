import struct


class hkMultipleVertexBufferLockedElement(object):
    vertexBufferIndex: int
    elementIndex: int
    lockedBufferIndex: int
    vertexFormatIndex: int
    lockFlags: int
    outputBufferIndex: int
    emulatedIndex: int

    def __init__(self, infile):
        self.vertexBufferIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.elementIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.lockedBufferIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.vertexFormatIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.lockFlags = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.outputBufferIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.emulatedIndex = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexBufferIndex={vertexBufferIndex}, elementIndex={elementIndex}, lockedBufferIndex={lockedBufferIndex}, vertexFormatIndex={vertexFormatIndex}, lockFlags={lockFlags}, outputBufferIndex={outputBufferIndex}, emulatedIndex={emulatedIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexBufferIndex": self.vertexBufferIndex,
            "elementIndex": self.elementIndex,
            "lockedBufferIndex": self.lockedBufferIndex,
            "vertexFormatIndex": self.vertexFormatIndex,
            "lockFlags": self.lockFlags,
            "outputBufferIndex": self.outputBufferIndex,
            "emulatedIndex": self.emulatedIndex,
        })
