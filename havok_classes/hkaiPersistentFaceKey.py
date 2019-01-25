import struct


class hkaiPersistentFaceKey(object):
    key: int
    offset: int

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))
        self.offset = struct.unpack('>h', infile.read(2))
