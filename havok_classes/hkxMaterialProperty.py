import struct


class hkxMaterialProperty(object):
    key: int
    value: int

    def __init__(self, infile):
        self.key = struct.unpack('>I', infile.read(4))
        self.value = struct.unpack('>I', infile.read(4))
