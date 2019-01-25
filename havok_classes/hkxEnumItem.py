import struct


class hkxEnumItem(object):
    value: int
    name: str

    def __init__(self, infile):
        self.value = struct.unpack('>i', infile.read(4))
        self.name = struct.unpack('>s', infile.read(0))
