import struct


class hkClassEnumItem(object):
    value: int
    name: str

    def __init__(self, infile):
        self.value = struct.unpack('>i', infile.read(4))
        self.name = str(infile)  # TYPE_CSTRING
