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
        self.vertexBufferIndex = struct.unpack('>B', infile.read(1))
        self.elementIndex = struct.unpack('>B', infile.read(1))
        self.lockedBufferIndex = struct.unpack('>B', infile.read(1))
        self.vertexFormatIndex = struct.unpack('>B', infile.read(1))
        self.lockFlags = struct.unpack('>B', infile.read(1))
        self.outputBufferIndex = struct.unpack('>B', infile.read(1))
        self.emulatedIndex = struct.unpack('>b', infile.read(1))
