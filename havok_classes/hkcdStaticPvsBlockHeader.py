import struct


class hkcdStaticPvsBlockHeader(object):
    offset: int
    length: int

    def __init__(self, infile):
        self.offset = struct.unpack('>I', infile.read(4))
        self.length = struct.unpack('>I', infile.read(4))
